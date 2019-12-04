#! /bin/bash

set -e

ROLE_NAME=${3}

function cleanup {
    ansible-galaxy remove ${ROLE_NAME}
    deactivate
    cd "$VENVDIR"
    rm -rf "$VENV_NAME"
}

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

PYEXEC='python2.7'
VENV_NAME="my_oci_ansible_role_test_venv-${CI_BUILD_ID}"

# create virtual env
cd "$VENVDIR"
echo "Creating virtualenv $VENV_NAME"
virtualenv -p "$(which "$PYEXEC")" "$VENV_NAME"
cd "$VENV_NAME"
source bin/activate

which python
python --version
which pip
pip --version

# run these smoke tests against the latest available oci and ansible in PyPi.
pip install oci
pip install ansible

which ansible
ansible --version
pip freeze

set +e
ansible-galaxy remove ${ROLE_NAME}
set -e

#This gitlab auth token is required to clone the `oci-ansible-role`
#repository without any additional credentials
API_TOKEN=3ywQiK1w8LczUzFjsxMa

# set the candidate tag name based on current job id and the tag in which it is running for
CANDIDATE_TAG_NAME=$2
echo "$CANDIDATE_TAG_NAME"
echo "installing $CANDIDATE_TAG_NAME of ${ROLE_NAME}"
ansible-galaxy -vvv -c install git+https://oauth2:${API_TOKEN}@${1},"$CANDIDATE_TAG_NAME"

trap cleanup EXIT

# run tests
export ANSIBLE_LIBRARY=~/.ansible/roles
export ANSIBLE_MODULE_UTILS=$ANSIBLE_LIBRARY/${ROLE_NAME}/module_utils

echo "${ROLE_NAME} version being used is:"
grep "__version__ =" $ANSIBLE_MODULE_UTILS/oracle/oci_utils.py

cd "$CI_PROJECT_DIR"
cd ./scripts/role-release-tests-playbooks
ansible-playbook -vvv bucket-test.yml
ansible-playbook -vvv group-facts-test.yml

# Run a set of integration tests with OCI Ansible role installed using Ansible Galaxy.
run_set_of_integration_tests_in_venv_with_role "$4" "$5" "$6"
