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
module: oci_apm_traces_aggregated_snapshot_facts
short_description: Fetches details about a AggregatedSnapshot resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AggregatedSnapshot resource in Oracle Cloud Infrastructure
    - Gets the aggregated snapshot identified by trace ID.
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
- name: Get a specific aggregated_snapshot
  oci_apm_traces_aggregated_snapshot_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    trace_key: trace_key_example

"""

RETURN = """
aggregated_snapshot:
    description:
        - AggregatedSnapshot resource
    returned: on success
    type: complex
    contains:
        details:
            description:
                - Aggregated snapshot details.
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
        aggregated_stack_traces:
            description:
                - List of aggregated stack trace.
            returned: on success
            type: complex
            contains:
                stack_trace_element:
                    description:
                        - ""
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
                        - List of child aggregated stack trace to represent branches.
                    returned: on success
                    type: complex
                    contains:
                        stack_trace_element:
                            description:
                                - ""
                            returned: on success
                            type: StackTraceElement
                            sample: "null"

                        children:
                            description:
                                - List of child aggregated stack trace to represent branches.
                            returned: on success
                            type: list
                            sample: []
    sample: {
        "details": [{
            "key": "key_example",
            "value": {}
        }],
        "aggregated_stack_traces": [{
            "stack_trace_element": {
                "method_name": "method_name_example",
                "file_name": "file_name_example",
                "line_number": 56,
                "class_name": "class_name_example",
                "weightage": 3.4
            },
            "children": [{
                "stack_trace_element": null,
                "children": []
            }]
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_traces import TraceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AggregatedSnapshotFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "trace_key",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_aggregated_snapshot,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            trace_key=self.module.params.get("trace_key"),
        )


AggregatedSnapshotFactsHelperCustom = get_custom_class(
    "AggregatedSnapshotFactsHelperCustom"
)


class ResourceFactsHelper(
    AggregatedSnapshotFactsHelperCustom, AggregatedSnapshotFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            trace_key=dict(type="str", required=True, no_log=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="aggregated_snapshot",
        service_client_class=TraceClient,
        namespace="apm_traces",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(aggregated_snapshot=result)


if __name__ == "__main__":
    main()
