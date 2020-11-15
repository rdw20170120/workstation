#!/usr/bin/env false
"""A logging formatter with color capability."""
# Internal packages (absolute references, distributed with Python)
from logging import Formatter
from logging import NOTSET

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.my_terminal import stderr_supports_color

# Project modules   (relative references, NOT packaged, in project)


DEFAULT_DATE_FORMAT = "%y%m%dT%H%M%S"
_levelname = "%(levelname)1.1s"
# _location = '%(module)s:%(lineno)d'
_location = "%(name)s:%(lineno)d"
_message = "%(message)s"
_time = "%(asctime)s"
_prefix = str(
    "%(color)s["
    + _levelname
    + " "
    + _time
    + " "
    + _location
    + "]%(end_color)s"
)
DEFAULT_FORMAT = _prefix + " " + _message


class ColorLogFormatter(Formatter):
    """Log formatter capable of color on a suitable terminal.

    Based on code in the `logzero` package, which imitates this code in
    `Tornado`.
    """

    def __init__(
        self,
        color=True,
        colors=None,
        datefmt=DEFAULT_DATE_FORMAT,
        fmt=DEFAULT_FORMAT,
    ):
        r"""
        :arg bool color: Enables color support.
        :arg string fmt: Log message format.
          It will be applied to the attributes dict of log records. The
          text between ``%(color)s`` and ``%(end_color)s`` will be colored
          depending on the level if color support is on.
        :arg dict colors: color mappings from logging level to terminal color
          code
        :arg string datefmt: Datetime format.
          Used for formatting ``(asctime)`` placeholder in ``prefix_fmt``.
        """
        super().__init__(datefmt=datefmt, fmt=fmt)

        self._fmt = fmt
        self._colors = {}
        self._normal = ""

        if color and stderr_supports_color():
            self._colors = colors
            self._normal = self._colors[NOTSET]

    def format(self, record):
        record.asctime = self.formatTime(record, self.datefmt)

        if record.levelno in self._colors:
            record.color = self._colors[record.levelno]
            record.end_color = self._normal
        else:
            record.color = record.end_color = ""

        formatted = self._fmt % record.__dict__

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        return formatted.replace("\n", "\n    ")


"""DisabledContent
"""
