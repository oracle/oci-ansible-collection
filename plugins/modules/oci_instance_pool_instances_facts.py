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
module: oci_instance_pool_instances_facts
short_description: Retrieve facts of instance pool instances of an instance pool in OCI Compute Service
description:
    - This module retrieves information of all instances in a specified instance pool.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        required: true
    instance_pool_id:
        description: The OCID of the instance pool.
        required: true
        aliases: [ 'id' ]
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get information of all instances in the specified instance_pool_id
  oci_instance_pool_instances_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd
    instance_pool_id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...efgh
"""

RETURN = """
instance_pool_instances:
    description: List of instances in a specified instance pool
    returned: On success
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain the instance is running in.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_attachment:
            description: Information of the boot volume attachment.
            returned: In experimental mode.
            type: dict
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
                    sample: 2016-08-25T21:10:29.600Z
        compartment_id:
            description: The OCID of the compartment that contains the instance.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        display_name:
            description: A user-friendly name for the instance
            returned: always
            type: string
            sample: ansible-instance-968
        extended_metadata:
            description: Additional key-value pairs associated with the instance
            returned: always
            type: dict(str, str)
            sample: {'foo': 'bar'}
        id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        image_id:
            description: The OCID of the image that the instance is based on
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        ipxe_script:
            description: A custom iPXE script that will run when the instance boots
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The current state of the instance.
            returned: always
            type: string
            sample: TERMINATED
        metadata:
            description: Custom metadata that was associated with the instance
            returned: always
            type: dict(str, str)
            sample: {"foo": "bar"}
        region:
            description: The region that contains the Availability Domain the instance is running in.
            returned: always
            type: string
            sample: phx
        shape:
            description: The shape of the instance. The shape determines the number of CPUs and the amount of memory
                         allocated to the instance.
            returned: always
            type: string
            sample: BM.Standard1.36
        time_created:
            description: The date and time the instance was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        volume_attachments:
            description: List of information about volume attachments
            returned: In experimental mode.
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

    sample: [{
      "availability_domain": "BnQb:PHX-AD-1",
      "boot_volume_attachment": {
                                  "availability_domain": "IwGV:US-ASHBURN-AD-1",
                                  "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                                  "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                                  "display_name": "Remote boot attachment for instance",
                                  "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                                  "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                                  "lifecycle_state": "ATTACHED",
                                  "time_created": "2018-01-15T07:23:10.838000+00:00"
      },
      "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq",
      "display_name": "ansible-modname-968",
      "extended_metadata": {},
      "id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx.....2siq",
      "image_id": "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....lnoa",
      "ipxe_script": null,
      "lifecycle_state": "TERMINATED",
      "metadata": {
        "baz": "quux",
        "foo": "bar"
      },
      "region": "phx",
      "shape": "BM.Standard1.36",
      "time_created": "2017-11-20T04:52:54.541000+00:00",
      "volume_attachments":  [{
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
                                "volume_id": "ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx"
      }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_management_client import ComputeManagementClient
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            instance_pool_id=dict(type="str", required=True, aliases=["id"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_management_client = oci_utils.create_service_client(
        module, ComputeManagementClient
    )
    compute_client = oci_utils.create_service_client(module, ComputeClient)

    try:
        compartment_id = module.params["compartment_id"]
        instance_pool_id = module.params["instance_pool_id"]
        instance_summaries = to_dict(
            oci_utils.list_all_resources(
                compute_management_client.list_instance_pool_instances,
                compartment_id=compartment_id,
                instance_pool_id=instance_pool_id,
            )
        )
        # Get model from summaries returned by `list_instance_pools_instances`
        result = to_dict(
            [
                oci_utils.call_with_backoff(
                    compute_client.get_instance, instance_id=inst_summ["id"]
                ).data
                for inst_summ in instance_summaries
            ]
        )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(instance_pool_instances=result)


if __name__ == "__main__":
    main()
