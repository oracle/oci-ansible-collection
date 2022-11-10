#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_cloud_vm_cluster_update_facts
short_description: Fetches details about one or multiple CloudVmClusterUpdate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CloudVmClusterUpdate resources in Oracle Cloud Infrastructure
    - Lists the maintenance updates that can be applied to the specified cloud VM cluster. Applies to Exadata Cloud Service instances only.
    - If I(update_id) is specified, the details of a single CloudVmClusterUpdate will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    update_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update.
            - Required to get a specific cloud_vm_cluster_update.
        type: str
        aliases: ["id"]
    cloud_vm_cluster_id:
        description:
            - The cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    update_type:
        description:
            - A filter to return only resources that match the given update type exactly.
        type: str
        choices:
            - "GI_UPGRADE"
            - "GI_PATCH"
            - "OS_UPDATE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cloud_vm_cluster_update
  oci_database_cloud_vm_cluster_update_facts:
    # required
    update_id: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List cloud_vm_cluster_updates
  oci_database_cloud_vm_cluster_update_facts:
    # required
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    update_type: GI_UPGRADE

"""

RETURN = """
cloud_vm_cluster_updates:
    description:
        - List of CloudVmClusterUpdate resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Details of the maintenance update package.
            returned: on success
            type: str
            sample: description_example
        last_action:
            description:
                - The update action.
            returned: on success
            type: str
            sample: ROLLING_APPLY
        available_actions:
            description:
                - The possible actions performed by the update operation on the infrastructure components.
            returned: on success
            type: list
            sample: []
        update_type:
            description:
                - The type of cloud VM cluster maintenance update.
            returned: on success
            type: str
            sample: GI_UPGRADE
        lifecycle_details:
            description:
                - Descriptive text providing additional details about the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the maintenance update. Dependent on value of `lastAction`.
            returned: on success
            type: str
            sample: AVAILABLE
        time_released:
            description:
                - The date and time the maintenance update was released.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The version of the maintenance update package.
            returned: on success
            type: str
            sample: version_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "last_action": "ROLLING_APPLY",
        "available_actions": [],
        "update_type": "GI_UPGRADE",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "AVAILABLE",
        "time_released": "2013-10-20T19:20:30+01:00",
        "version": "version_example"
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


class CloudVmClusterUpdateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cloud_vm_cluster_id",
            "update_id",
        ]

    def get_required_params_for_list(self):
        return [
            "cloud_vm_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster_update,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            update_id=self.module.params.get("update_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "update_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cloud_vm_cluster_updates,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            **optional_kwargs
        )


CloudVmClusterUpdateFactsHelperCustom = get_custom_class(
    "CloudVmClusterUpdateFactsHelperCustom"
)


class ResourceFactsHelper(
    CloudVmClusterUpdateFactsHelperCustom, CloudVmClusterUpdateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            update_id=dict(aliases=["id"], type="str"),
            cloud_vm_cluster_id=dict(type="str", required=True),
            update_type=dict(
                type="str", choices=["GI_UPGRADE", "GI_PATCH", "OS_UPDATE"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cloud_vm_cluster_update",
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

    module.exit_json(cloud_vm_cluster_updates=result)


if __name__ == "__main__":
    main()
