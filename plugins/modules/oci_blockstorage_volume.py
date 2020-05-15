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
module: oci_blockstorage_volume
short_description: Manage a Volume resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Volume resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new volume in the specified compartment. Volumes can be created in sizes ranging from
      50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB).
      For general information about block volumes, see
      L(Overview of Block Volume Service,https://docs.cloud.oracle.com/Content/Block/Concepts/overview.htm).
    - A volume and instance can be in separate compartments but must be in the same availability domain.
      For information about access control and compartments, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm). For information about
      availability domains, see L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the `ListAvailabilityDomains` operation
      in the Identity and Access Management Service API.
    - "You may optionally specify a *display name* for the volume, which is simply a friendly name or
      description. It does not have to be unique, and you can change it. Avoid entering confidential information."
version_added: "2.5"
options:
    availability_domain:
        description:
            - The availability domain of the volume.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
        type: str
    backup_policy_id:
        description:
            - If provided, specifies the ID of the volume backup policy to assign to the newly
              created volume. If omitted, no policy will be assigned.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the volume.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    kms_key_id:
        description:
            - The OCID of the Key Management key to assign as the master encryption key
              for the volume.
        type: str
    size_in_gbs:
        description:
            - The size of the volume in GBs.
        type: int
    size_in_mbs:
        description:
            - The size of the volume in MBs. The value must be a multiple of 1024.
              This field is deprecated. Use sizeInGBs instead.
        type: int
    source_details:
        description:
            - Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a
              Block volume backup.
              This is an optional field. If not specified or set to null, the new Block volume will be empty.
              When specified, the new Block volume will contain data from the source volume or backup.
        type: dict
        suboptions:
            type:
                description:
                    - ""
                type: str
                choices:
                    - "volume"
                    - "volumeBackup"
                required: true
            id:
                description:
                    - The OCID of the volume.
                type: str
                required: true
    volume_backup_id:
        description:
            - The OCID of the volume backup from which the data should be restored on the newly created volume.
              This field is deprecated. Use the sourceDetails field instead to specify the
              backup for the volume.
        type: str
    volume_id:
        description:
            - The OCID of the volume.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Volume.
            - Use I(state=present) to create or update a Volume.
            - Use I(state=absent) to delete a Volume.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create volume
  oci_blockstorage_volume:
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update volume using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update volume
  oci_blockstorage_volume:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    volume_id: ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete volume
  oci_blockstorage_volume:
    volume_id: ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete volume using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    state: absent

"""

RETURN = """
volume:
    description:
        - Details of the Volume resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the volume.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the volume.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        is_hydrated:
            description:
                - Specifies whether the cloned volume's data has finished copying from the source volume or backup.
            returned: on success
            type: bool
            sample: true
        kms_key_id:
            description:
                - The OCID of the Key Management key which is the master encryption key for the volume.
            returned: on success
            type: string
            sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of a volume.
            returned: on success
            type: string
            sample: PROVISIONING
        size_in_gbs:
            description:
                - The size of the volume in GBs.
            returned: on success
            type: int
            sample: 56
        size_in_mbs:
            description:
                - The size of the volume in MBs. This field is deprecated. Use sizeInGBs instead.
            returned: on success
            type: int
            sample: 56
        source_details:
            description:
                - The volume source, either an existing volume in the same availability domain or a volume backup.
                  If null, an empty volume is created.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - ""
                    returned: on success
                    type: string
                    sample: volume
                id:
                    description:
                        - The OCID of the volume.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the volume was created. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        volume_group_id:
            description:
                - The OCID of the source volume group.
            returned: on success
            type: string
            sample: ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_hydrated": true,
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "size_in_gbs": 56,
        "size_in_mbs": 56,
        "source_details": {
            "type": "volume",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import CreateVolumeDetails
    from oci.core.models import UpdateVolumeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "volume_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_id")

    def get_get_fn(self):
        return self.client.get_volume

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume, volume_id=self.module.params.get("volume_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "availability_domain",
            "display_name",
        ]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(self.client.list_volumes, **kwargs)

    def get_create_model_class(self):
        return CreateVolumeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(create_volume_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateVolumeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_id=self.module.params.get("volume_id"),
                update_volume_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(volume_id=self.module.params.get("volume_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


VolumeHelperCustom = get_custom_class("VolumeHelperCustom")


class ResourceHelper(VolumeHelperCustom, VolumeHelperGen):
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
            kms_key_id=dict(type="str"),
            size_in_gbs=dict(type="int"),
            size_in_mbs=dict(type="int"),
            source_details=dict(
                type="dict",
                options=dict(
                    type=dict(
                        type="str", required=True, choices=["volume", "volumeBackup"]
                    ),
                    id=dict(type="str", required=True),
                ),
            ),
            volume_backup_id=dict(type="str"),
            volume_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume",
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
