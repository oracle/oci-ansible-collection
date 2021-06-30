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
module: oci_analytics_private_access_channel_facts
short_description: Fetches details about a PrivateAccessChannel resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a PrivateAccessChannel resource in Oracle Cloud Infrastructure
    - Retrieve private access channel in the specified Analytics Instance.
version_added: "2.9"
author: Oracle (@oracle)
options:
    private_access_channel_key:
        description:
            - The unique identifier key of the Private Access Channel.
        type: str
        required: true
    analytics_instance_id:
        description:
            - The OCID of the AnalyticsInstance.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific private_access_channel
  oci_analytics_private_access_channel_facts:
    private_access_channel_key: private_access_channel_key_example
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
private_access_channel:
    description:
        - PrivateAccessChannel resource
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Private Access Channel unique identifier key.
            returned: on success
            type: string
            sample: key_example
        display_name:
            description:
                - Display Name of the Private Access Channel.
            returned: on success
            type: string
            sample: display_name_example
        vcn_id:
            description:
                - OCID of the customer VCN peered with private access channel.
            returned: on success
            type: string
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - OCID of the customer subnet connected to private access channel.
            returned: on success
            type: string
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - IP Address of the Private Access channel.
            returned: on success
            type: string
            sample: ip_address_example
        egress_source_ip_addresses:
            description:
                - The list of IP addresses from the customer subnet connected to private access channel, used as a source Ip by Private Access Channel
                  for network traffic from the AnalyticsInstance to Private Sources.
            returned: on success
            type: list
            sample: []
        private_source_dns_zones:
            description:
                - List of Private Source DNS zones registered with Private Access Channel,
                  where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
                  Min of 1 is required and Max of 30 Private Source DNS zones can be registered.
            returned: on success
            type: complex
            contains:
                dns_zone:
                    description:
                        - "Private Source DNS Zone. Ex: example-vcn.oraclevcn.com, corp.example.com."
                    returned: on success
                    type: string
                    sample: dns_zone_example
                description:
                    description:
                        - Description of private source dns zone.
                    returned: on success
                    type: string
                    sample: description_example
    sample: {
        "key": "key_example",
        "display_name": "display_name_example",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "egress_source_ip_addresses": [],
        "private_source_dns_zones": [{
            "dns_zone": "dns_zone_example",
            "description": "description_example"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.analytics import AnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateAccessChannelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "private_access_channel_key",
            "analytics_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_access_channel,
            private_access_channel_key=self.module.params.get(
                "private_access_channel_key"
            ),
            analytics_instance_id=self.module.params.get("analytics_instance_id"),
        )


PrivateAccessChannelFactsHelperCustom = get_custom_class(
    "PrivateAccessChannelFactsHelperCustom"
)


class ResourceFactsHelper(
    PrivateAccessChannelFactsHelperCustom, PrivateAccessChannelFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            private_access_channel_key=dict(type="str", required=True),
            analytics_instance_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="private_access_channel",
        service_client_class=AnalyticsClient,
        namespace="analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(private_access_channel=result)


if __name__ == "__main__":
    main()
