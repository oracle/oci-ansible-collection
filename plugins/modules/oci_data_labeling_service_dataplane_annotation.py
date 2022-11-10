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
module: oci_data_labeling_service_dataplane_annotation
short_description: Manage an Annotation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Annotation resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an annotation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    record_id:
        description:
            - The OCID of the record annotated.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment for the annotation.
            - Required for create using I(state=present).
        type: str
    entities:
        description:
            - The entity types are validated against the dataset to ensure consistency.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            bounding_polygon:
                description:
                    - ""
                    - Required when entity_type is 'IMAGEOBJECTSELECTION'
                type: dict
                suboptions:
                    normalized_vertices:
                        description:
                            - The normalized vertices that make up the polygon.  They are in the order of the segments they connect.
                            - Required when entity_type is 'IMAGEOBJECTSELECTION'
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            x:
                                description:
                                    - The X axis coordinate.
                                    - Required when entity_type is 'IMAGEOBJECTSELECTION'
                                type: float
                                required: true
                            y:
                                description:
                                    - The Y axis coordinate.
                                    - Required when entity_type is 'IMAGEOBJECTSELECTION'
                                type: float
                                required: true
            entity_type:
                description:
                    - "The entity type described in the annotation.
                      GENERIC  - An extensible entity type that is the base entity type for some annotation formats.
                      IMAGEOBJECTSELECTION- - This allows the labeler to use specify a bounding polygon on the image to represent an object and apply labels to
                      it.
                      TEXTSELECTION - This allows the labeler to highlight text, by specifying an offset and a length, and apply labels to it."
                type: str
                choices:
                    - "IMAGEOBJECTSELECTION"
                    - "GENERIC"
                    - "TEXTSELECTION"
                required: true
            labels:
                description:
                    - A collection of label entities.
                type: list
                elements: dict
                required: true
                suboptions:
                    label:
                        description:
                            - The label provided by the annotator.
                            - Required when entity_type is 'IMAGEOBJECTSELECTION'
                        type: str
                        required: true
            text_span:
                description:
                    - ""
                    - Required when entity_type is 'TEXTSELECTION'
                type: dict
                suboptions:
                    offset:
                        description:
                            - The offset of the selected text within the entire text.
                            - Applicable when entity_type is 'TEXTSELECTION'
                        type: float
                    length:
                        description:
                            - The length of the selected text.
                            - Applicable when entity_type is 'TEXTSELECTION'
                        type: float
            extended_metadata:
                description:
                    - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                      For example: `{\\"bar-key\\": \\"value\\"}`"
                type: dict
    freeform_tags:
        description:
            - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
              For example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "The defined tags for this resource. Each key is predefined and scoped to a namespace.
              For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    annotation_id:
        description:
            - A unique annotation identifier.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    dataset_id:
        description:
            - Filter the results by the OCID of the dataset.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the Annotation.
            - Use I(state=present) to create or update an Annotation.
            - Use I(state=absent) to delete an Annotation.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create annotation
  oci_data_labeling_service_dataplane_annotation:
    # required
    record_id: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    entities:
    - # required
      bounding_polygon:
        # required
        normalized_vertices:
        - # required
          x: 3.4
          y: 3.4
      entity_type: IMAGEOBJECTSELECTION
      labels:
      - # required
        label: label_example

      # optional
      extended_metadata: null

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update annotation
  oci_data_labeling_service_dataplane_annotation:
    # required
    annotation_id: "ocid1.annotation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    entities:
    - # required
      bounding_polygon:
        # required
        normalized_vertices:
        - # required
          x: 3.4
          y: 3.4
      entity_type: IMAGEOBJECTSELECTION
      labels:
      - # required
        label: label_example

      # optional
      extended_metadata: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete annotation
  oci_data_labeling_service_dataplane_annotation:
    # required
    annotation_id: "ocid1.annotation.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
annotation:
    description:
        - Details of the Annotation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        created_by:
            description:
                - The OCID of the principal which created the annotation.
            returned: on success
            type: str
            sample: created_by_example
        updated_by:
            description:
                - The OCID of the principal which updated the annotation.
            returned: on success
            type: str
            sample: updated_by_example
        record_id:
            description:
                - The OCID of the record annotated.
            returned: on success
            type: str
            sample: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"
        entities:
            description:
                - The entity types are validated against the dataset to ensure consistency.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "updated_by": "updated_by_example",
        "record_id": "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx",
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_labeling_service_dataplane import DataLabelingClient
    from oci.data_labeling_service_dataplane.models import CreateAnnotationDetails
    from oci.data_labeling_service_dataplane.models import UpdateAnnotationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnotationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AnnotationHelperGen, self).get_possible_entity_types() + [
            "datalabelingannotation",
            "datalabelingannotations",
            "dataLabelingServiceDataplanedatalabelingannotation",
            "dataLabelingServiceDataplanedatalabelingannotations",
            "datalabelingannotationresource",
            "datalabelingannotationsresource",
            "annotation",
            "annotations",
            "dataLabelingServiceDataplaneannotation",
            "dataLabelingServiceDataplaneannotations",
            "annotationresource",
            "annotationsresource",
            "datalabelingservicedataplane",
        ]

    def get_module_resource_id_param(self):
        return "annotation_id"

    def get_module_resource_id(self):
        return self.module.params.get("annotation_id")

    def get_get_fn(self):
        return self.client.get_annotation

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_annotation, annotation_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_annotation,
            annotation_id=self.module.params.get("annotation_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "dataset_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["record_id"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_annotations, **kwargs
        )

    def get_create_model_class(self):
        return CreateAnnotationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_annotation,
            call_fn_args=(),
            call_fn_kwargs=dict(create_annotation_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAnnotationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_annotation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                annotation_id=self.module.params.get("annotation_id"),
                update_annotation_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_annotation,
            call_fn_args=(),
            call_fn_kwargs=dict(annotation_id=self.module.params.get("annotation_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AnnotationHelperCustom = get_custom_class("AnnotationHelperCustom")


class ResourceHelper(AnnotationHelperCustom, AnnotationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            record_id=dict(type="str"),
            compartment_id=dict(type="str"),
            entities=dict(
                type="list",
                elements="dict",
                options=dict(
                    bounding_polygon=dict(
                        type="dict",
                        options=dict(
                            normalized_vertices=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    x=dict(type="float", required=True),
                                    y=dict(type="float", required=True),
                                ),
                            )
                        ),
                    ),
                    entity_type=dict(
                        type="str",
                        required=True,
                        choices=["IMAGEOBJECTSELECTION", "GENERIC", "TEXTSELECTION"],
                    ),
                    labels=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(label=dict(type="str", required=True)),
                    ),
                    text_span=dict(
                        type="dict",
                        options=dict(
                            offset=dict(type="float"), length=dict(type="float")
                        ),
                    ),
                    extended_metadata=dict(type="dict"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            annotation_id=dict(aliases=["id"], type="str"),
            dataset_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="annotation",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
