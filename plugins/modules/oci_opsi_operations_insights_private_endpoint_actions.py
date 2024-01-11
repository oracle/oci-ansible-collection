#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_opsi_operations_insights_private_endpoint_actions
short_description: Perform actions on an OperationsInsightsPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OperationsInsightsPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a private endpoint from one compartment to another. When provided, If-Match is checked against ETag values of the
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operations_insights_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Operation Insights private endpoint.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The new compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Private service accessed database.
        type: str
    action:
        description:
            - The action to perform on the OperationsInsightsPrivateEndpoint.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on operations_insights_private_endpoint
  oci_opsi_operations_insights_private_endpoint_actions:
    # required
    operations_insights_private_endpoint_id: "ocid1.operationsinsightsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
operations_insights_private_endpoint:
    description:
        - Details of the OperationsInsightsPrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Private service accessed database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the private endpoint.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The compartment OCID of the Private service accessed database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_ip:
            description:
                - The private IP addresses assigned to the private endpoint. All IP addresses will be concatenated if it is RAC DBs.
            returned: on success
            type: str
            sample: private_ip_example
        description:
            description:
                - The description of the private endpoint.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the private endpoint was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the private endpoint.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        private_endpoint_status_details:
            description:
                - A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable
                  information about the validity of the private endpoint connection.
            returned: on success
            type: str
            sample: private_endpoint_status_details_example
        is_used_for_rac_dbs:
            description:
                - The flag is to identify if private endpoint is used for rac database or not
            returned: on success
            type: bool
            sample: true
        nsg_ids:
            description:
                - The OCIDs of the network security groups that the private endpoint belongs to.
            returned: on success
            type: list
            sample: []
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_ip": "private_ip_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "private_endpoint_status_details": "private_endpoint_status_details_example",
        "is_used_for_rac_dbs": true,
        "nsg_ids": [],
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import (
        ChangeOperationsInsightsPrivateEndpointCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsPrivateEndpointActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "operations_insights_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("operations_insights_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_operations_insights_private_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_private_endpoint,
            operations_insights_private_endpoint_id=self.module.params.get(
                "operations_insights_private_endpoint_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params,
            ChangeOperationsInsightsPrivateEndpointCompartmentDetails,
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_operations_insights_private_endpoint_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_private_endpoint_id=self.module.params.get(
                    "operations_insights_private_endpoint_id"
                ),
                change_operations_insights_private_endpoint_compartment_details=action_details,
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


OperationsInsightsPrivateEndpointActionsHelperCustom = get_custom_class(
    "OperationsInsightsPrivateEndpointActionsHelperCustom"
)


class ResourceHelper(
    OperationsInsightsPrivateEndpointActionsHelperCustom,
    OperationsInsightsPrivateEndpointActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            operations_insights_private_endpoint_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="operations_insights_private_endpoint",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
