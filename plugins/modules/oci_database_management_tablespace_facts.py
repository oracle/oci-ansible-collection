#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_management_tablespace_facts
short_description: Fetches details about one or multiple Tablespace resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Tablespace resources in Oracle Cloud Infrastructure
    - Gets the list of tablespaces for the specified managedDatabaseId.
    - If I(tablespace_name) is specified, the details of a single Tablespace will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tablespace_name:
        description:
            - The name of the tablespace.
            - Required to get a specific tablespace.
        type: str
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'TIMECREATED' is descending and the default sort order for 'NAME' is ascending.
              The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific tablespace
  oci_database_management_tablespace_facts:
    # required
    tablespace_name: tablespace_name_example
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List tablespaces
  oci_database_management_tablespace_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
tablespaces:
    description:
        - List of Tablespace resources
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TablespaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "tablespace_name",
        ]

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tablespace,
            managed_database_id=self.module.params.get("managed_database_id"),
            tablespace_name=self.module.params.get("tablespace_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tablespaces,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


TablespaceFactsHelperCustom = get_custom_class("TablespaceFactsHelperCustom")


class ResourceFactsHelper(TablespaceFactsHelperCustom, TablespaceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tablespace_name=dict(type="str"),
            managed_database_id=dict(type="str", required=True),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tablespace",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tablespaces=result)


if __name__ == "__main__":
    main()
