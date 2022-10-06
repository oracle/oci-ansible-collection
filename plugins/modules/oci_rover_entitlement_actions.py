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
module: oci_rover_entitlement_actions
short_description: Perform actions on a RoverEntitlement resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RoverEntitlement resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an entitlement into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_entitlement_id:
        description:
            - ID of the rover node or cluster entitlement
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID],https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resources should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the RoverEntitlement.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on rover_entitlement
  oci_rover_entitlement_actions:
    # required
    rover_entitlement_id: "ocid1.roverentitlement.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
rover_entitlement:
    description:
        - Details of the RoverEntitlement resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        tenant_id:
            description:
                - tenant Id.
            returned: on success
            type: str
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - A property that can uniquely identify the rover entitlement.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment Id for the entitlement.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        requestor_name:
            description:
                - Requestor name for the entitlement.
            returned: on success
            type: str
            sample: requestor_name_example
        requestor_email:
            description:
                - Requestor email for the entitlement.
            returned: on success
            type: str
            sample: requestor_email_example
        lifecycle_state:
            description:
                - Lifecyclestate for the entitlement.
            returned: on success
            type: str
            sample: CREATING
        entitlement_details:
            description:
                - Details about the entitlement.
            returned: on success
            type: str
            sample: entitlement_details_example
        lifecycle_state_details:
            description:
                - A property that can contain details on the lifecycle.
            returned: on success
            type: str
            sample: lifecycle_state_details_example
        time_created:
            description:
                - Time of creation for the entitlement.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time when the entitlement was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "requestor_name": "requestor_name_example",
        "requestor_email": "requestor_email_example",
        "lifecycle_state": "CREATING",
        "entitlement_details": "entitlement_details_example",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.rover import RoverEntitlementClient
    from oci.rover.models import ChangeRoverEntitlementCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverEntitlementActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "rover_entitlement_id"

    def get_module_resource_id(self):
        return self.module.params.get("rover_entitlement_id")

    def get_get_fn(self):
        return self.client.get_rover_entitlement

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_entitlement,
            rover_entitlement_id=self.module.params.get("rover_entitlement_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRoverEntitlementCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_rover_entitlement_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_entitlement_id=self.module.params.get("rover_entitlement_id"),
                change_rover_entitlement_compartment_details=action_details,
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


RoverEntitlementActionsHelperCustom = get_custom_class(
    "RoverEntitlementActionsHelperCustom"
)


class ResourceHelper(
    RoverEntitlementActionsHelperCustom, RoverEntitlementActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            rover_entitlement_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rover_entitlement",
        service_client_class=RoverEntitlementClient,
        namespace="rover",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
