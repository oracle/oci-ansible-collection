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
module: oci_compute_volume_attachment_facts
short_description: Fetches details about one or multiple VolumeAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VolumeAttachment resources in Oracle Cloud Infrastructure
    - Lists the volume attachments in the specified compartment. You can filter the
      list by specifying an instance OCID, volume OCID, or both.
    - Currently, the only supported volume attachment type are L(IScsiVolumeAttachment,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/IScsiVolumeAttachment/) and
      L(ParavirtualizedVolumeAttachment,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ParavirtualizedVolumeAttachment/).
    - If I(volume_attachment_id) is specified, the details of a single VolumeAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    volume_attachment_id:
        description:
            - The OCID of the volume attachment.
            - Required to get a specific volume_attachment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific volume_attachment
  oci_compute_volume_attachment_facts:
    # required
    volume_attachment_id: "ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List volume_attachments
  oci_compute_volume_attachment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
volume_attachments:
    description:
        - List of VolumeAttachment resources
    returned: on success
    type: complex
    contains:
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
            sample: chap_username_example
        ipv4:
            description:
                - The volume's iSCSI IP address.
                - "Example: `169.254.0.2`"
            returned: on success
            type: str
            sample: ipv4_example
        iqn:
            description:
                - The target volume's iSCSI Qualified Name in the format defined
                  by L(RFC 3720,https://tools.ietf.org/html/rfc3720#page-32).
                - "Example: `iqn.2015-12.us.oracle.com:<CHAP_username>`"
            returned: on success
            type: str
            sample: iqn_example
        port:
            description:
                - The volume's iSCSI port, usually port 860 or 3260.
                - "Example: `3260`"
            returned: on success
            type: int
            sample: 56
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
                    sample: ipv4_example
                iqn:
                    description:
                        - The target volume's iSCSI Qualified Name in the format defined
                          by L(RFC 3720,https://tools.ietf.org/html/rfc3720#page-32).
                        - "Example: `iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195`"
                    returned: on success
                    type: str
                    sample: iqn_example
                port:
                    description:
                        - The volume's iSCSI port, usually port 860 or 3260.
                        - "Example: `3260`"
                    returned: on success
                    type: int
                    sample: 56
        encryption_in_transit_type:
            description:
                - Refer the top-level definition of encryptionInTransitType.
                  The default value is NONE.
            returned: on success
            type: str
            sample: NONE
        is_agent_auto_iscsi_login_enabled:
            description:
                - Whether Oracle Cloud Agent is enabled perform the iSCSI login and logout commands after the volume attach or detach operations for non
                  multipath-enabled iSCSI attachments.
            returned: on success
            type: bool
            sample: true
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
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
            sample: "2013-10-20T19:20:30+01:00"
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
                - Whether the Iscsi or Paravirtualized attachment is multipath or not, it is not applicable to NVMe attachment.
            returned: on success
            type: bool
            sample: true
        iscsi_login_state:
            description:
                - The iscsi login state of the volume attachment. For a Iscsi volume attachment,
                  all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.
            returned: on success
            type: str
            sample: UNKNOWN
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
    sample: [{
        "chap_secret": "chap_secret_example",
        "chap_username": "chap_username_example",
        "ipv4": "ipv4_example",
        "iqn": "iqn_example",
        "port": 56,
        "multipath_devices": [{
            "ipv4": "ipv4_example",
            "iqn": "iqn_example",
            "port": 56
        }],
        "encryption_in_transit_type": "NONE",
        "is_agent_auto_iscsi_login_enabled": true,
        "attachment_type": "emulated",
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "device": "device_example",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "is_read_only": true,
        "is_shareable": true,
        "lifecycle_state": "ATTACHING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx",
        "is_pv_encryption_in_transit_enabled": true,
        "is_multipath": true,
        "iscsi_login_state": "UNKNOWN",
        "iscsi_attach_commands": [  "sudo iscsiadm -m node -o new -T IQN -p IP:PORT", "sudo iscsiadm -m node -o update ..."  ],
        "iscsi_detach_commands": [  "sudo iscsiadm -m node -T IQN -p IP:PORT -u", "sudo iscsiadm -m node -o delete -T IQN"  ]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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

    module = OCIAnsibleModule(argument_spec=module_args)

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
