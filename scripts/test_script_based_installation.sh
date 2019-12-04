#! /bin/bash

set -e

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
VENV_NAME="my_oci_ansible_role_installation_test_venv-${CI_BUILD_ID}"

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

# cryptography>=2.5 does not have idna but pyopenssl of oci sdk needs idna. temporarily installing idna until the fix
pip install cryptography[idna]

pip install oci=="$OCI_VERSION"
pip install ansible=="$ANSIBLE_VERSION"

which ansible
ansible --version
pip freeze

# Clone the Ansible role directory and run the install script.

#This gitlab auth token is required to clone the `oci-ansible-role`
#repository without any additional credentials
API_TOKEN=3ywQiK1w8LczUzFjsxMa

# Get the URL of the repo to be cloned.
URL=$1
echo "URL of the repo to be cloned: $URL"

BRANCH_NAME=${CI_BUILD_TAG}_${CI_PIPELINE_ID}

git clone https://oauth2:${API_TOKEN}@${URL}
cd $2
git fetch --all --tags --prune
git checkout $BRANCH_NAME

ROLE_DIR=$(pwd)

./install.py --debug

trap cleanup EXIT

ansible-doc oci_volume > volume_documentation
# Check for one of the options of oci_volume module in the documentation to assert ansible-doc works.
if grep -q "source_details" volume_documentation;
 then
    cat volume_documentation
 else
    echo "ansible-doc failed."
    ansible-doc oci_volume
fi

cd "$CI_PROJECT_DIR"
cd ./scripts/role-release-tests-playbooks
ansible-playbook -vvv bucket-test.yml
ansible-playbook -vvv group-facts-test.yml

# Run a set of integration tests with OCI Ansible role installed using installer script.
run_set_of_integration_tests_in_venv_with_role "$3" "$4" "$5"