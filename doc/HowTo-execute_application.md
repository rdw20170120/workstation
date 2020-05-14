HowTo execute the application
=============================
This application is intended to be executed in a shell (on the command-line).
It will likely be deployed to execute under a `cron` job, or perhaps even
turned into a service.

This application relies upon the [AWS CLI][AWS CLI] tool to manage a
configuration for accessing the Amazon cloud.  We create an AWS CLI profile for
the application.

The profile name must be provided to the application, which is accomplished
during [activation][activate].  The [activate.src](../activate.src) script will
`source` the `context.src` script, if it exists.  You can create this script by
copying the [cfg/sample_context.src](../cfg/sample_context.src) script.
**Note** that the copied script MUST NOT be checked into source control.

Execute this application
------------------------
[Activate this project in a shell][activate].
~~~ bash
app-run.bash
~~~

[activate]: ./HowTo-activate_this_project.md "HowTo activate this project"
[application]: ./HowTo-execute_application.md "HowTo execute application"
[AWS CLI]: ./HowTo-setup-AWS_CLI.md "HowTo setup AWS CLI"
[clone]: ./HowTo-setup-source_control.md "HowTo setup source control"
[initiation]: ./project_initiation.md "How Rob initiated the project repository"
[install]: ./HowTo-install-packages.md "HowTo install Ubuntu packages"
[license]: ../LICENSE.md "License"
[ReadMe]: ../README.md "ReadMe"
[test]: ./HowTo-test.md "HowTo test"
[venv]: ./HowTo-setup-Python_virtual_environment.md "HowTo setup Python virtual environment"
[workstation]: ./HowTo-setup-workstation.md "HowTo setup workstation"

