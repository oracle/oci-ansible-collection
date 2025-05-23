#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_network_route_table
short_description: Manage a RouteTable resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RouteTable resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new route table for the specified VCN. In the request you must also include at least one route
      rule for the new route table. For information on the number of rules you can have in a route table, see
      L(Service Limits,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). For general information about route
      tables in your VCN and the types of targets you can use in route rules,
      see L(Route Tables,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
      compartment where you want the route
      table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,
      or other Networking Service components. If you're not sure which compartment to use, put the route
      table in the same compartment as the VCN. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the route table, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_route_table_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the route table.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the route table belongs to.
            - Required for create using I(state=present).
        type: str
    purge_route_rules:
        description:
            - Purge route rules from route table which are not present in the provided route table.
              If I(purge_route_rules=no), provided route rules would be appended to existing route
              rules. I(purge_route_rules) and I(delete_route_rules) are mutually exclusive.
            - This parameter is updatable.
        type: bool
        default: "true"
    delete_route_rules:
        description:
            - Delete route rules from existing route table which are present in the
              route rules provided by I(route_rules). If I(delete_route_rules=yes), route rules provided by
              I(route_rules) would be deleted, if they are part of existing route table. If they are not
              part of existing route table, they will be ignored. I(purge_route_rules) and I(delete_route_rules)
              are mutually exclusive.
            - This parameter is updatable.
        type: bool
        default: "false"
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
    route_rules:
        description:
            - The collection of rules used for routing destination IPs to network devices.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            cidr_block:
                description:
                    - Deprecated. Instead use `destination` and `destinationType`. Requests that include both
                      `cidrBlock` and `destination` will be rejected.
                    - A destination IP address range in CIDR notation. Matching packets will
                      be routed to the indicated network entity (the target).
                    - Cannot be an IPv6 prefix.
                    - "Example: `0.0.0.0/0`"
                type: str
            destination:
                description:
                    - Conceptually, this is the range of IP addresses used for matching when routing
                      traffic. Required if you provide a `destinationType`.
                    - "Allowed values:"
                    - " * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24`
                        or `2001:0db8:0123:45::/56`. If you set this to an IPv6 prefix, the route rule's target
                        can only be a DRG or internet gateway.
                        IPv6 addressing is supported for all commercial and government regions.
                        See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                    - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                          setting up a route rule for traffic destined for a particular `Service` through
                          a service gateway. For example: `oci-phx-objectstorage`."
                type: str
            destination_type:
                description:
                    - Type of destination for the rule. Required if you provide a `destination`.
                    - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                    - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                          L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                          particular `Service` through a service gateway)."
                type: str
                choices:
                    - "CIDR_BLOCK"
                    - "SERVICE_CIDR_BLOCK"
            network_entity_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the route rule's target. For information about
                      the type of
                      targets you can specify, see
                      L(Route Tables,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).
                type: str
                required: true
            description:
                description:
                    - An optional description of your choice for the rule.
                type: str
            route_type:
                description:
                    - A route rule can be STATIC if manually added to the route table, LOCAL if added by OCI to the route table.
                type: str
                choices:
                    - "STATIC"
                    - "LOCAL"
    rt_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RouteTable.
            - Use I(state=present) to create or update a RouteTable.
            - Use I(state=absent) to delete a RouteTable.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create route_table
  oci_network_route_table:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    route_rules:
    - # required
      network_entity_id: "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      cidr_block: cidr_block_example
      destination: destination_example
      destination_type: CIDR_BLOCK
      description: description_example
      route_type: STATIC

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update route_table
  oci_network_route_table:
    # required
    rt_id: "ocid1.rt.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    purge_route_rules: false
    delete_route_rules: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    route_rules:
    - # required
      network_entity_id: "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      cidr_block: cidr_block_example
      destination: destination_example
      destination_type: CIDR_BLOCK
      description: description_example
      route_type: STATIC

- name: Update route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_route_table:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    purge_route_rules: false
    delete_route_rules: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    route_rules:
    - # required
      network_entity_id: "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      cidr_block: cidr_block_example
      destination: destination_example
      destination_type: CIDR_BLOCK
      description: description_example
      route_type: STATIC

