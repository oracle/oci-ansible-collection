#! /bin/bash

# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

set -e

function demo_cleanup {
    # This tests dynamic inventory for a scenario in which one of the config parameters is passed as an environment
    # variable.
    config_file_parameters=$(cat ~/.oci/config)

    # Drop the 'region' parameter from the config.
    sed -i '/region=/c\' ~/.oci/config
    cat ~/.oci/config

    # Set the env variable for 'region': OCI_REGION.
    export OCI_REGION=us-ashburn-1

    # Run the script in debug mode.
    echo "sample compartment OCID is $SAMPLE_COMPARTMENT_OCID"
    OCI_CACHE_MAX_AGE=0 OCI_COMPARTMENT_OCID="$SAMPLE_COMPARTMENT_OCID" ../../../ansible/contrib/inventory/oci_inventory.py --debug

    OCI_HOSTNAME_FORMAT=private_ip OCI_CACHE_MAX_AGE=0 OCI_COMPARTMENT_OCID="$SAMPLE_COMPARTMENT_OCID" ansible-playbook -i ../../../ansible/contrib/inventory/oci_inventory.py demo_teardown_using_inventory.yaml
    echo "$config_file_parameters" > ~/.oci/config
    cat ~/.oci/config
}

trap demo_cleanup EXIT

ansible-playbook sample.yaml

# set proxy to use for `uri` calls in `check_secure_mongodb_deployment.yaml`
# see https://pdit-document-repository.oraclecorp.com/display/DISG/PDS-DIS+How+to+Configure+Proxy
export PROXY_SET_SCRIPT="/usr/local/remote/allarch/noarch/admin/scripts/Proxy-Config-set.sh"
if [ -e "$PROXY_SET_SCRIPT" ]; then
    source $PROXY_SET_SCRIPT
    echo "Using Proxy: "
    env | grep http
fi
ansible-playbook check_secure_mongodb_deployment.yaml
