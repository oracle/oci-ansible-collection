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
module: oci_data_labeling_service_dataplane_annotation_analytics_aggregation_facts
short_description: Fetches details about one or multiple AnnotationAnalyticsAggregation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AnnotationAnalyticsAggregation resources in Oracle Cloud Infrastructure
    - Summarize the annotations created for a given dataset.
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
    label:
        description:
            - It summarizes annotations with the specified label.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. The default order is descending. If no value is specified, updatedBy is used by
              default.
        type: str
        choices:
            - "count"
            - "label"
            - "updatedBy"
    annotation_group_by:
        description:
            - The field to group by. If no value is specified, updatedBy is used by default.
        type: str
        choices:
            - "updatedBy"
            - "label"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List annotation_analytics_aggregations
  oci_data_labeling_service_dataplane_annotation_analytics_aggregation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    label: label_example
    sort_order: ASC
    sort_by: count
    annotation_group_by: updatedBy

"""

RETURN = """
annotation_analytics_aggregations:
    description:
        - List of AnnotationAnalyticsAggregation resources
    returned: on success
    type: complex
    contains:
        count:
            description:
                - The count of the matching results.
            returned: on success
            type: float
            sample: 10
        dataset_id:
            description:
                - The OCID of the dataset the annotations belong to.
            returned: on success
            type: str
            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
        dimensions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                label:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - The label provided by the annotator.
                            returned: on success
                            type: str
                            sample: label_example
                updated_by:
                    description:
                        - The OCID of the principal which updated the resource.
                    returned: on success
                    type: str
                    sample: updated_by_example
        updated_by:
            description:
                - The OCID of the principal which updated the annotation.
            returned: on success
            type: str
            sample: updated_by_example
        compartment_id:
            description:
                - The OCID of the compartment containing the annotations.
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
        "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
        "dimensions": {
            "label": {
                "label": "label_example"
            },
            "updated_by": "updated_by_example"
        },
        "updated_by": "updated_by_example",
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


class AnnotationAnalyticsAggregationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "dataset_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "label",
            "sort_order",
            "sort_by",
            "annotation_group_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_annotation_analytics,
            compartment_id=self.module.params.get("compartment_id"),
            dataset_id=self.module.params.get("dataset_id"),
            **optional_kwargs
        )


AnnotationAnalyticsAggregationFactsHelperCustom = get_custom_class(
    "AnnotationAnalyticsAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    AnnotationAnalyticsAggregationFactsHelperCustom,
    AnnotationAnalyticsAggregationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            dataset_id=dict(type="str", required=True),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE", "DELETED"]),
            label=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["count", "label", "updatedBy"]),
            annotation_group_by=dict(type="str", choices=["updatedBy", "label"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="annotation_analytics_aggregation",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(annotation_analytics_aggregations=result)


if __name__ == "__main__":
    main()
