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
module: oci_data_connectivity_endpoint_actions
short_description: Perform actions on an Endpoint resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Endpoint resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), the endpoint will be moved to the specified compartment.
    - For I(action=validate_data_asset_network_reachablity), validates the dataAsset network reachability.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier
            - Required for I(action=change_compartment).
        type: str
    endpoint_id:
        description:
            - DCMS endpoint ID.
        type: str
        aliases: ["id"]
        required: true
    registry_id:
        description:
            - DCMS registry ID
        type: str
    action:
        description:
            - The action to perform on the Endpoint.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "validate_data_asset_network_reachablity"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on endpoint
  oci_data_connectivity_endpoint_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action validate_data_asset_network_reachablity on endpoint
  oci_data_connectivity_endpoint_actions:
    # required
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"
    action: validate_data_asset_network_reachablity

    # optional
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
endpoint:
    description:
        - Details of the Endpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        vcn_id:
            description:
                - VCN OCID where the subnet resides.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - Subnet OCID of the customer connected network where, for example, the databases reside.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        dns_zones:
            description:
                - "List of DNS zones to be used by the data assets to be harvested.
                  Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com"
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - Registry description
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - The Data Connectivity Management Registry display name; registries can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Time when the Data Connectivity Management registry was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time when the Data Connectivity Management registry was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - "Lifecycle states for registries in the Data Connectivity Management Service.
                  CREATING - The resource is being created and may not be usable until the entire metadata is defined.
                  UPDATING - The resource is being updated and may not be usable until all changes are commited.
                  DELETING - The resource is being deleted and might require deep cleanup of children.
                  ACTIVE   - The resource is valid and available for access.
                  INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                           administrative reasons.
                  DELETED  - The resource has been deleted and isn't available.
                  FAILED   - The resource is in a failed state due to validation or other errors."
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        id:
            description:
                - A unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_size:
            description:
                - Endpoint size for reverse connection capacity.
            returned: on success
            type: int
            sample: 56
        nsg_ids:
            description:
                - The list of NSGs to which the private endpoint VNIC must be added.
            returned: on success
            type: list
            sample: []
    sample: {
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "dns_zones": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_size": 56,
        "nsg_ids": []
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
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import ChangeEndpointCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EndpointActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        validate_data_asset_network_reachablity
    """

    @staticmethod
    def get_module_resource_id_param():
        return "endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("endpoint_id")

    def get_get_fn(self):
        return self.client.get_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_endpoint, endpoint_id=self.module.params.get("endpoint_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeEndpointCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_endpoint_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                endpoint_id=self.module.params.get("endpoint_id"),
                change_endpoint_compartment_details=action_details,
                registry_id=self.module.params.get("registry_id"),
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

    def validate_data_asset_network_reachablity(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_data_asset_network_reachablity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                endpoint_id=self.module.params.get("endpoint_id"),
                registry_id=self.module.params.get("registry_id"),
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


EndpointActionsHelperCustom = get_custom_class("EndpointActionsHelperCustom")


class ResourceHelper(EndpointActionsHelperCustom, EndpointActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            endpoint_id=dict(aliases=["id"], type="str", required=True),
            registry_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "validate_data_asset_network_reachablity",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="endpoint",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
