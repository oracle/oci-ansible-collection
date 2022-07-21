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
module: oci_identity_tag_namespace_actions
short_description: Perform actions on a TagNamespace resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TagNamespace resource in Oracle Cloud Infrastructure
    - For I(action=add_tag_namespace_lock), add a resource lock to a tag namespace.
    - "For I(action=cascade_delete), deletes the specified tag namespace. This operation triggers a process that removes all of the tags
      defined in the specified tag namespace from all resources in your tenancy and then deletes the tag namespace.
      After you start the delete operation:
        * New tag key definitions cannot be created under the namespace.
        * The state of the tag namespace changes to DELETING.
        * Tag removal from the resources begins.
      This process can take up to 48 hours depending on the number of tag definitions in the namespace, the number of resources
      that are tagged, and the locations of the regions in which those resources reside.
      After all tags are removed, the state changes to DELETED. You cannot restore a deleted tag namespace. After the deleted tag namespace
      changes its state to DELETED, you can use the name of the deleted tag namespace again.
      After you start this operation, you cannot start either the L(DeleteTag,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Tag/DeleteTag)
      or the L(BulkDeleteTags,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Tag/BulkDeleteTags) operation until this process completes.
      To delete a tag namespace, you must first retire it. Use L(UpdateTagNamespace,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/TagNamespace/UpdateTagNamespace)
      to retire a tag namespace."
    - For I(action=change_compartment), moves the specified tag namespace to the specified compartment within the same tenancy.
      To move the tag namespace, you must have the manage tag-namespaces permission on both compartments.
      For more information about IAM policies, see L(Details for IAM,https://docs.cloud.oracle.com/Content/Identity/policyreference/iampolicyreference.htm).
      Moving a tag namespace moves all the tag key definitions contained in the tag namespace.
    - For I(action=remove_tag_namespace_lock), remove a resource lock from a tag namespace.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    related_resource_id:
        description:
            - The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.
            - Applicable only for I(action=add_tag_namespace_lock).
        type: str
    msg:
        description:
            - A message added by the creator of the lock. This is typically used to give an
              indication of why the resource is locked.
            - Applicable only for I(action=add_tag_namespace_lock).
        type: str
        aliases: ["message"]
    compartment_id:
        description:
            - The Oracle Cloud ID (OCID) of the destination compartment.
            - Required for I(action=change_compartment).
        type: str
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
            - Applicable only for I(action=cascade_delete)I(action=change_compartment).
        type: bool
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - Type of the lock.
            - Required for I(action=add_tag_namespace_lock), I(action=remove_tag_namespace_lock).
        type: str
        choices:
            - "FULL"
            - "DELETE"
    action:
        description:
            - The action to perform on the TagNamespace.
        type: str
        required: true
        choices:
            - "add_tag_namespace_lock"
            - "cascade_delete"
            - "change_compartment"
            - "remove_tag_namespace_lock"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_tag_namespace_lock on tag_namespace
  oci_identity_tag_namespace_actions:
    # required
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: add_tag_namespace_lock

    # optional
    related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    msg: msg_example

- name: Perform action cascade_delete on tag_namespace
  oci_identity_tag_namespace_actions:
    # required
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    action: cascade_delete

    # optional
    is_lock_override: true

- name: Perform action change_compartment on tag_namespace
  oci_identity_tag_namespace_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    is_lock_override: true

- name: Perform action remove_tag_namespace_lock on tag_namespace
  oci_identity_tag_namespace_actions:
    # required
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: remove_tag_namespace_lock

"""

RETURN = """
tag_namespace:
    description:
        - Details of the TagNamespace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the tag namespace.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the tag namespace.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the tag namespace.
            returned: on success
            type: str
            sample: description_example
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
        is_retired:
            description:
                - Whether the tag namespace is retired.
                  See L(Retiring Key Definitions and Namespace
                  Definitions,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a
                  tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - "Date and time the tagNamespace was created, in the format defined by RFC3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        locks:
            description:
                - Locks associated with this resource.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the lock.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the creator of the lock. This is typically used to give an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - When the lock was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                is_active:
                    description:
                        - Indicates if the lock is active or not. For example, if there are mutliple FULL locks, the first-created FULL lock will be effective.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_retired": true,
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "is_active": true
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import AddLockDetails
    from oci.identity.models import ChangeTagNamespaceCompartmentDetail
    from oci.identity.models import RemoveLockDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagNamespaceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_tag_namespace_lock
        cascade_delete
        change_compartment
        remove_tag_namespace_lock
    """

    @staticmethod
    def get_module_resource_id_param():
        return "tag_namespace_id"

    def get_module_resource_id(self):
        return self.module.params.get("tag_namespace_id")

    def get_get_fn(self):
        return self.client.get_tag_namespace

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag_namespace,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
        )

    def add_tag_namespace_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_tag_namespace_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                add_lock_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def cascade_delete(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cascade_delete_tag_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                is_lock_override=self.module.params.get("is_lock_override"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeTagNamespaceCompartmentDetail
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_tag_namespace_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                change_tag_namespace_compartment_detail=action_details,
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove_tag_namespace_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_tag_namespace_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                remove_lock_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


TagNamespaceActionsHelperCustom = get_custom_class("TagNamespaceActionsHelperCustom")


class ResourceHelper(TagNamespaceActionsHelperCustom, TagNamespaceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            related_resource_id=dict(type="str"),
            msg=dict(aliases=["message"], type="str"),
            compartment_id=dict(type="str"),
            is_lock_override=dict(type="bool"),
            tag_namespace_id=dict(aliases=["id"], type="str", required=True),
            type=dict(type="str", choices=["FULL", "DELETE"]),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_tag_namespace_lock",
                    "cascade_delete",
                    "change_compartment",
                    "remove_tag_namespace_lock",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tag_namespace",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
