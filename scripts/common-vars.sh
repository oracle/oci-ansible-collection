#!/usr/bin/env bash

# common variables for the scripts
export ANSIBLE_NOCOWS=1 # no cowsay!
export WKSP="$(git rev-parse --show-toplevel)"
export COLLECTION_DIR="$WKSP"/ansible_collections/oracle/oci
# export COLLECTION_INSTALLED_DIR="$HOME/.ansible/collections/ansible_collections/oracle/oci"
export SCRIPTS_DIR="$WKSP"/scripts
export TEMP_DIR="/tmp"

# if running on the gitlab runner
if [[ ! -z "$CI_PROJECT_DIR" ]]
then
    export WKSP_ROOT='/scratch'
    export INSTALLDIR="$WKSP_ROOT/python-installs"
    export PATH="$INSTALLDIR/bin:$PATH"
    export LD_LIBRARY_PATH="$INSTALLDIR/lib:$LD_LIBRARY_PATH"
fi
