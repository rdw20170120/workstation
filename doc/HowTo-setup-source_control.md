HowTo setup source control
==========================
REF: https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html

**NOTE**: Substititue your own BitBucket profile name for PROFILE below.

Generate new SSH keys
---------------------
**NOTE**: You do not need to do this if you already have a BitBucket SSH key.

Open a BASH shell on a machine running Ubuntu Linux.

~~~ bash
ssh-keygen
# Press Enter to accept default file location of ~/.ssh
# Press Enter twice to skip the passphrase

ls ~/.ssh
~~~

Outputs at least these two new files:

    id_rsa id_rsa.pub

Let's rename those files so that their purpose is clear.

~~~ bash
mv ~/.ssh/id_rsa     ~/.ssh/BitBucket-PROFILE-private.key
mv ~/.ssh/id_rsa.pub ~/.ssh/BitBucket-PROFILE-public.key
~~~

Save the key files to a personal, private storage location.

Add the new SSH public key file to your BitBucket account.

Configure workstation to use SSH key to access BitBucket
--------------------------------------------------------
**NOTE**:  Do not bother with `ssh-agent`, if your key has no passphrase.

Open a BASH shell on target machine using target user account.

Copy private BitBucket SSH key file into `~/.ssh`.

~~~ bash
vim ~/.ssh/config
~~~

Add this content to the file:

    Host bb-git
        Compression yes
        HostName bitbucket.org
        IdentityFile ~/.ssh/BitBucket-PROFILE-private.key
        StrictHostKeyChecking no
        User git

Save & exit vim by pressing 'Escape :wq Enter'.

~~~ bash
chmod g=,o= ~/.ssh/*
ssh -T bb-git
~~~

If necessary, troubleshoot SSH issues and Git issues until it works.

Clone project repository
------------------------
**NOTE**: We use `bb-git` now as our prefix for the repo URL to trigger the use of the settings
in `~/.ssh/config` that we created above.

~~~ bash
mkdir ~/project
cd ~/project
git clone bb-git:potrero/potrero-cloud-lab.git
cd potrero-cloud-lab
~~~

Configure git for proper use
----------------------------
Open a BASH shell on target machine using target user account, then:

~~~ bash
cd ~/project/potrero-cloud-lab
git config --list --show-origin
~~~

which outputs something like this:

    file:.git/config        core.repositoryformatversion=0
    file:.git/config        core.filemode=true
    file:.git/config        core.bare=false
    file:.git/config        core.logallrefupdates=true
    file:.git/config        remote.origin.url=bb-git:potrero/potrero-cloud-lab.git
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
    file:.git/config        remote.origin.url=bb-git:potrero/potrero-cloud-lab.git
    file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
    file:.git/config        branch.master.remote=origin
    file:.git/config        branch.master.merge=refs/heads/master
    file:.git/config        user.name=Rob Williams
    file:.git/config        user.email=rob@refactory.biz

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

