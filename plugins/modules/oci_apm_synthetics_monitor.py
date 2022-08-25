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
module: oci_apm_synthetics_monitor
short_description: Manage a Monitor resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Monitor resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new monitor.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    monitor_type:
        description:
            - Type of monitor.
            - Required for create using I(state=present).
        type: str
        choices:
            - "SCRIPTED_BROWSER"
            - "BROWSER"
            - "SCRIPTED_REST"
            - "REST"
    display_name:
        description:
            - Unique name that can be edited. The name should not contain any confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    vantage_points:
        description:
            - A list of public and dedicated vantage points from which to execute the monitor.
              Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    script_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the script.
              scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
            - This parameter is updatable.
        type: str
    status:
        description:
            - Enables or disables the monitor.
            - This parameter is updatable.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
            - "INVALID"
    repeat_interval_in_seconds:
        description:
            - Interval in seconds after the start time when the job should be repeated.
              Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_run_once:
        description:
            - If runOnce is enabled, then the monitor will run once.
            - This parameter is updatable.
        type: bool
    timeout_in_seconds:
        description:
            - Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors.
              Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors.
              Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.
            - This parameter is updatable.
        type: int
    target:
        description:
            - Specify the endpoint on which to run the monitor.
              For BROWSER and REST monitor types, target is mandatory.
              If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor)
              against the specified target endpoint.
              If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.
            - This parameter is updatable.
        type: str
    script_parameters:
        description:
            - "List of script parameters in the monitor.
              This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
              Example: `[{\\"paramName\\": \\"userid\\", \\"paramValue\\":\\"testuser\\"}]`"
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            param_name:
                description:
                    - Name of the parameter.
                type: str
                required: true
            param_value:
                description:
                    - Value of the parameter.
                type: str
                required: true
    configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_redirection_enabled:
                description:
                    - If redirection enabled, then redirects will be allowed while accessing target URL.
                    - Applicable when config_type is 'REST_CONFIG'
                type: bool
            request_method:
                description:
                    - Request HTTP method.
                    - Applicable when config_type is 'REST_CONFIG'
                type: str
                choices:
                    - "GET"
                    - "POST"
            req_authentication_scheme:
                description:
                    - Request http authentication scheme.
                    - Applicable when config_type is 'REST_CONFIG'
                type: str
                choices:
                    - "OAUTH"
                    - "NONE"
                    - "BASIC"
                    - "BEARER"
            req_authentication_details:
                description:
                    - ""
                    - Applicable when config_type is 'REST_CONFIG'
                type: dict
                suboptions:
                    oauth_scheme:
                        description:
                            - Request http oauth scheme.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
                        choices:
                            - "NONE"
                            - "BASIC"
                    auth_user_name:
                        description:
                            - Username for authentication.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
                    auth_user_password:
                        description:
                            - User password for authentication.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
                    auth_token:
                        description:
                            - Authentication token.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
                    auth_url:
                        description:
                            - URL to get authetication token.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
                    auth_headers:
                        description:
                            - "List of authentication headers. Example: `[{\\"headerName\\": \\"content-type\\", \\"headerValue\\":\\"json\\"}]`"
                            - Applicable when config_type is 'REST_CONFIG'
                        type: list
                        elements: dict
                        suboptions:
                            header_name:
                                description:
                                    - Name of the header.
                                    - Required when config_type is 'REST_CONFIG'
                                type: str
                                required: true
                            header_value:
                                description:
                                    - Value of the header.
                                    - Applicable when config_type is 'REST_CONFIG'
                                type: str
                    auth_request_method:
                        description:
                            - Request method.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
                        choices:
                            - "GET"
                            - "POST"
                    auth_request_post_body:
                        description:
                            - Request post body.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
            request_headers:
                description:
                    - "List of request headers. Example: `[{\\"headerName\\": \\"content-type\\", \\"headerValue\\":\\"json\\"}]`"
                    - Applicable when config_type is 'REST_CONFIG'
                type: list
                elements: dict
                suboptions:
                    header_name:
                        description:
                            - Name of the header.
                            - Required when config_type is 'REST_CONFIG'
                        type: str
                        required: true
                    header_value:
                        description:
                            - Value of the header.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
            request_query_params:
                description:
                    - "List of request query params. Example: `[{\\"paramName\\": \\"sortOrder\\", \\"paramValue\\": \\"asc\\"}]`"
                    - Applicable when config_type is 'REST_CONFIG'
                type: list
                elements: dict
                suboptions:
                    param_name:
                        description:
                            - Name of request query parameter.
                            - Required when config_type is 'REST_CONFIG'
                        type: str
                        required: true
                    param_value:
                        description:
                            - Value of request query parameter.
                            - Applicable when config_type is 'REST_CONFIG'
                        type: str
            request_post_body:
                description:
                    - Request post body content.
                    - Applicable when config_type is 'REST_CONFIG'
                type: str
            verify_response_content:
                description:
                    - Verify response content against regular expression based string.
                      If response content does not match the verifyResponseContent value, then it will be considered a failure.
                    - Applicable when config_type is 'REST_CONFIG'
                type: str
            verify_response_codes:
                description:
                    - Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.
                    - Applicable when config_type is 'REST_CONFIG'
                type: list
                elements: str
            config_type:
                description:
                    - Type of configuration.
                type: str
                choices:
                    - "SCRIPTED_REST_CONFIG"
                    - "SCRIPTED_BROWSER_CONFIG"
                    - "REST_CONFIG"
                    - "BROWSER_CONFIG"
                required: true
            is_failure_retried:
                description:
                    - If isFailureRetried is enabled, then a failed call will be retried.
                type: bool
            dns_configuration:
                description:
                    - ""
                type: dict
                suboptions:
                    is_override_dns:
                        description:
                            - If isOverrideDns is true, then dns will be overridden.
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: bool
                    override_dns_ip:
                        description:
                            - "Override dns ip value. This value will be honored only if *ref-isOverrideDns is set to true."
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: str
            is_certificate_validation_enabled:
                description:
                    - If certificate validation is enabled, then the call will fail in case of certification errors.
                    - Applicable when config_type is one of ['SCRIPTED_BROWSER_CONFIG', 'REST_CONFIG', 'BROWSER_CONFIG']
                type: bool
            verify_texts:
                description:
                    - Verifies all the search strings present in the response.
                      If any search string is not present in the response, then it will be considered as a failure.
                    - Applicable when config_type is 'BROWSER_CONFIG'
                type: list
                elements: dict
                suboptions:
                    text:
                        description:
                            - Verification text in the response.
                            - Applicable when config_type is 'BROWSER_CONFIG'
                        type: str
            network_configuration:
                description:
                    - ""
                type: dict
                suboptions:
                    number_of_hops:
                        description:
                            - Number of hops.
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: int
                    probe_per_hop:
                        description:
                            - Number of probes per hop.
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: int
                    transmission_rate:
                        description:
                            - Number of probe packets sent out simultaneously.
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: int
                    protocol:
                        description:
                            - Type of protocol.
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: str
                        choices:
                            - "ICMP"
                            - "TCP"
                    probe_mode:
                        description:
                            - Type of probe mode when TCP protocol is selected.
                            - Applicable when config_type is 'SCRIPTED_REST_CONFIG'
                        type: str
                        choices:
                            - "SACK"
                            - "SYN"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    is_run_now:
        description:
            - If isRunNow is enabled, then the monitor will run now.
            - This parameter is updatable.
        type: bool
    scheduling_policy:
        description:
            - Scheduling policy on Vantage points.
            - This parameter is updatable.
        type: str
        choices:
            - "ALL"
            - "ROUND_ROBIN"
            - "BATCHED_ROUND_ROBIN"
    batch_interval_in_seconds:
        description:
            - "Time interval between 2 runs in round robin batch mode (*SchedulingPolicy - BATCHED_ROUND_ROBIN)."
            - This parameter is updatable.
        type: int
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    monitor_id:
        description:
            - The OCID of the monitor.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Monitor.
            - Use I(state=present) to create or update a Monitor.
            - Use I(state=absent) to delete a Monitor.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create monitor
  oci_apm_synthetics_monitor:
    # required
    monitor_type: SCRIPTED_BROWSER
    display_name: display_name_example
    vantage_points: [ "vantage_points_example" ]
    repeat_interval_in_seconds: 56
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"
    status: ENABLED
    is_run_once: true
    timeout_in_seconds: 56
    target: target_example
    script_parameters:
    - # required
      param_name: param_name_example
      param_value: param_value_example
    configuration:
      # required
      config_type: SCRIPTED_REST_CONFIG

      # optional
      is_failure_retried: true
      dns_configuration:
        # optional
        is_override_dns: true
        override_dns_ip: override_dns_ip_example
      network_configuration:
        # optional
        number_of_hops: 56
        probe_per_hop: 56
        transmission_rate: 56
        protocol: ICMP
        probe_mode: SACK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_run_now: true
    scheduling_policy: ALL
    batch_interval_in_seconds: 56

