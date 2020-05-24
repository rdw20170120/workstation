#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a BASH shell.

export TERM=vt102
export COLORTERM=truecolor

[[ -z "$BO_PathOriginal" ]] && export BO_PathOriginal=$PATH
export BO_PathHomebrew=/usr/local/bin
export BO_PathSystem=/usr/bin:/bin:/usr/sbin
export BO_PathUser=$BO_PathHomebrew:~/bin
export PATH=$BO_PathSystem:$BO_PathUser

# Secure login scripts
chmod u=rw,g=,o= ~/.bash_profile ~/.bashrc ~/*.bash

# Secure personal script directory
dir=~/bin
if [[ -d "$dir" ]] ; then
  chmod u=rwx,g=,o= $dir
  chmod u=rwx,g=,o= $dir/*
fi

# Secure SSH directory
if [[ -d ~/.ssh ]] ; then
  chmod u=rwx,g=,o= ~/.ssh
  chmod u=rw,g=,o=  ~/.ssh/*
fi

# Define BASH aliases
[[ -r alias.bash ]] && source alias.bash

