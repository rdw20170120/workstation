#!/usr/bin/env python

import argparse
import os
import sys

from logging import getLogger
from logging import Logger
from my_assert import has_type
from my_assert import has_type_message
from my_configuration import get_directory_output
from my_configuration import get_exam_id
from my_configuration import get_project_name
from my_configuration import get_project_version
from my_configuration import get_session_id
from my_configuration import get_task_count_init
from my_configuration import get_task_count_main
from my_exception import UnrecognizedValueError
from my_logging import configure_logging
from my_system import directory_exists
from my_system import get_current_directory
from my_system import get_empty_files
from my_system import get_files
from my_system import maybe_create_directory
from my_time import now
from tarball import ExamResultsTarball
from types import FileType
from types import IntType
from types import StringType


PHASE_ANSWER = 'answer'
PHASE_ANSWERED = 'answered'
PHASE_BEGAN = 'began'
PHASE_ENDED = 'ended'
PHASE_FINAL = 'final'
PHASE_GRADE = 'grade'
PHASE_GRADED = 'graded'
PHASE_INITIALIZE = 'initialize'
PHASE_PREPARE = 'prepare'
PHASE_SCORE = 'score'
PHASE_SCORED = 'scored'
PHASE_UNANSWER = 'unanswer'
PHASE_WRITE = 'write'

SESSION_ID_PREPARE = 'PREPARE'

STAGE_ENV = 'environment'
STAGE_INIT = 'init'
STAGE_INSTRUCT = 'instruction'
STAGE_MAIN = 'main'

COMMAND_ANSWER = PHASE_ANSWER
COMMAND_ANSWERED = PHASE_ANSWERED
COMMAND_BEGAN = PHASE_BEGAN
COMMAND_ENDED = PHASE_ENDED
COMMAND_FINAL = PHASE_FINAL
COMMAND_GRADE = PHASE_GRADE
COMMAND_GRADED = PHASE_GRADED
COMMAND_INITIALIZE = PHASE_INITIALIZE
COMMAND_INSTRUCT = STAGE_INSTRUCT
COMMAND_PREPARE = PHASE_PREPARE
COMMAND_RUN = 'run'
COMMAND_SCORE = PHASE_SCORE
COMMAND_SCORED = PHASE_SCORED
COMMAND_UNANSWER = PHASE_UNANSWER

LOG = getLogger('exam')


