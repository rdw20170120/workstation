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
1. [ ]  /  = 

1. [ ] 1/1 = Refactor hard-coded values into configuration
1. [ ] 1/1 = Rename application module `MODULE` to follow PEP8 conventions
1. [ ] 1/1 = Split generation of `activate.bash` into separate Python modules for before/after activation
1. [ ] 2/2 - Disable Python3 automatic encoding coercion between ASCII and Unicode
1. [ ] 2/2 - Extend code generation to all Bash scripts
1. [ ] 2/2 = Create scripts & aliases for showing environment variables for Anaconda
1. [ ] 2/2 = Create scripts & aliases for showing environment variables for BriteOnyx
1. [ ] 2/2 = Document use of Anaconda for our purposes
1. [ ] 2/2 = Filter sensitive values out of committed output (environment variables)
1. [ ] 2/2 = Integrate OpenTelemetry into Python code
1. [ ] 2/3 - Document conventions for executing Python module
1. [ ] 2/3 - Document disabled shebang for Bash scripts that are `source`d
1. [ ] 2/3 - Document disabled shebang for Python source
1. [ ] 2/3 - Document dropped file extension for scripts (Bash, Python, etc.)
1. [ ] 2/3 - Document use of `.bash` file extension for Bash scripts that are `source`d
1. [ ] 2/3 - Document use of `.py` file extension for Python source
1. [ ] 2/3 - Document use of shebang for Python scripts
1. [ ] 2/3 - Generate a file for each character encoding with every possible character
1. [ ] 2/3 - Generate a subshell environment for each character encoding with every possible character
1. [ ] 2/3 - Implement full test suite for code generation functionality
1. [ ] 2/3 - Implement full test suite for environment variable character encodings
1. [ ] 2/3 - Implement full test suite for file character encodings
1. [ ] 2/3 = Sort Anaconda packages in `cfg/anaconda.yml`
1. [ ] 3/3 - Configure Neovim to position itself
1. [ ] 3/3 - Configure shell to position itself
1. [ ] 3/3 - Copy Solarized color palettes from iTerm2 to Linux Mint terminal
1. [ ] 3/3 - Define code generation methods for common test result patterns
1. [ ] 3/3 - Fix inappropriate shebang on any source
1. [ ] 3/3 - Implement code generation for testing code generation functionality
1. [ ] 3/3 - Switch font in Neovim for better readability
1. [ ] 3/3 - Switch font in shell for better readability
1. [ ] 3/3 - Test for appropriate shebang on all source
1. [ ] 3/3 - Use pytest parameterization to extend test suites
1. [ ] 3/3 = Add encoding header to all Python source
1. [ ] 3/3 = Create scripts & aliases for showing environment variables for Python
1. [ ] 3/3 = Enhance functionality to synchronize dotfiles between repository and user account
1. [ ] 3/3 = Investigate whether I want to capture log files during `test-run`
1. [ ] 3/3 = `unset` relevant Bash variables when appropriate
1. [X] 1/1 - Add `redeclare` alias to `source` Bash function declarations again
1. [X] 1/1 - Convert to Python3 source code
1. [X] 1/1 - Enhance Bash activation to declare functions
1. [X] 1/1 - Fix broken code generation functionality
1. [X] 1/1 - Implement methods for always using text files with default UTF-8 encoding
1. [X] 1/1 - Log Bash messages to stderr instead of stdout
1. [X] 1/1 - Switch from Python virtual environment to Anaconda environment
1. [X] 1/1 = Create scripts & aliases for managing Anaconda environments
1. [X] 1/1 = Create scripts & aliases for managing Homebrew
1. [X] 1/1 = Refactor BriteOnyx source generation to better distinguish before, during, and after activation
1. [X] 1/1 = Restore reporting of `coverage`
1. [X] 1/1 = Restore reporting of test results
1. [X] 1/1 = Separate project temporary directory from `TMPDIR`
1. [X] 3/3 - Move captured output files to `out` directory

