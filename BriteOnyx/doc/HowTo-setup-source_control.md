# HowTo setup source control
Here is how to setup source control for this and other GitHub projects.
Use your own GitHub PROFILE name and REPO name below as appropriate.

## Generate a new SSH key
**NOTE**:  Do not bother with `ssh-agent`, if your new key has no passphrase.

Open a Bash shell as the target user account on a machine running Ubuntu Linux.

~~~ bash
ssh-keygen
# Press Enter to accept default file location of ~/.ssh
# Press Enter twice to skip the passphrase

ls ~/.ssh
~~~

   which outputs these two new files:

        id_rsa id_rsa.pub

Add the new SSH public key file (`id_rsa.pub`) to your GitHub account.

## Configure SSH connection to GitHub & GitLab

Create (or edit) your SSH configuration file.

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

        Host MeAtGitLab
            Compression yes
            HostName gitlab.com
            IdentityFile ~/.ssh/id_rsa
            StrictHostKeyChecking yes
            User git

Save & exit vim by pressing `Escape :wq Enter`.
Protect the new SSH files.

~~~ bash
chmod g=,o= ~/.ssh/*
~~~

Test and allow the new SSH connection to GitHub.

~~~ bash
ssh -T git@github.com
# Type 'yes' and hit 'Enter' to accept the authenticity of the GitHub host machine.
ssh -T MeAtGitHub
~~~

If necessary, troubleshoot SSH issues and Git issues until it works.

Test and allow the new SSH connection to GitLab.

~~~ bash
ssh -T git@gitlab.com
# Type 'yes' and hit 'Enter' to accept the authenticity of the GitLab host machine.
ssh -T MeAtGitLab
~~~

If necessary, troubleshoot SSH issues and Git issues until it works.

## Clone project repository
**NOTE**: We use `MeAtGitHub` now as our prefix for the repo URL to trigger the
use of the settings in `~/.ssh/config` that we created above.

Open a Bash shell.

~~~ bash
mkdir ~/project
cd ~/project
git clone MeAtGitHub:PROFILE/REPO.git
cd REPO
~~~

## Configure Git user local settings

View git configuration.

~~~ bash
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

   Upon initial install, this should output nothing about your GitHub user.

Let's change that.
   These commands will set
   your name and email address.
   If you do not want
   to set these globally
   for this user account on this machine,
   then drop the `--global` option
   on each command.

~~~ bash
git config --global user.name 'Rob Williams'
git/config --global user.email rdw6688@gmail.com
~~~

Let's also set our default `git pull` behavior:

~~~ bash
git config --global pull.ff only
~~~

You may also configure an editor for git to use:

~~~ bash
git config --global core.editor vim
~~~

Now, when you repeat the command above:

~~~ bash
git config --list --show-origin
~~~

   you should see the new settings.

        file:.git/config        core.editor=vim
        file:.git/config        user.name=Rob Williams
        file:.git/config        user.email=rdw6688@gmail.com

[activate]:    ./HowTo-activate_this_project.md "HowTo activate this project"
[application]: ./HowTo-execute_application.md "HowTo execute application"
[clone]:       ./HowTo-setup-source_control.md "HowTo setup source control"
[initiation]:  ./project_initiation.md "How Rob initiated the project repository"
[test]:        ./HowTo-test.md "HowTo test"
[venv]:        ./HowTo-setup-Python_virtual_environment.md "HowTo setup Python virtual environment"
[workstation]: ./HowTo-setup-workstation.md "HowTo setup workstation"

