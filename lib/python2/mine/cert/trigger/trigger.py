from my_time import datetime_as_compact_string_utc
from my_shared import get_command_filename
from my_shared import get_download_directory
from my_shared import get_exit_filename
from my_shared import get_pid_filename
from my_shared import get_process_directory
from my_shared import get_process_status
from my_shared import get_stderr_filename
from my_shared import get_stdout_filename
from my_shared import get_script_filename
from logging import getLogger
from my_assert import is_less_than
from my_assert import is_less_than_message
from my_system import maybe_create_directory
from my_shared import PROCESS_STATUS_DEAD
from my_shared import PROCESS_STATUS_FAILURE
from my_shared import PROCESS_STATUS_RUNNING
from my_shared import PROCESS_STATUS_SUCCESS
from my_shared import PROCESS_STATUS_UNSTARTED
from my_shared import run_command
from my_exam import WHEN_BEGINS
from my_exam import WHEN_DONE
from my_exam import WHEN_EARLY
from my_exam import WHEN_ENDS
from my_exam import WHEN_FINAL
from my_exam import WHEN_LATE
from my_exam import WHEN_LAUNCH
from my_exam import WHEN_STABLE
from my_exam import WHEN_TERMINATE


LOG = getLogger('trigger')

TRIGGER_STATUS_DEAD = PROCESS_STATUS_DEAD
TRIGGER_STATUS_DISABLED = 'DISABLED'
TRIGGER_STATUS_FAILURE = PROCESS_STATUS_FAILURE
TRIGGER_STATUS_OVER_MAXIMUM = 'MAXIMUM'
TRIGGER_STATUS_RUNNING = PROCESS_STATUS_RUNNING
TRIGGER_STATUS_SUCCESS = PROCESS_STATUS_SUCCESS
TRIGGER_STATUS_UNDER_MINIMUM = 'MINIMUM'
TRIGGER_STATUS_UNSTARTED = PROCESS_STATUS_UNSTARTED
TRIGGER_STATUS_WAITING = 'WAITING'


class Trigger(object):
    exam_id = None
    triggers = {}
    url_template = None

    @classmethod
    def visit_all(cls, uptime_in_minutes):
        for t in cls.triggers:
            cls.triggers[t].visit(uptime_in_minutes)

    def __init__(self,
        identifier,
        predecessor = None,
        minimum_uptime_in_minutes = None,
        maximum_uptime_in_minutes = None,
    ):
        super(Trigger, self).__init__()
        self._identifier = identifier
        self._maximum = maximum_uptime_in_minutes
        self._minimum = minimum_uptime_in_minutes
        self._predecessor = predecessor
        self._status = None
        self._status_as_of = None
        self.is_disabled = False
        assert self._minimum <= self._maximum, """Maximum '{0}' must NOT be less than minimum '{1}'
            for Trigger '{2}'""".format(self._maximum, self._minimum, self._identifier)
        self.triggers[self._identifier] = self
        LOG.debug("Constructed Trigger('%s', '%s', '%s', '%s')",
          self._identifier,
          self._predecessor_identifier(),
          self._minimum,
          self._maximum,
        )

    def _predecessor_identifier(self):
        return (None if self._predecessor is None else self._predecessor._identifier)

    def execute(self):
        if self.is_disabled: return None
        LOG.debug("'%s' is executing", self._identifier)
        maybe_create_directory(get_download_directory())
        maybe_create_directory(get_process_directory(self.exam_id))

        file_script = get_script_filename(self._identifier, self.exam_id)    # Real command
        command = "curl -fLsS --output {0} {1}".format(file_script, self.url_template)
        command = command.format(self._identifier)
        command += " ; chmod u+rx {0}".format(file_script)
        command += " ; {0}".format(file_script)

        run_command(
            command,
            get_exit_filename(self._identifier, self.exam_id),
            get_pid_filename(self._identifier, self.exam_id),
            get_stderr_filename(self._identifier, self.exam_id),
            get_stdout_filename(self._identifier, self.exam_id),
            get_command_filename(self._identifier, self.exam_id),
        )

    def get_status(self):
        return get_process_status(
            get_exit_filename(self._identifier, self.exam_id),
            get_pid_filename(self._identifier, self.exam_id),
        )

    def has_executed(self):
        status, as_of = self.get_status()
        if status == PROCESS_STATUS_RUNNING:   return False
        if status == PROCESS_STATUS_UNSTARTED: return False
        return True

    def is_over_maximum(self, uptime_in_minutes):
        return (uptime_in_minutes > self._maximum)

    def is_under_minimum(self, uptime_in_minutes):
        return (uptime_in_minutes < self._minimum)

    def is_waiting_on_predecessor(self):
        if self.is_disabled: return False
        if self._predecessor is None: return False
        if self.has_executed(): return False
        return not self._predecessor.has_executed()

    def visit(self, uptime_in_minutes):
        execute, result = False, None
        status, as_of = self.get_status()
        LOG.debug("At %d minutes uptime - '%s' has status '%s' as of '%s'",
            uptime_in_minutes, self._identifier, status, datetime_as_compact_string_utc(as_of)
        )
        if status == PROCESS_STATUS_DEAD:
            execute, result = False, TRIGGER_STATUS_DEAD
        elif status == PROCESS_STATUS_FAILURE:
            execute, result = False, TRIGGER_STATUS_FAILURE
        elif status == PROCESS_STATUS_RUNNING:
            execute, result = False, TRIGGER_STATUS_RUNNING
        elif status == PROCESS_STATUS_SUCCESS:
            execute, result = False, TRIGGER_STATUS_SUCCESS
        elif status == PROCESS_STATUS_UNSTARTED:
            execute, result = True, TRIGGER_STATUS_UNSTARTED

        if execute:
            if self.is_over_maximum(uptime_in_minutes):
                LOG.debug("At %d minutes uptime - '%s' is over maximum of %d",
                    uptime_in_minutes, self._identifier, self._maximum
                )
                execute, result = True, TRIGGER_STATUS_OVER_MAXIMUM
            if self.is_under_minimum(uptime_in_minutes):
                LOG.debug("At %d minutes uptime - '%s' is under minimum of %d",
                    uptime_in_minutes, self._identifier, self._minimum
                )
                execute, result = False, TRIGGER_STATUS_UNDER_MINIMUM
            if self.is_waiting_on_predecessor():
                LOG.debug("At %d minutes uptime - '%s' is waiting on predecessor '%s'",
                    uptime_in_minutes, self._identifier, self._predecessor_identifier()
                )
                execute, result = False, TRIGGER_STATUS_WAITING
            if self.is_disabled:
                LOG.debug("At %d minutes uptime - '%s' is disabled",
                    uptime_in_minutes, self._identifier
                )
                execute, result = False, TRIGGER_STATUS_DISABLED

        self._status, self._status_as_of = result, as_of
        LOG.info("At %d minutes uptime - trigger '%s' has status '%s' as of '%s'",
            uptime_in_minutes, self._identifier,
            self._status, datetime_as_compact_string_utc(self._status_as_of)
        )

        if execute:
            LOG.debug("At %d minutes uptime - '%s' SHOULD execute",
                uptime_in_minutes, self._identifier
            )
            self.execute()
        else:
            LOG.debug("At %d minutes uptime - '%s' should NOT execute",
                uptime_in_minutes, self._identifier
            )
        return self._status, self._status_as_of


