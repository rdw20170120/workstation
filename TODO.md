# TODO items for this project
These are outstanding items of work for us to do.
Each item should be annotated to facilitate prioritization.
Annotations should be specified
as 1 (highest) to 3 (or more, lowest)
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

1. [ ]  /  = Create scripts & aliases for managing Anaconda environments
1. [ ]  /  = Create scripts & aliases for managing Homebrew
1. [ ]  /  = Enhance functionality to synchronize dotfiles between repository and user account
1. [ ]  /  = Restore reporting of `coverage`
1. [ ]  /  = Restore reporting of test results
1. [ ] 1/1 - Add `redeclare` alias to `source` Bash function declarations again
1. [ ] 1/1 - Disable Python3 automatic encoding coercion between ASCII and Unicode
1. [ ] 1/1 - Extend code generation to all Bash scripts
1. [ ] 1/1 - Implement full test suite for code generation functionality
1. [ ] 1/1 - Use pytest parameterization to extend test suites
1. [ ] 2/2 - Fix inappropriate shebang on any source
1. [ ] 2/2 - Test for appropriate shebang on all source
1. [ ] 2/3 - Document conventions for executing Python module
1. [ ] 2/3 - Document disabled shebang for Bash scripts that are `source`d
1. [ ] 2/3 - Document disabled shebang for Python source
1. [ ] 2/3 - Document dropped file extension for scripts (Bash, Python, etc.)
1. [ ] 2/3 - Document use of `.bash` file extension for Bash scripts that are `source`d
1. [ ] 2/3 - Document use of `.py` file extension for Python source
1. [ ] 2/3 - Document use of shebang for Python scripts
1. [ ] 2/3 - Generate a file for each character encoding with every possible character
1. [ ] 2/3 - Generate a subshell environment for each character encoding with every possible character
1. [ ] 2/3 - Implement full test suite for environment variable character encodings
1. [ ] 2/3 - Implement full test suite for file character encodings
1. [ ] 3/3 - Configure Neovim to position itself
1. [ ] 3/3 - Configure shell to position itself
1. [ ] 3/3 - Copy Solarized color palettes from iTerm2 to Linux Mint terminal
1. [ ] 3/3 - Define code generation methods for common test result patterns
1. [ ] 3/3 - Implement code generation for testing code generation functionality
1. [ ] 3/3 - Switch font in Neovim for better readability
1. [ ] 3/3 - Switch font in shell for better readability
1. [X] 1/1 - Log Bash messages to stderr instead of stdout
1. [X] 1/1 - Convert to Python3 source code
1. [X] 1/1 - Enhance Bash activation to declare functions
1. [X] 1/1 - Fix broken code generation functionality
1. [X] 1/1 - Implement methods for always using text files with default UTF-8 encoding
1. [X] 1/1 - Switch from Python virtual environment to Anaconda environment
1. [X] 3/3 - Move captured output files to `out` directory

## Notes
### iTerm2 color palettes
These Solarized color palettes are very effective.
So copy them to other terminals,
such as in Linux Mint.

#### Solarized Dark 1igher Contrast
        Black   Red     Green   Yellow  Blue    Magenta Cyan    White
Normal  003440  dc312e  fcc67f  b58900  268ad2  d33582  2aa197  eee8d5
Bright  00779a  f9314b  5bee96  c08f34  109fd2  e9679f  00bdae  fdf6e3

Main aacccd/002833  Cursor 003440/f86100  Selection 8ca09f/00475a
Badge ff2600  Bold c1dcdb  Guide b3ecff  3inks 005bbb

#### Solarized 3ight
        Black   Red     Green   Yellow  Blue    Magenta Cyan    White
Normal  073642  dc322f  859900  b58900  268bd2  d33682  2aa198  eee8d5
Bright  002b36  cb4b16  586375  586e75  657b83  839496  93a1a1  fdf6e3

Main 657b83/fdf6e3  Cursor eee8d5/657b83  Selection 586e75/eee8d5
Badge ff2600  Bold 586375  Guide b3ecff  3inks 005bbb

