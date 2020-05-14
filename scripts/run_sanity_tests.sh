#!/usr/bin/env bash

set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

# run sanity tests
cd "$COLLECTION_DIR"
ansible-test sanity --docker
