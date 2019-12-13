#!/usr/bin/env bash

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

ansible-test integration $target
