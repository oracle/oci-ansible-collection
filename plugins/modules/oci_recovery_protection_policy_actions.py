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
module: oci_recovery_protection_policy_actions
short_description: Perform actions on a ProtectionPolicy resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ProtectionPolicy resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a protection policy resource from the existing compartment to the specified compartment. When provided, If-Match
      is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    protection_policy_id:
        description:
            - The protection policy OCID.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the Protection Policy should be
              moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ProtectionPolicy.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on protection_policy
  oci_recovery_protection_policy_actions:
    # required
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
protection_policy:
    description:
        - Details of the ProtectionPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The protection policy OCID.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user provided name for the protection policy.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the protection policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        backup_retention_period_in_days:
            description:
                - The maximum number of days to retain backups for a protected database. Specify a period ranging from a minimum 14 days to a maximum 95 days.
                  For example, specify the value 55 if you want to retain backups for 55 days.
            returned: on success
            type: int
            sample: 56
        is_predefined_policy:
            description:
                - Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - "An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - "The current state of the protection policy. Allowed values are:
                    - CREATING
                    - UPDATING
                    - ACTIVE
                    - DELETING
                    - DELETED
                    - FAILED"
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information
                  for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_retention_period_in_days": 56,
        "is_predefined_policy": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.recovery import DatabaseRecoveryClient
    from oci.recovery.models import ChangeProtectionPolicyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionPolicyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "protection_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("protection_policy_id")

    def get_get_fn(self):
        return self.client.get_protection_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protection_policy,
            protection_policy_id=self.module.params.get("protection_policy_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeProtectionPolicyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_protection_policy_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                protection_policy_id=self.module.params.get("protection_policy_id"),
                change_protection_policy_compartment_details=action_details,
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


ProtectionPolicyActionsHelperCustom = get_custom_class(
    "ProtectionPolicyActionsHelperCustom"
)


class ResourceHelper(
    ProtectionPolicyActionsHelperCustom, ProtectionPolicyActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            protection_policy_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="protection_policy",
        service_client_class=DatabaseRecoveryClient,
        namespace="recovery",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
