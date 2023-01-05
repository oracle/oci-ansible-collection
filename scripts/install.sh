#!/usr/bin/env bash

# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


# Description:
# Shell script for installing ansible collection for Oracle Cloud Infrastructure

SCRIPT_NAME="./install.py"
INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-ansible-collection/test-branch/scripts/install.py"

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
    
    --upgrade
        Users can specify this to upgrade the oci-ansible-collection and its required dependencies.
        This is will upgrade oci package and oci-ansible-collection to the latest one.
        Note: This will not upgrade ansible dependency to the latest version.

        Speciying --version along with --upgrade will result in a conflict
        Error will raised and installation will not continue.

    --help|-h
        Show help section
"


install_args=""
OFFLINE=false
PYTHON=""

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
    --ansible-version)
    ANSIBLE_VERSION="$2"
    install_args="$install_args --ansible-version $ANSIBLE_VERSION"
    shift
    shift
    ;;
    --oci-ansible-collection-path)
    OCI_ANSIBLE_COLLECTION_PATH="$2"
    install_args="$install_args --oci-ansible-collection-path $OCI_ANSIBLE_COLLECTION_PATH"
    shift
    shift
    ;;
    --version)
    OCI_ANSIBLE_COLLECTION_VERSION="$2"
    install_args="$install_args --version $OCI_ANSIBLE_COLLECTION_VERSION"
    shift
    shift
    ;;
    --verbose)
    install_args="$install_args --verbose"
    shift
    ;;
    --upgrade-pip)
    install_args="$install_args --upgrade-pip"
    shift
    ;;
    --dry-run)
    DRY_RUN=true
    install_args="$install_args --dry-run"
    shift
    ;;
    --upgrade)
    DRY_RUN=true
    install_args="$install_args --upgrade"
    shift
    ;;
    --python-path)
    PYTHON="$2"
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



downloaded_script=true
echo "Downloading installer script..."
# -t option does not work in all unix environments. Use it if available, else fallback to just mktemp.
install_script=$(mktemp -t oci_ansible_install_tmp_XXXX 2>/dev/null || mktemp) || exit
echo "Downloading oci-ansible-collection install script from $INSTALL_SCRIPT_URL to $install_script."
curl -# -f $INSTALL_SCRIPT_URL > $install_script
if [ $? -ne 0 ]; then
    downloaded_script=false
fi

SCRIPT_NAME=$install_script

if [ "$downloaded_script" == false ]; then
    echo "Error while downloading the installer script"
    exit 1
fi

set -e

chmod 775 $SCRIPT_NAME
# SCRIPT_NAME="./install.py" # ----> remove comment to run locally
echo "-- $python_exe $SCRIPT_NAME $install_args"
echo
$python_exe $SCRIPT_NAME $install_args
echo