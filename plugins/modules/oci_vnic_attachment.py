#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
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
module: oci_vnic_attachment
short_description: Create a secondary VNIC and attach it to a compute instance, detach or delete VNIC attachments from
                   a compute instance.
description:
    - This module allows the user to create a secondary VNIC and attach it to a compute instance, detach a secondary
      VNIC attachment from a compute instance, and delete the secondary VNIC.
version_added: "2.5"
options:
    instance_id:
        description: The OCID of the instance to which the secondary VNIC must be attached. Required when a secondary
                     VNIC needs to be created and attached to an instance with I(state=present).
        required: false
    display_name:
        description: A user-friendly name to be associated with the VNIC attachment. This does not have to be unique,
                     and can be changed later.
        required: false
        aliases: ['name']
    nic_index:
        description: Specifies the physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare
                     metal instance shapes have two active physical NICs (0 and 1). When a secondary VNIC is added to
                     one of these instances, the NIC that the VNIC will use can be specified using C(nic_index). This
                     option may be specified while creating a VNIC and attaching to an instance using I(state=present).
        required: false
    vnic:
        description: Details for creating a new secondary VNIC. This option must be specified when a secondary VNIC
                     needs to be created and associated with an instance using I(state=present).
        required: false
        aliases: ['create_vnic_details']
        suboptions:
            assign_public_ip:
                description: Determines whether the secondary VNIC should be assigned a public IP address.  If
                             not set and the VNIC is being created in a private subnet (that is,
                             where I(prohibitPublicIpOnVnic = true) in the Subnet), then no public
                             IP address is assigned. If not set and the subnet is public
                             I(prohibitPublicIpOnVnic = false), then a public IP address is
                             assigned. If set to true and I(prohibitPublicIpOnVnic = true),
                             an error is returned.
                required: false
            defined_tags:
                description: Defined tags for this resource. Each key is predefined and scoped to a namespace. For more
                             information, see
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm).
                required: false
            freeform_tags:
                description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                             type, or namespace. For more information, see
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm).
                required: false
            hostname_label:
                description: The hostname for the VNIC's primary private IP. Used for DNS. The value
                             is the hostname portion of the primary private IP's fully qualified
                             domain name (FQDN) (for example, bminstance-1 in FQDN
                             bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all
                             VNICs in the subnet and comply with RFC 952 and RFC 1123.
                required: false
            display_name:
                description: A user-friendly name for the VNIC. Does not have to be unique.
                required: false
            private_ip:
                description: The private IP to assign to the VNIC. Must be an available IP address
                             within the subnet's CIDR. If you don't specify a value, Oracle
                             automatically assigns a private IP address from the subnet. This is
                             the VNIC's primary private IP address.
                required: false
            skip_source_dest_check:
                description: Determines whether the source/destination check is disabled on the VNIC.
                             Defaults to false, which means the check is performed.
                required: false
                default: false
            subnet_id:
                description: The OCID of the subnet to create the VNIC in.
                required: true
    vnic_attachment_id:
        description: The OCID of the VNIC attachment. Required when a secondary VNIC needs to be detached from a compute
                     instance and deleted using I(state=absent).
        required: false
        aliases: ['id']
    state:
        description: The state of the VNIC attachment that must be asserted to. When I(state=present), and the
                     VNIC attachment doesn't exist, the secondary VNIC is created with the specified details, and is
                     attached to the specified compute instance. When I(state=absent), the secondary VNIC is detached
                     from the compute instance and deleted.
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create a new secondary VNIC and attach it to the specified compute instance
  oci_vnic_attachment:
    name: sec-vnic1-to-instance1
    instance_id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....dszaitd3da"
    nicindex: 1
    vnic:
        hostname_label: "myinstance1_1"
        private_ip: "10.0.0.6"
        subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

- name: Detach a secondary VNIC from an instance and delete the VNIC
  oci_vnic_attachment:
        id: "ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...lxasdsadgdq"
        state: "absent"
"""

RETURN = """
vnic_attachment:
    description: Details of the VNIC attachment
    returned: On success
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the instance.
            returned: always
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description: The OCID of the compartment the VNIC attachment is in, which is the same compartment the
                         instance is in.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...m62xq
        display_name:
            description: A user-friendly name. Does not have to be unique.
            returned: always
            type: string
            sample: sec_vnic1_for_my_instance
        id:
            description: The OCID of the VNIC attachment.
            returned: always
            type: string
            sample: ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx...3momq
        instance_id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...qkwr6q
        lifecycle_state:
            description: The current state of the VNIC attachment.
            returned: always
            type: string
            sample: DETACHED
        subnet_id:
            description: The OCID of the VNIC's subnet.
            returned: always
            type: string
            sample: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...mpqpaoa
        time_created:
            description: The date and time the VNIC attachment was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-26T16:24:35.487000+00:00
        vlan_tag:
            description: The Oracle-assigned VLAN tag of the attached VNIC. Available after the attachment process
                         is complete.
            returned: always
            type: string
            sample: 41
        vnic_id:
            description: The OCID of the VNIC. Available after the attachment process is complete.
            returned: always
            type: string
            sample: ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...mv2beqa
    sample:  {"availability_domain": "BnQb:PHX-AD-1",
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...m62xq",
              "display_name": "sec_vnic_1_for_my_instance",
              "id": "ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx...3momq",
              "instance_id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...qkwr6q",
              "lifecycle_state": "DETACHED",
              "subnet_id": "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...mpqpaoa",
              "time_created": "2017-11-26T16:24:35.487000+00:00",
              "vlan_tag": 41,
              "vnic_id": "ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...mv2beqa"
              }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import CreateVnicDetails
    from oci.core.models import AttachVnicDetails
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "vnic_attachment"


def get_vnic_details(module):
    vnic_details = module.params.get("vnic", None)
    if not vnic_details:
        # Primary VNIC details(especially subnet_id is required)
        module.fail_json(
            msg="state is present and instance_id is not specified, but the following are missing: "
            "create_vnic_details"
        )

    cvd = CreateVnicDetails()
    cvd.display_name = vnic_details.get("display_name", None)
    cvd.assign_public_ip = vnic_details.get("assign_public_ip", None)
    cvd.hostname_label = vnic_details.get("hostname_label", None)
    cvd.private_ip = vnic_details.get("private_ip", None)
    cvd.skip_source_dest_check = vnic_details.get("skip_source_dest_check", None)
    cvd.subnet_id = vnic_details["subnet_id"]
    cvd.defined_tags = vnic_details.get("defined_tags", None)
    cvd.freeform_tags = vnic_details.get("freeform_tags", None)
    return cvd


def attach_vnic(compute_client, module):
    avd = AttachVnicDetails()
    avd.display_name = module.params.get("display_name", None)
    avd.instance_id = module.params.get("instance_id")
    avd.create_vnic_details = get_vnic_details(module)
    avd.nic_index = module.params.get("nic_index", None)

    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        create_fn=compute_client.attach_vnic,
        kwargs_create={"attach_vnic_details": avd},
        get_fn=compute_client.get_vnic_attachment,
        get_param="vnic_attachment_id",
        module=module,
    )
    return result


