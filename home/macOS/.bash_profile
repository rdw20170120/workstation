#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a Bash shell.

umask u=rwx,g=,o=

[[ -r ~/.bashrc ]] && source ~/.bashrc

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/x299424/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/x299424/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/Users/x299424/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/Users/x299424/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/Users/x299424/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/Users/x299424/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<

