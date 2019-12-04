#! /bin/bash

function cleanup {
  cd "$ROLE_DIR"
  ./uninstall.py --debug
  deactivate
  cd "$VENVDIR"
  rm -rf "$VENV_NAME"
}

. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh
. "$CI_PROJECT_DIR"/scripts/common-vars.sh

PYEXEC='python2.7'
VENV_NAME="my_oci_ansible_role_installation_test_venv-${CI_COMMIT_REF_NAME}"

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

pip install oci
pip install ansible

which ansible
ansible --version
pip freeze

# Clone the Ansible role directory and run the install script.

#This gitlab auth token is required to clone the `oci-ansible-role`
#repository without any additional credentials
API_TOKEN=3ywQiK1w8LczUzFjsxMa

# set the candidate tag name based on current job id and the tag in which it is running for
CANDIDATE_TAG_NAME="${CI_COMMIT_TAG}_${CI_PIPELINE_ID}_candidate"
echo "$CANDIDATE_TAG_NAME"

#echo "Cloning $CANDIDATE_TAG_NAME of oci-ansible-role"
git clone https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/oci-ansible-role.git
cd oci-ansible-role
pwd
git fetch --all --tags --prune
git checkout "tags/$CANDIDATE_TAG_NAME" -b "branch-$CANDIDATE_TAG_NAME"

ROLE_DIR=$(pwd)

./install.py --debug
# just to make sure that duplicate install works
./install.py --debug

cd "$CI_PROJECT_DIR"
cd ./scripts/role-release-tests-playbooks
ansible-playbook -vvv bucket-test.yml
ansible-playbook -vvv group-facts-test.yml

# Run all integration tests with OCI Ansible role installed using installer script.
run_all_integration_tests_in_venv_with_role

cd "$ROLE_DIR"
ansible-doc oci_volume > volume_documentation
# Check for one of the options of oci_volume module in the documentation to assert ansible-doc works.
if grep -q "source_details" volume_documentation;
 then
    cat volume_documentation
 else
    echo "ansible-doc failed."
    ansible-doc oci_volume
    cleanup
    exit 1
fi
cleanup