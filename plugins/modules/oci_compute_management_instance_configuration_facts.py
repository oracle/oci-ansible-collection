#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_compute_management_instance_configuration_facts
short_description: Fetches details about one or multiple InstanceConfiguration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstanceConfiguration resources in Oracle Cloud Infrastructure
    - Lists the instance configurations in the specified compartment.
    - If I(instance_configuration_id) is specified, the details of a single InstanceConfiguration will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    instance_configuration_id:
        description:
            - The OCID of the instance configuration.
            - Required to get a specific instance_configuration.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple instance_configurations.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List instance_configurations
  oci_compute_management_instance_configuration_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific instance_configuration
  oci_compute_management_instance_configuration_facts:
    instance_configuration_id: ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
instance_configurations:
    description:
        - List of InstanceConfiguration resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
                  containing the instance configuration.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the instance configuration.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        instance_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                instance_type:
                    description:
                        - The type of instance details. Supported instanceType is compute
                    returned: on success
                    type: string
                    sample: instance_type_example
                block_volumes:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        attach_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
                                    returned: on success
                                    type: string
                                    sample: display_name_example
                                is_read_only:
                                    description:
                                        - Whether the attachment should be created in read-only mode.
                                    returned: on success
                                    type: bool
                                    sample: true
                                device:
                                    description:
                                        - The device name.
                                    returned: on success
                                    type: string
                                    sample: device_example
                                is_shareable:
                                    description:
                                        - Whether the attachment should be created in shareable mode. If an attachment
                                          is created in shareable mode, then other instances can attach the same volume, provided
                                          that they also create their attachments in shareable mode. Only certain volume types can
                                          be attached in shareable mode. Defaults to false if not specified.
                                    returned: on success
                                    type: bool
                                    sample: true
                                type:
                                    description:
                                        - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
                                    returned: on success
                                    type: string
                                    sample: iscsi
                                use_chap:
                                    description:
                                        - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_pv_encryption_in_transit_enabled:
                                    description:
                                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        create_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                availability_domain:
                                    description:
                                        - The availability domain of the volume.
                                        - "Example: `Uocm:PHX-AD-1`"
                                    returned: on success
                                    type: string
                                    sample: Uocm:PHX-AD-1
                                backup_policy_id:
                                    description:
                                        - If provided, specifies the ID of the volume backup policy to assign to the newly
                                          created volume. If omitted, no policy will be assigned.
                                    returned: on success
                                    type: string
                                    sample: ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx
                                compartment_id:
                                    description:
                                        - The OCID of the compartment that contains the volume.
                                    returned: on success
                                    type: string
                                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: string
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                kms_key_id:
                                    description:
                                        - The OCID of the Key Management key to assign as the master encryption key
                                          for the volume.
                                    returned: on success
                                    type: string
                                    sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
                                vpus_per_gb:
                                    description:
                                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                          representing the Block Volume service's elastic performance options.
                                          See L(Block Volume Elastic
                                          Performance,https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumeelasticperformance.htm) for more
                                          information.
                                        - "Allowed values:"
                                        - " * `0`: Represents Lower Cost option."
                                        - " * `10`: Represents Balanced option."
                                        - " * `20`: Represents Higher Performance option."
                                    returned: on success
                                    type: int
                                    sample: 56
                                size_in_gbs:
                                    description:
                                        - The size of the volume in GBs.
                                    returned: on success
                                    type: int
                                    sample: 56
                                source_details:
                                    description:
                                        - Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the
                                          same availability domain or a Block volume backup.
                                          This is an optional field. If not specified or set to null, the new Block volume will be empty.
                                          When specified, the new Block volume will contain data from the source volume or backup.
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - ""
                                            returned: on success
                                            type: string
                                            sample: volumeBackup
                                        id:
                                            description:
                                                - The OCID of the volume backup.
                                            returned: on success
                                            type: string
                                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                        volume_id:
                            description:
                                - The OCID of the volume.
                            returned: on success
                            type: string
                            sample: ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx
                launch_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        availability_domain:
                            description:
                                - The availability domain of the instance.
                                - "Example: `Uocm:PHX-AD-1`"
                            returned: on success
                            type: string
                            sample: Uocm:PHX-AD-1
                        compartment_id:
                            description:
                                - The OCID of the compartment.
                            returned: on success
                            type: string
                            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                        create_vnic_details:
                            description:
                                - Details for the primary VNIC, which is automatically created and attached when
                                  the instance is launched.
                            returned: on success
                            type: complex
                            contains:
                                assign_public_ip:
                                    description:
                                        - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name for the VNIC. Does not have to be unique.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: string
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                hostname_label:
                                    description:
                                        - The hostname for the VNIC's primary private IP.
                                          See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: string
                                    sample: hostname_label_example
                                nsg_ids:
                                    description:
                                        - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                          information about NSGs, see
                                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                                    returned: on success
                                    type: list
                                    sample: []
                                private_ip:
                                    description:
                                        - A private IP address of your choice to assign to the VNIC.
                                          See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: string
                                    sample: private_ip_example
                                skip_source_dest_check:
                                    description:
                                        - Whether the source/destination check is disabled on the VNIC.
                                          See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                subnet_id:
                                    description:
                                        - The OCID of the subnet to create the VNIC in.
                                          See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: string
                                    sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
                        defined_tags:
                            description:
                                - Defined tags for this resource. Each key is predefined and scoped to a
                                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            returned: on success
                            type: dict
                            sample: {'Operations': {'CostCenter': 'US'}}
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                  Avoid entering confidential information.
                                - "Example: `My bare metal instance`"
                            returned: on success
                            type: string
                            sample: My bare metal instance
                        extended_metadata:
                            description:
                                - Additional metadata key/value pairs that you provide. They serve the same purpose and
                                  functionality as fields in the `metadata` object.
                                - They are distinguished from `metadata` fields in that these can be nested JSON objects
                                  (whereas `metadata` fields are string/string maps only).
                                - The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
                                  32,000 bytes.
                            returned: on success
                            type: dict
                            sample: {}
                        freeform_tags:
                            description:
                                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                  predefined name, type, or namespace. For more information, see L(Resource
                                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        ipxe_script:
                            description:
                                - This is an advanced option.
                                - When a bare metal or virtual machine
                                  instance boots, the iPXE firmware that runs on the instance is
                                  configured to run an iPXE script to continue the boot process.
                                - If you want more control over the boot process, you can provide
                                  your own custom iPXE script that will run when the instance boots;
                                  however, you should be aware that the same iPXE script will run
                                  every time an instance boots; not only after the initial
                                  LaunchInstance call.
                                - "The default iPXE script connects to the instance's local boot
                                  volume over iSCSI and performs a network boot. If you use a custom iPXE
                                  script and want to network-boot from the instance's local boot volume
                                  over iSCSI the same way as the default iPXE script, you should use the
                                  following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                                  iqn.2015-02.oracle.boot."
                                - For more information about the Bring Your Own Image feature of
                                  Oracle Cloud Infrastructure, see
                                  L(Bring Your Own Image,https://docs.cloud.oracle.com/Content/Compute/References/bringyourownimage.htm).
                                - For more information about iPXE, see http://ipxe.org.
                            returned: on success
                            type: string
                            sample: ipxe_script_example
                        metadata:
                            description:
                                - Custom metadata key/value pairs that you provide, such as the SSH public key
                                  required to connect to the instance.
                                - "A metadata service runs on every launched instance. The service is an HTTP
                                  endpoint listening on 169.254.169.254. You can use the service to:"
                                - "* Provide information to L(Cloud-Init,https://cloudinit.readthedocs.org/en/latest/)
                                    to be used for various system initialization tasks."
                                - "* Get information about the instance, including the custom metadata that you
                                    provide when you launch the instance."
                                - "**Providing Cloud-Init Metadata**"
                                - "You can use the following metadata key names to provide information to
                                   Cloud-Init:"
                                - "**\\"ssh_authorized_keys\\"** - Provide one or more public SSH keys to be
                                   included in the `~/.ssh/authorized_keys` file for the default user on the
                                   instance. Use a newline character to separate multiple keys. The SSH
                                   keys must be in the format necessary for the `authorized_keys` file, as shown
                                   in the example below."
                                - "**\\"user_data\\"** - Provide your own base64-encoded data to be used by
                                   Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
                                   information about how to take advantage of user data, see the
                                   L(Cloud-Init Documentation,http://cloudinit.readthedocs.org/en/latest/topics/format.html)."
                                - "**Metadata Example**"
                                - "     \\"metadata\\" : {
                                           \\"quake_bot_level\\" : \\"Severe\\",
                                           \\"ssh_authorized_keys\\" : \\"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\\",
                                           \\"user_data\\" : \\"<your_public_SSH_key>==\\"
                                        }
                                   **Getting Metadata on the Instance**"
                                - "To get information about your instance, connect to the instance using SSH and issue any of the
                                   following GET requests:"
                                - "    curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/
                                       curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/
                                       curl -H \\"Authorization: Bearer Oracle\\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>"
                                -  You'll get back a response that includes all the instance information; only the metadata information; or
                                   the metadata information for the specified key name, respectively.
                                -  The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.
                            returned: on success
                            type: dict
                            sample: {}
                        shape:
                            description:
                                - The shape of an instance. The shape determines the number of CPUs, amount of memory,
                                  and other resources allocated to the instance.
                                - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/iaas/20160918/Shape/ListShapes).
                            returned: on success
                            type: string
                            sample: shape_example
                        shape_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpus:
                                    description:
                                        - The total number of OCPUs available to the instance.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                memory_in_gbs:
                                    description:
                                        - The total amount of memory available to the instance, in gigabytes.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                        source_details:
                            description:
                                - Details for creating an instance.
                                  Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.
                            returned: on success
                            type: complex
                            contains:
                                source_type:
                                    description:
                                        - The source type for the instance.
                                          Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                                          the boot volume OCID.
                                    returned: on success
                                    type: string
                                    sample: source_type_example
                                boot_volume_size_in_gbs:
                                    description:
                                        - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 16384 GB (16TB).
                                    returned: on success
                                    type: int
                                    sample: 56
                                image_id:
                                    description:
                                        - The OCID of the image used to boot the instance.
                                    returned: on success
                                    type: string
                                    sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
                                boot_volume_id:
                                    description:
                                        - The OCID of the boot volume used to boot the instance.
                                    returned: on success
                                    type: string
                                    sample: ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx
                        fault_domain:
                            description:
                                - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                                  Each availability domain contains three fault domains. Fault domains let you distribute your
                                  instances so that they are not on the same physical hardware within a single availability domain.
                                  A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                                  instances in other fault domains.
                                - If you do not specify the fault domain, the system selects one for you.
                                - To get a list of fault domains, use the
                                  L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation
                                  in the
                                  Identity and Access Management Service API.
                                - "Example: `FAULT-DOMAIN-1`"
                            returned: on success
                            type: string
                            sample: FAULT-DOMAIN-1
                        dedicated_vm_host_id:
                            description:
                                - The OCID of dedicated VM host.
                                - Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
                                  cannot be used to launch instance pools.
                            returned: on success
                            type: string
                            sample: ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx
                        launch_mode:
                            description:
                                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
                                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
                            returned: on success
                            type: string
                            sample: NATIVE
                        launch_options:
                            description:
                                - Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.
                            returned: on success
                            type: complex
                            contains:
                                boot_volume_type:
                                    description:
                                        - "Emulation type for the boot volume.
                                          * `ISCSI` - ISCSI attached block storage device.
                                          * `SCSI` - Emulated SCSI disk.
                                          * `IDE` - Emulated IDE disk.
                                          * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data
                                          volumes on Oracle provided images.
                                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                          storage volumes on Oracle-provided images."
                                    returned: on success
                                    type: string
                                    sample: ISCSI
                                firmware:
                                    description:
                                        - "Firmware used to boot VM.  Select the option that matches your operating system.
                                          * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating
                                          systems that boot using MBR style bootloaders.
                                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the
                                          default for Oracle-provided images."
                                    returned: on success
                                    type: string
                                    sample: BIOS
                                network_type:
                                    description:
                                        - "Emulation type for the physical network interface card (NIC).
                                          * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.
                                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                                    returned: on success
                                    type: string
                                    sample: E1000
                                remote_data_volume_type:
                                    description:
                                        - "Emulation type for volume.
                                          * `ISCSI` - ISCSI attached block storage device.
                                          * `SCSI` - Emulated SCSI disk.
                                          * `IDE` - Emulated IDE disk.
                                          * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data
                                          volumes on Oracle provided images.
                                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                          storage volumes on Oracle-provided images."
                                    returned: on success
                                    type: string
                                    sample: ISCSI
                                is_pv_encryption_in_transit_enabled:
                                    description:
                                        - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                                          L(InstanceConfigurationLaunchInstanceDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/datatypes/InstanceConfigurationLaunchInstanceDetails).
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_consistent_volume_naming_enabled:
                                    description:
                                        - Whether to enable consistent volume naming feature. Defaults to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        agent_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_monitoring_disabled:
                                    description:
                                        - Whether the agent running on the instance can gather performance metrics and monitor the instance.
                                          Default value is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_management_disabled:
                                    description:
                                        - Whether the agent running on the instance can run all the available management plugins.
                                          Default value is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        is_pv_encryption_in_transit_enabled:
                            description:
                                - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
                            returned: on success
                            type: bool
                            sample: true
                        preferred_maintenance_action:
                            description:
                                - "The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
                                  * `LIVE_MIGRATE` - Run maintenance using a live migration.
                                  * `REBOOT` - Run maintenance using a reboot."
                            returned: on success
                            type: string
                            sample: LIVE_MIGRATE
                        availability_config:
                            description:
                                - Options for defining the availabiity of a VM instance after a maintenance event that impacts the underlying hardware.
                            returned: on success
                            type: complex
                            contains:
                                recovery_action:
                                    description:
                                        - "The lifecycle state for an instance when it is recovered after infrastructure maintenance.
                                          * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event.
                                          If the instance was running, it is automatically rebooted. This is the default action when a value is not set.
                                          * `STOP_INSTANCE` - The instance is recovered in the stopped state."
                                    returned: on success
                                    type: string
                                    sample: RESTORE_INSTANCE
                secondary_vnics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        create_vnic_details:
                            description:
                                - Details for creating a new VNIC.
                            returned: on success
                            type: complex
                            contains:
                                assign_public_ip:
                                    description:
                                        - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name for the VNIC. Does not have to be unique.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: string
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                hostname_label:
                                    description:
                                        - The hostname for the VNIC's primary private IP.
                                          See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: string
                                    sample: hostname_label_example
                                nsg_ids:
                                    description:
                                        - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                          information about NSGs, see
                                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                                    returned: on success
                                    type: list
                                    sample: []
                                private_ip:
                                    description:
                                        - A private IP address of your choice to assign to the VNIC.
                                          See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: string
                                    sample: private_ip_example
                                skip_source_dest_check:
                                    description:
                                        - Whether the source/destination check is disabled on the VNIC.
                                          See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                subnet_id:
                                    description:
                                        - The OCID of the subnet to create the VNIC in.
                                          See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: string
                                    sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
                        display_name:
                            description:
                                - A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
                            returned: on success
                            type: string
                            sample: display_name_example
                        nic_index:
                            description:
                                - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                                  Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                                  you add a secondary VNIC to one of these instances, you can specify which NIC
                                  the VNIC will use. For more information, see
                                  L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/Content/Network/Tasks/managingVNICs.htm).
                            returned: on success
                            type: int
                            sample: 56
        deferred_fields:
            description:
                - Parameters that were not specified when the instance configuration was created, but that
                  are required to launch an instance from the instance configuration. See the
                  L(LaunchInstanceConfiguration,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Instance/LaunchInstanceConfiguration) operation.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the instance configuration was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_details": {
            "instance_type": "instance_type_example",
            "block_volumes": [{
                "attach_details": {
                    "display_name": "display_name_example",
                    "is_read_only": true,
                    "device": "device_example",
                    "is_shareable": true,
                    "type": "iscsi",
                    "use_chap": true,
                    "is_pv_encryption_in_transit_enabled": true
                },
                "create_details": {
                    "availability_domain": "Uocm:PHX-AD-1",
                    "backup_policy_id": "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx",
                    "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
                    "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                    "vpus_per_gb": 56,
                    "size_in_gbs": 56,
                    "source_details": {
                        "type": "volumeBackup",
                        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                    }
                },
                "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "launch_details": {
                "availability_domain": "Uocm:PHX-AD-1",
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
                    "hostname_label": "hostname_label_example",
                    "nsg_ids": [],
                    "private_ip": "private_ip_example",
                    "skip_source_dest_check": true,
                    "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                },
                "defined_tags": {'Operations': {'CostCenter': 'US'}},
                "display_name": "My bare metal instance",
                "extended_metadata": {},
                "freeform_tags": {'Department': 'Finance'},
                "ipxe_script": "ipxe_script_example",
                "metadata": {},
                "shape": "shape_example",
                "shape_config": {
                    "ocpus": 3.4,
                    "memory_in_gbs": 3.4
                },
                "source_details": {
                    "source_type": "source_type_example",
                    "boot_volume_size_in_gbs": 56,
                    "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                    "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
                },
                "fault_domain": "FAULT-DOMAIN-1",
                "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
                "launch_mode": "NATIVE",
                "launch_options": {
                    "boot_volume_type": "ISCSI",
                    "firmware": "BIOS",
                    "network_type": "E1000",
                    "remote_data_volume_type": "ISCSI",
                    "is_pv_encryption_in_transit_enabled": true,
                    "is_consistent_volume_naming_enabled": true
                },
                "agent_config": {
                    "is_monitoring_disabled": true,
                    "is_management_disabled": true
                },
                "is_pv_encryption_in_transit_enabled": true,
                "preferred_maintenance_action": "LIVE_MIGRATE",
                "availability_config": {
                    "recovery_action": "RESTORE_INSTANCE"
                }
            },
            "secondary_vnics": [{
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
                    "hostname_label": "hostname_label_example",
                    "nsg_ids": [],
                    "private_ip": "private_ip_example",
                    "skip_source_dest_check": true,
                    "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                },
                "display_name": "display_name_example",
                "nic_index": 56
            }]
        },
        "deferred_fields": [],
        "time_created": "2016-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "instance_configuration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_configuration,
            instance_configuration_id=self.module.params.get(
                "instance_configuration_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_instance_configurations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


InstanceConfigurationFactsHelperCustom = get_custom_class(
    "InstanceConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceConfigurationFactsHelperCustom, InstanceConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_configuration",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_configurations=result)


if __name__ == "__main__":
    main()
