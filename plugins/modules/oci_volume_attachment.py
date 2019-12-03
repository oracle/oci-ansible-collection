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
module: oci_volume_attachment
short_description: Attach or detach a volume in OCI Block Volume service
description:
    - This module allows the user to attach a volume to an instance or detach a volume from an instance in OCI.
version_added: "2.5"
options:
    instance_id:
        description: The OCID of the instance. Required to attach a volume to an instance with I(state=present).
        required: false
    is_read_only:
        description: Whether the attachment was created in read-only mode.
        required: false
        default: false
        type: bool
    state:
        description: Use I(state=present) to attach a volume to an instance. Use I(state=absent) to detach a volume from
                     an instance.
        required: false
        default: present
        choices: ['present', 'absent']
    type:
        description: The type of volume. Required to attach a volume to an instance with I(state=present).
        required: false
        choices: ['iscsi', 'paravirtualized']
    use_chap:
        description: Whether to use CHAP authentication for the volume attachment.
        required: false
        default: false
        type: bool
    volume_id:
        description: The OCID of the volume. Required to attach a volume to an instance with I(state=present).
        required: false
    volume_attachment_id:
        description: The OCID of the volume attachment. Required to detach a volume from an instance with
                     I(state=absent).
        required: False
        aliases: [ 'id' ]
    display_name:
        description: A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering
                     confidential information.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Attach a volume to an instance
  oci_volume_attachment:
    instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
    type: iscsi
    volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

- name: Detach a volume from an instance
  oci_volume_attachment:
    volume_attachment_id: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
volume_attachment:
    description: Information about the volume attachment
    returned: On successful attach operation
    type: dict
    sample: {
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
            }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_compute_utils


try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import (
        AttachIScsiVolumeDetails,
        AttachParavirtualizedVolumeDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "volume_attachment"


def get_model_class(module):
    if module.params.get("type") == "iscsi":
        return AttachIScsiVolumeDetails
    return AttachParavirtualizedVolumeDetails


def attach_volume(compute_client, module):
    model_class = get_model_class(module)
    attach_volume_details = model_class()
    for attribute in attach_volume_details.attribute_map.keys():
        if attribute in module.params:
            setattr(attach_volume_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        create_fn=compute_client.attach_volume,
        kwargs_create={"attach_volume_details": attach_volume_details},
        get_fn=compute_client.get_volume_attachment,
        get_param="volume_attachment_id",
        module=module,
    )
    return result


def add_iscsi_commands(result):
    if "volume_attachment" not in result:
        return result
    result["volume_attachment"] = oci_compute_utils.with_iscsi_commands(
        result["volume_attachment"]
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            instance_id=dict(type="str", required=False),
            is_read_only=dict(type="bool", required=False, default=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            type=dict(type="str", required=False, choices=["iscsi", "paravirtualized"]),
            use_chap=dict(type="bool", required=False, default=False),
            volume_id=dict(type="str", required=False),
            volume_attachment_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ["state", "absent", ["volume_attachment_id"]],
            ["state", "present", ["instance_id", "volume_id"]],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    state = module.params["state"]
    exclude_attributes = {"display_name": True}
    if state == "absent":
        result = oci_utils.delete_and_wait(
            resource_type=RESOURCE_NAME,
            client=compute_client,
            get_fn=compute_client.get_volume_attachment,
            kwargs_get={"volume_attachment_id": module.params["volume_attachment_id"]},
            delete_fn=compute_client.detach_volume,
            kwargs_delete={
                "volume_attachment_id": module.params["volume_attachment_id"]
            },
            module=module,
        )

    else:
        compartment_id = compute_client.get_instance(
            module.params["instance_id"]
        ).data.compartment_id
        model_class = get_model_class(module)
        result = oci_utils.check_and_create_resource(
            resource_type=RESOURCE_NAME,
            create_fn=attach_volume,
            kwargs_create={"compute_client": compute_client, "module": module},
            list_fn=compute_client.list_volume_attachments,
            kwargs_list={
                "compartment_id": compartment_id,
                "instance_id": module.params["instance_id"],
                "volume_id": module.params["volume_id"],
            },
            module=module,
            model=model_class(),
            exclude_attributes=exclude_attributes,
            default_attribute_values={"is_read_only": False, "use_chap": False},
        )

    module.exit_json(**add_iscsi_commands(result))


if __name__ == "__main__":
    main()
