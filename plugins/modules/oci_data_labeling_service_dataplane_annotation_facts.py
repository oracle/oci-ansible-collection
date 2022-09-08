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
module: oci_data_labeling_service_dataplane_annotation_facts
short_description: Fetches details about one or multiple Annotation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Annotation resources in Oracle Cloud Infrastructure
    - Returns a list of annotations.
    - If I(annotation_id) is specified, the details of a single Annotation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    annotation_id:
        description:
            - A unique annotation identifier.
            - Required to get a specific annotation.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple annotations.
        type: str
    dataset_id:
        description:
            - Filter the results by the OCID of the dataset.
            - Required to list multiple annotations.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
            - "DELETED"
    updated_by:
        description:
            - The OCID of the principal which updated the annotation.
        type: str
    record_id:
        description:
            - The OCID of the record annotated.
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - The date and time the resource was created, in the timestamp format defined by RFC3339.
        type: str
    time_created_less_than_or_equal_to:
        description:
            - The date and time the resource was created, in the timestamp format defined by RFC3339.
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
            - The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. If no value is specified timeCreated
              is used by default.
        type: str
        choices:
            - "timeCreated"
            - "label"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific annotation
  oci_data_labeling_service_dataplane_annotation_facts:
    # required
    annotation_id: "ocid1.annotation.oc1..xxxxxxEXAMPLExxxxxx"

- name: List annotations
  oci_data_labeling_service_dataplane_annotation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    updated_by: updated_by_example
    record_id: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
annotations:
    description:
        - List of Annotation resources
    returned: on success
    type: complex
    contains:
        created_by:
            description:
                - The OCID of the principal which created the annotation.
                - Returned for get operation
            returned: on success
            type: str
            sample: created_by_example
        updated_by:
            description:
                - The OCID of the principal which updated the annotation.
                - Returned for get operation
            returned: on success
            type: str
            sample: updated_by_example
        entities:
            description:
                - The entity types are validated against the dataset to ensure consistency.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                bounding_polygon:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        normalized_vertices:
                            description:
                                - The normalized vertices that make up the polygon.  They are in the order of the segments they connect.
                            returned: on success
                            type: complex
                            contains:
                                x:
                                    description:
                                        - The X axis coordinate.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                y:
                                    description:
                                        - The Y axis coordinate.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                entity_type:
                    description:
                        - "The entity type described in the annotation.
                          GENERIC  - An extensible entity type that is the base entity type for some annotation formats.
                          IMAGEOBJECTSELECTION- - This allows the labeler to use specify a bounding polygon on the image to represent an object and apply labels
                          to it.
                          TEXTSELECTION - This allows the labeler to highlight text, by specifying an offset and a length, and apply labels to it."
                    returned: on success
                    type: str
                    sample: GENERIC
                labels:
                    description:
                        - A collection of label entities.
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - The label provided by the annotator.
                            returned: on success
                            type: str
                            sample: label_example
                text_span:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        offset:
                            description:
                                - The offset of the selected text within the entire text.
                            returned: on success
                            type: float
                            sample: 10
                        length:
                            description:
                                - The length of the selected text.
                            returned: on success
                            type: float
                            sample: 10
                extended_metadata:
                    description:
                        - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                          For example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {}
        id:
            description:
                - The OCID of the annotation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the annotation was created, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was updated, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        record_id:
            description:
                - The OCID of the record annotated.
            returned: on success
            type: str
            sample: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment for the annotation. This is tied to the dataset. It is not changeable on the record itself.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - "The lifecycle state of an annotation.
                  ACTIVE - The annotation is active to be used for labeling.
                  INACTIVE - The annotation has been marked as inactive and should not be used for labeling.
                  DELETED - Tha annotation been deleted and no longer available for labeling."
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                  For example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "created_by": "created_by_example",
        "updated_by": "updated_by_example",
        "entities": [{
            "bounding_polygon": {
                "normalized_vertices": [{
                    "x": 3.4,
                    "y": 3.4
                }]
            },
            "entity_type": "GENERIC",
            "labels": [{
                "label": "label_example"
            }],
            "text_span": {
                "offset": 10,
                "length": 10
            },
            "extended_metadata": {}
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "record_id": "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
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
    from oci.data_labeling_service_dataplane import DataLabelingClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnotationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "annotation_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "dataset_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_annotation,
            annotation_id=self.module.params.get("annotation_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "updated_by",
            "record_id",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than_or_equal_to",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_annotations,
            compartment_id=self.module.params.get("compartment_id"),
            dataset_id=self.module.params.get("dataset_id"),
            **optional_kwargs
        )


AnnotationFactsHelperCustom = get_custom_class("AnnotationFactsHelperCustom")


class ResourceFactsHelper(AnnotationFactsHelperCustom, AnnotationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            annotation_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            dataset_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE", "DELETED"]),
            updated_by=dict(type="str"),
            record_id=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than_or_equal_to=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "label"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="annotation",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(annotations=result)


if __name__ == "__main__":
    main()
