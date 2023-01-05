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
module: oci_cloud_guard_security_zone_actions
short_description: Perform actions on a SecurityZone resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SecurityZone resource in Oracle Cloud Infrastructure
    - For I(action=add_compartment), add an existing compartment to a security zone. If you previously removed a subcompartment from a security zone, you can
      add it back to the same security zone. The security zone ensures that resources in the subcompartment comply with the security zone's policies.
    - For I(action=change_compartment), moves a security zone to a different compartment. When provided, `If-Match` is checked against `ETag` values of the
      resource.
    - For I(action=remove_compartment), removes an existing compartment from a security zone. When you remove a subcompartment from a security zone, it no
      longer enforces security zone policies on the resources in the subcompartment. You can't remove the primary compartment that was used to create the
      security zone.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    security_zone_id:
        description:
            - The unique identifier of the security zone (`SecurityZone`)
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to be added to the security zone.
        type: str
        required: true
    action:
        description:
            - The action to perform on the SecurityZone.
        type: str
        required: true
        choices:
            - "add_compartment"
            - "change_compartment"
            - "remove_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_compartment on security_zone
  oci_cloud_guard_security_zone_actions:
    # required
    security_zone_id: "ocid1.securityzone.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_compartment

- name: Perform action change_compartment on security_zone
  oci_cloud_guard_security_zone_actions:
    # required
    security_zone_id: "ocid1.securityzone.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_compartment on security_zone
  oci_cloud_guard_security_zone_actions:
    # required
    security_zone_id: "ocid1.securityzone.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_compartment

"""

RETURN = """
security_zone:
    description:
        - Details of the SecurityZone resource acted upon by the current operation
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
                - The security zone's name
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The security zone's description
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment for the security zone
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        security_zone_recipe_id:
            description:
                - The OCID of the recipe (`SecurityRecipe`) for the security zone
            returned: on success
            type: str
            sample: "ocid1.securityzonerecipe.oc1..xxxxxxEXAMPLExxxxxx"
        security_zone_target_id:
            description:
                - The OCID of the target associated with the security zone
            returned: on success
            type: str
            sample: "ocid1.securityzonetarget.oc1..xxxxxxEXAMPLExxxxxx"
        inherited_by_compartments:
            description:
                - List of inherited compartments
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time the security zone was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the security zone was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the security zone
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the
                  `Failed` state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        "security_zone_recipe_id": "ocid1.securityzonerecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "security_zone_target_id": "ocid1.securityzonetarget.oc1..xxxxxxEXAMPLExxxxxx",
        "inherited_by_compartments": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.cloud_guard.models import AddCompartmentDetails
    from oci.cloud_guard.models import ChangeSecurityZoneCompartmentDetails
    from oci.cloud_guard.models import RemoveCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecurityZoneActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_compartment
        change_compartment
        remove_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "security_zone_id"

    def get_module_resource_id(self):
        return self.module.params.get("security_zone_id")

    def get_get_fn(self):
        return self.client.get_security_zone

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_zone,
            security_zone_id=self.module.params.get("security_zone_id"),
        )

    def add_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_zone_id=self.module.params.get("security_zone_id"),
                add_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSecurityZoneCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_security_zone_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_zone_id=self.module.params.get("security_zone_id"),
                change_security_zone_compartment_details=action_details,
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

    def remove_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_zone_id=self.module.params.get("security_zone_id"),
                remove_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


SecurityZoneActionsHelperCustom = get_custom_class("SecurityZoneActionsHelperCustom")


class ResourceHelper(SecurityZoneActionsHelperCustom, SecurityZoneActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            security_zone_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["add_compartment", "change_compartment", "remove_compartment"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="security_zone",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
