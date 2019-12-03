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
module: oci_vnic_attachment_facts
short_description: Retrieve details about one or more VNIC attachments in the specified compartment
description:
    - This module retrieves details about a VNIC attachment, or all VNIC attachments in a specified Compartment in OCI
      Compute Service. A VNIC attachment resides in the same compartment as the attached instance.
version_added: "2.5"
options:
    availability_domain:
        description: The name of the Availability Domain.
        required: false
    compartment_id:
        description: The OCID of the compartment (either the tenancy or another compartment in the tenancy). Required
                     for retrieving information about all VNIC attachments in a Compartment/Tenancy, or a compute
                     instance.
        required: false
    instance_id:
        description: The OCID of the instance to which a VNIC attachment is attached to. Required
                     for retrieving information about all VNIC attachments of a compute instance.
        required: false
    vnic_attachment_id:
        description: The OCID of the VNIC attachment. Required for retrieving information about a specific VNIC
                     attachment
        required: false
        aliases: ['id']
    vnic_id:
        description: The OCID of the VNIC.
        required: false

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get details of all the VNIC attachments in a specified compartment
  oci_vnic_attachment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'

- name: Get VNIC attachments of a specific instance
  oci_vnic_attachment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
    instance_id: 'ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq'

- name: Get details of a specific VNIC attachment
  oci_vnic_attachment_facts:
    id: 'ocid1.vnic.oc1..xxxxxEXAMPLExxxxx...vm62asdaxq'
"""

RETURN = """
vnic_attachments:
    description: Information about one or more VNIC attachments
    returned: on success
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the instance
            returned: always
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description: The OCID of the compartment  the VNIC attachment is in, which is the same compartment the
                         instance is in.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
        display_name:
            description: A user-friendly name for the image. It does not have to be unique, and it's changeable.
            returned: always
            type: string
            sample: sec-vnic1-to-instance1
        id:
            description: The OCID of the VNIC attachment
            returned: always
            type: string
            sample: ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...asdadv3qca
        instance_id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...asdgrrv3qca
        lifecycle_state:
            description: The current state of the VNIC attachment
            returned: always
            type: string
            sample: ATTACHED
        nic_index:
            description: The physical network interface card (NIC) the VNIC is using in a bare metal instance.
            returned: always
            type: string
            sample: 0
        subnet_id:
            description: The OCID of the VNIC's subnet.
            returned: always
            type: string
            sample: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa
        time_created:
            description: The date and time the image was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        vlan_tag:
            description: The Oracle-assigned VLAN tag of the attached VNIC. Available after the attachment process is
                         complete.
            returned: always
            type: string
            sample: 0
        vnic_id:
            description: The OCID of the VNIC. Available after the attachment process is complete.
            returned: always
            type: string
            sample: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpasdadsaoa

    sample: [{
    "availability_domain": "BnQb:PHX-AD-1",
    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...wbvm62xq",
    "display_name": "sec_vnic_1_for_my_instance",
    "id": "ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx...b3momq",
    "instance_id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...qkwr6q",
    "lifecycle_state": "DETACHED",
    "subnet_id": "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...smpqpaoa",
    "time_created": "2017-11-26T16:24:35.487000+00:00",
    "vlan_tag": 41,
    "vnic_id": "ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...v2beqa"
   }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
            instance_id=dict(type="str", required=False),
            vnic_attachment_id=dict(type="str", required=False, aliases=["id"]),
            vnic_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("id", "compartment_id")],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    compartment_id = module.params.get("compartment_id", None)
    id = module.params["vnic_attachment_id"]

    result = dict()
    try:
        if compartment_id:
            # filter and get only key:values that have been provided by the user
            optional_list_method_params = [
                "availability_domain",
                "instance_id",
                "display_name",
                "vnic_id",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            inst = oci_utils.list_all_resources(
                compute_client.list_vnic_attachments,
                compartment_id=compartment_id,
                **optional_kwargs
            )
            result = to_dict(inst)
        else:
            inst = oci_utils.call_with_backoff(
                compute_client.get_vnic_attachment, vnic_attachment_id=id
            ).data
            result = to_dict([inst])
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))

    module.exit_json(vnic_attachments=result)


if __name__ == "__main__":
    main()