- name: Update monitor
  oci_apm_synthetics_monitor:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    vantage_points: [ "vantage_points_example" ]
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"
    status: ENABLED
    repeat_interval_in_seconds: 56
    is_run_once: true
    timeout_in_seconds: 56
    target: target_example
    script_parameters:
    - # required
      param_name: param_name_example
      param_value: param_value_example
    configuration:
      # required
      config_type: SCRIPTED_REST_CONFIG

      # optional
      is_failure_retried: true
      dns_configuration:
        # optional
        is_override_dns: true
        override_dns_ip: override_dns_ip_example
      network_configuration:
        # optional
        number_of_hops: 56
        probe_per_hop: 56
        transmission_rate: 56
        protocol: ICMP
        probe_mode: SACK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_run_now: true
    scheduling_policy: ALL
    batch_interval_in_seconds: 56

- name: Update monitor using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_synthetics_monitor:
    # required
    display_name: display_name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    vantage_points: [ "vantage_points_example" ]
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"
    status: ENABLED
    repeat_interval_in_seconds: 56
    is_run_once: true
    timeout_in_seconds: 56
    target: target_example
    script_parameters:
    - # required
      param_name: param_name_example
      param_value: param_value_example
    configuration:
      # required
      config_type: SCRIPTED_REST_CONFIG

      # optional
      is_failure_retried: true
      dns_configuration:
        # optional
        is_override_dns: true
        override_dns_ip: override_dns_ip_example
      network_configuration:
        # optional
        number_of_hops: 56
        probe_per_hop: 56
        transmission_rate: 56
        protocol: ICMP
        probe_mode: SACK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_run_now: true
    scheduling_policy: ALL
    batch_interval_in_seconds: 56

