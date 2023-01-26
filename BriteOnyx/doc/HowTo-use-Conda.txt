HowTo use Anaconda
by Rob Williams

REF: https://pythonspeed.com/articles/conda-vs-pip/
REF: https://pythonspeed.com/articles/faster-conda-install/
REF: https://github.com/conda-forge/miniforge

# Install Mambaforge
brew install mambaforge

conda init "$(basename "${SHELL}")"
mamba init

# TODO: Reconfigure ~/.bash_profile & ~/.bashrc to integrate Conda configuration

# Configure for Python packages only hosted on PyPI
# Consider conda-lock for version pinning
# Consider Jake for security scanning

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
conda env export --from-history

# Using PIP
# Avoid running pip in the root environment
# Always use an environment
# Install as much as possible using conda
# Use pip only after conda
# Use pip with --upgrade-strategy only-if-needed (default)
# Do NOT use pip --user
# conda will be unaware of changes made by pip
# In order to alter conda packages, rebuild the environment

# Managing Conda packages
mamba search PACKAGE
mamba install PACKAGE
mamba list

# Conda configuration
conda config
conda config --get

# Bash tab completion
mamba install argcomplete
# Add to Bash profile
eval "$(register-python-argcomplete conda)"

