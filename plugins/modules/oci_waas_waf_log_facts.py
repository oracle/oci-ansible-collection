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
module: oci_waas_waf_log_facts
short_description: Fetches details about one or multiple WafLog resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WafLog resources in Oracle Cloud Infrastructure
    - Gets structured Web Application Firewall event logs for a WAAS
      policy. Sorted by the `timeObserved` in ascending order (starting from the
      oldest recorded event).
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
            - A filter that matches log entries where the observed event occurred on or after a date and time specified in RFC 3339 format. If unspecified,
              defaults to two hours before receipt of the request.
        type: str
    time_observed_less_than:
        description:
            - A filter that matches log entries where the observed event occurred before a date and time, specified in RFC 3339 format.
        type: str
    text_contains:
        description:
            - A full text search for logs.
        type: str
    access_rule_key:
        description:
            - Filters logs by access rule key.
        type: list
        elements: str
    action:
        description:
            - Filters logs by Web Application Firewall action.
        type: list
        elements: str
        choices:
            - "BLOCK"
            - "DETECT"
            - "BYPASS"
            - "LOG"
            - "REDIRECTED"
    client_address:
        description:
            - Filters logs by client IP address.
        type: list
        elements: str
    country_code:
        description:
            - Filters logs by country code. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see L(ISO's
              website,https://www.iso.org/obp/ui/#search/code/).
        type: list
        elements: str
    country_name:
        description:
            - Filter logs by country name.
        type: list
        elements: str
    fingerprint:
        description:
            - Filter logs by device fingerprint.
        type: list
        elements: str
    http_method:
        description:
            - Filter logs by HTTP method.
        type: list
        elements: str
        choices:
            - "OPTIONS"
            - "GET"
            - "HEAD"
            - "POST"
            - "PUT"
            - "DELETE"
            - "TRACE"
            - "CONNECT"
    incident_key:
        description:
            - Filter logs by incident key.
        type: list
        elements: str
    log_type:
        description:
            - Filter by log type. For more information about WAF logs, see L(Logs,https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/logs.htm).
        type: list
        elements: str
        choices:
            - "ACCESS"
            - "PROTECTION_RULES"
            - "JS_CHALLENGE"
            - "CAPTCHA"
            - "ACCESS_RULES"
            - "THREAT_FEEDS"
            - "HUMAN_INTERACTION_CHALLENGE"
            - "DEVICE_FINGERPRINT_CHALLENGE"
            - "ADDRESS_RATE_LIMITING"
    origin_address:
        description:
            - Filter by origin IP address.
        type: list
        elements: str
    referrer:
        description:
            - Filter by referrer.
        type: list
        elements: str
    request_url:
        description:
            - Filter by request URL.
        type: list
        elements: str
    response_code:
        description:
            - Filter by response code.
        type: list
        elements: int
    threat_feed_key:
        description:
            - Filter by threat feed key.
        type: list
        elements: str
    user_agent:
        description:
            - Filter by user agent.
        type: list
        elements: str
    protection_rule_key:
        description:
            - Filter by protection rule key.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List waf_logs
  oci_waas_waf_log_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_observed_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_observed_less_than: 2013-10-20T19:20:30+01:00
    text_contains: text_contains_example
    access_rule_key: [ "access_rule_key_example" ]
    action: [ "BLOCK" ]
    client_address: [ "client_address_example" ]
    country_code: [ "country_code_example" ]
    country_name: [ "country_name_example" ]
    fingerprint: [ "fingerprint_example" ]
    http_method: [ "OPTIONS" ]
    incident_key: [ "incident_key_example" ]
    log_type: [ "ACCESS" ]
    origin_address: [ "origin_address_example" ]
    referrer: [ "referrer_example" ]
    request_url: [ "request_url_example" ]
    response_code: [ "56" ]
    threat_feed_key: [ "threat_feed_key_example" ]
    user_agent: [ "user_agent_example" ]
    protection_rule_key: [ "protection_rule_key_example" ]

"""

RETURN = """
waf_logs:
    description:
        - List of WafLog resources
    returned: on success
    type: complex
    contains:
        action:
            description:
                - The action taken on the request, either `ALLOW`, `DETECT`, or `BLOCK`.
            returned: on success
            type: str
            sample: action_example
        captcha_action:
            description:
                - The CAPTCHA action taken on the request, `ALLOW` or `BLOCK`. For more information about
                  CAPTCHAs, see `UpdateCaptchas`.
            returned: on success
            type: str
            sample: captcha_action_example
        captcha_expected:
            description:
                - The CAPTCHA challenge answer that was expected.
            returned: on success
            type: str
            sample: captcha_expected_example
        captcha_received:
            description:
                - The CAPTCHA challenge answer that was received.
            returned: on success
            type: str
            sample: captcha_received_example
        captcha_fail_count:
            description:
                - The number of times the CAPTCHA challenge was failed.
            returned: on success
            type: str
            sample: captcha_fail_count_example
        client_address:
            description:
                - The IPv4 address of the requesting client.
            returned: on success
            type: str
            sample: client_address_example
        country_name:
            description:
                - The name of the country where the request originated.
            returned: on success
            type: str
            sample: country_name_example
        user_agent:
            description:
                - The value of the request's `User-Agent` header field.
            returned: on success
            type: str
            sample: user_agent_example
        domain:
            description:
                - The `Host` header data of the request.
            returned: on success
            type: str
            sample: domain_example
        protection_rule_detections:
            description:
                - A map of protection rule keys to detection message details. Detections are
                  requests that matched the criteria of a protection rule but the rule's
                  action was set to `DETECT`.
            returned: on success
            type: dict
            sample: {}
        http_method:
            description:
                - The HTTP method of the request.
            returned: on success
            type: str
            sample: http_method_example
        request_url:
            description:
                - The path and query string of the request.
            returned: on success
            type: str
            sample: request_url_example
        http_headers:
            description:
                - The map of the request's header names to their respective values.
            returned: on success
            type: dict
            sample: {}
        referrer:
            description:
                - The `Referrer` header value of the request.
            returned: on success
            type: str
            sample: referrer_example
        response_code:
            description:
                - The status code of the response.
            returned: on success
            type: int
            sample: 56
        response_size:
            description:
                - The size in bytes of the response.
            returned: on success
            type: int
            sample: 56
        incident_key:
            description:
                - The incident key of a request. An incident key is generated for
                  each request processed by the Web Application Firewall and is used to
                  idenitfy blocked requests in applicable logs.
            returned: on success
            type: str
            sample: incident_key_example
        fingerprint:
            description:
                - The hashed signature of the device's fingerprint. For more information,
                  see `DeviceFingerPrintChallenge`.
            returned: on success
            type: str
            sample: fingerprint_example
        device:
            description:
                - The type of device that the request was made from.
            returned: on success
            type: str
            sample: device_example
        country_code:
            description:
                - ISO 3166-1 alpha-2 code of the country from which the request originated.
                  For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
            returned: on success
            type: str
            sample: country_code_example
        request_headers:
            description:
                - A map of header names to values of the request sent to the origin, including any headers
                  appended by the Web Application Firewall.
            returned: on success
            type: dict
            sample: {}
        threat_feed_key:
            description:
                - The `ThreatFeed` key that matched the request. For more information about
                  threat feeds, see `UpdateThreatFeeds`.
            returned: on success
            type: str
            sample: threat_feed_key_example
        access_rule_key:
            description:
                - The `AccessRule` key that matched the request. For more information about
                  access rules, see `UpdateAccessRules`.
            returned: on success
            type: str
            sample: access_rule_key_example
        address_rate_limiting_key:
            description:
                - The `AddressRateLimiting` key that matched the request. For more information
                  about address rate limiting, see `UpdateWafAddressRateLimiting`.
            returned: on success
            type: str
            sample: address_rate_limiting_key_example
        timestamp:
            description:
                - The date and time the Web Application Firewall processed the request and logged it.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        log_type:
            description:
                - The type of log of the request. For more about log types, see L(Logs,https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/logs.htm).
            returned: on success
            type: str
            sample: log_type_example
        origin_address:
            description:
                - The address of the origin server where the request was sent.
            returned: on success
            type: str
            sample: origin_address_example
        origin_response_time:
            description:
                - The amount of time it took the origin server to respond to the request, in seconds.
            returned: on success
            type: str
            sample: origin_response_time_example
    sample: [{
        "action": "action_example",
        "captcha_action": "captcha_action_example",
        "captcha_expected": "captcha_expected_example",
        "captcha_received": "captcha_received_example",
        "captcha_fail_count": "captcha_fail_count_example",
        "client_address": "client_address_example",
        "country_name": "country_name_example",
        "user_agent": "user_agent_example",
        "domain": "domain_example",
        "protection_rule_detections": {},
        "http_method": "http_method_example",
        "request_url": "request_url_example",
        "http_headers": {},
        "referrer": "referrer_example",
        "response_code": 56,
        "response_size": 56,
        "incident_key": "incident_key_example",
        "fingerprint": "fingerprint_example",
        "device": "device_example",
        "country_code": "country_code_example",
        "request_headers": {},
        "threat_feed_key": "threat_feed_key_example",
        "access_rule_key": "access_rule_key_example",
        "address_rate_limiting_key": "address_rate_limiting_key_example",
        "timestamp": "2013-10-20T19:20:30+01:00",
        "log_type": "log_type_example",
        "origin_address": "origin_address_example",
        "origin_response_time": "origin_response_time_example"
    }]
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


class WafLogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
            "text_contains",
            "access_rule_key",
            "action",
            "client_address",
            "country_code",
            "country_name",
            "fingerprint",
            "http_method",
            "incident_key",
            "log_type",
            "origin_address",
            "referrer",
            "request_url",
            "response_code",
            "threat_feed_key",
            "user_agent",
            "protection_rule_key",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_waf_logs,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


WafLogFactsHelperCustom = get_custom_class("WafLogFactsHelperCustom")


class ResourceFactsHelper(WafLogFactsHelperCustom, WafLogFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            waas_policy_id=dict(type="str", required=True),
            time_observed_greater_than_or_equal_to=dict(type="str"),
            time_observed_less_than=dict(type="str"),
            text_contains=dict(type="str"),
            access_rule_key=dict(type="list", elements="str", no_log=True),
            action=dict(
                type="list",
                elements="str",
                choices=["BLOCK", "DETECT", "BYPASS", "LOG", "REDIRECTED"],
            ),
            client_address=dict(type="list", elements="str"),
            country_code=dict(type="list", elements="str"),
            country_name=dict(type="list", elements="str"),
            fingerprint=dict(type="list", elements="str"),
            http_method=dict(
                type="list",
                elements="str",
                choices=[
                    "OPTIONS",
                    "GET",
                    "HEAD",
                    "POST",
                    "PUT",
                    "DELETE",
                    "TRACE",
                    "CONNECT",
                ],
            ),
            incident_key=dict(type="list", elements="str", no_log=True),
            log_type=dict(
                type="list",
                elements="str",
                choices=[
                    "ACCESS",
                    "PROTECTION_RULES",
                    "JS_CHALLENGE",
                    "CAPTCHA",
                    "ACCESS_RULES",
                    "THREAT_FEEDS",
                    "HUMAN_INTERACTION_CHALLENGE",
                    "DEVICE_FINGERPRINT_CHALLENGE",
                    "ADDRESS_RATE_LIMITING",
                ],
            ),
            origin_address=dict(type="list", elements="str"),
            referrer=dict(type="list", elements="str"),
            request_url=dict(type="list", elements="str"),
            response_code=dict(type="list", elements="int"),
            threat_feed_key=dict(type="list", elements="str", no_log=True),
            user_agent=dict(type="list", elements="str"),
            protection_rule_key=dict(type="list", elements="str", no_log=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waf_log",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waf_logs=result)


if __name__ == "__main__":
    main()
