#!/usr/bin/env bash

# This script either runs all the integration tests if no parameter is passed
# or runs a specific integration test passed as the parameter to the script.
# Ex: ./run_integration_test.sh # Runs all the integration tests sequentially
# Ex: ./run_integration_test.sh oci_generated_core # Runs oci_generated_core integration test
set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

# ansible-test works only from the collection directory
cd "$COLLECTION_DIR"

target=$1
if [[ -z $target ]];
then
    echo "Running all the integration tests."
    ansible-test integration --list-targets
else
    echo "Running the integration test target $target"
fi

ansible-test integration "$@"