- name: Delete route_table
  oci_network_route_table:
    # required
    rt_id: "ocid1.rt.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_route_table:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
route_table:
    description:
        - Details of the RouteTable resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the route table.
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
                - The route table's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The route table's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        route_rules:
            description:
                - The collection of rules for routing destination IPs to network devices.
            returned: on success
            type: complex
            contains:
                cidr_block:
                    description:
                        - Deprecated. Instead use `destination` and `destinationType`. Requests that include both
                          `cidrBlock` and `destination` will be rejected.
                        - A destination IP address range in CIDR notation. Matching packets will
                          be routed to the indicated network entity (the target).
                        - Cannot be an IPv6 prefix.
                        - "Example: `0.0.0.0/0`"
                    returned: on success
                    type: str
                    sample: cidr_block_example
                destination:
                    description:
                        - Conceptually, this is the range of IP addresses used for matching when routing
                          traffic. Required if you provide a `destinationType`.
                        - "Allowed values:"
                        - " * IP address range in CIDR notation. Can be an IPv4 CIDR block or IPv6 prefix. For example: `192.168.1.0/24`
                            or `2001:0db8:0123:45::/56`. If you set this to an IPv6 prefix, the route rule's target
                            can only be a DRG or internet gateway.
                            IPv6 addressing is supported for all commercial and government regions.
                            See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                              setting up a route rule for traffic destined for a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                    returned: on success
                    type: str
                    sample: destination_example
                destination_type:
                    description:
                        - Type of destination for the rule. Required if you provide a `destination`.
                        - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                              particular `Service` through a service gateway)."
                    returned: on success
                    type: str
                    sample: CIDR_BLOCK
                network_entity_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the route rule's target. For information
                          about the type of
                          targets you can specify, see
                          L(Route Tables,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx"
                description:
                    description:
                        - An optional description of your choice for the rule.
                    returned: on success
                    type: str
                    sample: description_example
                route_type:
                    description:
                        - A route rule can be STATIC if manually added to the route table, LOCAL if added by OCI to the route table.
                    returned: on success
                    type: str
                    sample: STATIC
        time_created:
            description:
                - The date and time the route table was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the route table list belongs to.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "route_rules": [{
            "cidr_block": "cidr_block_example",
            "destination": "destination_example",
            "destination_type": "CIDR_BLOCK",
            "network_entity_id": "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx",
            "description": "description_example",
            "route_type": "STATIC"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateRouteTableDetails
    from oci.core.models import UpdateRouteTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RouteTableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RouteTableHelperGen, self).get_possible_entity_types() + [
            "routetable",
            "routetables",
            "coreroutetable",
            "coreroutetables",
            "routetableresource",
            "routetablesresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "rt_id"

    def get_module_resource_id(self):
        return self.module.params.get("rt_id")

    def get_get_fn(self):
        return self.client.get_route_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_route_table, rt_id=self.module.params.get("rt_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vcn_id", "display_name"]

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
            self.client.list_route_tables, **kwargs
        )

    def get_create_model_class(self):
        return CreateRouteTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(create_route_table_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRouteTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rt_id=self.module.params.get("rt_id"),
                update_route_table_details=update_details,
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
            call_fn=self.client.delete_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(rt_id=self.module.params.get("rt_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RouteTableHelperCustom = get_custom_class("RouteTableHelperCustom")


class ResourceHelper(RouteTableHelperCustom, RouteTableHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            purge_route_rules=dict(type="bool", default="true"),
            delete_route_rules=dict(type="bool", default="false"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            route_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    cidr_block=dict(type="str"),
                    destination=dict(type="str"),
                    destination_type=dict(
                        type="str", choices=["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
                    ),
                    network_entity_id=dict(type="str", required=True),
                    description=dict(type="str"),
                    route_type=dict(type="str", choices=["STATIC", "LOCAL"]),
                ),
            ),
            rt_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="route_table",
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
