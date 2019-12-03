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
module: oci_instance_configuration
short_description: Manage Instance Configurations in OCI
description:
    - This module allows the user to create, update and delete an Instance Configuration in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the instance configuration. Required to create an instance
                     configuration.
        required: false
    name:
        description: A user-friendly name for the instance configuration
        required: false
        aliases: ['display_name']
    instance_details:
        description: Details about the compute instance details that are part of the Instance Configuration. Required
                     to create an instance configuration.
        required: false
        suboptions:
            instance_type:
                description: The type of instance details. Supported instanceType is compute
                required: true
                choices: ['compute']
            block_volumes:
                description: A list of new block volumes to create, or attach to an existing volume.
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
                    defined_tags:
                        description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
                        required: false
                    extended_metadata:
                        description: Additional metadata key/value pairs that you provide. They serve a similar
                                     purpose and functionality from fields in the I(metadata) object. They are
                                     distinguished from I(metadata) fields in that these can be nested JSON
                                     objects (whereas 'metadata' fields are string/string maps only).
                                     If you don't need nested metadata values, it is strongly advised to avoid
                                     using this object and use the Metadata object instead.
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
                            boot_volume_size_in_gbs:
                                description: The size of the boot volume in GBs. The minimum value is 50 GB
                                             and the maximum value is 16384 GB (16TB).
                            boot_volume_id:
                                description: The OCID of the boot volume used to boot the instance. Required
                                             if I(source_type) is "bootVolume".
                                required: false
                    create_vnic_details:
                        description: Details for the primary VNIC that is automatically created and attached
                                     when the instance is launched. Required when creating a compute instance
                                     with I(state=present).
                        required: false
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
                            display_name:
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
                    nic_index:
                        description: Specifies the physical network interface card (NIC) the VNIC will use. Defaults to
                                     0. Certain bare metal instance shapes have two active physical NICs (0 and 1).
                                     When a secondary VNIC is added to one of these instances, the NIC that the VNIC
                                     will use can be specified using C(nic_index). This option may be specified while
                                     creating a VNIC and attaching to an instance using I(state=present).
                        required: false
                    create_vnic_details:
                        description: Details for creating a new secondary VNIC. This option must be specified when a
                                     secondary VNIC needs to be created and associated with an instance using
                                     I(state=present).
                        required: false
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
    instance_configuration_id:
        description: The OCID of the instance configuration. Required to update or delete an instance configuration.
        required: false
        aliases: ['id']
    state:
        description: Create or update an instance configuration with I(state=present). Use I(state=absent) to delete an
                     instance configuration.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_tags ]
"""

EXAMPLES = """
- name: Create an instance configuration that describes launch details for a compute instance of VM.Standard2.1 shape
        and a specific image. No details are provided for additional block volume attachments or secondary VNICs
  oci_instance_configuration:
    name: "backend-servers"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    instance_details:
        instance_type: "compute"
        launch_details:
            compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
            shape: "VM.Standard2.1"
            source_details:
                source_type: "image"
                image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...sa7klnoa"
            metadata:
                foo: bar

- name: Create an instance configuration that describes launch details for a compute instance of VM.Standard2.1 shape
        and a specific image, with additional block volume details (stating that a new block volume must be created and
        that it must be a clone of an existing volume, and an existing iscsi volume be attached)
  oci_instance_configuration:
    name: "backend-servers"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    instance_details:
        instance_type: "compute"
        launch_details:
            compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
            shape: "VM.Standard2.1"
            source_details:
                source_type: "image"
                image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...sa7klnoa"
        block_volumes:
            - create_details:
                source_details:
                    type: volume
                    id: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx...abcd
              attach_details:
                type: iscsi
                volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx...defg

- name: Update an instance configuration's display name
  oci_instance_configuration:
    id: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    name: "old-backend-servers"

- name: Delete an instance configuration
  oci_instance_configuration:
    id: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: absent
