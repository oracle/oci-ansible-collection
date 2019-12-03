#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_boot_volume_attachment_facts
short_description: Retrieve facts of boot volume attachments in OCI
description:
    - This module retrieves information of a specified boot volume attachment or all the boot volume attachments in the
      specified compartment and availability domain.
version_added: "2.5"
options:
    availability_domain:
        description: The name of the Availability Domain. Required to get information of all the boot volume attachments
                     in the specified I(compartment_id) and I(availability_domain).
        required: false
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the boot volume attachments in the
                     specified I(compartment_id) and I(availability_domain).
        required: false
    instance_id:
        description: The OCID of the instance. Use I(instance_id) with I(compartment_id) and I(availability_domain) to
                     get boot volume attachment information related to I(instance_id).
        required: false
    boot_volume_attachment_id:
        description: The OCID of the boot volume attachment. Required to get information of a specific boot volume
                     attachment.
        required: false
        aliases: [ 'id' ]
    boot_volume_id:
        description: The OCID of the boot volume. Use I(boot_volume_id) with I(compartment_id) and
                     I(availability_domain) to get boot volume attachment information related to I(boot_volume_id).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all boot volume attachments in a compartment and availability domain
  oci_boot_volume_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    availability_domain: IwGV:US-ASHBURN-AD-1

- name: Get information of a specific boot volume attachment
  oci_boot_volume_attachment:
    id: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
boot_volume_attachments:
    description: List of information about boot volume attachments
    returned: On success
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
            sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of the boot volume attachment.
            returned: always
            type: string
            sample: ATTACHED
        time_created:
            description: The date and time the boot volume was created, in the format defined by RFC3339.
            returned: always
            type: string
    sample: [{
              "availability_domain": "IwGV:US-ASHBURN-AD-1",
              "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
              "display_name": "Remote boot attachment for instance",
              "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
              "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
              "lifecycle_state": "ATTACHED",
              "time_created": "2018-01-15T07:23:10.838000+00:00"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

from ansible.module_utils import six

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            instance_id=dict(type="str", required=False),
            boot_volume_id=dict(type="str", required=False),
            boot_volume_attachment_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    boot_volume_attachment_id = module.params["boot_volume_attachment_id"]

    try:
        if boot_volume_attachment_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        compute_client.get_boot_volume_attachment,
                        boot_volume_attachment_id=boot_volume_attachment_id,
                    ).data
                )
            ]

        else:
            key_list = [
                "availability_domain",
                "compartment_id",
                "instance_id",
                "boot_volume_id",
                "display_name",
            ]
            param_map = dict(
                (k, v)
                for (k, v) in six.iteritems(module.params)
                if k in key_list and v is not None
            )

            result = to_dict(
                oci_utils.list_all_resources(
                    compute_client.list_boot_volume_attachments, **param_map
                )
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(boot_volume_attachments=result)


if __name__ == "__main__":
    main()
