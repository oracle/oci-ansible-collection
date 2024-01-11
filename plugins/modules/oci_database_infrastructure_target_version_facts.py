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
module: oci_database_infrastructure_target_version_facts
short_description: Fetches details about a InfrastructureTargetVersion resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a InfrastructureTargetVersion resource in Oracle Cloud Infrastructure
    - Gets details of the Exadata Infrastructure target system software versions that can be applied to the specified infrastructure resource for maintenance
      updates.
      Applies to Exadata Cloud@Customer and Exadata Cloud instances only.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    target_resource_id:
        description:
            - The target resource ID.
        type: str
    target_resource_type:
        description:
            - The type of the target resource.
        type: str
        choices:
            - "AUTONOMOUS_EXADATA_INFRASTRUCTURE"
            - "AUTONOMOUS_CONTAINER_DATABASE"
            - "EXADATA_DB_SYSTEM"
            - "CLOUD_EXADATA_INFRASTRUCTURE"
            - "EXACC_INFRASTRUCTURE"
            - "AUTONOMOUS_VM_CLUSTER"
            - "AUTONOMOUS_DATABASE"
            - "CLOUD_AUTONOMOUS_VM_CLUSTER"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific infrastructure_target_version
  oci_database_infrastructure_target_version_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    target_resource_id: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"
    target_resource_type: AUTONOMOUS_EXADATA_INFRASTRUCTURE

"""

RETURN = """
infrastructure_target_version:
    description:
        - InfrastructureTargetVersion resource
    returned: on success
    type: complex
    contains:
        target_db_version_history_entry:
            description:
                - The history entry of the target system software version for the database server patching operation.
            returned: on success
            type: list
            sample: []
        target_storage_version_history_entry:
            description:
                - The history entry of the target storage cell system software version for the storage cell patching operation.
            returned: on success
            type: list
            sample: []
        target_resource_type:
            description:
                - The resource type of the target Exadata infrastructure resource that will receive the system software update.
            returned: on success
            type: str
            sample: EXADATA_DB_SYSTEM
        target_resource_id:
            description:
                - The OCID of the target Exadata Infrastructure resource that will receive the maintenance update.
            returned: on success
            type: str
            sample: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "target_db_version_history_entry": [],
        "target_storage_version_history_entry": [],
        "target_resource_type": "EXADATA_DB_SYSTEM",
        "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"
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


class InfrastructureTargetVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "target_resource_id",
            "target_resource_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_infrastructure_target_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


InfrastructureTargetVersionFactsHelperCustom = get_custom_class(
    "InfrastructureTargetVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    InfrastructureTargetVersionFactsHelperCustom,
    InfrastructureTargetVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            target_resource_id=dict(type="str"),
            target_resource_type=dict(
                type="str",
                choices=[
                    "AUTONOMOUS_EXADATA_INFRASTRUCTURE",
                    "AUTONOMOUS_CONTAINER_DATABASE",
                    "EXADATA_DB_SYSTEM",
                    "CLOUD_EXADATA_INFRASTRUCTURE",
                    "EXACC_INFRASTRUCTURE",
                    "AUTONOMOUS_VM_CLUSTER",
                    "AUTONOMOUS_DATABASE",
                    "CLOUD_AUTONOMOUS_VM_CLUSTER",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="infrastructure_target_version",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(infrastructure_target_version=result)


if __name__ == "__main__":
    main()
