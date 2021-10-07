#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_compute_volume_attachment
short_description: Manage a VolumeAttachment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VolumeAttachment resource in Oracle Cloud Infrastructure
    - For I(state=present), attaches the specified storage volume to the specified instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    device:
        description:
            - The device name.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    instance_id:
        description:
            - The OCID of the instance.
            - Required for create using I(state=present).
        type: str
    is_read_only:
        description:
            - Whether the attachment was created in read-only mode.
        type: bool
    is_shareable:
        description:
            - Whether the attachment should be created in shareable mode. If an attachment
              is created in shareable mode, then other instances can attach the same volume, provided
              that they also create their attachments in shareable mode. Only certain volume types can
              be attached in shareable mode. Defaults to false if not specified.
        type: bool
    type:
        description:
            - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
            - Required for create using I(state=present).
        type: str
        choices:
            - "service_determined"
            - "emulated"
            - "iscsi"
            - "paravirtualized"
    volume_id:
        description:
            - The OCID of the volume.
            - Required for create using I(state=present).
        type: str
    use_chap:
        description:
            - Whether to use CHAP authentication for the volume attachment. Defaults to false.
            - Applicable when type is 'iscsi'
        type: bool
    encryption_in_transit_type:
        description:
            - Refer the top-level definition of encryptionInTransitType.
              The default value is NONE.
            - Applicable when type is 'iscsi'
        type: str
        choices:
            - "NONE"
            - "BM_ENCRYPTION_IN_TRANSIT"
    is_pv_encryption_in_transit_enabled:
        description:
            - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
            - Applicable when type is 'paravirtualized'
        type: bool
    volume_attachment_id:
        description:
            - The OCID of the volume attachment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    iscsi_login_state:
        description:
            - The iscsi login state of the volume attachment. For a multipath volume attachment,
              all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.
            - This parameter is updatable.
        type: str
        choices:
            - "UNKNOWN"
            - "LOGGING_IN"
            - "LOGIN_SUCCEEDED"
            - "LOGIN_FAILED"
            - "LOGGING_OUT"
            - "LOGOUT_SUCCEEDED"
            - "LOGOUT_FAILED"
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the VolumeAttachment.
            - Use I(state=present) to create or update a VolumeAttachment.
            - Use I(state=absent) to delete a VolumeAttachment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create volume_attachment
  oci_compute_volume_attachment:
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    type: paravirtualized
    volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update volume_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_volume_attachment:
    display_name: display_name_example
    iscsi_login_state: UNKNOWN
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update volume_attachment
  oci_compute_volume_attachment:
    volume_attachment_id: "ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx"
    iscsi_login_state: UNKNOWN

- name: Delete volume_attachment
  oci_compute_volume_attachment:
    volume_attachment_id: "ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete volume_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_volume_attachment:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
