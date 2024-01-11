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
module: oci_network_vlan_facts
short_description: Fetches details about one or multiple Vlan resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Vlan resources in Oracle Cloud Infrastructure
    - Lists the VLANs in the specified VCN and the specified compartment.
    - If I(vlan_id) is specified, the details of a single Vlan will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vlan_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
            - Required to get a specific vlan.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple vlans.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
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
            - A filter to only return resources that match the given lifecycle
              state. The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
            - "UPDATING"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vlan
  oci_network_vlan_facts:
    # required
    vlan_id: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vlans
  oci_network_vlan_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING

"""

RETURN = """
vlans:
    description:
        - List of Vlan resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The VLAN's availability domain. This attribute will be null if this is a regional VLAN
                  rather than an AD-specific VLAN.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        cidr_block:
            description:
                - The range of IPv4 addresses that will be used for layer 3 communication with
                  hosts outside the VLAN.
                - "Example: `192.168.1.0/24`"
            returned: on success
            type: str
            sample: cidr_block_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the VLAN.
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
                - The VLAN's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The VLAN's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        nsg_ids:
            description:
                - A list of the OCIDs of the network security groups (NSGs) to use with this VLAN.
                  All VNICs in the VLAN belong to these NSGs. For more
                  information about NSGs, see
                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
            returned: on success
            type: list
            sample: []
        vlan_tag:
            description:
                - The IEEE 802.1Q VLAN tag of this VLAN.
                - "Example: `100`"
            returned: on success
            type: int
            sample: 56
        route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that the VLAN uses.
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the VLAN was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the VLAN is in.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "cidr_block": "cidr_block_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "nsg_ids": [],
        "vlan_tag": 56,
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VlanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vlan_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vlan, vlan_id=self.module.params.get("vlan_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
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
            self.client.list_vlans,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VlanFactsHelperCustom = get_custom_class("VlanFactsHelperCustom")


class ResourceFactsHelper(VlanFactsHelperCustom, VlanFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vlan_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "TERMINATING",
                    "TERMINATED",
                    "UPDATING",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vlan",
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

    module.exit_json(vlans=result)


if __name__ == "__main__":
    main()
