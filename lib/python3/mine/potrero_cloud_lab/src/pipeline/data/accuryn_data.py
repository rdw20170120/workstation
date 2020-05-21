'''
Created on Mar 1, 2019

@author: kstanton
'''
from datetime import datetime as dt 
from re       import search as re_search

from logzero import logger as log
from numpy   import arange as np_arange 
from numpy   import argwhere as np_argwhere 
from numpy   import concatenate as np_concatenate 
from numpy   import delete as np_delete 
from numpy   import dtype as np_dtype 
from numpy   import floor as np_floor 
from numpy   import frombuffer as np_frombuffer 
from numpy   import full as np_full
from numpy   import insert as np_insert 
from numpy   import int as np_int 
from numpy   import squeeze as np_squeeze 
from numpy   import sum as np_sum 
from numpy   import vectorize as np_vectorize 
from pandas  import concat as pd_concat 
from pandas  import timedelta_range as pd_timedelta_range 
from pandas  import to_datetime as pd_to_datetime 
from pandas  import DataFrame as pd_DataFrame 
from pandas  import Series as pd_Series 
from pandas  import Timedelta as pd_Timedelta 
from pandas  import Timestamp as pd_Timestamp 

from ..utility.filesystem import file_size
from ..utility.math       import Percentage
from ..utility.math       import Rate
from ..utility.time       import now_utc

"""Potrero binary data format matches the structure of the following Numpy
structured array.  Reference structured arrays at:
https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.scalars.html
Data structure defined in potrero-controller Data.h
"""
accuryn_record = np_dtype([
    # record head
    ('start_code', 'B'),
    # Real-Time Clock (RTC)
    ('second', 'B'),
    ('minute', 'B'),
    ('hour', 'B'),
    ('day', 'B'),
    ('month', 'B'),
    ('year', 'B'),
    # patient Electronic Medical Record (EMR)
    ('patient_partial_id', '10S'), # TODO: patient partial id?
    ('patient_dry_weight', 'H'), # patient dry weight (kg)
    ('urine_rate', 'h'), # UO Rate (mL/hr)
    ('urine_volume', 'i'), # Total Volume (mL)
    ('bladder_pressure_filtered', 'h'), # IAP (mmHg*100)
    ('bladder_temperature', 'h'), # Temp (Celcius * 10)
    ('battery_life', 'H'), # Battery Life (%)
    ('power_status', 'H'), # (0=on, 1=off)
    ('error_code', 'h'), # TODO: ??? 
    ('dummy1', 'h'), # Dummy Int
    # engineering data
    ('bladder_pressure_raw', 'h'), # Raw Pressure Signal (mmHg*100)
    ('prime_status', 'h'), # Prime Status
    ('respiration_pressure', 'h'), # Filtered Pressure Signal
    ('loop_time', 'h'), # Loop Time (uS)
    ('respiration_rate', 'h'), # Calculated respiratory rate
    ('battery_voltage', 'H'), # Battery Voltage (uV)
    ('urine_state', 'h'), # UO State
    ('urine_pressure', 'h'), # UO Pressure
    ('pressure_volume_raw', 'h'),
    ('pressure_volume_filtered', 'h'),
    ('chamber_pressure_raw', 'h'),
    ('chamber_pressure_filtered', 'h'),
    ('ultrasonic_signal', 'h'),
    ('ultrasonic_volume', 'h'),
    ('tilt_side', 'h'), # degrees*10
    ('tilt_forward', 'h'), # degrees*10
    # record tail
    ('crc', 'h'), # Dummy Int
    ('end_code', 'B') # Dummy Int
    ])

# function to convert hex coded decimal values to decimal
def parseHexCodedDecimal(x):
    """Convert a number from hex-coded bytes? to decimal.
    
    TODO: What exactly comes in and goes out?
    TODO: Write unit tests
    """
    return int(hex(x)[2:])

# TODO: Put this into a function somewhere, rather than in module initialization
parseHexCodedDecimal = np_vectorize(parseHexCodedDecimal, otypes=[np_int])

# TODO: Put this into a function somewhere, rather than in module initialization
# TODO: What does this do exactly?!?!
NANVALUE = -30000
# insert a nan record
nan_rec = np_full(shape=72, fill_value=NANVALUE, dtype='B')
nan_rec[[0, -1]] = 126
nan_rec[1:4] = 0
nan_rec[[4, 5]] = 1
nan_rec[6] = 0
for ii, code in enumerate('NAN RECORD'.encode('ascii')):
    nan_rec[7 + ii] = code


class AccurynData:
    def __init__(self, source_file):
        self._source_file = source_file

    def __iter__(self):
        return AccurynDataIter(self)


