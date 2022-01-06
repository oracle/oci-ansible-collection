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
module: oci_compute_boot_volume_attachment
short_description: Manage a BootVolumeAttachment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a BootVolumeAttachment resource in Oracle Cloud Infrastructure
    - For I(state=present), attaches the specified boot volume to the specified instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    boot_volume_id:
        description:
            - The OCID of the  boot volume.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    instance_id:
        description:
            - The OCID of the instance.
            - Required for create using I(state=present).
        type: str
    encryption_in_transit_type:
        description:
            - Refer the top-level definition of encryptionInTransitType.
              The default value is NONE.
        type: str
        choices:
            - "NONE"
            - "BM_ENCRYPTION_IN_TRANSIT"
    boot_volume_attachment_id:
        description:
            - The OCID of the boot volume attachment.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the BootVolumeAttachment.
            - Use I(state=present) to create a BootVolumeAttachment.
            - Use I(state=absent) to delete a BootVolumeAttachment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create boot_volume_attachment
  oci_compute_boot_volume_attachment:
    # required
    boot_volume_id: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    encryption_in_transit_type: NONE

- name: Delete boot_volume_attachment
  oci_compute_boot_volume_attachment:
    # required
    boot_volume_attachment_id: "ocid1.bootvolumeattachment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete boot_volume_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_boot_volume_attachment:
    # required
    display_name: display_name_example
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
boot_volume_attachment:
    description:
        - Details of the BootVolumeAttachment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of an instance.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        boot_volume_id:
            description:
                - The OCID of the boot volume.
            returned: on success
            type: str
            sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The OCID of the boot volume attachment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the instance the boot volume is attached to.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the boot volume attachment.
            returned: on success
            type: str
            sample: ATTACHING
        time_created:
            description:
                - The date and time the boot volume was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_pv_encryption_in_transit_enabled:
            description:
                - Whether in-transit encryption for the boot volume's paravirtualized attachment is enabled or not.
            returned: on success
            type: bool
            sample: true
        encryption_in_transit_type:
            description:
                - Refer the top-level definition of encryptionInTransitType.
                  The default value is NONE.
            returned: on success
            type: str
            sample: NONE
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "is_pv_encryption_in_transit_enabled": true,
        "encryption_in_transit_type": "NONE"
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
    from oci.core import ComputeClient
    from oci.core.models import AttachBootVolumeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "boot_volume_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("boot_volume_attachment_id")

    def get_get_fn(self):
        return self.client.get_boot_volume_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume_attachment,
            boot_volume_attachment_id=self.module.params.get(
                "boot_volume_attachment_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "availability_domain",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["instance_id", "boot_volume_id"]

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
            self.client.list_boot_volume_attachments, **kwargs
        )

    def get_create_model_class(self):
        return AttachBootVolumeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_boot_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(attach_boot_volume_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_boot_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_attachment_id=self.module.params.get(
                    "boot_volume_attachment_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


BootVolumeAttachmentHelperCustom = get_custom_class("BootVolumeAttachmentHelperCustom")


class ResourceHelper(BootVolumeAttachmentHelperCustom, BootVolumeAttachmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            boot_volume_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            instance_id=dict(type="str"),
            encryption_in_transit_type=dict(
                type="str", choices=["NONE", "BM_ENCRYPTION_IN_TRANSIT"]
            ),
            boot_volume_attachment_id=dict(aliases=["id"], type="str"),
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="boot_volume_attachment",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
