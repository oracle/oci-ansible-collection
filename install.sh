#!/usr/bin/env bash

# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


# Description:
# Shell script for installing ansible collection for Oracle Cloud Infrastructure

SCRIPT_NAME="install.py"
INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/install.py"

usage="$(basename "$0")
        -- Bash script to install oci-ansible-collection for Oracle Cloud Infrastructure           
           The script supports multiple input arguments, which if not specified, the default
           values for these arguments will be used
    

Following arguments can be passed to the script:
    --virtual-env-dir
        Users can use this flag to specify the location of the python virtual environment where
        python dependencies for oci-ansible-collection will be installed. If not specified 
        default values will be used.
        Ex: --virtual-env-dir /home

    --virtual-env-name
        Users can use this flag to specify the name of the python virtual env name where
        python dependencies for oci-ansible-collection will be installed. If not specified 
        default values will be used.
        Ex: --virtual-env-name my-venv

    --oci-ansible-collection-path
        Users can use this flag to specify the location of collections where oci-ansible-collection 
        will be installed. If not specified the latest value will be used.
        Ex: --oci-ansible-collection-path /home/collections

    --oci-ansible-collection-version
        Users can use this flag to specify the version of oci-ansible-collection will be installed.
        To use the latest version don't set any value(recommended). If not specified the latest 
        version will be used.
        Ex: 2.20

    --verbose
        Users can use this flag to enable more loggings in case of debugging purpose.
        Ex: --verbose    will enable logging

    --dry-run
        Runs the script in dry run mode i.e no network calls and installation of dependecies.
        Ex: --dry-run    will enable the dry run mode

    --offline
        Executes the local copy of the python intaller script. Helpful for debugging locally 

    --help
        Show help section
"

install_args=""
OFFLINE=false

while [[ $# -gt 0 ]];do
key=$1

case $key in
    --virtual-env-dir)
    VIRTUAL_ENV_DIR="$2"
    install_args="$install_args --virtual-env-dir $VIRTUAL_ENV_DIR"
    shift
    shift
    ;;
    --virtual-env-name)
    VIRTUAL_ENV_NAME="$2"
    install_args="$install_args --virtual-env-name $VIRTUAL_ENV_NAME"
    shift
    shift
    ;;
    --oci-ansible-collection-path)
    OCI_ANSIBLE_COLLECTION_PATH="$2"
    install_args="$install_args --oci-ansible-collection-path $OCI_ANSIBLE_COLLECTION_PATH"
    shift
    shift
    ;;
    --oci-ansible-collection-version)
    OCI_ANSIBLE_COLLECTION_VERSION="$2"
    install_args="$install_args --oci-ansible-collection-version $OCI_ANSIBLE_COLLECTION_VERSION"
    shift
    shift
    ;;
    --verbose)
    install_args="$install_args --verbose"
    shift
    ;;
    --dry-run)
    DRY_RUN=true
    install_args="$install_args --dry-run"
    shift
    ;;
    --offline)
    OFFLINE=true
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
python_exe=python3
python_installed=false
command -v python >/dev/null 2>&1
if [ $? -eq 0 ]; then
    # python3 is installed.   
    # check if python>=3.6 is present
    python3 -c "import sys; v = sys.version_info; valid = v >= (3, 6, ); sys.exit(0) if valid else sys.exit(1)"
    if [ $? -eq 0 ]; then
        python_exe=python3
        python_installed=true
    else
        exit 1
    fi
fi


if [ "$python_installed" == false ]; then
    echo "WARN: python version >=3.6 is needed to install oci-ansible-collection"
    exit 1
fi


if [ "$OFFLINE" == false ]; then
    downloaded_script=false
    echo "Downloading installer script"
    install_script=$(mktemp -t oci_cli_install_tmp_XXXX) || exit
    echo "Downloading oci-ansible-collection install script from $INSTALL_SCRIPT_URL to $install_script."
    curl -# -f $INSTALL_SCRIPT_URL > $install_script
    if [ $? -ne 0 ]; then
        exit 1
    fi
    downloaded_script=true
    SCRIPT_NAME=$install_script
else
    echo "Using offline mode, installing using local script $SCRIPT_NAME"
fi

echo "$downloaded_script"
if [ "$downloaded_script" == false ]; then
    echo "Error while downloading the installer script"
    exit 1
fi

chmod 775 $SCRIPT_NAME

echo "-- $python_exe $SCRIPT_NAME $install_args"
echo
$python_exe $SCRIPT_NAME $install_args
echo