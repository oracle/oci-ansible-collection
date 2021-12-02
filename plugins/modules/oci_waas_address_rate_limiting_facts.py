#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_waas_address_rate_limiting_facts
short_description: Fetches details about a AddressRateLimiting resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AddressRateLimiting resource in Oracle Cloud Infrastructure
    - Gets the address rate limiting settings of the Web Application Firewall configuration for a WAAS policy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific address_rate_limiting
  oci_waas_address_rate_limiting_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
address_rate_limiting:
    description:
        - AddressRateLimiting resource
    returned: on success
    type: complex
    contains:
        is_enabled:
            description:
                - Enables or disables the address rate limiting Web Application Firewall feature.
            returned: on success
            type: bool
            sample: true
        allowed_rate_per_address:
            description:
                - The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.
            returned: on success
            type: int
            sample: 56
        max_delayed_count_per_address:
            description:
                - The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.
            returned: on success
            type: int
            sample: 56
        block_response_code:
            description:
                - "The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response codes: `400`,
                  `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `494`, `495`, `496`, `497`, `499`, `500`, `501`,
                  `502`, `503`, `504`, `507`."
            returned: on success
            type: int
            sample: 56
    sample: {
        "is_enabled": true,
        "allowed_rate_per_address": 56,
        "max_delayed_count_per_address": 56,
        "block_response_code": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddressRateLimitingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "waas_policy_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_waf_address_rate_limiting,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )


AddressRateLimitingFactsHelperCustom = get_custom_class(
    "AddressRateLimitingFactsHelperCustom"
)


class ResourceFactsHelper(
    AddressRateLimitingFactsHelperCustom, AddressRateLimitingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(waas_policy_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="address_rate_limiting",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(address_rate_limiting=result)


if __name__ == "__main__":
    main()
