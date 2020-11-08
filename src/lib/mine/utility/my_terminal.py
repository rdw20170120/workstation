#!/usr/bin/env false
"""My module for managing the terminal.

Target effective recognition of my favorite development workstations:
* Apple macOS 10.14.6 Mojave running iTerm2 TODO
  with 'TODO' palette
  and 'TODO' scheme
* Linux Mint 19.3 Tricia Cinnamon running default Gnome Terminal
  with 'Solarized' palette
  and 'solarized dark' scheme
"""
# Internal packages  (absolute references, distributed with Python)
try:
    import curses
except ImportError:
    curses = None
import sys

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import environment

# Co-located modules (relative references, NOT packaged, in project)


def stderr_supports_color():
    """Return whether the stderr stream supports color.

    Based on code in the `logzero` package, which imitates this code in
    `Tornado`.
    """
    # Detect color support of stderr with curses (Linux/macOS)
    if curses and hasattr(sys.stderr, "isatty") and sys.stderr.isatty():
        try:
            curses.setupterm()
            if curses.tigetnum("colors") > 0:
                return True
        except Exception:
            pass
    return False


def using_gnome():
    """Return whether we think that we are using a Gnome terminal."""
    return environment.has("GNOME_TERMINAL_SCREEN") or environment.has(
        "GNOME_TERMINAL_SERVICE"
    )


def using_iterm2():
    """Return whether we think that we are using an iTerm2 terminal.

    TODO: Consider checking TERM_PROGRAM=iTerm.app and LC_TERMINAL=iTerm2
    """
    return environment.has("ITERM_PROFILE") or environment.has("ITERM_SESSION")


"""DisabledContent
logzero.colors.Fore:
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37
RESET = 39
LIGHTBLACK_EX = 90
LIGHTRED_EX = 91
LIGHTGREEN_EX = 92
LIGHTYELLOW_EX = 93
LIGHTBLUE_EX = 94
LIGHTMAGENTA_EX = 95
LIGHTCYAN_EX = 96
LIGHTWHITE_EX = 97
"""
