#!/bin/bash
# Report tool dependencies

Rule=##########

check() {
    echo $Rule
    echo $1
    $1
}

checkExecutable() {
    check "type $1"
    check "which $1"
}

checkVariable() {
    echo $Rule
    echo "$1=$2"
}

# operating system
check 'uname --all'
checkExecutable uname
checkVariable PATH "$PATH"

# BASH
check 'bash --version'
checkExecutable bash

# Python shared
check 'python --version'
checkExecutable python
checkVariable PYTHONPATH "$PYTHONPATH"

# Python 2
check 'pip --version'
checkExecutable pip
check 'python2 --version' 2>&1
checkExecutable python2
echo $Rule
python2 -c 'import platform; print(platform.python_version())'
echo $Rule
python2 -c 'import os; print(os.sys.path)'

# Python 3
check 'pip3 --version'
checkExecutable pip3
check 'python3 --version'
checkExecutable python3
echo $Rule
python3 -c 'import platform; print(platform.python_version())'
echo $Rule
python3 -c 'import os; print(os.sys.path)'

# Git
check 'git --version'
checkExecutable git

# Python testing
check 'py.test --version' 2>&1
checkExecutable py.test

