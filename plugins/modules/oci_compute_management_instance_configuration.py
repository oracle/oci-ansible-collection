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
module: oci_compute_management_instance_configuration
short_description: Manage an InstanceConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an InstanceConfiguration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an instance configuration. An instance configuration is a template that defines the
      settings to use when creating Compute instances.
    - "This resource has the following action operations in the M(oci_instance_configuration_actions) module: launch."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              containing the instance configuration.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name for the instance configuration.  Does not have to be unique,
              and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    source:
        description:
            - The source of the instance configuration. An instance configuration defines the
              settings to use when creating Compute instances, including details
              such as the base image, shape, and metadata. You can also specify the associated resources for the
              instance, such as block volume attachments and network configuration.
            - "The following values are supported:"
            - "* `NONE`: Creates an instance configuration using the list of settings that you specify."
            - "* `INSTANCE`: Creates an instance configuration using an existing instance as a template. The
              instance configuration uses the same settings as the instance."
        type: str
        choices:
            - "NONE"
            - "INSTANCE"
        default: "NONE"
    instance_details:
        description:
            - ""
            - Required when source is 'NONE'
        type: dict
        suboptions:
            instance_type:
                description:
                    - The type of instance details. Supported instanceType is compute
                type: str
                choices:
                    - "compute"
                required: true
            block_volumes:
                description:
                    - ""
                type: list
                suboptions:
                    attach_details:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            display_name:
                                description:
                                    - A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
                                type: str
                                aliases: ["name"]
                            is_read_only:
                                description:
                                    - Whether the attachment should be created in read-only mode.
                                type: bool
                            type:
                                description:
                                    - "The type of volume. The only supported values are \\"iscsi\\" and \\"paravirtualized\\"."
                                type: str
                                choices:
                                    - "iscsi"
                                    - "paravirtualized"
                                required: true
                            use_chap:
                                description:
                                    - Whether to use CHAP authentication for the volume attachment. Defaults to false.
                                    - Applicable when type is 'iscsi'
                                type: bool
                    create_details:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            availability_domain:
                                description:
                                    - The availability domain of the volume.
                                    - "Example: `Uocm:PHX-AD-1`"
                                type: str
                            backup_policy_id:
                                description:
                                    - If provided, specifies the ID of the volume backup policy to assign to the newly
                                      created volume. If omitted, no policy will be assigned.
                                type: str
                            compartment_id:
                                description:
                                    - The OCID of the compartment that contains the volume.
                                type: str
                            defined_tags:
                                description:
                                    - Defined tags for this resource. Each key is predefined and scoped to a
                                      namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                                type: dict
                            display_name:
                                description:
                                    - A user-friendly name. Does not have to be unique, and it's changeable.
                                      Avoid entering confidential information.
                                type: str
                                aliases: ["name"]
                            freeform_tags:
                                description:
                                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                                      predefined name, type, or namespace. For more information, see L(Resource
                                      Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                                type: dict
                            size_in_gbs:
                                description:
                                    - The size of the volume in GBs.
                                type: int
                            source_details:
                                description:
                                    - Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same
                                      availability domain or a Block volume backup.
                                      This is an optional field. If not specified or set to null, the new Block volume will be empty.
                                      When specified, the new Block volume will contain data from the source volume or backup.
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - ""
                                        type: str
                                        choices:
                                            - "volumeBackup"
                                            - "volume"
                                        required: true
                                    id:
                                        description:
                                            - The OCID of the volume backup.
                                        type: str
                    volume_id:
                        description:
                            - The OCID of the volume.
                        type: str
            launch_details:
                description:
                    - ""
                type: dict
                suboptions:
                    availability_domain:
                        description:
                            - The availability domain of the instance.
                            - "Example: `Uocm:PHX-AD-1`"
                        type: str
                    compartment_id:
                        description:
                            - The OCID of the compartment.
                        type: str
                    create_vnic_details:
                        description:
                            - Details for the primary VNIC, which is automatically created and attached when
                              the instance is launched.
                        type: dict
                        suboptions:
                            assign_public_ip:
                                description:
                                    - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                      L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)
                                      for more information.
                                type: bool
                            display_name:
                                description:
                                    - A user-friendly name for the VNIC. Does not have to be unique.
                                      Avoid entering confidential information.
                                type: str
                                aliases: ["name"]
                            hostname_label:
                                description:
                                    - The hostname for the VNIC's primary private IP.
                                      See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: str
                            nsg_ids:
                                description:
                                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                      information about NSGs, see
                                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                                type: list
                            private_ip:
                                description:
                                    - A private IP address of your choice to assign to the VNIC.
                                      See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: str
                            skip_source_dest_check:
                                description:
                                    - Whether the source/destination check is disabled on the VNIC.
                                      See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: bool
                            subnet_id:
                                description:
                                    - The OCID of the subnet to create the VNIC in.
                                      See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: str
                    defined_tags:
                        description:
                            - Defined tags for this resource. Each key is predefined and scoped to a
                              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                        type: dict
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable.
                              Avoid entering confidential information.
                            - "Example: `My bare metal instance`"
                        type: str
                        aliases: ["name"]
                    extended_metadata:
                        description:
                            - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata'
                              object.
                            - They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are
                              string/string maps only).
                        type: dict
                    freeform_tags:
                        description:
                            - Free-form tags for this resource. Each tag is a simple key-value pair with no
                              predefined name, type, or namespace. For more information, see L(Resource
                              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Department\\": \\"Finance\\"}`"
                        type: dict
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
                        type: str
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
                            - "**Note:** Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`
                               path. When the instance launches and either of these keys are provided, the key values are formatted as
                               OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:"
                            - "`http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob
                               contains, among other things, the SSH keys that you provided for
                                **\\"ssh_authorized_keys\\"**."
                            - "`http://169.254.169.254/openstack/latest/user_data` - Contains the
                               base64-decoded data that you provided for **\\"user_data\\"**."
                            - "**Metadata Example**"
                            - "     \\"metadata\\" : {
                                       \\"quake_bot_level\\" : \\"Severe\\",
                                       \\"ssh_authorized_keys\\" : \\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZe
                                       v7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4L
                                       BBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9Zj
                                       RmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                                       ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt
                                       +zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5
                                       FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFr
                                       wiT/oPEhhEK1S5Q== rsa-key-20160227\\",
                                       \\"user_data\\" : \\"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\\"
                                    }
                               **Getting Metadata on the Instance**"
                            - "To get information about your instance, connect to the instance using SSH and issue any of the
                               following GET requests:"
                            -      curl http://169.254.169.254/opc/v1/instance/
                                   curl http://169.254.169.254/opc/v1/instance/metadata/
                                   curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>
                            -  You'll get back a response that includes all the instance information; only the metadata information; or
                               the metadata information for the specified key name, respectively.
                        type: dict
                    shape:
                        description:
                            - The shape of an instance. The shape determines the number of CPUs, amount of memory,
                              and other resources allocated to the instance.
                            - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/iaas/20160918/Shape/ListShapes).
                        type: str
                    source_details:
                        description:
                            - Details for creating an instance.
                              Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.
                        type: dict
                        suboptions:
                            source_type:
                                description:
                                    - The source type for the instance.
                                      Use `image` when specifying the image OCID. Use `bootVolume` when specifying
                                      the boot volume OCID.
                                type: str
                                choices:
                                    - "image"
                                    - "bootVolume"
                                required: true
                            boot_volume_size_in_gbs:
                                description:
                                    - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 16384 GB (16TB).
                                    - Applicable when source_type is 'image'
                                type: int
                            image_id:
                                description:
                                    - The OCID of the image used to boot the instance.
                                    - Applicable when source_type is 'image'
                                type: str
                            boot_volume_id:
                                description:
                                    - The OCID of the boot volume used to boot the instance.
                                    - Applicable when source_type is 'bootVolume'
                                type: str
            secondary_vnics:
                description:
                    - ""
                type: list
                suboptions:
                    create_vnic_details:
                        description:
                            - Details for creating a new VNIC.
                        type: dict
                        suboptions:
                            assign_public_ip:
                                description:
                                    - Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of
                                      L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)
                                      for more information.
                                type: bool
                            display_name:
                                description:
                                    - A user-friendly name for the VNIC. Does not have to be unique.
                                      Avoid entering confidential information.
                                type: str
                                aliases: ["name"]
                            hostname_label:
                                description:
                                    - The hostname for the VNIC's primary private IP.
                                      See the `hostnameLabel` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: str
                            nsg_ids:
                                description:
                                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                                      information about NSGs, see
                                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                                type: list
                            private_ip:
                                description:
                                    - A private IP address of your choice to assign to the VNIC.
                                      See the `privateIp` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: str
                            skip_source_dest_check:
                                description:
                                    - Whether the source/destination check is disabled on the VNIC.
                                      See the `skipSourceDestCheck` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: bool
                            subnet_id:
                                description:
                                    - The OCID of the subnet to create the VNIC in.
                                      See the `subnetId` attribute of L(CreateVnicDetails,https://docs.cloud.oracle.com/en-
                                      us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
                                type: str
                    display_name:
                        description:
                            - A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
                        type: str
                        aliases: ["name"]
                    nic_index:
                        description:
                            - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
                              Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                              you add a secondary VNIC to one of these instances, you can specify which NIC
                              the VNIC will use. For more information, see
                              L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/Content/Network/Tasks/managingVNICs.htm).
                        type: int
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance to use to create the
              instance configuration.
            - Required when source is 'INSTANCE'
        type: str
    instance_configuration_id:
        description:
            - The OCID of the instance configuration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the InstanceConfiguration.
            - Use I(state=present) to create or update an InstanceConfiguration.
            - Use I(state=absent) to delete an InstanceConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create instance_configuration
  oci_compute_management_instance_configuration:
    compartment_id: ocid1.compartment.oc1..&lt;unique_id&gt;
    display_name: example-instance-configuration
    source: INSTANCE
    instance_id: ocid1.instance.oc1.phx.&lt;unique_id&gt;

