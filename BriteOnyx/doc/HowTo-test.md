# HowTo test
Testing is performed using the `pytest` tool.
The Python source has been organized under a parent `src` directory, and the test code has been mixed in with the production code.
For a Python library, this would be unacceptable.
But this code will never be released as a Python library.
Instead, it will be executed from source only.
Having the tests mixed in keeps everything simpler.

## Run tests

[Activate this project in a shell][activate].

~~~ bash
test-run
~~~

[activate]:    ./HowTo-activate_this_project.md "HowTo activate this project"
[application]: ./HowTo-execute_application.md "HowTo execute application"
[clone]:       ./HowTo-setup-source_control.md "HowTo setup source control"
[initiation]:  ./project_initiation.md "How Rob initiated the project repository"
[test]:        ./HowTo-test.md "HowTo test"
[venv]:        ./HowTo-setup-Python_virtual_environment.md "HowTo setup Python virtual environment"
[workstation]: ./HowTo-setup-workstation.md "HowTo setup workstation"

