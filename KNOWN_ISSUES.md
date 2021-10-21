# Known Issues

## OCI Ansible Modules

### oci_compute_volume_attachment_facts gets Linux iscsi attach commands for both Linux and Windows
When using the oci_compute_volume_attachment_facts module, it outputs Linux iscsi connect commands for Windows attached Block Volumes.

This issue is fixed in v2.14.0 but only when fetching getting the of a specific volume attachment using volume_attachment_id. Please check [this](https://github.com/oracle/oci-ansible-collection/issues/15) for more details.

### oci_nosql_table module is not idempotent
The nosql service may change the user provided ddl_statement to a functinoally equivalent ddl_statement. 
This can cause future runs of the playbook to fail because the module compares each attribute with existin values and this might cause a mismatch and thus attemps to perform the operation again. 
For create operation, you can get around this problem by using `key_by` module parameter and not having `ddl_statement` in it.

## OCI Inventory Plugin

### fetch_db_host does not work with tag filters
When the tag filters (freeform_tags and defined_tags) are specified in the config, the db hosts are not returned. This happens because the db hosts do not support tags yet so the plugin filters them since they don't have the specified tags.

Workaround: Avoid using tag filters when fetching db hosts and do any filtering as post processing of the inventory

### Instances with valid hostname_format for secondary vnics but not primary vnic are skipped
The inventory plugin was not processing the secondary VNICs of a compute instance with valid specified hostname_format if the primary VNIC does not have a valid hostname_format.

This issue is fixed in v2.16.0

### Inventory generation fails with JSONDecodeError in ansible tower
The OCI Inventory Plugin outputs some informational log messages along with the inventory. But ansible tower expects the output from the inventory plugin to only contain the inventory in JSON format which caused the failure.

This issue is fixed in v2.16.0

### Issues while creating/updating private_ip using oci_network_private_ip module
Whenever we want to create private ip, we need to specify the `vnic_id` (`vlan_id` in case of VMWare solution). While updating the private_ip resource,
we can use `OCI_USE_NAME_AS_IDENTIFIER` variable to update by passing the name. `vnic_id` is an updatable field but it doesn't get updated when `OCI_USE_NAME_AS_IDENTIFIER` is set.
Instead it creates a new resource (if possible) in the new `vnic_id`. To update the `vnic_id` of a private_ip resource, we use `private_ip_id` (`id` of the resource) without
setting the `OCI_USE_NAME_AS_IDENTIFIER`.

### ChangeCompartment action on InstanceConfiguration resource
There are two actions which can be performed on instance_configuration resource i.e launch and change_compartment.
These actions return different repsonse models when performed.
`launch` returns `Instance` type while `change_compartment` returns `instance_configuration`
Use `result['instance']` to access response of `launch` action and `result['instance_configuration']` for change_compartment action.
