HowTo setup source control
==========================
**NOTE**: Substitute your own GitHub profile name for PROFILE below.

Generate new SSH keys
---------------------
Open a BASH shell on a machine running Ubuntu Linux.

~~~ bash
ssh-keygen
# Press Enter to accept default file location of ~/.ssh
# Press Enter twice to skip the passphrase

ls ~/.ssh
~~~

Outputs at least these two new files:

    id_rsa id_rsa.pub

Add the new SSH public key file to your GitHub account.

Configure workstation to use SSH key to access GitHub
-----------------------------------------------------
**NOTE**:  Do not bother with `ssh-agent`, if your key has no passphrase.

Open a BASH shell on target machine using target user account.

~~~ bash
vim ~/.ssh/config
~~~

Add this content to the file:

    Host MeAtGitHub
        Compression yes
        HostName github.com
        IdentityFile ~/.ssh/id_rsa
        StrictHostKeyChecking yes
        User git

Save & exit vim by pressing `Escape :wq Enter`.

~~~ bash
chmod g=,o= ~/.ssh/*
ssh -T MeAtGitHub
~~~

If necessary, troubleshoot SSH issues and Git issues until it works.

Clone project repository
------------------------
**NOTE**: We use `MeAtGitHub` now as our prefix for the repo URL to trigger the
use of the settings in `~/.ssh/config` that we created above.

~~~ bash
mkdir ~/project
cd ~/project
git clone MeAtGitHub:PROFILE/REPO.git
cd REPO
~~~

Configure git for proper use
----------------------------
Open a BASH shell on target machine using target user account, then:

~~~ bash
cd ~/project/REPO
git config --list --show-origin
~~~

which outputs something like this:

    file:.git/config        core.repositoryformatversion=0
    file:.git/config        core.filemode=true
    file:.git/config        core.bare=false
    file:.git/config        core.logallrefupdates=true
    file:.git/config        remote.origin.url=MeAtGitHub:PROFILE/REPO.git
    file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
    file:.git/config        branch.master.remote=origin
    file:.git/config        branch.master.merge=refs/heads/master

Upon initial install, this should output nothing about your git user.  Let's
change that.  These commands will set your name and email address for only
this project.  If you want to set them globally for this user account on this
machine, then add the '--global' option to each command.

~~~ bash
git config user.name 'Rob Williams'
git config user.email rob@refactory.biz
~~~

You may also configure an editor for git to use:

~~~ bash
git config core.editor vim
~~~

Now, when you repeat the command above:

~~~ bash
git config --list --show-origin
~~~

you should see the new settings.

    file:.git/config        core.repositoryformatversion=0
    file:.git/config        core.filemode=true
    file:.git/config        core.bare=false
    file:.git/config        core.logallrefupdates=true
    file:.git/config        core.editor=vim
    file:.git/config        remote.origin.url=MeAtGitHub:PROFILE/REPO.git
    file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
    file:.git/config        branch.master.remote=origin
    file:.git/config        branch.master.merge=refs/heads/master
    file:.git/config        user.name=Rob Williams
    file:.git/config        user.email=rob@refactory.biz

TODO: Document how to change git remote URLs

~~~ bash
git remove -v
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
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

