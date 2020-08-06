#!/usr/bin/env false
"""My module for logging.

Target effective logging on my favorite development workstations:
* Apple macOS 10.14.6 Mojave running iTerm2 3.3.9
  with 'Solarized Dark Higher Contrast' color preset
* Linux Mint 19.3 Tricia Cinnamon running default Gnome Terminal
  with 'Solarized' palette
  and 'solarized dark' scheme

TODO: Add visitors for other `logging` handlers
"""
# Internal packages  (absolute references, distributed with Python)
from   logging import getLogger
import logging
# External packages  (absolute references, NOT distributed with Python)
from   logzero.colors import Fore
import logzero
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.source                     import generate
from src_gen.source                     import my_visitor_map as parent_visitor_map
from src_gen.structure                  import *
from throw_out_your_templates.section_3 import VisitorMap
# Co-located modules (relative references, NOT packaged, in project)
from .color_log_formatter import ColorLogFormatter
from .my_terminal         import using_gnome
from .my_terminal         import using_iterm2


DEFAULT_DATE_FORMAT = '%Y%m%dT%H%M%S'
_levelname = '%(levelname)5s'
# _location = '%(module)s:%(lineno)d'
_location = '%(name)s:%(lineno)d'
_message='%(message)s'
_time = '%(asctime)s'
_prefix = '[' + _levelname + ' ' + _time + ' ' + _location + ']'
DEFAULT_FORMAT = _prefix + ' ' + _message

_file_handler = None
_root_logger = None
_stderr_handler = None

log = getLogger(__name__)
my_visitor_map = VisitorMap(parent_map=parent_visitor_map)


def _ansi_color(name, index, codes):
    return [
        codes,
        'This is ANSI foreground color ', index,
        ' known to logzero as ', name,
        Fore.RESET,
        eol(),
    ]

def _ansi_colors():
    return [
        _ansi_color('BLACK', 30, Fore.BLACK),
        _ansi_color('RED', 31, Fore.RED),
        _ansi_color('GREEN', 32, Fore.GREEN),
        _ansi_color('YELLOW', 33, Fore.YELLOW),
        _ansi_color('BLUE', 34, Fore.BLUE),
        _ansi_color('MAGENTA', 35, Fore.MAGENTA),
        _ansi_color('CYAN', 36, Fore.CYAN),
        _ansi_color('WHITE', 37, Fore.WHITE),
        _ansi_color('RESET', 39, Fore.RESET),
        _ansi_color('LIGHTBLACK_EX', 90, Fore.LIGHTBLACK_EX),
        _ansi_color('LIGHTRED_EX', 91, Fore.LIGHTRED_EX),
        _ansi_color('LIGHTGREEN_EX', 92, Fore.LIGHTGREEN_EX),
        _ansi_color('LIGHTYELLOW_EX', 93, Fore.LIGHTYELLOW_EX),
        _ansi_color('LIGHTBLUE_EX', 94, Fore.LIGHTBLUE_EX),
        _ansi_color('LIGHTMAGENTA_EX', 95, Fore.LIGHTMAGENTA_EX),
        _ansi_color('LIGHTCYAN_EX', 96, Fore.LIGHTCYAN_EX),
        _ansi_color('LIGHTWHITE_EX', 97, Fore.LIGHTWHITE_EX),
    ]

def _dump():
    """Dump current `log` configuration."""
    content = [
        _ansi_colors(),
        nvp('my_terminal.using_gnome', using_gnome()), eol(),
        nvp('my_terminal.using_iterm2', using_iterm2()), eol(),
        nvp('logzero.logger', logzero.logger), eol(),
        nvp('logging.getLogger()', logging.getLogger()), eol(),
    ]
    generate(content, visitor_map=my_visitor_map)

def _formatter(for_stderr=False):
    if for_stderr:
        return ColorLogFormatter(colors=_level_colors())
    else:
        return logging.Formatter(
            fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT
            )

