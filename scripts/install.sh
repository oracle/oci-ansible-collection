#!/usr/bin/env bash

# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


# Description:
# Shell script for installing ansible collection for Oracle Cloud Infrastructure

SCRIPT_NAME="./install.py"
INSTALL_SCRIPT_REF="${INSTALL_SCRIPT_REF:-v5.5.0}"
INSTALL_SCRIPT_URL="${INSTALL_SCRIPT_URL:-https://raw.githubusercontent.com/oracle/oci-ansible-collection/${INSTALL_SCRIPT_REF}/scripts/install.py}"
INSTALL_SCRIPT_SHA256="${INSTALL_SCRIPT_SHA256:-}"

set -e

usage="$(basename "$0")
        -- Bash script to install oci-ansible-collection for Oracle Cloud Infrastructure           
           The script supports multiple input arguments, which if not specified, the default
           values for these arguments will be used
    

Following arguments can be passed to the script:
    --virtual-env-dir
        Users can use this flag to specify the location where the virtual environment is located or should be created
        if not already present. If this path already exists then it will be used else it will be created.

        default value: ~/lib

    --virtual-env-name
        Users can use this flag to specify the python virtual env name where
        python dependencies for oci-ansible-collections will be installed.
        This virtual env is created in the path sepcified in --virtual-env-dir flag else in the default folder path
        used by --virtual-env-dir flag.
        
        default value: oci-ansible-collection

    --ansible-version
        Users can specify particular version of ansible python package they want to install. Ex: 2.9
        To use the latest version dont't set this flag (recommended).
        This flag doesn't support upgrading the version in case user has already installed ansible 
        and wants to upgrade to a higher version.

        default value: latest version will be installed

    --oci-ansible-collection-path
        Users can use this flag to specify the location of collections where oci-ansible-collection 
        will be installed. Default path for this is determined by ansible-galaxy installer.

    --version
        Users can use this flag to specify the version of oci-ansible-collection will be installed.
        To use the latest version don't set any value(recommended). If not specified the latest 
        version will be used.
        Ex: 2.20.0

        Speciying --version along with --upgrade will result in a conflict
        Error will raised and installation will not continue.

        default value: latest version is picked
    
    --python-path
        Users can specify the specific python they want to use for installation.
        Note: minimum python version supported is python3.6

    --verbose
        Users can use this flag to enable more loggings in case of debugging purpose.
        Disabled by default.
        Ex: --verbose    will enable logging

    --dry-run
        Runs the script in dry run mode i.e no network calls during installation and installation of dependecies.
        Disabled by default.
        Ex: --dry-run    will enable the dry run mode

    --install-script-ref
        Git ref used to download install.py when a local install.py is not available.
        Defaults to the release tag for this installer.

    --install-script-sha256
        SHA-256 checksum for the downloaded install.py. Required for remote downloads.
    
    --upgrade
        Users can specify this to upgrade the oci-ansible-collection and its required dependencies.
        This is will upgrade oci package and oci-ansible-collection to the latest one.
        Note: This will not upgrade ansible dependency to the latest version.

        Speciying --version along with --upgrade will result in a conflict
        Error will raised and installation will not continue.

    --help|-h
        Show help section
"


install_args=()
OFFLINE=false
PYTHON=""

while [[ $# -gt 0 ]];do
key=$1

case $key in
    --virtual-env-dir)
    VIRTUAL_ENV_DIR="$2"
    install_args+=(--virtual-env-dir "$VIRTUAL_ENV_DIR")
    shift
    shift
    ;;
    --virtual-env-name)
    VIRTUAL_ENV_NAME="$2"
    install_args+=(--virtual-env-name "$VIRTUAL_ENV_NAME")
    shift
    shift
    ;;
    --ansible-version)
    ANSIBLE_VERSION="$2"
    install_args+=(--ansible-version "$ANSIBLE_VERSION")
    shift
    shift
    ;;
    --oci-ansible-collection-path)
    OCI_ANSIBLE_COLLECTION_PATH="$2"
    install_args+=(--oci-ansible-collection-path "$OCI_ANSIBLE_COLLECTION_PATH")
    shift
    shift
    ;;
    --version)
    OCI_ANSIBLE_COLLECTION_VERSION="$2"
    install_args+=(--version "$OCI_ANSIBLE_COLLECTION_VERSION")
    if [ "$INSTALL_SCRIPT_REF" = "v5.5.0" ]; then
        INSTALL_SCRIPT_REF="v$OCI_ANSIBLE_COLLECTION_VERSION"
        INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-ansible-collection/${INSTALL_SCRIPT_REF}/scripts/install.py"
    fi
    shift
    shift
    ;;
    --verbose)
    install_args+=(--verbose)
    shift
    ;;
    --upgrade-pip)
    install_args+=(--upgrade-pip)
    shift
    ;;
    --dry-run)
    DRY_RUN=true
    install_args+=(--dry-run)
    shift
    ;;
    --upgrade)
    DRY_RUN=true
    install_args+=(--upgrade)
    shift
    ;;
    --python-path)
    PYTHON="$2"
    shift
    shift
    ;;
    --install-script-ref)
    INSTALL_SCRIPT_REF="$2"
    INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-ansible-collection/${INSTALL_SCRIPT_REF}/scripts/install.py"
    shift
    shift
    ;;
    --install-script-sha256)
    INSTALL_SCRIPT_SHA256="$2"
    shift
    shift
    ;;
    --help|-h)
    echo "$usage"
    exit 1
    ;;
    *)    # unknown option
    echo "Failed to run install script. Unrecognized argument: $1"
    exit 1
    ;;
