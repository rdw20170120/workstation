#!/bin/bash
set -ex

# Clean project directory
# TODO: Enhance to handle directories

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

if [[ -z "$PVE" ]] ; then
    echo "FATAL: Environment variable 'PVE' is undefined, aborting"
    exit 1
fi

findAnd () {
    # Find and perform action $1 on files within project directory matching pattern $2
    # $1 = action to perform, typically either 'delete' or 'print'
    # $2 = file name pattern to match
    find $DirProject -not -path "$DirProject/.git/*" -and -not -path "$PVE/*" -and -name "$2" -$1 -and -type f
}

echo "INFO: Found these files..."
findAnd print '__pycache'
findAnd print '*.log'
findAnd print '*.pyc'

echo "INFO: Deleting files..."
findAnd delete '__pycache'
findAnd delete '*.log'
findAnd delete '*.pyc'

dir=$DirProject/src/.pytest_cache
echo "INFO: Deleting special directory '$dir' directly..."
rm -fr "$dir"

echo "WARN: Found these files REMAINING..."
findAnd print '__pycache'
findAnd print '*.log'
findAnd print '*.pyc'

