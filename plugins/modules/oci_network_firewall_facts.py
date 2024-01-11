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
module: oci_network_firewall_facts
short_description: Fetches details about one or multiple NetworkFirewall resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkFirewall resources in Oracle Cloud Infrastructure
    - Returns a list of NetworkFirewalls.
    - If I(network_firewall_id) is specified, the details of a single NetworkFirewall will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_firewall_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
            - Required to get a specific network_firewall.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple network_firewalls.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    network_firewall_policy_id:
        description:
            - A filter to return only resources that match the entire networkFirewallPolicyId given.
        type: str
    availability_domain:
        description:
            - "A filter to return only resources that are present within the specified availability domain.
              To get a list of availability domains for a tenancy, use L(ListAvailabilityDomains,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/identity/20160918/AvailabilityDomain/ListAvailabilityDomains) operation.
              Example: `kIdk:PHX-AD-1`"
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources with a lifecycleState matching the given value.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific network_firewall
  oci_network_firewall_facts:
    # required
    network_firewall_id: "ocid1.networkfirewall.oc1..xxxxxxEXAMPLExxxxxx"

- name: List network_firewalls
  oci_network_firewall_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
network_firewalls:
    description:
        - List of NetworkFirewall resources
    returned: on success
    type: complex
    contains:
        network_security_group_ids:
            description:
                - An array of network security groups L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with the
                  Network Firewall.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Network Firewall.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet associated with the Network Firewall.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - "Availability Domain where Network Firewall instance is created.
                  To get a list of availability domains for a tenancy, use L(ListAvailabilityDomains,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/identity/20160918/AvailabilityDomain/ListAvailabilityDomains) operation.
                  Example: `kIdk:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        ipv4_address:
            description:
                - IPv4 address for the Network Firewall.
            returned: on success
            type: str
            sample: ipv4_address_example
        ipv6_address:
            description:
                - IPv6 address for the Network Firewall.
            returned: on success
            type: str
            sample: ipv6_address_example
        network_firewall_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall Policy.
            returned: on success
            type: str
            sample: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The time instant at which the Network Firewall was created in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time instant at which the Network Firewall was updated in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Network Firewall.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "network_security_group_ids": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "ipv4_address": "ipv4_address_example",
        "ipv6_address": "ipv6_address_example",
        "network_firewall_policy_id": "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.network_firewall import NetworkFirewallClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkFirewallFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "network_firewall_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_firewall,
            network_firewall_id=self.module.params.get("network_firewall_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "network_firewall_policy_id",
            "availability_domain",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_firewalls,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NetworkFirewallFactsHelperCustom = get_custom_class("NetworkFirewallFactsHelperCustom")


class ResourceFactsHelper(
    NetworkFirewallFactsHelperCustom, NetworkFirewallFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_firewall_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            network_firewall_policy_id=dict(type="str"),
            availability_domain=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="network_firewall",
        service_client_class=NetworkFirewallClient,
        namespace="network_firewall",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(network_firewalls=result)


if __name__ == "__main__":
    main()
