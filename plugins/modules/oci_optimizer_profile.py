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
module: oci_optimizer_profile
short_description: Manage a Profile resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Profile resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new profile.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy. The tenancy is the root compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - Text describing the profile. Avoid entering confidential information.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    aggregation_interval_in_days:
        description:
            - The time period over which to collect data for the recommendations, measured in number of days.
            - This parameter is updatable.
        type: int
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - Simple key-value pair applied without any predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Exists for cross-compatibility
              only.
            - "Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    levels_configuration:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            items:
                description:
                    - The array of configuration levels.
                type: list
                elements: dict
                suboptions:
                    recommendation_id:
                        description:
                            - The unique OCID of the recommendation.
                        type: str
                    level:
                        description:
                            - The pre-defined profile level.
                        type: str
    target_compartments:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            items:
                description:
                    - The list of OCIDs attached to the compartments specified in the current profile override.
                type: list
                elements: str
                required: true
    target_tags:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            items:
                description:
                    - The list of tags specified in the current profile override.
                type: list
                elements: dict
                required: true
                suboptions:
                    tag_namespace_name:
                        description:
                            - The name of the tag namespace.
                        type: str
                        required: true
                    tag_definition_name:
                        description:
                            - The name you use to refer to the tag, also known as the tag key.
                        type: str
                        required: true
                    tag_value_type:
                        description:
                            - Specifies which tag value types in the `tagValues` field result in overrides of the recommendation criteria.
                            - When the value for this field is `ANY`, the `tagValues` field should be empty, which enforces overrides to the recommendation
                              for resources with any tag values attached to them.
                            - When the value for this field value is `VALUE`, the `tagValues` field must include a specific value or list of values.
                              Overrides to the recommendation criteria only occur for resources that match the values in the `tagValues` fields.
                        type: str
                        choices:
                            - "VALUE"
                            - "ANY"
                        required: true
                    tag_values:
                        description:
                            - The list of tag values. The tag value is the value that the user applying the tag adds to the tag key.
                        type: list
                        elements: str
    name:
        description:
            - The name assigned to the profile. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    profile_id:
        description:
            - The unique OCID of the profile.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Profile.
            - Use I(state=present) to create or update a Profile.
            - Use I(state=absent) to delete a Profile.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create profile
  oci_optimizer_profile:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    description: description_example
    levels_configuration:
      # optional
      items:
      - # optional
        recommendation_id: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
        level: level_example
    name: name_example

    # optional
    aggregation_interval_in_days: 56
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    target_compartments:
      # required
      items: [ "items_example" ]
    target_tags:
      # required
      items:
      - # required
        tag_namespace_name: tag_namespace_name_example
        tag_definition_name: tag_definition_name_example
        tag_value_type: VALUE

        # optional
        tag_values: [ "tag_values_example" ]

- name: Update profile
  oci_optimizer_profile:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    aggregation_interval_in_days: 56
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    levels_configuration:
      # optional
      items:
      - # optional
        recommendation_id: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
        level: level_example
    target_compartments:
      # required
      items: [ "items_example" ]
    target_tags:
      # required
      items:
      - # required
        tag_namespace_name: tag_namespace_name_example
        tag_definition_name: tag_definition_name_example
        tag_value_type: VALUE

        # optional
        tag_values: [ "tag_values_example" ]
    name: name_example

- name: Update profile using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_optimizer_profile:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    description: description_example
    aggregation_interval_in_days: 56
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    levels_configuration:
      # optional
      items:
      - # optional
        recommendation_id: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
        level: level_example
    target_compartments:
      # required
      items: [ "items_example" ]
    target_tags:
      # required
      items:
      - # required
        tag_namespace_name: tag_namespace_name_example
        tag_definition_name: tag_definition_name_example
        tag_value_type: VALUE

        # optional
        tag_values: [ "tag_values_example" ]

- name: Delete profile
  oci_optimizer_profile:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete profile using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_optimizer_profile:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
profile:
    description:
        - Details of the Profile resource acted upon by the current operation
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
        lifecycle_state:
            description:
                - The profile's current state.
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "aggregation_interval_in_days": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
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
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.optimizer import OptimizerClient
    from oci.optimizer.models import CreateProfileDetails
    from oci.optimizer.models import UpdateProfileDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProfileHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ProfileHelperGen, self).get_possible_entity_types() + [
            "profile",
            "profiles",
            "optimizerprofile",
            "optimizerprofiles",
            "profileresource",
            "profilesresource",
            "optimizer",
        ]

    def get_module_resource_id_param(self):
        return "profile_id"

    def get_module_resource_id(self):
        return self.module.params.get("profile_id")

    def get_get_fn(self):
        return self.client.get_profile

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=self.module.params.get("profile_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_profiles, **kwargs)

    def get_create_model_class(self):
        return CreateProfileDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(create_profile_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateProfileDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(
                profile_id=self.module.params.get("profile_id"),
                update_profile_details=update_details,
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
            call_fn=self.client.delete_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(profile_id=self.module.params.get("profile_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ProfileHelperCustom = get_custom_class("ProfileHelperCustom")


class ResourceHelper(ProfileHelperCustom, ProfileHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            aggregation_interval_in_days=dict(type="int"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            levels_configuration=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            recommendation_id=dict(type="str"), level=dict(type="str")
                        ),
                    )
                ),
            ),
            target_compartments=dict(
                type="dict",
                options=dict(items=dict(type="list", elements="str", required=True)),
            ),
            target_tags=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            tag_namespace_name=dict(type="str", required=True),
                            tag_definition_name=dict(type="str", required=True),
                            tag_value_type=dict(
                                type="str", required=True, choices=["VALUE", "ANY"]
                            ),
                            tag_values=dict(type="list", elements="str"),
                        ),
                    )
                ),
            ),
            name=dict(type="str"),
            profile_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="profile",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
