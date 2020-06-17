#!/usr/bin/env false
"""My module for managing logging.

Target effective logging on my favorite development workstations:
* Apple macOS 10.14.6 Mojave running iTerm2 TODO
  with 'TODO' palette
  and 'TODO' scheme
* Linux Mint 19.3 Tricia Cinnamon running default Gnome Terminal
  with 'Solarized' palette
  and 'solarized dark' scheme
"""
import logging

import logzero
from   logzero.colors import Fore

from src_gen.source                     import generate
from src_gen.source                     import my_visitor_map as parent_visitor_map
from src_gen.structure                  import *
from throw_out_your_templates.section_3 import VisitorMap

from .my_terminal import using_gnome
from .my_terminal import using_iterm2


log = logzero.logger
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
    """Dump current logging (logzero) configuration."""
    content = [
        _ansi_colors(),
        nvp('my_terminal.using_gnome', using_gnome()), eol(),
        nvp('my_terminal.using_iterm2', using_iterm2()), eol(),
        nvp('logzero.logger', logzero.logger), eol(),
    ]
    generate(content, visitor_map=my_visitor_map)

def _level_colors():
    result = logzero.LogFormatter.DEFAULT_COLORS
    if using_gnome():
        log.debug("Using Gnome terminal")
        result[logging.CRITICAL] = Fore.WHITE
        return result
    elif using_iterm2():
        log.debug("Using iTerm2 terminal")
        result[logging.CRITICAL] = Fore.WHITE
        return result
    else:
        log.debug("Using unrecognized terminal")
        return result

def _log_samples():
    """Log samples of output at all severity levels."""
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

def configure(config):
    # TODO: Write method to dump actual logging configuration
    # TODO: Set file handler to DEBUG, but stderr handler to INFO
    # TODO: Adjust logging between dev & prd
#   _dump()

    config.log_directory.mkdir(exist_ok=True)
    formatter = logzero.LogFormatter(colors=_level_colors())
    global log
    log = logzero.logger = logzero.setup_logger(
        level=logging.INFO, formatter=formatter,
        logfile=config.log_file, fileLoglevel=logging.DEBUG,
        backupCount=9, maxBytes=1e6
        )

    _log_samples()
    _dump()


'''DisabledContent
# TODO: FIX: This does not work because visitor lookup fails
@my_visitor_map.register(logzero.colors.AnsiCodes)
def _visit_ansi_codes(element, walker):
    for name in dir(element):
        walker.walk(name)
        walker.emit(' = ')
        walker.walk(getattr(element, name))
        walker.emit('\n')
assert my_visitor_map.get_visitor(logzero.colors.Fore) == _visit_ansi_codes

# TODO: FIX: This does not work because visitor lookup fails
@my_visitor_map.register(logzero.colors.AnsiFore)
def _visit_ansi_fore(element, walker):
    for name in dir(element):
        walker.walk(name)
        walker.emit(' = ')
        walker.walk(getattr(element, name))
        walker.emit('\n')
assert my_visitor_map.get_visitor(logzero.colors.Fore) == _visit_ansi_fore
'''

