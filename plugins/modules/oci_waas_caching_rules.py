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
module: oci_waas_caching_rules
short_description: Manage a CachingRules resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a CachingRules resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    caching_rules_details:
        description:
            - ""
        type: list
        required: true
        suboptions:
            key:
                description:
                    - The unique key for the caching rule.
                    - This parameter is updatable.
                type: str
            name:
                description:
                    - The name of the caching rule.
                    - This parameter is updatable.
                type: str
                required: true
            action:
                description:
                    - "The action to take when the criteria of a caching rule are met.
                      - **CACHE:** Caches requested content when the criteria of the rule are met."
                    - "- **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met."
                    - This parameter is updatable.
                type: str
                choices:
                    - "CACHE"
                    - "BYPASS_CACHE"
                required: true
            caching_duration:
                description:
                    - "The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours,
                      days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when
                      the `action` is set to `CACHE`.
                      Example: `PT1H`"
                    - This parameter is updatable.
                type: str
            is_client_caching_enabled:
                description:
                    - Enables or disables client caching.
                      Browsers use the `Cache-Control` header value for caching content locally in the browser. This setting overrides the addition of a `Cache-
                      Control` header in responses.
                    - This parameter is updatable.
                type: bool
            client_caching_duration:
                description:
                    - "The duration to cache content in the user's browser, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours,
                      days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when
                      the `action` is set to `CACHE`.
                      Example: `PT1H`"
                    - This parameter is updatable.
                type: str
            criteria:
                description:
                    - The array of the rule criteria with condition and value. The caching rule would be applied for the requests that matched any of the listed
                      conditions.
                type: list
                required: true
                suboptions:
                    condition:
                        description:
                            - "The condition of the caching rule criteria.
                              - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field."
                            - "- **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field."
                            - "- **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value`
                              field."
                            - "- **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field."
                            - URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'` `&` `?`
                              symbols. Resources to cache can only be specified by a URL, any query parameters are ignored.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "URL_IS"
                            - "URL_STARTS_WITH"
                            - "URL_PART_ENDS_WITH"
                            - "URL_PART_CONTAINS"
                        required: true
                    value:
                        description:
                            - The value of the caching rule criteria.
                            - This parameter is updatable.
                        type: str
                        required: true
    state:
        description:
            - The state of the CachingRules.
            - Use I(state=present) to update an existing a CachingRules.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update caching_rules
  oci_waas_caching_rules:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx
    caching_rules_details:
    - name: name_example
      action: CACHE
      criteria:
      - condition: URL_IS
        value: value_example

"""

RETURN = """
caching_rules:
    description:
        - Details of the CachingRules resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key for the caching rule.
            returned: on success
            type: string
            sample: key_example
        name:
            description:
                - The name of the caching rule.
            returned: on success
            type: string
            sample: name_example
        action:
            description:
                - "The action to take when the criteria of a caching rule are met.
                  - **CACHE:** Caches requested content when the criteria of the rule are met."
                - "- **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met."
            returned: on success
            type: string
            sample: CACHE
        caching_duration:
            description:
                - "The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days,
                  weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the
                  `action` is set to `CACHE`.
                  Example: `PT1H`"
            returned: on success
            type: string
            sample: PT1H
        is_client_caching_enabled:
            description:
                - Enables or disables client caching.
                  Browsers use the `Cache-Control` header value for caching content locally in the browser. This setting overrides the addition of a `Cache-
                  Control` header in responses.
            returned: on success
            type: bool
            sample: true
        client_caching_duration:
            description:
                - "The duration to cache content in the user's browser, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days,
                  weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the
                  `action` is set to `CACHE`.
                  Example: `PT1H`"
            returned: on success
            type: string
            sample: PT1H
        criteria:
            description:
                - The array of the rule criteria with condition and value. The caching rule would be applied for the requests that matched any of the listed
                  conditions.
            returned: on success
            type: complex
            contains:
                condition:
                    description:
                        - "The condition of the caching rule criteria.
                          - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field."
                        - "- **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field."
                        - "- **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field."
                        - "- **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field."
                        - URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'` `&` `?` symbols.
                          Resources to cache can only be specified by a URL, any query parameters are ignored.
                    returned: on success
                    type: string
                    sample: URL_IS
                value:
                    description:
                        - The value of the caching rule criteria.
                    returned: on success
                    type: string
                    sample: value_example
    sample: {
        "key": "key_example",
        "name": "name_example",
        "action": "CACHE",
        "caching_duration": "PT1H",
        "is_client_caching_enabled": true,
        "client_caching_duration": "PT1H",
        "criteria": [{
            "condition": "URL_IS",
            "value": "value_example"
        }]
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
    from oci.waas.models import CachingRule

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CachingRulesHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "waas_policy_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_caching_rules, **kwargs
        )

    def get_update_model_class(self):
        return CachingRule

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_caching_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                caching_rules_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CachingRulesHelperCustom = get_custom_class("CachingRulesHelperCustom")


class ResourceHelper(CachingRulesHelperCustom, CachingRulesHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            caching_rules_details=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str"),
                    name=dict(type="str", required=True),
                    action=dict(
                        type="str", required=True, choices=["CACHE", "BYPASS_CACHE"]
                    ),
                    caching_duration=dict(type="str"),
                    is_client_caching_enabled=dict(type="bool"),
                    client_caching_duration=dict(type="str"),
                    criteria=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            condition=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "URL_IS",
                                    "URL_STARTS_WITH",
                                    "URL_PART_ENDS_WITH",
                                    "URL_PART_CONTAINS",
                                ],
                            ),
                            value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="caching_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
