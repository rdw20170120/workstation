# Notes on project initiation
These notes describe how Rob first initiated this project by preparing his development workstation and creating this source directory tree.
Rob based his approach on his pre-existing open-source project BriteOnyx, which is likewise based on his many years of technical experience.

## Install tools
* Using Apple MacBook Pro (Retina, 15-inch, Late 2013)
    * Processor: 2.3 GHz Intel Core i7
    * Memory:    16 GB 1600 MHz DDR3
    * Graphics:  NVIDIA GeForce GT 750M 2 GB & Intel Iris Pro 1536 MB
* Running Apple macOS 10.14.6 Mojave

1. Install VMware Fusion 8.5.10.7527438
1. Create Linux VM
1. Install Linux Mint 19.3 Tricia Cinnamon amd64 20191213
1. Use Software Manager to install:
    * `git`           Source control
    * `meld`          Visual directory & file comparison
    * `python3-venv`  Update Python3 with `venv` (virtual environment)
    * `vim`           Enhanced text editing

## Prepare project directory
1. [Setup source control including cloning the repository][clone].
1. Copy in various files from Rob's previous BriteOnyx project

## Create a project-specific Python virtual environment
[Activate this project in a shell][activate].

~~~ bash
pve-create
source $PVE/bin/activate
pip3 install wheel
dep-capture
tool-capture
exit
~~~

Create [activate.bash](../activate.bash) to source `$PVE/bin/activate`.

TODO: Add link references

