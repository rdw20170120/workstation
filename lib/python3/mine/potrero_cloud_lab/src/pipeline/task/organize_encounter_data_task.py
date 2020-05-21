#!/bin/false

from avro.datafile import DataFileReader
from avro.datafile import DataFileWriter
from avro.io       import DatumReader
from avro.io       import DatumWriter
from avro.schema   import Parse
from logzero       import logger as log

from ..config             import Config
from ..utility.filesystem import touch
from ..utility.math       import Percentage
from ..utility.time       import is_naive
from .mapping             import Mapping
from .task                import Task

c, m = Config(), Mapping()


class OrganizeEncounterDataTask(Task):
    """Organize data for encounter."""
    def __init__(self, encounter):
        assert isinstance(encounter, dict)
        super().__init__()
        self._encounter = encounter

        self._count_records_1_Hz = 0
        self._count_records_100_Hz = 0
        self._count_records_incoming = 0
        self._count_records_sparse = 0

    def __str__(self):
        m = "OrganizeEncounterDataTask for encounter '{}'"
        return m.format(self._encounter)

    def _distribute(self, record):
        self._count_records_incoming += 1
        timestamp = record['timestamp_second']
        assert is_naive(timestamp)
        if timestamp >= self._began:
            if timestamp <= self._ended:
                elapsed = timestamp - self._began
                assert is_naive(elapsed)
                assert is_naive(record['loop_time'])
                assert is_naive(record['milliseconds'])
                
                self._write_100_Hz(record, elapsed)
                if self._previous_elapsed is None:
                    self._previous_elapsed = elapsed
                    self._previous_record = record
                elif elapsed > self._previous_elapsed:
                    self._write_1_Hz(
                        self._previous_record, self._previous_elapsed
                        )
                    self._write_sparse(
                        self._previous_record, self._previous_elapsed
                        )
                    self._previous_elapsed = elapsed
                    self._previous_record = record
                else:
                    assert elapsed == self._previous_elapsed
                    # NOTE: 'loop_time' is not monotonically increasing!
                    assert (
                        record['milliseconds'] >=
                        self._previous_record['milliseconds']
                        )
                    self._update(self._previous_record, record)

    def _fake_execute(self):
        log.warn("Executing task with FAKE data processing")
        touch(self._target_1_Hz_file)
        touch(self._target_100_Hz_file)
        touch(self._target_sparse_file)

    def _organize_encounter_data(self):
        self._began = self._encounter['timestamp_began']
        self._ended = self._encounter['timestamp_ended']
        self._id = self._encounter['encounter_id']
        self._previous_elapsed = None
        self._previous_record = None
        assert is_naive(self._began)
        assert is_naive(self._ended)

        schema_1_Hz = Parse(c.avro_1_Hz_schema_file.read_text(
            encoding='utf_8'
            ))
        schema_100_Hz = Parse(c.avro_100_Hz_schema_file.read_text(
            encoding='utf_8'
            ))
        schema_sparse = Parse(c.avro_sparse_schema_file.read_text(
            encoding='utf_8'
            ))

        with DataFileWriter(
            self._target_1_Hz_file.open('wb'),
            DatumWriter(),
            schema_1_Hz
            ) as self._writer_1_Hz:
            with DataFileWriter(
                self._target_100_Hz_file.open('wb'),
                DatumWriter(),
                schema_100_Hz
                ) as self._writer_100_Hz:
                with DataFileWriter(
                    self._target_sparse_file.open('wb'),
                    DatumWriter(),
                    schema_sparse
                    ) as self._writer_sparse:
                    for f in self._encounter['extracted_files']:
                        source_file = self._monitor_directory / f
                        log.debug("Reading data from file '%s'", source_file)
                        with DataFileReader(
                            source_file.open('rb'), DatumReader()
                            ) as self._reader:
                            for r in self._reader:
                                self._distribute(r)
        self._report()

    def _real_execute(self):
        self._skip_for_dry_run()

        must_process_data = False
        if not self._target_1_Hz_file.exists(): must_process_data = True
        if not self._target_100_Hz_file.exists(): must_process_data = True
        if not self._target_sparse_file.exists(): must_process_data = True

        try:
            if must_process_data: self._organize_encounter_data()
        except BaseException:
            self._delete_output_file_upon_exception(self._target_1_Hz_file)
            self._delete_output_file_upon_exception(self._target_100_Hz_file)
            self._delete_output_file_upon_exception(self._target_sparse_file)
            raise

    def _report(self):
        p = Percentage(
            self._count_records_1_Hz, self._count_records_incoming
            )
        log.info("Wrote %d %s records of %d incoming records = %.2f%%",
            p.numerator, '1 Hz', p.denominator, p.percentage
            )
        p = Percentage(
            self._count_records_100_Hz, self._count_records_incoming
            )
        log.info("Wrote %d %s records of %d incoming records = %.2f%%",
            p.numerator, '100 Hz', p.denominator, p.percentage
            )
        p = Percentage(
            self._count_records_sparse, self._count_records_incoming,
            )
        log.info("Wrote %d %s records of %d incoming records = %.2f%%",
            p.numerator, 'sparse', p.denominator, p.percentage
            )

    def _update(self, previous_record, next_record):
        self._update_if_greater(previous_record, next_record,
            'battery_life')
        self._update_if_greater(previous_record, next_record,
            'battery_voltage')
        self._update_if_greater(previous_record, next_record,
            'bladder_pressure_filtered')
        self._update_if_greater(previous_record, next_record,
            'bladder_temperature')
        self._update_if_greater(previous_record, next_record,
            'chamber_pressure_filtered')
        self._update_if_greater(previous_record, next_record,
            'pressure_volume_filtered')
        self._update_if_greater(previous_record, next_record,
            'pressure_volume_raw')
        self._update_if_greater(previous_record, next_record,
            'respiration_pressure')
        self._update_if_greater(previous_record, next_record,
            'respiration_rate')
        self._update_if_greater(previous_record, next_record,
            'tilt_forward')
        self._update_if_greater(previous_record, next_record,
            'tilt_side')
        self._update_if_greater(previous_record, next_record,
            'ultrasonic_signal')
        self._update_if_greater(previous_record, next_record,
            'ultrasonic_volume')
        self._update_if_greater(previous_record, next_record,
            'urine_pressure')
        self._update_if_greater(previous_record, next_record,
            'urine_rate')
        self._update_if_greater(previous_record, next_record,
            'urine_volume')

        self._update_if_nondefault(previous_record, next_record,
            'error_code')
        self._update_if_nondefault(previous_record, next_record,
            'power_status')
        self._update_if_nondefault(previous_record, next_record,
            'prime_status')
        self._update_if_nondefault(previous_record, next_record,
            'urine_state')

    def _update_if_greater(self, previous_record, next_record, key):
        p, n = previous_record[key], next_record[key]
        if n is not None:
            if p is None: previous_record[key] = n
            elif n > p: previous_record[key] = n

    def _update_if_nondefault(self, previous_record, next_record, key, default=0):
        p, n = previous_record[key], next_record[key]
        if n is not None:
            if n != default:
                if p is None: previous_record[key] = n
                elif p == default: previous_record[key] = n
                elif n == p: pass
                else:
                    s = """Found nondefault value '%d' for key '%s' in record:
                    %s
                    while updating previous record:
                    %s
                    """
                    log.debug(s, n, key, next_record, previous_record)
                    previous_record[key] = n

    def _write(self, writer, record):
        writer.append(record)

    def _write_1_Hz(self, record, elapsed):
        self._write(self._writer_1_Hz,
            {
            'encounter_id': self._id,
            'elapsed_seconds': elapsed,
            'battery_life': record['battery_life'],
            'battery_voltage': record['battery_voltage'],
            'bladder_pressure_filtered': record['bladder_pressure_filtered'],
            'bladder_temperature': record['bladder_temperature'],
            'chamber_pressure_filtered': record['chamber_pressure_filtered'],
            'pressure_volume_filtered': record['pressure_volume_filtered'],
            'pressure_volume_raw': record['pressure_volume_raw'],
            'respiration_pressure': record['respiration_pressure'],
            'respiration_rate': record['respiration_rate'],
            'tilt_forward': record['tilt_forward'],
            'tilt_side': record['tilt_side'],
            'ultrasonic_signal': record['ultrasonic_signal'],
            'ultrasonic_volume': record['ultrasonic_volume'],
            'urine_pressure': record['urine_pressure'],
            'urine_rate': record['urine_rate'],
            'urine_volume': record['urine_volume'],
            })
        self._count_records_1_Hz += 1

    def _write_100_Hz(self, record, elapsed):
        self._write(self._writer_100_Hz,
            {
            'encounter_id': self._id,
            'elapsed_seconds': elapsed,
            'loop_time': record['loop_time'],
            'milliseconds': record['milliseconds'],
            'bladder_pressure_raw': record['bladder_pressure_raw'],
            'chamber_pressure_raw': record['chamber_pressure_raw'],
            })
        self._count_records_100_Hz += 1

    def _write_sparse(self, record, elapsed):
        must_write = False
        if record['error_code'] != 0: must_write = True
        if record['power_status'] != 0: must_write = True
        if record['prime_status'] != 0: must_write = True
        if record['urine_state'] != 6: must_write = True
        if must_write:
            self._write(self._writer_sparse,
                {
                'encounter_id': self._id,
                'elapsed_seconds': elapsed,
                'error_code': record['error_code'],
                'power_status': record['power_status'],
                'prime_status': record['prime_status'],
                'urine_state': record['urine_state'],
                })
            self._count_records_sparse += 1

    def execute(self):
        super().execute()
        self._id = self._encounter['encounter_id']
        monitor = self._encounter['monitor']
        self._monitor_directory = m.map_monitor_to_monitor_directory(monitor)
        self._target_1_Hz_file = m.encounter_1_Hz_file(monitor, self._id)
        self._target_100_Hz_file = m.encounter_100_Hz_file(monitor, self._id)
        self._target_sparse_file = m.encounter_sparse_file(monitor, self._id)

        if c.should_fake_it: self._fake_execute()
        else:                self._real_execute()

