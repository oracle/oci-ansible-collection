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
module: oci_network_dhcp_options_facts
short_description: Fetches details about one or multiple DhcpOptions resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DhcpOptions resources in Oracle Cloud Infrastructure
    - Lists the sets of DHCP options in the specified VCN and specified compartment.
      The response includes the default set of options that automatically comes with each VCN,
      plus any other sets you've created.
    - If I(dhcp_id) is specified, the details of a single DhcpOptions will be returned.
version_added: "2.5"
options:
    dhcp_id:
        description:
            - The OCID for the set of DHCP options.
            - Required to get a specific dhcp_options.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple dhcp_options.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
            - Required to list multiple dhcp_options.
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
- name: List dhcp_options
  oci_network_dhcp_options_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific dhcp_options
  oci_network_dhcp_options_facts:
    dhcp_id: ocid1.dhcp.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
dhcp_options:
    description:
        - List of DhcpOptions resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the set of DHCP options.
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
                - Oracle ID (OCID) for the set of DHCP options.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the set of DHCP options.
            returned: on success
            type: string
            sample: PROVISIONING
        options:
            description:
                - The collection of individual DHCP options.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The specific DHCP option. Either `DomainNameServer`
                          (for L(DhcpDnsOption,https://docs.cloud.oracle.com/#/en/iaas/20160918/DhcpDnsOption/)) or
                          `SearchDomain` (for L(DhcpSearchDomainOption,https://docs.cloud.oracle.com/#/en/iaas/20160918/DhcpSearchDomainOption/)).
                    returned: on success
                    type: string
                    sample: DomainNameServer
                custom_dns_servers:
                    description:
                        - If you set `serverType` to `CustomDnsServer`, specify the
                          IP address of at least one DNS server of your choice (three maximum).
                    returned: on success
                    type: list
                    sample: []
                server_type:
                    description:
                        - "* **VcnLocal:** Reserved for future use."
                        - "* **VcnLocalPlusInternet:** Also referred to as \\"Internet and VCN Resolver\\".
                          Instances can resolve internet hostnames (no internet gateway is required),
                          and can resolve hostnames of instances in the VCN. This is the default
                          value in the default set of DHCP options in the VCN. For the Internet and
                          VCN Resolver to work across the VCN, there must also be a DNS label set for
                          the VCN, a DNS label set for each subnet, and a hostname for each instance.
                          The Internet and VCN Resolver also enables reverse DNS lookup, which lets
                          you determine the hostname corresponding to the private IP address. For more
                          information, see
                          L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm)."
                        - "* **CustomDnsServer:** Instances use a DNS server of your choice (three
                          maximum)."
                    returned: on success
                    type: string
                    sample: VcnLocal
                search_domain_names:
                    description:
                        - A single search domain name according to L(RFC 952,https://tools.ietf.org/html/rfc952)
                          and L(RFC 1123,https://tools.ietf.org/html/rfc1123). During a DNS query,
                          the OS will append this search domain name to the value being queried.
                        - If you set L(DhcpDnsOption,https://docs.cloud.oracle.com/#/en/iaas/20160918/DhcpDnsOption/) to `VcnLocalPlusInternet`,
                          and you assign a DNS label to the VCN during creation, the search domain name in the
                          VCN's default set of DHCP options is automatically set to the VCN domain
                          (for example, `vcn1.oraclevcn.com`).
                        - If you don't want to use a search domain name, omit this option from the
                          set of DHCP options. Do not include this option with an empty list
                          of search domain names, or with an empty string as the value for any search
                          domain name.
                    returned: on success
                    type: list
                    sample: []
        time_created:
            description:
                - Date and time the set of DHCP options was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the set of DHCP options belongs to.
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
        "options": [{
            "type": "DomainNameServer",
            "custom_dns_servers": [],
            "server_type": "VcnLocal",
            "search_domain_names": []
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


class DhcpOptionsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dhcp_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "vcn_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dhcp_options, dhcp_id=self.module.params.get("dhcp_id"),
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
            self.client.list_dhcp_options,
            compartment_id=self.module.params.get("compartment_id"),
            vcn_id=self.module.params.get("vcn_id"),
            **optional_kwargs
        )


DhcpOptionsFactsHelperCustom = get_custom_class("DhcpOptionsFactsHelperCustom")


class ResourceFactsHelper(DhcpOptionsFactsHelperCustom, DhcpOptionsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dhcp_id=dict(aliases=["id"], type="str"),
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
        resource_type="dhcp_options",
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

    module.exit_json(dhcp_options=result)


if __name__ == "__main__":
    main()
