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
module: oci_blockstorage_volume_group
short_description: Manage a VolumeGroup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VolumeGroup resource in Oracle Cloud Infrastructure
    - "For I(state=present), creates a new volume group in the specified compartment.
      A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing
      volume group, or by restoring a volume group backup.
      You may optionally specify a *display name* for the volume group, which is simply a friendly name or
      description. It does not have to be unique, and you can change it. Avoid entering confidential information."
    - For more information, see L(Volume Groups,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).
    - "This resource has the following action operations in the M(oci_volume_group_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain of the volume group.
            - Required for create using I(state=present).
        type: str
    backup_policy_id:
        description:
            - If provided, specifies the ID of the volume backup policy to assign to the newly
              created volume group. If omitted, no policy will be assigned.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the volume group.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name for the volume group. Does not have to be
              unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    source_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            type:
                description:
                    - ""
                type: str
                choices:
                    - "volumeGroupId"
                    - "volumeIds"
                    - "volumeGroupBackupId"
                required: true
            volume_group_id:
                description:
                    - The OCID of the volume group to clone from.
                    - Required when type is 'volumeGroupId'
                type: str
            volume_ids:
                description:
                    - OCIDs for the volumes in this volume group.
                    - Required when type is 'volumeIds'
                type: list
            volume_group_backup_id:
                description:
                    - The OCID of the volume group backup to restore from.
                    - Required when type is 'volumeGroupBackupId'
                type: str
    volume_group_id:
        description:
            - The Oracle Cloud ID (OCID) that uniquely identifies the volume group.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    volume_ids:
        description:
            - OCIDs for the volumes in this volume group.
            - This parameter is updatable.
        type: list
    state:
        description:
            - The state of the VolumeGroup.
            - Use I(state=present) to create or update a VolumeGroup.
            - Use I(state=absent) to delete a VolumeGroup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create volume_group
  oci_blockstorage_volume_group:
    availability_domain: "Uocm:PHX-AD-1"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    source_details:
      type: "volumeIds"
      volume_ids:
      - "ocid1.volume.oc1..xxxxxEXAMPLExxxxx...vm62xq"

- name: Update volume_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_group:
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update volume_group
  oci_blockstorage_volume_group:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    volume_group_id: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete volume_group
  oci_blockstorage_volume_group:
    volume_group_id: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete volume_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_group:
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    display_name: display_name_example
    state: absent

"""

RETURN = """
volume_group:
    description:
        - Details of the VolumeGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the volume group.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume group.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the volume group. Does not have to be
                  unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID for the volume group.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of a volume group.
            returned: on success
            type: string
            sample: PROVISIONING
        size_in_mbs:
            description:
                - The aggregate size of the volume group in MBs.
            returned: on success
            type: int
            sample: 56
        size_in_gbs:
            description:
                - The aggregate size of the volume group in GBs.
            returned: on success
            type: int
            sample: 56
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - ""
                    returned: on success
                    type: string
                    sample: volumeGroupId
                volume_group_id:
                    description:
                        - The OCID of the volume group to clone from.
                    returned: on success
                    type: string
                    sample: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
                volume_ids:
                    description:
                        - OCIDs for the volumes in this volume group.
                    returned: on success
                    type: list
                    sample: []
                volume_group_backup_id:
                    description:
                        - The OCID of the volume group backup to restore from.
                    returned: on success
                    type: string
                    sample: "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the volume group was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        volume_ids:
            description:
                - OCIDs for the volumes in this volume group.
            returned: on success
            type: list
            sample: []
        is_hydrated:
            description:
                - Specifies whether the newly created cloned volume group's data has finished copying
                  from the source volume group or backup.
            returned: on success
            type: bool
            sample: true
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "size_in_mbs": 56,
        "size_in_gbs": 56,
        "source_details": {
            "type": "volumeGroupId",
            "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx",
            "volume_ids": [],
            "volume_group_backup_id": "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "volume_ids": [],
        "is_hydrated": true
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
    from oci.core.models import CreateVolumeGroupDetails
    from oci.core.models import UpdateVolumeGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeGroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "volume_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_group_id")

    def get_get_fn(self):
        return self.client.get_volume_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_group,
            volume_group_id=self.module.params.get("volume_group_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["availability_domain", "display_name"]

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
            self.client.list_volume_groups, **kwargs
        )

    def get_create_model_class(self):
        return CreateVolumeGroupDetails

    def get_exclude_attributes(self):
        return ["backup_policy_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_volume_group,
            call_fn_args=(),
            call_fn_kwargs=dict(create_volume_group_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVolumeGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_id=self.module.params.get("volume_group_id"),
                update_volume_group_details=update_details,
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
            call_fn=self.client.delete_volume_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_id=self.module.params.get("volume_group_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VolumeGroupHelperCustom = get_custom_class("VolumeGroupHelperCustom")


class ResourceHelper(VolumeGroupHelperCustom, VolumeGroupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            backup_policy_id=dict(type="str"),
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            source_details=dict(
                type="dict",
                options=dict(
                    type=dict(
                        type="str",
                        required=True,
                        choices=["volumeGroupId", "volumeIds", "volumeGroupBackupId"],
                    ),
                    volume_group_id=dict(type="str"),
                    volume_ids=dict(type="list"),
                    volume_group_backup_id=dict(type="str"),
                ),
            ),
            volume_group_id=dict(aliases=["id"], type="str"),
            volume_ids=dict(type="list"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_group",
        service_client_class=BlockstorageClient,
        namespace="core",
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
