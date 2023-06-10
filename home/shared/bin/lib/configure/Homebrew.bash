#!/usr/bin/env false
################################################################################
# Configure Homebrew

case "${BO_ARCH}" in
    arm64) 
        # NOTE: On Apple macOS running on Apple Silicon
        export HOMEBREW_PREFIX=/opt/homebrew
        ;;
    *)
        echo "WARN: HOMEBREW_PREFIX is UNKNOWN for architecture '${BO_ARCH}'"
        export HOMEBREW_PREFIX=UNKNOWN
        ;;
esac
# NOTE: On Apple macOS running on Intel CPU
# export HOMEBREW_PREFIX=/usr/local
export BO_PathHomebrew=${HOMEBREW_PREFIX}/bin:${HOMEBREW_PREFIX}/sbin

: << 'DisabledContent'
DisabledContent

