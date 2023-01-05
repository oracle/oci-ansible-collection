#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_cloud_migrations_target_asset_facts
short_description: Fetches details about one or multiple TargetAsset resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TargetAsset resources in Oracle Cloud Infrastructure
    - Returns a list of target assets.
    - If I(target_asset_id) is specified, the details of a single TargetAsset will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_plan_id:
        description:
            - Unique migration plan identifier
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire given display name.
        type: str
        aliases: ["name"]
    target_asset_id:
        description:
            - Unique target asset identifier
            - Required to get a specific target_asset.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - The current state of the target asset.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "NEEDS_ATTENTION"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. The default order for 'timeCreated' is descending. The default order for 'displayName'
              is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific target_asset
  oci_cloud_migrations_target_asset_facts:
    # required
    target_asset_id: "ocid1.targetasset.oc1..xxxxxxEXAMPLExxxxxx"

- name: List target_assets
  oci_cloud_migrations_target_asset_facts:

    # optional
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    target_asset_id: "ocid1.targetasset.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
target_assets:
    description:
        - List of TargetAsset resources
    returned: on success
    type: complex
    contains:
        preferred_shape_type:
            description:
                - Preferred VM shape type that you provide.
                - Returned for get operation
            returned: on success
            type: str
            sample: VM
        test_spec:
            description:
                - ""
                - Returned for get operation
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
                        - The OCID of the compute capacity reservation under which this instance is launched.
                          You can opt out of all default reservations by specifying an empty string as input for this field.
                          For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-
                          capacity.htm#default).
                    returned: on success
                    type: str
                    sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The OCID of the compartment.
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
                                - Whether the VNIC should be assigned a public IP address. Defaults to whether
                                  the subnet is public or private. If not set and the VNIC is being created
                                  in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
                                  L(Subnet,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Subnet/)), then no public IP address is assigned.
                                  If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
                                  a public IP address is assigned. If set to true and
                                  `prohibitPublicIpOnVnic` = true, an error is returned.
                                - "**Note:** This public IP address is associated with the primary private IP
                                  on the VNIC. For more information, see
                                  L(IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm)."
                                - "**Note:** There's a limit to the number of L(public IPs,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/iaas/latest/PublicIp/)
                                  a VNIC or instance can have. If you try to create a secondary VNIC
                                  with an assigned public IP for an instance that has already
                                  reached its public IP limit, an error is returned. For information
                                  about the public IP limits, see
                                  L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)."
                                - "Example: `false`"
                                - If you specify a `vlanId`, then `assignPublicIp` must be set to false. See
                                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: bool
                            sample: true
                        assign_private_dns_record:
                            description:
                                - Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record
                                  registration for the VNIC. If set to true, the DNS record will be registered. By default,
                                  the value is true.
                                - If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.
                            returned: on success
                            type: bool
                            sample: true
                        defined_tags:
                            description:
                                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                                  Example: `{\\"bar-key\\": \\"value\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        hostname_label:
                            description:
                                - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                                  portion of the primary private IP's fully qualified domain name (FQDN)
                                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                                  Must be unique across all VNICs in the subnet and comply with
                                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                                  The value appears in the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                                  L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                                  L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp).
                                - For more information, see
                                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                                - When launching an instance, use this `hostnameLabel` instead
                                  of the deprecated `hostnameLabel` in
                                  L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                                  If you provide both, the values must match.
                                - "Example: `bminstance-1`"
                                - If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN
                                  can not be assigned a hostname. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: str
                            sample: hostname_label_example
                        nsg_ids:
                            description:
                                - List of OCIDs of the network security groups (NSGs) that are added to the VNIC. For more
                                   information about NSGs, see
                                   L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                -  If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId`
                                   indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs,
                                   all VNICs in the VLAN belong to the NSGs that are associated with the VLAN.
                                   See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: list
                            sample: []
                        private_ip:
                            description:
                                - "A private IP address of your choice to assign to the VNIC. Must be an
                                  available IP address within the subnet's CIDR. If you don't specify a
                                  value, Oracle automatically assigns a private IP address from the subnet.
                                  This is the VNIC's *primary* private IP address. The value appears in
                                  the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                                  L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                                  L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp)."
                                - If you specify a `vlanId`, the `privateIp` cannot be specified.
                                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - "Example: `10.0.3.3`"
                            returned: on success
                            type: str
                            sample: private_ip_example
                        skip_source_dest_check:
                            description:
                                - Whether the source/destination check is disabled on the VNIC.
                                  Defaults to `false`, which means the check is performed. For information
                                  about why you should skip the source/destination check, see
                                  L(Using a Private IP as a Route
                                  Target,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).
                                - If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the
                                  source/destination check is always disabled for VNICs in a VLAN. See
                                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        subnet_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create the VNIC. When
                                  launching an instance,
                                  use this `subnetId` instead of the deprecated `subnetId` in
                                  L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                                  At least one of them is required; if you provide both, the values must match.
                                - If you are an Oracle Cloud VMware Solution customer and creating a secondary
                                  VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`.
                                  If you provide both `vlanId` and `subnetId`, the request fails.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        vlan_id:
                            description:
                                - Provide this attribute only if you are an Oracle Cloud VMware Solution
                                  customer and creating a secondary VNIC in a VLAN. The value is the
                                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
                                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - Provide a `vlanId` instead of a `subnetId`. If you provide both
                                  `vlanId` and `subnetId`, the request fails.
                            returned: on success
                            type: str
                            sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                dedicated_vm_host_id:
                    description:
                        - The OCID of the dedicated VM host.
                    returned: on success
                    type: str
                    sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                fault_domain:
                    description:
                        - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                          Each availability domain contains three fault domains. Fault domains lets you distribute your
                          instances so that they are not on the same physical hardware within a single availability domain.
                          A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                          instances in other fault domains.
                        - If you do not specify the fault domain, the system selects one for you.
                        - To get a list of fault domains, use the
                          L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
                          Identity and Access Management Service API.
                        - "Example: `FAULT-DOMAIN-1`"
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                freeform_tags:
                    description:
                        - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                hostname_label:
                    description:
                        - Deprecated. Instead use `hostnameLabel` in
                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/).
                          If you provide both, the values must match.
                    returned: on success
                    type: str
                    sample: hostname_label_example
                ipxe_script:
                    description:
                        - This is an advanced option.
                        - When a bare metal or virtual machine
                          instance boots, the iPXE firmware that runs on the instance is
                          configured to run an iPXE script to continue the boot process.
                        - If you want more control over the boot process, you can provide
                          your own custom iPXE script that will run when the instance boots.
                          Be aware that the same iPXE script will run
                          every time an instance boots, not only after the initial
                          LaunchInstance call.
                        - "By default, the iPXE script connects to the instance's local boot
                          volume over iSCSI and performs a network boot. If you use a custom iPXE
                          script and want to network-boot from the instance's local boot volume
                          over iSCSI in the same way as the default iPXE script, use the
                          following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                          iqn.2015-02.oracle.boot."
                        - If your instance boot volume type is paravirtualized,
                          the boot volume is attached to the instance through virtio-scsi and no iPXE script is used.
                          If your instance boot volume type is paravirtualized
                          and you use custom iPXE to perform network-boot into your instance,
                          the primary boot volume is attached as a data volume through the virtio-scsi drive.
                        - For more information about the Bring Your Own Image feature of
                          Oracle Cloud Infrastructure, see
                          L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                        - For more information about iPXE, see http://ipxe.org.
                    returned: on success
                    type: str
                    sample: ipxe_script_example
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
                                        - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated.
                                          By default, it is false if not specified.
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
                                  monitoring plugins. By default, the value is false (monitoring plugins are enabled).
                                - "These are the monitoring plugins: Compute instance monitoring
                                  and Custom logs monitoring."
                                - The monitoring plugins are controlled by this parameter and by the per-plugin
                                  configuration in the `pluginsConfig` object.
                                - "- If `isMonitoringDisabled` is true, all the monitoring plugins are disabled, regardless of
                                  the per-plugin configuration.
                                  - If `isMonitoringDisabled` is false, all the monitoring plugins are enabled. You
                                  can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                  object."
                            returned: on success
                            type: bool
                            sample: true
                        is_management_disabled:
                            description:
                                - Whether Oracle Cloud Agent can run all the available management plugins.
                                  By default, the value is false (management plugins are enabled).
                                - "These are the management plugins: OS Management Service Agent and Compute instance
                                  run command."
                                - The management plugins are controlled by this parameter and the per-plugin
                                  configuration in the `pluginsConfig` object.
                                - "- If `isManagementDisabled` is true, all the management plugins are disabled, regardless of
                                  the per-plugin configuration.
                                  - If `isManagementDisabled` is false, all the management plugins are enabled. You
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
                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
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
                                - The total amount of memory in gigabytes that is available to the instance.
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
                                - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 32,768 GB (32 TB).
                            returned: on success
                            type: int
                            sample: 56
                        image_id:
                            description:
                                - The OCID of the image used to boot the instance.
                            returned: on success
                            type: str
                            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                        kms_key_id:
                            description:
                                - The OCID of the key management key to assign as the master encryption key for the boot volume.
                            returned: on success
                            type: str
                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                        boot_volume_vpus_per_gb:
                            description:
                                - The number of volume performance units (VPUs) that will be applied to this volume per GB that
                                  represents the Block Volume service's elastic performance options.
                                  See L(Block Volume Performance
                                  Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
                                - "Allowed values:"
                                - " * `10`: Represents Balanced option."
                                - " * `20`: Represents Higher Performance option."
                                - " * `30`-`120`: Represents the Ultra High Performance option."
                                - For volumes with the auto-tuned performance feature enabled, this is set to the default (minimum) VPUs/GB.
                            returned: on success
                            type: int
                            sample: 56
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and
                          boot volumes. By default, the value is false.
                    returned: on success
                    type: bool
                    sample: true
        block_volumes_performance:
            description:
                - Performance of the block volumes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        ms_license:
            description:
                - Microsoft license for VM configuration.
                - Returned for get operation
            returned: on success
            type: str
            sample: ms_license_example
        user_spec:
            description:
                - ""
                - Returned for get operation
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
                        - The OCID of the compute capacity reservation under which this instance is launched.
                          You can opt out of all default reservations by specifying an empty string as input for this field.
                          For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-
                          capacity.htm#default).
                    returned: on success
                    type: str
                    sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The OCID of the compartment.
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
                                - Whether the VNIC should be assigned a public IP address. Defaults to whether
                                  the subnet is public or private. If not set and the VNIC is being created
                                  in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
                                  L(Subnet,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Subnet/)), then no public IP address is assigned.
                                  If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
                                  a public IP address is assigned. If set to true and
                                  `prohibitPublicIpOnVnic` = true, an error is returned.
                                - "**Note:** This public IP address is associated with the primary private IP
                                  on the VNIC. For more information, see
                                  L(IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm)."
                                - "**Note:** There's a limit to the number of L(public IPs,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/iaas/latest/PublicIp/)
                                  a VNIC or instance can have. If you try to create a secondary VNIC
                                  with an assigned public IP for an instance that has already
                                  reached its public IP limit, an error is returned. For information
                                  about the public IP limits, see
                                  L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)."
                                - "Example: `false`"
                                - If you specify a `vlanId`, then `assignPublicIp` must be set to false. See
                                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: bool
                            sample: true
                        assign_private_dns_record:
                            description:
                                - Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record
                                  registration for the VNIC. If set to true, the DNS record will be registered. By default,
                                  the value is true.
                                - If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.
                            returned: on success
                            type: bool
                            sample: true
                        defined_tags:
                            description:
                                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                                  Example: `{\\"bar-key\\": \\"value\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        hostname_label:
                            description:
                                - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                                  portion of the primary private IP's fully qualified domain name (FQDN)
                                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                                  Must be unique across all VNICs in the subnet and comply with
                                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                                  The value appears in the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                                  L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                                  L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp).
                                - For more information, see
                                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                                - When launching an instance, use this `hostnameLabel` instead
                                  of the deprecated `hostnameLabel` in
                                  L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                                  If you provide both, the values must match.
                                - "Example: `bminstance-1`"
                                - If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN
                                  can not be assigned a hostname. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: str
                            sample: hostname_label_example
                        nsg_ids:
                            description:
                                - List of OCIDs of the network security groups (NSGs) that are added to the VNIC. For more
                                   information about NSGs, see
                                   L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                -  If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId`
                                   indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs,
                                   all VNICs in the VLAN belong to the NSGs that are associated with the VLAN.
                                   See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: list
                            sample: []
                        private_ip:
                            description:
                                - "A private IP address of your choice to assign to the VNIC. Must be an
                                  available IP address within the subnet's CIDR. If you don't specify a
                                  value, Oracle automatically assigns a private IP address from the subnet.
                                  This is the VNIC's *primary* private IP address. The value appears in
                                  the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                                  L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                                  L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp)."
                                - If you specify a `vlanId`, the `privateIp` cannot be specified.
                                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - "Example: `10.0.3.3`"
                            returned: on success
                            type: str
                            sample: private_ip_example
                        skip_source_dest_check:
                            description:
                                - Whether the source/destination check is disabled on the VNIC.
                                  Defaults to `false`, which means the check is performed. For information
                                  about why you should skip the source/destination check, see
                                  L(Using a Private IP as a Route
                                  Target,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).
                                - If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the
                                  source/destination check is always disabled for VNICs in a VLAN. See
                                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        subnet_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create the VNIC. When
                                  launching an instance,
                                  use this `subnetId` instead of the deprecated `subnetId` in
                                  L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                                  At least one of them is required; if you provide both, the values must match.
                                - If you are an Oracle Cloud VMware Solution customer and creating a secondary
                                  VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`.
                                  If you provide both `vlanId` and `subnetId`, the request fails.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        vlan_id:
                            description:
                                - Provide this attribute only if you are an Oracle Cloud VMware Solution
                                  customer and creating a secondary VNIC in a VLAN. The value is the
                                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
                                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - Provide a `vlanId` instead of a `subnetId`. If you provide both
                                  `vlanId` and `subnetId`, the request fails.
                            returned: on success
                            type: str
                            sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                dedicated_vm_host_id:
                    description:
                        - The OCID of the dedicated VM host.
                    returned: on success
                    type: str
                    sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                fault_domain:
                    description:
                        - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                          Each availability domain contains three fault domains. Fault domains lets you distribute your
                          instances so that they are not on the same physical hardware within a single availability domain.
                          A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                          instances in other fault domains.
                        - If you do not specify the fault domain, the system selects one for you.
                        - To get a list of fault domains, use the
                          L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
                          Identity and Access Management Service API.
                        - "Example: `FAULT-DOMAIN-1`"
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                freeform_tags:
                    description:
                        - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                hostname_label:
                    description:
                        - Deprecated. Instead use `hostnameLabel` in
                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/).
                          If you provide both, the values must match.
                    returned: on success
                    type: str
                    sample: hostname_label_example
                ipxe_script:
                    description:
                        - This is an advanced option.
                        - When a bare metal or virtual machine
                          instance boots, the iPXE firmware that runs on the instance is
                          configured to run an iPXE script to continue the boot process.
                        - If you want more control over the boot process, you can provide
                          your own custom iPXE script that will run when the instance boots.
                          Be aware that the same iPXE script will run
                          every time an instance boots, not only after the initial
                          LaunchInstance call.
                        - "By default, the iPXE script connects to the instance's local boot
                          volume over iSCSI and performs a network boot. If you use a custom iPXE
                          script and want to network-boot from the instance's local boot volume
                          over iSCSI in the same way as the default iPXE script, use the
                          following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                          iqn.2015-02.oracle.boot."
                        - If your instance boot volume type is paravirtualized,
                          the boot volume is attached to the instance through virtio-scsi and no iPXE script is used.
                          If your instance boot volume type is paravirtualized
                          and you use custom iPXE to perform network-boot into your instance,
                          the primary boot volume is attached as a data volume through the virtio-scsi drive.
                        - For more information about the Bring Your Own Image feature of
                          Oracle Cloud Infrastructure, see
                          L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                        - For more information about iPXE, see http://ipxe.org.
                    returned: on success
                    type: str
                    sample: ipxe_script_example
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
                                        - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated.
                                          By default, it is false if not specified.
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
                                  monitoring plugins. By default, the value is false (monitoring plugins are enabled).
                                - "These are the monitoring plugins: Compute instance monitoring
                                  and Custom logs monitoring."
                                - The monitoring plugins are controlled by this parameter and by the per-plugin
                                  configuration in the `pluginsConfig` object.
                                - "- If `isMonitoringDisabled` is true, all the monitoring plugins are disabled, regardless of
                                  the per-plugin configuration.
                                  - If `isMonitoringDisabled` is false, all the monitoring plugins are enabled. You
                                  can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                  object."
                            returned: on success
                            type: bool
                            sample: true
                        is_management_disabled:
                            description:
                                - Whether Oracle Cloud Agent can run all the available management plugins.
                                  By default, the value is false (management plugins are enabled).
                                - "These are the management plugins: OS Management Service Agent and Compute instance
                                  run command."
                                - The management plugins are controlled by this parameter and the per-plugin
                                  configuration in the `pluginsConfig` object.
                                - "- If `isManagementDisabled` is true, all the management plugins are disabled, regardless of
                                  the per-plugin configuration.
                                  - If `isManagementDisabled` is false, all the management plugins are enabled. You
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
                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
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
                                - The total amount of memory in gigabytes that is available to the instance.
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
                                - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 32,768 GB (32 TB).
                            returned: on success
                            type: int
                            sample: 56
                        image_id:
                            description:
                                - The OCID of the image used to boot the instance.
                            returned: on success
                            type: str
                            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                        kms_key_id:
                            description:
                                - The OCID of the key management key to assign as the master encryption key for the boot volume.
                            returned: on success
                            type: str
                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                        boot_volume_vpus_per_gb:
                            description:
                                - The number of volume performance units (VPUs) that will be applied to this volume per GB that
                                  represents the Block Volume service's elastic performance options.
                                  See L(Block Volume Performance
                                  Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
                                - "Allowed values:"
                                - " * `10`: Represents Balanced option."
                                - " * `20`: Represents Higher Performance option."
                                - " * `30`-`120`: Represents the Ultra High Performance option."
                                - For volumes with the auto-tuned performance feature enabled, this is set to the default (minimum) VPUs/GB.
                            returned: on success
                            type: int
                            sample: 56
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and
                          boot volumes. By default, the value is false.
                    returned: on success
                    type: bool
                    sample: true
        recommended_spec:
            description:
                - ""
                - Returned for get operation
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
                        - The OCID of the compute capacity reservation under which this instance is launched.
                          You can opt out of all default reservations by specifying an empty string as input for this field.
                          For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-
                          capacity.htm#default).
                    returned: on success
                    type: str
                    sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The OCID of the compartment.
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
                                - Whether the VNIC should be assigned a public IP address. Defaults to whether
                                  the subnet is public or private. If not set and the VNIC is being created
                                  in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
                                  L(Subnet,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Subnet/)), then no public IP address is assigned.
                                  If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
                                  a public IP address is assigned. If set to true and
                                  `prohibitPublicIpOnVnic` = true, an error is returned.
                                - "**Note:** This public IP address is associated with the primary private IP
                                  on the VNIC. For more information, see
                                  L(IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm)."
                                - "**Note:** There's a limit to the number of L(public IPs,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/iaas/latest/PublicIp/)
                                  a VNIC or instance can have. If you try to create a secondary VNIC
                                  with an assigned public IP for an instance that has already
                                  reached its public IP limit, an error is returned. For information
                                  about the public IP limits, see
                                  L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)."
                                - "Example: `false`"
                                - If you specify a `vlanId`, then `assignPublicIp` must be set to false. See
                                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: bool
                            sample: true
                        assign_private_dns_record:
                            description:
                                - Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record
                                  registration for the VNIC. If set to true, the DNS record will be registered. By default,
                                  the value is true.
                                - If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.
                            returned: on success
                            type: bool
                            sample: true
                        defined_tags:
                            description:
                                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                                  Example: `{\\"bar-key\\": \\"value\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        hostname_label:
                            description:
                                - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                                  portion of the primary private IP's fully qualified domain name (FQDN)
                                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                                  Must be unique across all VNICs in the subnet and comply with
                                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                                  The value appears in the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                                  L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                                  L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp).
                                - For more information, see
                                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                                - When launching an instance, use this `hostnameLabel` instead
                                  of the deprecated `hostnameLabel` in
                                  L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                                  If you provide both, the values must match.
                                - "Example: `bminstance-1`"
                                - If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN
                                  can not be assigned a hostname. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: str
                            sample: hostname_label_example
                        nsg_ids:
                            description:
                                - List of OCIDs of the network security groups (NSGs) that are added to the VNIC. For more
                                   information about NSGs, see
                                   L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                                -  If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId`
                                   indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs,
                                   all VNICs in the VLAN belong to the NSGs that are associated with the VLAN.
                                   See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                            returned: on success
                            type: list
                            sample: []
                        private_ip:
                            description:
                                - "A private IP address of your choice to assign to the VNIC. Must be an
                                  available IP address within the subnet's CIDR. If you don't specify a
                                  value, Oracle automatically assigns a private IP address from the subnet.
                                  This is the VNIC's *primary* private IP address. The value appears in
                                  the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                                  L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                                  L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp)."
                                - If you specify a `vlanId`, the `privateIp` cannot be specified.
                                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - "Example: `10.0.3.3`"
                            returned: on success
                            type: str
                            sample: private_ip_example
                        skip_source_dest_check:
                            description:
                                - Whether the source/destination check is disabled on the VNIC.
                                  Defaults to `false`, which means the check is performed. For information
                                  about why you should skip the source/destination check, see
                                  L(Using a Private IP as a Route
                                  Target,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).
                                - If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the
                                  source/destination check is always disabled for VNICs in a VLAN. See
                                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        subnet_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create the VNIC. When
                                  launching an instance,
                                  use this `subnetId` instead of the deprecated `subnetId` in
                                  L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                                  At least one of them is required; if you provide both, the values must match.
                                - If you are an Oracle Cloud VMware Solution customer and creating a secondary
                                  VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`.
                                  If you provide both `vlanId` and `subnetId`, the request fails.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        vlan_id:
                            description:
                                - Provide this attribute only if you are an Oracle Cloud VMware Solution
                                  customer and creating a secondary VNIC in a VLAN. The value is the
                                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
                                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                                - Provide a `vlanId` instead of a `subnetId`. If you provide both
                                  `vlanId` and `subnetId`, the request fails.
                            returned: on success
                            type: str
                            sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                dedicated_vm_host_id:
                    description:
                        - The OCID of the dedicated VM host.
                    returned: on success
                    type: str
                    sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                fault_domain:
                    description:
                        - A fault domain is a grouping of hardware and infrastructure within an availability domain.
                          Each availability domain contains three fault domains. Fault domains lets you distribute your
                          instances so that they are not on the same physical hardware within a single availability domain.
                          A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
                          instances in other fault domains.
                        - If you do not specify the fault domain, the system selects one for you.
                        - To get a list of fault domains, use the
                          L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation in the
                          Identity and Access Management Service API.
                        - "Example: `FAULT-DOMAIN-1`"
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                freeform_tags:
                    description:
                        - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                hostname_label:
                    description:
                        - Deprecated. Instead use `hostnameLabel` in
                          L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/).
                          If you provide both, the values must match.
                    returned: on success
                    type: str
                    sample: hostname_label_example
                ipxe_script:
                    description:
                        - This is an advanced option.
                        - When a bare metal or virtual machine
                          instance boots, the iPXE firmware that runs on the instance is
                          configured to run an iPXE script to continue the boot process.
                        - If you want more control over the boot process, you can provide
                          your own custom iPXE script that will run when the instance boots.
                          Be aware that the same iPXE script will run
                          every time an instance boots, not only after the initial
                          LaunchInstance call.
                        - "By default, the iPXE script connects to the instance's local boot
                          volume over iSCSI and performs a network boot. If you use a custom iPXE
                          script and want to network-boot from the instance's local boot volume
                          over iSCSI in the same way as the default iPXE script, use the
                          following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                          iqn.2015-02.oracle.boot."
                        - If your instance boot volume type is paravirtualized,
                          the boot volume is attached to the instance through virtio-scsi and no iPXE script is used.
                          If your instance boot volume type is paravirtualized
                          and you use custom iPXE to perform network-boot into your instance,
                          the primary boot volume is attached as a data volume through the virtio-scsi drive.
                        - For more information about the Bring Your Own Image feature of
                          Oracle Cloud Infrastructure, see
                          L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                        - For more information about iPXE, see http://ipxe.org.
                    returned: on success
                    type: str
                    sample: ipxe_script_example
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
                                        - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated.
                                          By default, it is false if not specified.
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
                                  monitoring plugins. By default, the value is false (monitoring plugins are enabled).
                                - "These are the monitoring plugins: Compute instance monitoring
                                  and Custom logs monitoring."
                                - The monitoring plugins are controlled by this parameter and by the per-plugin
                                  configuration in the `pluginsConfig` object.
                                - "- If `isMonitoringDisabled` is true, all the monitoring plugins are disabled, regardless of
                                  the per-plugin configuration.
                                  - If `isMonitoringDisabled` is false, all the monitoring plugins are enabled. You
                                  can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig`
                                  object."
                            returned: on success
                            type: bool
                            sample: true
                        is_management_disabled:
                            description:
                                - Whether Oracle Cloud Agent can run all the available management plugins.
                                  By default, the value is false (management plugins are enabled).
                                - "These are the management plugins: OS Management Service Agent and Compute instance
                                  run command."
                                - The management plugins are controlled by this parameter and the per-plugin
                                  configuration in the `pluginsConfig` object.
                                - "- If `isManagementDisabled` is true, all the management plugins are disabled, regardless of
                                  the per-plugin configuration.
                                  - If `isManagementDisabled` is false, all the management plugins are enabled. You
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
                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
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
                                - The total amount of memory in gigabytes that is available to the instance.
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
                                - The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 32,768 GB (32 TB).
                            returned: on success
                            type: int
                            sample: 56
                        image_id:
                            description:
                                - The OCID of the image used to boot the instance.
                            returned: on success
                            type: str
                            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                        kms_key_id:
                            description:
                                - The OCID of the key management key to assign as the master encryption key for the boot volume.
                            returned: on success
                            type: str
                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                        boot_volume_vpus_per_gb:
                            description:
                                - The number of volume performance units (VPUs) that will be applied to this volume per GB that
                                  represents the Block Volume service's elastic performance options.
                                  See L(Block Volume Performance
                                  Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
                                - "Allowed values:"
                                - " * `10`: Represents Balanced option."
                                - " * `20`: Represents Higher Performance option."
                                - " * `30`-`120`: Represents the Ultra High Performance option."
                                - For volumes with the auto-tuned performance feature enabled, this is set to the default (minimum) VPUs/GB.
                            returned: on success
                            type: int
                            sample: 56
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and
                          boot volumes. By default, the value is false.
                    returned: on success
                    type: bool
                    sample: true
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the target asset.
            returned: on success
            type: str
            sample: CREATING
        migration_plan_id:
            description:
                - OCID of the associated migration plan.
            returned: on success
            type: str
            sample: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        created_resource_id:
            description:
                - Created resource identifier
            returned: on success
            type: str
            sample: "ocid1.createdresource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The type of target asset.
            returned: on success
            type: str
            sample: INSTANCE
        is_excluded_from_execution:
            description:
                - A boolean indicating whether the asset should be migrated.
            returned: on success
            type: bool
            sample: true
        compatibility_messages:
            description:
                - Messages about the compatibility issues.
            returned: on success
            type: complex
            contains:
                severity:
                    description:
                        - Severity level of the compatibility issue.
                    returned: on success
                    type: str
                    sample: ERROR
                name:
                    description:
                        - Name of the compatibility issue.
                    returned: on success
                    type: str
                    sample: NOT_ENOUGH_DATA
                message:
                    description:
                        - Detailed description of the compatibility issue.
                    returned: on success
                    type: str
                    sample: message_example
        estimated_cost:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compute:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpu_per_hour:
                            description:
                                - OCPU per hour
                            returned: on success
                            type: float
                            sample: 10
                        ocpu_per_hour_by_subscription:
                            description:
                                - OCPU per hour by subscription
                            returned: on success
                            type: float
                            sample: 10
                        memory_gb_per_hour:
                            description:
                                - Gigabyte per hour
                            returned: on success
                            type: float
                            sample: 10
                        memory_gb_per_hour_by_subscription:
                            description:
                                - Gigabyte per hour by subscription
                            returned: on success
                            type: float
                            sample: 10
                        gpu_per_hour:
                            description:
                                - GPU per hour
                            returned: on success
                            type: float
                            sample: 10
                        gpu_per_hour_by_subscription:
                            description:
                                - GPU per hour by subscription
                            returned: on success
                            type: float
                            sample: 10
                        total_per_hour:
                            description:
                                - Total per hour
                            returned: on success
                            type: float
                            sample: 10
                        total_per_hour_by_subscription:
                            description:
                                - Total usage per hour by subscription
                            returned: on success
                            type: float
                            sample: 10
                        ocpu_count:
                            description:
                                - Total number of OCPUs
                            returned: on success
                            type: float
                            sample: 10
                        memory_amount_gb:
                            description:
                                - Total usage of memory
                            returned: on success
                            type: float
                            sample: 10
                        gpu_count:
                            description:
                                - Total number of GPU
                            returned: on success
                            type: float
                            sample: 10
                storage:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        volumes:
                            description:
                                - Volume estimation
                            returned: on success
                            type: complex
                            contains:
                                capacity_gb:
                                    description:
                                        - Gigabyte storage capacity
                                    returned: on success
                                    type: float
                                    sample: 10
                                description:
                                    description:
                                        - Volume description
                                    returned: on success
                                    type: str
                                    sample: description_example
                                total_gb_per_month:
                                    description:
                                        - Gigabyte storage capacity per month.
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_gb_per_month_by_subscription:
                                    description:
                                        - Gigabyte storage capacity per month by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                        total_gb_per_month:
                            description:
                                - Gigabyte storage capacity per month.
                            returned: on success
                            type: float
                            sample: 10
                        total_gb_per_month_by_subscription:
                            description:
                                - Gigabyte storage capacity per month by subscription.
                            returned: on success
                            type: float
                            sample: 10
                os_image:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        total_per_hour:
                            description:
                                - Total price per hour
                            returned: on success
                            type: float
                            sample: 10
                        total_per_hour_by_subscription:
                            description:
                                - Total price per hour by subscription
                            returned: on success
                            type: float
                            sample: 10
                currency_code:
                    description:
                        - Currency code in the ISO format.
                    returned: on success
                    type: str
                    sample: currency_code_example
                total_estimation_per_month:
                    description:
                        - Total estimation per month
                    returned: on success
                    type: float
                    sample: 10
                total_estimation_per_month_by_subscription:
                    description:
                        - Total estimation per month by subscription.
                    returned: on success
                    type: float
                    sample: 10
                subscription_id:
                    description:
                        - Subscription ID
                    returned: on success
                    type: str
                    sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when the target asset was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_updated:
            description:
                - The time when the target asset was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_assessed:
            description:
                - The time when the assessment was done. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        migration_asset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - Asset ID generated by mirgration service. It is used in the mirgration service pipeline.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The type of asset referenced for inventory.
                    returned: on success
                    type: str
                    sample: type_example
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                compartment_id:
                    description:
                        - Compartment Identifier
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the migration asset.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_created:
                    description:
                        - The time when the migration asset was created. An RFC3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The time when the migration asset was updated. An RFC3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                migration_id:
                    description:
                        - OCID of the associated migration.
                    returned: on success
                    type: str
                    sample: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
                snapshots:
                    description:
                        - "Key-value pair representing disks ID mapped to the OCIDs of replicated or hydration server volume snapshots.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: complex
                    contains:
                        uuid:
                            description:
                                - ID of the vCenter disk obtained from Inventory.
                            returned: on success
                            type: str
                            sample: uuid_example
                        volume_id:
                            description:
                                - ID of the hydration server volume
                            returned: on success
                            type: str
                            sample: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
                        volume_type:
                            description:
                                - The hydration server volume type
                            returned: on success
                            type: str
                            sample: BOOT
                        unmodified_volume_id:
                            description:
                                - ID of the unmodified volume
                            returned: on success
                            type: str
                            sample: "ocid1.unmodifiedvolume.oc1..xxxxxxEXAMPLExxxxxx"
                parent_snapshot:
                    description:
                        - The parent snapshot of the migration asset to be used by the replication task.
                    returned: on success
                    type: str
                    sample: parent_snapshot_example
                source_asset_data:
                    description:
                        - "Key-value pair representing asset metadata keys and values scoped to a namespace.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {}
                notifications:
                    description:
                        - List of notifications
                    returned: on success
                    type: list
                    sample: []
                source_asset_id:
                    description:
                        - OCID that is referenced to an asset for an inventory.
                    returned: on success
                    type: str
                    sample: "ocid1.sourceasset.oc1..xxxxxxEXAMPLExxxxxx"
                replication_schedule_id:
                    description:
                        - Replication schedule identifier
                    returned: on success
                    type: str
                    sample: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
                availability_domain:
                    description:
                        - Availability domain
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                replication_compartment_id:
                    description:
                        - Replication compartment identifier
                    returned: on success
                    type: str
                    sample: "ocid1.replicationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
                tenancy_id:
                    description:
                        - Tenancy identifier
                    returned: on success
                    type: str
                    sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
                snap_shot_bucket_name:
                    description:
                        - Name of snapshot bucket
                    returned: on success
                    type: str
                    sample: snap_shot_bucket_name_example
                depended_on_by:
                    description:
                        - List of migration assets that depend on the asset.
                    returned: on success
                    type: list
                    sample: []
                depends_on:
                    description:
                        - List of migration assets that depends on the asset.
                    returned: on success
                    type: list
                    sample: []
                snapshot_info:
                    description:
                        - The snapshot information.
                    returned: on success
                    type: str
                    sample: snapshot_info_example
    sample: [{
        "preferred_shape_type": "VM",
        "test_spec": {
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
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
                "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "display_name": "display_name_example",
            "fault_domain": "FAULT-DOMAIN-1",
            "freeform_tags": {'Department': 'Finance'},
            "hostname_label": "hostname_label_example",
            "ipxe_script": "ipxe_script_example",
            "instance_options": {
                "are_legacy_imds_endpoints_disabled": true
            },
            "preemptible_instance_config": {
                "preemption_action": {
                    "type": "TERMINATE",
                    "preserve_boot_volume": true
                }
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
            "shape": "shape_example",
            "shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4,
                "baseline_ocpu_utilization": "BASELINE_1_8"
            },
            "source_details": {
                "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
                "source_type": "bootVolume",
                "boot_volume_size_in_gbs": 56,
                "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                "boot_volume_vpus_per_gb": 56
            },
            "is_pv_encryption_in_transit_enabled": true
        },
        "block_volumes_performance": 56,
        "ms_license": "ms_license_example",
        "user_spec": {
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
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
                "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "display_name": "display_name_example",
            "fault_domain": "FAULT-DOMAIN-1",
            "freeform_tags": {'Department': 'Finance'},
            "hostname_label": "hostname_label_example",
            "ipxe_script": "ipxe_script_example",
            "instance_options": {
                "are_legacy_imds_endpoints_disabled": true
            },
            "preemptible_instance_config": {
                "preemption_action": {
                    "type": "TERMINATE",
                    "preserve_boot_volume": true
                }
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
            "shape": "shape_example",
            "shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4,
                "baseline_ocpu_utilization": "BASELINE_1_8"
            },
            "source_details": {
                "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
                "source_type": "bootVolume",
                "boot_volume_size_in_gbs": 56,
                "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                "boot_volume_vpus_per_gb": 56
            },
            "is_pv_encryption_in_transit_enabled": true
        },
        "recommended_spec": {
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
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
                "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "display_name": "display_name_example",
            "fault_domain": "FAULT-DOMAIN-1",
            "freeform_tags": {'Department': 'Finance'},
            "hostname_label": "hostname_label_example",
            "ipxe_script": "ipxe_script_example",
            "instance_options": {
                "are_legacy_imds_endpoints_disabled": true
            },
            "preemptible_instance_config": {
                "preemption_action": {
                    "type": "TERMINATE",
                    "preserve_boot_volume": true
                }
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
            "shape": "shape_example",
            "shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4,
                "baseline_ocpu_utilization": "BASELINE_1_8"
            },
            "source_details": {
                "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
                "source_type": "bootVolume",
                "boot_volume_size_in_gbs": 56,
                "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
                "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
                "boot_volume_vpus_per_gb": 56
            },
            "is_pv_encryption_in_transit_enabled": true
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "migration_plan_id": "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_resource_id": "ocid1.createdresource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "INSTANCE",
        "is_excluded_from_execution": true,
        "compatibility_messages": [{
            "severity": "ERROR",
            "name": "NOT_ENOUGH_DATA",
            "message": "message_example"
        }],
        "estimated_cost": {
            "compute": {
                "ocpu_per_hour": 10,
                "ocpu_per_hour_by_subscription": 10,
                "memory_gb_per_hour": 10,
                "memory_gb_per_hour_by_subscription": 10,
                "gpu_per_hour": 10,
                "gpu_per_hour_by_subscription": 10,
                "total_per_hour": 10,
                "total_per_hour_by_subscription": 10,
                "ocpu_count": 10,
                "memory_amount_gb": 10,
                "gpu_count": 10
            },
            "storage": {
                "volumes": [{
                    "capacity_gb": 10,
                    "description": "description_example",
                    "total_gb_per_month": 10,
                    "total_gb_per_month_by_subscription": 10
                }],
                "total_gb_per_month": 10,
                "total_gb_per_month_by_subscription": 10
            },
            "os_image": {
                "total_per_hour": 10,
                "total_per_hour_by_subscription": 10
            },
            "currency_code": "currency_code_example",
            "total_estimation_per_month": 10,
            "total_estimation_per_month_by_subscription": 10,
            "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_assessed": "2013-10-20T19:20:30+01:00",
        "migration_asset": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "type_example",
            "display_name": "display_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "migration_id": "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx",
            "snapshots": {
                "uuid": "uuid_example",
                "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx",
                "volume_type": "BOOT",
                "unmodified_volume_id": "ocid1.unmodifiedvolume.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "parent_snapshot": "parent_snapshot_example",
            "source_asset_data": {},
            "notifications": [],
            "source_asset_id": "ocid1.sourceasset.oc1..xxxxxxEXAMPLExxxxxx",
            "replication_schedule_id": "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx",
            "availability_domain": "Uocm:PHX-AD-1",
            "replication_compartment_id": "ocid1.replicationcompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
            "snap_shot_bucket_name": "snap_shot_bucket_name_example",
            "depended_on_by": [],
            "depends_on": [],
            "snapshot_info": "snapshot_info_example"
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_migrations import MigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetAssetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "target_asset_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_asset,
            target_asset_id=self.module.params.get("target_asset_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "migration_plan_id",
            "display_name",
            "target_asset_id",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_target_assets, **optional_kwargs
        )


TargetAssetFactsHelperCustom = get_custom_class("TargetAssetFactsHelperCustom")


class ResourceFactsHelper(TargetAssetFactsHelperCustom, TargetAssetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            migration_plan_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            target_asset_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "NEEDS_ATTENTION",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="target_asset",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(target_assets=result)


if __name__ == "__main__":
    main()
