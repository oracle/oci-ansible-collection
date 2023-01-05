#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_optimizer_resource_action_facts
short_description: Fetches details about one or multiple ResourceAction resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResourceAction resources in Oracle Cloud Infrastructure
    - Lists the Cloud Advisor resource actions that are supported.
    - If I(resource_action_id) is specified, the details of a single ResourceAction will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resource_action_id:
        description:
            - The unique OCID associated with the resource action.
            - Required to get a specific resource_action.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple resource_actions.
        type: str
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the
              the setting of `accessLevel`.
            - Can only be set to true when performing ListCompartments on the tenancy (root compartment).
            - Required to list multiple resource_actions.
        type: bool
    recommendation_id:
        description:
            - The unique OCID associated with the recommendation.
        type: str
    recommendation_name:
        description:
            - Optional. A filter that returns results that match the recommendation name specified.
        type: str
    child_tenancy_ids:
        description:
            - A list of child tenancies for which the respective data will be returned. Please note that
              the parent tenancy id can also be included in this list. For example, if there is a parent P with two
              children A and B, to return results of only parent P and child A, this list should be populated with
              tenancy id of parent P and child A.
            - If this list contains a tenancy id that isn't part of the organization of parent P, the request will
              fail. That is, let's say there is an organization with parent P with children A and B, and also one
              other tenant T that isn't part of the organization. If T is included in the list of
              childTenancyIds, the request will fail.
            - It is important to note that if you are setting the includeOrganization parameter value as true and
              also populating the childTenancyIds parameter with a list of child tenancies, the request will fail.
              The childTenancyIds and includeOrganization should be used exclusively.
            - When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.
        type: list
        elements: str
    include_organization:
        description:
            - When set to true, the data for all child tenancies including the parent is returned. That is, if
              there is an organization with parent P and children A and B, to return the data for the parent P, child
              A and child B, this parameter value should be set to true.
            - Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like
              to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate
              the list with tenancy id of P and A.
            - When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.
        type: bool
    name:
        description:
            - Optional. A filter that returns results that match the name specified.
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
- name: Get a specific resource_action
  oci_optimizer_resource_action_facts:
    # required
    resource_action_id: "ocid1.resourceaction.oc1..xxxxxxEXAMPLExxxxxx"

- name: List resource_actions
  oci_optimizer_resource_action_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true

    # optional
    recommendation_id: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
    recommendation_name: recommendation_name_example
    child_tenancy_ids: [ "child_tenancy_ids_example" ]
    include_organization: true
    name: name_example
    resource_type: resource_type_example
    sort_order: ASC
    sort_by: NAME
    lifecycle_state: ACTIVE
    status: PENDING

"""

RETURN = """
resource_actions:
    description:
        - List of ResourceAction resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID associated with the resource action.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        category_id:
            description:
                - The unique OCID associated with the category.
            returned: on success
            type: str
            sample: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"
        recommendation_id:
            description:
                - The unique OCID associated with the recommendation.
            returned: on success
            type: str
            sample: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The unique OCID associated with the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name assigned to the resource.
            returned: on success
            type: str
            sample: name_example
        resource_type:
            description:
                - The kind of resource.
            returned: on success
            type: str
            sample: resource_type_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_name:
            description:
                - The name associated with the compartment.
            returned: on success
            type: str
            sample: compartment_name_example
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
                    type: str
                    sample: KB_ARTICLE
                description:
                    description:
                        - Text describing the recommended action.
                    returned: on success
                    type: str
                    sample: description_example
                url:
                    description:
                        - The URL path to documentation that explains how to perform the action.
                    returned: on success
                    type: str
                    sample: url_example
        lifecycle_state:
            description:
                - The resource action's current state.
            returned: on success
            type: str
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
            type: str
            sample: PENDING
        time_status_begin:
            description:
                - The date and time that the resource action entered its current status. The format is defined by RFC3339.
                - "For example, \\"The status of the resource action changed from `pending` to `current(ignored)` on this date and time.\\""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_status_end:
            description:
                - The date and time the current status will change. The format is defined by RFC3339.
                - "For example, \\"The current `postponed` status of the resource action will end and change to `pending` on this
                  date and time.\\""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                - The date and time the resource action details were created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource action details were last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "recommendation_id": "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "resource_type": "resource_type_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_name": "compartment_name_example",
        "action": {
            "type": "KB_ARTICLE",
            "description": "description_example",
            "url": "url_example"
        },
        "lifecycle_state": "ACTIVE",
        "estimated_cost_saving": 1.2,
        "status": "PENDING",
        "time_status_begin": "2013-10-20T19:20:30+01:00",
        "time_status_end": "2013-10-20T19:20:30+01:00",
        "metadata": {},
        "extended_metadata": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.optimizer import OptimizerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceActionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "resource_action_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "compartment_id_in_subtree",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_resource_action,
            resource_action_id=self.module.params.get("resource_action_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "recommendation_id",
            "recommendation_name",
            "child_tenancy_ids",
            "include_organization",
            "name",
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
            self.client.list_resource_actions,
            compartment_id=self.module.params.get("compartment_id"),
            compartment_id_in_subtree=self.module.params.get(
                "compartment_id_in_subtree"
            ),
            **optional_kwargs
        )


ResourceActionFactsHelperCustom = get_custom_class("ResourceActionFactsHelperCustom")


class ResourceFactsHelper(
    ResourceActionFactsHelperCustom, ResourceActionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            resource_action_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            recommendation_id=dict(type="str"),
            recommendation_name=dict(type="str"),
            child_tenancy_ids=dict(type="list", elements="str"),
            include_organization=dict(type="bool"),
            name=dict(type="str"),
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

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_action",
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

    module.exit_json(resource_actions=result)


if __name__ == "__main__":
    main()
