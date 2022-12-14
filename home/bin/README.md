# `bin`
This is the `bin` directory for the user home directory on the workstation.
This directory should be included on the shell's PATH in the login scripts.
This directory tends to contain mostly Bash scripts, though I am leaning more
towards using Python for simple scripts.
These scripts are designed to be invoked directly by the user in the shell.
Therefore, these scripts should have proper shebangs and proper file
permissions to make them executable as intended in the user's shell.
This directory should have a [`lib` subdirectory][bin/lib] subdirectory for holding supporting scripts
that are used by these scripts.

[bin/lib]: ./bin/lib/README.md "`bin/lib` directory"