def _level_colors():
    result = logzero.LogFormatter.DEFAULT_COLORS
    result[logging.NOTSET] = Fore.RESET
    if using_gnome():
        result[logging.DEBUG] = Fore.GREEN
        result[logging.INFO] = Fore.CYAN
        result[logging.WARNING] = Fore.YELLOW
        result[logging.ERROR] = Fore.RED
        result[logging.CRITICAL] = Fore.WHITE
    elif using_iterm2():
        result[logging.DEBUG] = Fore.CYAN
        result[logging.INFO] = Fore.LIGHTGREEN_EX
        result[logging.WARNING] = Fore.LIGHTYELLOW_EX
        result[logging.ERROR] = Fore.LIGHTRED_EX
        result[logging.CRITICAL] = Fore.LIGHTWHITE_EX
    else:
        # These are the logzero defaults
        result[logging.DEBUG] = Fore.CYAN
        result[logging.INFO] = Fore.GREEN
        result[logging.WARNING] = Fore.YELLOW
        result[logging.ERROR] = Fore.RED
        # Except logzero has no default for CRITICAL
        result[logging.CRITICAL] = Fore.WHITE
    return result

def _log_samples():
    """Samples of log output at each severity level."""
    log.debug('This is a sample DEBUG message.')
    log.info('This is a sample INFO message.')
    log.warn('This is a sample WARNING message.')
    log.error('This is a sample ERROR message.')
    log.fatal('This is a sample CRITICAL message.')

@my_visitor_map.register(logging.Formatter)
def _visit_formatter(element, walker):
    walker.emit('Formatter(')
#   walker.emit('attributes: ')
#   walker.walk(repr(dir(element)))
    walker.emit(')')

@my_visitor_map.register(logzero.LogFormatter)
def _visit_logformatter(element, walker):
    walker.emit('LogFormatter(')
    walker.emit('_colors: ')
    walker.walk(repr(element._colors))
#   walker.emit(', attributes: ')
#   walker.walk(repr(dir(element)))
    walker.emit(')')

@my_visitor_map.register(logging.Logger)
def _visit_logger(element, walker):
    walker.emit('Logger(')
    walker.emit('name=')
    walker.walk(element.name)
    walker.emit(', disabled=')
    walker.walk(element.disabled)
    walker.emit(', getEffectiveLevel=')
    walker.walk(element.getEffectiveLevel())
    walker.emit(', propagate=')
    walker.walk(element.propagate)
#   walker.emit(', attributes: ')
#   walker.walk(repr(dir(element)))
    walker.emit(')')
    walker.emit('\nhandlers:\n')
    for h in element.handlers:
        walker.walk(h)
        walker.emit('\n')

@my_visitor_map.register(logging.StreamHandler)
def _visit_streamhandler(element, walker):
    walker.emit('StreamHandler(')
    walker.emit('name=')
    walker.walk(element.name)
    walker.emit(', formatter=')
    walker.walk(element.formatter)
    walker.emit(', level=')
    walker.walk(element.level)
#   walker.emit(', attributes: ')
#   walker.walk(repr(dir(element)))
    walker.emit(')')

def apply_verbosity(verbosity=0):
    _file_handler.setLevel(logging.DEBUG)
    _root_logger.setLevel(logging.DEBUG)
    if not verbosity:
        _stderr_handler.setLevel(logging.FATAL)
    elif verbosity == 1:
        _stderr_handler.setLevel(logging.ERROR)
    elif verbosity == 2:
        _stderr_handler.setLevel(logging.WARNING)
    elif verbosity == 3:
        _stderr_handler.setLevel(logging.INFO)
    else:
        _stderr_handler.setLevel(logging.DEBUG)

def configure(config):
    # TODO: Adjust logging between dev & prd
    logzero.logger = None
    config.log_directory.mkdir(exist_ok=True)

    global _root_logger
    _root_logger = logging.getLogger()

    global _file_handler
    _file_handler = logging.handlers.RotatingFileHandler(
        config.log_file, encoding='utf_8',
        backupCount=9, maxBytes=1e6
        )
    _file_handler.setFormatter(_formatter(for_stderr=False))
    _root_logger.addHandler(_file_handler)

    global _stderr_handler
    _stderr_handler = logging.StreamHandler()
    _stderr_handler.setFormatter(_formatter(for_stderr=True))
    _root_logger.addHandler(_stderr_handler)
    apply_verbosity()

def debug(logger, name, value):
    logger.debug("%s = %s", name, value)

def report_configuration():
    _dump()
    # TODO: Temporarily increase verbosity to show all samples
    _log_samples()


'''DisabledContent
'''

