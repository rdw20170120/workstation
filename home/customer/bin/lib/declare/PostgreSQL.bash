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
    _postgresql-connect DB_HostFqdn$1 DB_Name$1 DB_User$1$2 DB_Pass$1$2
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
# Variable naming convention is: DB_<attribute><environment>[<kind>]
# Variable attributes are: HostFqdn, HostName, Name, Pass, User

# TODO: How do I tell whether a given PostgreSQL user is a Legato "admin" versus "regular" user?
# TODO: How do I tell whether a given PostgreSQL user is read-only?
# TODO: What do "SCUS" & "WUS" mean?

DB_HostPrefix=legato-pim-postgres-
DB_HostSuffix=.postgres.database.azure.com

# This is what is contained in the reference
# TODO: Comment-out what becomes known to be incorrect
export DB_HostNameDev=${DB_HostPrefix}np
export DB_HostNamePqaScus=${DB_HostPrefix}pqa-scus
export DB_HostNameProdScus=${DB_HostPrefix}prod-scus
export DB_HostNameProdWus=${DB_HostPrefix}prod-wus
export DB_HostNameQa=${DB_HostPrefix}np
export DB_HostNameStage=${DB_HostPrefix}stage

export DB_HostFqdnDev=${DB_HostNameDev}${DB_HostSuffix}
export DB_HostFqdnPqaScus=${DB_HostNamePqaScus}${DB_HostSuffix}
export DB_HostFqdnProdScus=${DB_HostNameProdScus}${DB_HostSuffix}
export DB_HostFqdnProdWus=${DB_HostNameProdWus}${DB_HostSuffix}
export DB_HostFqdnQa=${DB_HostNameQa}${DB_HostSuffix}
export DB_HostFqdnStage=${DB_HostNameStage}${DB_HostSuffix}

export DB_NameDev=pim
export DB_NamePqaScus=pim_pqa
export DB_NameProdScus=postgres
export DB_NameProdWus=postgres
# NO: export DB_NameQa=pim_qa
export DB_NameStage=postgres

export DB_UserDevAdmin=UNKNOWN@${DB_HostNameDev}
export DB_UserDevRegular=UNKNOWN@${DB_HostNameDev}
export DB_UserDevUnknown=legato_dev@${DB_HostNameDev}
export DB_UserPqaScusAdmin=UNKNOWN@${DB_HostNamePqaScus}
export DB_UserPqaScusRegular=UNKNOWN@${DB_HostNamePqaScus}
export DB_UserPqaScusUnknown=legato_dev@${DB_HostNamePqaScus}
export DB_UserProdScusAdmin=UNKNOWN@${DB_HostNameProdScus}
export DB_UserProdScusRegular=UNKNOWN@${DB_HostNameProdScus}
export DB_UserProdScusUnknown=legato_dev@${DB_HostNameProdScus}
export DB_UserProdWusAdmin=UNKNOWN@${DB_HostNameWus}
export DB_UserProdWusRegular=UNKNOWN@${DB_HostNameWus}
export DB_UserProdWusUnknown=legato_reader@${DB_HostNameWus}
export DB_UserQaAdmin=UNKNOWN@${DB_HostNameQa}
export DB_UserQaRegular=UNKNOWN@${DB_HostNameQa}
export DB_UserQaUnknown=legato_dev@${DB_HostNameQa}
export DB_UserStageAdmin=UNKNOWN@${DB_HostNameStage}
export DB_UserStageRegular=UNKNOWN@${DB_HostNameStage}
export DB_UserStageUnknown=legato_dev@${DB_HostNameStage}

###############################################################################
# NOTE: This is in `legato-be` repository at `pim/env/*.py`
# TODO: Fill in from Django environment files

###############################################################################
# NOTE: This is what I was told by Arti (different from reference)
export DB_HostNameDev=devsamsitm
export DB_HostNameQa=${DB_HostPrefix}np

export DB_HostFqdnDev=${DB_HostNameDev}${DB_HostSuffix}
export DB_HostFqdnQa=${DB_HostNameQa}${DB_HostSuffix}

export DB_NameQa=postgres

export DB_UserDevAdmin=samsitem@${DB_HostNameDev}
export DB_UserDevRegular=legato_dev@${DB_HostPrefix}np
export DB_UserQaAdmin=samsitem@devsamsitm
export DB_UserQaRegular=legato_dev@${DB_HostPrefix}np

###############################################################################
# NOTE: This is what I was told by Bhavana (different from reference)
export DB_UserStageUnknown=legato_dev@samspimstage

###############################################################################
# NOTE: This is what actually works, so far (different from reference)
export DB_HostNameDev=devsamsitm
export DB_HostNameQa=${DB_HostPrefix}np

export DB_HostFqdnDev=${DB_HostNameDev}${DB_HostSuffix}
export DB_HostFqdnQa=${DB_HostNameQa}${DB_HostSuffix}

export DB_NameQa=postgres

export DB_UserDevAdmin=samsitem@${DB_HostNameDev}
export DB_UserQaRegular=legato_dev@${DB_HostPrefix}np
export DB_UserStageUnknown=legato_dev@samspimstage

: << 'DisabledContent'
###############################################################################
# This is what was given to me
export DB_HostDev=devsamsitm.postgres.database.azure.com
export DB_HostQa=legato-pim-postgres-np.postgres.database.azure.com
export DB_NameDev=pim
export DB_NameQa=postgres
export DB_UserDevAdmin=samsitem@devsamsitm
export DB_UserDevRegular=legato_dev@legato-pim-postgres-np
export DB_UserQaAdmin=samsitem@devsamsitm
export DB_UserQaRegular=legato_dev@legato-pim-postgres-np

###############################################################################
# This is what I am trying

export DB_UserDevAdmin=UNKNOWN@${DB_HostNameDev}
export DB_UserDevRegular=UNKNOWN@${DB_HostNameDev}
export DB_UserDevUnknown=legato_dev@${DB_HostNameDev}
export DB_UserQaAdmin=UNKNOWN@${DB_HostNameQa}
export DB_UserQaRegular=UNKNOWN@${DB_HostNameQa}
export DB_UserQaUnknown=legato_dev@${DB_HostNameQa}
DisabledContent

