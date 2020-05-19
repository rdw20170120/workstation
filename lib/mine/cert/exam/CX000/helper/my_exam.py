EXAM_ID = 'CX000'

# Known environments
ENV_DEV = 'development'
ENV_PROD = 'production'
ENV_TEST = 'test'

####################################################################################################
# Exam timing in minutes from boot (uptime)

# Proctor PSI defines exam timing as environment launch and terminate, calculated around the
# scheduled exam start.  PSI uses "setup" to refer to the time between launch and exam start.
# They use "breakdown" to refer to the time after the exam ends until terminate.  PSI allows the
# examinee to arrive as much as fifteen minutes before exam start, to as much as fifteen minutes
# after exam start.

WHEN_LAUNCH = 0
WHEN_STABLE = WHEN_LAUNCH + 15

# NOTE: Production - move as needed for deployed environment, last one executed wins
environment = ENV_PROD
PSI_DURATION_BREAKDOWN = 15
PSI_DURATION_EXAM = 5
PSI_DURATION_GRACE = 1
PSI_DURATION_SETUP = 20

# NOTE: Dev/Test - move as needed for deployed environment, last one executed wins
environment = ENV_DEV
environment = ENV_TEST
PSI_DURATION_BREAKDOWN = 15
PSI_DURATION_EXAM = 5
PSI_DURATION_GRACE = 1
PSI_DURATION_SETUP = 20

# Derived constants
PSI_DURATION_TOTAL = PSI_DURATION_SETUP + PSI_DURATION_EXAM + PSI_DURATION_BREAKDOWN
WHEN_TERMINATE = WHEN_LAUNCH + PSI_DURATION_TOTAL
WHEN_BEGINS = WHEN_LAUNCH + PSI_DURATION_SETUP
WHEN_EARLY = WHEN_BEGINS - PSI_DURATION_GRACE
WHEN_LATE = WHEN_BEGINS + PSI_DURATION_GRACE
WHEN_ENDS = WHEN_LATE + PSI_DURATION_EXAM
WHEN_DONE = WHEN_ENDS + 4*PSI_DURATION_GRACE
WHEN_FINAL = WHEN_TERMINATE - 4*PSI_DURATION_GRACE


""" Disabled content
"""

