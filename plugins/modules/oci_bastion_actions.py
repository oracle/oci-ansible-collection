#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_bastion_actions
short_description: Perform actions on a Bastion resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Bastion resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a bastion into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bastion_id:
        description:
            - The unique identifier (OCID) of the bastion.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment that the bastion should move to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Bastion.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on bastion
  oci_bastion_actions:
    # required
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
bastion:
    description:
        - Details of the Bastion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        bastion_type:
            description:
                - The type of bastion.
            returned: on success
            type: str
            sample: bastion_type_example
        id:
            description:
                - The unique identifier (OCID) of the bastion, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the bastion, which can't be changed after creation.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The unique identifier (OCID) of the compartment where the bastion is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        target_vcn_id:
            description:
                - The unique identifier (OCID) of the virtual cloud network (VCN) that the bastion connects to.
            returned: on success
            type: str
            sample: "ocid1.targetvcn.oc1..xxxxxxEXAMPLExxxxxx"
        target_subnet_id:
            description:
                - The unique identifier (OCID) of the subnet that the bastion connects to.
            returned: on success
            type: str
            sample: "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        phone_book_entry:
            description:
                - The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.
            returned: on success
            type: str
            sample: phone_book_entry_example
        client_cidr_block_allow_list:
            description:
                - A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.
            returned: on success
            type: list
            sample: []
        static_jump_host_ip_addresses:
            description:
                - A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.
            returned: on success
            type: list
            sample: []
        private_endpoint_ip_address:
            description:
                - The private IP address of the created private endpoint.
            returned: on success
            type: str
            sample: private_endpoint_ip_address_example
        max_session_ttl_in_seconds:
            description:
                - The maximum amount of time that any session on the bastion can remain active.
            returned: on success
            type: int
            sample: 56
        max_sessions_allowed:
            description:
                - The maximum number of active sessions allowed on the bastion.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The time the bastion was created. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the bastion was updated. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the bastion.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
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
        "bastion_type": "bastion_type_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_vcn_id": "ocid1.targetvcn.oc1..xxxxxxEXAMPLExxxxxx",
        "target_subnet_id": "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "phone_book_entry": "phone_book_entry_example",
        "client_cidr_block_allow_list": [],
        "static_jump_host_ip_addresses": [],
        "private_endpoint_ip_address": "private_endpoint_ip_address_example",
        "max_session_ttl_in_seconds": 56,
        "max_sessions_allowed": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
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
    from oci.bastion import BastionClient
    from oci.bastion.models import ChangeBastionCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BastionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "bastion_id"

    def get_module_resource_id(self):
        return self.module.params.get("bastion_id")

    def get_get_fn(self):
        return self.client.get_bastion

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bastion, bastion_id=self.module.params.get("bastion_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeBastionCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_bastion_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bastion_id=self.module.params.get("bastion_id"),
                change_bastion_compartment_details=action_details,
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


BastionActionsHelperCustom = get_custom_class("BastionActionsHelperCustom")


class ResourceHelper(BastionActionsHelperCustom, BastionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            bastion_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bastion",
        service_client_class=BastionClient,
        namespace="bastion",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
