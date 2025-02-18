#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_database_management_tablespace
short_description: Manage a Tablespace resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Tablespace resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a tablespace within the Managed Database specified by managedDatabaseId.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_tablespace_actions) module: add_data_files, drop,
      remove_data_file, resize_data_file."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    is_bigfile:
        description:
            - Specifies whether the tablespace is a bigfile or smallfile tablespace.
              A bigfile tablespace contains only one data file or temp file, which can contain up to approximately 4 billion (232) blocks.
              A smallfile tablespace is a traditional Oracle tablespace, which can contain 1022 data files or temp files, each of which can contain up to
              approximately 4 million (222) blocks.
        type: bool
    data_files:
        description:
            - The list of data files or temp files created for the tablespace.
        type: list
        elements: str
    file_count:
        description:
            - The number of data files or temp files created for the tablespace. This is for Oracle Managed Files only.
        type: int
    is_reusable:
        description:
            - Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.
        type: bool
    block_size_in_kilobytes:
        description:
            - Block size for the tablespace.
        type: int
    is_encrypted:
        description:
            - Indicates whether the tablespace is encrypted.
        type: bool
    encryption_algorithm:
        description:
            - The name of the encryption algorithm to be used for tablespace encryption.
        type: str
    default_compress:
        description:
            - The default compression of data for all tables created in the tablespace.
        type: str
        choices:
            - "NO_COMPRESS"
            - "BASIC_COMPRESS"
    extent_management:
        description:
            - Specifies how the extents of the tablespace should be managed.
        type: str
        choices:
            - "AUTOALLOCATE"
            - "UNIFORM"
    extent_uniform_size:
        description:
            - The size of the extent when the tablespace is managed with uniform extents of a specific size.
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    segment_management:
        description:
            - Specifies whether tablespace segment management should be automatic or manual.
        type: str
        choices:
            - "AUTO"
            - "MANUAL"
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    credential_details:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            password:
                description:
                    - The database user's password encoded using BASE64 scheme.
                    - Required when tablespace_admin_credential_type is 'PASSWORD'
                type: str
            tablespace_admin_credential_type:
                description:
                    - The type of the credential for tablespace administration tasks.
                type: str
                choices:
                    - "PASSWORD"
                    - "SECRET"
                required: true
            username:
                description:
                    - The user to connect to the database.
                type: str
                required: true
            role:
                description:
                    - The role of the database user.
                type: str
                choices:
                    - "NORMAL"
                    - "SYSDBA"
                required: true
            password_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret
                      where the database password is stored.
                    - Required when tablespace_admin_credential_type is 'SECRET'
                type: str
    name:
        description:
            - The name of the tablespace. It must be unique within a database.
        type: str
        required: true
    type:
        description:
            - The type of tablespace.
            - This parameter is updatable.
        type: str
        choices:
            - "PERMANENT"
            - "TEMPORARY"
    file_size:
        description:
            - The size of each data file or temp file.
            - This parameter is updatable.
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    status:
        description:
            - The status of the tablespace.
            - This parameter is updatable.
        type: str
        choices:
            - "READ_ONLY"
            - "READ_WRITE"
    is_auto_extensible:
        description:
            - Specifies whether the data file or temp file can be extended automatically.
            - This parameter is updatable.
        type: bool
    auto_extend_next_size:
        description:
            - The size of the next increment of disk space to be allocated automatically when more extents are required.
            - This parameter is updatable.
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    auto_extend_max_size:
        description:
            - The maximum disk space allowed for automatic extension of the data files or temp files.
            - This parameter is updatable.
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    is_max_size_unlimited:
        description:
            - Specifies whether the disk space of the data file or temp file can be limited.
            - This parameter is updatable.
        type: bool
    is_default:
        description:
            - Specifies whether the tablespace is the default tablespace.
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the Tablespace.
            - Use I(state=present) to create or update a Tablespace.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create tablespace
  oci_database_management_tablespace:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    credential_details:
      # required
      password: example-password
      tablespace_admin_credential_type: PASSWORD
      username: username_example
      role: NORMAL
    name: name_example

    # optional
    is_bigfile: true
    data_files: [ "data_files_example" ]
    file_count: 56
    is_reusable: true
    block_size_in_kilobytes: 56
    is_encrypted: true
    encryption_algorithm: encryption_algorithm_example
    default_compress: NO_COMPRESS
    extent_management: AUTOALLOCATE
    extent_uniform_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    segment_management: AUTO
    type: PERMANENT
    file_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    status: READ_ONLY
    is_auto_extensible: true
    auto_extend_next_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    auto_extend_max_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    is_max_size_unlimited: true
    is_default: true

