HowTo use Anaconda

REF: https://pythonspeed.com/articles/conda-vs-pip/
REF: https://pythonspeed.com/articles/faster-conda-install/
REF: https://github.com/conda-forge/miniforge

# How I use Anaconda
- I do not like Homebrew,
  but I have yet to find something
  that I like better and that is tractable
- use Homebrew to install tools strictly for the user,
  but not required by any project:
  e.g., developers favorite terminal, editor, etc.
- use Homebrew to install Anaconda
- use Mamba, so use Homebrew to install Mambaforge
- leave the `base` Anaconda environment empty
- do NOT activate Anaconda/Mamba except
  within a specific project repository
- create an Anaconda environment as a subdirectory within the project repository
- configure each project repository with scripts to populate the Anaconda environment
- write scripts & aliases to manage the Anaconda environment
- do NOT manipulate Homebrew from within a project repository
  (leave it to the user & workstation)
- do we need to make the project aware of the Anaconda/Mamba versions?!?!
- can we install tools like Terraform/Terragrunt from within Anaconda?
- do NOT recreate the Anaconda environment during project activation, unless it does not exist
- therefore, do NOT `conda init` or `mamba init` for the user account
  - do NOT modify ~/.bash_profile
  - do NOT modify ~/.bashrc
  - instead, integrate `conda init` and `mamba init` RESULTS
    into a script
    to configure Anaconda/Mamba
    in each project repository

# Install Mambaforge
brew install mambaforge
conda init "$(basename "${SHELL}")"
mamba init
conda --version
mamba --version
mamba update conda mamba
python --version

# Managing Conda environments
# NOTE: Edit `create_default_packages` section of `.condarc`
# NOTE:  It is best to install packages all together
# so that dependency management can work against the entire set,
# rather than one-by-one.
conda activate
conda activate ENV
conda create --name ENV
conda create --name ENV python=3.10
conda create --prefix DIR 
conda info --envs
conda remove --name ENV --all

# Create an environment from a YAML file (name is on the first line)
conda env create --file environment.yml
conda activate ENV
conda env list
conda env update --file environment.yml -prune
conda list --explicit >FILE
conda list --show-channel-urls
conda env export --from-history

# Managing Conda packages
mamba search PACKAGE
mamba install PACKAGE
mamba list

# Conda configuration
conda config
conda config --get
conda config --show-sources

# Bash tab completion
mamba install argcomplete
# Add to Bash profile
eval "$(register-python-argcomplete conda)"

# Using PIP
# Avoid running pip in the root environment
# Always use an environment
# Install as much as possible using conda
# Use pip only after conda
# Use pip with --upgrade-strategy only-if-needed (default)
# Do NOT use pip --user
# conda will be unaware of changes made by pip
# In order to alter conda packages, rebuild the environment

# Configure for Python packages only hosted on PyPI
# Consider conda-lock for version pinning
# Consider Jake for security scanning

