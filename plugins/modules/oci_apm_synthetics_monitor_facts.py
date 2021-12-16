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
module: oci_apm_synthetics_monitor_facts
short_description: Fetches details about one or multiple Monitor resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Monitor resources in Oracle Cloud Infrastructure
    - Returns a list of monitors.
    - If I(monitor_id) is specified, the details of a single Monitor will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    monitor_id:
        description:
            - The OCID of the monitor.
            - Required to get a specific monitor.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    script_id:
        description:
            - A filter to return only monitors using scriptId.
        type: str
    monitor_type:
        description:
            - A filter to return only monitors that match the given monitor type.
              Supported values are SCRIPTED_BROWSER, BROWSER, SCRIPTED_REST and REST.
        type: str
    status:
        description:
            - A filter to return only monitors that match the status given.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
            - "INVALID"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order of displayName is ascending.
              Default order of timeCreated and timeUpdated is descending.
              The displayName sort by is case insensitive.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
            - "timeUpdated"
            - "status"
            - "monitorType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific monitor
  oci_apm_synthetics_monitor_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"

- name: List monitors
  oci_apm_synthetics_monitor_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"
    monitor_type: monitor_type_example
    status: ENABLED
    sort_order: ASC
    sort_by: displayName

"""

RETURN = """
monitors:
    description:
        - List of Monitor resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the monitor.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Unique name that can be edited. The name should not contain any confidential information.
            returned: on success
            type: str
            sample: display_name_example
        monitor_type:
            description:
                - Type of the monitor.
            returned: on success
            type: str
            sample: SCRIPTED_BROWSER
        vantage_points:
            description:
                - List of vantage points from where monitor is running.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the vantage point.
                    returned: on success
                    type: str
                    sample: name_example
                display_name:
                    description:
                        - Unique name that can be edited. The name should not contain any confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
        vantage_point_count:
            description:
                - Number of vantage points where monitor is running.
            returned: on success
            type: int
            sample: 56
        script_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the script.
                  scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
            returned: on success
            type: str
            sample: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"
        script_name:
            description:
                - Name of the script.
            returned: on success
            type: str
            sample: script_name_example
        status:
            description:
                - Enables or disables the monitor.
            returned: on success
            type: str
            sample: ENABLED
        repeat_interval_in_seconds:
            description:
                - Interval in seconds after the start time when the job should be repeated.
                  Minimum repeatIntervalInSeconds should be 300 seconds.
            returned: on success
            type: int
            sample: 56
        is_run_once:
            description:
                - If runOnce is enabled, then the monitor will run once.
            returned: on success
            type: bool
            sample: true
        timeout_in_seconds:
            description:
                - Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors.
                  Also, timeoutInSeconds should be a multiple of 60. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after
                  that.
            returned: on success
            type: int
            sample: 56
        target:
            description:
                - Specify the endpoint on which to run the monitor.
                  For BROWSER and REST monitor types, target is mandatory.
                  If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor)
                  against the specified target endpoint.
                  If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.
            returned: on success
            type: str
            sample: target_example
        script_parameters:
            description:
                - "List of script parameters. Example: `[{\\"monitorScriptParameter\\": {\\"paramName\\": \\"userid\\", \\"paramValue\\":\\"testuser\\"},
                  \\"isSecret\\": false, \\"isOverwritten\\": false}]`"
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                monitor_script_parameter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        param_name:
                            description:
                                - Name of the parameter.
                            returned: on success
                            type: str
                            sample: param_name_example
                        param_value:
                            description:
                                - Value of the parameter.
                            returned: on success
                            type: str
                            sample: param_value_example
                is_secret:
                    description:
                        - Describes if  the parameter value is secret and should be kept confidential.
                          isSecret is specified in either CreateScript or UpdateScript API.
                    returned: on success
                    type: bool
                    sample: true
                is_overwritten:
                    description:
                        - If parameter value is default or overwritten.
                    returned: on success
                    type: bool
                    sample: true
        configuration:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                config_type:
                    description:
                        - Type of configuration.
                    returned: on success
                    type: str
                    sample: BROWSER_CONFIG
                is_failure_retried:
                    description:
                        - If isFailureRetried is enabled, then a failed call will be retried.
                    returned: on success
                    type: bool
                    sample: true
                is_certificate_validation_enabled:
                    description:
                        - If certificate validation is enabled, then the call will fail in case of certification errors.
                    returned: on success
                    type: bool
                    sample: true
                verify_texts:
                    description:
                        - Verify all the search strings present in response.
                          If any search string is not present in the response, then it will be considered as a failure.
                    returned: on success
                    type: complex
                    contains:
                        text:
                            description:
                                - Verification text in the response.
                            returned: on success
                            type: str
                            sample: text_example
                network_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        number_of_hops:
                            description:
                                - Number of hops.
                            returned: on success
                            type: int
                            sample: 56
                        probe_per_hop:
                            description:
                                - Number of probes per hop.
                            returned: on success
                            type: int
                            sample: 56
                        transmission_rate:
                            description:
                                - Number of probe packets sent out simultaneously.
                            returned: on success
                            type: int
                            sample: 56
                        protocol:
                            description:
                                - Type of protocol.
                            returned: on success
                            type: str
                            sample: ICMP
                        probe_mode:
                            description:
                                - Type of probe mode when TCP protocol is selected.
                            returned: on success
                            type: str
                            sample: SACK
                is_redirection_enabled:
                    description:
                        - If redirection enabled, then redirects will be allowed while accessing target URL.
                    returned: on success
                    type: bool
                    sample: true
                request_method:
                    description:
                        - Request HTTP method.
                    returned: on success
                    type: str
                    sample: GET
                req_authentication_scheme:
                    description:
                        - Request http authentication scheme.
                    returned: on success
                    type: str
                    sample: OAUTH
                req_authentication_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        oauth_scheme:
                            description:
                                - Request http oauth scheme.
                            returned: on success
                            type: str
                            sample: NONE
                        auth_user_name:
                            description:
                                - Username for authentication.
                            returned: on success
                            type: str
                            sample: auth_user_name_example
                        auth_user_password:
                            description:
                                - User password for authentication.
                            returned: on success
                            type: str
                            sample: example-password
                        auth_token:
                            description:
                                - Authentication token.
                            returned: on success
                            type: str
                            sample: auth_token_example
                        auth_url:
                            description:
                                - URL to get authetication token.
                            returned: on success
                            type: str
                            sample: auth_url_example
                        auth_headers:
                            description:
                                - "List of authentication headers. Example: `[{\\"headerName\\": \\"content-type\\", \\"headerValue\\":\\"json\\"}]`"
                            returned: on success
                            type: complex
                            contains:
                                header_name:
                                    description:
                                        - Name of the header.
                                    returned: on success
                                    type: str
                                    sample: header_name_example
                                header_value:
                                    description:
                                        - Value of the header.
                                    returned: on success
                                    type: str
                                    sample: header_value_example
                        auth_request_method:
                            description:
                                - Request method.
                            returned: on success
                            type: str
                            sample: GET
                        auth_request_post_body:
                            description:
                                - Request post body.
                            returned: on success
                            type: str
                            sample: auth_request_post_body_example
                request_headers:
                    description:
                        - "List of request headers. Example: `[{\\"headerName\\": \\"content-type\\", \\"headerValue\\":\\"json\\"}]`"
                    returned: on success
                    type: complex
                    contains:
                        header_name:
                            description:
                                - Name of the header.
                            returned: on success
                            type: str
                            sample: header_name_example
                        header_value:
                            description:
                                - Value of the header.
                            returned: on success
                            type: str
                            sample: header_value_example
                request_query_params:
                    description:
                        - "List of request query params. Example: `[{\\"paramName\\": \\"sortOrder\\", \\"paramValue\\": \\"asc\\"}]`"
                    returned: on success
                    type: complex
                    contains:
                        param_name:
                            description:
                                - Name of request query parameter.
                            returned: on success
                            type: str
                            sample: param_name_example
                        param_value:
                            description:
                                - Value of request query parameter.
                            returned: on success
                            type: str
                            sample: param_value_example
                request_post_body:
                    description:
                        - Request post body content.
                    returned: on success
                    type: str
                    sample: request_post_body_example
                verify_response_content:
                    description:
                        - Verify response content against regular expression based string.
                          If response content does not match the verifyResponseContent value, then it will be considered a failure.
                    returned: on success
                    type: str
                    sample: verify_response_content_example
                verify_response_codes:
                    description:
                        - Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.
                    returned: on success
                    type: list
                    sample: []
        time_created:
            description:
                - "The time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-13T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "monitor_type": "SCRIPTED_BROWSER",
        "vantage_points": [{
            "name": "name_example",
            "display_name": "display_name_example"
        }],
        "vantage_point_count": 56,
        "script_id": "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx",
        "script_name": "script_name_example",
        "status": "ENABLED",
        "repeat_interval_in_seconds": 56,
        "is_run_once": true,
        "timeout_in_seconds": 56,
        "target": "target_example",
        "script_parameters": [{
            "monitor_script_parameter": {
                "param_name": "param_name_example",
                "param_value": "param_value_example"
            },
            "is_secret": true,
            "is_overwritten": true
        }],
        "configuration": {
            "config_type": "BROWSER_CONFIG",
            "is_failure_retried": true,
            "is_certificate_validation_enabled": true,
            "verify_texts": [{
                "text": "text_example"
            }],
            "network_configuration": {
                "number_of_hops": 56,
                "probe_per_hop": 56,
                "transmission_rate": 56,
                "protocol": "ICMP",
                "probe_mode": "SACK"
            },
            "is_redirection_enabled": true,
            "request_method": "GET",
            "req_authentication_scheme": "OAUTH",
            "req_authentication_details": {
                "oauth_scheme": "NONE",
                "auth_user_name": "auth_user_name_example",
                "auth_user_password": "example-password",
                "auth_token": "auth_token_example",
                "auth_url": "auth_url_example",
                "auth_headers": [{
                    "header_name": "header_name_example",
                    "header_value": "header_value_example"
                }],
                "auth_request_method": "GET",
                "auth_request_post_body": "auth_request_post_body_example"
            },
            "request_headers": [{
                "header_name": "header_name_example",
                "header_value": "header_value_example"
            }],
            "request_query_params": [{
                "param_name": "param_name_example",
                "param_value": "param_value_example"
            }],
            "request_post_body": "request_post_body_example",
            "verify_response_content": "verify_response_content_example",
            "verify_response_codes": []
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "monitor_id",
        ]

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitor,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            monitor_id=self.module.params.get("monitor_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "script_id",
            "monitor_type",
            "status",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_monitors,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


MonitorFactsHelperCustom = get_custom_class("MonitorFactsHelperCustom")


class ResourceFactsHelper(MonitorFactsHelperCustom, MonitorFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            monitor_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            script_id=dict(type="str"),
            monitor_type=dict(type="str"),
            status=dict(type="str", choices=["ENABLED", "DISABLED", "INVALID"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "displayName",
                    "timeCreated",
                    "timeUpdated",
                    "status",
                    "monitorType",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="monitor",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(monitors=result)


if __name__ == "__main__":
    main()
