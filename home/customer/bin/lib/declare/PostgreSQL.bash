#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source`.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ "${BO_Trace:-UNDEFINED}" != UNDEFINED ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace:-UNDEFINED}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
###############################################################################
# Declare Bash functions for accessing PostgreSQL databases at Sam's Club

# NOTE: Passwords MUST ABSOLUTELY NOT be stored in this file,
# or committed to source control,
# EVER!!!

postgresql-connect() {
    # Connect to one of our PostgreSQL databases
    # $1 = database host FQDN
    # $2 = database name
    # $3 = database user name
    # $4 = name of variable containing database user password
    local Pass="$4" ; Pass="${!Pass}"
    local _Status

    echo "Connecting to PostgreSQL database '$2' on host '$1' as user '$3' with '$4'"
    psql "port=5432 sslmode=require host=$1 dbname=$2 user=$3 password=${Pass}" --list
    _Status=$?
    echo "psql exited with status: ${_Status}"
    return ${_Status}
} && export -f postgresql-connect

postgresql-connect-indirect() {
    # Connect to one of our PostgreSQL databases
    # indirectly through environment variables
    # $1 = name of variable containing database host FQDN
    # $2 = name of variable containing database name
    # $3 = name of variable containing database user name
    # $4 = name of variable containing database user password
    local Fqdn="$1" ; Fqdn="${!Fqdn}"
    local Name="$2" ; Name="${!Name}"
    local User="$3" ; User="${!User}"
    local Pass="$4"
    local _Status

    echo "Connecting to PostgreSQL database '$2' on host '$1' as user '$3' with '$4'"
    postgresql-connect ${Fqdn} ${Name} ${User} ${Pass}
    _Status=$?
    return ${_Status}
} && export -f postgresql-connect-indirect

# Kinds of users: Owner (owner) and Readonly
# Environments: Dev, Qa, Stage, PqaScus, ProdScus, ProdWus
# Variable attributes are: HostFqdn, HostName, Name, Pass, User
# Variable naming convention is: Postgres<attribute>

# TODO: What do "SCUS" & "WUS" mean?

PostgresHostSuffix=.postgres.database.azure.com

PostgresUserLocal=pimuser
PostgresUserOwner=samsitem
PostgresUserReadonly=legato_dev

: << 'DisabledContent'
DisabledContent

