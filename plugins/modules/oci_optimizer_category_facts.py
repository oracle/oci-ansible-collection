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
module: oci_optimizer_category_facts
short_description: Fetches details about one or multiple Category resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Category resources in Oracle Cloud Infrastructure
    - Lists the supported Cloud Advisor categories.
    - If I(category_id) is specified, the details of a single Category will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    category_id:
        description:
            - The unique OCID associated with the category.
            - Required to get a specific category.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple categories.
        type: str
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the
              the setting of `accessLevel`.
            - Can only be set to true when performing ListCompartments on the tenancy (root compartment).
            - Required to list multiple categories.
        type: bool
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific category
  oci_optimizer_category_facts:
    # required
    category_id: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"

- name: List categories
  oci_optimizer_category_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true

    # optional
    child_tenancy_ids: [ "child_tenancy_ids_example" ]
    include_organization: true
    name: name_example
    sort_order: ASC
    sort_by: NAME
    lifecycle_state: ACTIVE

"""

RETURN = """
categories:
    description:
        - List of Category resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID of the category.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy. The tenancy is the root compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_name:
            description:
                - The name associated with the compartment.
            returned: on success
            type: str
            sample: compartment_name_example
        name:
            description:
                - The name assigned to the category.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Text describing the category.
            returned: on success
            type: str
            sample: description_example
        recommendation_counts:
            description:
                - An array of `RecommendationCount` objects grouped by the level of importance assigned to the recommendation.
            returned: on success
            type: complex
            contains:
                importance:
                    description:
                        - The level of importance assigned to the recommendation.
                    returned: on success
                    type: str
                    sample: CRITICAL
                count:
                    description:
                        - The count of recommendations.
                    returned: on success
                    type: int
                    sample: 56
        resource_counts:
            description:
                - An array of `ResourceCount` objects grouped by the status of the recommendation.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - The recommendation status of the resource.
                    returned: on success
                    type: str
                    sample: PENDING
                count:
                    description:
                        - The count of resources.
                    returned: on success
                    type: int
                    sample: 56
        lifecycle_state:
            description:
                - The category's current state.
            returned: on success
            type: str
            sample: ACTIVE
        estimated_cost_saving:
            description:
                - The estimated cost savings, in dollars, for the category.
            returned: on success
            type: float
            sample: 1.2
        time_created:
            description:
                - The date and time the category details were created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the category details were last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        extended_metadata:
            description:
                - Additional metadata key/value pairs for the category.
                - "For example:"
                - "`{\\"EstimatedSaving\\": \\"200\\"}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_name": "compartment_name_example",
        "name": "name_example",
        "description": "description_example",
        "recommendation_counts": [{
            "importance": "CRITICAL",
            "count": 56
        }],
        "resource_counts": [{
            "status": "PENDING",
            "count": 56
        }],
        "lifecycle_state": "ACTIVE",
        "estimated_cost_saving": 1.2,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "extended_metadata": {}
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


class CategoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "category_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "compartment_id_in_subtree",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_category, category_id=self.module.params.get("category_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "child_tenancy_ids",
            "include_organization",
            "name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_categories,
            compartment_id=self.module.params.get("compartment_id"),
            compartment_id_in_subtree=self.module.params.get(
                "compartment_id_in_subtree"
            ),
            **optional_kwargs
        )


CategoryFactsHelperCustom = get_custom_class("CategoryFactsHelperCustom")


class ResourceFactsHelper(CategoryFactsHelperCustom, CategoryFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            category_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            child_tenancy_ids=dict(type="list", elements="str"),
            include_organization=dict(type="bool"),
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
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="category",
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

    module.exit_json(categories=result)


if __name__ == "__main__":
    main()
