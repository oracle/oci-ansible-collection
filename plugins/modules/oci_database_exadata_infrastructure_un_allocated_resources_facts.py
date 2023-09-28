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
module: oci_database_exadata_infrastructure_un_allocated_resources_facts
short_description: Fetches details about a ExadataInfrastructureUnAllocatedResources resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ExadataInfrastructureUnAllocatedResources resource in Oracle Cloud Infrastructure
    - Gets un allocated resources information for the specified Exadata infrastructure. Applies to Exadata Cloud@Customer instances only.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    db_servers:
        description:
            - The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Db servers.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific exadata_infrastructure_un_allocated_resources
  oci_database_exadata_infrastructure_un_allocated_resources_facts:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_servers: [ "db_servers_example" ]

"""

RETURN = """
exadata_infrastructure_un_allocated_resources:
    description:
        - ExadataInfrastructureUnAllocatedResources resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        local_storage_in_gbs:
            description:
                - The minimum amount of un allocated storage that is available across all nodes in the infrastructure.
            returned: on success
            type: int
            sample: 56
        ocpus:
            description:
                - The minimum amount of un allocated ocpus that is available across all nodes in the infrastructure.
            returned: on success
            type: int
            sample: 56
        memory_in_gbs:
            description:
                - The minimum amount of un allocated memory that is available across all nodes in the infrastructure.
            returned: on success
            type: int
            sample: 56
        exadata_storage_in_tbs:
            description:
                - Total unallocated exadata storage in the infrastructure in TBs.
            returned: on success
            type: float
            sample: 1.2
        autonomous_vm_clusters:
            description:
                - The list of Autonomous VM Clusters on the Infra and their associated unallocated resources details
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                un_allocated_adb_storage_in_tbs:
                    description:
                        - Total unallocated autonomous data storage in the AVM in TBs.
                    returned: on success
                    type: float
                    sample: 1.2
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "local_storage_in_gbs": 56,
        "ocpus": 56,
        "memory_in_gbs": 56,
        "exadata_storage_in_tbs": 1.2,
        "autonomous_vm_clusters": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "un_allocated_adb_storage_in_tbs": 1.2
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
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureUnAllocatedResourcesFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "exadata_infrastructure_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "db_servers",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_infrastructure_un_allocated_resources,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            **optional_kwargs
        )


ExadataInfrastructureUnAllocatedResourcesFactsHelperCustom = get_custom_class(
    "ExadataInfrastructureUnAllocatedResourcesFactsHelperCustom"
)


class ResourceFactsHelper(
    ExadataInfrastructureUnAllocatedResourcesFactsHelperCustom,
    ExadataInfrastructureUnAllocatedResourcesFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            exadata_infrastructure_id=dict(aliases=["id"], type="str", required=True),
            db_servers=dict(type="list", elements="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="exadata_infrastructure_un_allocated_resources",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(exadata_infrastructure_un_allocated_resources=result)


if __name__ == "__main__":
    main()
