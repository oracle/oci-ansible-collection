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
module: oci_network_fast_connect_provider_service_key_facts
short_description: Fetches details about a FastConnectProviderServiceKey resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a FastConnectProviderServiceKey resource in Oracle Cloud Infrastructure
    - Gets the specified provider service key's information. Use this operation to validate a
      provider service key. An invalid key returns a 404 error.
version_added: "2.9"
author: Oracle (@oracle)
options:
    provider_service_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the provider service.
        type: str
        required: true
    provider_service_key_name:
        description:
            - The provider service key that the provider gives you when you set up a virtual circuit connection
              from the provider to Oracle Cloud Infrastructure. You can set up that connection and get your
              provider service key at the provider's website or portal. For the portal location, see the `description`
              attribute of the L(FastConnectProviderService,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/FastConnectProviderService/).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific fast_connect_provider_service_key
  oci_network_fast_connect_provider_service_key_facts:
    provider_service_id: "ocid1.providerservice.oc1..xxxxxxEXAMPLExxxxxx"
    provider_service_key_name: provider_service_key_name_example

"""

RETURN = """
fast_connect_provider_service_key:
    description:
        - FastConnectProviderServiceKey resource
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The service key that the provider gives you when you set up a virtual circuit connection
                  from the provider to Oracle Cloud Infrastructure. Use this value as the `providerServiceKeyName`
                  query parameter for
                  L(GetFastConnectProviderServiceKey,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/FastConnectProviderServiceKey/GetFastConnectProviderServiceKey).
            returned: on success
            type: string
            sample: name_example
        bandwidth_shape_name:
            description:
                - The provisioned data rate of the connection. To get a list of the
                  available bandwidth levels (that is, shapes), see
                  L(ListFastConnectProviderServiceVirtualCircuitBandwidthShapes,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).
                - "Example: `10 Gbps`"
            returned: on success
            type: string
            sample: 10 Gbps
        peering_location:
            description:
                - The provider's peering location.
            returned: on success
            type: string
            sample: peering_location_example
    sample: {
        "name": "name_example",
        "bandwidth_shape_name": "10 Gbps",
        "peering_location": "peering_location_example"
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


class FastConnectProviderServiceKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "provider_service_id",
            "provider_service_key_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fast_connect_provider_service_key,
            provider_service_id=self.module.params.get("provider_service_id"),
            provider_service_key_name=self.module.params.get(
                "provider_service_key_name"
            ),
        )


FastConnectProviderServiceKeyFactsHelperCustom = get_custom_class(
    "FastConnectProviderServiceKeyFactsHelperCustom"
)


class ResourceFactsHelper(
    FastConnectProviderServiceKeyFactsHelperCustom,
    FastConnectProviderServiceKeyFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            provider_service_id=dict(type="str", required=True),
            provider_service_key_name=dict(type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fast_connect_provider_service_key",
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

    module.exit_json(fast_connect_provider_service_key=result)


if __name__ == "__main__":
    main()
