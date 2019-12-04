#! /bin/bash

# Generate ansible-doc in text form for all OCI ansible cloud modules that are
# shipped as part of a given Tag.
# The docs are generated under $DOCS_DIR/$TAGNAME

set -e

DOCS_DIR="/tmp/ansible-doc"

if [ ! -d $DOCS_DIR ]; then
  echo "$DOCS_DIR doesn't exit"; exit 1
fi

if [ -z "$1" ]; then
  echo "No tag name provided. Usage: $0 tagname."; exit 1
fi

TAG_NAME="$1"

TAG_DOCS_DIR="$DOCS_DIR/$TAG_NAME"
mkdir -p "$TAG_DOCS_DIR"
TAG_DOCS_TEMP_DIR="$TAG_DOCS_DIR/temp"
mkdir -p "$TAG_DOCS_TEMP_DIR"

cd "$TAG_DOCS_TEMP_DIR"

# get a Tag's workspace
git clone git@gitlab-odx.oracledx.com:oci/ansible-cloud-module.git
cd ansible-cloud-module
pwd
git fetch --all --tags --prune
git checkout "tags/$TAG_NAME" -b "branch-$TAG_NAME"

source ./ansible/hacking/env-setup

# generate ansible-doc for all modules in this workspace
# and save each module's doc into its own file under $TAG_DOCS_DIR
for mod in $(ansible-doc -l | grep "^oci_" | cut -d" " -f1);
do
  ansible-doc "$mod" | tee "$TAG_DOCS_DIR/$mod.txt"
done

cd "$TAG_DOCS_DIR"
# replace all references to $TAG_DOCS_TEMP_DIR in ansible-doc output so
# that one tag's docs can be compared to another
sed -i "s@$TAG_DOCS_TEMP_DIR@@g" oci_*.txt

# remove the temporary directory for the given tag
rm -rf "$TAG_DOCS_TEMP_DIR"
