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
module: oci_compute_instance
short_description: Manage an Instance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Instance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new instance in the specified compartment and the specified availability domain.
      For general information about instances, see
      L(Overview of the Compute Service,https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm).
    - For information about access control and compartments, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - For information about availability domains, see
      L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the `ListAvailabilityDomains` operation
      in the Identity and Access Management Service API.
    - All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned,
      unique ID called an Oracle Cloud Identifier (OCID).
      When you create a resource, you can find its OCID in the response. You can
      also retrieve a resource's OCID by using a List API operation
      on that resource type, or by viewing the resource in the Console.
    - To launch an instance using an image or a boot volume use the `sourceDetails` parameter in
      L(LaunchInstanceDetails,https://docs.cloud.oracle.com/#/en/iaas/20160918/LaunchInstanceDetails).
    - "When you launch an instance, it is automatically attached to a virtual
      network interface card (VNIC), called the *primary VNIC*. The VNIC
      has a private IP address from the subnet's CIDR. You can either assign a
      private IP address of your choice or let Oracle automatically assign one.
      You can choose whether the instance has a public IP address. To retrieve the
      addresses, use the L(ListVnicAttachments,https://docs.cloud.oracle.com/#/en/iaas/20160918/VnicAttachment/ListVnicAttachments)
      operation to get the VNIC ID for the instance, and then call
      L(GetVnic,https://docs.cloud.oracle.com/#/en/iaas/20160918/Vnic/GetVnic) with the VNIC ID."
    - You can later add secondary VNICs to an instance. For more information, see
      L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/Content/Network/Tasks/managingVNICs.htm).
    - "This resource has the following action operations in the M(oci_instance_actions) module: stop, start, softreset, reset."
version_added: "2.5"
options:
    availability_domain:
        description:
            - The availability domain of the instance.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    create_vnic_details:
        description:
            - Details for the primary VNIC, which is automatically created and attached when
              the instance is launched.
        type: dict
        suboptions:
            assign_public_ip:
                description:
                    - Whether the VNIC should be assigned a public IP address. Defaults to whether
                      the subnet is public or private. If not set and the VNIC is being created
                      in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
                      L(Subnet,https://docs.cloud.oracle.com/#/en/iaas/20160918/Subnet/)), then no public IP address is assigned.
                      If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
                      a public IP address is assigned. If set to true and
                      `prohibitPublicIpOnVnic` = true, an error is returned.
                    - "**Note:** This public IP address is associated with the primary private IP
                      on the VNIC. For more information, see
                      L(IP Addresses,https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPaddresses.htm)."
                    - "**Note:** There's a limit to the number of L(public IPs,https://docs.cloud.oracle.com/#/en/iaas/20160918/PublicIp/)
                      a VNIC or instance can have. If you try to create a secondary VNIC
                      with an assigned public IP for an instance that has already
                      reached its public IP limit, an error is returned. For information
                      about the public IP limits, see
                      L(Public IP Addresses,https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm)."
                    - "Example: `false`"
                type: bool
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a
                      namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                type: dict
            display_name:
                description:
                    - A user-friendly name for the VNIC. Does not have to be unique.
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
            hostname_label:
                description:
                    - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                      portion of the primary private IP's fully qualified domain name (FQDN)
                      (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                      Must be unique across all VNICs in the subnet and comply with
                      L(RFC 952,https://tools.ietf.org/html/rfc952) and
                      L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                      The value appears in the L(Vnic,https://docs.cloud.oracle.com/#/en/iaas/20160918/Vnic/) object and also the
                      L(PrivateIp,https://docs.cloud.oracle.com/#/en/iaas/20160918/PrivateIp/) object returned by
                      L(ListPrivateIps,https://docs.cloud.oracle.com/#/en/iaas/20160918/PrivateIp/ListPrivateIps) and
                      L(GetPrivateIp,https://docs.cloud.oracle.com/#/en/iaas/20160918/PrivateIp/GetPrivateIp).
                    - For more information, see
                      L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                    - When launching an instance, use this `hostnameLabel` instead
                      of the deprecated `hostnameLabel` in
                      L(LaunchInstanceDetails,https://docs.cloud.oracle.com/#/en/iaas/20160918/requests/LaunchInstanceDetails).
                      If you provide both, the values must match.
                    - "Example: `bminstance-1`"
                type: str
            nsg_ids:
                description:
                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                      information about NSGs, see
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/).
                type: list
            private_ip:
                description:
                    - "A private IP address of your choice to assign to the VNIC. Must be an
                      available IP address within the subnet's CIDR. If you don't specify a
                      value, Oracle automatically assigns a private IP address from the subnet.
                      This is the VNIC's *primary* private IP address. The value appears in
                      the L(Vnic,https://docs.cloud.oracle.com/#/en/iaas/20160918/Vnic/) object and also the
                      L(PrivateIp,https://docs.cloud.oracle.com/#/en/iaas/20160918/PrivateIp/) object returned by
                      L(ListPrivateIps,https://docs.cloud.oracle.com/#/en/iaas/20160918/PrivateIp/ListPrivateIps) and
                      L(GetPrivateIp,https://docs.cloud.oracle.com/#/en/iaas/20160918/PrivateIp/GetPrivateIp)."
                    - "Example: `10.0.3.3`"
                type: str
            skip_source_dest_check:
                description:
                    - Whether the source/destination check is disabled on the VNIC.
                      Defaults to `false`, which means the check is performed. For information
                      about why you would skip the source/destination check, see
                      L(Using a Private IP as a Route Target,https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip).
                    - "Example: `true`"
                type: bool
            subnet_id:
                description:
                    - The OCID of the subnet to create the VNIC in. When launching an instance,
                      use this `subnetId` instead of the deprecated `subnetId` in
                      L(LaunchInstanceDetails,https://docs.cloud.oracle.com/#/en/iaas/20160918/requests/LaunchInstanceDetails).
                      At least one of them is required; if you provide both, the values must match.
                type: str
                required: true
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
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    extended_metadata:
        description:
            - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.
            - They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only).
        type: dict
    fault_domain:
        description:
            - A fault domain is a grouping of hardware and infrastructure within an availability domain.
              Each availability domain contains three fault domains. Fault domains let you distribute your
              instances so that they are not on the same physical hardware within a single availability domain.
              A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
              instances in other fault domains.
            - If you do not specify the fault domain, the system selects one for you. To change the fault
              domain for an instance, terminate it and launch a new instance in the preferred fault domain.
            - To get a list of fault domains, use the
              L(ListFaultDomains,https://docs.cloud.oracle.com/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
              Identity and Access Management Service API.
            - "Example: `FAULT-DOMAIN-1`"
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    hostname_label:
        description:
            - Deprecated. Instead use `hostnameLabel` in
              L(CreateVnicDetails,https://docs.cloud.oracle.com/#/en/iaas/20160918/CreateVnicDetails/).
              If you provide both, the values must match.
        type: str
    image_id:
        description:
            - Deprecated. Use `sourceDetails` with
              L(InstanceSourceViaImageDetails,https://docs.cloud.oracle.com/#/en/iaas/latest/requests/InstanceSourceViaImageDetails)
              source type instead. If you specify values for both, the values must match.
        type: str
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
                       \\"ssh_authorized_keys\\" : \\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80Z
                       BZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErR
                       eBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                       ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwX
                       cJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4Cjyxa
                       eLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\\",
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
    agent_config:
        description:
            - ""
        type: dict
        suboptions:
            is_monitoring_disabled:
                description:
                    - Whether the agent running on the instance can gather performance metrics and monitor the instance.
                      Default value is false.
                type: bool
    shape:
        description:
            - The shape of an instance. The shape determines the number of CPUs, amount of memory,
              and other resources allocated to the instance.
            - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/#/en/iaas/20160918/Shape/ListShapes).
            - Required for create using I(state=present).
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
                    - The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).
                    - Applicable when source_type is 'image'
                type: int
            image_id:
                description:
                    - The OCID of the image used to boot the instance.
                    - Required when source_type is 'image'
                type: str
            boot_volume_id:
                description:
                    - The OCID of the boot volume used to boot the instance.
                    - Required when source_type is 'bootVolume'
                type: str
    subnet_id:
        description:
            - Deprecated. Instead use `subnetId` in
              L(CreateVnicDetails,https://docs.cloud.oracle.com/#/en/iaas/20160918/CreateVnicDetails/).
              At least one of them is required; if you provide both, the values must match.
        type: str
    is_pv_encryption_in_transit_enabled:
        description:
            - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.
        type: bool
    instance_id:
        description:
            - The OCID of the instance.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    preserve_boot_volume:
        description:
            - Specifies whether to delete or preserve the boot volume when terminating an instance.
              The default value is false.
        type: bool
    state:
        description:
            - The state of the Instance.
            - Use I(state=present) to create or update an Instance.
            - Use I(state=absent) to delete an Instance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create instance
  oci_compute_instance:
    display_name: myinstance1
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
    shape: VM.Standard2.1
    metadata:
      foo: bar
      baz: quux
    source_details:
      source_type: image
      image_id: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx
    create_vnic_details:
      hostname_label: myinstance1
      private_ip: 10.0.0.5
      subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa

- name: Create instance
  oci_compute_instance:
    display_name: myinstance1
    availability_domain: Uocm:PHX-AD-1
    fault_domain: FAULT-DOMAIN-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
    shape: VM.Standard2.1
    source_details:
      source_type: bootVolume
      boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
    create_vnic_details:
      hostname_label: myinstance1
      private_ip: 10.0.0.5
      subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa

- name: Create instance
  oci_compute_instance:
    display_name: myinstance1
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
    shape: VM.Standard2.1
    source_details:
      source_type: image
      image_id: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx
      boot_volume_size_in_gbs: 100
    create_vnic_details:
      hostname_label: myinstance1
      subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa

- name: Update instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_instance:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: myinstance1
    freeform_tags: {'Department': 'Finance'}

- name: Update instance
  oci_compute_instance:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: myinstance1
    instance_id: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete instance
  oci_compute_instance:
    instance_id: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_instance:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
    display_name: myinstance1
    state: absent

"""

RETURN = """
instance:
    description:
        - Details of the Instance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the instance is running in.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the instance.
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My bare metal instance`"
            returned: on success
            type: string
            sample: My bare metal instance
        extended_metadata:
            description:
                - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.
                - They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps
                  only).
            returned: on success
            type: dict
            sample: {}
        fault_domain:
            description:
                - The name of the fault domain the instance is running in.
                - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                  Each availability domain contains three fault domains. Fault domains let you distribute your
                  instances so that they are not on the same physical hardware within a single availability domain.
                  A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                  instances in other fault domains.
                - If you do not specify the fault domain, the system selects one for you. To change the fault
                  domain for an instance, terminate it and launch a new instance in the preferred fault domain.
                - "Example: `FAULT-DOMAIN-1`"
            returned: on success
            type: string
            sample: FAULT-DOMAIN-1
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
                - The OCID of the instance.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        image_id:
            description:
                - Deprecated. Use `sourceDetails` instead.
            returned: on success
            type: string
            sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        ipxe_script:
            description:
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
        launch_mode:
            description:
                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.
                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
            returned: on success
            type: string
            sample: NATIVE
        launch_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                boot_volume_type:
                    description:
                        - "Emulation type for volume.
                          * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block
                          Storage volumes on Oracle provided images.
                          * `SCSI` - Emulated SCSI disk.
                          * `IDE` - Emulated IDE disk.
                          * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data
                          volumes on Oracle provided images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk."
                    returned: on success
                    type: string
                    sample: ISCSI
                firmware:
                    description:
                        - "Firmware used to boot VM.  Select the option that matches your operating system.
                          * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating
                          systems that boot using MBR style bootloaders.
                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the
                          default for Oracle provided images."
                    returned: on success
                    type: string
                    sample: BIOS
                network_type:
                    description:
                        - "Emulation type for the physical network interface card (NIC).
                          * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.
                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers."
                    returned: on success
                    type: string
                    sample: E1000
                remote_data_volume_type:
                    description:
                        - "Emulation type for volume.
                          * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block
                          Storage volumes on Oracle provided images.
                          * `SCSI` - Emulated SCSI disk.
                          * `IDE` - Emulated IDE disk.
                          * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data
                          volumes on Oracle provided images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk."
                    returned: on success
                    type: string
                    sample: ISCSI
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Whether to enable in-transit encryption for the boot volume's paravirtualized attachment. The default value is false.
                    returned: on success
                    type: bool
                    sample: true
                is_consistent_volume_naming_enabled:
                    description:
                        - Whether to enable consistent volume naming feature. Defaults to false.
                    returned: on success
                    type: bool
                    sample: true
        lifecycle_state:
            description:
                - The current state of the instance.
            returned: on success
            type: string
            sample: PROVISIONING
        metadata:
            description:
                - Custom metadata that you provide.
            returned: on success
            type: dict
            sample: {}
        region:
            description:
                - The region that contains the availability domain the instance is running in.
                - For the us-phoenix-1 and us-ashburn-1 regions, `phx` and `iad` are returned, respectively.
                  For all other regions, the full region name is returned.
                - "Examples: `phx`, `eu-frankfurt-1`"
            returned: on success
            type: string
            sample: region_example
        shape:
            description:
                - The shape of the instance. The shape determines the number of CPUs and the amount of memory
                  allocated to the instance. You can enumerate all available shapes by calling
                  L(ListShapes,https://docs.cloud.oracle.com/#/en/iaas/20160918/Shape/ListShapes).
            returned: on success
            type: string
            sample: shape_example
        source_details:
            description:
                - Details for creating an instance
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
                        - The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).
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
        time_created:
            description:
                - The date and time the instance was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        agent_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_monitoring_disabled:
                    description:
                        - Whether the agent running on the instance can gather performance metrics and monitor the instance.
                    returned: on success
                    type: bool
                    sample: true
        time_maintenance_reboot_due:
            description:
                - "The date and time the instance is expected to be stopped / started,  in the format defined by RFC3339.
                  After that time if instance hasn't been rebooted, Oracle will reboot the instance within 24 hours of the due time.
                  Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state.
                  Example: `2018-05-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2018-05-25T21:10:29.600Z
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "My bare metal instance",
        "extended_metadata": {},
        "fault_domain": "FAULT-DOMAIN-1",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "ipxe_script": "ipxe_script_example",
        "launch_mode": "NATIVE",
        "launch_options": {
            "boot_volume_type": "ISCSI",
            "firmware": "BIOS",
            "network_type": "E1000",
            "remote_data_volume_type": "ISCSI",
            "is_pv_encryption_in_transit_enabled": true,
            "is_consistent_volume_naming_enabled": true
        },
        "lifecycle_state": "PROVISIONING",
        "metadata": {},
        "region": "region_example",
        "shape": "shape_example",
        "source_details": {
            "source_type": "source_type_example",
            "boot_volume_size_in_gbs": 56,
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2016-08-25T21:10:29.600Z",
        "agent_config": {
            "is_monitoring_disabled": true
        },
        "time_maintenance_reboot_due": "2018-05-25T21:10:29.600Z"
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
    from oci.core import ComputeClient
    from oci.core.models import LaunchInstanceDetails
    from oci.core.models import UpdateInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_id")

    def get_get_fn(self):
        return self.client.get_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance, instance_id=self.module.params.get("instance_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "availability_domain",
            "display_name",
        ]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(self.client.list_instances, **kwargs)

    def get_create_model_class(self):
        return LaunchInstanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.launch_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(launch_instance_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_id=self.module.params.get("instance_id"),
                update_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.terminate_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_id=self.module.params.get("instance_id"),
                preserve_boot_volume=self.module.params.get("preserve_boot_volume"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_terminated_states(),
        )


InstanceHelperCustom = get_custom_class("InstanceHelperCustom")


class ResourceHelper(InstanceHelperCustom, InstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            create_vnic_details=dict(
                type="dict",
                options=dict(
                    assign_public_ip=dict(type="bool"),
                    defined_tags=dict(type="dict"),
                    display_name=dict(aliases=["name"], type="str"),
                    freeform_tags=dict(type="dict"),
                    hostname_label=dict(type="str"),
                    nsg_ids=dict(type="list"),
                    private_ip=dict(type="str"),
                    skip_source_dest_check=dict(type="bool"),
                    subnet_id=dict(type="str", required=True),
                ),
            ),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            extended_metadata=dict(type="dict"),
            fault_domain=dict(type="str"),
            freeform_tags=dict(type="dict"),
            hostname_label=dict(type="str"),
            image_id=dict(type="str"),
            ipxe_script=dict(type="str"),
            metadata=dict(type="dict"),
            agent_config=dict(
                type="dict", options=dict(is_monitoring_disabled=dict(type="bool"))
            ),
            shape=dict(type="str"),
            source_details=dict(
                type="dict",
                options=dict(
                    source_type=dict(
                        type="str", required=True, choices=["image", "bootVolume"]
                    ),
                    boot_volume_size_in_gbs=dict(type="int"),
                    image_id=dict(type="str"),
                    boot_volume_id=dict(type="str"),
                ),
            ),
            subnet_id=dict(type="str"),
            is_pv_encryption_in_transit_enabled=dict(type="bool"),
            instance_id=dict(aliases=["id"], type="str"),
            preserve_boot_volume=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance",
        service_client_class=ComputeClient,
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
