# HowTo install Ubuntu packages
Ubuntu provides most of what we need
for an effective development, testing, and execution environment.
Here is how to get the last few bits specific to this project.

## Install packages
~~~bash
sudo apt-get update
sudo apt-get install git
sudo apt-get install dropbox python3-gpg
~~~

TODO: Document extended installation of Python 3.6 (default on this Ubuntu release)

## Install Neovim with Python3 support
REF: https://launchpad.net/~neovim-ppa/+archive/ubuntu/stable

Using Linux Mint 19.3 Tricia Cinnamon (Ubuntu 18.04.1 Bionic Beaver)

~~~bash
sudo add-apt-repository ppa:neovim-ppa/stable
sudo apt-get update
sudo apt-get install neovim neovim-qt neovim-runtime python3-neovim
~~~

## Install vim-plug
~~~bash
sh -c 'curl -fLo \
    "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim \
    --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
cp $BO_Project/home/Linux/.config/nvim/init.vim 
~~~

~~~bash
mkdir ~/.config/nvim
# For Linux
cp $BO_Project/home/Linux/.config/nvim/init.vim ~/.config/nvim/
# OR
# For Linux
cp $BO_Project/home/macOS/.config/nvim/init.vim ~/.config/nvim/
~~~

## Install Python3.8 with standard (not debugging) support
REF: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa

NOTE: ABORTED:  Need to research how to use Python 3.8 cleanly on Ubuntu

Using Linux Mint 19.3 Tricia Cinnamon (Ubuntu 18.04.1 Bionic Beaver)

1. Open a shell
1. Add Python PPA

~~~bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
~~~

1. Install these packages

~~~bash
sudo apt-get install libpython3.8-minimal libpython3.8-stdlib python3.8 \
  python3.8-minimal idle-python3.8 python3.8-doc python3.8-examples \
  python3.8-venv
~~~

1. Do NOT attempt to install these packages, as they collide with Python 3.6
   included with this Ubuntu release.

    python3.8-distutils
    python3.8-gdbm
    python3.8-lib2to3
    python3.8-tk

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

