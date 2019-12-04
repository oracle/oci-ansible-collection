#! /bin/bash

# Smoke tests for new roles. Runs a couple of playbooks using the role
# to test whether it works
set -e

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

PYEXEC='python2.7'
VENV_NAME="my_oci_ansible_role_smoke_test_venv-${CI_COMMIT_REF_NAME}"

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
ansible-galaxy remove oci-ansible-role
set -e

# install ansible role

#This gitlab auth token is required to clone the `oci-ansible-role`
#repository without any additional credentials
API_TOKEN=3ywQiK1w8LczUzFjsxMa

# set the candidate tag name based on current job id and the tag in which it is running for
CANDIDATE_TAG_NAME="${CI_COMMIT_TAG}_${CI_PIPELINE_ID}_candidate"
echo "$CANDIDATE_TAG_NAME"
echo "installing $CANDIDATE_TAG_NAME of oci-ansible-role"
ansible-galaxy -vvv -c install git+https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/oci-ansible-role.git,"$CANDIDATE_TAG_NAME"

# run tests
export ANSIBLE_LIBRARY=~/.ansible/roles
export ANSIBLE_MODULE_UTILS=$ANSIBLE_LIBRARY/oci-ansible-role/library

echo "oci-ansible-role version being used is:"
grep "__version__ =" $ANSIBLE_MODULE_UTILS/oci_utils.py

cd "$CI_PROJECT_DIR"
cd ./scripts/role-release-tests-playbooks
ansible-playbook bucket-test.yml
ansible-playbook group-facts-test.yml

run_all_integration_tests_in_venv_with_role

# cleanup
ansible-galaxy remove oci-ansible-role
deactivate

cd "$VENVDIR"
rm -rf "$VENV_NAME"
