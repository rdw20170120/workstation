import sys

from my_time import datetime_formatted

EXTENSION = ".tb2"


class Tarball(object):
    def __init__(self, filename):
        self._filename = filename

    def assemble(self):
        pass

    def upload(self):
        pass


class ExamResultsTarball(Tarball):
    def __init__(
        self,
        project_name,
        project_version,
        exam_id,
        phase,
        date_time,
        session_id,
    ):
        self._phase = phase
        Tarball.__init__(
            self,
            "{0}-{1}-{2}-{3}-{6}-{4}{5}".format(
                project_name,
                project_version,
                exam_id,
                phase,
                session_id,
                EXTENSION,
                datetime_formatted(date_time, "{0:%Y%m%dT%H%M%S}Z"),
            ),
        )


""" Disabled content
"""