def _requireTimeOrder(earlierName, earlierMinutes, laterName, laterMinutes):
    if not is_less_than(earlierName, earlierMinutes, laterName, laterMinutes):
        raise ValueError(is_less_than_message(earlierName, earlierMinutes, laterName, laterMinutes))

def configure():
    # Assert proper time ordering relationships
    _requireTimeOrder('WHEN_LAUNCH', WHEN_LAUNCH, 'WHEN_STABLE',    WHEN_STABLE)
    _requireTimeOrder('WHEN_STABLE', WHEN_STABLE, 'WHEN_EARLY',     WHEN_EARLY)
    _requireTimeOrder('WHEN_EARLY',  WHEN_EARLY,  'WHEN_BEGINS',    WHEN_BEGINS)
    _requireTimeOrder('WHEN_BEGINS', WHEN_BEGINS, 'WHEN_LATE',      WHEN_LATE)
    _requireTimeOrder('WHEN_LATE',   WHEN_LATE,   'WHEN_ENDS',      WHEN_ENDS)
    _requireTimeOrder('WHEN_ENDS',   WHEN_ENDS,   'WHEN_DONE',      WHEN_DONE)
    _requireTimeOrder('WHEN_DONE',   WHEN_DONE,   'WHEN_FINAL',     WHEN_FINAL)
    _requireTimeOrder('WHEN_FINAL',  WHEN_FINAL,  'WHEN_TERMINATE', WHEN_TERMINATE)

    initialize = Trigger('initialize', None,       WHEN_STABLE, WHEN_BEGINS)
    began      = Trigger('began',      initialize, WHEN_STABLE, WHEN_EARLY)
    answer     = Trigger('answer',     began,      WHEN_EARLY,  WHEN_LATE)
    ended      = Trigger('ended',      began,      WHEN_ENDS,   WHEN_DONE)
    answered   = Trigger('answered',   ended,      WHEN_ENDS,   WHEN_DONE)
    grade      = Trigger('grade',      ended,      WHEN_ENDS,   WHEN_DONE)
    graded     = Trigger('graded',     grade,      WHEN_ENDS,   WHEN_DONE)
    score      = Trigger('score',      grade,      WHEN_ENDS,   WHEN_DONE)
    scored     = Trigger('scored',     score,      WHEN_ENDS,   WHEN_DONE)
    unanswer   = Trigger('unanswer',   scored,     WHEN_ENDS,   WHEN_DONE)
    final      = Trigger('final',      unanswer,   WHEN_ENDS,   WHEN_FINAL)

    # NOTE: Rearrange these as appropriate for deployed environment
    answer.is_disabled = True   # For manual testing and production
    answer.is_disabled = False  # For automated testing


""" Disabled content
NOTE:  For Trigger.execute()

    from random import randint

    command = "echo Hello ; echo World 1>&2 ; exit 1"                    # Force failure
    command = "echo 'Hello World'"                                       # Force success
    command = "echo 'Hello World' ; sleep {0}".format(randint(0, 1000))  # Force random wait
"""

