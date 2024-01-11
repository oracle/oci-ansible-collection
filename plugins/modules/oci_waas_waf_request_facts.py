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
module: oci_waas_waf_request_facts
short_description: Fetches details about one or multiple WafRequest resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WafRequest resources in Oracle Cloud Infrastructure
    - Gets the number of requests managed by a Web Application Firewall
      over a specified period of time, including blocked requests. Sorted
      by `timeObserved` in ascending order (starting from oldest requests).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
    time_observed_greater_than_or_equal_to:
        description:
            - A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30
              minutes before receipt of the request.
        type: str
    time_observed_less_than:
        description:
            - A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List waf_requests
  oci_waas_waf_request_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_observed_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_observed_less_than: 2013-10-20T19:20:30+01:00

"""

RETURN = """
waf_requests:
    description:
        - List of WafRequest resources
    returned: on success
    type: complex
    contains:
        time_observed:
            description:
                - The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_range_in_seconds:
            description:
                - The number of seconds this data covers.
            returned: on success
            type: int
            sample: 56
        count:
            description:
                - The total number of requests received in this time period.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "time_observed": "2013-10-20T19:20:30+01:00",
        "time_range_in_seconds": 56,
        "count": 56
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


class WafRequestFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_waf_requests,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


WafRequestFactsHelperCustom = get_custom_class("WafRequestFactsHelperCustom")


class ResourceFactsHelper(WafRequestFactsHelperCustom, WafRequestFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            waas_policy_id=dict(type="str", required=True),
            time_observed_greater_than_or_equal_to=dict(type="str"),
            time_observed_less_than=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waf_request",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waf_requests=result)


if __name__ == "__main__":
    main()
