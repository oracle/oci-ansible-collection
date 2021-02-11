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
module: oci_optimizer_profile
short_description: Manage a Profile resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Profile resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new profile.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy. The tenancy is the root compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name assigned to the profile.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - Text describing the profile.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
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
                suboptions:
                    recommendation_id:
                        description:
                            - The unique OCID of the recommendation.
                        type: str
                    level:
                        description:
                            - The pre-defined profile level.
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
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    description: description_example

- name: Update profile using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_optimizer_profile:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    description: description_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update profile
  oci_optimizer_profile:
    description: description_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    profile_id: ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete profile
  oci_optimizer_profile:
    profile_id: ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete profile using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_optimizer_profile:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the tenancy. The tenancy is the root compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name assigned to the profile.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - Text describing the profile.
            returned: on success
            type: string
            sample: description_example
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
                recommendation_id:
                    description:
                        - The unique OCID of the recommendation.
                    returned: on success
                    type: string
                    sample: ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx
                level:
                    description:
                        - The pre-defined profile level.
                    returned: on success
                    type: string
                    sample: level_example
        lifecycle_state:
            description:
                - The profile's current state.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - The date and time the profile was created, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
        time_updated:
            description:
                - The date and time the profile was last updated, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "levels_configuration": {
            "recommendation_id": "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx",
            "level": "level_example"
        },
        "lifecycle_state": "ACTIVE",
        "time_created": "2020-08-25T21:10:29.600Z",
        "time_updated": "2020-08-25T21:10:29.600Z"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
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

    def get_module_resource_id_param(self):
        return "profile_id"

    def get_module_resource_id(self):
        return self.module.params.get("profile_id")

    def get_get_fn(self):
        return self.client.get_profile

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
            name=dict(type="str"),
            description=dict(type="str"),
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
            profile_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
