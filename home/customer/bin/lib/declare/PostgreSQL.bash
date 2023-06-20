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

_postgresql-connect() {
    # Connect to one of our PostgreSQL databases
    # $1 = database host FQDN
    # $2 = database name
    # $3 = database user name
    # $4 = database user password
    echo "Connecting to PostgreSQL database using variables '$1', '$2', '$3', and '$4'"
    local Fqdn="$1" ; Fqdn="${!Fqdn}"
    local Name="$2" ; Name="${!Name}"
    local User="$3" ; User="${!User}"
    local Pass="$4" ; Pass="${!Pass}"
    echo "Connecting to PostgreSQL database '${Name}' as user '${User}' on host '${Fqdn}'"
    psql "port=5432 sslmode=require host=${Fqdn} dbname=${Name} user=${User} password=${Pass}" --list
    echo "psql exited with status: $?"
} && export -f _postgresql-connect

_postgresql-connect-indirect() {
    # Connect to one of our PostgreSQL databases, using variable indirection
    # $1 = desired environment (see above)
    # $2 = desired kind of user (see above)
    _postgresql-connect PostgresHostFqdn$1 PostgresName$1 PostgresUser$1$2 PostgresPass$1$2
} && export -f _postgresql-connect

postgresql-connect-dev-admin() {
    _postgresql-connect-indirect Dev Admin
} && export -f postgresql-connect-dev-admin

postgresql-connect-dev-regular() {
    _postgresql-connect-indirect Dev Regular
} && export -f postgresql-connect-dev-regular

postgresql-connect-dev-unknown() {
    _postgresql-connect-indirect Dev Unknown
} && export -f postgresql-connect-dev-unknown

postgresql-connect-qa-admin() {
    _postgresql-connect-indirect Qa Admin
} && export -f postgresql-connect-qa-admin

postgresql-connect-qa-regular() {
    _postgresql-connect-indirect Qa Regular
} && export -f postgresql-connect-qa-regular

postgresql-connect-qa-unknown() {
    _postgresql-connect-indirect Qa Unknown
} && export -f postgresql-connect-qa-unknown

postgresql-connect-stage-admin() {
    _postgresql-connect-indirect Stage Admin
} && export -f postgresql-connect-stage-admin

postgresql-connect-stage-regular() {
    _postgresql-connect-indirect Stage Regular
} && export -f postgresql-connect-stage-regular

postgresql-connect-stage-unknown() {
    _postgresql-connect-indirect Stage Unknown
} && export -f postgresql-connect-stage-unknown

###############################################################################
# REF: https://gecgithub01.walmart.com/legato-pim/legato-be/blob/main/docs/environments.md

# Kinds of users: Admin, Regular, Unknown
# Environments: Dev, Qa, Stage, PqaScus, ProdScus, ProdWus
# Variable naming convention is: Postgres<attribute><environment>[<kind>]
# Variable attributes are: HostFqdn, HostName, Name, Pass, User

# TODO: How do I tell whether a given PostgreSQL user is a Legato "admin" versus "regular" user?
# TODO: How do I tell whether a given PostgreSQL user is read-only?
# TODO: What do "SCUS" & "WUS" mean?

PostgresHostPrefix=legato-pim-postgres-
PostgresHostSuffix=.postgres.database.azure.com

# This is what is contained in the reference
# TODO: Comment-out what becomes known to be incorrect
export PostgresHostNameDev=${PostgresHostPrefix}np
export PostgresHostNamePqaScus=${PostgresHostPrefix}pqa-scus
export PostgresHostNameProdScus=${PostgresHostPrefix}prod-scus
export PostgresHostNameProdWus=${PostgresHostPrefix}prod-wus
export PostgresHostNameQa=${PostgresHostPrefix}np
export PostgresHostNameStage=${PostgresHostPrefix}stage

export PostgresHostFqdnDev=${PostgresHostNameDev}${PostgresHostSuffix}
export PostgresHostFqdnPqaScus=${PostgresHostNamePqaScus}${PostgresHostSuffix}
export PostgresHostFqdnProdScus=${PostgresHostNameProdScus}${PostgresHostSuffix}
export PostgresHostFqdnProdWus=${PostgresHostNameProdWus}${PostgresHostSuffix}
export PostgresHostFqdnQa=${PostgresHostNameQa}${PostgresHostSuffix}
export PostgresHostFqdnStage=${PostgresHostNameStage}${PostgresHostSuffix}

export PostgresNameDev=pim
export PostgresNamePqaScus=pim_pqa
export PostgresNameProdScus=postgres
export PostgresNameProdWus=postgres
# NO: export PostgresNameQa=pim_qa
export PostgresNameStage=postgres

