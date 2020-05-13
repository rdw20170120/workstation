TODO items for this project
===========================
These are outstanding items to do for this project.  Prioritizing can be
accomplished by physically reordering the items in the list.  Each item should
be annotated to facilitate prioritization.  Annotations should be specified as
low (L), medium (M), or high (H) for the importance (I) and the urgency (U) of
each item.  Obviously (I hope), items with higher importance and/or higher
urgency should be prioritized for earlier implementation.  Of course, ordering
should also respect dependencies between items.

Items should be struck-out and moved to the bottom when completed.

I|U|Item
-|-|---------------------------------------------------------------------------
H|H|
H|H|Format encounter id in stg6 file names with three digits & leading zeros
H|H|Resolve how to avoid creating stg6 files until stg5 is complete
H|H|Output some Accuryn fields at 1 Hz
H|H|Output some Accuryn fields initially at 1 Hz, sparsely later
L|L|Output some Accuryn fields sparsely
H|H|Output final files with monitor serial number in file name
H|H|Output final files in Avro format
H|H|Load data into Amazon Redshift
M|M|Deploy data pipeline server
M|M|Implement pipeline starting from local inbox only
M|M|Convert Kelly's code to use generators
M|M|Divide data into smaller files (1 hour per file?)
L|L|Test data processing steps
L|L|Accumulate data files per monitor
L|L|Output original noncorrupt records from extraction
L|L|Include loop sequence numbers during extraction
L|L|Name each file to mark that it has no PHI present
L|L|Check record CRC code
L|L|Recreate output files older than input files
L|L|Log task metrics for history
L|L|Estimate task durations from historical logs
L|L|Consider converting Kelly's code to use `struct` module
L|L|Enhance tooling to clean project files
L|L|Output final files in Parquet format
L|L|Move `logzero` configuration to external file
L|L|Add tooling for project filesystem ownership and permissions
L|L|Add tooling for Python style and quality
L|L|Add tooling for Python testing coverage
L|L|Enhance with multithreading
L|L|Tune application for RAM performance
L|L|Tune application for CPU performance
L|L|Tune application for network performance
L|L|Tune application for I/O performance
H|H|~~Drop duplicated records during extraction due to device logging bug~~
H|H|~~Download inbox objects~~
H|H|~~Decompress monitor archive files~~
H|H|~~Configure application with a fake-it mode~~
H|H|~~Fake data processing by `touch`ing output files~~
H|H|~~Configure application with a dry-run mode~~
M|H|~~Use runtime exceptions to simplify task logic~~
H|H|~~Extract a Accuryn raw data file to a single Avro file~~
H|H|~~Skip a task when filesystem lacks sufficient "buffer"~~
H|H|~~Calculate filesystem "buffer" specific to task type~~
H|H|~~Delete partial output files from aborted tasks~~
H|H|~~Switch to rolling log file~~
H|H|~~Enforce singleton execution~~
M|H|~~Remove hifi and lofi Avro schemas and related code~~
M|H|~~Remove dead code inherited from prior projects~~
M|H|~~Leverage `pathlib` throughout~~
M|H|~~Represent S3 keys using PurePosixPath~~
M|H|~~Add BASH script to invoke Python Tab Nanny~~
L|L|~~Enhance activate.src script to source BASH alias definitions~~
H|H|~~Productionize Kelly's code~~
M|H|~~Implement configuration setting to force overwriting output files~~
M|H|~~Implement configuration setting to limit input file size for a quick run~~
H|H|~~Output patient monitoring encounters during transform~~
M|M|~~Perform graceful interruption for shutdown~~
H|H|~~Resolve handling of observation jitter~~
H|H|~~Adjust file references in data to be relative to monitor directory~~
H|H|~~Combine encounters from separate files~~
H|H|~~Save anonymization mappings~~
H|H|~~Add monitor serial number to encounters~~
H|H|~~Use encounters to process extracted data~~
H|H|~~Output some Accuryn fields at original 100 Hz~~
H|H|~~Anonymize data files~~
H|H|~~Extract anonymized fields into secure files~~

