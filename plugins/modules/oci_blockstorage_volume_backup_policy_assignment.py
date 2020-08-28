#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_blockstorage_volume_backup_policy_assignment
short_description: Manage a VolumeBackupPolicyAssignment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a VolumeBackupPolicyAssignment resource in Oracle Cloud Infrastructure
    - For I(state=present), assigns a volume backup policy to the specified volume. Note that a given volume can
      only have one backup policy assigned to it. If this operation is used for a volume that already
      has a different backup policy assigned, the prior backup policy will be silently unassigned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    asset_id:
        description:
            - The OCID of the volume to assign the policy to.
            - Required for create using I(state=present).
        type: str
    policy_id:
        description:
            - The OCID of the volume backup policy to assign to the volume.
            - Required for create using I(state=present).
        type: str
    policy_assignment_id:
        description:
            - The OCID of the volume backup policy assignment.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VolumeBackupPolicyAssignment.
            - Use I(state=present) to create a VolumeBackupPolicyAssignment.
            - Use I(state=absent) to delete a VolumeBackupPolicyAssignment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create volume_backup_policy_assignment
  oci_blockstorage_volume_backup_policy_assignment:
    asset_id: ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx
    policy_id: ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete volume_backup_policy_assignment
  oci_blockstorage_volume_backup_policy_assignment:
    policy_assignment_id: ocid1.policyassignment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
volume_backup_policy_assignment:
    description:
        - Details of the VolumeBackupPolicyAssignment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        asset_id:
            description:
                - The OCID of the volume the policy has been assigned to.
            returned: on success
            type: string
            sample: ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The OCID of the volume backup policy assignment.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        policy_id:
            description:
                - The OCID of the volume backup policy that has been assigned to the volume.
            returned: on success
            type: string
            sample: ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the volume backup policy was assigned to the volume. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "asset_id": "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "policy_id": "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.core import BlockstorageClient
    from oci.core.models import CreateVolumeBackupPolicyAssignmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupPolicyAssignmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "policy_assignment_id"

    def get_module_resource_id(self):
        return self.module.params.get("policy_assignment_id")

    def get_get_fn(self):
        return self.client.get_volume_backup_policy_assignment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup_policy_assignment,
            policy_assignment_id=self.module.params.get("policy_assignment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "asset_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.get_volume_backup_policy_asset_assignment, **kwargs
        )

    def get_create_model_class(self):
        return CreateVolumeBackupPolicyAssignmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_volume_backup_policy_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_volume_backup_policy_assignment_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_volume_backup_policy_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                policy_assignment_id=self.module.params.get("policy_assignment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


VolumeBackupPolicyAssignmentHelperCustom = get_custom_class(
    "VolumeBackupPolicyAssignmentHelperCustom"
)


class ResourceHelper(
    VolumeBackupPolicyAssignmentHelperCustom, VolumeBackupPolicyAssignmentHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            asset_id=dict(type="str"),
            policy_id=dict(type="str"),
            policy_assignment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_backup_policy_assignment",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
