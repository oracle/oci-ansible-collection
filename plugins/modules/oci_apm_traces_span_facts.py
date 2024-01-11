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
module: oci_apm_traces_span_facts
short_description: Fetches details about a Span resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Span resource in Oracle Cloud Infrastructure
    - Gets the span details identified by spanId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
        type: str
        required: true
    span_key:
        description:
            - Unique Application Performance Monitoring span identifier (spanId).
        type: str
        required: true
    trace_key:
        description:
            - Unique Application Performance Monitoring trace identifier (traceId).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific span
  oci_apm_traces_span_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    span_key: span_key_example
    trace_key: trace_key_example

"""

RETURN = """
span:
    description:
        - Span resource
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique identifier (spanId) for the span.  Note that this field is
                  defined as spanKey in the API and it maps to the spanId in the trace data
                  in Application Performance Monitoring.
            returned: on success
            type: str
            sample: key_example
        parent_span_key:
            description:
                - Unique parent identifier for the span if one exists. For root spans this will be null.
            returned: on success
            type: str
            sample: parent_span_key_example
        trace_key:
            description:
                - Unique identifier for the trace.
            returned: on success
            type: str
            sample: trace_key_example
        time_started:
            description:
                - Span start time.  Timestamp when the span was started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - Span end time.  Timestamp when the span was completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        duration_in_ms:
            description:
                - Total span duration in milliseconds.
            returned: on success
            type: int
            sample: 56
        operation_name:
            description:
                - Span name associated with the trace.  This is usually the method or URI of the request.
            returned: on success
            type: str
            sample: operation_name_example
        service_name:
            description:
                - Service name associated with the span.
            returned: on success
            type: str
            sample: service_name_example
        kind:
            description:
                - Kind associated with the span.
            returned: on success
            type: str
            sample: kind_example
        tags:
            description:
                - List of tags associated with the span.
            returned: on success
            type: complex
            contains:
                tag_name:
                    description:
                        - Key that specifies the tag name.
                    returned: on success
                    type: str
                    sample: tag_name_example
                tag_value:
                    description:
                        - Value associated with the tag key.
                    returned: on success
                    type: str
                    sample: tag_value_example
        logs:
            description:
                - List of logs associated with the span.
            returned: on success
            type: complex
            contains:
                time_created:
                    description:
                        - Timestamp at which the log is created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                span_logs:
                    description:
                        - List of logs associated with the span at the given timestamp.
                    returned: on success
                    type: complex
                    contains:
                        log_key:
                            description:
                                - Key that specifies the log name.
                            returned: on success
                            type: str
                            sample: log_key_example
                        log_value:
                            description:
                                - Value associated with the log key.
                            returned: on success
                            type: str
                            sample: log_value_example
        is_error:
            description:
                - Indicates if the span has an error.
            returned: on success
            type: bool
            sample: true
    sample: {
        "key": "key_example",
        "parent_span_key": "parent_span_key_example",
        "trace_key": "trace_key_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "duration_in_ms": 56,
        "operation_name": "operation_name_example",
        "service_name": "service_name_example",
        "kind": "kind_example",
        "tags": [{
            "tag_name": "tag_name_example",
            "tag_value": "tag_value_example"
        }],
        "logs": [{
            "time_created": "2013-10-20T19:20:30+01:00",
            "span_logs": [{
                "log_key": "log_key_example",
                "log_value": "log_value_example"
            }]
        }],
        "is_error": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apm_traces import TraceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SpanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "span_key",
            "trace_key",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_span,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            span_key=self.module.params.get("span_key"),
            trace_key=self.module.params.get("trace_key"),
        )


SpanFactsHelperCustom = get_custom_class("SpanFactsHelperCustom")


class ResourceFactsHelper(SpanFactsHelperCustom, SpanFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            span_key=dict(type="str", required=True, no_log=True),
            trace_key=dict(type="str", required=True, no_log=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="span",
        service_client_class=TraceClient,
        namespace="apm_traces",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(span=result)


if __name__ == "__main__":
    main()
