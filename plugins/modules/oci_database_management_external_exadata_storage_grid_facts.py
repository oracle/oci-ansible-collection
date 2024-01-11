#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_management_external_exadata_storage_grid_facts
short_description: Fetches details about a ExternalExadataStorageGrid resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ExternalExadataStorageGrid resource in Oracle Cloud Infrastructure
    - Gets the details for the storage server grid specified by exadataStorageGridId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_exadata_storage_grid_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage grid.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific external_exadata_storage_grid
  oci_database_management_external_exadata_storage_grid_facts:
    # required
    external_exadata_storage_grid_id: "ocid1.externalexadatastoragegrid.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_exadata_storage_grid:
    description:
        - ExternalExadataStorageGrid resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - The version of the resource.
            returned: on success
            type: str
            sample: version_example
        internal_id:
            description:
                - The internal ID.
            returned: on success
            type: str
            sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the entity.
            returned: on success
            type: str
            sample: status_example
        lifecycle_state:
            description:
                - The current lifecycle state of the database resource.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The timestamp of the creation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The timestamp of the last update.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - The details of the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        additional_details:
            description:
                - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        resource_type:
            description:
                - The type of resource.
            returned: on success
            type: str
            sample: INFRASTRUCTURE_SUMMARY
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of Exadata infrastructure system.
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        server_count:
            description:
                - The number of the storage servers in the Exadata infrastructure.
            returned: on success
            type: float
            sample: 10
        storage_servers:
            description:
                - A list of monitored Exadata storage server.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
                    returned: on success
                    type: str
                    sample: display_name_example
                version:
                    description:
                        - The version of the resource.
                    returned: on success
                    type: str
                    sample: version_example
                internal_id:
                    description:
                        - The internal ID.
                    returned: on success
                    type: str
                    sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
                status:
                    description:
                        - The status of the entity.
                    returned: on success
                    type: str
                    sample: status_example
                lifecycle_state:
                    description:
                        - The current lifecycle state of the database resource.
                    returned: on success
                    type: str
                    sample: CREATING
                time_created:
                    description:
                        - The timestamp of the creation.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The timestamp of the last update.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_details:
                    description:
                        - The details of the lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                additional_details:
                    description:
                        - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {}
                resource_type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: str
                    sample: INFRASTRUCTURE_SUMMARY
                make_model:
                    description:
                        - The make model of the storage server.
                    returned: on success
                    type: str
                    sample: make_model_example
                ip_address:
                    description:
                        - The IP address of the storage server.
                    returned: on success
                    type: str
                    sample: ip_address_example
                cpu_count:
                    description:
                        - The CPU count of the storage server
                    returned: on success
                    type: float
                    sample: 10
                memory_gb:
                    description:
                        - The storage server memory size in GB
                    returned: on success
                    type: float
                    sample: 1.2
                max_hard_disk_iops:
                    description:
                        - The maximum hard disk IO operations per second of the storage server
                    returned: on success
                    type: int
                    sample: 56
                max_hard_disk_throughput:
                    description:
                        - The maximum hard disk IO throughput in MB/s of the storage server
                    returned: on success
                    type: int
                    sample: 56
                max_flash_disk_iops:
                    description:
                        - The maximum flash disk IO operations per second of the storage server
                    returned: on success
                    type: int
                    sample: 56
                max_flash_disk_throughput:
                    description:
                        - The maximum flash disk IO throughput in MB/s of the storage server
                    returned: on success
                    type: int
                    sample: 56
                connector_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of connector.
                    returned: on success
                    type: str
                    sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "version": "version_example",
        "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "status_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "additional_details": {},
        "resource_type": "INFRASTRUCTURE_SUMMARY",
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "server_count": 10,
        "storage_servers": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "version": "version_example",
            "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
            "status": "status_example",
            "lifecycle_state": "CREATING",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_details": "lifecycle_details_example",
            "additional_details": {},
            "resource_type": "INFRASTRUCTURE_SUMMARY",
            "make_model": "make_model_example",
            "ip_address": "ip_address_example",
            "cpu_count": 10,
            "memory_gb": 1.2,
            "max_hard_disk_iops": 56,
            "max_hard_disk_throughput": 56,
            "max_flash_disk_iops": 56,
            "max_flash_disk_throughput": 56,
            "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
        }]
    }
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


class ExternalExadataStorageGridFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "external_exadata_storage_grid_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_storage_grid,
            external_exadata_storage_grid_id=self.module.params.get(
                "external_exadata_storage_grid_id"
            ),
        )


ExternalExadataStorageGridFactsHelperCustom = get_custom_class(
    "ExternalExadataStorageGridFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalExadataStorageGridFactsHelperCustom,
    ExternalExadataStorageGridFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_exadata_storage_grid_id=dict(
                aliases=["id"], type="str", required=True
            ),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_exadata_storage_grid",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_exadata_storage_grid=result)


if __name__ == "__main__":
    main()
