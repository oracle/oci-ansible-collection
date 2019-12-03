#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_route_table
short_description: Create,update and delete OCI Route Table
description:
    - Creates OCI Route Table
    - Update OCI Route Table, if present, with a new display name
    - Update OCI Route Table, if present, by appending new Route Rules to existing Route Rules
    - Update OCI Route Table, if present, by purging existing Route Rules and replacing them with
      specified ones
    - Delete OCI Route Table, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this
                     Route Table would be created. Mandatory for create
                     operation.Optional for delete and update. Mutually exclusive
                     with rt_id.
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the
                     Route Table should be attached. Mandatory for create
                     operation. Optional for delete and update. Mutually exclusive
                     with rt_id.
        required: false
    rt_id:
        description: Identifier of the Route Table. Mandatory for delete and update,
                     if compartment_id and vcn_id is not specified. Mutually exclusive
                     with compartment_id and vcn_id.
        required: false
        aliases: ['id']
    display_name:
        description: Name of the Route Table. A user friendly name. Does not have to be unique,
                     and could be changed. If not specified, a default name would be provided.
        aliases: ['name']
        required: false
    route_rules:
        description: List containing dictionaries describing a route rule. Suboptions should be
                     the CIDR block which is destination ip address in CIDR notation and the
                     identifier of the target entity such as Internet Getway.
        required: false
        suboptions:
            cidr_block:
                description: A destination IP address range in CIDR notation. Matching packets
                             will be routed to the indicated network entity (the target). This
                             option is deprecated, use destination and destination_type instead.
                required: false
            destination:
                description: Conceptually, this is the range of IP addresses used for matching when
                             routing traffic. Required if you provide a destination_type. Allowed
                             values are, IP address range in CIDR notation (For example, 192.168.1.0/24)
                             or The cidr_block value for a service, if you're setting up a route rule for
                             traffic destined for a particular service through a service gateway
                             (For example, oci-phx-objectstorage).

                required: false
            destination_type:
                description: Type of destination for the rule. Required if you provide a destination. If the
                             rule's destination is an IP address range in CIDR notation, the value should be
                             CIDR_BLOCK.If the rule's destination is the cidr_block value for a service, the
                             value should be SERVICE_CIDR_BLOCK.
                required: false
                choices: ['CIDR_BLOCK', 'SERVICE_CIDR_BLOCK']
            network_entity_id:
                description: The identifier for the target of route rules, such as identifier
                             of the Internet Gateway or Service Gateway.
                required: true
    purge_route_rules:
        description: Purge route rules in existing Route Table which are not present in the provided
                     Route Rules. If I(purge_route_rules=no), provided route rules would be
                     appended to existing route rules. I(purge_route_rules) and I(delete_route_rules)
                     are mutually exclusive.
        required: false
        default: 'yes'
        type: bool
    delete_route_rules:
        description: Delete route rules in existing Route Table which are present in the provided
                     Route Rules. If I(delete_route_rules=yes), route rules provided by I(route_rules)
                     would be deleted from existing route rules, if they are part of existing route rules. If
                     they are not part of existing route rules, they will be ignored. I(delete_route_rules)
                     and I(purge_route_rules) are mutually exclusive.
        required: false
        default: 'no'
        type: bool
    state:
        description: Create,update or delete Route Table. For I(state=present), if it
                     does not exist, it gets created. If it exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create/update Route Table
- name: Create a Route Table with a route rule
  oci_route_table:
    compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
    vcn_id: 'ocid1.vcn..xxxxxEXAMPLExxxxx'
    name: 'ansible_route_table'
    route_rules:
        - cidr_block: '10.0.0.0/8'
          network_entity_id: 'ocid1.internetgateway..xxxxxEXAMPLExxxxx'
        - destination: 'oci-phx-objectstorage'
          destination_type: 'SERVICE_CIDR_BLOCK'
          network_entity_id: 'ocid1.servicegateway..xxxxxEXAMPLExxxxx'
    freeform_tags:
        region: 'east'
    defined_tags:
        features:
           capacity: 'medium'
    state: 'present'