volume_attachment:
    description:
        - Details of the VolumeAttachment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        attachment_type:
            description:
                - The type of volume attachment.
            returned: on success
            type: str
            sample: emulated
        availability_domain:
            description:
                - The availability domain of an instance.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        device:
            description:
                - The device name.
            returned: on success
            type: str
            sample: device_example
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it cannot be changed.
                  Avoid entering confidential information.
                - "Example: `My volume attachment`"
            returned: on success
            type: str
            sample: My volume attachment
        id:
            description:
                - The OCID of the volume attachment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the instance the volume is attached to.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        is_read_only:
            description:
                - Whether the attachment was created in read-only mode.
            returned: on success
            type: bool
            sample: true
        is_shareable:
            description:
                - Whether the attachment should be created in shareable mode. If an attachment
                  is created in shareable mode, then other instances can attach the same volume, provided
                  that they also create their attachments in shareable mode. Only certain volume types can
                  be attached in shareable mode. Defaults to false if not specified.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the volume attachment.
            returned: on success
            type: str
            sample: ATTACHING
        time_created:
            description:
                - The date and time the volume was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        volume_id:
            description:
                - The OCID of the volume.
            returned: on success
            type: str
            sample: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
        is_pv_encryption_in_transit_enabled:
            description:
                - Whether in-transit encryption for the data volume's paravirtualized attachment is enabled or not.
            returned: on success
            type: bool
            sample: true
        is_multipath:
            description:
                - Whether the attachment is multipath or not.
            returned: on success
            type: bool
            sample: true
        iscsi_login_state:
            description:
                - The iscsi login state of the volume attachment. For a multipath volume attachment,
                  all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.
            returned: on success
            type: str
            sample: UNKNOWN
        chap_secret:
            description:
                - "The Challenge-Handshake-Authentication-Protocol (CHAP) secret
                  valid for the associated CHAP user name.
                  (Also called the \\"CHAP password\\".)"
            returned: on success
            type: str
            sample: chap_secret_example
        chap_username:
            description:
                - The volume's system-generated Challenge-Handshake-Authentication-Protocol
                  (CHAP) user name. See L(RFC 1994,https://tools.ietf.org/html/rfc1994) for more on CHAP.
                - "Example: `ocid1.volume.oc1.phx.<unique_ID>`"
            returned: on success
            type: str
            sample: ocid1.volume.oc1.phx.<unique_ID>
        ipv4:
            description:
                - The volume's iSCSI IP address.
                - "Example: `169.254.0.2`"
            returned: on success
            type: str
            sample: 169.254.0.2
        iqn:
            description:
                - The target volume's iSCSI Qualified Name in the format defined
                  by L(RFC 3720,https://tools.ietf.org/html/rfc3720#page-32).
                - "Example: `iqn.2015-12.us.oracle.com:<CHAP_username>`"
            returned: on success
            type: str
            sample: iqn.2015-12.us.oracle.com:<CHAP_username>
        port:
            description:
                - The volume's iSCSI port, usually port 860 or 3260.
                - "Example: `3260`"
            returned: on success
            type: int
            sample: 3260
        multipath_devices:
            description:
                - A list of secondary multipath devices
            returned: on success
            type: complex
            contains:
                ipv4:
                    description:
                        - The volume's iSCSI IP address.
                        - "Example: `169.254.2.2`"
                    returned: on success
                    type: str
                    sample: 169.254.2.2
                iqn:
                    description:
                        - The target volume's iSCSI Qualified Name in the format defined
                          by L(RFC 3720,https://tools.ietf.org/html/rfc3720#page-32).
                        - "Example: `iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195`"
                    returned: on success
                    type: str
                    sample: iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195
                port:
                    description:
                        - The volume's iSCSI port, usually port 860 or 3260.
                        - "Example: `3260`"
                    returned: on success
                    type: int
                    sample: 3260
        encryption_in_transit_type:
            description:
                - Refer the top-level definition of encryptionInTransitType.
                  The default value is NONE.
            returned: on success
            type: str
            sample: NONE
        iscsi_attach_commands:
            description:
                - Commands to attach the iSCSI block volume. Empty if attachment_type is not iscsi.
            returned: on success
            type: list
            sample: [  "sudo iscsiadm -m node -o new -T IQN -p IP:PORT", "sudo iscsiadm -m node -o update ..."  ]
        iscsi_detach_commands:
            description:
                - Commands to detach the iSCSI block volume. Empty if attachment_type is not iscsi.
            returned: on success
            type: list
            sample: [  "sudo iscsiadm -m node -T IQN -p IP:PORT -u", "sudo iscsiadm -m node -o delete -T IQN"  ]
    sample: {
        "attachment_type": "emulated",
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "device": "device_example",
        "display_name": "My volume attachment",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "is_read_only": true,
        "is_shareable": true,
        "lifecycle_state": "ATTACHING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx",
        "is_pv_encryption_in_transit_enabled": true,
        "is_multipath": true,
        "iscsi_login_state": "UNKNOWN",
        "chap_secret": "chap_secret_example",
        "chap_username": "ocid1.volume.oc1.phx.<unique_ID>",
        "ipv4": "169.254.0.2",
        "iqn": "iqn.2015-12.us.oracle.com:<CHAP_username>",
        "port": 3260,
        "multipath_devices": [{
            "ipv4": "169.254.2.2",
            "iqn": "iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195",
            "port": 3260
        }],
        "encryption_in_transit_type": "NONE",
        "iscsi_attach_commands": [  "sudo iscsiadm -m node -o new -T IQN -p IP:PORT", "sudo iscsiadm -m node -o update ..."  ],
        "iscsi_detach_commands": [  "sudo iscsiadm -m node -T IQN -p IP:PORT -u", "sudo iscsiadm -m node -o delete -T IQN"  ]
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
    from oci.core.models import AttachVolumeDetails
    from oci.core.models import UpdateVolumeAttachmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "volume_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_attachment_id")

    def get_get_fn(self):
        return self.client.get_volume_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_attachment,
            volume_attachment_id=self.module.params.get("volume_attachment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["instance_id", "volume_id"]

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
            self.client.list_volume_attachments, **kwargs
        )

    def get_create_model_class(self):
        return AttachVolumeDetails

    def get_exclude_attributes(self):
        return ["type", "use_chap"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(attach_volume_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVolumeAttachmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_attachment_id=self.module.params.get("volume_attachment_id"),
                update_volume_attachment_details=update_details,
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
            call_fn=self.client.detach_volume,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_attachment_id=self.module.params.get("volume_attachment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VolumeAttachmentHelperCustom = get_custom_class("VolumeAttachmentHelperCustom")


class ResourceHelper(VolumeAttachmentHelperCustom, VolumeAttachmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            device=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            instance_id=dict(type="str"),
            is_read_only=dict(type="bool"),
            is_shareable=dict(type="bool"),
            type=dict(
                type="str",
                choices=["service_determined", "emulated", "iscsi", "paravirtualized"],
            ),
            volume_id=dict(type="str"),
            use_chap=dict(type="bool"),
            encryption_in_transit_type=dict(
                type="str", choices=["NONE", "BM_ENCRYPTION_IN_TRANSIT"]
            ),
            is_pv_encryption_in_transit_enabled=dict(type="bool"),
            volume_attachment_id=dict(aliases=["id"], type="str"),
            iscsi_login_state=dict(
                type="str",
                choices=[
                    "UNKNOWN",
                    "LOGGING_IN",
                    "LOGIN_SUCCEEDED",
                    "LOGIN_FAILED",
                    "LOGGING_OUT",
                    "LOGOUT_SUCCEEDED",
                    "LOGOUT_FAILED",
                ],
            ),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_attachment",
        service_client_class=ComputeClient,
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
