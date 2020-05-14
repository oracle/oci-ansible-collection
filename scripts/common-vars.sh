#!/usr/bin/env bash

# common variables for the scripts
export ANSIBLE_NOCOWS=1 # no cowsay!
export WKSP="$(git rev-parse --show-toplevel)"
export COLLECTION_DIR="$WKSP"/ansible_collections/oracle/oci
# export COLLECTION_INSTALLED_DIR="$HOME/.ansible/collections/ansible_collections/oracle/oci"
export SCRIPTS_DIR="$WKSP"/scripts
export TEMP_DIR="/tmp"

# obtain the current version number from the python file
version_last_line=$( tail -n 1 "$COLLECTION_DIR"/plugins/module_utils/oci_version.py) # read from last line of py file
version="${version_last_line#*= }" # remove the '__version__ = ' part from last_line
export COLLECTIONS_VERSION="${version//\"/}"   # remove quotes
export RELEASE_TEMP_DIR="$TEMP_DIR"/release_"$COLLECTIONS_VERSION"
export TEMP_SCRIPTS="$TEMP_DIR"/collections_scripts
export COLLECTIONS_NAME="oci-ansible-collections"
export GITHUB_COLLECTIONS_TARGET="git@github.com:oracle/$COLLECTIONS_NAME.git"
export GITLAB_COLLECTIONS_TARGET="git@gitlab-odx.oracledx.com:oci/ansible_collections_oci.git"

# if running on the gitlab runner
if [[ ! -z "$CI_PROJECT_DIR" ]]
then
    export WKSP_ROOT='/scratch'
    export INSTALLDIR="$WKSP_ROOT/python-installs"
    export PATH="$INSTALLDIR/bin:$PATH"
    export LD_LIBRARY_PATH="$INSTALLDIR/lib:$LD_LIBRARY_PATH"
fi
