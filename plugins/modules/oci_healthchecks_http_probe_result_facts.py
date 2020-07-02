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
module: oci_healthchecks_http_probe_result_facts
short_description: Fetches details about one or multiple HttpProbeResult resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HttpProbeResult resources in Oracle Cloud Infrastructure
    - Gets the HTTP probe results for the specified probe or monitor, where
      the `probeConfigurationId` is the OCID of either a monitor or an
      on-demand probe.
version_added: "2.9"
author: Oracle (@oracle)
options:
    probe_configuration_id:
        description:
            - The OCID of a monitor or on-demand probe.
        type: str
        required: true
    start_time_greater_than_or_equal_to:
        description:
            - Returns results with a `startTime` equal to or greater than the specified value.
        type: float
    start_time_less_than_or_equal_to:
        description:
            - Returns results with a `startTime` equal to or less than the specified value.
        type: float
    sort_order:
        description:
            - Controls the sort order of results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    target:
        description:
            - Filters results that match the `target`.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List http_probe_results
  oci_healthchecks_http_probe_result_facts:
    probe_configuration_id: ocid1.probeconfiguration.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
http_probe_results:
    description:
        - List of HttpProbeResult resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - A value identifying this specific probe result. The key is only unique within
                  the results of its probe configuration. The key may be reused after 90 days.
            returned: on success
            type: string
            sample: key_example
        probe_configuration_id:
            description:
                - The OCID of the monitor or on-demand probe responsible for creating this result.
            returned: on success
            type: string
            sample: ocid1.probeconfiguration.oc1..xxxxxxEXAMPLExxxxxx
        start_time:
            description:
                - The date and time the probe was executed, expressed in milliseconds since the
                  POSIX epoch. This field is defined by the PerformanceResourceTiming interface
                  of the W3C Resource Timing specification. For more information, see
                  L(Resource Timing,https://w3c.github.io/resource-timing/#sec-resource-timing).
            returned: on success
            type: float
            sample: 1.2
        target:
            description:
                - The target hostname or IP address of the probe.
            returned: on success
            type: string
            sample: target_example
        vantage_point_name:
            description:
                - The name of the vantage point that executed the probe.
            returned: on success
            type: string
            sample: vantage_point_name_example
        is_timed_out:
            description:
                - True if the probe did not complete before the configured `timeoutInSeconds` value.
            returned: on success
            type: bool
            sample: true
        is_healthy:
            description:
                - True if the probe result is determined to be healthy based on probe
                  type-specific criteria.  For HTTP probes, a probe result is considered
                  healthy if the HTTP response code is greater than or equal to 200 and
                  less than 300.
            returned: on success
            type: bool
            sample: true
        error_category:
            description:
                - "The category of error if an error occurs executing the probe.
                  The `errorMessage` field provides a message with the error details.
                  * NONE - No error
                  * DNS - DNS errors
                  * TRANSPORT - Transport-related errors, for example a \\"TLS certificate expired\\" error.
                  * NETWORK - Network-related errors, for example a \\"network unreachable\\" error.
                  * SYSTEM - Internal system errors."
            returned: on success
            type: string
            sample: NONE
        error_message:
            description:
                - The error information indicating why a probe execution failed.
            returned: on success
            type: string
            sample: error_message_example
        protocol:
            description:
                - ""
            returned: on success
            type: string
            sample: HTTP
        connection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                address:
                    description:
                        - The connection IP address.
                    returned: on success
                    type: string
                    sample: address_example
                port:
                    description:
                        - The port.
                    returned: on success
                    type: int
                    sample: 56
                connect_duration:
                    description:
                        - Total connect duration, calculated using `connectEnd` minus `connectStart`.
                    returned: on success
                    type: float
                    sample: 1.2
                secure_connect_duration:
                    description:
                        - The duration to secure the connection.  This value will be zero for
                          insecure connections.  Calculated using `connectEnd` minus `secureConnectionStart`.
                    returned: on success
                    type: float
                    sample: 1.2
        dns:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                domain_lookup_duration:
                    description:
                        - Total DNS resolution duration, in milliseconds. Calculated using `domainLookupEnd`
                          minus `domainLookupStart`.
                    returned: on success
                    type: float
                    sample: 1.2
                addresses:
                    description:
                        - The addresses returned by DNS resolution.
                    returned: on success
                    type: list
                    sample: []
        status_code:
            description:
                - The HTTP response status code.
            returned: on success
            type: int
            sample: 56
        domain_lookup_start:
            description:
                - The time immediately before the vantage point starts the domain name lookup for
                  the resource.
            returned: on success
            type: float
            sample: 1.2
        domain_lookup_end:
            description:
                - The time immediately before the vantage point finishes the domain name lookup for
                  the resource.
            returned: on success
            type: float
            sample: 1.2
        connect_start:
            description:
                - The time immediately before the vantage point starts establishing the connection
                  to the server to retrieve the resource.
            returned: on success
            type: float
            sample: 1.2
        secure_connection_start:
            description:
                - The time immediately before the vantage point starts the handshake process to
                  secure the current connection.
            returned: on success
            type: float
            sample: 1.2
        connect_end:
            description:
                - The time immediately after the vantage point finishes establishing the connection
                  to the server to retrieve the resource.
            returned: on success
            type: float
            sample: 1.2
        fetch_start:
            description:
                - The time immediately before the vantage point starts to fetch the resource.
            returned: on success
            type: float
            sample: 1.2
        request_start:
            description:
                - The time immediately before the vantage point starts requesting the resource from
                  the server.
            returned: on success
            type: float
            sample: 1.2
        response_start:
            description:
                - The time immediately after the vantage point's HTTP parser receives the first byte
                  of the response.
            returned: on success
            type: float
            sample: 1.2
        response_end:
            description:
                - The time immediately after the vantage point receives the last byte of the response
                  or immediately before the transport connection is closed, whichever comes first.
            returned: on success
            type: float
            sample: 1.2
        duration:
            description:
                - The total duration from start of request until response is fully consumed or the
                  connection is closed.
            returned: on success
            type: float
            sample: 1.2
        encoded_body_size:
            description:
                - The size, in octets, of the payload body prior to removing any applied
                  content-codings.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "key": "key_example",
        "probe_configuration_id": "ocid1.probeconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
        "start_time": 1.2,
        "target": "target_example",
        "vantage_point_name": "vantage_point_name_example",
        "is_timed_out": true,
        "is_healthy": true,
        "error_category": "NONE",
        "error_message": "error_message_example",
        "protocol": "HTTP",
        "connection": {
            "address": "address_example",
            "port": 56,
            "connect_duration": 1.2,
            "secure_connect_duration": 1.2
        },
        "dns": {
            "domain_lookup_duration": 1.2,
            "addresses": []
        },
        "status_code": 56,
        "domain_lookup_start": 1.2,
        "domain_lookup_end": 1.2,
        "connect_start": 1.2,
        "secure_connection_start": 1.2,
        "connect_end": 1.2,
        "fetch_start": 1.2,
        "request_start": 1.2,
        "response_start": 1.2,
        "response_end": 1.2,
        "duration": 1.2,
        "encoded_body_size": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.healthchecks import HealthChecksClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpProbeResultFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "probe_configuration_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "start_time_greater_than_or_equal_to",
            "start_time_less_than_or_equal_to",
            "sort_order",
            "target",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_http_probe_results,
            probe_configuration_id=self.module.params.get("probe_configuration_id"),
            **optional_kwargs
        )


HttpProbeResultFactsHelperCustom = get_custom_class("HttpProbeResultFactsHelperCustom")


class ResourceFactsHelper(
    HttpProbeResultFactsHelperCustom, HttpProbeResultFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            probe_configuration_id=dict(type="str", required=True),
            start_time_greater_than_or_equal_to=dict(type="float"),
            start_time_less_than_or_equal_to=dict(type="float"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            target=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="http_probe_result",
        service_client_class=HealthChecksClient,
        namespace="healthchecks",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(http_probe_results=result)


if __name__ == "__main__":
    main()
