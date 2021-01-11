# `lib`
This is the `bin/lib` directory for the user home directory on the workstation.
This directory should NEVER be included on the shell's PATH.
This directory contains supporting scripts for those scripts in the parent
`bin` directory.
These scripts are NOT designed to stand alone, or to be invoked directly by the
user.
These scripts should ONLY be `source`d (Bash scripts) or `import`ed (Python
scripts) by other scripts that use them.

