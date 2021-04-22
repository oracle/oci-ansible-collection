#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_update_history_entry_facts
short_description: Fetches details about one or multiple UpdateHistoryEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple UpdateHistoryEntry resources in Oracle Cloud Infrastructure
    - Gets the history of the maintenance update actions performed on the specified cloud VM cluster. Applies to Exadata Cloud Service instances only.
    - If I(update_history_entry_id) is specified, the details of a single UpdateHistoryEntry will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    cloud_vm_cluster_id:
        description:
            - The cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    update_history_entry_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update history entry.
            - Required to get a specific update_history_entry.
        type: str
        aliases: ["id"]
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
- name: List update_history_entries
  oci_database_update_history_entry_facts:
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific update_history_entry
  oci_database_update_history_entry_facts:
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    update_history_entry_id: "ocid1.updatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
update_history_entries:
    description:
        - List of UpdateHistoryEntry resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update history entry.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        update_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update.
            returned: on success
            type: string
            sample: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
        update_action:
            description:
                - The update action.
            returned: on success
            type: string
            sample: ROLLING_APPLY
        update_type:
            description:
                - The type of cloud VM cluster maintenance update.
            returned: on success
            type: string
            sample: GI_UPGRADE
        lifecycle_state:
            description:
                - The current lifecycle state of the maintenance update operation.
            returned: on success
            type: string
            sample: IN_PROGRESS
        lifecycle_details:
            description:
                - Descriptive text providing additional details about the lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_started:
            description:
                - The date and time when the maintenance update action started.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_completed:
            description:
                - The date and time when the maintenance update action completed.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "update_id": "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx",
        "update_action": "ROLLING_APPLY",
        "update_type": "GI_UPGRADE",
        "lifecycle_state": "IN_PROGRESS",
        "lifecycle_details": "lifecycle_details_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_completed": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UpdateHistoryEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cloud_vm_cluster_id",
            "update_history_entry_id",
        ]

    def get_required_params_for_list(self):
        return [
            "cloud_vm_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster_update_history_entry,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            update_history_entry_id=self.module.params.get("update_history_entry_id"),
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
            self.client.list_cloud_vm_cluster_update_history_entries,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            **optional_kwargs
        )


UpdateHistoryEntryFactsHelperCustom = get_custom_class(
    "UpdateHistoryEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    UpdateHistoryEntryFactsHelperCustom, UpdateHistoryEntryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cloud_vm_cluster_id=dict(type="str", required=True),
            update_history_entry_id=dict(aliases=["id"], type="str"),
            update_type=dict(
                type="str", choices=["GI_UPGRADE", "GI_PATCH", "OS_UPDATE"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="update_history_entry",
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

    module.exit_json(update_history_entries=result)


if __name__ == "__main__":
    main()
