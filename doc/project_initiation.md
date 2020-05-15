Notes on project initiation
===========================
These notes describe how Rob first initiated this project by preparing his
development workstation and creating this source directory tree.
Rob based his approach on his pre-existing open-source project BriteOnyx, which
is likewise based on his many years of technical experience.

Install tools
-------------
* Using Apple MacBook Pro
* Running Apple macOS Mojave 10.14.6

1. Install VMware Fusion 8.5.10.7527438
1. Create Linux VM
1. Install Linux Mint 19.3 Tricia Cinnamon amd64 20191213
1. Use Software Manager to install:
    * `git`           Source control
    * `meld`          Visual directory & file comparison
    * `python3-venv`  Update Python3 with `venv` (virtual environment)
    * `vim`           Enhanced text editing

Prepare project directory
-------------------------
1. [Setup source control including cloning the repository][clone].
1. Copy in various files from Rob's previous BriteOnyx project

Create a project-specific Python virtual environment
----------------------------------------------------
[Activate this project in a shell][activate].

~~~ bash
pve-create
source $PVE/bin/activate
pip3 install wheel
dep-capture
tool-capture
exit
~~~

Create [activate](../activate) to source `$PVE/bin/activate`.

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

