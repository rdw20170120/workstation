# HowTo activate this project (directory)
This project is designed to be developed and executed in a BASH shell running on Ubuntu.
It should work on Ubuntu and derivatives.
It may be possible to adapt it to run in other shells and/or on other operating systems.

For each session during which you want to develop or use the code in this project, you MUST [activate this project in a shell][activate].
You can THEN [run the tests][test] and [execute the application][application].
It is assumed that you will use that shell throughout your session, then `exit` it when done.
The primary motivation for this approach is ensure the integrity of the development, test, deployment, and execution activities.
The EXACT same steps and commands MUST be used on the development workstation as on the Continuous Integration server as on the production server.
The configuration must be tightly controlled and replicated.
Deviations must be quickly identified and remediated.

If you also use an IDE (Integrated Development Environment), you MUST NOT allow
the IDE to circumvent or compromise the work done in the shell.  This generally
means configuring the IDE to invoke various project scripts to perform actions
against the project such as [running the tests][test] and
[executing the application][application].  An IDE tends to make it impossible
to reproduce the same configuration and conditions across multiple machines.
It makes no sense to deploy an IDE on a Continuous Integration server nor a
production server.  Therefore, an IDE is optional for work on this project, BUT
it is also our intention to NOT prevent the use of any IDE.  How a developer
edits the code is purposefully left to their discretion.  It is simply
impossible to allow any IDE to become an essential part of testing, deploying,
or executing the resulting code.

**NOTE**: A basic assumption of this approach is that a shell session that has
been activated for this project *MUST NOT* be reused for other purposes.
Therefore, we do *NOT* attempt to provide a way to deactivate the shell session
using the project environment.  This also means that we do *NOT* attempt to use
the deactivate script of the Python virtual environment (`venv`) tool.  This
approach is motivated by two primary factors:

* it is very easy to simply open another shell session for work that does not
  require activation, and
* it is practically impossible to be certain that any attempt at deactivation
  is thorough enough.

Activate this project in a shell
--------------------------------
**NOTE**: You must first have [setup your workstation][workstation].

Open a new BASH shell, then:

~~~ bash
cd PROJECT-ROOT-DIRECTORY
source activate.bash
~~~

Do work.  When finished, then

~~~ bash
exit
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

