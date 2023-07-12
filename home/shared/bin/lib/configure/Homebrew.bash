#!/usr/bin/env false
################################################################################
# Configure Homebrew

case "${BO_ARCH}" in
    arm64) 
        # NOTE: On Apple macOS running on Apple Silicon
        export HOMEBREW_PREFIX=/opt/homebrew
        ;;
    x86_64)
        # NOTE: On Apple macOS running on Intel CPU
        export HOMEBREW_PREFIX=/usr/local
        ;;
    *)
        echo "WARN: HOMEBREW_PREFIX is UNKNOWN for architecture '${BO_ARCH}'"
        export HOMEBREW_PREFIX=${HOME}/HomeBrew
        ;;
esac

export BO_PathHomebrew=${HOMEBREW_PREFIX}/bin:${HOMEBREW_PREFIX}/sbin

: << 'DisabledContent'
DisabledContent

