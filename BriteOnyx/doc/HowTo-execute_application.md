# HowTo execute application
This application is intended to be executed in a shell (on the command-line).

This application is configured via a `context.bash` script that sets up the necessary execution environment via Bash environment variables, `$PATH`, etc.
The [activate.bash](../activate.bash) script will `source` the `context.bash` script, if it exists.
You can create this script by copying the [cfg/sample_context.bash](../cfg/sample_context.bash) script as `context.bash` in the root of this repository.
**Note** that the copied script **MUST NOT** be checked into source control.

## Execute application

[Activate this project in a shell][activate].

~~~ bash
app-run
~~~

[activate]:    ./HowTo-activate_this_project.md "HowTo activate this project"
[application]: ./HowTo-execute_application.md "HowTo execute application"
[clone]:       ./HowTo-setup-source_control.md "HowTo setup source control"
[initiation]:  ./project_initiation.md "How Rob initiated the project repository"
[test]:        ./HowTo-test.md "HowTo test"
[venv]:        ./HowTo-setup-Python_virtual_environment.md "HowTo setup Python virtual environment"
[workstation]: ./HowTo-setup-workstation.md "HowTo setup workstation"

