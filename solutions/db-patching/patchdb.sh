#Copyright © 2020, Oracle and/or its affiliates.
#The Universal Permissive License (UPL), Version 1.0

# Using Instance principal
OCI_ANSIBLE_AUTH_TYPE="instance_principal" ansible-playbook-3 patchdb.yml

# Using user based API authentication
##ansible-playbook-3 patchdb.yml -vvv
