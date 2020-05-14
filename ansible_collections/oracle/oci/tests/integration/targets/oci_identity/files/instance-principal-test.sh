#!/usr/bin/env bash

# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


# This script runs an ansible-playbook using OCI ansible modules to list
# all compute instances in the current compartment. It employs the instance
# principal for authentication

# This script assumes an Centos/RHEL/Oracle Linux(OL) instance

set -e
set -x

# install pre-reqs (python, git, oci SDK, oci ansible modules)
sudo yum install -y python-pip
sudo yum install -y git
sudo yum install -y jq

# pinning virtualenv to 16.7.9 as 20.x.x seems to have some problems because of dependencies which are not supported
# by python2 anymore
sudo pip install virtualenv==16.7.9

# setup a virtualenv
virtualenv -p "$(which python)" /tmp/mypyenv
source /tmp/mypyenv/bin/activate
python --version
pip --version
which python
which pip

# install oci SDK library
pip install oci

# install ansible
pip install ansible>=2.9

ansible --version

# allow this script to be idempotent by removing any existing clone
rm -rf oci-ansible-collections

# install OCI ansible modules from zip
mkdir oci-ansible-collections
tar -xf oci-ansible-collections.tar.gz -C oci-ansible-collections/

cd oci-ansible-collections

# install collection
export TEMP_DIR="/tmp/"
rm -rf "TEMP_DIR"/oracle-oci-*.tar.gz
ansible-galaxy collection build --output-path "$TEMP_DIR" --force
ansible-galaxy collection install "$TEMP_DIR"/oracle-oci-*.tar.gz --force-with-deps

echo "Installed collection successfully"

# -- pre-requisites installation complete.

# create playbook to test basic OCI operations
cat > basic-sanity-checks.yaml <<EOL
---
# Copyright (c) 2020, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

- name : Performs some basic OCI operations to validate that configuration is correct
  connection: local
  hosts: localhost

  collections:
    - oracle.oci

  tasks:
    - name: Lists information about current instances
      oci_compute_instance_facts:
        # pick the compartment_id from the environment variable SAMPLE_COMPARTMENT_OCID
        compartment_id: "{{ lookup('env', 'SAMPLE_COMPARTMENT_OCID') }}"
      register: currinstances
    - debug:
        msg: "{{currinstances}}"

    - name: Lists OCI regions
      oci_identity_region_facts:
      register: oci_regions
    - set_fact:
        first_region: "{{ oci_regions.regions[0].name }}"
    - debug: msg="First region {{ first_region }}"
EOL


# get the compartment id of the current instance using the instance metadata
# endpoint https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm
SAMPLE_COMPARTMENT_OCID=$(curl -Ls http://169.254.169.254/opc/v1/instance | jq -r '.compartmentId')
export SAMPLE_COMPARTMENT_OCID

# Set the ansible auth_type to "instance_principal" to have the OCI ansible modules
# use the instance principal associated with this instance, to interact with the
# OCI APIs
OCI_ANSIBLE_AUTH_TYPE="instance_principal" ansible-playbook basic-sanity-checks.yaml
