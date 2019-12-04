#! /bin/bash

set -e # fail-fast -- fail on first unit-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh

PYVERSIONS2=( 'python2.7' )
PYVERSIONS3=( 'python3.5' 'python3.6' )

echo "Running unit tests for $CI_COMMIT_REF_NAME in $(pwd)"

function run_unit_tests {
  pytest -r a --cov=. --cov-report=html --cov-report term --fulltrace --color yes ansible/test/units/modules/cloud/oracle ansible/test/units/module_utils/oracle/ -vvv
  return $?
}

function run_tests {
  PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}"
  echo "Running units tests for $CI_COMMIT_REF_NAME in env $VENVNAME using the venv at $VENVDIR"
  cd "${VENVDIR}/${VENVNAME}"
  source bin/activate
  cd -

  # print env
  python --version
  pip --version
  tox --version
  pytest --version

  # setup dev environment to run unit tests
  cd ansible; source hacking/env-setup
  ansible --version
  cd ..

  run_unit_tests
  #preserve exit code of run_unit_tests, but deactivate first
  eval "deactivate; exit $?"
}

for PYEXEC in "${PYVERSIONS2[@]}"
do
  run_tests
done

for PYEXEC in "${PYVERSIONS3[@]}"
do
  run_tests
done
