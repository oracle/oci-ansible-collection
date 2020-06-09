# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.1.0-Beta] - 2020-6-8

### Added:
- Added Database modules
- Added the following modules:
    - oci_blockstorage_boot_volume_kms_key
    - oci_blockstorage_boot_volume_kms_key_facts
    - oci_blockstorage_volume_kms_key
    - oci_blockstorage_volume_kms_key_facts
    - oci_compute_management_instance_pool_load_balancer_attachment_facts
    - oci_vault_secret
    - oci_vault_secret_version_facts
    - oci_vault_secret_facts
    - oci_vault_secret_version_actions
    - oci_vault_secret_actions
    - oci_secrets_secret_bundle_facts
    - oci_secrets_secret_bundle_version_facts

- Added new parameters to the following modules:
    - `backup_policy_id` in oci_blockstorage_boot_volume
    - `is_shareable` in oci_compute_volume_attachment
    - `fault_domains` in oci_compute_management_instance_pool
    - `purge_security_rules` and `delete_security_rules` in `oci_network_security_list`

### Changed:
- Removed the parameter `launch_options` in the module oci_compute_image.

## [2.0.0-Beta] - 2020-5-14

### Added:
New release of collection modules.

### Changed:
- Please update to the latest version of OCI Python SDK.
- Please expect a few breaking changes as we transition from legacy modules to the new collection modules.
We recommend you to refer to the [Migration Guide](https://github.com/oracle/oci-ansible-collections/blob/master/MigrationGuide.md) as you plan to migrate.
