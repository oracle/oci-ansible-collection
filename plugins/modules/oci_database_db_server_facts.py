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
module: oci_database_db_server_facts
short_description: Fetches details about one or multiple DbServer resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbServer resources in Oracle Cloud Infrastructure
    - Lists the Exadata DB servers in the ExadataInfrastructureId and specified compartment.
    - If I(db_server_id) is specified, the details of a single DbServer will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_server_id:
        description:
            - The DB server L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_server.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple db_servers.
        type: str
    exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ExadataInfrastructure.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort by TIMECREATED.  Default order for TIMECREATED is descending.
        type: str
        choices:
            - "TIMECREATED"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "CREATING"
            - "AVAILABLE"
            - "UNAVAILABLE"
            - "DELETING"
            - "DELETED"
            - "MAINTENANCE_IN_PROGRESS"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_server
  oci_database_db_server_facts:
    # required
    db_server_id: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_servers
  oci_database_db_server_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: TIMECREATED
    lifecycle_state: CREATING
    display_name: display_name_example

"""

RETURN = """
db_servers:
    description:
        - List of DbServer resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exacc Db server.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the Db server. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the Db server.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The allocated memory in GBs on the Db server.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The allocated local node storage in GBs on the Db server.
            returned: on success
            type: int
            sample: 56
        vm_cluster_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM Clusters associated with the Db server.
            returned: on success
            type: list
            sample: []
        db_node_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Db nodes associated with the Db server.
            returned: on success
            type: list
            sample: []
        shape:
            description:
                - The shape of the Db server. The shape determines the amount of CPU, storage, and memory resources available.
            returned: on success
            type: str
            sample: shape_example
        lifecycle_state:
            description:
                - The current state of the Db server.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        max_cpu_count:
            description:
                - The total number of CPU cores available.
            returned: on success
            type: int
            sample: 56
        max_memory_in_gbs:
            description:
                - The total memory available in GBs.
            returned: on success
            type: int
            sample: 56
        max_db_node_storage_in_gbs:
            description:
                - The total local node storage available in GBs.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time that the Db Server was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_server_patching_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                estimated_patch_duration:
                    description:
                        - Estimated time, in minutes, to patch one database server.
                    returned: on success
                    type: int
                    sample: 56
                patching_status:
                    description:
                        - The status of the patching operation.
                    returned: on success
                    type: str
                    sample: SCHEDULED
                time_patching_started:
                    description:
                        - The time when the patching operation started.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_patching_ended:
                    description:
                        - The time when the patching operation ended.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "cpu_core_count": 56,
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "vm_cluster_ids": [],
        "db_node_ids": [],
        "shape": "shape_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "max_cpu_count": 56,
        "max_memory_in_gbs": 56,
        "max_db_node_storage_in_gbs": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "db_server_patching_details": {
            "estimated_patch_duration": 56,
            "patching_status": "SCHEDULED",
            "time_patching_started": "2013-10-20T19:20:30+01:00",
            "time_patching_ended": "2013-10-20T19:20:30+01:00"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbServerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "exadata_infrastructure_id",
            "db_server_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "exadata_infrastructure_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_server,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            db_server_id=self.module.params.get("db_server_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_servers,
            compartment_id=self.module.params.get("compartment_id"),
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            **optional_kwargs
        )


DbServerFactsHelperCustom = get_custom_class("DbServerFactsHelperCustom")


class ResourceFactsHelper(DbServerFactsHelperCustom, DbServerFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_server_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            exadata_infrastructure_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "AVAILABLE",
                    "UNAVAILABLE",
                    "DELETING",
                    "DELETED",
                    "MAINTENANCE_IN_PROGRESS",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_server",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_servers=result)


if __name__ == "__main__":
    main()
