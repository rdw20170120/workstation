#!/usr/bin/env false
################################################################################
# Activate Homebrew

export BO_PathHomebrewBefore=${PATH}

if >/dev/null which brew ; then
    eval "$(${HOMEBREW_PREFIX}/bin/brew shellenv)"
else
    echo "DEBUG: Missing 'brew', skipping activation of Homebrew"
fi

export BO_PathHomebrewAfter=${PATH}

: << 'DisabledContent'
DisabledContent

