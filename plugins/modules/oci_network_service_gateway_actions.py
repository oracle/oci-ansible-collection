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
module: oci_network_service_gateway_actions
short_description: Perform actions on a ServiceGateway resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ServiceGateway resource in Oracle Cloud Infrastructure
    - "For I(action=attach_service_id), adds the specified L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) to the list of
      enabled
      `Service` objects for the specified gateway. You must also set up a route rule with the
      `cidrBlock` of the `Service` as the rule's destination and the service gateway as the rule's
      target. See L(Route Table,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/RouteTable/).
      **Note:** The `AttachServiceId` operation is an easy way to add an individual `Service` to
      the service gateway. Compare it with
      L(UpdateServiceGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway), which replaces
      the entire existing list of enabled `Service` objects with the list that you provide in the
      `Update` call."
    - For I(action=change_compartment), moves a service gateway into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - "For I(action=detach_service_id), removes the specified L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) from the list of
      enabled
      `Service` objects for the specified gateway. You do not need to remove any route
      rules that specify this `Service` object's `cidrBlock` as the destination CIDR. However, consider
      removing the rules if your intent is to permanently disable use of the `Service` through this
      service gateway.
      **Note:** The `DetachServiceId` operation is an easy way to remove an individual `Service` from
      the service gateway. Compare it with
      L(UpdateServiceGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway), which replaces
      the entire existing list of enabled `Service` objects with the list that you provide in the
      `Update` call. `UpdateServiceGateway` also lets you block all traffic through the service
      gateway without having to remove each of the individual `Service` objects."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    service_gateway_id:
        description:
            - The service gateway's L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    service_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(Service,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/iaas/latest/Service/).
            - Required for I(action=attach_service_id), I(action=detach_service_id).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              service gateway to.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the ServiceGateway.
        type: str
        required: true
        choices:
            - "attach_service_id"
            - "change_compartment"
            - "detach_service_id"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_service_id on service_gateway
  oci_network_service_gateway_actions:
    # required
    service_gateway_id: "ocid1.servicegateway.oc1..xxxxxxEXAMPLExxxxxx"
    service_id: "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_service_id

- name: Perform action change_compartment on service_gateway
  oci_network_service_gateway_actions:
    # required
    service_gateway_id: "ocid1.servicegateway.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action detach_service_id on service_gateway
  oci_network_service_gateway_actions:
    # required
    service_gateway_id: "ocid1.servicegateway.oc1..xxxxxxEXAMPLExxxxxx"
    service_id: "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_service_id

"""

RETURN = """
service_gateway:
    description:
        - Details of the ServiceGateway resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        block_traffic:
            description:
                - Whether the service gateway blocks all traffic through it. The default is `false`. When
                  this is `true`, traffic is not routed to any services, regardless of route rules.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the
                  service gateway.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service gateway.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The service gateway's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        route_table_id:
            description:
                - "The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table the service gateway is using.
                  For information about why you would associate a route table with a service gateway, see
                  L(Transit Routing: Private Access to Oracle
                  Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)."
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        services:
            description:
                - List of the L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) objects enabled for this service gateway.
                  The list can be empty. You can enable a particular `Service` by using
                  L(AttachServiceId,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ServiceGateway/AttachServiceId) or
                  L(UpdateServiceGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway).
            returned: on success
            type: complex
            contains:
                service_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service.
                    returned: on success
                    type: str
                    sample: "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx"
                service_name:
                    description:
                        - The name of the service.
                    returned: on success
                    type: str
                    sample: service_name_example
        time_created:
            description:
                - The date and time the service gateway was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the service gateway
                  belongs to.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "block_traffic": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "services": [{
            "service_id": "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx",
            "service_name": "service_name_example"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import ServiceIdRequestDetails
    from oci.core.models import ChangeServiceGatewayCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceGatewayActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_service_id
        change_compartment
        detach_service_id
    """

    @staticmethod
    def get_module_resource_id_param():
        return "service_gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("service_gateway_id")

    def get_get_fn(self):
        return self.client.get_service_gateway

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_gateway,
            service_gateway_id=self.module.params.get("service_gateway_id"),
        )

    def attach_service_id(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ServiceIdRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_service_id,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_gateway_id=self.module.params.get("service_gateway_id"),
                attach_service_details=action_details,
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
            self.module.params, ChangeServiceGatewayCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_service_gateway_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_gateway_id=self.module.params.get("service_gateway_id"),
                change_service_gateway_compartment_details=action_details,
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

    def detach_service_id(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ServiceIdRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_service_id,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_gateway_id=self.module.params.get("service_gateway_id"),
                detach_service_details=action_details,
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


ServiceGatewayActionsHelperCustom = get_custom_class(
    "ServiceGatewayActionsHelperCustom"
)


class ResourceHelper(ServiceGatewayActionsHelperCustom, ServiceGatewayActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            service_gateway_id=dict(aliases=["id"], type="str", required=True),
            service_id=dict(type="str"),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_service_id",
                    "change_compartment",
                    "detach_service_id",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="service_gateway",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
