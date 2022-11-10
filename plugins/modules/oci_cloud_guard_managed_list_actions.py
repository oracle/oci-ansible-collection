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
module: oci_cloud_guard_managed_list_actions
short_description: Perform actions on a ManagedList resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedList resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the ManagedList from current compartment to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_list_id:
        description:
            - The cloudguard list OCID to be passed in the request.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment into which the ManagedList should be moved
        type: str
        required: true
    action:
        description:
            - The action to perform on the ManagedList.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on managed_list
  oci_cloud_guard_managed_list_actions:
    # required
    managed_list_id: "ocid1.managedlist.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
managed_list:
    description:
        - Details of the ManagedList resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - ManagedList display name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - ManagedList description.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier where the resource is created
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        source_managed_list_id:
            description:
                - OCID of the Source ManagedList
            returned: on success
            type: str
            sample: "ocid1.sourcemanagedlist.oc1..xxxxxxEXAMPLExxxxxx"
        list_type:
            description:
                - type of the list
            returned: on success
            type: str
            sample: CIDR_BLOCK
        list_items:
            description:
                - List of ManagedListItem
            returned: on success
            type: list
            sample: []
        feed_provider:
            description:
                - provider of the feed
            returned: on success
            type: str
            sample: CUSTOMER
        is_editable:
            description:
                - If this list is editable or not
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The date and time the managed list was created. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the managed list was updated. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Avoid entering confidential information.
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "source_managed_list_id": "ocid1.sourcemanagedlist.oc1..xxxxxxEXAMPLExxxxxx",
        "list_type": "CIDR_BLOCK",
        "list_items": [],
        "feed_provider": "CUSTOMER",
        "is_editable": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import ChangeManagedListCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedListActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_list_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_list_id")

    def get_get_fn(self):
        return self.client.get_managed_list

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_list,
            managed_list_id=self.module.params.get("managed_list_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeManagedListCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_managed_list_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_list_id=self.module.params.get("managed_list_id"),
                change_managed_list_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ManagedListActionsHelperCustom = get_custom_class("ManagedListActionsHelperCustom")


class ResourceHelper(ManagedListActionsHelperCustom, ManagedListActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_list_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_list",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
