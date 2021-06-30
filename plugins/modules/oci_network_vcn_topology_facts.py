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
module: oci_network_vcn_topology_facts
short_description: Fetches details about a VcnTopology resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a VcnTopology resource in Oracle Cloud Infrastructure
    - Gets a virtual network topology for a given VCN.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
        required: true
    access_level:
        description:
            - Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`.
              Setting this to `ACCESSIBLE` returns only compartments for which a
              user has INSPECT permissions, either directly or indirectly (permissions can be on a
              resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has
              indirect INSPECT permissions.
            - When set to `ANY` permissions are not checked.
        type: str
        choices:
            - "ANY"
            - "ACCESSIBLE"
    query_compartment_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed
              and the specified compartment and its subcompartments are
              inspected depending on the the setting of `accessLevel`.
              Default is false.
        type: bool
    cache_control:
        description:
            - The Cache-Control HTTP header holds directives (instructions)
              for caching in both requests and responses.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vcn_topology
  oci_network_vcn_topology_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
vcn_topology:
    description:
        - VcnTopology resource
    returned: on success
    type: complex
    contains:
        type:
            description:
                - Type of the topology object.
            returned: on success
            type: string
            sample: NETWORKING
        entities:
            description:
                - Lists entities comprising the virtual network topology.
            returned: on success
            type: list
            sample: []
        relationships:
            description:
                - Lists relationships between entities in the virtual network topology.
            returned: on success
            type: complex
            contains:
                id1:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the first entity in the relationship.
                    returned: on success
                    type: string
                    sample: id1_example
                id2:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the second entity in the relationship.
                    returned: on success
                    type: string
                    sample: id2_example
                type:
                    description:
                        - The type of relationship between the entities.
                    returned: on success
                    type: string
                    sample: ROUTES_TO
                route_rule_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        destination_type:
                            description:
                                - "The destinationType can be set to one of two values:"
                                - "* Use `CIDR_BLOCK` if the rule's `destination` is an IP address range in CIDR notation."
                                - "* Use `SERVICE_CIDR_BLOCK` if the rule's `destination` is the `cidrBlock` value for a
                                  L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/)."
                            returned: on success
                            type: string
                            sample: destination_type_example
                        destination:
                            description:
                                - An IP address range in CIDR notation or the `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/iaas/latest/Service/).
                            returned: on success
                            type: string
                            sample: destination_example
                        route_table_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the routing table that contains the
                                  route rule.
                            returned: on success
                            type: string
                            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Records when the virtual network topology was created, in L(RFC3339,https://tools.ietf.org/html/rfc3339) format for date and time.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN for which the topology is generated.
            returned: on success
            type: string
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "type": "NETWORKING",
        "entities": [],
        "relationships": [{
            "id1": "id1_example",
            "id2": "id2_example",
            "type": "ROUTES_TO",
            "route_rule_details": {
                "destination_type": "destination_type_example",
                "destination": "destination_example",
                "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
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


class VcnTopologyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "vcn_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "access_level",
            "query_compartment_subtree",
            "cache_control",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_vcn_topology,
            compartment_id=self.module.params.get("compartment_id"),
            vcn_id=self.module.params.get("vcn_id"),
            **optional_kwargs
        )


VcnTopologyFactsHelperCustom = get_custom_class("VcnTopologyFactsHelperCustom")


class ResourceFactsHelper(VcnTopologyFactsHelperCustom, VcnTopologyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            vcn_id=dict(type="str", required=True),
            access_level=dict(type="str", choices=["ANY", "ACCESSIBLE"]),
            query_compartment_subtree=dict(type="bool"),
            cache_control=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vcn_topology",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vcn_topology=result)


if __name__ == "__main__":
    main()