class ExamStatus(object):
    def __init__(self, session_id, stage, phase):
        assert has_type(stage, StringType), has_type_message(stage, StringType)
        assert has_type(phase, StringType), has_type_message(phase, StringType)
        self._exam_id = get_exam_id()
        self._phase = phase
        self._session_id = session_id
        self._stage = stage

    def _debug(self, message, of):
        assert has_type(message, StringType), has_type_message(message, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        LOG.debug(message)
        of.write(message)

    def _fail(self, message, of):
        assert has_type(message, StringType), has_type_message(message, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        self._warn("FAIL:  {0}".format(message), of)

    def _get_output_directory(self, phase):
        assert has_type(phase, StringType), has_type_message(phase, StringType)
        return os.path.join(get_directory_output(), self._stage, phase)

    def _grab_output_files(self):
        LOG.info("Grabbing exam output for phase '%s'", self._phase)
        tarball = ExamResultsTarball(
            get_project_name(),
            get_project_version(),
            self._exam_id,
            self._phase,
            now(),
            self._session_id,
        )
        tarball.assemble()
        tarball.upload()

    def _info(self, message, of):
        assert has_type(message, StringType), has_type_message(message, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        LOG.info(message)
        of.write(message)

    def _pass(self, message, of):
        assert has_type(message, StringType), has_type_message(message, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        self._info("PASS:  {0}".format(message), of)

    def _report_status(self, task_count):
        assert has_type(task_count, IntType), has_type_message(task_count, IntType)
        od = self._get_output_directory(self._phase)
        maybe_create_directory(od)
        of = os.path.join(od, 'status.log')
        with open(of, 'w') as of:
            self._info(
                "Reporting status of exam phase '{0}' to file '{1}'".format(self._phase, of.name), of
            )
            self._report_status_of_tasks(PHASE_ANSWER,   task_count, od, of)
            self._report_status_of_tasks(PHASE_GRADE,    task_count, od, of)
            self._report_status_of_tasks(PHASE_UNANSWER, task_count, od, of)
            od = self._get_output_directory(PHASE_SCORE)
            if directory_exists(od):
                self._report_found_directory(od, of)
                self._report_status_of_files('err',   1, 1, od, of)
                self._report_status_of_files('out',   1, 1, od, of)
                self._report_status_of_files('score', 1, 0, od, of)
            else:
                self._report_missing_directory(od, of)

    def _report_found_directory(self, od, of):
        assert has_type(od, StringType), has_type_message(od, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        self._debug("CHECK: Found   directory '{0}'".format(od), of)

    def _report_missing_directory(self, od, of):
        assert has_type(od, StringType), has_type_message(od, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        self._warn("SKIP:  Missing directory '{0}'".format(od), of)

    def _report_status_of_files(
        self, file_extension, total_file_count, empty_file_count, od, of
    ):
        assert has_type(file_extension, StringType), has_type_message(file_extension, StringType)
        assert has_type(total_file_count, IntType), has_type_message(total_file_count, IntType)
        assert has_type(empty_file_count, IntType), has_type_message(empty_file_count, IntType)
        assert has_type(od, StringType), has_type_message(od, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        pattern = '.+\.{0}'.format(file_extension)
        empty = get_empty_files(od, pattern)
        # LOG.info('Empty = %s', empty)
        empty = len(empty)
        total = get_files(od, pattern)
        # LOG.info('Total = %s', total)
        total = len(total)
        message = "Found {0}/{1} '{2}' files, of which {3}/{4} are empty".format(
            total, total_file_count, file_extension, empty, empty_file_count
        )
        if total != total_file_count:   self._fail(message, of)
        elif empty != empty_file_count: self._fail(message, of)
        else:                           self._pass(message, of)

    def _report_status_of_tasks(self, phase, task_count, od, of):
        assert has_type(phase, StringType), has_type_message(phase, StringType)
        assert has_type(task_count, IntType), has_type_message(task_count, IntType)
        assert has_type(od, StringType), has_type_message(od, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        self._info(
            "Reporting status of exam phase '{0}' to file '{1}'".format(phase, of.name), of
        )
        if directory_exists(od):
            self._report_found_directory(od, of)
            self._report_status_of_files('err',    task_count, task_count, od, of)
            self._report_status_of_files('out',    task_count, 0,          od, of)
            self._report_status_of_files('timing', task_count, 0,          od, of)
        else:
            self._report_missing_directory(od, of)
        pass

    def report(self, task_count):
        assert has_type(task_count, IntType), has_type_message(task_count, IntType)
        self._report_status(task_count)
        self._grab_output_files()

    def _warn(self, message, of):
        assert has_type(message, StringType), has_type_message(message, StringType)
        assert has_type(of, FileType), has_type_message(of, FileType)
        LOG.warn(message)
        of.write(message)

class Exam(object):
    def __init__(self):
        self._directory = get_current_directory()

    def answer(self):
        LOG.info('Executing answer()')
        stage, phase = STAGE_MAIN, PHASE_ANSWER
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-answer.bash \
        #   self._directory/helper/tasks-main.bash \
        #   self._directory/helper/segments.src
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def answered(self):
        LOG.info('Executing answered()')
        stage, phase = STAGE_MAIN, PHASE_ANSWERED
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/files-grab-answer.bash $2

    def began(self):
        LOG.info('Executing began()')
        stage, phase = STAGE_MAIN, PHASE_BEGAN
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def ended(self):
        LOG.info('Executing ended()')
        stage, phase = STAGE_MAIN, PHASE_ENDED
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def final(self):
        LOG.info('Executing final()')
        stage, phase = STAGE_MAIN, PHASE_FINAL
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def grade(self):
        LOG.info('Executing grade()')
        stage, phase = STAGE_MAIN, PHASE_GRADE
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-grade.bash \
        #   self._directory/helper/tasks-main.bash \
        #   self._directory/helper/segments.src
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def graded(self):
        LOG.info('Executing graded()')
        stage, phase = STAGE_MAIN, PHASE_GRADED
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def initialize(self):
        LOG.info('Executing initialize()')
        stage, phase = STAGE_INIT, PHASE_INITIALIZE
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # variableRequire CB_Client_FileSessionId
        # Write a new Couchbase session id
        # openssl rand -hex -out $CB_Client_FileSessionId 32
        # abortOnFail $0:$FUNCNAME $LINENO $?
        # variableRequire CB_ExamTasksInit
        # local -r ScriptTasks=self._directory/helper/tasks-init.bash
        # local -r ScriptSegments=self._directory/helper/segments.src
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-answer.bash $ScriptTasks $ScriptSegments
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-grade.bash  $ScriptTasks $ScriptSegments
        # local -r DirGrade="$(getOutputDirectory $1 grade)"
        # local -r DirScore="$(getOutputDirectory $1 score)"
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-score.bash \
        #   self._directory/helper/score_weights.data \
        #   $DirGrade \
        #   $DirScore
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_init())

    def instruction(self):
        LOG.info('Executing instruction()')
        stage, phase = STAGE_INSTRUCT, PHASE_WRITE
        # CB_Container=Hatsize
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # Script=$BO_Project/bin/helper/Linux/declare-instructions.src
        # scriptRequire $0:$FUNCNAME $LINENO $Script ; source $Script ; abortOnFail $0:$FUNCNAME $LINENO $?
        # export TMPDIR=$CB_Client_DirTmp/instruction/$CB_ExamId
        # directoryCreate "$TMPDIR"
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-write-support.bash
        # export TMPDIR=$CB_Client_DirTmp/instruction/$CB_ExamId/init
        # directoryCreate "$TMPDIR"
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-write-agenda.bash \
        #   self._directory/helper/tasks-init.bash \
        #   self._directory/helper/segments.src
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-write-tasks.bash \
        #   self._directory/helper/tasks-init.bash \
        #   self._directory/helper/segments.src
        # export TMPDIR=$CB_Client_DirTmp/instruction/$CB_ExamId/main
        # directoryCreate "$TMPDIR"
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-write-agenda.bash \
        #   self._directory/helper/tasks-main.bash \
        #   self._directory/helper/segments.src
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-write-tasks.bash \
        #   self._directory/helper/tasks-main.bash \
        #   self._directory/helper/segments.src

    def prepare(self):
        LOG.info('Executing prepare()')
        stage, phase = STAGE_ENV, PHASE_PREPARE
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # Script=$BO_Project/bin/helper/Linux/declare-download.src
        # scriptRequire $0:$FUNCNAME $LINENO $Script ; source $Script ; abortOnFail $0:$FUNCNAME $LINENO $?
        # scriptExecute $0:$FUNCNAME $LINENO self._directory/helper/files-download.bash
        # scriptExecute $0:$FUNCNAME $LINENO self._directory/helper/OS-configure.bash
        # [[ -z "$CB_SessionId" ]] && export CB_SessionId=PREPARE
        status = ExamStatus(SESSION_ID_PREPARE, stage, phase)
        status.report(get_task_count_main())

    def run(self):
        LOG.info('Executing run()')
        Exam().initialize()
        Exam().began()
        Exam().answer()
        Exam().ended()
        Exam().answered()
        Exam().grade()
        Exam().graded()
        Exam().score()
        Exam().scored()
        Exam().unanswer()
        Exam().final()

    def score(self):
        LOG.info('Executing score()')
        stage, phase = STAGE_MAIN, PHASE_SCORE
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # local -r DirGrade="$(getOutputDirectory $1 grade)"
        # local -r DirScore="$(getOutputDirectory $1 score)"
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-score.bash \
        #   self._directory/helper/score_weights.data $DirGrade $DirScore
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def scored(self):
        LOG.info('Executing scored()')
        stage, phase = STAGE_MAIN, PHASE_SCORED
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

    def unanswer(self):
        LOG.info('Executing unanswer()')
        stage, phase = STAGE_MAIN, PHASE_UNANSWER
        LOG.info("Executing phase '%s' within stage '%s' in directory '%s'",
            phase, stage, self._directory)
        # scriptExecute $0:$FUNCNAME $LINENO $BO_Project/bin/helper/Linux/exam-setup.bash \
        #   self._directory/helper/tasks-main.bash \
        #   self._directory/helper/segments.src
        status = ExamStatus(get_session_id(), stage, phase)
        status.report(get_task_count_main())

def main():
    try:
        configure_logging()
        # adjust_logging()

        parser = argparse.ArgumentParser()
        parser.add_argument('subcommand', help='...to execute, typically an exam phase')
        args = parser.parse_args()

        if   args.subcommand == COMMAND_INSTRUCT:   Exam().instruction()
        elif args.subcommand == COMMAND_PREPARE:    Exam().prepare()
        elif args.subcommand == COMMAND_INITIALIZE: Exam().initialize()
        elif args.subcommand == COMMAND_BEGAN:      Exam().began()
        elif args.subcommand == COMMAND_ANSWER:     Exam().answer()
        elif args.subcommand == COMMAND_ENDED:      Exam().ended()
        elif args.subcommand == COMMAND_ANSWERED:   Exam().answered()
        elif args.subcommand == COMMAND_GRADE:      Exam().grade()
        elif args.subcommand == COMMAND_GRADED:     Exam().graded()
        elif args.subcommand == COMMAND_SCORE:      Exam().score()
        elif args.subcommand == COMMAND_SCORED:     Exam().scored()
        elif args.subcommand == COMMAND_UNANSWER:   Exam().unanswer()
        elif args.subcommand == COMMAND_FINAL:      Exam().final()
        elif args.subcommand == COMMAND_RUN:        Exam().run()
        else: raise UnrecognizedValueError(args.subcommand, type(args.subcommand), 'subcommand')

        LOG.debug("main() try = began")
    except Exception as e:
        LOG.error("main() except Exception = failure")
        LOG.exception(e)
        sys.exit(1)
    else:
        LOG.debug("main() else = success")
        sys.exit(0)
    finally:
        LOG.debug("main() finally = ended")


if __name__ == '__main__':
    main()


""" Disabled content
"""

