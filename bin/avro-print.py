#!/usr/bin/env python3

from argparse import ArgumentParser
from argparse import FileType
from sys      import stdout

from avro.datafile import DataFileReader
from avro.io       import DatumReader

def main():
    parser = ArgumentParser(
        description='Print a file stored in Apache Avro format.'
        )
    parser.add_argument('infile', type=FileType('rb'))
    parser.add_argument('outfile',
            nargs='?', type=FileType('wt'), default=stdout)
    args = parser.parse_args()

    with args.outfile as writer:
        with DataFileReader(args.infile, DatumReader()) as reader:
            for r in reader:
                writer.write(str(r) + '\n')

if __name__ == "__main__":
    main()

