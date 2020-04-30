#!/usr/bin/env bash

[[ -n "$DEBUG" || -n "$ANSIBLE_DEBUG" ]] && set -x

set -euo pipefail

# Required to differentiate between Python 2 and 3 environ
PYTHON=${ANSIBLE_TEST_PYTHON_INTERPRETER:-python}

echo "${PYTHON}"
export ANSIBLE_CONFIG=ansible.cfg
OCI_INVENTORY_CONFIG=test_config.oci.yaml

# Get inventory
ansible-inventory -i ${OCI_INVENTORY_CONFIG} --list

echo "Check if cache is working for inventory plugin"
if [ ! -n "$(find "$(pwd)/oci_inventory_cache" -maxdepth 1 -name 'oci_*' -print -quit)" ]; then
    echo "Cache directory not found. Please debug"
    exit 1
fi
echo "Cache is working"


# Test playbook with given inventory
ansible-playbook -i ${OCI_INVENTORY_CONFIG} playbooks/test_oci_inventory_plugin.yaml --connection=local "$@"
