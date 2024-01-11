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
module: oci_optimizer_profile_level_facts
short_description: Fetches details about one or multiple ProfileLevel resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProfileLevel resources in Oracle Cloud Infrastructure
    - Lists the existing profile levels.
version_added: "2.9.0"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List profile_levels
  oci_optimizer_profile_level_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true

    # optional
    name: name_example
    recommendation_name: recommendation_name_example
    sort_order: ASC
    sort_by: NAME

"""

RETURN = """
profile_levels:
    description:
        - List of ProfileLevel resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A unique name for the profile level.
            returned: on success
            type: str
            sample: name_example
        recommendation_name:
            description:
                - The name of the recommendation this profile level applies to.
            returned: on success
            type: str
            sample: recommendation_name_example
        metrics:
            description:
                - The metrics that will be evaluated by profiles using this profile level.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the metric (e.g., `CpuUtilization`).
                    returned: on success
                    type: str
                    sample: name_example
                statistic:
                    description:
                        - The name of the statistic (e.g., `p95`).
                    returned: on success
                    type: str
                    sample: statistic_example
                threshold:
                    description:
                        - The threshold that must be crossed for the recommendation to appear.
                    returned: on success
                    type: float
                    sample: 1.2
                target:
                    description:
                        - Optional. The metric value that the recommendation will target.
                    returned: on success
                    type: float
                    sample: 1.2
        default_interval:
            description:
                - The default aggregation interval (in days) for profiles using this profile level.
            returned: on success
            type: int
            sample: 56
        valid_intervals:
            description:
                - An array of aggregation intervals (in days) allowed for profiles using this profile level.
            returned: on success
            type: list
            sample: []
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
    sample: [{
        "name": "name_example",
        "recommendation_name": "recommendation_name_example",
        "metrics": [{
            "name": "name_example",
            "statistic": "statistic_example",
            "threshold": 1.2,
            "target": 1.2
        }],
        "default_interval": 56,
        "valid_intervals": [],
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


class ProfileLevelFactsHelperGen(OCIResourceFactsHelperBase):
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
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_profile_levels,
            compartment_id=self.module.params.get("compartment_id"),
            compartment_id_in_subtree=self.module.params.get(
                "compartment_id_in_subtree"
            ),
            **optional_kwargs
        )


ProfileLevelFactsHelperCustom = get_custom_class("ProfileLevelFactsHelperCustom")


class ResourceFactsHelper(ProfileLevelFactsHelperCustom, ProfileLevelFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool", required=True),
            name=dict(type="str"),
            recommendation_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="profile_level",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(profile_levels=result)


if __name__ == "__main__":
    main()
