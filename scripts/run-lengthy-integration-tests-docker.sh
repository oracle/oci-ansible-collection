#! /bin/bash

function run_lengthy_integration_tests_in_docker {
  # Don't run manual and lengthy tests
  cd "$CI_PROJECT_DIR"
  for test_target in $(find ansible/test/integration/targets/ -type d -name "oci_*" | grep lengthy | grep -v manual | sort)
  do
      ./ansible/test/runner/ansible-test integration -v "$(basename "$test_target")" --docker --python 2.7 --coverage
  done
  for test_target in $(find ansible/test/integration/targets/ -type d -name "oci_*" | grep lengthy | grep -v manual | sort)
  do
      ./ansible/test/runner/ansible-test integration -v "$(basename "$test_target")" --docker ubuntu1604py3 --python 3.5 --coverage
  done
  return $?
}

run_lengthy_integration_tests_in_docker
