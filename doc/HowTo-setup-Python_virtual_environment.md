HowTo setup Python virtual environment
======================================
**TODO**: Upgrade to latest version of Python3

**NOTE**: But upgrading the Python version on Ubuntu gets rather involved, so
put it off unless truly necessary.

We are using
dependencies documented in [cfg/requirements.txt](../cfg/requirements.txt) and
tools documented in [cfg/tool.out](../cfg/tool.out).

Recreate the Python virtual environment
---------------------------------------
This is needed the first time you build a working copy of this project, and
then only rarely for troubleshooting later.

[Activate this project][activate].
~~~ bash
pve-recreate.bash
~~~

Rebuild the Python virtual environment
--------------------------------------
If you need to rebuild the Python virtual environment at a much more
fundamental level, then do this.  **NOTE**: It is wise to do this every once
in a while just to be sure that it is up-to-date and completely accurate.  For
example, it was incomplete the first time that I wrote it.

[Activate this project][activate].
~~~ bash
pve-rebuild.bash
dep-check.bash
~~~

Upgrade the Python virtual environment (periodically)
-----------------------------------------------------
[Activate this project][activate].
~~~ bash
dep-upgrade.bash
# Verify that everything still works...
dep-capture.bash
~~~

Check dependency versions
-------------------------
This command should output nothing if all dependencies match their expected
versions.

[Activate this project][activate].
~~~ bash
dep-check.bash
tool-check.bash
~~~
OR
~~~ bash
all-check.bash | less
~~~

Capture dependency versions
---------------------------
[Activate this project][activate].
~~~ bash
dep-capture.bash
tool-capture.bash
~~~
OR
~~~ bash
all-capture.bash
~~~

Check paths
-----------
~~~ bash
tool-check.bash | less
~~~

[activate]: ./HowTo-activate_this_project.md "HowTo activate this project"
[application]: ./HowTo-execute_application.md "HowTo execute application"
[AWS CLI]: ./HowTo-setup-AWS_CLI.md "HowTo setup AWS CLI"
[clone]: ./HowTo-setup-source_control.md "HowTo setup source control"
[deploy]: ./HowTo-deploy-server.md "HowTo deploy server"
[initiation]: ./project_initiation.md "How Rob initiated the project repository"
[install]: ./HowTo-install-packages.md "HowTo install Ubuntu packages"
[license]: ../LICENSE.md "License"
[ReadMe]: ../README.md "ReadMe"
[test]: ./HowTo-test.md "HowTo test"
[venv]: ./HowTo-setup-Python_virtual_environment.md "HowTo setup Python virtual environment"
[workstation]: ./HowTo-setup-workstation.md "HowTo setup workstation"

