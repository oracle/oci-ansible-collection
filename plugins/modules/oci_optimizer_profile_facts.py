#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_optimizer_profile_facts
short_description: Fetches details about one or multiple Profile resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Profile resources in Oracle Cloud Infrastructure
    - Lists the existing profiles.
    - If I(profile_id) is specified, the details of a single Profile will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    profile_id:
        description:
            - The unique OCID of the profile.
            - Required to get a specific profile.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple profiles.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific profile
  oci_optimizer_profile_facts:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"

- name: List profiles
  oci_optimizer_profile_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: NAME
    lifecycle_state: ACTIVE

"""

RETURN = """
profiles:
    description:
        - List of Profile resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID of the profile.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy. The tenancy is the root compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name assigned to the profile. Avoid entering confidential information.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Text describing the profile. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        aggregation_interval_in_days:
            description:
                - The time period over which to collect data for the recommendations, measured in number of days.
            returned: on success
            type: int
            sample: 56
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Simple key-value pair applied without any predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Exists for cross-
                  compatibility only.
                - "Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        lifecycle_state:
            description:
                - The profile's current state.
            returned: on success
            type: str
            sample: ACTIVE
        levels_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The array of configuration levels.
                    returned: on success
                    type: complex
                    contains:
                        recommendation_id:
                            description:
                                - The unique OCID of the recommendation.
                            returned: on success
                            type: str
                            sample: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
                        level:
                            description:
                                - The pre-defined profile level.
                            returned: on success
                            type: str
                            sample: level_example
        target_compartments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The list of OCIDs attached to the compartments specified in the current profile override.
                    returned: on success
                    type: list
                    sample: []
        target_tags:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The list of tags specified in the current profile override.
                    returned: on success
                    type: complex
                    contains:
                        tag_namespace_name:
                            description:
                                - The name of the tag namespace.
                            returned: on success
                            type: str
                            sample: tag_namespace_name_example
                        tag_definition_name:
                            description:
                                - The name you use to refer to the tag, also known as the tag key.
                            returned: on success
                            type: str
                            sample: tag_definition_name_example
                        tag_value_type:
                            description:
                                - Specifies which tag value types in the `tagValues` field result in overrides of the recommendation criteria.
                                - When the value for this field is `ANY`, the `tagValues` field should be empty, which enforces overrides to the recommendation
                                  for resources with any tag values attached to them.
                                - When the value for this field value is `VALUE`, the `tagValues` field must include a specific value or list of values.
                                  Overrides to the recommendation criteria only occur for resources that match the values in the `tagValues` fields.
                            returned: on success
                            type: str
                            sample: VALUE
                        tag_values:
                            description:
                                - The list of tag values. The tag value is the value that the user applying the tag adds to the tag key.
                            returned: on success
                            type: list
                            sample: []
        time_created:
            description:
                - The date and time the profile was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the profile was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "aggregation_interval_in_days": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "lifecycle_state": "ACTIVE",
        "levels_configuration": {
            "items": [{
                "recommendation_id": "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx",
                "level": "level_example"
            }]
        },
        "target_compartments": {
            "items": []
        },
        "target_tags": {
            "items": [{
                "tag_namespace_name": "tag_namespace_name_example",
                "tag_definition_name": "tag_definition_name_example",
                "tag_value_type": "VALUE",
                "tag_values": []
            }]
        },
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


class ProfileFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "profile_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=self.module.params.get("profile_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_profiles,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProfileFactsHelperCustom = get_custom_class("ProfileFactsHelperCustom")


class ResourceFactsHelper(ProfileFactsHelperCustom, ProfileFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            profile_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="profile",
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

    module.exit_json(profiles=result)


if __name__ == "__main__":
    main()