class AccurynDataIter:
    """Iterate through raw Accuryn data file, fixing corruption issues."""
    def __init__(self, parent):
        self._parent = parent
        self._began = now_utc()
        self._stopped = False

        # Track file TODO: Refactor to use context manager for self._file
        self._bytes_in_file = file_size(self._parent._source_file)
        self._file = open(self._parent._source_file, 'rb')

        # Track records
        self._last_chunk_end_time = pd_to_datetime('1/1/2000')
        self._next_record_index = 0
        self._records = []
        self._records_per_buffer = 1000
        self._total_corrupt_records = 0
        self._total_records = 0

    def __next__(self):
        if self._next_record_index >= len(self._records):
            # Reload buffer when we exhaust it
            self._next_record_index = 0
            records_df = self._read_records()
            self._records = records_df.reset_index().to_dict(
                orient='records'
                )
            self._report_progress()

        # Grab next record
        result = self._records[self._next_record_index]
        self._next_record_index += 1
        self._total_records += 1

        # Tweak record
        result = {
            key: (value if value != NANVALUE else None)
            for key, value in list(result.items())
            }
        result['timestamp'] = (
            result['timestamp']
            - pd_Timestamp("1970-01-01")
            ) // pd_Timedelta('1ms')

        # Adjust handling of time
        result['milliseconds'] = result['timestamp'] % 1000
        result['timestamp_second'] = result['timestamp'] // 1000
        del result['timestamp']
        return result

    def _read_records(self):
        """Read records from file, stream them as dictionaries."""
        if self._stopped: raise StopIteration

        # read the appropriate number of bytes into a numpy array of bytes
        read_bytes_buffer = np_frombuffer(
            self._file.read(accuryn_record.itemsize * self._records_per_buffer),
            dtype='B'
            )

        # if we did not read anything then at the EoF, so stop
        if len(read_bytes_buffer) == 0:
            self._report_progress()
            log.info("Finished importing file: %s", str(self._parent._source_file))
            self._stopped = True
            raise StopIteration
        count_corrupt_records = 0
        records = None
        while True:
            # interpret the byte stream as the accuryn record
            num_records_to_read = int(
                np_floor(len(read_bytes_buffer) / accuryn_record.itemsize)
                * accuryn_record.itemsize
                )
            records = np_frombuffer(
                read_bytes_buffer[:num_records_to_read],
                dtype=accuryn_record
                )

            # check to make sure the time vars are numbers
            time_bad = [
                bool(
                    re_search(
                        '[^0-9]',
                        hex(s)[2:] + hex(m)[2:] + hex(h)[2:]
                        + hex(D)[2:] + hex(M)[2:] + hex(Y)[2:]
                        )
                    )
                or int(hex(s)[2:]) < 0
                or int(hex(s)[2:]) > 59
                or int(hex(m)[2:]) < 0
                or int(hex(m)[2:]) > 59
                or int(hex(h)[2:]) < 0
                or int(hex(h)[2:]) > 23
                or int(hex(D)[2:]) < 1
                or int(hex(D)[2:]) > 31
                or int(hex(M)[2:]) < 1
                or int(hex(M)[2:]) > 12
                or int(hex(Y)[2:]) < 0
                for s, m, h, D, M, Y in records[[
                    'second', 'minute', 'hour', 'day', 'month', 'year'
                    ]]
                ]
            bad_records =  np_squeeze(
                np_argwhere(
                    (records["start_code"] != 0x7e)
                    | (records["end_code"] != 0x7e)
                    | time_bad),
                axis=1
                )
            if len(bad_records) == 0: break
            count_corrupt_records += 1
            self._total_corrupt_records += 1

            # delete bytes corresponding to the first bad record
            delete_start = bad_records[0] * accuryn_record.itemsize
            next_stop =  np_squeeze(
                np_argwhere(read_bytes_buffer[(delete_start + 1):] == 0x7e),
                axis=1
                )
            if len(next_stop) == 0:
                next_stop = len(read_bytes_buffer[(delete_start + 1):])
            else:
                next_stop = next_stop[0]
            delete_stop = delete_start + next_stop + 1
            read_bytes_buffer = np_delete(
                read_bytes_buffer,
                np_arange(delete_start, delete_stop)
                )

            # if the partial record delete was greater than half a record
            # TODO: make this a while loop
            if delete_stop - delete_start > 72 / 2:
                read_bytes_buffer = np_insert(
                    read_bytes_buffer, delete_start, nan_rec
                    )
            if delete_stop - delete_start > 3 * 72 / 2:
                read_bytes_buffer = np_insert(
                    read_bytes_buffer, delete_start, nan_rec
                    )
            # read_bytes_buffer = np_concatenate((read_bytes_buffer, nan_rec))

            # ensure buffer is multiple of itemsize by reading additional bytes
            read_bytes_buffer = np_concatenate((
                read_bytes_buffer, 
                np_frombuffer(
                    self._file.read(
                        72 - len(read_bytes_buffer) % accuryn_record.itemsize
                    ),
                    dtype='B'
                    )
                ))

        # interpret byte stream as an Accuryn record
        num_records_to_read = int(np_floor(
            len(read_bytes_buffer) / accuryn_record.itemsize
            ) * accuryn_record.itemsize)
        records = np_frombuffer(
            read_bytes_buffer[:num_records_to_read],
            dtype=accuryn_record
            )

        # convert the numpy array to a dataframe
        df = pd_DataFrame(records)

        # change time variables to a datetime type
        # time variables
        time_vars = ['second', 'minute', 'hour', 'day', 'month', 'year']

        # parse binary coded decimal values to a date time
        df.loc[:, time_vars] = parseHexCodedDecimal(df.loc[:, time_vars])

        # FIXME: Our Y2K fix we pull century from import time because it is not
        # stored in the record.  This may cause a couple of records to have
        # incorrectly assigned century near midnight on 31-Dec-2099.
        df['year'] = df['year'] + round(dt.utcnow().year, -2)
        timestamp = pd_to_datetime(df.loc[:, time_vars])

        # drop the time vars and dummys
        df.drop(
            time_vars + ['crc', 'start_code', 'end_code', 'dummy1'],
            axis=1,
            inplace=True
            )

        # add the timestamps
        df['timestamp'] = timestamp

        # fix issue where are not strictly increasing
        # set records to nan when it goes back in time
        cm = pd_concat((
            pd_Series(self._last_chunk_end_time.replace(microsecond=0)),
            df['timestamp']
            )).cummax().iloc[1:]
        df.loc[df['timestamp'] < cm, 'timestamp'] = cm

        # if we are still on the same second as the last chunk
        if (
            self._last_chunk_end_time.replace(microsecond=0)
            ==
            df['timestamp'].min().replace(microsecond=0)
            ):
            # adjust first record leftover milliseconds from the previous chunk
            df.loc[
                df['timestamp'] == df['timestamp'].min(), 'timestamp'
                ] += pd_Timedelta(
                    microseconds=self._last_chunk_end_time.microsecond + 10000
                    )

        def add_ms (x):
            """Add milliseconds to the rest of the records."""
            ms = pd_timedelta_range(
                pd_Timedelta('00:00:00'),
                pd_Timedelta('00:00:00.01') * len(x),
                freq=pd_Timedelta('00:00:00.01'),
                closed='left'
                )
            return(x + ms)
        df.index = df['timestamp']
        df['timestamp'] = df['timestamp'].groupby('timestamp').transform(add_ms)
        df.index = df['timestamp']

        # FIXME: round to nearest 10 millisecond (not sure why this occurs)
        df.index = df.index.round(freq='10ms')
        df['timestamp'] = df.index

        # drop duplicated records
        # TODO: Let's figure out whether this is truly necessary
        if np_sum(df.index.duplicated()) > 0:
            log.debug(
                "Dropping %d records with duplicate timestamps",
                np_sum(df.index.duplicated())
                )
            df = df[~df.index.duplicated(keep='first')]

        # set the last chunk end time
        self._last_chunk_end_time = df['timestamp'].iloc[-1]

        # drop uneeded field (timestamp is already the index)
        df = df.drop('timestamp', axis=1)

        # drop nan records
        df = df.loc[df['patient_partial_id'] != b'NAN RECORD']

        # undo the rfid byte encoding
        df['patient_partial_id'] = df['patient_partial_id'].str.decode('ascii')

        # file has corrupt records, compensate with smaller buffer size
        if count_corrupt_records > 0:
            self._records_per_buffer = 1000
        else:
            self._records_per_buffer = 100000
        
        # check if we still have data after all the processing
        if len(df) == 0:
            self._report_progress()
            log.info("Finished importing file: %s", self._parent._source_file)
            self._stopped = True
            raise StopIteration
        return df

    def _report_progress(self):
        bytes_so_far = self._file.tell()
        duration = now_utc() - self._began
        p = Percentage(bytes_so_far, self._bytes_in_file)
        log.debug("Processed %d of %d bytes in file = %.2f%%",
            p.numerator, p.denominator, p.percentage
            )
        r = Rate(
            bytes_so_far, 'bytes', duration.total_seconds(), 'seconds', 'Bps'
            )
        log.info(
            "Processed %d %s so far in %s %s = %.2f %s",
            r.numerator, r.numerator_units,
            r.denominator, r.denominator_units,
            r.rate, r.rate_units
            )
        p = Percentage(self._total_corrupt_records, self._total_records)
        m = "Deleted %d corrupt records of %d total records so far = %.2f%%,"
        m += " using buffer size of %d"
        log.warn(m,
            p.numerator, p.denominator, p.percentage, self._records_per_buffer
            )

