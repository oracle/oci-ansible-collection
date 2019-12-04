#! /bin/bash

# This script accepts two parameters. First parameter represents list of paths of all the targets and the second
# parameter is a number representing the set number of the job calling the script.

set -e # fail-fast -- fail on first integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

# for now only run against python 2.7
PYVERSIONS2=( 'python2.7' )

echo "Running integration tests for $CI_COMMIT_REF_NAME in $(pwd)"

function run_tests {
  PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}"
  
  echo "Running integration tests for $CI_COMMIT_REF_NAME in env $VENVNAME using the venv at $VENVDIR"
  
  cd "${VENVDIR}/${VENVNAME}"
  source bin/activate

  cd "$CI_PROJECT_DIR"
  print_env_lite
  
  pip install -r ./ansible/test/runner/requirements/integration.cloud.oci.txt

  run_set_of_integration_tests_in_venv "$1" "$2" "$3"

  #preserve exit code of run_integration_tests, but deactivate first
  eval "deactivate; exit $?"
}

echo "Parameters: $1"
echo "Parameters: $2"
echo "Parameters: $3"

for PYEXEC in "${PYVERSIONS2[@]}"
do
  run_tests "$1" "$2" "$3"
done
