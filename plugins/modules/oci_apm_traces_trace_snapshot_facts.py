#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_apm_traces_trace_snapshot_facts
short_description: Fetches details about a TraceSnapshot resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a TraceSnapshot resource in Oracle Cloud Infrastructure
    - Gets the trace snapshots data identified by trace ID.
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
    is_summarized:
        description:
            - If enabled, then only span level details will be sent.
        type: bool
    thread_id:
        description:
            - Thread id for which snapshots needs to be retrieved. This is an identifier of a thread, and is a positive long number generated when when a thread
              is created.
        type: str
    snapshot_time:
        description:
            - Epoch time of snapshot.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific trace_snapshot
  oci_apm_traces_trace_snapshot_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    trace_key: trace_key_example

    # optional
    is_summarized: true
    thread_id: "ocid1.thread.oc1..xxxxxxEXAMPLExxxxxx"
    snapshot_time: snapshot_time_example

"""

RETURN = """
trace_snapshot:
    description:
        - TraceSnapshot resource
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
        time_started:
            description:
                - Start time of the trace.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - End time of the trace.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        trace_snapshot_details:
            description:
                - Trace snapshots properties.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Name of the property.
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - Value of the property.
                    returned: on success
                    type: dict
                    sample: {}
        span_snapshots:
            description:
                - List of spans.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique identifier (spanId) for the trace span.
                    returned: on success
                    type: str
                    sample: key_example
                span_name:
                    description:
                        - Span name associated with the trace.
                    returned: on success
                    type: str
                    sample: span_name_example
                time_started:
                    description:
                        - Start time of the span.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_ended:
                    description:
                        - End time of the span.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                span_snapshot_details:
                    description:
                        - Span snapshots properties.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - Name of the property.
                            returned: on success
                            type: str
                            sample: key_example
                        value:
                            description:
                                - Value of the property.
                            returned: on success
                            type: dict
                            sample: {}
                thread_snapshots:
                    description:
                        - Thread snapshots.
                    returned: on success
                    type: complex
                    contains:
                        time_stamp:
                            description:
                                - Snapshot time.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        thread_snapshot_details:
                            description:
                                - Snapshot details.
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - Name of the property.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                value:
                                    description:
                                        - Value of the property.
                                    returned: on success
                                    type: dict
                                    sample: {}
                        stack_trace:
                            description:
                                - Stack trace.
                            returned: on success
                            type: complex
                            contains:
                                method_name:
                                    description:
                                        - Name of the method containing the execution point.
                                    returned: on success
                                    type: str
                                    sample: method_name_example
                                file_name:
                                    description:
                                        - Name of the source file containing the execution point.
                                    returned: on success
                                    type: str
                                    sample: file_name_example
                                line_number:
                                    description:
                                        - Line number of the source line containing the execution point.
                                    returned: on success
                                    type: int
                                    sample: 56
                                class_name:
                                    description:
                                        - Name of the class containing the execution point.
                                    returned: on success
                                    type: str
                                    sample: class_name_example
                                weightage:
                                    description:
                                        - The weight distribution that denotes the percentage occurrence of a method in the captured snapshots.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                children:
                    description:
                        - An array of child span snapshots.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - Unique identifier (spanId) for the trace span.
                            returned: on success
                            type: str
                            sample: key_example
                        span_name:
                            description:
                                - Span name associated with the trace.
                            returned: on success
                            type: str
                            sample: span_name_example
                        time_started:
                            description:
                                - Start time of the span.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_ended:
                            description:
                                - End time of the span.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        span_snapshot_details:
                            description:
                                - Span snapshots properties.
                            returned: on success
                            type: list
                            sample: []
                        thread_snapshots:
                            description:
                                - Thread snapshots.
                            returned: on success
                            type: list
                            sample: []
                        children:
                            description:
                                - An array of child span snapshots.
                            returned: on success
                            type: list
                            sample: []
    sample: {
        "key": "key_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "trace_snapshot_details": [{
            "key": "key_example",
            "value": {}
        }],
        "span_snapshots": [{
            "key": "key_example",
            "span_name": "span_name_example",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_ended": "2013-10-20T19:20:30+01:00",
            "span_snapshot_details": [{
                "key": "key_example",
                "value": {}
            }],
            "thread_snapshots": [{
                "time_stamp": "2013-10-20T19:20:30+01:00",
                "thread_snapshot_details": [{
                    "key": "key_example",
                    "value": {}
                }],
                "stack_trace": [{
                    "method_name": "method_name_example",
                    "file_name": "file_name_example",
                    "line_number": 56,
                    "class_name": "class_name_example",
                    "weightage": 3.4
                }]
            }],
            "children": [{
                "key": "key_example",
                "span_name": "span_name_example",
                "time_started": "2013-10-20T19:20:30+01:00",
                "time_ended": "2013-10-20T19:20:30+01:00",
                "span_snapshot_details": [],
                "thread_snapshots": [],
                "children": []
            }]
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


class TraceSnapshotFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "trace_key",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "is_summarized",
            "thread_id",
            "snapshot_time",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_trace_snapshot,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            trace_key=self.module.params.get("trace_key"),
            **optional_kwargs
        )


TraceSnapshotFactsHelperCustom = get_custom_class("TraceSnapshotFactsHelperCustom")


class ResourceFactsHelper(TraceSnapshotFactsHelperCustom, TraceSnapshotFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            trace_key=dict(type="str", required=True, no_log=True),
            is_summarized=dict(type="bool"),
            thread_id=dict(type="str"),
            snapshot_time=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="trace_snapshot",
        service_client_class=TraceClient,
        namespace="apm_traces",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(trace_snapshot=result)


if __name__ == "__main__":
    main()
