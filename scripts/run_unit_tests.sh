#!/usr/bin/env bash

set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

# set pythonpath
export PYTHONPATH="$WKSP:$PYTHONPATH"
echo $PYTHONPATH

# run unit tests
pytest -r a --fulltrace --color yes $COLLECTION_DIR/tests/unit/ -vvv
