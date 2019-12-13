#!/usr/bin/env bash

set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

# run sanity tests
cd "$COLLECTION_DIR"
#ansible-test sanity --docker --skip-test future-import-boilerplate --skip-test metaclass-boilerplate
#ansible-test sanity --docker --test future-import-boilerplate --test metaclass-boilerplate plugins/inventory/*py plugins/modules/*py plugins/module_utils/*py
ansible-test sanity --docker
