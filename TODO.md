# TODO items for this project
These are outstanding items of work for us to do.
Each item should be annotated to facilitate prioritization.
Annotations should be specified
as low (L), medium (M), or high (H)
for the importance (I) and the urgency (U) of each item.
Prioritizing can be accomplished
by physically reordering the items in the list.
Obviously, items with higher importance and/or higher urgency
should be prioritized for earlier implementation.
Of course,
ordering should also respect dependencies between items,
when relevant.

Items should be checked-off
and perhaps moved to the bottom
when completed.
Items should be struck-out
to indicate that they have been canceled,
unless they should merely be deleted.

1. [ ] I/U = Item Description

1. [ ] H/H - Switch from Python virtual environment to Anaconda environment
1. [ ] H/H - Copy Solarized color palettes from iTerm2 to Linux Mint terminal
1. [ ] H/H - Add `redeclare` alias to `source` Bash function declarations again
1. [ ] H/H - Extend code generation to all Bash scripts
1. [ ] H/H - Implement full test suite for code generation functionality
1. [ ] H/H - Disable Python3 automatic encoding coercion between ASCII and Unicode
1. [ ] H/H - Use pytest parameterization to extend test suites
1. [ ] M/M - Test for appropriate shebang on all source
1. [ ] M/M - Fix inappropriate shebang on any source
1. [ ] M/L - Document use of `.bash` file extension for Bash scripts that are `source`d
1. [ ] M/L - Document use of `.py` file extension for Python source
1. [ ] M/L - Document dropped file extension for scripts (Bash, Python, etc.)
1. [ ] M/L - Document use of shebang for Python scripts
1. [ ] M/L - Document disabled shebang for Python source
1. [ ] M/L - Document disabled shebang for Bash scripts that are `source`d
1. [ ] M/L - Document conventions for executing Python module
1. [ ] M/L - Implement full test suite for environment variable character encodings
1. [ ] M/L - Generate a subshell environment for each character encoding with every possible character
1. [ ] M/L - Implement full test suite for file character encodings
1. [ ] M/L - Generate a file for each character encoding with every possible character
1. [ ] L/L - Define code generation methods for common test result patterns
1. [ ] L/L - Implement code generation for testing code generation functionality
1. [ ] L/L - Switch font in Neovim for better readability
1. [ ] L/L - Switch font in shell for better readability
1. [ ] L/L - Configure Neovim to position itself
1. [ ] L/L - Configure shell to position itself
1. [X] H/H - Convert to Python3 source code
1. [X] L/L - Move captured output files to `out` directory
1. [X] H/H - Fix broken code generation functionality
1. [X] H/H - Implement methods for always using text files with default UTF-8 encoding
1. [X] H/H - Log Bash messages to stderr instead of stdout
1. [X] H/H - Enhance Bash activation to declare functions

## Notes
### iTerm2 color palettes
These Solarized color palettes are very effective.
So copy them to other terminals,
such as in Linux Mint.

#### Solarized Dark Higher Contrast
        Black   Red     Green   Yellow  Blue    Magenta Cyan    White
Normal  003440  dc312e  fcc67f  b58900  268ad2  d33582  2aa197  eee8d5
Bright  00779a  f9314b  5bee96  c08f34  109fd2  e9679f  00bdae  fdf6e3

Main aacccd/002833  Cursor 003440/f86100  Selection 8ca09f/00475a
Badge ff2600  Bold c1dcdb  Guide b3ecff  Links 005bbb

#### Solarized Light
        Black   Red     Green   Yellow  Blue    Magenta Cyan    White
Normal  073642  dc322f  859900  b58900  268bd2  d33682  2aa198  eee8d5
Bright  002b36  cb4b16  586375  586e75  657b83  839496  93a1a1  fdf6e3

Main 657b83/fdf6e3  Cursor eee8d5/657b83  Selection 586e75/eee8d5
Badge ff2600  Bold 586375  Guide b3ecff  Links 005bbb

