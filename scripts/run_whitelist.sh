#!/usr/bin/env bash

# This runs the github-tools to make sure the github public release
# consists of the whitelisted files. Even the tests files are included
# at the moment which will be deleted in another script

set -e

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

cd "$WKSP"/..

# create a virtualenv for
virtualenv tools-venv
source tools-venv/bin/activate

# install github-tools
cd "$WKSP"/github-tools
pip install -e .

# creata temp directory
if [ -d "$RELEASE_TEMP_DIR" ]; then
  rm -rf "$RELEASE_TEMP_DIR"
fi
mkdir "$RELEASE_TEMP_DIR"

cd "$WKSP"
github copy . "$RELEASE_TEMP_DIR" --dry-run=false
ls -la "$RELEASE_TEMP_DIR"
ls -la "$RELEASE_TEMP_DIR"/ansible_collections/oracle/oci

# copy over the target tests and tox for testing purposes theses tests will
# be deleted in a `push_to_github` script after the tests have run and passed
cp -r "$COLLECTION_DIR"/tests "$RELEASE_TEMP_DIR"/ansible_collections/oracle/oci/tests
cp -r "$WKSP"/scripts "$RELEASE_TEMP_DIR"
cp -r "$WKSP"/tox.ini "$RELEASE_TEMP_DIR"
ls -la "$RELEASE_TEMP_DIR"
ls -la "$RELEASE_TEMP_DIR"/ansible_collections/oracle/oci

# copy over the scripts to another file location
if [ -d "$TEMP_SCRIPTS" ]; then
  rm -rf "$TEMP_SCRIPTS"
fi
mkdir "$TEMP_SCRIPTS"
cp -r "$WKSP"/scripts/* "$TEMP_SCRIPTS"/

# remove all current files and replace it with the ones saved in the temp_dir
cd "$WKSP"
rm -rf *
cp -r "$RELEASE_TEMP_DIR"/* .
ls -la
