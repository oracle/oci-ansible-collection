#! /bin/bash

# Common functions related to running IT tests

set -e # fail-fast -- fail on first integration-test suite failure

. "$CI_PROJECT_DIR"/scripts/common-vars.sh

function print_env {
  # debug: print environment details
  pwd
  python --version
  pip --version
  tox --version
  pytest --version

  python -c "import oci;print('oci sdk version: %s' % (oci.__version__))"
  python -c "import ansible; print('ansible version: %s' % (ansible.__version__))"

  ansible-playbook --version
  ansible-galaxy --version
  # print ansible version being used in the tests
  ansible localhost -m debug -a "msg={{ansible_version}}"
}

first_index=0
last_index=0

function set_first_and_last_index {
    oci_targets=$1
    set_no="$2"
    total_target_sets=$3
    echo "All targets: ${oci_targets[@]}"

    total_targets=${#oci_targets[@]}
    echo "Total number of targets: $total_targets"

    no_of_targets_in_each_set=$(( $total_targets / $total_target_sets ))
    echo "Least number of targets in each set: $no_of_targets_in_each_set"

    first_index=$(( $set_no * $no_of_targets_in_each_set ))
    if [ $set_no == $(( $total_target_sets - 1 )) ]
    then
        last_index=$(( $total_targets - 1 ))
    else
        last_index=$(( $first_index + $no_of_targets_in_each_set - 1 ))
    fi
    echo "First index: $first_index"
    echo "Last index: $last_index"
}

function run_set_of_integration_tests_in_venv {

    cd "$CI_PROJECT_DIR"
    oci_targets=($1)
    set_no="$2"
    total_target_sets="$3"

    echo "Targets: ${oci_targets[@]}"
    echo "Set number: $set_no"
    echo "Number of sets: $total_target_sets"

    set_first_and_last_index $oci_targets $set_no $total_target_sets

    echo "Targets being executed in this set:"
    for (( i=$first_index; i<=$last_index; i++ ))
    do
        echo "${oci_targets[$i]}"
    done

    for (( i=$first_index; i<=$last_index; i++ ))
    do
        ./ansible/test/runner/ansible-test integration -v "$(basename "${oci_targets[$i]}")" --coverage
    done
    ./ansible/test/runner/ansible-test coverage html
    return $?
}

function run_set_of_integration_tests_in_venv_with_role {
    cd "$CI_PROJECT_DIR"
    oci_targets=($1)
    set_no="$2"
    total_target_sets="$3"

    echo "Targets: $oci_targets"
    echo "Set number: $set_no"
    echo "Number of sets: $total_target_sets"

    set_first_and_last_index $oci_targets $set_no $total_target_sets

    echo "Targets being executed in this set:"
    for (( i=$first_index; i<=$last_index; i++ ))
    do
        echo "${oci_targets[$i]}"
    done

    for (( i=$first_index; i<=$last_index; i++ ))
    do
        run_single_test_target_with_role "${oci_targets[$i]}"
    done
    return $?
}

function run_single_test_target_with_role {
  echo "Running integration test target $1"
  echo "Setting ansible roles path is $CI_PROJECT_DIR/ansible/test/integration/targets"
  echo "Target to run is $(basename "$1")"
  ANSIBLE_ROLES_PATH="$CI_PROJECT_DIR/ansible/test/integration/targets" EXTRA_VARS_FILE="$CI_PROJECT_DIR/ansible/test/integration/integration_config.yml" "$CI_PROJECT_DIR"/scripts/run-integration-test-target-in-venv.py "$(basename "$1")"
}

function run_integration_tests_in_venv_with_role {
  # Don't run manual and lengthy tests
  cd "$CI_PROJECT_DIR"
  for test_target in $(find ansible/test/integration/targets/ -type d -name "oci*" | grep -v lengthy | grep -v manual | sort)
  do
      run_single_test_target_with_role "$test_target"
  done

  return $?
}

function run_all_integration_tests_in_venv_with_role {
  cd "$CI_PROJECT_DIR"
  for test_target in $(find ansible/test/integration/targets/ -type d -name "oci*" | grep -v manual | sort)
  do
      run_single_test_target_with_role "$test_target"
  done

  return $?
}


function run_it_tests_in_venv_using_oci_ansible_role {
  #PYVER=$($PYEXEC -c 'import sys; print(".".join([str(i) for i in sys.version_info[:2]]))')
  VENVNAME="$1"
  echo "Running integration tests for $CI_COMMIT_REF_NAME in env $VENVNAME using the venv at $VENVDIR"
  cd "${VENVDIR}/${VENVNAME}"
  pwd
  source bin/activate
  cd -

  # { debug information
    echo "$PATH"
    whoami
    which ansible
    which ansible-galaxy
    which python
    python -c "import sys;print(sys.path)"
    echo "$PYTHONPATH"
    echo "$PATH"
    ansible-galaxy --version
    ansible --version
  # debug information }

  # install latest ansible role in this machine
  # remove any installed ansible roles that was installed earlier
  set +e
  ansible-galaxy remove oci-ansible-role
  set -e

  #This gitlab auth token is required to clone the `oci-ansible-role`
  #repository without any additional credentials
  API_TOKEN=3ywQiK1w8LczUzFjsxMa
  # install the candidate tag ansible role
  echo "installing $CANDIDATE_TAG_NAME of oci-ansible-role"
  ansible-galaxy -vvv -c install git+https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/oci-ansible-role.git,"$CANDIDATE_TAG_NAME"

  export ANSIBLE_LIBRARY=~/.ansible/roles
  export ANSIBLE_MODULE_UTILS=$ANSIBLE_LIBRARY/oci-ansible-role/library

  # print debug details
  print_env

  echo "oci-ansible-role version being used is:"
  grep "__version__ =" $ANSIBLE_MODULE_UTILS/oci_utils.py

  # run tests
  run_integration_tests_in_venv_with_role

  #preserve exit code of run_integration_tests, but deactivate first
  eval "deactivate; exit $?"
}

