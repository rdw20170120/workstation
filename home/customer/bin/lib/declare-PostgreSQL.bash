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

export DB_HostDev=devsamsitm.postgres.database.azure.com
export DB_HostQa=legato-pim-postgres-np.postgres.database.azure.com
export DB_NameDev=pim
export DB_NameQa=postgres
export DB_UserDevAdmin=samsitem@devsamsitm
export DB_UserDevRegular=legato_dev@legato-pim-postgres-np
export DB_UserQaAdmin=samsitem@devsamsitm
export DB_UserQaRegular=legato_dev@legato-pim-postgres-np

_db_connect() {
    # Connect to one of our PostgreSQL databases
    # $1 = database host
    # $2 = database name
    # $3 = database user name
    # $4 = database user password
    echo "Connecting to PostgreSQL database '$2' as user '$3' on host '$1'"
    psql "port=5432 sslmode=require host=$1 dbname=$2 user=$3 password=$4" --list
} && export -f _db_connect

db-connect-dev-admin() {
    _db_connect ${DB_HostDev} ${DB_NameDev} ${DB_UserDevAdmin} ${DB_PassDevAdmin}
} && export -f db-connect-dev-admin

db-connect-dev-regular() {
    _db_connect ${DB_HostDev} ${DB_NameDev} ${DB_UserDevRegular} ${DB_PassDevRegular}
} && export -f db-connect-dev-regular

db-connect-qa-admin() {
    _db_connect ${DB_HostQa} ${DB_NameQa} ${DB_UserQaAdmin} ${DB_PassQaAdmin}
} && export -f db-connect-qa-admin

db-connect-qa-regular() {
    _db_connect ${DB_HostQa} ${DB_NameQa} ${DB_UserQaRegular} ${DB_PassQaRegular}
} && export -f db-connect-qa-regular

: << 'DisabledContent'
DisabledContent

