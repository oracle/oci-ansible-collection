#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
version_added: "2.9.0"
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
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
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
- name: Get a specific instance_configuration
  oci_compute_management_instance_configuration_facts:
    # required
    instance_configuration_id: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List instance_configurations
  oci_compute_management_instance_configuration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
instance_configurations:
    description:
        - List of InstanceConfiguration resources
    returned: on success
    type: complex
    contains:
        instance_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                instance_type:
                    description:
                        - The type of instance details. Supported instanceType is compute
                    returned: on success
                    type: str
                    sample: compute
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
                                use_chap:
                                    description:
                                        - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
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
                                    type: str
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
                                    type: str
                                    sample: iscsi
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
                                    type: str
                                    sample: Uocm:PHX-AD-1
                                backup_policy_id:
                                    description:
                                        - If provided, specifies the ID of the volume backup policy to assign to the newly
                                          created volume. If omitted, no policy will be assigned.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx"
                                compartment_id:
                                    description:
                                        - The OCID of the compartment that contains the volume.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                kms_key_id:
                                    description:
                                        - The OCID of the Key Management key to assign as the master encryption key
                                          for the volume.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                                vpus_per_gb:
                                    description:
                                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                          representing the Block Volume service's elastic performance options.
                                          See L(Block Volume Performance
                                          Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more
                                          information.
                                        - "Allowed values:"
                                        - " * `0`: Represents Lower Cost option."
                                        - " * `10`: Represents Balanced option."
                                        - " * `20`: Represents Higher Performance option."
                                        - " * `30`-`120`: Represents the Ultra High Performance option."
                                        - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
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
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - ""
                                            returned: on success
                                            type: str
                                            sample: volume
                                        id:
                                            description:
                                                - The OCID of the volume.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                                autotune_policies:
                                    description:
                                        - The list of autotune policies enabled for this volume.
                                    returned: on success
                                    type: complex
                                    contains:
                                        autotune_type:
                                            description:
                                                - This specifies the type of autotunes supported by OCI.
                                            returned: on success
                                            type: str
                                            sample: DETACHED_VOLUME
                                        max_vpus_per_gb:
                                            description:
                                                - This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
                                                  temporarily based on performance monitoring.
                                            returned: on success
                                            type: int
                                            sample: 56
                        volume_id:
                            description:
                                - The OCID of the volume.
                            returned: on success
                            type: str
                            sample: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
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
                            type: str
                            sample: Uocm:PHX-AD-1
                        capacity_reservation_id:
                            description:
                                - The OCID of the compute capacity reservation this instance is launched under.
                            returned: on success
                            type: str
                            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                        compartment_id:
                            description:
                                - The OCID of the compartment containing the instance.
                                  Instances created from instance configurations are placed in the same compartment
                                  as the instance that was used to create the instance configuration.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        create_vnic_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                assign_public_ip:
                                    description:
                                        - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                assign_private_dns_record:
                                    description:
                                        - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                hostname_label:
                                    description:
                                        - The hostname for the VNIC's primary private IP.
                                          See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: hostname_label_example
                                nsg_ids:
                                    description:
                                        - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                          information about NSGs, see
                                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                    returned: on success
                                    type: list
                                    sample: []
                                private_ip:
                                    description:
                                        - A private IP address of your choice to assign to the VNIC.
                                          See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: private_ip_example
                                skip_source_dest_check:
                                    description:
                                        - Whether the source/destination check is disabled on the VNIC.
                                          See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                subnet_id:
                                    description:
                                        - The OCID of the subnet to create the VNIC in.
                                          See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        defined_tags:
                            description:
                                - Defined tags for this resource. Each key is predefined and scoped to a
                                  namespace. For more information, see L(Resource
                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            returned: on success
                            type: dict
                            sample: {'Operations': {'CostCenter': 'US'}}
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                  Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
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
                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
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
                                  L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                                - For more information about iPXE, see http://ipxe.org.
                            returned: on success
                            type: str
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
                                  us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
                            returned: on success
                            type: str
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
                                baseline_ocpu_utilization:
                                    description:
                                        - The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
                                          non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.
                                        - "The following values are supported:
                                          - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
                                          - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
                                          - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance."
                                    returned: on success
                                    type: str
                                    sample: BASELINE_1_8
                                nvmes:
                                    description:
                                        - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                                    returned: on success
                                    type: int
                                    sample: 56
                        platform_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_access_control_service_enabled:
                                    description:
                                        - Whether the Access Control Service is enabled on the instance. When enabled,
                                          the platform can enforce PCIe device isolation, required for VFIO device pass-through.
                                    returned: on success
                                    type: bool
                                    sample: true
                                are_virtual_instructions_enabled:
                                    description:
                                        - Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
                                          or VT-x for Intel shapes.
                                    returned: on success
                                    type: bool
                                    sample: true
                                numa_nodes_per_socket:
                                    description:
                                        - The number of NUMA nodes per socket (NPS).
                                    returned: on success
                                    type: str
                                    sample: NPS0
                                is_symmetric_multi_threading_enabled:
                                    description:
                                        - Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
                                          called simultaneous multithreading (SMT) or Intel Hyper-Threading.
                                        - Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
                                          independent threads of execution, to better use the resources and increase the efficiency
                                          of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
                                          can provide higher or more predictable performance for some workloads.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_input_output_memory_management_unit_enabled:
                                    description:
                                        - Whether the input-output memory management unit is enabled.
                                    returned: on success
                                    type: bool
                                    sample: true
                                percentage_of_cores_enabled:
                                    description:
                                        - The percentage of cores enabled. Value must be a multiple of 25%. If the requested percentage
                                          results in a fractional number of cores, the system rounds up the number of cores across processors
                                          and provisions an instance with a whole number of cores.
                                        - If the applications that you run on the instance use a core-based licensing model and need fewer cores
                                          than the full size of the shape, you can disable cores to reduce your licensing costs. The instance
                                          itself is billed for the full shape, regardless of whether all cores are enabled.
                                    returned: on success
                                    type: int
                                    sample: 56
                                type:
                                    description:
                                        - The type of platform being configured.
                                    returned: on success
                                    type: str
                                    sample: AMD_MILAN_BM
                                is_secure_boot_enabled:
                                    description:
                                        - Whether Secure Boot is enabled on the instance.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_trusted_platform_module_enabled:
                                    description:
                                        - Whether the Trusted Platform Module (TPM) is enabled on the instance.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_measured_boot_enabled:
                                    description:
                                        - Whether the Measured Boot feature is enabled on the instance.
                                    returned: on success
                                    type: bool
                                    sample: true
                        source_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                boot_volume_id:
                                    description:
                                        - The OCID of the boot volume used to boot the instance.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
                                source_type:
                                    description:
                                        - The source type for the instance.
                                          Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                                          the boot volume OCID.
                                    returned: on success
                                    type: str
                                    sample: bootVolume
                                boot_volume_size_in_gbs:
                                    description:
                                        - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
                                          value is 32,768 GB (32 TB).
                                    returned: on success
                                    type: int
                                    sample: 56
                                image_id:
                                    description:
                                        - The OCID of the image used to boot the instance.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                                boot_volume_vpus_per_gb:
                                    description:
                                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                                          representing the Block Volume service's elastic performance options.
                                          See L(Block Volume Performance
                                          Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more
                                          information.
                                        - "Allowed values:"
                                        - " * `10`: Represents Balanced option."
                                        - " * `20`: Represents Higher Performance option."
                                        - " * `30`-`120`: Represents the Ultra High Performance option."
                                        - For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.
                                    returned: on success
                                    type: int
                                    sample: 56
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
                            type: str
                            sample: FAULT-DOMAIN-1
                        dedicated_vm_host_id:
                            description:
                                - The OCID of dedicated VM host.
                                - Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
                                  cannot be used to launch instance pools.
                            returned: on success
                            type: str
                            sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                        launch_mode:
                            description:
                                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
                            returned: on success
                            type: str
                            sample: NATIVE
                        launch_options:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                boot_volume_type:
                                    description:
                                        - "Emulation type for the boot volume.
                                          * `ISCSI` - ISCSI attached block storage device.
                                          * `SCSI` - Emulated SCSI disk.
                                          * `IDE` - Emulated IDE disk.
                                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                          volumes on platform images.
                                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                          storage volumes on platform images."
                                    returned: on success
                                    type: str
                                    sample: ISCSI
                                firmware:
                                    description:
                                        - "Firmware used to boot VM. Select the option that matches your operating system.
                                          * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                                          systems that boot using MBR style bootloaders.
                                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                                          default for platform images."
                                    returned: on success
                                    type: str
                                    sample: BIOS
                                network_type:
                                    description:
                                        - "Emulation type for the physical network interface card (NIC).
                                          * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                                    returned: on success
                                    type: str
                                    sample: E1000
                                remote_data_volume_type:
                                    description:
                                        - "Emulation type for volume.
                                          * `ISCSI` - ISCSI attached block storage device.
                                          * `SCSI` - Emulated SCSI disk.
                                          * `IDE` - Emulated IDE disk.
                                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                                          volumes on platform images.
                                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                                          storage volumes on platform images."
                                    returned: on success
                                    type: str
                                    sample: ISCSI
                                is_pv_encryption_in_transit_enabled:
                                    description:
                                        - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                                          L(InstanceConfigurationLaunchInstanceDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/datatypes/InstanceConfigurationLaunchInstanceDetails).
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
                                        - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                                          monitoring plugins. Default value is false (monitoring plugins are enabled).
                                        - "These are the monitoring plugins: Compute Instance Monitoring
                                          and Custom Logs Monitoring."
                                        - The monitoring plugins are controlled by this parameter and by the per-plugin
                                          configuration in the `pluginsConfig` object.
                                        - "- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of
                                          the per-plugin configuration.
                                          - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You
                                          can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                          object."
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_management_disabled:
                                    description:
                                        - Whether Oracle Cloud Agent can run all the available management plugins.
                                          Default value is false (management plugins are enabled).
                                        - "These are the management plugins: OS Management Service Agent and Compute Instance
                                          Run Command."
                                        - The management plugins are controlled by this parameter and by the per-plugin
                                          configuration in the `pluginsConfig` object.
                                        - "- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of
                                          the per-plugin configuration.
                                          - If `isManagementDisabled` is false, all of the management plugins are enabled. You
                                          can optionally disable individual management plugins by providing a value in the `pluginsConfig`
                                          object."
                                    returned: on success
                                    type: bool
                                    sample: true
                                are_all_plugins_disabled:
                                    description:
                                        - Whether Oracle Cloud Agent can run all the available plugins.
                                          This includes the management and monitoring plugins.
                                        - To get a list of available plugins, use the
                                          L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                          operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                          L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-
                                          plugins.htm).
                                    returned: on success
                                    type: bool
                                    sample: true
                                plugins_config:
                                    description:
                                        - The configuration of plugins associated with this instance.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - The plugin name. To get a list of available plugins, use the
                                                  L(ListInstanceagentAvailablePlugins,https://docs.cloud.oracle.com/en-
                                                  us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins)
                                                  operation in the Oracle Cloud Agent API. For more information about the available plugins, see
                                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-
                                                  plugins.htm).
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        desired_state:
                                            description:
                                                - Whether the plugin should be enabled or disabled.
                                                - To enable the monitoring and management plugins, the `isMonitoringDisabled` and
                                                  `isManagementDisabled` attributes must also be set to false.
                                            returned: on success
                                            type: str
                                            sample: ENABLED
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
                            type: str
                            sample: LIVE_MIGRATE
                        instance_options:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                are_legacy_imds_endpoints_disabled:
                                    description:
                                        - Whether to disable the legacy (/v1) instance metadata service endpoints.
                                          Customers who have migrated to /v2 should set this to true for added security.
                                          Default is false.
                                    returned: on success
                                    type: bool
                                    sample: true
                        availability_config:
                            description:
                                - ""
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
                                    type: str
                                    sample: RESTORE_INSTANCE
                        preemptible_instance_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                preemption_action:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - The type of action to run when the instance is interrupted for eviction.
                                            returned: on success
                                            type: str
                                            sample: TERMINATE
                                        preserve_boot_volume:
                                            description:
                                                - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is
                                                  terminated. Defaults to false if not specified.
                                            returned: on success
                                            type: bool
                                            sample: true
                secondary_vnics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        create_vnic_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                assign_public_ip:
                                    description:
                                        - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                assign_private_dns_record:
                                    description:
                                        - Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of
                                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)
                                          for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                defined_tags:
                                    description:
                                        - Defined tags for this resource. Each key is predefined and scoped to a
                                          namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Operations': {'CostCenter': 'US'}}
                                display_name:
                                    description:
                                        - A user-friendly name. Does not have to be unique, and it's changeable.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                freeform_tags:
                                    description:
                                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                          predefined name, type, or namespace. For more information, see L(Resource
                                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {'Department': 'Finance'}
                                hostname_label:
                                    description:
                                        - The hostname for the VNIC's primary private IP.
                                          See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: hostname_label_example
                                nsg_ids:
                                    description:
                                        - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                          information about NSGs, see
                                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                    returned: on success
                                    type: list
                                    sample: []
                                private_ip:
                                    description:
                                        - A private IP address of your choice to assign to the VNIC.
                                          See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: private_ip_example
                                skip_source_dest_check:
                                    description:
                                        - Whether the source/destination check is disabled on the VNIC.
                                          See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: bool
                                    sample: true
                                subnet_id:
                                    description:
                                        - The OCID of the subnet to create the VNIC in.
                                          See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/iaas/latest/CreateVnicDetails/) for more information.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable.
                                  Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        nic_index:
                            description:
                                - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                                  Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                                  you add a secondary VNIC to one of these instances, you can specify which NIC
                                  the VNIC will use. For more information, see
                                  L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
                            returned: on success
                            type: int
                            sample: 56
        deferred_fields:
            description:
                - Parameters that were not specified when the instance configuration was created, but that
                  are required to launch an instance from the instance configuration. See the
                  L(LaunchInstanceConfiguration,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstanceConfiguration) operation.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
                  containing the instance configuration.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the instance configuration was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: [{
        "instance_details": {
            "instance_type": "compute",
            "block_volumes": [{
                "attach_details": {
                    "use_chap": true,
                    "display_name": "display_name_example",
                    "is_read_only": true,
                    "device": "device_example",
                    "is_shareable": true,
                    "type": "iscsi",
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
                        "type": "volume",
                        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                    },
                    "autotune_policies": [{
                        "autotune_type": "DETACHED_VOLUME",
                        "max_vpus_per_gb": 56
                    }]
                },
                "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "launch_details": {
                "availability_domain": "Uocm:PHX-AD-1",
                "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "assign_private_dns_record": true,
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
                "display_name": "display_name_example",
                "extended_metadata": {},
                "freeform_tags": {'Department': 'Finance'},
                "ipxe_script": "ipxe_script_example",
                "metadata": {},
                "shape": "shape_example",
                "shape_config": {
                    "ocpus": 3.4,
                    "memory_in_gbs": 3.4,
                    "baseline_ocpu_utilization": "BASELINE_1_8",
                    "nvmes": 56
                },
                "platform_config": {
                    "is_access_control_service_enabled": true,
                    "are_virtual_instructions_enabled": true,
                    "numa_nodes_per_socket": "NPS0",
                    "is_symmetric_multi_threading_enabled": true,
                    "is_input_output_memory_management_unit_enabled": true,
                    "percentage_of_cores_enabled": 56,
                    "type": "AMD_MILAN_BM",
                    "is_secure_boot_enabled": true,
                    "is_trusted_platform_module_enabled": true,
                    "is_measured_boot_enabled": true
                },
                "source_details": {
                    "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
                    "source_type": "bootVolume",
                    "boot_volume_size_in_gbs": 56,
                    "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                    "boot_volume_vpus_per_gb": 56
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
                    "is_management_disabled": true,
                    "are_all_plugins_disabled": true,
                    "plugins_config": [{
                        "name": "name_example",
                        "desired_state": "ENABLED"
                    }]
                },
                "is_pv_encryption_in_transit_enabled": true,
                "preferred_maintenance_action": "LIVE_MIGRATE",
                "instance_options": {
                    "are_legacy_imds_endpoints_disabled": true
                },
                "availability_config": {
                    "recovery_action": "RESTORE_INSTANCE"
                },
                "preemptible_instance_config": {
                    "preemption_action": {
                        "type": "TERMINATE",
                        "preserve_boot_volume": true
                    }
                }
            },
            "secondary_vnics": [{
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "assign_private_dns_record": true,
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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

    module = OCIAnsibleModule(argument_spec=module_args)

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
