#!/usr/bin/env bash

# This script runs a subset of integration tests passed based on the parameters.
# This script accepts three parameters.
# First parameter represents list of paths of all the integration tests targets
# Second parameter is a number representing the set number of the job calling the script
# Third parameter is a number representing the total number of sets.
# Ex: ./run_integration_tests.sh "oci_generated_core" 0 3

set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

targets=$1
set_no=$2
total_target_sets=$3
if [[ -z $targets ]];
then
    echo "Need to pass integration test targets."
    exit 1
fi

if [[ -z $set_no ]];
then
    echo "Need to pass set_no."
    exit 1
fi

if [[ -z $total_target_sets ]];
then
    echo "Need to pass total_target_sets."
    exit 1
fi

first_index=0
last_index=0

# Finds the integration tests that needs to be run in this set. It does so by dividing the integration tests
# into a given number of sets (third parameter to the script) and sets the first and last indices of the
# specific set (second parameter to the script).
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

# Find the integration tests that need to be run in this set
set_first_and_last_index $targets $set_no $total_target_sets
for (( i=$first_index; i<=$last_index; i++ ))
do
    $SCRIPTS_DIR/run_integration_test.sh "$(basename "${targets[$i]}")"
done


