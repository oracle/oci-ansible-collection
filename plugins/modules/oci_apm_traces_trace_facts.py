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
module: oci_apm_traces_trace_facts
short_description: Fetches details about a Trace resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Trace resource in Oracle Cloud Infrastructure
    - Gets the trace details identified by traceId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
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
- name: Get a specific trace
  oci_apm_traces_trace_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    trace_key: trace_key_example

"""

RETURN = """
trace:
    description:
        - Trace resource
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique identifier (traceId) for the trace that represents the span set.  Note that this field is
                  defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance
                  Monitoring.
            returned: on success
            type: str
            sample: key_example
        root_span_operation_name:
            description:
                - Root span name associated with the trace. This is the flow start operation name.
                  Null is displayed if the root span is not yet completed.
            returned: on success
            type: str
            sample: root_span_operation_name_example
        time_earliest_span_started:
            description:
                - Start time of the earliest span in the span collection.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_latest_span_ended:
            description:
                - End time of the span that most recently ended in the span collection.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        span_count:
            description:
                - The number of spans that have been processed by the system for the trace.  Note that there
                  could be additional spans that have not been processed or reported yet if the trace is still
                  in progress.
            returned: on success
            type: int
            sample: 56
        error_span_count:
            description:
                - The number of spans with errors that have been processed by the system for the trace.
                  Note that the number of spans with errors will be less than or equal to the total number of spans in the trace.
            returned: on success
            type: int
            sample: 56
        root_span_service_name:
            description:
                - Service associated with the trace.
            returned: on success
            type: str
            sample: root_span_service_name_example
        time_root_span_started:
            description:
                - Start time of the root span for the span collection.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_root_span_ended:
            description:
                - End time of the root span for the span collection.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        root_span_duration_in_ms:
            description:
                - Time taken for the root span operation to complete in milliseconds.
            returned: on success
            type: int
            sample: 56
        trace_duration_in_ms:
            description:
                - Time between the start of the earliest span and the end of the most recent span in milliseconds.
            returned: on success
            type: int
            sample: 56
        is_fault:
            description:
                - Boolean flag that indicates whether the trace has an error.
            returned: on success
            type: bool
            sample: true
        trace_status:
            description:
                - "The status of the trace.
                  The trace statuses are defined as follows:
                  complete - a root span has been recorded, but there is no information on the errors.
                  success - a complete root span is recorded there is a successful error type and error code - HTTP 200.
                  incomplete - the root span has not yet been received.
                  error - the root span returned with an error. There may or may not be an associated error code or error type."
            returned: on success
            type: str
            sample: trace_status_example
        trace_error_type:
            description:
                - Error type of the trace.
            returned: on success
            type: str
            sample: trace_error_type_example
        trace_error_code:
            description:
                - Error code of the trace.
            returned: on success
            type: str
            sample: trace_error_code_example
        service_summaries:
            description:
                - A summary of the spans by service.
            returned: on success
            type: complex
            contains:
                span_service_name:
                    description:
                        - Name associated with the service.
                    returned: on success
                    type: str
                    sample: span_service_name_example
                total_spans:
                    description:
                        - Number of spans for serviceName in the trace.
                    returned: on success
                    type: int
                    sample: 56
                error_spans:
                    description:
                        - Number of spans with errors for serviceName in the trace.
                    returned: on success
                    type: int
                    sample: 56
        span_summary:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique identifier (traceId) for the trace that represents the span set.  Note that this field is
                          defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance
                          Monitoring.
                    returned: on success
                    type: str
                    sample: key_example
                root_span_operation_name:
                    description:
                        - Root span name associated with the trace. This is the flow start operation name.
                          Null is displayed if the root span is not yet completed.
                    returned: on success
                    type: str
                    sample: root_span_operation_name_example
                time_earliest_span_started:
                    description:
                        - Start time of the earliest span in the span collection.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_latest_span_ended:
                    description:
                        - End time of the span that most recently ended in the span collection.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                span_count:
                    description:
                        - The number of spans that have been processed by the system for the trace.  Note that there
                          could be additional spans that have not been processed or reported yet if the trace is still
                          in progress.
                    returned: on success
                    type: int
                    sample: 56
                error_span_count:
                    description:
                        - The number of spans with errors that have been processed by the system for the trace.
                          Note that the number of spans with errors will be less than or equal to the total number of spans in the trace.
                    returned: on success
                    type: int
                    sample: 56
                root_span_service_name:
                    description:
                        - Service associated with the trace.
                    returned: on success
                    type: str
                    sample: root_span_service_name_example
                time_root_span_started:
                    description:
                        - Start time of the root span for the span collection.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_root_span_ended:
                    description:
                        - End time of the root span for the span collection.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                root_span_duration_in_ms:
                    description:
                        - Time taken for the root span operation to complete in milliseconds.
                    returned: on success
                    type: int
                    sample: 56
                trace_duration_in_ms:
                    description:
                        - Time between the start of the earliest span and the end of the most recent span in milliseconds.
                    returned: on success
                    type: int
                    sample: 56
                is_fault:
                    description:
                        - Boolean flag that indicates whether the trace has an error.
                    returned: on success
                    type: bool
                    sample: true
                trace_status:
                    description:
                        - "The status of the trace.
                          The trace statuses are defined as follows:
                          complete - a root span has been recorded, but there is no information on the errors.
                          success - a complete root span is recorded there is a successful error type and error code - HTTP 200.
                          incomplete - the root span has not yet been received.
                          error - the root span returned with an error. There may or may not be an associated error code or error type."
                    returned: on success
                    type: str
                    sample: trace_status_example
                trace_error_type:
                    description:
                        - Error type of the trace.
                    returned: on success
                    type: str
                    sample: trace_error_type_example
                trace_error_code:
                    description:
                        - Error code of the trace.
                    returned: on success
                    type: str
                    sample: trace_error_code_example
                service_summaries:
                    description:
                        - A summary of the spans by service.
                    returned: on success
                    type: complex
                    contains:
                        span_service_name:
                            description:
                                - Name associated with the service.
                            returned: on success
                            type: str
                            sample: span_service_name_example
                        total_spans:
                            description:
                                - Number of spans for serviceName in the trace.
                            returned: on success
                            type: int
                            sample: 56
                        error_spans:
                            description:
                                - Number of spans with errors for serviceName in the trace.
                            returned: on success
                            type: int
                            sample: 56
        spans:
            description:
                - An array of spans in the trace.
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
        "root_span_operation_name": "root_span_operation_name_example",
        "time_earliest_span_started": "2013-10-20T19:20:30+01:00",
        "time_latest_span_ended": "2013-10-20T19:20:30+01:00",
        "span_count": 56,
        "error_span_count": 56,
        "root_span_service_name": "root_span_service_name_example",
        "time_root_span_started": "2013-10-20T19:20:30+01:00",
        "time_root_span_ended": "2013-10-20T19:20:30+01:00",
        "root_span_duration_in_ms": 56,
        "trace_duration_in_ms": 56,
        "is_fault": true,
        "trace_status": "trace_status_example",
        "trace_error_type": "trace_error_type_example",
        "trace_error_code": "trace_error_code_example",
        "service_summaries": [{
            "span_service_name": "span_service_name_example",
            "total_spans": 56,
            "error_spans": 56
        }],
        "span_summary": {
            "key": "key_example",
            "root_span_operation_name": "root_span_operation_name_example",
            "time_earliest_span_started": "2013-10-20T19:20:30+01:00",
            "time_latest_span_ended": "2013-10-20T19:20:30+01:00",
            "span_count": 56,
            "error_span_count": 56,
            "root_span_service_name": "root_span_service_name_example",
            "time_root_span_started": "2013-10-20T19:20:30+01:00",
            "time_root_span_ended": "2013-10-20T19:20:30+01:00",
            "root_span_duration_in_ms": 56,
            "trace_duration_in_ms": 56,
            "is_fault": true,
            "trace_status": "trace_status_example",
            "trace_error_type": "trace_error_type_example",
            "trace_error_code": "trace_error_code_example",
            "service_summaries": [{
                "span_service_name": "span_service_name_example",
                "total_spans": 56,
                "error_spans": 56
            }]
        },
        "spans": [{
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
        }]
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


class TraceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "trace_key",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_trace,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            trace_key=self.module.params.get("trace_key"),
        )


TraceFactsHelperCustom = get_custom_class("TraceFactsHelperCustom")


class ResourceFactsHelper(TraceFactsHelperCustom, TraceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            trace_key=dict(type="str", required=True, no_log=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="trace",
        service_client_class=TraceClient,
        namespace="apm_traces",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(trace=result)


if __name__ == "__main__":
    main()
