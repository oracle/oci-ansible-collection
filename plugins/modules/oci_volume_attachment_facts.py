#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_volume_attachment_facts
short_description: Retrieve facts of volume attachments in OCI
description:
    - This module retrieves information of a specified volume attachment or all the volume attachments in a specified
      compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the volume attachments in a
                     specific compartment.
        required: false
    instance_id:
        description: The OCID of the instance. Use I(instance_id) with I(compartment_id) to get volume attachment
                     information related to I(instance_id).
        required: false
    volume_attachment_id:
        description: The OCID of the volume attachment. Required to get information of a specific volume attachment.
        required: false
        aliases: [ 'id' ]
    volume_id:
        description: The OCID of the volume. Use I(volume_id) with I(compartment_id) to get volume attachment
                     information related to I(volume_id).
        required: false
    availability_domain:
        description: The name of the availability domain
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all volume attachments in a compartment
  oci_volume_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get volume attachment information for a specified compartment & instance
  oci_volume_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx

- name: Get volume attachment information for a specified compartment & block volume
  oci_volume_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

- name: Get information of a specific volume attachment
  oci_volume_attachment:
    volume_attachment_id: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
volume_attachments:
    description: List of information about volume attachments
    returned: On success
    type: complex
    contains:
        attachment_type:
            description: The type of volume attachment.
            returned: always
            type: string
            sample: iscsi
        availability_domain:
            description: The Availability Domain of an instance.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        chap_secret:
            description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
            returned: always
            type: string
            sample: d6866c0d-298b-48ba-95af-309b4faux45e
        chap_username:
            description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
            returned: always
            type: string
            sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
        compartment_id:
            description: The OCID of the compartment.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: A user-friendly name. Does not have to be unique, and it cannot be changed.
            returned: always
            type: string
            sample: My volume attachment
        id:
            description: The OCID of the volume attachment.
            returned: always
            type: string
            sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
        instance_id:
            description: The OCID of the instance the volume is attached to.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        ipv4:
            description: The volume's iSCSI IP address.
            returned: always
            type: string
            sample: 169.254.0.2
        iqn:
            description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
            returned: always
            type: string
            sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
        lifecycle_state:
            description: The current state of the volume attachment.
            returned: always
            type: string
            sample: ATTACHED
        port:
            description: The volume's iSCSI port.
            returned: always
            type: int
            sample: 3260
        time_created:
            description: The date and time the volume was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        volume_id:
            description: The OCID of the volume.
            returned: always
            type: string
            sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
        iscsi_attach_commands:
            description: Commands to attach the iSCSI block volume. Empty if attachment_type is not iscsi.
            returned: always
            type: list
            sample: [
                "sudo iscsiadm -m node -o new -T iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3 -p 169.254.2.2:3260",
                "sudo iscsiadm -m node -o update -T iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3 -n node.startup -v automatic",
                "sudo iscsiadm -m node -T iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3 -p 169.254.2.2:3260 -l"
            ]
        iscsi_detach_commands:
            description: Commands to detach the iSCSI block volume. Empty if attachment_type is not iscsi.
            returned: always
            type: list
            sample: [
                "sudo iscsiadm -m node -T iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3 -p 169.254.2.2:3260 -u",
                "sudo iscsiadm -m node -o delete -T iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3"
            ]
    sample: [{
                "attachment_type": "iscsi",
                "availability_domain": "BnQb:PHX-AD-1",
                "chap_secret": null,
                "chap_username": null,
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                "display_name": "ansible_volume_attachment",
                "id": "ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx",
                "instance_id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx",
                "ipv4": "169.254.2.2",
                "iqn": "iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3",
                "lifecycle_state": "ATTACHED",
                "port": 3260,
                "time_created": "2017-11-23T11:17:50.139000+00:00",
                "volume_id": "ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx",
                "iscsi_attach_commands": [
                    "sudo iscsiadm -m node -o new -T iqn.2015-12.com.oracleiaas:1edac499-4d1b-4451-ba52-b803d0fb7328 -p 169.254.2.2:3260",
                    "sudo iscsiadm -m node -o update -T iqn.2015-12.com.oracleiaas:1edac499-4d1b-4451-ba52-b803d0fb7328 -n node.startup -v automatic",
                    "sudo iscsiadm -m node -T iqn.2015-12.com.oracleiaas:1edac499-4d1b-4451-ba52-b803d0fb7328 -p 169.254.2.2:3260 -l"
                ],
                "iscsi_detach_commands": [
                    "sudo iscsiadm -m node -T iqn.2015-12.com.oracleiaas:1edac499-4d1b-4451-ba52-b803d0fb7328 -p 169.254.2.2:3260 -u",
                    "sudo iscsiadm -m node -o delete -T iqn.2015-12.com.oracleiaas:1edac499-4d1b-4451-ba52-b803d0fb7328"
                ],
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_compute_utils

from ansible.module_utils import six

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def add_iscsi_commands(volume_attachments):
    return [
        oci_compute_utils.with_iscsi_commands(volume_attachment)
        for volume_attachment in volume_attachments
    ]


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            instance_id=dict(type="str", required=False),
            volume_id=dict(type="str", required=False),
            volume_attachment_id=dict(type="str", required=False, aliases=["id"]),
            availability_domain=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "volume_attachment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    volume_attachment_id = module.params["volume_attachment_id"]

    try:
        if volume_attachment_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        compute_client.get_volume_attachment,
                        volume_attachment_id=volume_attachment_id,
                    ).data
                )
            ]

        else:
            key_list = [
                "compartment_id",
                "instance_id",
                "volume_id",
                "display_name",
                "availability_domain",
            ]
            param_map = dict(
                (k, v)
                for (k, v) in six.iteritems(module.params)
                if k in key_list and v is not None
            )

            result = to_dict(
                oci_utils.list_all_resources(
                    compute_client.list_volume_attachments, **param_map
                )
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(volume_attachments=add_iscsi_commands(result))


if __name__ == "__main__":
    main()
