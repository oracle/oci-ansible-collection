#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_waas_caching_rules_facts
short_description: Fetches details about one or multiple CachingRules resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CachingRules resources in Oracle Cloud Infrastructure
    - Gets the currently configured caching rules for the Web Application Firewall configuration of a specified WAAS policy.
      The rules are processed in the order they are specified in and the first matching rule will be used when processing a request.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List caching_rules
  oci_waas_caching_rules_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
caching_rules:
    description:
        - List of CachingRules resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key for the caching rule.
            returned: on success
            type: str
            sample: key_example
        name:
            description:
                - The name of the caching rule.
            returned: on success
            type: str
            sample: name_example
        action:
            description:
                - "The action to take when the criteria of a caching rule are met.
                  - **CACHE:** Caches requested content when the criteria of the rule are met."
                - "- **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met."
            returned: on success
            type: str
            sample: CACHE
        caching_duration:
            description:
                - "The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days,
                  weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported. Only applies when the
                  `action` is set to `CACHE`.
                  Example: `PT1H`"
            returned: on success
            type: str
            sample: caching_duration_example
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
            type: str
            sample: client_caching_duration_example
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
                    type: str
                    sample: URL_IS
                value:
                    description:
                        - The value of the caching rule criteria.
                    returned: on success
                    type: str
                    sample: value_example
    sample: [{
        "key": "key_example",
        "name": "name_example",
        "action": "CACHE",
        "caching_duration": "caching_duration_example",
        "is_client_caching_enabled": true,
        "client_caching_duration": "client_caching_duration_example",
        "criteria": [{
            "condition": "URL_IS",
            "value": "value_example"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CachingRulesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_caching_rules,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


CachingRulesFactsHelperCustom = get_custom_class("CachingRulesFactsHelperCustom")


class ResourceFactsHelper(CachingRulesFactsHelperCustom, CachingRulesFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(waas_policy_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="caching_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(caching_rules=result)


if __name__ == "__main__":
    main()
