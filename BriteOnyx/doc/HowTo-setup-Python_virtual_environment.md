# HowTo setup Python virtual environment
We are using
dependencies documented in [cfg/requirements.txt](../cfg/requirements.txt)
and tools documented in [cfg/tool.out](../cfg/tool.out).

## Recreate Python virtual environment
This is needed the first time you build a working copy of this project,
then only rarely for troubleshooting later.

[Activate this project][activate].

~~~ bash
pve-recreate
~~~

## Rebuild Python virtual environment
If you need to rebuild the Python virtual environment at a more fundamental level, then do this.
**NOTE**: It is wise to do this every once in a while
just to be sure that it is up-to-date and completely accurate.
For example, the dependencies were incomplete the first time that I wrote and executed these scripts.

[Activate this project][activate].

~~~ bash
pve-rebuild
dep-check
~~~

## Upgrade Python virtual environment (periodically)
This procedure attempts to upgrade all the Python dependencies, if possible.
Note that this can be very disruptive, so one should allow space and time for the process.
In particular, one should take steps to prepare to undo the attempt.

[Activate this project][activate].

~~~ bash
dep-upgrade
# Verify that everything still works...
generate
test-run
app-run
dep-capture
~~~

## Check dependency versions
This step should output nothing if all dependencies match their expected versions.

[Activate this project][activate].

~~~ bash
dep-check
tool-check
~~~

OR

~~~ bash
all-check | less
~~~

## Capture dependency versions

[Activate this project][activate].

~~~ bash
dep-capture
tool-capture
~~~

OR

~~~ bash
all-capture
~~~

## Check paths

[Activate this project][activate].

~~~ bash
tool-check | less
~~~

[activate]:    ./HowTo-activate_this_project.md "HowTo activate this project"
[application]: ./HowTo-execute_application.md "HowTo execute application"
[clone]:       ./HowTo-setup-source_control.md "HowTo setup source control"
[initiation]:  ./project_initiation.md "How Rob initiated the project repository"
[test]:        ./HowTo-test.md "HowTo test"
[venv]:        ./HowTo-setup-Python_virtual_environment.md "HowTo setup Python virtual environment"
[workstation]: ./HowTo-setup-workstation.md "HowTo setup workstation"

