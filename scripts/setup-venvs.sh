#! /bin/bash

# Assumes the corresponding python versions have already been installed in $INSTALLDIR

# Use https://danieleriksson.net/2017/02/08/how-to-install-latest-python-on-centos/
# to install the required versions

# Creates a temporary virtual environment for every $CI_COMMIT_REF_NAME (Branch) in $VENVDIR
# corresponding to every Python version we must support,
# and installs all the development/test pip requirements, and customer requirements
# in those virtual-environments

. "$CI_PROJECT_DIR"/scripts/common-vars.sh

PYVERSIONS2=( 'python2.7' )
PYVERSIONS3=( 'python3.5' 'python3.6' )

# Variable to signal whether a new venv got created.
venv_created=0

# activates a virtualenv, installs ansible dev deps, and deactivates the venv
function install_requirements_in_current_venv {
      echo "Installing requirements in $(pwd)"
      source bin/activate
      pip install --upgrade pip
      install_ansible_dev_requirements
      deactivate
}

function install_ansible_dev_requirements {
  # install all ansible and ansible-test requirements
  cd "$CI_PROJECT_DIR/ansible"
  pip install requirements.txt

  cd test/runner/requirements
  pip install -U -r integration.cloud.oci.txt
  pip install -r units.txt -r sanity.txt -r ansible-test.txt -r integration.txt

  # install general requirements
  cd "$CI_PROJECT_DIR"
  pip install pytest-cov
  pip install tox
  pip install jinja2
  pip install -U flake8
}

# activates a virtualenv, installs minimum customer pre-reqs, and deactivates the venv
function install_customer_prereqs_in_current_venv {
    if [ "$venv_created" -eq 1 ]; then
      echo "Installing requirements in $(pwd)"
      source bin/activate
      pip install --upgrade pip
      install_customer_prereqs
      deactivate
    fi
}

# Only setup a customer's customer pre-reqs in a virtual environment to test our
# modules from a customer PoV
function install_customer_prereqs {
  # install all ansible and ansible-test requirements
  cd "$CI_PROJECT_DIR/ansible"

  # Use pip to install a particular version of our customer pre-reqs (oci and ansible)
  pip install oci=="$OCI_VERSION"
  pip install ansible=="$ANSIBLE_VERSION"

  # We can also use "pip install -I" from https://stackoverflow.com/a/5226504 to ignore
  # the current installation and reinstall a particular version ...
  # Unfortunately this increases test execution time.

  # since we run integration tests, we need integration test dependencies too
  cd test/runner/requirements
  pip install -r integration.txt
}

function create_venv_py2 {
  venv_created=0
  if [ ! -d "${VENVDIR}/${VENVNAME}" ]
  then
    echo "Creating virtual environment for $PYVER named $VENVNAME in $VENVDIR"
    cd "$VENVDIR"
    virtualenv -p "$(which "$PYEXEC")" "$VENVNAME"
    venv_created=1
  else
    echo "Virtual environment for $PYVER named $VENVNAME in $VENVDIR is already created. So skipping."
  fi

}

function create_venv_py3 {
  venv_created=0
  if [ ! -d "${VENVDIR}/${VENVNAME}" ]
  then
    echo "Creating virtual environment for $PYVER named $VENVNAME in $VENVDIR"
    cd "$VENVDIR"
    $PYEXEC -m venv "$VENVNAME"
    venv_created=1
  else
    echo "Virtual environment for $PYVER named $VENVNAME in $VENVDIR is already created. So skipping."
  fi
}


# create virtual envs for Python 2.x
for PYEXEC in "${PYVERSIONS2[@]}"
do
  PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')

  # create a virtual environment that has all dev and test dependencies installed
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}"
  create_venv_py2
  cd "${VENVDIR}/${VENVNAME}"
  install_requirements_in_current_venv

  # create a virtual environment that has only the minimum customer pre-reqs installed
  cd "$VENVDIR"
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}-release-min-customer-env"
  create_venv_py2
  cd "${VENVDIR}/${VENVNAME}"
  ANSIBLE_VERSION="$MIN_ANSIBLE_RELEASE_SUPPORTED"
  OCI_VERSION="$MIN_OCI_PYTHON_SDK_RELEASE_SUPPORTED"
  install_customer_prereqs_in_current_venv

  # create a virtual environment that has only the minimum customer pre-reqs installed
  cd "$VENVDIR"
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}-release-latest-ansible-customer-env"
  create_venv_py2
  cd "${VENVDIR}/${VENVNAME}"
  ANSIBLE_VERSION="$LATEST_ANSIBLE_RELEASE"
  OCI_VERSION="$MIN_OCI_PYTHON_SDK_RELEASE_SUPPORTED"
  install_customer_prereqs_in_current_venv
done

# create virtual envs for Python 3.x
for PYEXEC in "${PYVERSIONS3[@]}"
do
  PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}"
  create_venv_py3
  cd "${VENVDIR}/${VENVNAME}"
  install_requirements_in_current_venv

  # create a virtual environment that has only the minimum customer pre-reqs installed
  cd "$VENVDIR"
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}-release-min-customer-env"
  create_venv_py3
  cd "${VENVDIR}/${VENVNAME}"
  ANSIBLE_VERSION="$MIN_ANSIBLE_RELEASE_SUPPORTED"
  OCI_VERSION="$MIN_OCI_PYTHON_SDK_RELEASE_SUPPORTED"
  install_customer_prereqs_in_current_venv

  # create a virtual environment that has recent ansible as a customer pre-req installed
  cd "$VENVDIR"
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}-release-latest-ansible-customer-env"
  create_venv_py3
  cd "${VENVDIR}/${VENVNAME}"
  ANSIBLE_VERSION="$LATEST_ANSIBLE_RELEASE"
  OCI_VERSION="$MIN_OCI_PYTHON_SDK_RELEASE_SUPPORTED"
  install_customer_prereqs_in_current_venv
done