- name: Update tablespace
  oci_database_management_tablespace:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    credential_details:
      # required
      password: example-password
      tablespace_admin_credential_type: PASSWORD
      username: username_example
      role: NORMAL
    name: name_example

    # optional
    type: PERMANENT
    file_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    status: READ_ONLY
    is_auto_extensible: true
    auto_extend_next_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    auto_extend_max_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    is_max_size_unlimited: true
    is_default: true

"""

RETURN = """
tablespace:
    description:
        - Details of the Tablespace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the tablespace.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - The type of tablespace.
            returned: on success
            type: str
            sample: UNDO
        status:
            description:
                - The status of the tablespace.
            returned: on success
            type: str
            sample: ONLINE
        block_size_bytes:
            description:
                - The tablespace block size.
            returned: on success
            type: float
            sample: 10
        logging:
            description:
                - The default logging attribute.
            returned: on success
            type: str
            sample: LOGGING
        is_force_logging:
            description:
                - Indicates whether the tablespace is under Force Logging mode.
            returned: on success
            type: bool
            sample: true
        extent_management:
            description:
                - Indicates whether the extents in the tablespace are Locally managed or Dictionary managed.
            returned: on success
            type: str
            sample: LOCAL
        allocation_type:
            description:
                - The type of extent allocation in effect for the tablespace.
            returned: on success
            type: str
            sample: SYSTEM
        is_plugged_in:
            description:
                - Indicates whether the tablespace is plugged in.
            returned: on success
            type: bool
            sample: true
        segment_space_management:
            description:
                - Indicates whether the free and used segment space in the tablespace is managed using free lists (MANUAL) or bitmaps (AUTO).
            returned: on success
            type: str
            sample: MANUAL
        default_table_compression:
            description:
                - Indicates whether default table compression is enabled or disabled.
            returned: on success
            type: str
            sample: ENABLED
        retention:
            description:
                - Indicates whether undo retention guarantee is enabled for the tablespace.
            returned: on success
            type: str
            sample: GUARANTEE
        is_bigfile:
            description:
                - Indicates whether the tablespace is a Bigfile tablespace or a Smallfile tablespace.
            returned: on success
            type: bool
            sample: true
        predicate_evaluation:
            description:
                - Indicates whether predicates are evaluated by Host or by Storage.
            returned: on success
            type: str
            sample: HOST
        is_encrypted:
            description:
                - Indicates whether the tablespace is encrypted.
            returned: on success
            type: bool
            sample: true
        compress_for:
            description:
                - The operation type for which default compression is enabled.
            returned: on success
            type: str
            sample: BASIC
        default_in_memory:
            description:
                - Indicates whether the In-Memory Column Store (IM column store) is by default enabled or disabled for tables in the tablespace.
            returned: on success
            type: str
            sample: ENABLED
        default_in_memory_priority:
            description:
                - Indicates the default priority for In-Memory Column Store (IM column store) population for the tablespace.
            returned: on success
            type: str
            sample: LOW
        default_in_memory_distribute:
            description:
                - Indicates how the IM column store is distributed by default for the tablespace in an Oracle Real Application Clusters (Oracle RAC)
                  environment.
            returned: on success
            type: str
            sample: AUTO
        default_in_memory_compression:
            description:
                - Indicates the default compression level for the IM column store for the tablespace.
            returned: on success
            type: str
            sample: NO_MEMCOMPRESS
        default_in_memory_duplicate:
            description:
                - Indicates the duplicate setting for the IM column store in an Oracle RAC environment.
            returned: on success
            type: str
            sample: NO_DUPLICATE
        shared:
            description:
                - Indicates whether the tablespace is for shared tablespace, or for local temporary tablespace for leaf (read-only) instances, or for local
                  temporary tablespace for all instance types.
            returned: on success
            type: str
            sample: SHARED
        default_index_compression:
            description:
                - Indicates whether default index compression is enabled or disabled.
            returned: on success
            type: str
            sample: ENABLED
        index_compress_for:
            description:
                - The operation type for which default index compression is enabled.
            returned: on success
            type: str
            sample: ADVANCED_LOW
        default_cell_memory:
            description:
                - This specifies the default value for the CELLMEMORY attribute that tables created in the tablespace will inherit unless the behavior is
                  overridden explicitly. This column is intended for use with Oracle Exadata.
            returned: on success
            type: str
            sample: default_cell_memory_example
        default_in_memory_service:
            description:
                - Indicates how the IM column store is populated on various instances by default for the tablespace.
            returned: on success
            type: str
            sample: DEFAULT
        default_in_memory_service_name:
            description:
                - Indicates the service name for the service on which the IM column store should be populated by default for the tablespace. This column has a
                  value only when the corresponding DEF_INMEMORY_SERVICE is USER_DEFINED. In all other cases, this column is null.
            returned: on success
            type: str
            sample: default_in_memory_service_name_example
        lost_write_protect:
            description:
                - The lost write protection setting for the tablespace.
            returned: on success
            type: str
            sample: ENABLED
        is_chunk_tablespace:
            description:
                - Indicates whether this is a chunk tablespace.
            returned: on success
            type: bool
            sample: true
        temp_group:
            description:
                - The temporary tablespace group.
            returned: on success
            type: str
            sample: temp_group_example
        max_size_kb:
            description:
                - The maximum tablespace size in KB. If the tablespace contains any data files with Autoextend enabled, then this column displays the amount of
                  underlying free storage space for the tablespace. For example, if the current tablespace size is 1 GB, the combined maximum size of all its
                  data files is 32 GB, and its underlying storage (for example, ASM or file system storage) has 20 GB of free space, then this column will have
                  a value of approximately 20 GB. If the tablespace contains only data files with autoextend disabled, then this column displays the allocated
                  space for the entire tablespace, that is, the combined size of all data files in the tablespace.
            returned: on success
            type: float
            sample: 10
        allocated_size_kb:
            description:
                - The allocated tablespace size in KB.
            returned: on success
            type: float
            sample: 10
        user_size_kb:
            description:
                - The size of the tablespace available for user data in KB. The difference between tablespace size and user data size is used for storing
                  metadata.
            returned: on success
            type: float
            sample: 10
        free_space_kb:
            description:
                - The free space available in the tablespace in KB.
            returned: on success
            type: float
            sample: 10
        used_space_kb:
            description:
                - The total space used by the tablespace in KB.
            returned: on success
            type: float
            sample: 10
        used_percent_available:
            description:
                - The percentage of used space out of the maximum available space in the tablespace.
            returned: on success
            type: float
            sample: 1.2
        used_percent_allocated:
            description:
                - The percentage of used space out of the total allocated space in the tablespace.
            returned: on success
            type: float
            sample: 1.2
        is_default:
            description:
                - Indicates whether this is the default tablespace.
            returned: on success
            type: bool
            sample: true
        datafiles:
            description:
                - A list of the data files associated with the tablespace.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The filename (including the path) of the data file or temp file.
                    returned: on success
                    type: str
                    sample: name_example
                status:
                    description:
                        - The status of the file. INVALID status is used when the file number is not in use, for example, a file in a tablespace that was
                          removed.
                    returned: on success
                    type: str
                    sample: AVAILABLE
                online_status:
                    description:
                        - The online status of the file.
                    returned: on success
                    type: str
                    sample: SYSOFF
                is_auto_extensible:
                    description:
                        - Indicates whether the data file is auto-extensible.
                    returned: on success
                    type: bool
                    sample: true
                lost_write_protect:
                    description:
                        - The lost write protection status of the file.
                    returned: on success
                    type: str
                    sample: ENABLED
                shared:
                    description:
                        - Type of tablespace this file belongs to. If it's for a shared tablespace, for a local temporary tablespace for RIM (read-only)
                          instances, or for local temporary tablespace for all instance types.
                    returned: on success
                    type: str
                    sample: SHARED
                instance_id:
                    description:
                        - Instance ID of the instance to which the temp file belongs. This column has a NULL value for temp files that belong to shared
                          tablespaces.
                    returned: on success
                    type: float
                    sample: 10
                max_size_kb:
                    description:
                        - The maximum file size in KB.
                    returned: on success
                    type: float
                    sample: 10
                allocated_size_kb:
                    description:
                        - The allocated file size in KB.
                    returned: on success
                    type: float
                    sample: 10
                user_size_kb:
                    description:
                        - The size of the file available for user data in KB. The actual size of the file minus the USER_BYTES value is used to store file-
                          related metadata.
                    returned: on success
                    type: float
                    sample: 10
                increment_by:
                    description:
                        - The number of blocks used as auto-extension increment.
                    returned: on success
                    type: float
                    sample: 10
                free_space_kb:
                    description:
                        - The free space available in the data file in KB.
                    returned: on success
                    type: float
                    sample: 10
                used_space_kb:
                    description:
                        - The total space used in the data file in KB.
                    returned: on success
                    type: float
                    sample: 10
                used_percent_available:
                    description:
                        - The percentage of used space out of the maximum available space in the file.
                    returned: on success
                    type: float
                    sample: 1.2
                used_percent_allocated:
                    description:
                        - The percentage of used space out of the total allocated space in the file.
                    returned: on success
                    type: float
                    sample: 1.2
    sample: {
        "name": "name_example",
        "type": "UNDO",
        "status": "ONLINE",
        "block_size_bytes": 10,
        "logging": "LOGGING",
        "is_force_logging": true,
        "extent_management": "LOCAL",
        "allocation_type": "SYSTEM",
        "is_plugged_in": true,
        "segment_space_management": "MANUAL",
        "default_table_compression": "ENABLED",
        "retention": "GUARANTEE",
        "is_bigfile": true,
        "predicate_evaluation": "HOST",
        "is_encrypted": true,
        "compress_for": "BASIC",
        "default_in_memory": "ENABLED",
        "default_in_memory_priority": "LOW",
        "default_in_memory_distribute": "AUTO",
        "default_in_memory_compression": "NO_MEMCOMPRESS",
        "default_in_memory_duplicate": "NO_DUPLICATE",
        "shared": "SHARED",
        "default_index_compression": "ENABLED",
        "index_compress_for": "ADVANCED_LOW",
        "default_cell_memory": "default_cell_memory_example",
        "default_in_memory_service": "DEFAULT",
        "default_in_memory_service_name": "default_in_memory_service_name_example",
        "lost_write_protect": "ENABLED",
        "is_chunk_tablespace": true,
        "temp_group": "temp_group_example",
        "max_size_kb": 10,
        "allocated_size_kb": 10,
        "user_size_kb": 10,
        "free_space_kb": 10,
        "used_space_kb": 10,
        "used_percent_available": 1.2,
        "used_percent_allocated": 1.2,
        "is_default": true,
        "datafiles": [{
            "name": "name_example",
            "status": "AVAILABLE",
            "online_status": "SYSOFF",
            "is_auto_extensible": true,
            "lost_write_protect": "ENABLED",
            "shared": "SHARED",
            "instance_id": 10,
            "max_size_kb": 10,
            "allocated_size_kb": 10,
            "user_size_kb": 10,
            "increment_by": 10,
            "free_space_kb": 10,
            "used_space_kb": 10,
            "used_percent_available": 1.2,
            "used_percent_allocated": 1.2
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import CreateTablespaceDetails
    from oci.database_management.models import UpdateTablespaceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TablespaceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(TablespaceHelperGen, self).get_possible_entity_types() + [
            "tablespace",
            "tablespaces",
            "databaseManagementtablespace",
            "databaseManagementtablespaces",
            "tablespaceresource",
            "tablespacesresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_tablespace

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_tablespace,
            tablespace_name=summary_model.name,
            managed_database_id=self.module.params.get("managed_database_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tablespace,
            managed_database_id=self.module.params.get("managed_database_id"),
            tablespace_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "managed_database_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_tablespaces, **kwargs
        )

    def get_create_model_class(self):
        return CreateTablespaceDetails

    def get_exclude_attributes(self):
        return [
            "file_count",
            "block_size_in_kilobytes",
            "auto_extend_next_size",
            "segment_management",
            "is_auto_extensible",
            "is_max_size_unlimited",
            "extent_management",
            "data_files",
            "auto_extend_max_size",
            "file_size",
            "default_compress",
            "is_reusable",
            "extent_uniform_size",
            "encryption_algorithm",
            "credential_details",
        ]

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tablespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                create_tablespace_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTablespaceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tablespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                tablespace_name=self.module.params.get("name"),
                update_tablespace_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


TablespaceHelperCustom = get_custom_class("TablespaceHelperCustom")


class ResourceHelper(TablespaceHelperCustom, TablespaceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            is_bigfile=dict(type="bool"),
            data_files=dict(type="list", elements="str"),
            file_count=dict(type="int"),
            is_reusable=dict(type="bool"),
            block_size_in_kilobytes=dict(type="int"),
            is_encrypted=dict(type="bool"),
            encryption_algorithm=dict(type="str"),
            default_compress=dict(
                type="str", choices=["NO_COMPRESS", "BASIC_COMPRESS"]
            ),
            extent_management=dict(type="str", choices=["AUTOALLOCATE", "UNIFORM"]),
            extent_uniform_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            segment_management=dict(type="str", choices=["AUTO", "MANUAL"]),
            managed_database_id=dict(type="str", required=True),
            credential_details=dict(
                type="dict",
                required=True,
                options=dict(
                    password=dict(type="str", no_log=True),
                    tablespace_admin_credential_type=dict(
                        type="str", required=True, choices=["PASSWORD", "SECRET"]
                    ),
                    username=dict(type="str", required=True),
                    role=dict(type="str", required=True, choices=["NORMAL", "SYSDBA"]),
                    password_secret_id=dict(type="str"),
                ),
            ),
            name=dict(type="str", required=True),
            type=dict(type="str", choices=["PERMANENT", "TEMPORARY"]),
            file_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            status=dict(type="str", choices=["READ_ONLY", "READ_WRITE"]),
            is_auto_extensible=dict(type="bool"),
            auto_extend_next_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            auto_extend_max_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            is_max_size_unlimited=dict(type="bool"),
            is_default=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tablespace",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
