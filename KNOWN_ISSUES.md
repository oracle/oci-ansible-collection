# Known Issues

## OCI Ansible Modules

### oci_compute_volume_attachment_facts gets Linux iscsi attach commands for both Linux and Windows
When using the oci_compute_volume_attachment_facts module, it outputs Linux iscsi connect commands for Windows attached Block Volumes.

This issue is fixed in v2.14.0 but only when fetching getting the of a specific volume attachment using volume_attachment_id. Please check [this](https://github.com/oracle/oci-ansible-collection/issues/15) for more details.

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