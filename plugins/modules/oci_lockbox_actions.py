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
module: oci_lockbox_actions
short_description: Perform actions on a Lockbox resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Lockbox resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Lockbox resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lockbox_id:
        description:
            - unique Lockbox identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment where the resource is located.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Lockbox.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on lockbox
  oci_lockbox_actions:
    # required
    lockbox_id: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
lockbox:
    description:
        - Details of the Lockbox resource acted upon by the current operation
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
                - Lockbox Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        partner_compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The unique identifier (OCID) of associated resource that the lockbox is created for.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lockbox_partner:
            description:
                - The partner using this lockbox to lock a resource.
            returned: on success
            type: str
            sample: FAAAS
        time_created:
            description:
                - The time the the Lockbox was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Lockbox was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Lockbox.
            returned: on success
            type: str
            sample: ACTIVE
        access_context_attributes:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of context attributes.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the context attribute
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The description of the context attribute
                            returned: on success
                            type: str
                            sample: description_example
                        default_value:
                            description:
                                - An optional default value used when access request context value is not provided
                            returned: on success
                            type: str
                            sample: default_value_example
        approval_template_id:
            description:
                - Approval template ID
            returned: on success
            type: str
            sample: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
        max_access_duration:
            description:
                - The maximum amount of time operator has access to associated resources.
            returned: on success
            type: str
            sample: max_access_duration_example
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "partner_compartment_id": "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lockbox_partner": "FAAAS",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "access_context_attributes": {
            "items": [{
                "name": "name_example",
                "description": "description_example",
                "default_value": "default_value_example"
            }]
        },
        "approval_template_id": "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx",
        "max_access_duration": "max_access_duration_example",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.lockbox import LockboxClient
    from oci.lockbox.models import ChangeLockboxCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LockboxActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "lockbox_id"

    def get_module_resource_id(self):
        return self.module.params.get("lockbox_id")

    def get_get_fn(self):
        return self.client.get_lockbox

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lockbox, lockbox_id=self.module.params.get("lockbox_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLockboxCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_lockbox_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lockbox_id=self.module.params.get("lockbox_id"),
                change_lockbox_compartment_details=action_details,
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


LockboxActionsHelperCustom = get_custom_class("LockboxActionsHelperCustom")


class ResourceHelper(LockboxActionsHelperCustom, LockboxActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            lockbox_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="lockbox",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
