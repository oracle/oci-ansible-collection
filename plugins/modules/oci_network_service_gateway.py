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
module: oci_network_service_gateway
short_description: Manage a ServiceGateway resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ServiceGateway resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new service gateway in the specified compartment.
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
      compartment where you want
      the service gateway to reside. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the service gateway, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_service_gateway_actions) module: attach_service_id, change_compartment,
      detach_service_id."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID],https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to contain the service gateway.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table the service gateway will use.
            - If you don't specify a route table here, the service gateway is created without an associated route
              table. The Networking service does NOT automatically associate the attached VCN's default route table
              with the service gateway.
            - "For information about why you would associate a route table with a service gateway, see
              L(Transit Routing: Private Access to Oracle Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)."
            - This parameter is updatable.
        type: str
    services:
        description:
            - List of the OCIDs of the L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) objects to
              enable for the service gateway. This list can be empty if you don't want to enable any
              `Service` objects when you create the gateway. You can enable a `Service`
              object later by using either L(AttachServiceId,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ServiceGateway/AttachServiceId)
              or L(UpdateServiceGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway).
            - For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock`
              as the rule's destination and the service gateway as the rule's target. See
              L(Route Table,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/RouteTable/).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            service_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(Service,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/latest/Service/).
                type: str
                required: true
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
            - Required for create using I(state=present).
        type: str
    service_gateway_id:
        description:
            - The service gateway's L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    block_traffic:
        description:
            - Whether the service gateway blocks all traffic through it. The default is `false`. When
              this is `true`, traffic is not routed to any services, regardless of route rules.
            - "Example: `true`"
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the ServiceGateway.
            - Use I(state=present) to create or update a ServiceGateway.
            - Use I(state=absent) to delete a ServiceGateway.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create service_gateway
  oci_network_service_gateway:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    services:
    - # required
      service_id: "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update service_gateway
  oci_network_service_gateway:
    # required
    service_gateway_id: "ocid1.servicegateway.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
    services:
    - # required
      service_id: "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx"
    block_traffic: true

- name: Update service_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_service_gateway:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
    services:
    - # required
      service_id: "ocid1.service.oc1..xxxxxxEXAMPLExxxxxx"
    block_traffic: true

- name: Delete service_gateway
  oci_network_service_gateway:
    # required
    service_gateway_id: "ocid1.servicegateway.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete service_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_service_gateway:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
            sample: "2016-08-25T21:10:29.600Z"
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
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateServiceGatewayDetails
    from oci.core.models import UpdateServiceGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceGatewayHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vcn_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_service_gateways, **kwargs
        )

    def get_create_model_class(self):
        return CreateServiceGatewayDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_service_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(create_service_gateway_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateServiceGatewayDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_service_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_gateway_id=self.module.params.get("service_gateway_id"),
                update_service_gateway_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_service_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_gateway_id=self.module.params.get("service_gateway_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ServiceGatewayHelperCustom = get_custom_class("ServiceGatewayHelperCustom")


class ResourceHelper(ServiceGatewayHelperCustom, ServiceGatewayHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            route_table_id=dict(type="str"),
            services=dict(
                type="list",
                elements="dict",
                options=dict(service_id=dict(type="str", required=True)),
            ),
            vcn_id=dict(type="str"),
            service_gateway_id=dict(aliases=["id"], type="str"),
            block_traffic=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
