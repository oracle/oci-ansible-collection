#! /bin/bash

set -e # fail-fast -- fail on first integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

PYVERSIONS2=( 'python2.7' )
PYVERSIONS3=( 'python3.5' 'python3.6' )

echo "Running flake8 for $CI_COMMIT_REF_NAME in $(pwd)"

function run_flake8 {
  cd "$CI_PROJECT_DIR"
  flake8 --ignore W503,W504,E402 --count ansible/lib/ansible/module_utils/oracle/*py
  flake8 --ignore W503,E402 --count ansible/lib/ansible/modules/cloud/oracle/*py
  flake8 --ignore W503,E402 --count ansible/contrib/inventory/oci*.py
}

function run_tests {
  PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}"

  echo "Running flake8 tests for $CI_COMMIT_REF_NAME in env $VENVNAME using the venv at $VENVDIR"

  cd "${VENVDIR}/${VENVNAME}"
  source bin/activate

  print_env_lite
  
  run_flake8

  deactivate
}

for PYEXEC in "${PYVERSIONS2[@]}"
do
  run_tests
done

for PYEXEC in "${PYVERSIONS3[@]}"
do
  run_tests
done
