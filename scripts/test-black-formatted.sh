#! /bin/bash

# Tests if all the python files have been formatted by Black

set -e # fail-fast -- fail on first integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

echo "Running flake8 for $CI_COMMIT_REF_NAME in $(pwd)"

# Black requires python 3.6, so use the Python 3.6 venv
VENVNAME="my-3.6-venv-${CI_COMMIT_REF_NAME}"

cd "${VENVDIR}/${VENVNAME}"
source bin/activate

print_env_lite

pip install black
black --version

cd "$CI_PROJECT_DIR"
black -v --check .
