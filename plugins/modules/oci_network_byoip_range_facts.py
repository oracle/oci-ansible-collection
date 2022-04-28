#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_network_byoip_range_facts
short_description: Fetches details about one or multiple ByoipRange resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ByoipRange resources in Oracle Cloud Infrastructure
    - Lists the `ByoipRange` resources in the specified compartment.
      You can filter the list using query parameters.
    - If I(byoip_range_id) is specified, the details of a single ByoipRange will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    byoip_range_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR
              block.
            - Required to get a specific byoip_range.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple byoip_ranges.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state name exactly.
        type: str
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific byoip_range
  oci_network_byoip_range_facts:
    # required
    byoip_range_id: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"

- name: List byoip_ranges
  oci_network_byoip_range_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: lifecycle_state_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
byoip_ranges:
    description:
        - List of ByoipRange resources
    returned: on success
    type: complex
    contains:
        time_validated:
            description:
                - The date and time the `ByoipRange` resource was validated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_advertised:
            description:
                - The date and time the `ByoipRange` resource was advertised to the internet by BGP, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_withdrawn:
            description:
                - The date and time the `ByoipRange` resource was withdrawn from advertisement by BGP to the internet, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        validation_token:
            description:
                - The validation token is an internally-generated ASCII string used in the validation process. See L(Importing a CIDR
                  block,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr) for details.
                - Returned for get operation
            returned: on success
            type: str
            sample: validation_token_example
        byoip_range_vcn_ipv6_allocations:
            description:
                - A list of `ByoipRangeVcnIpv6AllocationSummary` objects.
            returned: on success
            type: complex
            contains:
                byoip_range_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR
                          block belongs.
                    returned: on success
                    type: str
                    sample: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
                          `ByoipRange`.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                ipv6_cidr_block:
                    description:
                        - The BYOIPv6 CIDR block range or subrange allocated to a VCN. This could be all or part of a BYOIPv6 CIDR block.
                          Each VCN allocation must be /64 or larger.
                    returned: on success
                    type: str
                    sample: ipv6_cidr_block_example
                vcn_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `Vcn` resource to which the ByoipRange
                          belongs.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        cidr_block:
            description:
                - The public IPv4 CIDR block being imported from on-premises to the Oracle cloud.
            returned: on success
            type: str
            sample: cidr_block_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the BYOIP CIDR block.
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ipv6_cidr_block:
            description:
                - The IPv6 CIDR block being imported to the Oracle cloud. This CIDR block must be /48 or larger, and can be subdivided into sub-ranges used
                  across multiple VCNs. A BYOIPv6 prefix can be also assigned across multiple VCNs, and each VCN must be /64 or larger. You may specify
                  a ULA or private IPv6 prefix of /64 or larger to use in the VCN. IPv6-enabled subnets will remain a fixed /64 in size.
            returned: on success
            type: str
            sample: ipv6_cidr_block_example
        lifecycle_state:
            description:
                - The `ByoipRange` resource's current state.
            returned: on success
            type: str
            sample: INACTIVE
        lifecycle_details:
            description:
                - The `ByoipRange` resource's current status.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the `ByoipRange` resource was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "time_validated": "2013-10-20T19:20:30+01:00",
        "time_advertised": "2013-10-20T19:20:30+01:00",
        "time_withdrawn": "2013-10-20T19:20:30+01:00",
        "validation_token": "validation_token_example",
        "byoip_range_vcn_ipv6_allocations": [{
            "byoip_range_id": "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "ipv6_cidr_block": "ipv6_cidr_block_example",
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "cidr_block": "cidr_block_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ipv6_cidr_block": "ipv6_cidr_block_example",
        "lifecycle_state": "INACTIVE",
        "lifecycle_details": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class ByoipRangeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "byoip_range_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_byoip_range,
            byoip_range_id=self.module.params.get("byoip_range_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_byoip_ranges,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ByoipRangeFactsHelperCustom = get_custom_class("ByoipRangeFactsHelperCustom")


class ResourceFactsHelper(ByoipRangeFactsHelperCustom, ByoipRangeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            byoip_range_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="byoip_range",
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

    module.exit_json(byoip_ranges=result)


if __name__ == "__main__":
    main()
