# HowTo execute the application
This application is intended to be executed in a shell (on the command-line).

This application is configured via a `context.bash` script that sets up the necessary execution environment via BASH environment variables, `$PATH`, etc.
The [activate](../activate.bash) script will `source` the `context.bash` script, if it exists.
You can create this script by copying the [sample/context.bash](../sample/context.bash) script as `context.bash` in the root of this repository.
**Note** that the copied script MUST NOT be checked into source control.

## Execute this application
[Activate this project in a shell][activate].

~~~ bash
app-run
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

