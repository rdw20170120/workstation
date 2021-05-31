#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a Bash shell.

umask u=rwx,g=,o=

# Added by Nix installer
if [ -e ~/.nix-profile/etc/profile.d/nix.sh ]; then
    source ~/.nix-profile/etc/profile.d/nix.sh
fi

# Disable use of Nix channels,
# in favor of release pinning
# when ready.
# export NIX_PATH=

[[ -r ~/.bashrc ]] && source ~/.bashrc

