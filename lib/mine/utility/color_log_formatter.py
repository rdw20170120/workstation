#!/usr/bin/env false
"""A logging formatter with color capability."""
# Internal packages  (absolute references, distributed with Python)
from logging import Formatter
from logging import NOTSET 
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .my_terminal import stderr_supports_color


DEFAULT_DATE_FORMAT = '%y%m%dT%H%M%S'
_levelname = '%(levelname)1.1s'
# _location = '%(module)s:%(lineno)d'
_location = '%(name)s:%(lineno)d'
_message='%(message)s'
_time = '%(asctime)s'
_prefix = ('%(color)s['
    + _levelname + ' ' + _time + ' ' + _location
    + ']%(end_color)s')
DEFAULT_FORMAT = _prefix + ' ' + _message


class ColorLogFormatter(Formatter):
    """Log formatter capable of color on a suitable terminal.

    Based on code in the `logzero` package, which imitates this code in
    `Tornado`.
    """
    def __init__(self,
                 color=True,
                 fmt=DEFAULT_FORMAT,
                 datefmt=DEFAULT_DATE_FORMAT,
                 colors=None):
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
        super().__init__(self, datefmt=datefmt)

        self._fmt = fmt
        self._colors = {}
        self._normal = ''

        if color and stderr_supports_color():
            self._colors = colors
            self._normal = self._colors[NOTSET]

    def format(self, record):
        record.asctime = self.formatTime(record, self.datefmt)

        if record.levelno in self._colors:
            record.color = self._colors[record.levelno]
            record.end_color = self._normal
        else:
            record.color = record.end_color = ''

        formatted = self._fmt % record.__dict__

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        return formatted.replace("\n", "\n    ")


'''DisabledContent
        try:
            message = record.getMessage()
            assert isinstance(message,
                              basestring_type)  # guaranteed by logging
            # Encoding notes:  The logging module prefers to work with character
            # strings, but only enforces that log messages are instances of
            # basestring.  In python 2, non-ascii bytestrings will make
            # their way through the logging framework until they blow up with
            # an unhelpful decoding error (with this formatter it happens
            # when we attach the prefix, but there are other opportunities for
            # exceptions further along in the framework).
            #
            # If a byte string makes it this far, convert it to unicode to
            # ensure it will make it out to the logs.  Use repr() as a fallback
            # to ensure that all byte strings can be converted successfully,
            # but don't do it by default so we don't add extra quotes to ascii
            # bytestrings.  This is a bit of a hacky place to do this, but
            # it's worth it since the encoding errors that would otherwise
            # result are so useless (and tornado is fond of using utf8-encoded
            # byte strings wherever possible).
            record.message = _safe_unicode(message)
        except Exception as e:
            record.message = "Bad message (%r): %r" % (e, record.__dict__)

        if record.exc_text:
            # exc_text contains multiple lines.  We need to _safe_unicode
            # each line separately so that non-utf8 bytes don't cause
            # all the newlines to turn into '\n'.
            lines = [formatted.rstrip()]
            lines.extend(
                _safe_unicode(ln) for ln in record.exc_text.split('\n'))
            formatted = '\n'.join(lines)
'''

