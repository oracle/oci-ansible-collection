#!/usr/bin/env bash

set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

# build collection
cd "$COLLECTION_DIR"
ansible-galaxy collection build --output-path "$TEMP_DIR" --force

ansible-galaxy collection install "$TEMP_DIR"/oracle-oci_modules-2.0.0.tar.gz --force-with-deps
