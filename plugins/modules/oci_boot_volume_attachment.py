#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_boot_volume_attachment
short_description: Attach or detach a boot volume in OCI Block Volume service
description:
    - This module allows the user to attach a boot volume to an instance or detach a boot volume from an instance in
      OCI.
version_added: "2.5"
options:
    instance_id:
        description: The OCID of the instance. Required to attach a boot volume to an instance with I(state=present).
        required: false
    state:
        description: Use I(state=present) to attach a boot volume to an instance. Use I(state=absent) to detach a boot
                     volume from an instance.
        required: false
        default: present
        choices: ['present', 'absent']
    boot_volume_id:
        description: The OCID of the boot volume. Required to attach a boot volume to an instance with I(state=present).
        required: false
    boot_volume_attachment_id:
        description: The OCID of the boot volume attachment. Required to detach a boot volume from an instance with
                     I(state=absent).
        required: False
        aliases: [ 'id' ]
    display_name:
        description: A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering
                     confidential information.
        required: false
        aliases: [ 'name' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Attach a boot volume to an instance
  oci_boot_volume_attachment:
    instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
    boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx

- name: Detach a boot volume from an instance
  oci_boot_volume_attachment:
    boot_volume_attachment_id: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
boot_volume_attachment:
    description: Information about the boot volume attachment
    returned: On successful attach & detach operation
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the instance.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_id:
            description: The OCID of the boot volume.
            returned: always
            type: string
            sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        compartment_id:
            description: The OCID of the compartment.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: A user-friendly name. Does not have to be unique, and it cannot be changed.
            returned: always
            type: string
            sample: My boot volume attachment
        id:
            description: The OCID of the boot volume attachment.
            returned: always
            type: string
            sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
        instance_id:
            description: The OCID of the instance the boot volume is attached to.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of the boot volume attachment.
            returned: always
            type: string
            sample: ATTACHED
        time_created:
            description: The date and time the boot volume was created, in the format defined by RFC3339.
            returned: always
            type: string
    sample: {
              "availability_domain": "IwGV:US-ASHBURN-AD-1",
              "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
              "display_name": "Remote boot attachment for instance",
              "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
              "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
              "lifecycle_state": "ATTACHED",
              "time_created": "2018-01-15T07:23:10.838000+00:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import AttachBootVolumeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "boot_volume_attachment"


def attach_boot_volume(compute_client, module):
    attach_boot_volume_details = AttachBootVolumeDetails()
    for attribute in attach_boot_volume_details.attribute_map.keys():
        if attribute in module.params:
            setattr(attach_boot_volume_details, attribute, module.params[attribute])

    return oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        create_fn=compute_client.attach_boot_volume,
        kwargs_create={"attach_boot_volume_details": attach_boot_volume_details},
        get_fn=compute_client.get_boot_volume_attachment,
        get_param="boot_volume_attachment_id",
        module=module,
    )


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            instance_id=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            boot_volume_id=dict(type="str", required=False),
            boot_volume_attachment_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False, aliases=["name"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ["state", "absent", ["boot_volume_attachment_id"]],
            ["state", "present", ["instance_id", "boot_volume_id"]],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    exclude_attributes = {"display_name": True}
    state = module.params["state"]

    if state == "absent":
        result = oci_utils.delete_and_wait(
            resource_type=RESOURCE_NAME,
            client=compute_client,
            get_fn=compute_client.get_boot_volume_attachment,
            kwargs_get={
                "boot_volume_attachment_id": module.params["boot_volume_attachment_id"]
            },
            delete_fn=compute_client.detach_boot_volume,
            kwargs_delete={
                "boot_volume_attachment_id": module.params["boot_volume_attachment_id"]
            },
            module=module,
        )

    else:
        instance = compute_client.get_instance(module.params["instance_id"]).data
        result = oci_utils.check_and_create_resource(
            resource_type=RESOURCE_NAME,
            create_fn=attach_boot_volume,
            kwargs_create={"compute_client": compute_client, "module": module},
            list_fn=compute_client.list_boot_volume_attachments,
            kwargs_list={
                "availability_domain": instance.availability_domain,
                "compartment_id": instance.compartment_id,
                "instance_id": module.params["instance_id"],
                "boot_volume_id": module.params["boot_volume_id"],
            },
            exclude_attributes=exclude_attributes,
            module=module,
            model=AttachBootVolumeDetails(),
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
