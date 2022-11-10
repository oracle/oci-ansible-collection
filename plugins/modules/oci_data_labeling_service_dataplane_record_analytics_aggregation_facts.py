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
module: oci_data_labeling_service_dataplane_record_analytics_aggregation_facts
short_description: Fetches details about one or multiple RecordAnalyticsAggregation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RecordAnalyticsAggregation resources in Oracle Cloud Infrastructure
    - Summarize the records created for a given dataset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    dataset_id:
        description:
            - Filter the results by the OCID of the dataset.
        type: str
        required: true
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
            - "DELETED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    record_group_by:
        description:
            - The field to group by. If no value is specified isLabeled is used by default.
        type: str
        choices:
            - "isLabeled"
            - "annotationLabelContains"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. The default order is descending. If no value is specified, count is used by default.
        type: str
        choices:
            - "count"
            - "isLabeled"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List record_analytics_aggregations
  oci_data_labeling_service_dataplane_record_analytics_aggregation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    sort_order: ASC
    record_group_by: isLabeled
    sort_by: count

"""

RETURN = """
record_analytics_aggregations:
    description:
        - List of RecordAnalyticsAggregation resources
    returned: on success
    type: complex
    contains:
        count:
            description:
                - the count of the matching results
            returned: on success
            type: float
            sample: 10
        dimensions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_labeled:
                    description:
                        - Whether or not the record has been labeled and has associated annotations.
                    returned: on success
                    type: bool
                    sample: true
                annotation_label_contains:
                    description:
                        - Whether or not the annotation contains a label.
                    returned: on success
                    type: str
                    sample: annotation_label_contains_example
        dataset_id:
            description:
                - ocid of the dataset the annotation belongs to
            returned: on success
            type: str
            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - ocid of the compartment the records
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Describes the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_state_example
    sample: [{
        "count": 10,
        "dimensions": {
            "is_labeled": true,
            "annotation_label_contains": "annotation_label_contains_example"
        },
        "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "lifecycle_state_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_labeling_service_dataplane import DataLabelingClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecordAnalyticsAggregationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "dataset_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_order",
            "record_group_by",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_record_analytics,
            compartment_id=self.module.params.get("compartment_id"),
            dataset_id=self.module.params.get("dataset_id"),
            **optional_kwargs
        )


RecordAnalyticsAggregationFactsHelperCustom = get_custom_class(
    "RecordAnalyticsAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    RecordAnalyticsAggregationFactsHelperCustom,
    RecordAnalyticsAggregationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            dataset_id=dict(type="str", required=True),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE", "DELETED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            record_group_by=dict(
                type="str", choices=["isLabeled", "annotationLabelContains"]
            ),
            sort_by=dict(type="str", choices=["count", "isLabeled"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="record_analytics_aggregation",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(record_analytics_aggregations=result)


if __name__ == "__main__":
    main()
