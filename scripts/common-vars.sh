#! /bin/bash

# common environment variables used in all scripts
export WKSP_ROOT='/scratch'
export INSTALLDIR="$WKSP_ROOT/python-installs"
export VENVDIR="$WKSP_ROOT/python-venvs"

export PATH="$INSTALLDIR/bin:$PATH"
export LD_LIBRARY_PATH="$INSTALLDIR/lib:$LD_LIBRARY_PATH"

# The minimum Ansible distribution public release that we intend to support our modules with.
export MIN_ANSIBLE_RELEASE_SUPPORTED="2.5.4"
# The latest public release of Ansible that we want to test with and verify.
export LATEST_ANSIBLE_RELEASE="2.8"

export MIN_OCI_PYTHON_SDK_RELEASE_SUPPORTED="2.2.21"

function print_env_lite {
  # print env details
  python --version
  pip --version
  tox --version
  pytest --version
}

