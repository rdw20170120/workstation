# Activate BriteOnyx framework
BriteOnyx is Rob Williams' open-source framework
to manage a project's source directory tree
during development and testing.

This activation is focused
on working within a BASH shell,
also known as a terminal
or command-line interface (CLI).
The intent is to facilitate
the user's activities
while managing and working around
various characteristics
of BASH.
Some of the main features
of the BriteOnyx framework
include:

* Empower the user
  to safely and effectively use BASH
* Manage the project's software configuration (SCM)
* Ensure consistent execution
  under all invocation scenarios
* Elevate the user's BASH scripting
  well above BASH's low-level quirkiness

NOTE: We **MUST NOT EVER** `exit` during BriteOnyx activation!

The `activate.bash` script,
and EVERY script that it calls,
must NOT invoke `exit`!
The user that executes `source activate.bash`
must be allowed to preserve their shell.
Every effort must be made
to inform the user of problems
while continuing execution where possible.
Terminating the shell
robs the user of useful feedback and
interrupts their work,
which is unacceptable.
Instead of `exit`,
the BASH `return` statement should be invoked
to terminate execution
with an appropriate status code.

Likewise,
we must be very careful
invoking special BASH options
during BriteOnyx activation,
particularly the `set -e` option.
The user is inheriting the shell
that we are configuring,
which they will then use for the rest of their session,
each and every time
they develop, test, etc.
It would be very disruptive
for the shell to abort
on every error raised
by every part of every command that they execute.
If you are unclear about this,
then please experiment
by editing `activate.bash`
to invoke `set -x`
at the beginning of the script,
then activate new shell.
Having learned that lesson,
let's never use `set -x`
in a BASH script
intended to be `source`d
(except by the user while troubleshooting).
Similarly,
the `set -e` BASH option is problematic
because its haphazard behavior
does not deliver
on its promised usefulness.

The most effective tactic
for troubleshooting issues
with BriteOnyx activation
is to invoke `bash activate.bash`
instead of invoking `source activate.bash`.
It is also very helpful
to `export BO_Debug=defined` and
perhaps `set -o xtrace`
to visualize the execution.

NOTE: Rob Williams is now investigating
Fish--the friendly interactive shell--
as a complete replacement
for BASH.