esac
done

# check if there is a python >=3.6 as oci-ansible-collection is supported for python>=3.6
declare -a supported_versions=(python3.10 python3.9 python3.8 python3.7 python3.6)

unsupported_py_version=false
python_installed=false
python_exe=$PYTHON

set +e
if [ ! -z "$PYTHON" ]; then
        $PYTHON -c "import sys; v = sys.version_info; valid = v >= (3, 6, ); sys.exit(0) if valid else sys.exit(1)"
        if [ ! $? -eq 0 ]; then
            unsupported_py_version=true
        else
            python_installed=true
        fi
fi

if [ "$unsupported_py_version" == true ]; then
    echo "Incorrect/Unsupported python path $PYTHON passed as argument"
    exit 1
fi

if [ -z "$PYTHON" ]; then # if no python path provided
    command -v python3 >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "ERROR: python version 3 not found. python version >=3.6 is needed to install oci-ansible-collection"
        exit 1
    fi

    # python3 is installed.
    # Try with python3 first since if it works we need not go through a list of hard coded
    # versions. The problem with hard coded versions is we need to keep on updating it when
    # a new version is installed. For now, I don't see a simple alternative for doing the
    # python interpreter discovery without a list of hard coded versions. But python3 generally
    # points to the recent installation and most of the times it being the newest version, I think
    # it is a reasonable assumption to go with python3 if it satisfies our requirements.
    python3 -c "import sys; v = sys.version_info; valid = v >= (3, 6, ); sys.exit(0) if valid else sys.exit(1)"
    if [ ! $? -eq 0 ]; then
        for i in "${supported_versions[@]}"; do
          echo $i
          $i -c "import sys; v = sys.version_info; valid = v >= (3, 6, ); sys.exit(0) if valid else sys.exit(1)"
          if [ $? -eq 0 ]; then
              python_exe=$i
              python_installed=true
              break
          fi
        done
    else
        python_exe=python3
        python_installed=true
    fi
fi
set -e


if [ "$python_installed" == false ]; then
    echo "ERROR: python version >=3.6 is needed to install oci-ansible-collection"
    exit 1
fi

verify_sha256() {
    local file_path="$1"
    local expected_sha="$2"
    local actual_sha=""

    if command -v sha256sum >/dev/null 2>&1; then
        actual_sha=$(sha256sum "$file_path" | awk '{print $1}')
    elif command -v shasum >/dev/null 2>&1; then
        actual_sha=$(shasum -a 256 "$file_path" | awk '{print $1}')
    else
        echo "ERROR: sha256sum or shasum is required to verify downloaded installer integrity"
        exit 1
    fi

    if [ "$actual_sha" != "$expected_sha" ]; then
        echo "ERROR: installer checksum verification failed"
        echo "Expected: $expected_sha"
        echo "Actual:   $actual_sha"
        exit 1
    fi
}



downloaded_script=true
echo "Downloading installer script..."
# -t option does not work in all unix environments. Use it if available, else fallback to just mktemp.
install_script=$(mktemp -t oci_ansible_install_tmp_XXXX 2>/dev/null || mktemp) || exit
chmod 600 "$install_script"
echo "Downloading oci-ansible-collection install script from $INSTALL_SCRIPT_URL to $install_script."
curl -# -fL "$INSTALL_SCRIPT_URL" -o "$install_script"
if [ $? -ne 0 ]; then
    downloaded_script=false
fi

SCRIPT_NAME=$install_script

if [ "$downloaded_script" == false ]; then
    echo "Error while downloading the installer script"
    exit 1
fi

if [ -z "$INSTALL_SCRIPT_SHA256" ]; then
    echo "ERROR: --install-script-sha256 or INSTALL_SCRIPT_SHA256 is required for remote installer downloads"
    exit 1
fi

verify_sha256 "$install_script" "$INSTALL_SCRIPT_SHA256"

set -e

# SCRIPT_NAME="./install.py" # ----> remove comment to run locally
echo "-- $python_exe $SCRIPT_NAME ${install_args[*]}"
echo
"$python_exe" "$SCRIPT_NAME" "${install_args[@]}"
echo
