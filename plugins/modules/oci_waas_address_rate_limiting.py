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
module: oci_waas_address_rate_limiting
short_description: Manage an AddressRateLimiting resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an AddressRateLimiting resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    is_enabled:
        description:
            - Enables or disables the address rate limiting Web Application Firewall feature.
        type: bool
        required: true
    allowed_rate_per_address:
        description:
            - The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.
            - This parameter is updatable.
        type: int
    max_delayed_count_per_address:
        description:
            - The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.
            - This parameter is updatable.
        type: int
    block_response_code:
        description:
            - "The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response codes: `400`,
              `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`,
              `503`, `504`, `507`."
            - This parameter is updatable.
        type: int
    state:
        description:
            - The state of the AddressRateLimiting.
            - Use I(state=present) to update an existing an AddressRateLimiting.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update address_rate_limiting
  oci_waas_address_rate_limiting:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    is_enabled: true

    # optional
    allowed_rate_per_address: 56
    max_delayed_count_per_address: 56
    block_response_code: 56

"""

RETURN = """
address_rate_limiting:
    description:
        - Details of the AddressRateLimiting resource acted upon by the current operation
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
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import AddressRateLimiting

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddressRateLimitingHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_waf_address_rate_limiting

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_waf_address_rate_limiting,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return AddressRateLimiting

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_waf_address_rate_limiting,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_waf_address_rate_limiting_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AddressRateLimitingHelperCustom = get_custom_class("AddressRateLimitingHelperCustom")


class ResourceHelper(AddressRateLimitingHelperCustom, AddressRateLimitingHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            is_enabled=dict(type="bool", required=True),
            allowed_rate_per_address=dict(type="int"),
            max_delayed_count_per_address=dict(type="int"),
            block_response_code=dict(type="int"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="address_rate_limiting",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
