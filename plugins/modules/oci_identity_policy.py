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
module: oci_identity_policy
short_description: Manage a Policy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Policy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new policy in the specified compartment (either the tenancy or another of your compartments).
      If you're new to policies, see L(Getting Started with Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm).
    - "You must specify a *name* for the policy, which must be unique across all policies in your tenancy
      and cannot be changed."
    - "You must also specify a *description* for the policy (although it can be an empty string). It does not
      have to be unique, and you can change it anytime with L(UpdatePolicy,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/Policy/UpdatePolicy)."
    - You must specify one or more policy statements in the statements array. For information about writing
      policies, see L(How Policies Work,https://docs.cloud.oracle.com/Content/Identity/Concepts/policies.htm) and
      L(Common Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/commonpolicies.htm).
    - After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
      object, first make sure its `lifecycleState` has changed to ACTIVE.
    - New policies take effect typically within 10 seconds.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment containing the policy (either the tenancy or another compartment).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the policy during creation. The name must be unique across all policies
              in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    statements:
        description:
            - An array of policy statements written in the policy language. See
              L(How Policies Work,https://docs.cloud.oracle.com/Content/Identity/Concepts/policies.htm) and
              L(Common Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/commonpolicies.htm).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
    description:
        description:
            - The description you assign to the policy during creation. Does not have to be unique, and it's changeable.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    version_date:
        description:
            - The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
              policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
              date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    policy_id:
        description:
            - The OCID of the policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Policy.
            - Use I(state=present) to create or update a Policy.
            - Use I(state=absent) to delete a Policy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create policy
  oci_identity_policy:
    compartment_id: "ocid1.tenancy.oc1..aaaaaaaaba3pexampleuniqueID"
    description: "Policy for users who need to launch instances, attach volumes, manage images"
    name: "LaunchInstances"
    statements:
    - "Allow group InstanceLaunchers to manage instance-family in compartment ABC"
    - "Allow group InstanceLaunchers to use volume-family in compartment ABC"
    - "Allow group InstanceLaunchers to use virtual-network-family in compartment Network"

- name: Update policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_policy:
    compartment_id: "ocid1.tenancy.oc1..aaaaaaaaba3pexampleuniqueID"
    name: LaunchInstances
    statements: [ "Allow group InstanceLaunchers to manage instance-family in compartment ABC" ]
    description: Policy for users who need to launch instances, attach volumes, manage images
    version_date: 2013-10-20T19:20:30+01:00
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update policy
  oci_identity_policy:
    statements: [ "Allow group InstanceLaunchers to manage instance-family in compartment ABC" ]
    description: Policy for users who need to launch instances, attach volumes, manage images
    policy_id: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete policy
  oci_identity_policy:
    policy_id: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_policy:
    compartment_id: "ocid1.tenancy.oc1..aaaaaaaaba3pexampleuniqueID"
    name: LaunchInstances
    state: absent

"""

RETURN = """
policy:
    description:
        - Details of the Policy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the policy.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the policy (either the tenancy or another compartment).
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the policy during creation. The name must be unique across all policies
                  in the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        statements:
            description:
                - An array of one or more policy statements written in the policy language.
            returned: on success
            type: list
            sample: []
        description:
            description:
                - The description you assign to the policy. Does not have to be unique, and it's changeable.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - Date and time the policy was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The policy's current state. After creating a policy, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        version_date:
            description:
                - The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
                  policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
                  date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "statements": [],
        "description": "description_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "version_date": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.identity import IdentityClient
    from oci.identity.models import CreatePolicyDetails
    from oci.identity.models import UpdatePolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("policy_id")

    def get_get_fn(self):
        return self.client.get_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_policy, policy_id=self.module.params.get("policy_id"),
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
        return oci_common_utils.list_all_resources(self.client.list_policies, **kwargs)

    def get_create_model_class(self):
        return CreatePolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_policy_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                policy_id=self.module.params.get("policy_id"),
                update_policy_details=update_details,
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
            call_fn=self.client.delete_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(policy_id=self.module.params.get("policy_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PolicyHelperCustom = get_custom_class("PolicyHelperCustom")


class ResourceHelper(PolicyHelperCustom, PolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            statements=dict(type="list"),
            description=dict(type="str"),
            version_date=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="policy",
        service_client_class=IdentityClient,
        namespace="identity",
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