- name: Update instance_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_management_instance_configuration:
    compartment_id: ocid1.compartment.oc1..&lt;unique_id&gt;
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: example-instance-configuration
    freeform_tags: {'Department': 'Finance'}

- name: Update instance_configuration
  oci_compute_management_instance_configuration:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: example-instance-configuration
    instance_configuration_id: ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete instance_configuration
  oci_compute_management_instance_configuration:
    instance_configuration_id: ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete instance_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_management_instance_configuration:
    compartment_id: ocid1.compartment.oc1..&lt;unique_id&gt;
    display_name: example-instance-configuration
    state: absent

"""

RETURN = """
instance_configuration:
    description:
        - Details of the InstanceConfiguration resource acted upon by the current operation
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
                                display_name:
                                    description:
                                        - A user-friendly name for the VNIC. Does not have to be unique.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: string
                                    sample: display_name_example
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
                                - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the
                                  'metadata' object.
                                - They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are
                                  string/string maps only).
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
                                - "**Note:** Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`
                                   path. When the instance launches and either of these keys are provided, the key values are formatted as
                                   OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:"
                                - "`http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob
                                   contains, among other things, the SSH keys that you provided for
                                    **\\"ssh_authorized_keys\\"**."
                                - "`http://169.254.169.254/openstack/latest/user_data` - Contains the
                                   base64-decoded data that you provided for **\\"user_data\\"**."
                                - "**Metadata Example**"
                                - "     \\"metadata\\" : {
                                           \\"quake_bot_level\\" : \\"Severe\\",
                                           \\"ssh_authorized_keys\\" : \\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+
                                           CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimi
                                           etWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8m
                                           SpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                                           ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZv
                                           BkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zq
                                           enordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPf
                                           aT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\\",
                                           \\"user_data\\" : \\"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\\"
                                        }
                                   **Getting Metadata on the Instance**"
                                - "To get information about your instance, connect to the instance using SSH and issue any of the
                                   following GET requests:"
                                -      curl http://169.254.169.254/opc/v1/instance/
                                       curl http://169.254.169.254/opc/v1/instance/metadata/
                                       curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>
                                -  You'll get back a response that includes all the instance information; only the metadata information; or
                                   the metadata information for the specified key name, respectively.
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
                                display_name:
                                    description:
                                        - A user-friendly name for the VNIC. Does not have to be unique.
                                          Avoid entering confidential information.
                                    returned: on success
                                    type: string
                                    sample: display_name_example
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
                - The date and time the instance configuration was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
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
                    "type": "iscsi",
                    "use_chap": true
                },
                "create_details": {
                    "availability_domain": "Uocm:PHX-AD-1",
                    "backup_policy_id": "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx",
                    "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                    "defined_tags": {'Operations': {'CostCenter': 'US'}},
                    "display_name": "display_name_example",
                    "freeform_tags": {'Department': 'Finance'},
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
                    "display_name": "display_name_example",
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
                "source_details": {
                    "source_type": "source_type_example",
                    "boot_volume_size_in_gbs": 56,
                    "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                    "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
                }
            },
            "secondary_vnics": [{
                "create_vnic_details": {
                    "assign_public_ip": true,
                    "display_name": "display_name_example",
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeManagementClient
    from oci.core.models import CreateInstanceConfigurationBase
    from oci.core.models import UpdateInstanceConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "instance_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_configuration_id")

    def get_get_fn(self):
        return self.client.get_instance_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_configuration,
            instance_configuration_id=self.module.params.get(
                "instance_configuration_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_instance_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateInstanceConfigurationBase

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_instance_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_instance_configuration=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateInstanceConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_instance_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_configuration_id=self.module.params.get(
                    "instance_configuration_id"
                ),
                update_instance_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_instance_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_configuration_id=self.module.params.get(
                    "instance_configuration_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


InstanceConfigurationHelperCustom = get_custom_class(
    "InstanceConfigurationHelperCustom"
)


class ResourceHelper(InstanceConfigurationHelperCustom, InstanceConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            source=dict(type="str", default="NONE", choices=["NONE", "INSTANCE"]),
            instance_details=dict(
                type="dict",
                options=dict(
                    instance_type=dict(type="str", required=True, choices=["compute"]),
                    block_volumes=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            attach_details=dict(
                                type="dict",
                                options=dict(
                                    display_name=dict(aliases=["name"], type="str"),
                                    is_read_only=dict(type="bool"),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["iscsi", "paravirtualized"],
                                    ),
                                    use_chap=dict(type="bool"),
                                ),
                            ),
                            create_details=dict(
                                type="dict",
                                options=dict(
                                    availability_domain=dict(type="str"),
                                    backup_policy_id=dict(type="str"),
                                    compartment_id=dict(type="str"),
                                    defined_tags=dict(type="dict"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    freeform_tags=dict(type="dict"),
                                    size_in_gbs=dict(type="int"),
                                    source_details=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["volumeBackup", "volume"],
                                            ),
                                            id=dict(type="str"),
                                        ),
                                    ),
                                ),
                            ),
                            volume_id=dict(type="str"),
                        ),
                    ),
                    launch_details=dict(
                        type="dict",
                        options=dict(
                            availability_domain=dict(type="str"),
                            compartment_id=dict(type="str"),
                            create_vnic_details=dict(
                                type="dict",
                                options=dict(
                                    assign_public_ip=dict(type="bool"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    hostname_label=dict(type="str"),
                                    nsg_ids=dict(type="list"),
                                    private_ip=dict(type="str"),
                                    skip_source_dest_check=dict(type="bool"),
                                    subnet_id=dict(type="str"),
                                ),
                            ),
                            defined_tags=dict(type="dict"),
                            display_name=dict(aliases=["name"], type="str"),
                            extended_metadata=dict(type="dict"),
                            freeform_tags=dict(type="dict"),
                            ipxe_script=dict(type="str"),
                            metadata=dict(type="dict"),
                            shape=dict(type="str"),
                            source_details=dict(
                                type="dict",
                                options=dict(
                                    source_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["image", "bootVolume"],
                                    ),
                                    boot_volume_size_in_gbs=dict(type="int"),
                                    image_id=dict(type="str"),
                                    boot_volume_id=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    secondary_vnics=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            create_vnic_details=dict(
                                type="dict",
                                options=dict(
                                    assign_public_ip=dict(type="bool"),
                                    display_name=dict(aliases=["name"], type="str"),
                                    hostname_label=dict(type="str"),
                                    nsg_ids=dict(type="list"),
                                    private_ip=dict(type="str"),
                                    skip_source_dest_check=dict(type="bool"),
                                    subnet_id=dict(type="str"),
                                ),
                            ),
                            display_name=dict(aliases=["name"], type="str"),
                            nic_index=dict(type="int"),
                        ),
                    ),
                ),
            ),
            instance_id=dict(type="str"),
            instance_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_configuration",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