def debug(s):
    get_logger().debug(s)


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def main():
    my_logger = oci_utils.get_logger("oci_instance")
    set_logger(my_logger)

    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            display_name=dict(type="str", required=False, aliases=["name"]),
            instance_id=dict(type="str", required=False),
            vnic_attachment_id=dict(type="str", required=False, aliases=["id"]),
            nic_index=dict(type="int", required=False, default=0),
            create_vnic_details=dict(type="dict", required=False, aliases=["vnic"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("id", "create_vnic_details")],
        required_if=[("state", "absent", ["vnic_attachment_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    state = module.params["state"]

    result = dict(changed=False)

    vna_id = module.params["vnic_attachment_id"]
    debug("VNIC attachment Id provided by user is " + str(vna_id))

    try:
        if vna_id is not None:
            vna = oci_utils.get_existing_resource(
                compute_client.get_vnic_attachment, module, vnic_attachment_id=vna_id
            )

            if state == "absent":
                if vna is not None:
                    debug("Deleting " + vna.id)
                    result = oci_utils.delete_and_wait(
                        resource_type=RESOURCE_NAME,
                        client=compute_client,
                        get_fn=compute_client.get_vnic_attachment,
                        kwargs_get={"vnic_attachment_id": vna_id},
                        delete_fn=compute_client.detach_vnic,
                        kwargs_delete={"vnic_attachment_id": vna_id},
                        module=module,
                        wait_applicable=True,
                    )
                else:
                    debug(
                        "VNIC attachment "
                        + vna_id
                        + " already detached. So returning changed=False."
                    )
            else:
                module.fail_json("To delete a VNIC attachment, set state=absent")
        else:
            # Create a secondary VNIC and attach it to an instance
            instance_id = module.params.get("instance_id")
            exclude_attributes = {"display_name": True}
            default_attribute_values = {"nic_index": 0}
            compartment_id = compute_client.get_instance(
                instance_id=instance_id
            ).data.compartment_id
            result = oci_utils.check_and_create_resource(
                resource_type=RESOURCE_NAME,
                create_fn=attach_vnic,
                kwargs_create={"compute_client": compute_client, "module": module},
                list_fn=compute_client.list_vnic_attachments,
                kwargs_list={
                    "compartment_id": compartment_id,
                    "instance_id": instance_id,
                },
                module=module,
                model=AttachVnicDetails(),
                exclude_attributes=exclude_attributes,
                default_attribute_values=default_attribute_values,
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
