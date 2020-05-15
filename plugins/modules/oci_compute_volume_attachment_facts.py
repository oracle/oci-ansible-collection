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
module: oci_compute_volume_attachment_facts
short_description: Fetches details about one or multiple VolumeAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VolumeAttachment resources in Oracle Cloud Infrastructure
    - Lists the volume attachments in the specified compartment. You can filter the
      list by specifying an instance OCID, volume OCID, or both.
    - Currently, the only supported volume attachment type are L(IScsiVolumeAttachment,https://docs.cloud.oracle.com/#/en/iaas/20160918/IScsiVolumeAttachment/)
      and
      L(ParavirtualizedVolumeAttachment,https://docs.cloud.oracle.com/#/en/iaas/20160918/ParavirtualizedVolumeAttachment/).
    - If I(volume_attachment_id) is specified, the details of a single VolumeAttachment will be returned.
version_added: "2.5"
options:
    volume_attachment_id:
        description:
            - The OCID of the volume attachment.
            - Required to get a specific volume_attachment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple volume_attachments.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    instance_id:
        description:
            - The OCID of the instance.
        type: str
    volume_id:
        description:
            - The OCID of the volume.
        type: str
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List volume_attachments
  oci_compute_volume_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific volume_attachment
  oci_compute_volume_attachment_facts:
    volume_attachment_id: ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
volume_attachments:
    description:
        - List of VolumeAttachment resources
    returned: on success
    type: complex
    contains:
        attachment_type:
            description:
                - The type of volume attachment.
            returned: on success
            type: string
            sample: attachment_type_example
        availability_domain:
            description:
                - The availability domain of an instance.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        device:
            description:
                - The device name.
            returned: on success
            type: string
            sample: device_example
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it cannot be changed.
                  Avoid entering confidential information.
                - "Example: `My volume attachment`"
            returned: on success
            type: string
            sample: My volume attachment
        id:
            description:
                - The OCID of the volume attachment.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        instance_id:
            description:
                - The OCID of the instance the volume is attached to.
            returned: on success
            type: string
            sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
        is_read_only:
            description:
                - Whether the attachment was created in read-only mode.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the volume attachment.
            returned: on success
            type: string
            sample: ATTACHING
        time_created:
            description:
                - The date and time the volume was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        volume_id:
            description:
                - The OCID of the volume.
            returned: on success
            type: string
            sample: ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx
        is_pv_encryption_in_transit_enabled:
            description:
                - Whether in-transit encryption for the data volume's paravirtualized attachment is enabled or not.
            returned: on success
            type: bool
            sample: true
        chap_secret:
            description:
                - "The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name.
                  (Also called the \\"CHAP password\\".)"
                - "Example: `d6866c0d-298b-48ba-95af-309b4faux45e`"
            returned: on success
            type: string
            sample: d6866c0d-298b-48ba-95af-309b4faux45e
        chap_username:
            description:
                - The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                - "Example: `ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q`"
            returned: on success
            type: string
            sample: ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q
        ipv4:
            description:
                - The volume's iSCSI IP address.
                - "Example: `169.254.0.2`"
            returned: on success
            type: string
            sample: 169.254.0.2
        iqn:
            description:
                - The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                - "Example: `iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9`"
            returned: on success
            type: string
            sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
        port:
            description:
                - The volume's iSCSI port.
                - "Example: `3260`"
            returned: on success
            type: int
            sample: 3260
        iscsi_attach_commands:
            description:
                - Commands to attach the iSCSI block volume. Empty if attachment_type is not iscsi.
            returned: on success
            type: list
            sample: [ "sudo iscsiadm -m node -o new -T IQN -p IP:PORT", "sudo iscsiadm -m node -o update ..." ]
        iscsi_detach_commands:
            description:
                - Commands to detach the iSCSI block volume. Empty if attachment_type is not iscsi.
            returned: on success
            type: list
            sample: [ "sudo iscsiadm -m node -T IQN -p IP:PORT -u", "sudo iscsiadm -m node -o delete -T IQN" ]
    sample: [{
        "attachment_type": "attachment_type_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "device": "device_example",
        "display_name": "My volume attachment",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "is_read_only": true,
        "lifecycle_state": "ATTACHING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx",
        "is_pv_encryption_in_transit_enabled": true,
        "chap_secret": "d6866c0d-298b-48ba-95af-309b4faux45e",
        "chap_username": "ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q",
        "ipv4": "169.254.0.2",
        "iqn": "iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9",
        "port": 3260,
        "iscsi_attach_commands": [ "sudo iscsiadm -m node -o new -T IQN -p IP:PORT", "sudo iscsiadm -m node -o update ..." ],
        "iscsi_detach_commands": [ "sudo iscsiadm -m node -T IQN -p IP:PORT -u", "sudo iscsiadm -m node -o delete -T IQN" ]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "volume_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_attachment,
            volume_attachment_id=self.module.params.get("volume_attachment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "instance_id",
            "volume_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_volume_attachments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VolumeAttachmentFactsHelperCustom = get_custom_class(
    "VolumeAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    VolumeAttachmentFactsHelperCustom, VolumeAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            volume_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            instance_id=dict(type="str"),
            volume_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="volume_attachment",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(volume_attachments=result)


if __name__ == "__main__":
    main()
