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
module: oci_data_connectivity_test_network_connectivity_actions
short_description: Perform actions on a TestNetworkConnectivity resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TestNetworkConnectivity resource in Oracle Cloud Infrastructure
    - For I(action=create), execute network validation on the selected data assets associated with the provided private endpoint.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
        type: str
        aliases: ["id"]
        required: true
    data_asset_key:
        description:
            - Data Asset key
        type: str
        required: true
    endpoint_id:
        description:
            - Endpoint ID used for getDataAssetFullDetails.
        type: str
    action:
        description:
            - The action to perform on the TestNetworkConnectivity.
        type: str
        required: true
        choices:
            - "create"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action create on test_network_connectivity
  oci_data_connectivity_test_network_connectivity_actions:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: create

    # optional
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
test_network_connectivity:
    description:
        - Details of the TestNetworkConnectivity resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        network_validation_output:
            description:
                - Last line from network validation command execution output.
            returned: on success
            type: str
            sample: network_validation_output_example
        is_reachable:
            description:
                - True if the data asset has a valid network path.
            returned: on success
            type: bool
            sample: true
        exception_message:
            description:
                - Exception or error message encountered while testing network reachability for the data asset.
            returned: on success
            type: str
            sample: exception_message_example
    sample: {
        "network_validation_output": "network_validation_output_example",
        "is_reachable": true,
        "exception_message": "exception_message_example"
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
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import CreateTestNetworkConnectivityDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TestNetworkConnectivityActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        create
    """

    @staticmethod
    def get_module_resource_id_param():
        return "registry_id"

    def get_module_resource_id(self):
        return self.module.params.get("registry_id")

    def create(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateTestNetworkConnectivityDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_test_network_connectivity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                create_test_network_connectivity_details=action_details,
                endpoint_id=self.module.params.get("endpoint_id"),
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


TestNetworkConnectivityActionsHelperCustom = get_custom_class(
    "TestNetworkConnectivityActionsHelperCustom"
)


class ResourceHelper(
    TestNetworkConnectivityActionsHelperCustom, TestNetworkConnectivityActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            registry_id=dict(aliases=["id"], type="str", required=True),
            data_asset_key=dict(type="str", required=True, no_log=True),
            endpoint_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["create"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="test_network_connectivity",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
