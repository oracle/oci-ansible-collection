#! /bin/bash

# Runs the Integration tests in a virtual environment that only has the
# minimum customer requirements (ie min supported ansible and OCI python SDK)
# This test simulates the usecase scenario where our customers use our modules.

set -e # fail-fast -- fail on first integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

PYVER='3.5'

echo "Running SDK fidelity checks (in minimum customer prereqs) for $CI_COMMIT_REF_NAME in $(pwd)"

VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}-release-min-customer-env"
cd "${VENVDIR}/${VENVNAME}"
pwd
source bin/activate
cd -

which pip
which python
python --version
pip --version

python -c "import oci;print('oci sdk version: %s' % (oci.__version__))"
python -c "import ansible; print('ansible version: %s' % (ansible.__version__))"
pip install -r "$CI_PROJECT_DIR"/scripts/check_sdk_fidelity_requirements.txt

cd "$CI_PROJECT_DIR"/ansible; source hacking/env-setup
ansible --version
cd "$CI_PROJECT_DIR"

python -u "$CI_PROJECT_DIR"/scripts/check_sdk_fidelity.py | tee sdk-fidelity-check-report.md
