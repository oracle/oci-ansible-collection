#! /bin/bash

# Runs the Integration tests in a virtual environment that has the recent release
# of ansible installed and the minimum OCI python SDK

# This test simulates the usecase scenario where our customers has a recent release of
# ansible

set -e # fail-fast -- fail on first integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

# For now run, only in Python 2.7
# XXX later expand this to run base minimum 3.5 and 3.6 python versions as well
PYVERSIONS2=( '2.7' )

echo "Running integration test targets (with recent release of ansible) for $CI_COMMIT_REF_NAME in $(pwd)"

# set the candidate tag name based on current job id and the tag in which it is running for
CANDIDATE_TAG_NAME="${CI_COMMIT_TAG}_${CI_PIPELINE_ID}_candidate"
echo "Candidate tag name: $CANDIDATE_TAG_NAME"

for PYVER in "${PYVERSIONS2[@]}"
do
  VENVNAME="my-${PYVER}-venv-${CI_COMMIT_REF_NAME}-release-latest-ansible-customer-env"
  run_it_tests_in_venv_using_oci_ansible_role "$VENVNAME"
done