# Update Route Table with rt id
- name: Update the display name of a Route Table
  oci_route_table:
    rt_id: 'ocid1.routetable..xxxxxEXAMPLExxxxx'
    display_name: 'ansible_route_table_updated'
    state: 'present'

# Update a route table with a new set of route rules,
# and purge any existing route rules that is not in the
# specified set of route rules.
- name: Update a Route Table with purge route rules
  oci_route_table:
    rt_id: 'ocid1.routetable..xxxxxEXAMPLExxxxx'
    purge_route_rules: 'yes'
    route_rules:
        - cidr_block: '10.0.0.0/12'
          network_entity_id: 'ocid1.internetgateway..abcd'
    state: 'present'

- name: Update a Route Table by deleting route rules
  oci_route_table:
    rt_id: 'ocid1.routetable..xxxxxEXAMPLExxxxx'
    delete_route_rules: 'yes'
    route_rules:
        - cidr_block: '10.0.0.0/12'
          network_entity_id: 'ocid1.internetgateway..abcd'
    state: 'present'

# Delete Route Table
- name: Delete Route Table
  oci_route_table:
    rt_id: 'ocid1.routetable..xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    route_table:
        description: Attributes of the created/updated Route Table.
                    For delete, deleted Route Table description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Route Table
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Route Table during creation
                returned: always
                type: string
                sample: ansible_route_table
            id:
                description: Identifier of the Route Table
                returned: always
                type: string
                sample: ocid1.routetable.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Route Table is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Route Table
                returned: always
                type: string
                sample: AVAILABLE
            route_rules:
                description: The collection of rules for routing destination IPs to network devices.
                returned: always
                type: string
                sample: [{'cidr_block': '0.0.0.0/0', 'destination': '0.0.0.0', 'destination_type': 'CIDR_BLOCK',
                    'network_entity_id': 'ocid1.internetgateway.xxxxxEXAMPLExxxxx'}]
            time_created:
                description: Date and time when the Route Table was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"east"},
                    "defined_tags":{"features":{"capacity":"medium"}},
                    "display_name":"ansible_route_table",
                    "id":"ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "route_rules":[
                                    {
                                        "cidr_block":"0.0.0.0/0",
                                        "destination": "0.0.0.0",
                                        "destination_type": "CIDR_BLOCK",
                                        "network_entity_id":"ocid1.internetgateway.oc1.phx.xxxxxEXAMPLExxxxx"
                                    },
                                    {
                                        "cidr_block": null,
                                        "destination": "oci-phx-objectstorage",
                                        "destination_type": "SERVICE_CIDR_BLOCK",
                                        "network_entity_id":"ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx"
                                    }
                                ],
                    "time_created":"2017-11-17T17:39:33.190000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                }

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded, ClientError
    from oci.util import to_dict
    from oci.core.models import (
        CreateRouteTableDetails,
        RouteRule,
        UpdateRouteTableDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_route_table(virtual_network_client, module):
    result = dict(changed=False, route_table="")
    rt_id = module.params.get("rt_id")
    exclude_attributes = {"display_name": True}
    try:
        if rt_id:
            existing_route_table = oci_utils.get_existing_resource(
                virtual_network_client.get_route_table, module, rt_id=rt_id
            )
            result = update_route_table(
                virtual_network_client, existing_route_table, module
            )
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="route_table",
                create_fn=create_route_table,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_route_tables,
                kwargs_list={
                    "compartment_id": module.params.get("compartment_id"),
                    "vcn_id": module.params.get("vcn_id"),
                },
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateRouteTableDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def create_route_table(virtual_network_client, module):
    route_rules = []
    input_route_rules = module.params["route_rules"]
    if input_route_rules:
        route_rules = get_route_rules(input_route_rules)
    create_route_table_details = CreateRouteTableDetails()
    for attribute in create_route_table_details.attribute_map:
        create_route_table_details.__setattr__(attribute, module.params.get(attribute))
    create_route_table_details.route_rules = route_rules
    result = oci_utils.create_and_wait(
        resource_type="route_table",
        create_fn=virtual_network_client.create_route_table,
        kwargs_create={"create_route_table_details": create_route_table_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_route_table,
        get_param="rt_id",
        module=module,
    )
    return result


def get_route_rules(input_route_rules):
    route_rules = []
    for route_rule_dict in input_route_rules:
        route_rule = RouteRule()
        for attribute in route_rule.attribute_map:
            route_rule.__setattr__(attribute, route_rule_dict.get(attribute))

        # This is a temporary fix till deprecated cidr_block parameter gets removed.
        # Right now, the value of cidr_block gets updated in destination but reverse is not true
        # after route rule gets created. This causes problem in idempotency. So performing the same
        # while creating input route table.
        if route_rule_dict.get("destination") is None:
            route_rule.__setattr__("destination", route_rule_dict.get("cidr_block"))

        if route_rule_dict.get("destination_type") is None:
            route_rule.__setattr__(
                "destination_type", RouteRule.DESTINATION_TYPE_CIDR_BLOCK
            )

        route_rules.append(route_rule)
    return route_rules


def update_route_table(virtual_network_client, existing_route_table, module):
    if existing_route_table is None:
        raise ClientError(
            Exception(
                "No Route Table with id "
                + module.params.get("rt_id")
                + " is found for update"
            )
        )
    result = dict(route_table=to_dict(existing_route_table), changed=False)
    input_route_rules = module.params.get("route_rules")
    purge_route_rules = module.params["purge_route_rules"]
    delete_route_rules = module.params["delete_route_rules"]
    name_tag_changed = False
    route_rules_changed = False
    existing_route_rules = existing_route_table.route_rules
    update_route_table_details = UpdateRouteTableDetails()
    attributes_to_compare = ["display_name", "freeform_tags", "defined_tags"]
    for attribute in attributes_to_compare:
        name_tag_changed = oci_utils.check_and_update_attributes(
            update_route_table_details,
            attribute,
            module.params.get(attribute),
            getattr(existing_route_table, attribute),
            name_tag_changed,
        )
    if input_route_rules is not None:
        if input_route_rules:
            route_rules_object_list = get_route_rules(input_route_rules)
            route_rules, route_rules_changed = oci_utils.get_component_list_difference(
                get_hashed_route_rules(route_rules_object_list),
                get_hashed_route_rules(existing_route_rules),
                purge_route_rules,
                delete_route_rules,
            )
        else:
            route_rules = []
            route_rules_changed = True
    if route_rules_changed:
        update_route_table_details.route_rules = route_rules
    else:
        update_route_table_details.route_rules = existing_route_rules

    if name_tag_changed or route_rules_changed:
        result = oci_utils.update_and_wait(
            resource_type="route_table",
            update_fn=virtual_network_client.update_route_table,
            kwargs_update={
                "rt_id": existing_route_table.id,
                "update_route_table_details": update_route_table_details,
            },
            client=virtual_network_client,
            get_fn=virtual_network_client.get_route_table,
            get_param="rt_id",
            module=module,
        )

    return result


def get_hashed_route_rules(route_rules):
    route_rules_reprs = []
    supported_route_rule_attributes = [
        "cidr_block",
        "destination",
        "destination_type",
        "network_entity_id",
    ]
    for route_rule in route_rules:
        hashed_route_rule = oci_utils.get_hashed_object(
            RouteRule, route_rule, supported_attributes=supported_route_rule_attributes
        )
        route_rules_reprs.append(hashed_route_rule)
    return route_rules_reprs


def delete_route_table(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="route_table",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_route_table,
        kwargs_get={"rt_id": module.params["rt_id"]},
        delete_fn=virtual_network_client.delete_route_table,
        kwargs_delete={"rt_id": module.params["rt_id"]},
        module=module,
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        compartment_id=dict(type="str", required=False),
        display_name=dict(type="str", required=False, aliases=["name"]),
        vcn_id=dict(type="str", required=False),
        rt_id=dict(type="str", required=False, aliases=["id"]),
        state=dict(
            type="str", required=False, default="present", choices=["present", "absent"]
        ),
        route_rules=dict(type=list, required=False),
        purge_route_rules=dict(type="bool", required=False, default=True),
        delete_route_rules=dict(type="bool", required=False, default=False),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_route_rules", "delete_route_rules"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]

    if state == "present":
        result = create_or_update_route_table(virtual_network_client, module)
    elif state == "absent":
        result = delete_route_table(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
