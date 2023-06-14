#!/usr/bin/env false
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################

alias legato-be_activate='source ~/bin/lib/activate_legato-be.bash'
alias legato-rule_engine_activate='source ~/bin/lib/activate_legato-rule-engine.bash'
alias legato-ui_activate='source ~/bin/lib/activate_legato-ui.bash'

alias jump_legato-be='cd ~/repo/SamsClub/wip/legato-be'
alias jump_legato-rule-engine='cd ~/repo/SamsClub/wip/legato-rule-engine'
alias jump_legato-ui='cd ~/repo/SamsClub/wip/legato-ui'

: << 'DisabledContent'
# Manually installed NodeJS via `nvm` installed via Homebrew
# TODO: Integrate this somehow into automated scripts
nvm install 14
nvm install 16
DisabledContent

