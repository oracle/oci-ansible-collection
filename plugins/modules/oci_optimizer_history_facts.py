#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_optimizer_history_facts
short_description: Fetches details about one or multiple History resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple History resources in Oracle Cloud Infrastructure
    - Lists changes to the recommendations based on user activity.
      For example, lists when recommendations have been implemented, dismissed, postponed, or reactivated.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the
              the setting of `accessLevel`.
            - Can only be set to true when performing ListCompartments on the tenancy (root compartment).
        type: bool
        required: true
    name:
        description:
            - Optional. A filter that returns results that match the name specified.
        type: str
    recommendation_name:
        description:
            - Optional. A filter that returns results that match the recommendation name specified.
        type: str
    recommendation_id:
        description:
            - The unique OCID associated with the recommendation.
        type: str
    resource_type:
        description:
            - Optional. A filter that returns results that match the resource type specified.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is
              ascending. The NAME sort order is case sensitive.
        type: str
        choices:
            - "NAME"
            - "TIMECREATED"
    lifecycle_state:
        description:
            - A filter that returns results that match the lifecycle state specified.
        type: str
        choices:
            - "ACTIVE"
            - "FAILED"
            - "INACTIVE"
            - "ATTACHING"
            - "DETACHING"
            - "DELETING"
            - "DELETED"
            - "UPDATING"
            - "CREATING"
    status:
        description:
            - A filter that returns recommendations that match the status specified.
        type: str
        choices:
            - "PENDING"
            - "DISMISSED"
            - "POSTPONED"
            - "IMPLEMENTED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List histories
  oci_optimizer_history_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id_in_subtree: true

"""

RETURN = """
histories:
    description:
        - List of History resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID associated with the recommendation history.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name assigned to the resource.
            returned: on success
            type: string
            sample: name_example
        resource_type:
            description:
                - The kind of resource.
            returned: on success
            type: string
            sample: resource_type_example
        category_id:
            description:
                - The unique OCID associated with the category.
            returned: on success
            type: string
            sample: ocid1.category.oc1..xxxxxxEXAMPLExxxxxx
        recommendation_id:
            description:
                - The unique OCID associated with the recommendation.
            returned: on success
            type: string
            sample: ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx
        recommendation_name:
            description:
                - The name assigned to the recommendation.
            returned: on success
            type: string
            sample: recommendation_name_example
        resource_id:
            description:
                - The unique OCID associated with the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        resource_action_id:
            description:
                - The unique OCID associated with the resource action.
            returned: on success
            type: string
            sample: ocid1.resourceaction.oc1..xxxxxxEXAMPLExxxxxx
        action:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The status of the resource action.
                    returned: on success
                    type: string
                    sample: KB_ARTICLE
                description:
                    description:
                        - Text describing the recommended action.
                    returned: on success
                    type: string
                    sample: description_example
                url:
                    description:
                        - The URL path to documentation that explains how to perform the action.
                    returned: on success
                    type: string
                    sample: url_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        compartment_name:
            description:
                - The name assigned to the compartment.
            returned: on success
            type: string
            sample: compartment_name_example
        lifecycle_state:
            description:
                - The recommendation history's current state.
            returned: on success
            type: string
            sample: ACTIVE
        estimated_cost_saving:
            description:
                - The estimated cost savings, in dollars, for the resource action.
            returned: on success
            type: float
            sample: 1.2
        status:
            description:
                - The current status of the resource action.
            returned: on success
            type: string
            sample: PENDING
        metadata:
            description:
                - Custom metadata key/value pairs for the resource action.
                - "**Metadata Example**"
                - "     \\"metadata\\" : {
                           \\"cpuRecommendedShape\\": \\"VM.Standard1.1\\",
                           \\"computeMemoryUtilization\\": \\"26.05734124418388\\",
                           \\"currentShape\\": \\"VM.Standard1.2\\",
                           \\"instanceRecommendedShape\\": \\"VM.Standard1.1\\",
                           \\"computeCpuUtilization\\": \\"7.930035319720132\\",
                           \\"memoryRecommendedShape\\": \\"None\\"
                        }"
            returned: on success
            type: dict
            sample: {}
        extended_metadata:
            description:
                - Additional metadata key/value pairs that you provide.
                  They serve the same purpose and functionality as fields in the `metadata` object.
                - They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps
                  only).
                - "For example:"
                - "`{\\"CurrentShape\\": {\\"name\\":\\"VM.Standard2.16\\"}, \\"RecommendedShape\\": {\\"name\\":\\"VM.Standard2.8\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The date and time the recommendation history was created, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "resource_type": "resource_type_example",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "recommendation_id": "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx",
        "recommendation_name": "recommendation_name_example",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_action_id": "ocid1.resourceaction.oc1..xxxxxxEXAMPLExxxxxx",
        "action": {
            "type": "KB_ARTICLE",
            "description": "description_example",
            "url": "url_example"
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_name": "compartment_name_example",
        "lifecycle_state": "ACTIVE",
        "estimated_cost_saving": 1.2,
        "status": "PENDING",
        "metadata": {},
        "extended_metadata": {},
        "time_created": "2020-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.optimizer import OptimizerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HistoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "compartment_id_in_subtree",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "recommendation_name",
            "recommendation_id",
            "resource_type",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "status",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_histories,
            compartment_id=self.module.params.get("compartment_id"),
            compartment_id_in_subtree=self.module.params.get(
                "compartment_id_in_subtree"
            ),
            **optional_kwargs
        )


HistoryFactsHelperCustom = get_custom_class("HistoryFactsHelperCustom")


class ResourceFactsHelper(HistoryFactsHelperCustom, HistoryFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool", required=True),
            name=dict(type="str"),
            recommendation_name=dict(type="str"),
            recommendation_id=dict(type="str"),
            resource_type=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "FAILED",
                    "INACTIVE",
                    "ATTACHING",
                    "DETACHING",
                    "DELETING",
                    "DELETED",
                    "UPDATING",
                    "CREATING",
                ],
            ),
            status=dict(
                type="str", choices=["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="history",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(histories=result)


if __name__ == "__main__":
    main()
