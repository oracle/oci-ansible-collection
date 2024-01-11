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
module: oci_fusion_apps_fusion_environment_family
short_description: Manage a FusionEnvironmentFamily resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a FusionEnvironmentFamily resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new FusionEnvironmentFamily.
    - "This resource has the following action operations in the M(oracle.oci.oci_fusion_apps_fusion_environment_family_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where the environment family is located.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    family_maintenance_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            quarterly_upgrade_begin_times:
                description:
                    - The quarterly maintenance month group schedule of the Fusion environment family.
                type: str
            is_monthly_patching_enabled:
                description:
                    - When True, monthly patching is enabled for the environment family.
                    - This parameter is updatable.
                type: bool
            concurrent_maintenance:
                description:
                    - Option to upgrade both production and non-production environments at the same time. When set to PROD both types of environnments are
                      upgraded on the production schedule. When set to NON_PROD both types of environments are upgraded on the non-production schedule.
                    - This parameter is updatable.
                type: str
                choices:
                    - "PROD"
                    - "NON_PROD"
                    - "DISABLED"
    subscription_ids:
        description:
            - The list of the IDs of the applications subscriptions that are associated with the environment family.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    fusion_environment_family_id:
        description:
            - The unique identifier (OCID) of the FusionEnvironmentFamily.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the FusionEnvironmentFamily.
            - Use I(state=present) to create or update a FusionEnvironmentFamily.
            - Use I(state=absent) to delete a FusionEnvironmentFamily.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create fusion_environment_family
  oci_fusion_apps_fusion_environment_family:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    subscription_ids: [ "subscription_ids_example" ]

    # optional
    family_maintenance_policy:
      # optional
      quarterly_upgrade_begin_times: quarterly_upgrade_begin_times_example
      is_monthly_patching_enabled: true
      concurrent_maintenance: PROD
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update fusion_environment_family
  oci_fusion_apps_fusion_environment_family:
    # required
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    family_maintenance_policy:
      # optional
      quarterly_upgrade_begin_times: quarterly_upgrade_begin_times_example
      is_monthly_patching_enabled: true
      concurrent_maintenance: PROD
    subscription_ids: [ "subscription_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update fusion_environment_family using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_fusion_apps_fusion_environment_family:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    family_maintenance_policy:
      # optional
      quarterly_upgrade_begin_times: quarterly_upgrade_begin_times_example
      is_monthly_patching_enabled: true
      concurrent_maintenance: PROD
    subscription_ids: [ "subscription_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete fusion_environment_family
  oci_fusion_apps_fusion_environment_family:
    # required
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete fusion_environment_family using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_fusion_apps_fusion_environment_family:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
fusion_environment_family:
    description:
        - Details of the FusionEnvironmentFamily resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier (OCID) of the environment family. Can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.
            returned: on success
            type: str
            sample: display_name_example
        family_maintenance_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                quarterly_upgrade_begin_times:
                    description:
                        - The quarterly maintenance month group schedule of the Fusion environment family.
                    returned: on success
                    type: str
                    sample: quarterly_upgrade_begin_times_example
                is_monthly_patching_enabled:
                    description:
                        - When True, monthly patching is enabled for the environment family.
                    returned: on success
                    type: bool
                    sample: true
                concurrent_maintenance:
                    description:
                        - Option to upgrade both production and non-production environments at the same time. When set to PROD both types of environnments are
                          upgraded on the production schedule. When set to NON_PROD both types of environments are upgraded on the non-production schedule.
                    returned: on success
                    type: str
                    sample: PROD
        compartment_id:
            description:
                - The OCID of the compartment where the environment family is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_ids:
            description:
                - The list of the IDs of the applications subscriptions that are associated with the environment family.
            returned: on success
            type: list
            sample: []
        is_subscription_update_needed:
            description:
                - When set to True, a subscription update is required for the environment family.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the the FusionEnvironmentFamily was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the FusionEnvironmentFamily.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        system_name:
            description:
                - Environment Specific Guid/ System Name
            returned: on success
            type: str
            sample: system_name_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "family_maintenance_policy": {
            "quarterly_upgrade_begin_times": "quarterly_upgrade_begin_times_example",
            "is_monthly_patching_enabled": true,
            "concurrent_maintenance": "PROD"
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_ids": [],
        "is_subscription_update_needed": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "system_name": "system_name_example",
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
    from oci.fusion_apps import FusionApplicationsClient
    from oci.fusion_apps.models import CreateFusionEnvironmentFamilyDetails
    from oci.fusion_apps.models import UpdateFusionEnvironmentFamilyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FusionEnvironmentFamilyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            FusionEnvironmentFamilyHelperGen, self
        ).get_possible_entity_types() + [
            "fusionenvironmentfamily",
            "fusionenvironmentfamilies",
            "fusionAppsfusionenvironmentfamily",
            "fusionAppsfusionenvironmentfamilies",
            "fusionenvironmentfamilyresource",
            "fusionenvironmentfamiliesresource",
            "fusionapps",
        ]

    def get_module_resource_id_param(self):
        return "fusion_environment_family_id"

    def get_module_resource_id(self):
        return self.module.params.get("fusion_environment_family_id")

    def get_get_fn(self):
        return self.client.get_fusion_environment_family

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_family,
            fusion_environment_family_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_family,
            fusion_environment_family_id=self.module.params.get(
                "fusion_environment_family_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["fusion_environment_family_id", "display_name"]

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
            self.client.list_fusion_environment_families, **kwargs
        )

    def get_create_model_class(self):
        return CreateFusionEnvironmentFamilyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_fusion_environment_family,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_fusion_environment_family_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateFusionEnvironmentFamilyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_fusion_environment_family,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fusion_environment_family_id=self.module.params.get(
                    "fusion_environment_family_id"
                ),
                update_fusion_environment_family_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_fusion_environment_family,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fusion_environment_family_id=self.module.params.get(
                    "fusion_environment_family_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


FusionEnvironmentFamilyHelperCustom = get_custom_class(
    "FusionEnvironmentFamilyHelperCustom"
)


class ResourceHelper(
    FusionEnvironmentFamilyHelperCustom, FusionEnvironmentFamilyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            family_maintenance_policy=dict(
                type="dict",
                options=dict(
                    quarterly_upgrade_begin_times=dict(type="str"),
                    is_monthly_patching_enabled=dict(type="bool"),
                    concurrent_maintenance=dict(
                        type="str", choices=["PROD", "NON_PROD", "DISABLED"]
                    ),
                ),
            ),
            subscription_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            fusion_environment_family_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="fusion_environment_family",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
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
