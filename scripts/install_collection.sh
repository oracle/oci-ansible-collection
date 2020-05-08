#!/usr/bin/env bash

set -e # fail on non-zero exits

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

# build collection
cd "$COLLECTION_DIR"
ansible-galaxy collection build --output-path "$TEMP_DIR" --force

# obtain the current version number from the python file
version_last_line=$( tail -n 1 "$COLLECTION_DIR"/plugins/module_utils/oci_version.py) # read from last line of py file
version="${version_last_line#*= }" # remove the '__version__ = ' part from last_line
version="${version//\"/}"   # remove quotes

ansible-galaxy collection install "$TEMP_DIR"/oracle-oci-"$version".tar.gz --force-with-deps
