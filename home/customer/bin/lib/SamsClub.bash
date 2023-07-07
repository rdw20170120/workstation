#!/usr/bin/env false
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# For job j0062

alias legato-be_activate='source ~/bin/lib/activate_legato-be.bash'
alias legato-client_activate='source ~/bin/lib/activate_legato-client.bash'
alias legato-rule-engine_activate='source ~/bin/lib/activate_legato-rule-engine.bash'
alias legato-server_activate='source ~/bin/lib/activate_legato-server.bash'
alias legato-ui_activate='source ~/bin/lib/activate_legato-ui.bash'

alias jump_j0062='cd ~/repo/GitHub/wip/j0062'
alias jump_legato-be='cd ~/repo/SamsClub/wip/legato-be'
alias jump_legato-client='cd ~/repo/SamsClub/wip/legato-client'
alias jump_legato-rule-engine='cd ~/repo/SamsClub/wip/legato-rule-engine'
alias jump_legato-server='cd ~/repo/SamsClub/wip/legato-server'
alias jump_legato-ui='cd ~/repo/SamsClub/wip/legato-ui'

: << 'DisabledContent'
# Manually installed NodeJS via `nvm` installed via Homebrew
# TODO: Integrate this somehow into automated scripts
nvm install 12
nvm install 14
nvm install 16
DisabledContent

