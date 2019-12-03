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
module: oci_boot_volume_facts
short_description: Retrieve facts of boot volumes in OCI Block Volume service
description:
    - This module retrieves information of a specified boot volume or all the boot volumes in a specified compartment
      and availability domain.
version_added: "2.5"
options:
    availability_domain:
        description: The name of the Availability Domain. Required to get information of all the boot volumes in the
                     specified I(compartment_id) and I(availability_domain). This option is mutually exclusive with
                     I(boot_volume_id).
        required: false
    boot_volume_id:
        description: The OCID of the boot volume. Required to get information of a specific boot volume. This option is
                     mutually exclusive with I(availability_domain).
        required: false
        aliases: [ 'id' ]
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the boot volumes in the specified
                     I(compartment_id) and I(availability_domain).
        required: false
    lookup_attached_instance:
        description: Whether to fetch information of the compute instance attached to this boot volume from all the
                     compartments in the tenancy.Fetching this information requires traversing through all the
                     compartments in the  Tenancy and therefore can potentially take a long time. This option is only
                     supported in experimental mode.

                     When I(lookup_all_attached_instances=False), only an attached compute instance belonging to this
                     boot volume's compartment, is returned. This is useful when the boot volume is used within
                     a single compartment. When I(lookup_all_attached_instances=True), all the compartments in the
                     tenancy are searched to find out the compute instance that is attached to this boot volume.
                     Fetching information about compute instances attached to this boot volume is an experimental
                     feature (ie, this may or may not be supported in future releases). To use such experimental
                     features, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        required: false
        default: no
        type: bool
    volume_group_id:
        description: The OCID of the volume group.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all the boot volumes for a specific availability domain & compartment_id
  oci_boot_volume_facts:
    availability_domain: BnQb:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get information of a boot volume
  oci_boot_volume_facts:
    boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
boot_volumes:
    description: List of boot volume information
    returned: On success
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the boot volume.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-2
        compartment_id:
            description: The OCID of the compartment that contains the boot volume.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the boot volume.
            returned: always
            type: string
            sample: ansible_boot_volume
        id:
            description: The OCID of the boot volume.
            returned: always
            type: string
            sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        image_id:
            description: The image OCID used to create the boot volume.
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of a boot volume.
            returned: always
            type: string
            sample: PROVISIONING
        size_in_gbs:
            description: The size of the boot volume in GBs.
            returned: always
            type: int
            sample: 50
        size_in_mbs:
            description: The size of the boot volume in MBs.
            returned: always
            type: int
            sample: 51200
        time_created:
            description: The date and time the boot volume was created. Format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2017-11-22T19:40:08.871000+00:00
        attached_instance_information:
            description: Information of the instances the boot volume is attached to.
            returned: always
            type: list
            contains:
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
    sample: [{
                "attached_instance_information": {
                    "availability_domain": "IwGV:US-ASHBURN-AD-1",
                    "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "display_name": "Remote boot attachment for instance",
                    "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                    "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state": "ATTACHED",
                    "time_created": "2018-01-14T19:02:49.085000+00:00"
                },
                "availability_domain": "IwGV:US-ASHBURN-AD-1",
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                "display_name": "demo-20171214-100_bastion_instance (Boot Volume)",
                "id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                "image_id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx",
                "lifecycle_state": "AVAILABLE",
                "size_in_gbs": 46,
                "size_in_mbs": 47694,
                "time_created": "2018-01-14T19:02:49.042000+00:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle.oci_utils import check_mode

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


@check_mode
def add_attached_instance_info(module, boot_volumes, lookup_attached_instance):
    compute_client = oci_utils.create_service_client(module, ComputeClient)
    if boot_volumes:
        for boot_volume in boot_volumes:
            try:
                boot_volume[
                    "attached_instance_information"
                ] = oci_utils.get_attached_instances_info(
                    module,
                    lookup_attached_instance,
                    list_attachments_fn=compute_client.list_boot_volume_attachments,
                    list_attachments_args={
                        "boot_volume_id": boot_volume["id"],
                        "availability_domain": boot_volume["availability_domain"],
                        "compartment_id": boot_volume["compartment_id"],
                    },
                )
            except ServiceError as ex:
                module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            boot_volume_id=dict(type="str", required=False, aliases=["id"]),
            lookup_attached_instance=dict(type="bool", required=False, default="no"),
            volume_group_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["availability_domain", "boot_volume_id"]],
        required_one_of=[
            ["compartment_id", "boot_volume_id"],
            ["availability_domain", "boot_volume_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    boot_volume_id = module.params["boot_volume_id"]

    try:
        if boot_volume_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_boot_volume,
                        boot_volume_id=boot_volume_id,
                    ).data
                )
            ]

        else:
            availability_domain = module.params["availability_domain"]
            compartment_id = module.params["compartment_id"]
            optional_list_method_params = ["display_name", "volume_group_id"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    block_storage_client.list_boot_volumes,
                    compartment_id=compartment_id,
                    availability_domain=availability_domain,
                    **optional_kwargs
                )
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    add_attached_instance_info(
        module, result, module.params["lookup_attached_instance"]
    )

    module.exit_json(boot_volumes=result)


if __name__ == "__main__":
    main()
