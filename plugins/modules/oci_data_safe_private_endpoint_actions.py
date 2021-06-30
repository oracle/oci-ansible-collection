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
module: oci_data_safe_private_endpoint_actions
short_description: Perform actions on a DataSafePrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataSafePrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the Data Safe private endpoint and its dependent resources to the specified compartment.
version_added: "2.9"
author: Oracle (@oracle)
options:
    data_safe_private_endpoint_id:
        description:
            - The OCID of the private endpoint.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the new compartment.
        type: str
    action:
        description:
            - The action to perform on the DataSafePrivateEndpoint.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on data_safe_private_endpoint
  oci_data_safe_private_endpoint_actions:
    data_safe_private_endpoint_id: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
data_safe_private_endpoint:
    description:
        - Details of the DataSafePrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Data Safe private endpoint.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the private endpoint.
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: string
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet.
            returned: on success
            type: string
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_id:
            description:
                - The OCID of the underlying private endpoint.
            returned: on success
            type: string
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_ip:
            description:
                - The private IP address of the private endpoint.
            returned: on success
            type: string
            sample: private_endpoint_ip_example
        endpoint_fqdn:
            description:
                - The three-label fully qualified domain name (FQDN) of the private endpoint. The customer VCN's DNS records are updated with this FQDN.
            returned: on success
            type: string
            sample: endpoint_fqdn_example
        description:
            description:
                - The description of the private endpoint.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - The date and time the private endpoint was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the private endpoint.
            returned: on success
            type: string
            sample: CREATING
        nsg_ids:
            description:
                - The OCIDs of the network security groups that the private endpoint belongs to.
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_ip": "private_endpoint_ip_example",
        "endpoint_fqdn": "endpoint_fqdn_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "nsg_ids": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import ChangeDataSafePrivateEndpointCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafePrivateEndpointActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "data_safe_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_safe_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_data_safe_private_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_safe_private_endpoint,
            data_safe_private_endpoint_id=self.module.params.get(
                "data_safe_private_endpoint_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDataSafePrivateEndpointCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_data_safe_private_endpoint_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_safe_private_endpoint_id=self.module.params.get(
                    "data_safe_private_endpoint_id"
                ),
                change_data_safe_private_endpoint_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafePrivateEndpointActionsHelperCustom = get_custom_class(
    "DataSafePrivateEndpointActionsHelperCustom"
)


class ResourceHelper(
    DataSafePrivateEndpointActionsHelperCustom, DataSafePrivateEndpointActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            data_safe_private_endpoint_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_safe_private_endpoint",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
