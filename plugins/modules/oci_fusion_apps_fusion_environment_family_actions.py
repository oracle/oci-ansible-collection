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
module: oci_fusion_apps_fusion_environment_family_actions
short_description: Perform actions on a FusionEnvironmentFamily resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a FusionEnvironmentFamily resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a FusionEnvironmentFamily into a different compartment. When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fusion_environment_family_id:
        description:
            - The unique identifier (OCID) of the FusionEnvironmentFamily.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the FusionEnvironmentFamily.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on fusion_environment_family
  oci_fusion_apps_fusion_environment_family_actions:
    # required
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.fusion_apps import FusionApplicationsClient
    from oci.fusion_apps.models import ChangeFusionEnvironmentFamilyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FusionEnvironmentFamilyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "fusion_environment_family_id"

    def get_module_resource_id(self):
        return self.module.params.get("fusion_environment_family_id")

    def get_get_fn(self):
        return self.client.get_fusion_environment_family

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_family,
            fusion_environment_family_id=self.module.params.get(
                "fusion_environment_family_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeFusionEnvironmentFamilyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_fusion_environment_family_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fusion_environment_family_id=self.module.params.get(
                    "fusion_environment_family_id"
                ),
                change_fusion_environment_family_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


FusionEnvironmentFamilyActionsHelperCustom = get_custom_class(
    "FusionEnvironmentFamilyActionsHelperCustom"
)


class ResourceHelper(
    FusionEnvironmentFamilyActionsHelperCustom, FusionEnvironmentFamilyActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            fusion_environment_family_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