- name: Delete monitor
  oci_apm_synthetics_monitor:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete monitor using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_synthetics_monitor:
    # required
    display_name: display_name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
monitor:
    description:
        - Details of the Monitor resource acted upon by the current operation
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
                - List of public and dedicated vantage points where the monitor is running.
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
                  Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST
                  monitor.
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
                  Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors.
                  Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.
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
            returned: on success
            type: complex
            contains:
                verify_texts:
                    description:
                        - Verifies all the search strings present in the response.
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
                is_certificate_validation_enabled:
                    description:
                        - If certificate validation is enabled, then the call will fail in case of certification errors.
                    returned: on success
                    type: bool
                    sample: true
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
                dns_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_override_dns:
                            description:
                                - If isOverrideDns is true, then dns will be overridden.
                            returned: on success
                            type: bool
                            sample: true
                        override_dns_ip:
                            description:
                                - "Override dns ip value. This value will be honored only if *ref-isOverrideDns is set to true."
                            returned: on success
                            type: str
                            sample: override_dns_ip_example
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
        is_run_now:
            description:
                - If isRunNow is enabled, then the monitor will run now.
            returned: on success
            type: bool
            sample: true
        scheduling_policy:
            description:
                - Scheduling policy on Vantage points.
            returned: on success
            type: str
            sample: ALL
        batch_interval_in_seconds:
            description:
                - "Time interval between 2 runs in round robin batch mode (*SchedulingPolicy - BATCHED_ROUND_ROBIN)."
            returned: on success
            type: int
            sample: 56
    sample: {
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
            "verify_texts": [{
                "text": "text_example"
            }],
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
            "verify_response_codes": [],
            "is_certificate_validation_enabled": true,
            "config_type": "BROWSER_CONFIG",
            "is_failure_retried": true,
            "dns_configuration": {
                "is_override_dns": true,
                "override_dns_ip": "override_dns_ip_example"
            },
            "network_configuration": {
                "number_of_hops": 56,
                "probe_per_hop": 56,
                "transmission_rate": 56,
                "protocol": "ICMP",
                "probe_mode": "SACK"
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_run_now": true,
        "scheduling_policy": "ALL",
        "batch_interval_in_seconds": 56
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
    from oci.apm_synthetics import ApmSyntheticClient
    from oci.apm_synthetics.models import CreateMonitorDetails
    from oci.apm_synthetics.models import UpdateMonitorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MonitorHelperGen, self).get_possible_entity_types() + [
            "monitor",
            "monitors",
            "apmSyntheticsmonitor",
            "apmSyntheticsmonitors",
            "monitorresource",
            "monitorsresource",
            "apmsynthetics",
        ]

    def get_module_resource_id_param(self):
        return "monitor_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitor_id")

    def get_get_fn(self):
        return self.client.get_monitor

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitor,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            monitor_id=self.module.params.get("monitor_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "apm_domain_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "monitor_type"]
            if self._use_name_as_identifier()
            else ["display_name", "script_id", "monitor_type", "status"]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_monitors, **kwargs)

    def get_create_model_class(self):
        return CreateMonitorDetails

    def get_exclude_attributes(self):
        return ["script_parameters.param_value", "script_parameters.param_name"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                create_monitor_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMonitorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                monitor_id=self.module.params.get("monitor_id"),
                update_monitor_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                monitor_id=self.module.params.get("monitor_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MonitorHelperCustom = get_custom_class("MonitorHelperCustom")


class ResourceHelper(MonitorHelperCustom, MonitorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            monitor_type=dict(
                type="str",
                choices=["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            vantage_points=dict(type="list", elements="str"),
            script_id=dict(type="str"),
            status=dict(type="str", choices=["ENABLED", "DISABLED", "INVALID"]),
            repeat_interval_in_seconds=dict(type="int"),
            is_run_once=dict(type="bool"),
            timeout_in_seconds=dict(type="int"),
            target=dict(type="str"),
            script_parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    param_name=dict(type="str", required=True),
                    param_value=dict(type="str", required=True),
                ),
            ),
            configuration=dict(
                type="dict",
                options=dict(
                    is_redirection_enabled=dict(type="bool"),
                    request_method=dict(type="str", choices=["GET", "POST"]),
                    req_authentication_scheme=dict(
                        type="str", choices=["OAUTH", "NONE", "BASIC", "BEARER"]
                    ),
                    req_authentication_details=dict(
                        type="dict",
                        options=dict(
                            oauth_scheme=dict(type="str", choices=["NONE", "BASIC"]),
                            auth_user_name=dict(type="str"),
                            auth_user_password=dict(type="str", no_log=True),
                            auth_token=dict(type="str", no_log=True),
                            auth_url=dict(type="str"),
                            auth_headers=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    header_name=dict(type="str", required=True),
                                    header_value=dict(type="str"),
                                ),
                            ),
                            auth_request_method=dict(
                                type="str", choices=["GET", "POST"]
                            ),
                            auth_request_post_body=dict(type="str"),
                        ),
                    ),
                    request_headers=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            header_name=dict(type="str", required=True),
                            header_value=dict(type="str"),
                        ),
                    ),
                    request_query_params=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            param_name=dict(type="str", required=True),
                            param_value=dict(type="str"),
                        ),
                    ),
                    request_post_body=dict(type="str"),
                    verify_response_content=dict(type="str"),
                    verify_response_codes=dict(type="list", elements="str"),
                    config_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "SCRIPTED_REST_CONFIG",
                            "SCRIPTED_BROWSER_CONFIG",
                            "REST_CONFIG",
                            "BROWSER_CONFIG",
                        ],
                    ),
                    is_failure_retried=dict(type="bool"),
                    dns_configuration=dict(
                        type="dict",
                        options=dict(
                            is_override_dns=dict(type="bool"),
                            override_dns_ip=dict(type="str"),
                        ),
                    ),
                    is_certificate_validation_enabled=dict(type="bool"),
                    verify_texts=dict(
                        type="list",
                        elements="dict",
                        options=dict(text=dict(type="str")),
                    ),
                    network_configuration=dict(
                        type="dict",
                        options=dict(
                            number_of_hops=dict(type="int"),
                            probe_per_hop=dict(type="int"),
                            transmission_rate=dict(type="int"),
                            protocol=dict(type="str", choices=["ICMP", "TCP"]),
                            probe_mode=dict(type="str", choices=["SACK", "SYN"]),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_run_now=dict(type="bool"),
            scheduling_policy=dict(
                type="str", choices=["ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN"]
            ),
            batch_interval_in_seconds=dict(type="int"),
            apm_domain_id=dict(type="str", required=True),
            monitor_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="monitor",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
