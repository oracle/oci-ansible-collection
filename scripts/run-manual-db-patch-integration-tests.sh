#! /bin/bash

set -e # fail-fast -- fail on first lengthy-integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh

PYVERSIONS2=( 'python2.7' )

echo "Running manual-integration tests for $CI_COMMIT_REF_NAME in $(pwd)"

function run_lengthy_integration_tests {
  for i in $(find ansible/test/integration/targets/ -type d -name oci* | grep oci_db_patch-manual)
    do ./ansible/test/runner/ansible-test integration -v $(basename $i)
  done
  return $?
}

function run_tests {
  PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}"
  echo "Running lengthy integration tests for $CI_COMMIT_REF_NAME in env $VENVNAME using the venv at $VENVDIR"
  cd "${VENVDIR}/${VENVNAME}"
  source bin/activate
  cd -

  # print env
  python --version
  pip --version
  tox --version
  pytest --version

  pip install -r ./ansible/test/runner/requirements/integration.cloud.oci.txt

  run_lengthy_integration_tests
  #preserve exit code of run_lengthy_integration_tests, but deactivate first
  eval "deactivate; exit $?"
}

for PYEXEC in "${PYVERSIONS2[@]}"
do
  run_tests
done
