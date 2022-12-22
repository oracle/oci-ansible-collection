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
module: oci_data_safe_target_alert_policy_association
short_description: Manage a TargetAlertPolicyAssociation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TargetAlertPolicyAssociation resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new target-alert policy association to track a alert policy applied on target.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_safe_target_alert_policy_association_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    policy_id:
        description:
            - The OCID of the alert policy.
            - Required for create using I(state=present).
        type: str
    target_id:
        description:
            - The OCID of the target.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment where the target-alert policy association is created.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_enabled:
        description:
            - Indicates if the target-alert policy association is enabled or disabled.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    display_name:
        description:
            - The display name of the target-alert policy association.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Describes the target-alert policy association.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    target_alert_policy_association_id:
        description:
            - The OCID of the target-alert policy association.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the TargetAlertPolicyAssociation.
            - Use I(state=present) to create or update a TargetAlertPolicyAssociation.
            - Use I(state=absent) to delete a TargetAlertPolicyAssociation.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create target_alert_policy_association
  oci_data_safe_target_alert_policy_association:
    # required
    policy_id: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_enabled: true

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update target_alert_policy_association
  oci_data_safe_target_alert_policy_association:
    # required
    target_alert_policy_association_id: "ocid1.targetalertpolicyassociation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_enabled: true
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update target_alert_policy_association using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_target_alert_policy_association:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    is_enabled: true
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete target_alert_policy_association
  oci_data_safe_target_alert_policy_association:
    # required
    target_alert_policy_association_id: "ocid1.targetalertpolicyassociation.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete target_alert_policy_association using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_target_alert_policy_association:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
target_alert_policy_association:
    description:
        - Details of the TargetAlertPolicyAssociation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the target-alert policy association.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the target-alert policy association.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Describes the target-alert policy association.
            returned: on success
            type: str
            sample: description_example
        policy_id:
            description:
                - The OCID of the alert policy.
            returned: on success
            type: str
            sample: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The OCID of the target on which alert policy is to be applied.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        is_enabled:
            description:
                - Indicates if the target-alert policy association is enabled or disabled.
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The OCID of the compartment that contains the policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Creation date and time of the alert policy, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Last date and time the alert policy was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the target-alert policy association.
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "policy_id": "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import CreateTargetAlertPolicyAssociationDetails
    from oci.data_safe.models import UpdateTargetAlertPolicyAssociationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeTargetAlertPolicyAssociationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataSafeTargetAlertPolicyAssociationHelperGen, self
        ).get_possible_entity_types() + [
            "targetalertpolicyassociation",
            "targetalertpolicyassociations",
            "dataSafetargetalertpolicyassociation",
            "dataSafetargetalertpolicyassociations",
            "targetalertpolicyassociationresource",
            "targetalertpolicyassociationsresource",
            "datasafe",
        ]

    def get_module_resource_id_param(self):
        return "target_alert_policy_association_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_alert_policy_association_id")

    def get_get_fn(self):
        return self.client.get_target_alert_policy_association

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_alert_policy_association,
            target_alert_policy_association_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_alert_policy_association,
            target_alert_policy_association_id=self.module.params.get(
                "target_alert_policy_association_id"
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
        optional_list_method_params = [
            "target_alert_policy_association_id",
            "target_id",
        ]

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
            self.client.list_target_alert_policy_associations, **kwargs
        )

    def get_create_model_class(self):
        return CreateTargetAlertPolicyAssociationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target_alert_policy_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_target_alert_policy_association_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTargetAlertPolicyAssociationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target_alert_policy_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_alert_policy_association_id=self.module.params.get(
                    "target_alert_policy_association_id"
                ),
                update_target_alert_policy_association_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_target_alert_policy_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_alert_policy_association_id=self.module.params.get(
                    "target_alert_policy_association_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafeTargetAlertPolicyAssociationHelperCustom = get_custom_class(
    "DataSafeTargetAlertPolicyAssociationHelperCustom"
)


class ResourceHelper(
    DataSafeTargetAlertPolicyAssociationHelperCustom,
    DataSafeTargetAlertPolicyAssociationHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            policy_id=dict(type="str"),
            target_id=dict(type="str"),
            compartment_id=dict(type="str"),
            is_enabled=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            target_alert_policy_association_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_alert_policy_association",
        service_client_class=DataSafeClient,
        namespace="data_safe",
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
