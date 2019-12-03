#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_instance_configuration_facts
short_description: Retrieve facts of instance configurations in OCI Compute Service
description:
    - This module retrieves information of a specified instance configuration or all the instance configurations in a specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the instance configurations in a
                     specified compartment.
        required: false
    instance_configuration_id:
        description: The OCID of the instance configuration. Required to get information of the specified instance
                     configuration.
        required: false
        aliases: [ 'id' ]
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all the instance configurations for a specific availability domain & compartment_id
  oci_instance_configuration_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd

- name: Get information of a instance configuration
  oci_instance_configuration_facts:
    instance_configuration_id: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...efgh
"""

RETURN = """
instance_configurations:
    description: List of instance configuration information
    returned: On success
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the instance configuration.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name for the instance configuration
            returned: always
            type: string
            sample: "backend-servers"
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The OCID of the instance configuration.
            returned: always
            type: string
            sample: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
        instance_details:
            description: Details of the instance
            returned: always
            type: string
            suboptions:

                instance_type:
                    description: The type of instance details. Supported instanceType is compute
                    returned: always
                    sample: compute
                block_volumes:
                    description: Create new block volumes or attach to an existing volume.
                    required: false
                    suboptions:
                        attach_details:
                            description: Volume attachment details.
                            required: false
                            suboptions:
                                display_name:
                                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                                                 Avoid entering confidential information.
                                    required: false
                                is_read_only:
                                    description: Whether the attachment was created in read-only mode.
                                    required: false
                                    default: false
                                type:
                                    description: The type of volume. Required to specify the attachment of a volume in the
                                                 instance configuration.
                                    required: false
                                    choices: ['iscsi', 'paravirtualized']
                                use_chap:
                                    description: Whether to use CHAP authentication for the volume attachment.
                                    required: false
                                    default: false
                        create_details:
                            description: Details for creating a new Block volume
                            required: false
                            suboptions:
                                availability_domain:
                                    description: The availability domain of the volume.
                                    required: false
                                backup_policy_id:
                                    description: If provided, specifies the ID of the volume backup policy to assign to the
                                                 newly created volume. If omitted, no policy will be assigned.
                                    required: false
                                compartment_id:
                                    description: The OCID of the compartment that contains the volume.
                                    required: false
                                defined_tags:
                                    description: Defined tags for this resource. Each key is predefined and scoped to a
                                                 namespace.
                                    required: false
                                display_name:
                                    description: A user-friendly name. Does not have to be unique, and it's changeable.
                                                 Avoid entering confidential information.
                                    required: false
                                freeform_tags:
                                    description: Free-form tags for this resource. Each tag is a simple key-value pair with
                                                 no predefined name, type, or namespace
                                    required: false
                                size_in_gbs:
                                    description: The size of the volume in GBs.
                                    required: false
                                source_details:
                                    description: Specifies the volume source details for a new Block volume. The volume
                                                 source is either another Block volume in the same Availability Domain or a
                                                 Block volume backup. This is an optional field. If not specified or set to
                                                 null, the new Block volume will be empty. When specified, the new Block
                                                 volume will contain data from the source volume or backup.
                                    required: false
                                    suboptions:
                                        id:
                                            description: The OCID of the volume backup from which the data should be
                                                         restored on the newly created volume when
                                                         I(source_details.type=volumeBackup) or the OCID of the volume to
                                                         be cloned when I(source_details.type=volume).
                                            required: false
                                        type:
                                            description: Type of volume source details. Use
                                                         I(source_details.type=volumeBackup) for restoring a volume backup.
                                                         Use I(source_details.type=volume) for cloning a volume.
                                            required: false
                                            choices: ['volumeBackup', 'volume']
                        volume_id:
                            description: The OCID of the volume.
                            required: false
                launch_details:
                    description: Instance launch details
                    required: false
                    suboptions:
                        availability_domain:
                            description: The Availability Domain of the instance.
                            required: false
                        compartment_id:
                            description: The OCID of the compartment. Required when I(state=present).
                            required: false
                        extended_metadata:
                            description: Additional metadata key/value pairs that you provide. They serve a similar
                                         purpose and functionality from fields in the I(metadata) object. They are
                                         distinguished from I(metadata) fields in that these can be nested JSON
                                         objects (whereas 'metadata' fields are string/string maps only).
                                         If you don't need nested metadata values, it is strongly advised to avoid
                                         using this object and use the Metadata object instead.
                            required: false
                        fault_domain:
                            description: A fault domain is a grouping of hardware and infrastructure within an
                                         availability domain. Each availability domain contains three fault domains.
                                         Fault domains let you distribute your instances
                                         so that they are not on the same physical hardware within a single
                                         availability domain. A hardware failure or Compute hardware maintenance
                                         that affects one fault domain does not affect instances in other fault
                                         domains. If you do not specify the fault domain, the system selects one
                                         for you. To change the fault domain for an instance, terminate it and
                                         launch a new instance in the preferred fault domain. To get a list of
                                         fault domains, use M(oci_fault_domain_facts).
                            required: false
                        freeform_tags:
                            description: Free-form tags for this resource. Each tag is a simple key-value pair with no
                                         predefined name, type, or namespace.
                            required: false
                        metadata:
                            description: A hash/dictionary of custom key/value pairs that are associated with the
                                         instance. This option is also used to provide information to cloud-init
                                         and specifying "ssh_authorized_keys" for the default user of the instance.
                                         This hash is specified as '{"key":"value"}' and '{"key":"value",
                                         "key":"value"}'.
                            required: false
                        display_name:
                            description: A user-friendly name. Does not have to be unique, and it's changeable.
                                         Avoid entering confidential information.
                            required: false
                            aliases: ['name']
                        ipxe_script:
                            description: custom iPXE script that will run when the instance boots.
                            required: false
                        shape:
                            description: The shape of the instance.
                            required: false
                        source_details:
                            description: Details for creating an instance. Use this parameter to specify whether a
                                         boot volume or an image should be used to launch a new instance.
                            required: true
                            suboptions:
                                source_type:
                                    description: The source type for the instance. Use image when specifying the
                                                 image OCID. Use bootVolume when specifying the boot volume OCID.
                                    required: true
                                    choices: ['image', 'bootVolume']
                                image_id:
                                    description: The OCID of the image used to boot the instance. Required if
                                                 I(source_type) is "image".
                                    required: false
                                boot_volume_id:
                                    description: The OCID of the boot volume used to boot the instance. Required
                                                 if I(source_type) is "bootVolume".
                                    required: false
                        vnic:
                            description: Details for the primary VNIC that is automatically created and attached
                                         when the instance is launched. Required when creating a compute instance
                                         with I(state=present).
                            required: false
                            aliases: ['create_vnic_details']
                            suboptions:
                                assign_public_ip:
                                    description: Determines whether the VNIC should be assigned a public IP
                                                 address. If not set and the VNIC is being created in a private
                                                 subnet (that is, where I(prohibitPublicIpOnVnic = true) in the
                                                 Subnet), then no public IP address is assigned. If not set and the
                                                 subnet is public I(prohibitPublicIpOnVnic = false), then a public
                                                 IP address is assigned. If set to true and
                                                 I(prohibitPublicIpOnVnic = true), an error is returned.
                                    required: false
                                hostname_label:
                                    description: The hostname for the VNIC's primary private IP. Used for DNS. The
                                                 value is the hostname portion of the primary private IP's fully
                                                 qualified domain name (FQDN) (for example, bminstance-1 in FQDN
                                                 bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across
                                                 all VNICs in the subnet and comply with RFC 952 and RFC 1123.
                                    required: false
                                name:
                                    description: A user-friendly name for the VNIC. Does not have to be unique.
                                    required: false
                                private_ip:
                                    description: The private IP to assign to the VNIC. Must be an available IP
                                                 address within the subnet's CIDR. If you don't specify a value,
                                                 Oracle automatically assigns a private IP address from the subnet.
                                                 This is the VNIC's primary private IP address.
                                    required: false
                                skip_source_dest_check:
                                    description: Determines whether the source/destination check is disabled on
                                                 the VNIC. Defaults to false, which means the check is performed.
                                    required: false
                                    default: false
                                subnet_id:
                                    description: The OCID of the subnet to create the VNIC in.
                                    required: true
                secondary_vnics:
                    description: Details of secondary VNICs attached with the instance
                    required: false
                    suboptions:
                        display_name:
                            description: A user-friendly name to be associated with the VNIC attachment. This does not have
                                         to be unique, and can be changed later.
                            required: false
                            aliases: ['name']
                        nic_index:
                            description: Specifies the physical network interface card (NIC) the VNIC will use. Defaults to
                                         0. Certain bare metal instance shapes have two active physical NICs (0 and 1).
                                         When a secondary VNIC is added to one of these instances, the NIC that the VNIC
                                         will use can be specified using C(nic_index). This option may be specified while
                                         creating a VNIC and attaching to an instance using I(state=present).
                            required: false
                        vnic:
                            description: Details for creating a new secondary VNIC. This option must be specified when a
                                         secondary VNIC needs to be created and associated with an instance using
                                         I(state=present).
                            required: false
                            aliases: ['create_vnic_details']
                            suboptions:
                                assign_public_ip:
                                    description: Determines whether the secondary VNIC should be assigned a public IP
                                                 address. If not set and the VNIC is being created in a private subnet
                                                 (that is, where I(prohibitPublicIpOnVnic = true) in the Subnet), then no
                                                 public IP address is assigned. If not set and the subnet is public
                                                 I(prohibitPublicIpOnVnic = false), then a public IP address is
                                                 assigned. If set to true and I(prohibitPublicIpOnVnic = true),
                                                 an error is returned.
                                    required: false
                                hostname_label:
                                    description: The hostname for the VNIC's primary private IP. Used for DNS. The value is
                                                 the hostname portion of the primary private IP's fully qualified domain
                                                 name (FQDN) (for example, bminstance-1 in FQDN
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
                                    required: false
        deferred_fields:
            description: List of deferred fields
            returned: always
            type: list
            sample: '["instanceDetails.launchDetails.availabilityDomain",
                        "instanceDetails.launchDetails.createVnicDetails.subnetId"]'
        time_created:
            description: The date and time the instance configuration was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: "2018-11-07T04:16:20.454000+00:00"

    sample: [{
                "compartment-id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...mkwq",
                "deferred-fields": [
                  "instanceDetails.launchDetails.availabilityDomain",
                  "instanceDetails.launchDetails.createVnicDetails.subnetId"
                ],
                "defined-tags": {},
                "display-name": "siva-test-conf-3",
                "freeform-tags": {},
                "id": "ocid1.instanceconfiguration.oc1.iad.xxxxxEXAMPLExxxxx...ejka",
                "instance-details": {
                  "block-volumes": null,
                  "instance-type": "compute",
                  "launch-details": {
                    "availability-domain": null,
                    "compartment-id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...mkwq",
                    "create-vnic-details": {
                      "assign-public-ip": true,
                      "display-name": "siva-test-3",
                      "hostname-label": null,
                      "private-ip": null,
                      "skip-source-dest-check": false,
                      "subnet-id": null
                    },
                    "defined-tags": null,
                    "display-name": "siva-test-3",
                    "extended-metadata": null,
                    "freeform-tags": null,
                    "ipxe-script": null,
                    "metadata": {
                      "ssh_authorized_keys": "ssh-rsa ...k8Id/ug/xxxxxEXAMPLExxxxx...RYzAEYT foo@bar",
                      "user_data": "dW5kZWZpbmVk"
                    },
                    "shape": "VM.Standard2.1",
                    "source-details": {
                      "image-id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx...ayda",
                      "source-type": "image"
                    }
                  },
                  "secondary-vnics": null
                },
                "time-created": "2018-11-07T04:16:20.454000+00:00"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_management_client import ComputeManagementClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            instance_configuration_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "instance_configuration_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_management_client = oci_utils.create_service_client(
        module, ComputeManagementClient
    )

    instance_configuration_id = module.params["instance_configuration_id"]

    try:
        if instance_configuration_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        compute_management_client.get_instance_configuration,
                        instance_configuration_id=instance_configuration_id,
                    ).data
                )
            ]

        else:
            compartment_id = module.params["compartment_id"]
            inst_conf_summaries = to_dict(
                oci_utils.list_all_resources(
                    compute_management_client.list_instance_configurations,
                    compartment_id=compartment_id,
                )
            )
            # Get model from summaries returned by `list_instance_configurations`
            result = to_dict(
                [
                    oci_utils.call_with_backoff(
                        compute_management_client.get_instance_configuration,
                        instance_configuration_id=ic["id"],
                    ).data
                    for ic in inst_conf_summaries
                ]
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(instance_configurations=result)


if __name__ == "__main__":
    main()