"""

RETURN = """
instance_configuration:
    description: Information about the Instance Configuration
    returned: On successful create, delete operations on instance configurations
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
                        defined_tags:
                            description: Defined tags for this resource. Each key is predefined and scoped to a
                                         namespace.
                            required: false
                        extended_metadata:
                            description: Additional metadata key/value pairs that you provide. They serve a similar
                                         purpose and functionality from fields in the I(metadata) object. They are
                                         distinguished from I(metadata) fields in that these can be nested JSON
                                         objects (whereas 'metadata' fields are string/string maps only).
                                         If you don't need nested metadata values, it is strongly advised to avoid
                                         using this object and use the Metadata object instead.
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
                                boot_volume_size_in_gbs:
                                    description: The size of the boot volume in GBs. The minimum value is 50 GB
                                                 and the maximum value is 16384 GB (16TB).
                                    type: int
                                boot_volume_id:
                                    description: The OCID of the boot volume used to boot the instance. Required
                                                 if I(source_type) is "bootVolume".
                                    required: false
                        create_vnic_details:
                            description: Details for the primary VNIC that is automatically created and attached
                                         when the instance is launched. Required when creating a compute instance
                                         with I(state=present).
                            required: false
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
                        nic_index:
                            description: Specifies the physical network interface card (NIC) the VNIC will use. Defaults to
                                         0. Certain bare metal instance shapes have two active physical NICs (0 and 1).
                                         When a secondary VNIC is added to one of these instances, the NIC that the VNIC
                                         will use can be specified using C(nic_index). This option may be specified while
                                         creating a VNIC and attaching to an instance using I(state=present).
                            required: false
                        create_vnic_details:
                            description: Details for creating a new secondary VNIC. This option must be specified when a
                                         secondary VNIC needs to be created and associated with an instance using
                                         I(state=present).
                            required: false
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

    sample: {
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
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_management_client import ComputeManagementClient
    from oci.core.models import (
        CreateInstanceConfigurationDetails,
        UpdateInstanceConfigurationDetails,
        ComputeInstanceDetails,
        InstanceConfigurationBlockVolumeDetails,
        InstanceConfigurationCreateVolumeDetails,
        InstanceConfigurationLaunchInstanceDetails,
        InstanceConfigurationCreateVnicDetails,
        InstanceConfigurationAttachVnicDetails,
        InstanceConfigurationInstanceSourceViaImageDetails,
        InstanceConfigurationInstanceSourceViaBootVolumeDetails,
        InstanceConfigurationIscsiAttachVolumeDetails,
        InstanceConfigurationParavirtualizedAttachVolumeDetails,
        InstanceConfigurationVolumeSourceFromVolumeBackupDetails,
        InstanceConfigurationVolumeSourceFromVolumeDetails,
    )

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "instance_configuration"


def delete_instance_configuration(compute_management_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_management_client,
        get_fn=compute_management_client.get_instance_configuration,
        kwargs_get={
            "instance_configuration_id": module.params["instance_configuration_id"]
        },
        delete_fn=compute_management_client.delete_instance_configuration,
        kwargs_delete={
            "instance_configuration_id": module.params["instance_configuration_id"]
        },
        module=module,
    )
    return result


def create_instance_configuration(compute_management_client, module):
    create_instance_configuration_details = CreateInstanceConfigurationDetails()
    _update_model_with_attrs(create_instance_configuration_details, module.params)

    instance_details = module.params["instance_details"]

    compute_instance_details = ComputeInstanceDetails()
    compute_instance_details.block_volumes = _get_block_volumes(
        instance_details.get("block_volumes"), module
    )
    compute_instance_details.launch_details = _get_launch_details(
        instance_details.get("launch_details")
    )
    compute_instance_details.secondary_vnics = _get_secondary_vnics(
        instance_details.get("secondary_vnics")
    )

    create_instance_configuration_details.instance_details = compute_instance_details

    # no need to wait as instance_configuration doesn't have a lifecycle_state
    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        create_fn=compute_management_client.create_instance_configuration,
        kwargs_create={
            "create_instance_configuration": create_instance_configuration_details
        },
        client=compute_management_client,
        get_fn=compute_management_client.get_instance_configuration,
        get_param="instance_configuration_id",
        module=module,
        wait_applicable=False,
    )
    return result


def _get_secondary_vnics(secondary_vnic_details):
    if not secondary_vnic_details:
        return None

    sec_vnics = []
    for item in secondary_vnic_details:
        sec_vnic = InstanceConfigurationAttachVnicDetails()
        _update_model_with_attrs(sec_vnic, item)

        user_create_vnic_details = item.get("create_vnic_details")
        if user_create_vnic_details:
            create_vnic_details = InstanceConfigurationCreateVnicDetails()
            _update_model_with_attrs(create_vnic_details, user_create_vnic_details)
            sec_vnic.create_vnic_details = create_vnic_details

        sec_vnics.append(sec_vnic)
    return sec_vnics


