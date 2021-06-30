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
module: oci_optimizer_recommendation_facts
short_description: Fetches details about one or multiple Recommendation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Recommendation resources in Oracle Cloud Infrastructure
    - Lists the Cloud Advisor recommendations that are currently supported in the specified category.
    - If I(recommendation_id) is specified, the details of a single Recommendation will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    recommendation_id:
        description:
            - The unique OCID associated with the recommendation.
            - Required to get a specific recommendation.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple recommendations.
        type: str
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the
              the setting of `accessLevel`.
            - Can only be set to true when performing ListCompartments on the tenancy (root compartment).
            - Required to list multiple recommendations.
        type: bool
    category_id:
        description:
            - The unique OCID associated with the category.
            - Required to list multiple recommendations.
        type: str
    name:
        description:
            - Optional. A filter that returns results that match the name specified.
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
- name: List recommendations
  oci_optimizer_recommendation_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true
    category_id: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific recommendation
  oci_optimizer_recommendation_facts:
    recommendation_id: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
recommendations:
    description:
        - List of Recommendation resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID associated with the recommendation.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy. The tenancy is the root compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        category_id:
            description:
                - The unique OCID associated with the category.
            returned: on success
            type: string
            sample: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name assigned to the recommendation.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - Text describing the recommendation.
            returned: on success
            type: string
            sample: description_example
        importance:
            description:
                - The level of importance assigned to the recommendation.
            returned: on success
            type: string
            sample: CRITICAL
        resource_counts:
            description:
                - An array of `ResourceCount` objects grouped by the status of the resource actions.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - The recommendation status of the resource.
                    returned: on success
                    type: string
                    sample: PENDING
                count:
                    description:
                        - The count of resources.
                    returned: on success
                    type: int
                    sample: 56
        lifecycle_state:
            description:
                - The recommendation's current state.
            returned: on success
            type: string
            sample: ACTIVE
        estimated_cost_saving:
            description:
                - The estimated cost savings, in dollars, for the recommendation.
            returned: on success
            type: float
            sample: 1.2
        status:
            description:
                - The current status of the recommendation.
            returned: on success
            type: string
            sample: PENDING
        time_status_begin:
            description:
                - The date and time that the recommendation entered its current status. The format is defined by RFC3339.
                - "For example, \\"The status of the recommendation changed from `pending` to `current(ignored)` on this date and time.\\""
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_status_end:
            description:
                - The date and time the current status will change. The format is defined by RFC3339.
                - "For example, \\"The current `postponed` status of the recommendation will end and change to `pending` on this
                  date and time.\\""
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_created:
            description:
                - The date and time the recommendation details were created, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
        time_updated:
            description:
                - The date and time the recommendation details were last updated, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
        supported_levels:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The list of supported levels.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the profile level.
                            returned: on success
                            type: string
                            sample: name_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "importance": "CRITICAL",
        "resource_counts": [{
            "status": "PENDING",
            "count": 56
        }],
        "lifecycle_state": "ACTIVE",
        "estimated_cost_saving": 1.2,
        "status": "PENDING",
        "time_status_begin": "2013-10-20T19:20:30+01:00",
        "time_status_end": "2013-10-20T19:20:30+01:00",
        "time_created": "2020-08-25T21:10:29.600Z",
        "time_updated": "2020-08-25T21:10:29.600Z",
        "supported_levels": {
            "items": [{
                "name": "name_example"
            }]
        }
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


class RecommendationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "recommendation_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "compartment_id_in_subtree",
            "category_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_recommendation,
            recommendation_id=self.module.params.get("recommendation_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
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
            self.client.list_recommendations,
            compartment_id=self.module.params.get("compartment_id"),
            compartment_id_in_subtree=self.module.params.get(
                "compartment_id_in_subtree"
            ),
            category_id=self.module.params.get("category_id"),
            **optional_kwargs
        )


RecommendationFactsHelperCustom = get_custom_class("RecommendationFactsHelperCustom")


class ResourceFactsHelper(
    RecommendationFactsHelperCustom, RecommendationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            recommendation_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            category_id=dict(type="str"),
            name=dict(type="str"),
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
        resource_type="recommendation",
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

    module.exit_json(recommendations=result)


if __name__ == "__main__":
    main()
