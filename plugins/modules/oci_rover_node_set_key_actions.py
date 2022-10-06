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
module: oci_rover_node_set_key_actions
short_description: Perform actions on a RoverNodeSetKey resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RoverNodeSetKey resource in Oracle Cloud Infrastructure
    - For I(action=rover_node_action_set_key), get the resource principal public key for a rover node
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_node_id:
        description:
            - Unique RoverNode identifier
        type: str
        aliases: ["id"]
        required: true
    jwt:
        description:
            - The Java Web Token which is a signature of the request that is signed with the resource's private key
              This is meant solely in the context of getRpt
        type: str
        required: true
    public_key:
        description:
            - The public key of the resource principal
        type: str
    action:
        description:
            - The action to perform on the RoverNodeSetKey.
        type: str
        required: true
        choices:
            - "rover_node_action_set_key"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action rover_node_action_set_key on rover_node_set_key
  oci_rover_node_set_key_actions:
    # required
    rover_node_id: "ocid1.rovernode.oc1..xxxxxxEXAMPLExxxxxx"
    jwt: jwt_example
    action: rover_node_action_set_key

    # optional
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."

"""

RETURN = """
rover_node_set_key:
    description:
        - Details of the RoverNodeSetKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_successful:
            description:
                - Whether the node's resource principal public key was set correctly
            returned: on success
            type: bool
            sample: true
    sample: {
        "is_successful": true
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
    from oci.rover import RoverNodeClient
    from oci.rover.models import RoverNodeActionSetKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverNodeSetKeyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        rover_node_action_set_key
    """

    @staticmethod
    def get_module_resource_id_param():
        return "rover_node_id"

    def get_module_resource_id(self):
        return self.module.params.get("rover_node_id")

    def rover_node_action_set_key(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RoverNodeActionSetKeyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rover_node_action_set_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_node_id=self.module.params.get("rover_node_id"),
                jwt=self.module.params.get("jwt"),
                rover_node_action_set_key_details=action_details,
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


RoverNodeSetKeyActionsHelperCustom = get_custom_class(
    "RoverNodeSetKeyActionsHelperCustom"
)


class ResourceHelper(
    RoverNodeSetKeyActionsHelperCustom, RoverNodeSetKeyActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            rover_node_id=dict(aliases=["id"], type="str", required=True),
            jwt=dict(type="str", required=True),
            public_key=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["rover_node_action_set_key"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rover_node_set_key",
        service_client_class=RoverNodeClient,
        namespace="rover",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