def _get_block_volumes(block_volumes_details, module):
    if not block_volumes_details:
        return None

    block_volumes = []

    for block_vol in block_volumes_details:
        if block_vol.get("volume_id") and block_vol.get("create_details"):
            module.fail_json(
                "Specify either createDetails or volumeId in block_volumes {0}".format(
                    block_vol
                )
            )

        bvd = InstanceConfigurationBlockVolumeDetails()
        _update_model_with_attrs(bvd, block_vol)

        user_attach_details = block_vol.get("attach_details")
        if user_attach_details:
            attach_type = user_attach_details["type"]
            if attach_type == "iscsi":
                attach_details = InstanceConfigurationIscsiAttachVolumeDetails()
            elif attach_type == "paravirtualized":
                attach_details = (
                    InstanceConfigurationParavirtualizedAttachVolumeDetails()
                )
            _update_model_with_attrs(attach_details, user_attach_details)
            bvd.attach_details = attach_details

        user_create_details = block_vol.get("create_details")
        if user_create_details:
            create_details = InstanceConfigurationCreateVolumeDetails()
            _update_model_with_attrs(create_details, user_create_details)
            user_create_source_details = user_create_details.get("source_details")
            if user_create_source_details:
                user_create_source_type = user_create_source_details["type"]
                if user_create_source_type == "volumeBackup":
                    create_source_details = (
                        InstanceConfigurationVolumeSourceFromVolumeBackupDetails()
                    )
                elif user_create_source_type == "volume":
                    create_source_details = (
                        InstanceConfigurationVolumeSourceFromVolumeDetails()
                    )
                _update_model_with_attrs(
                    create_source_details, user_create_source_details
                )
            create_details.source_details = create_source_details

            bvd.create_details = create_details

        block_volumes.append(bvd)

    return block_volumes


def _get_launch_details(launch_details):
    if not launch_details:
        return None

    ld = InstanceConfigurationLaunchInstanceDetails()
    _update_model_with_attrs(ld, launch_details)

    user_create_vnic_details = launch_details.get("create_vnic_details")
    create_vnic_details = InstanceConfigurationCreateVnicDetails()
    _update_model_with_attrs(create_vnic_details, user_create_vnic_details)
    ld.create_vnic_details = create_vnic_details

    user_source_details = launch_details.get("source_details")
    if user_source_details:
        sd_type = user_source_details["source_type"]

        if sd_type == "image":
            source_details = InstanceConfigurationInstanceSourceViaImageDetails()
        elif sd_type == "bootVolume":
            source_details = InstanceConfigurationInstanceSourceViaBootVolumeDetails()
        _update_model_with_attrs(source_details, user_source_details)
        ld.source_details = source_details

    return ld


def _update_model_with_attrs(model_instance, value_dict):
    for attribute in model_instance.attribute_map:
        if attribute in value_dict:
            setattr(model_instance, attribute, value_dict[attribute])


def update_instance_configuration(compute_management_client, module):
    return oci_utils.check_and_update_resource(
        resource_type=RESOURCE_NAME,
        get_fn=compute_management_client.get_instance_configuration,
        kwargs_get={
            "instance_configuration_id": module.params["instance_configuration_id"]
        },
        update_fn=compute_management_client.update_instance_configuration,
        primitive_params_update=["instance_configuration_id"],
        kwargs_non_primitive_update={
            UpdateInstanceConfigurationDetails: "update_instance_configuration_details"
        },
        module=module,
        wait_applicable=False,
        update_attributes=UpdateInstanceConfigurationDetails().attribute_map.keys(),
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_create=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            instance_details=dict(type="dict", required=False),
            instance_configuration_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("instance_configuration_id", "compartment_id")],
        required_if=[("state", "absent", ["instance_configuration_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_management_client = oci_utils.create_service_client(
        module, ComputeManagementClient
    )

    state = module.params["state"]

    if state == "absent":
        result = delete_instance_configuration(compute_management_client, module)

    else:
        instance_configuration_id = module.params["instance_configuration_id"]

        if instance_configuration_id is None:
            kwargs_list = {"compartment_id": module.params["compartment_id"]}
            # XXX Remove supports_sort_by_time_created once the backend implementation is fixed
            result = oci_utils.check_and_create_resource(
                resource_type=RESOURCE_NAME,
                create_fn=create_instance_configuration,
                kwargs_create={
                    "compute_management_client": compute_management_client,
                    "module": module,
                },
                list_fn=compute_management_client.list_instance_configurations,
                kwargs_list=kwargs_list,
                module=module,
                model=CreateInstanceConfigurationDetails(),
                exclude_attributes=None,
                supports_sort_by_time_created=False,
            )
        else:
            result = update_instance_configuration(compute_management_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