export PostgresUserDevAdmin=UNKNOWN@${PostgresHostNameDev}
export PostgresUserDevRegular=UNKNOWN@${PostgresHostNameDev}
export PostgresUserDevUnknown=legato_dev@${PostgresHostNameDev}
export PostgresUserPqaScusAdmin=UNKNOWN@${PostgresHostNamePqaScus}
export PostgresUserPqaScusRegular=UNKNOWN@${PostgresHostNamePqaScus}
export PostgresUserPqaScusUnknown=legato_dev@${PostgresHostNamePqaScus}
export PostgresUserProdScusAdmin=UNKNOWN@${PostgresHostNameProdScus}
export PostgresUserProdScusRegular=UNKNOWN@${PostgresHostNameProdScus}
export PostgresUserProdScusUnknown=legato_dev@${PostgresHostNameProdScus}
export PostgresUserProdWusAdmin=UNKNOWN@${PostgresHostNameWus}
export PostgresUserProdWusRegular=UNKNOWN@${PostgresHostNameWus}
export PostgresUserProdWusUnknown=legato_reader@${PostgresHostNameWus}
export PostgresUserQaAdmin=UNKNOWN@${PostgresHostNameQa}
export PostgresUserQaRegular=UNKNOWN@${PostgresHostNameQa}
export PostgresUserQaUnknown=legato_dev@${PostgresHostNameQa}
export PostgresUserStageAdmin=UNKNOWN@${PostgresHostNameStage}
export PostgresUserStageRegular=UNKNOWN@${PostgresHostNameStage}
export PostgresUserStageUnknown=legato_dev@${PostgresHostNameStage}

###############################################################################
# NOTE: This is in `legato-be` repository at `pim/env/*.py`
# TODO: Fill in from Django environment files

###############################################################################
# NOTE: This is what I was told by Arti (different from reference)
export PostgresHostNameDev=devsamsitm
export PostgresHostNameQa=${PostgresHostPrefix}np

export PostgresHostFqdnDev=${PostgresHostNameDev}${PostgresHostSuffix}
export PostgresHostFqdnQa=${PostgresHostNameQa}${PostgresHostSuffix}

export PostgresNameQa=postgres

export PostgresUserDevAdmin=samsitem@${PostgresHostNameDev}
export PostgresUserDevRegular=legato_dev@${PostgresHostPrefix}np
export PostgresUserQaAdmin=samsitem@devsamsitm
export PostgresUserQaRegular=legato_dev@${PostgresHostPrefix}np

###############################################################################
# NOTE: This is what I was told by Bhavana (different from reference)
export PostgresUserStageUnknown=legato_dev@samspimstage

###############################################################################
# NOTE: This is what actually works, so far (different from reference)
export PostgresHostNameDev=devsamsitm
export PostgresHostNameQa=${PostgresHostPrefix}np

export PostgresHostFqdnDev=${PostgresHostNameDev}${PostgresHostSuffix}
export PostgresHostFqdnQa=${PostgresHostNameQa}${PostgresHostSuffix}

export PostgresNameQa=postgres

export PostgresUserDevAdmin=samsitem@${PostgresHostNameDev}
export PostgresUserQaRegular=legato_dev@${PostgresHostPrefix}np
export PostgresUserStageUnknown=legato_dev@samspimstage

: << 'DisabledContent'
###############################################################################
# This is what was given to me
export PostgresHostDev=devsamsitm.postgres.database.azure.com
export PostgresHostQa=legato-pim-postgres-np.postgres.database.azure.com
export PostgresNameDev=pim
export PostgresNameQa=postgres
export PostgresUserDevAdmin=samsitem@devsamsitm
export PostgresUserDevRegular=legato_dev@legato-pim-postgres-np
export PostgresUserQaAdmin=samsitem@devsamsitm
export PostgresUserQaRegular=legato_dev@legato-pim-postgres-np

###############################################################################
# This is what I am trying

export PostgresUserDevAdmin=UNKNOWN@${PostgresHostNameDev}
export PostgresUserDevRegular=UNKNOWN@${PostgresHostNameDev}
export PostgresUserDevUnknown=legato_dev@${PostgresHostNameDev}
export PostgresUserQaAdmin=UNKNOWN@${PostgresHostNameQa}
export PostgresUserQaRegular=UNKNOWN@${PostgresHostNameQa}
export PostgresUserQaUnknown=legato_dev@${PostgresHostNameQa}
DisabledContent

