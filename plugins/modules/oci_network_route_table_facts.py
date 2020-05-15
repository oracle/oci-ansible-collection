#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_network_route_table_facts
short_description: Fetches details about one or multiple RouteTable resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RouteTable resources in Oracle Cloud Infrastructure
    - Lists the route tables in the specified VCN and specified compartment. The response
      includes the default route table that automatically comes with each VCN, plus any route tables
      you've created.
    - If I(rt_id) is specified, the details of a single RouteTable will be returned.
version_added: "2.5"
options:
    rt_id:
        description:
            - The OCID of the route table.
            - Required to get a specific route_table.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple route_tables.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
            - Required to list multiple route_tables.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List route_tables
  oci_network_route_table_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific route_table
  oci_network_route_table_facts:
    rt_id: ocid1.rt.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
route_tables:
    description:
        - List of RouteTable resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the route table.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The route table's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The route table's current state.
            returned: on success
            type: string
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
                        - "Example: `0.0.0.0/0`"
                    returned: on success
                    type: string
                    sample: 0.0.0.0/0
                destination:
                    description:
                        - Conceptually, this is the range of IP addresses used for matching when routing
                          traffic. Required if you provide a `destinationType`.
                        - "Allowed values:"
                        - " * IP address range in CIDR notation. For example: `192.168.1.0/24`"
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/), if you're
                              setting up a route rule for traffic destined for a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                    returned: on success
                    type: string
                    sample: destination_example
                destination_type:
                    description:
                        - Type of destination for the rule. Required if you provide a `destination`.
                        - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/) (the rule is for traffic destined for a
                              particular `Service` through a service gateway)."
                    returned: on success
                    type: string
                    sample: CIDR_BLOCK
                network_entity_id:
                    description:
                        - The OCID for the route rule's target. For information about the type of
                          targets you can specify, see
                          L(Route Tables,https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm).
                    returned: on success
                    type: string
                    sample: ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx
                description:
                    description:
                        - An optional description of your choice for the rule.
                    returned: on success
                    type: string
                    sample: description_example
        time_created:
            description:
                - The date and time the route table was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the route table list belongs to.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "route_rules": [{
            "cidr_block": "0.0.0.0/0",
            "destination": "destination_example",
            "destination_type": "CIDR_BLOCK",
            "network_entity_id": "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx",
            "description": "description_example"
        }],
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RouteTableFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "rt_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "vcn_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_route_table, rt_id=self.module.params.get("rt_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_route_tables,
            compartment_id=self.module.params.get("compartment_id"),
            vcn_id=self.module.params.get("vcn_id"),
            **optional_kwargs
        )


RouteTableFactsHelperCustom = get_custom_class("RouteTableFactsHelperCustom")


class ResourceFactsHelper(RouteTableFactsHelperCustom, RouteTableFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            rt_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="route_table",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(route_tables=result)


if __name__ == "__main__":
    main()
