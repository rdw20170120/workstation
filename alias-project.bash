#!/bin/false
# NOTE: Intended to be sourced into a BASH shell

# BASH alias definitions specific to this project

alias avro-no='find $DirIntermediate -name "*.avro"  -delete'
alias fake-no='find $DirIntermediate -name "*.fake"  -delete'

alias avro-list='find $DirIntermediate -name "*.avro"  -exec ls -l "{}" \;'
alias fake-list='find $DirIntermediate -name "*.fake"  -exec ls -l "{}" \;'

alias list-sort='sort -nr --key=5'

