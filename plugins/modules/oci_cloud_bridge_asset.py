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
module: oci_cloud_bridge_asset
short_description: Manage an Asset resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Asset resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an asset.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_bridge_asset_actions) module: change_compartment, change_asset_tags."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    inventory_id:
        description:
            - Inventory ID to which an asset belongs.
            - Required for create using I(state=present).
            - Required when asset_type is 'VMWARE_VM'
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that the asset belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required when asset_type is 'VMWARE_VM'
        type: str
    source_key:
        description:
            - The source key to which the asset belongs.
            - Required for create using I(state=present).
            - Required when asset_type is 'VMWARE_VM'
        type: str
    external_asset_key:
        description:
            - The key of the asset from the external environment.
            - Required for create using I(state=present).
            - Required when asset_type is 'VMWARE_VM'
        type: str
    display_name:
        description:
            - Asset display name.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    asset_type:
        description:
            - The type of asset.
            - Required for create using I(state=present), update using I(state=present) with asset_id present.
        type: str
        choices:
            - "VMWARE_VM"
            - "VM"
    asset_source_ids:
        description:
            - List of asset source OCID.
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
              predefined name, type, or namespace/scope. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    compute:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when asset_type is 'VMWARE_VM'
        type: dict
        suboptions:
            primary_ip:
                description:
                    - Primary IP address of the compute instance.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            dns_name:
                description:
                    - Fully Qualified DNS Name.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            description:
                description:
                    - Information about the asset.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            cores_count:
                description:
                    - Number of CPUs.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            cpu_model:
                description:
                    - CPU model name.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            gpu_devices_count:
                description:
                    - Number of GPU devices.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            gpu_devices:
                description:
                    - List of GPU devices attached to a virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - GPU device name.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    description:
                        description:
                            - GPU device description.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    cores_count:
                        description:
                            - Number of GPU cores.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
                    memory_in_mbs:
                        description:
                            - GPU memory size in MBs.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
                    manufacturer:
                        description:
                            - The manufacturer of GPU.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
            threads_per_core_count:
                description:
                    - Number of threads per core.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            memory_in_mbs:
                description:
                    - Memory size in MBs.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            is_pmem_enabled:
                description:
                    - Whether Pmem is enabled. Decides if NVDIMMs are used as a permanent memory.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: bool
            pmem_in_mbs:
                description:
                    - Pmem size in MBs.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            operating_system:
                description:
                    - Operating system.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            operating_system_version:
                description:
                    - Operating system version.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            host_name:
                description:
                    - Host name of the VM.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            power_state:
                description:
                    - The current power state of the virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            guest_state:
                description:
                    - Guest state.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            is_tpm_enabled:
                description:
                    - Whether Trusted Platform Module (TPM) is enabled.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: bool
            connected_networks:
                description:
                    - Number of connected networks.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            nics_count:
                description:
                    - Number of network ethernet cards.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            nics:
                description:
                    - List of network ethernet cards attached to a virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: list
                elements: dict
                suboptions:
                    label:
                        description:
                            - Provides a label and summary information for the device.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    switch_name:
                        description:
                            - Switch name.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    mac_address:
                        description:
                            - Mac address of the VM.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    mac_address_type:
                        description:
                            - Mac address type.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    network_name:
                        description:
                            - Network name.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    ip_addresses:
                        description:
                            - List of IP addresses.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: list
                        elements: str
            storage_provisioned_in_mbs:
                description:
                    - Provision storage size in MBs.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            disks_count:
                description:
                    - Number of disks.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            disks:
                description:
                    - Lists the set of disks belonging to the virtual machine. This list is unordered.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Disk name.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    boot_order:
                        description:
                            - Order of boot volumes.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
                    uuid:
                        description:
                            - Disk UUID for the virtual disk, if available.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    uuid_lun:
                        description:
                            - Disk UUID LUN for the virtual disk, if available.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    size_in_mbs:
                        description:
                            - The size of the volume in MBs.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
                    location:
                        description:
                            - Location of the boot/data volume.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    persistent_mode:
                        description:
                            - The disk persistent mode.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
            firmware:
                description:
                    - Information about firmware type for this virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            latency_sensitivity:
                description:
                    - Latency sensitivity.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            nvdimms:
                description:
                    - The properties of the NVDIMMs attached to a virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: list
                elements: dict
                suboptions:
                    label:
                        description:
                            - Provides a label and summary information for the device.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    unit_number:
                        description:
                            - The unit number of NVDIMM.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
                    controller_key:
                        description:
                            - Controller key.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
            nvdimm_controller:
                description:
                    - ""
                    - Applicable when asset_type is 'VMWARE_VM'
                type: dict
                suboptions:
                    label:
                        description:
                            - Provides a label and summary information for the device.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    bus_number:
                        description:
                            - Bus number.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
            scsi_controller:
                description:
                    - ""
                    - Applicable when asset_type is 'VMWARE_VM'
                type: dict
                suboptions:
                    label:
                        description:
                            - Provides a label and summary information for the device.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    unit_number:
                        description:
                            - The unit number of the SCSI controller.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: int
                    shared_bus:
                        description:
                            - Shared bus.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
            hardware_version:
                description:
                    - Hardware version.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
    vm:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when asset_type is 'VMWARE_VM'
        type: dict
        suboptions:
            hypervisor_vendor:
                description:
                    - Hypervisor vendor.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            hypervisor_version:
                description:
                    - Hypervisor version.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            hypervisor_host:
                description:
                    - Host name/IP address of VM on which the host is running.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
    vmware_vm:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when asset_type is 'VMWARE_VM'
        type: dict
        suboptions:
            cluster:
                description:
                    - Cluster name.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            customer_fields:
                description:
                    - Customer fields.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: list
                elements: str
            customer_tags:
                description:
                    - Customer defined tags.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The tag name.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
                    description:
                        description:
                            - The tag description.
                            - Applicable when asset_type is 'VMWARE_VM'
                        type: str
            instance_uuid:
                description:
                    - vCenter-specific identifier of the virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            path:
                description:
                    - Path directory of the asset.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            vmware_tools_status:
                description:
                    - VMware tools status.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            is_disks_uuid_enabled:
                description:
                    - Whether changed block tracking for this VM's disk is active.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: bool
            is_disks_cbt_enabled:
                description:
                    - Indicates that change tracking is supported for virtual disks of this virtual machine.
                      However, even if change tracking is supported, it might not be available for all disks of the virtual machine.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: bool
            fault_tolerance_state:
                description:
                    - Fault tolerance state.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            fault_tolerance_bandwidth:
                description:
                    - Fault tolerance bandwidth.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
            fault_tolerance_secondary_latency:
                description:
                    - Fault tolerance to secondary latency.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: int
    vmware_v_center:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when asset_type is 'VMWARE_VM'
        type: dict
        suboptions:
            vcenter_key:
                description:
                    - vCenter unique key.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            vcenter_version:
                description:
                    - Dot-separated version string.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
            data_center:
                description:
                    - Data center name.
                    - Applicable when asset_type is 'VMWARE_VM'
                type: str
    asset_id:
        description:
            - Unique asset identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Asset.
            - Use I(state=present) to create or update an Asset.
            - Use I(state=absent) to delete an Asset.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create asset with asset_type = VMWARE_VM
  oci_cloud_bridge_asset:
    # required
    inventory_id: "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source_key: source_key_example
    external_asset_key: external_asset_key_example
    asset_type: VMWARE_VM

    # optional
    display_name: display_name_example
    asset_source_ids: [ "asset_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compute:
      # optional
      primary_ip: primary_ip_example
      dns_name: dns_name_example
      description: description_example
      cores_count: 56
      cpu_model: cpu_model_example
      gpu_devices_count: 56
      gpu_devices:
      - # optional
        name: name_example
        description: description_example
        cores_count: 56
        memory_in_mbs: 56
        manufacturer: manufacturer_example
      threads_per_core_count: 56
      memory_in_mbs: 56
      is_pmem_enabled: true
      pmem_in_mbs: 56
      operating_system: operating_system_example
      operating_system_version: operating_system_version_example
      host_name: host_name_example
      power_state: power_state_example
      guest_state: guest_state_example
      is_tpm_enabled: true
      connected_networks: 56
      nics_count: 56
      nics:
      - # optional
        label: label_example
        switch_name: switch_name_example
        mac_address: mac_address_example
        mac_address_type: mac_address_type_example
        network_name: network_name_example
        ip_addresses: [ "ip_addresses_example" ]
      storage_provisioned_in_mbs: 56
      disks_count: 56
      disks:
      - # optional
        name: name_example
        boot_order: 56
        uuid: uuid_example
        uuid_lun: uuid_lun_example
        size_in_mbs: 56
        location: location_example
        persistent_mode: persistent_mode_example
      firmware: firmware_example
      latency_sensitivity: latency_sensitivity_example
      nvdimms:
      - # optional
        label: label_example
        unit_number: 56
        controller_key: 56
      nvdimm_controller:
        # optional
        label: label_example
        bus_number: 56
      scsi_controller:
        # optional
        label: label_example
        unit_number: 56
        shared_bus: shared_bus_example
      hardware_version: hardware_version_example
    vm:
      # optional
      hypervisor_vendor: hypervisor_vendor_example
      hypervisor_version: hypervisor_version_example
      hypervisor_host: hypervisor_host_example
    vmware_vm:
      # optional
      cluster: cluster_example
      customer_fields: [ "customer_fields_example" ]
      customer_tags:
      - # optional
        name: name_example
        description: description_example
      instance_uuid: instance_uuid_example
      path: path_example
      vmware_tools_status: vmware_tools_status_example
      is_disks_uuid_enabled: true
      is_disks_cbt_enabled: true
      fault_tolerance_state: fault_tolerance_state_example
      fault_tolerance_bandwidth: 56
      fault_tolerance_secondary_latency: 56
    vmware_v_center:
      # optional
      vcenter_key: vcenter_key_example
      vcenter_version: vcenter_version_example
      data_center: data_center_example

- name: Create asset with asset_type = VM
  oci_cloud_bridge_asset:
    # required
    asset_type: VM

    # optional
    display_name: display_name_example
    asset_source_ids: [ "asset_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update asset with asset_type = VMWARE_VM
  oci_cloud_bridge_asset:
    # required
    asset_type: VMWARE_VM

    # optional
    display_name: display_name_example
    asset_source_ids: [ "asset_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compute:
      # optional
      primary_ip: primary_ip_example
      dns_name: dns_name_example
      description: description_example
      cores_count: 56
      cpu_model: cpu_model_example
      gpu_devices_count: 56
      gpu_devices:
      - # optional
        name: name_example
        description: description_example
        cores_count: 56
        memory_in_mbs: 56
        manufacturer: manufacturer_example
      threads_per_core_count: 56
      memory_in_mbs: 56
      is_pmem_enabled: true
      pmem_in_mbs: 56
      operating_system: operating_system_example
      operating_system_version: operating_system_version_example
      host_name: host_name_example
      power_state: power_state_example
      guest_state: guest_state_example
      is_tpm_enabled: true
      connected_networks: 56
      nics_count: 56
      nics:
      - # optional
        label: label_example
        switch_name: switch_name_example
        mac_address: mac_address_example
        mac_address_type: mac_address_type_example
        network_name: network_name_example
        ip_addresses: [ "ip_addresses_example" ]
      storage_provisioned_in_mbs: 56
      disks_count: 56
      disks:
      - # optional
        name: name_example
        boot_order: 56
        uuid: uuid_example
        uuid_lun: uuid_lun_example
        size_in_mbs: 56
        location: location_example
        persistent_mode: persistent_mode_example
      firmware: firmware_example
      latency_sensitivity: latency_sensitivity_example
      nvdimms:
      - # optional
        label: label_example
        unit_number: 56
        controller_key: 56
      nvdimm_controller:
        # optional
        label: label_example
        bus_number: 56
      scsi_controller:
        # optional
        label: label_example
        unit_number: 56
        shared_bus: shared_bus_example
      hardware_version: hardware_version_example
    vm:
      # optional
      hypervisor_vendor: hypervisor_vendor_example
      hypervisor_version: hypervisor_version_example
      hypervisor_host: hypervisor_host_example
    vmware_vm:
      # optional
      cluster: cluster_example
      customer_fields: [ "customer_fields_example" ]
      customer_tags:
      - # optional
        name: name_example
        description: description_example
      instance_uuid: instance_uuid_example
      path: path_example
      vmware_tools_status: vmware_tools_status_example
      is_disks_uuid_enabled: true
      is_disks_cbt_enabled: true
      fault_tolerance_state: fault_tolerance_state_example
      fault_tolerance_bandwidth: 56
      fault_tolerance_secondary_latency: 56
    vmware_v_center:
      # optional
      vcenter_key: vcenter_key_example
      vcenter_version: vcenter_version_example
      data_center: data_center_example

- name: Update asset with asset_type = VM
  oci_cloud_bridge_asset:
    # required
    asset_type: VM

    # optional
    display_name: display_name_example
    asset_source_ids: [ "asset_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with asset_type = VMWARE_VM
  oci_cloud_bridge_asset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    asset_type: VMWARE_VM

    # optional
    display_name: display_name_example
    asset_source_ids: [ "asset_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compute:
      # optional
      primary_ip: primary_ip_example
      dns_name: dns_name_example
      description: description_example
      cores_count: 56
      cpu_model: cpu_model_example
      gpu_devices_count: 56
      gpu_devices:
      - # optional
        name: name_example
        description: description_example
        cores_count: 56
        memory_in_mbs: 56
        manufacturer: manufacturer_example
      threads_per_core_count: 56
      memory_in_mbs: 56
      is_pmem_enabled: true
      pmem_in_mbs: 56
      operating_system: operating_system_example
      operating_system_version: operating_system_version_example
      host_name: host_name_example
      power_state: power_state_example
      guest_state: guest_state_example
      is_tpm_enabled: true
      connected_networks: 56
      nics_count: 56
      nics:
      - # optional
        label: label_example
        switch_name: switch_name_example
        mac_address: mac_address_example
        mac_address_type: mac_address_type_example
        network_name: network_name_example
        ip_addresses: [ "ip_addresses_example" ]
      storage_provisioned_in_mbs: 56
      disks_count: 56
      disks:
      - # optional
        name: name_example
        boot_order: 56
        uuid: uuid_example
        uuid_lun: uuid_lun_example
        size_in_mbs: 56
        location: location_example
        persistent_mode: persistent_mode_example
      firmware: firmware_example
      latency_sensitivity: latency_sensitivity_example
      nvdimms:
      - # optional
        label: label_example
        unit_number: 56
        controller_key: 56
      nvdimm_controller:
        # optional
        label: label_example
        bus_number: 56
      scsi_controller:
        # optional
        label: label_example
        unit_number: 56
        shared_bus: shared_bus_example
      hardware_version: hardware_version_example
    vm:
      # optional
      hypervisor_vendor: hypervisor_vendor_example
      hypervisor_version: hypervisor_version_example
      hypervisor_host: hypervisor_host_example
    vmware_vm:
      # optional
      cluster: cluster_example
      customer_fields: [ "customer_fields_example" ]
      customer_tags:
      - # optional
        name: name_example
        description: description_example
      instance_uuid: instance_uuid_example
      path: path_example
      vmware_tools_status: vmware_tools_status_example
      is_disks_uuid_enabled: true
      is_disks_cbt_enabled: true
      fault_tolerance_state: fault_tolerance_state_example
      fault_tolerance_bandwidth: 56
      fault_tolerance_secondary_latency: 56
    vmware_v_center:
      # optional
      vcenter_key: vcenter_key_example
      vcenter_version: vcenter_version_example
      data_center: data_center_example

- name: Update asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with asset_type = VM
  oci_cloud_bridge_asset:
    # required
    asset_type: VM

    # optional
    display_name: display_name_example
    asset_source_ids: [ "asset_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete asset
  oci_cloud_bridge_asset:
    # required
    asset_id: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_bridge_asset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
asset:
    description:
        - Details of the Asset resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Asset display name.
            returned: on success
            type: str
            sample: display_name_example
        inventory_id:
            description:
                - Inventory ID to which an asset belongs to.
            returned: on success
            type: str
            sample: "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Asset OCID that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment to which an asset belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        source_key:
            description:
                - The source key that the asset belongs to.
            returned: on success
            type: str
            sample: source_key_example
        external_asset_key:
            description:
                - The key of the asset from the external environment.
            returned: on success
            type: str
            sample: external_asset_key_example
        asset_type:
            description:
                - The type of asset.
            returned: on success
            type: str
            sample: VMWARE_VM
        time_created:
            description:
                - The time when the asset was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the asset was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        asset_source_ids:
            description:
                - List of asset source OCID.
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The current state of the asset.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace/scope. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        compute:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                primary_ip:
                    description:
                        - Primary IP address of the compute instance.
                    returned: on success
                    type: str
                    sample: primary_ip_example
                dns_name:
                    description:
                        - Fully Qualified DNS Name.
                    returned: on success
                    type: str
                    sample: dns_name_example
                description:
                    description:
                        - Information about the asset.
                    returned: on success
                    type: str
                    sample: description_example
                cores_count:
                    description:
                        - Number of CPUs.
                    returned: on success
                    type: int
                    sample: 56
                cpu_model:
                    description:
                        - CPU model name.
                    returned: on success
                    type: str
                    sample: cpu_model_example
                gpu_devices_count:
                    description:
                        - Number of GPU devices.
                    returned: on success
                    type: int
                    sample: 56
                gpu_devices:
                    description:
                        - List of GPU devices attached to a virtual machine.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - GPU device name.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - GPU device description.
                            returned: on success
                            type: str
                            sample: description_example
                        cores_count:
                            description:
                                - Number of GPU cores.
                            returned: on success
                            type: int
                            sample: 56
                        memory_in_mbs:
                            description:
                                - GPU memory size in MBs.
                            returned: on success
                            type: int
                            sample: 56
                        manufacturer:
                            description:
                                - The manufacturer of GPU.
                            returned: on success
                            type: str
                            sample: manufacturer_example
                threads_per_core_count:
                    description:
                        - Number of threads per core.
                    returned: on success
                    type: int
                    sample: 56
                memory_in_mbs:
                    description:
                        - Memory size in MBs.
                    returned: on success
                    type: int
                    sample: 56
                is_pmem_enabled:
                    description:
                        - Whether Pmem is enabled. Decides if NVDIMMs are used as a permanent memory.
                    returned: on success
                    type: bool
                    sample: true
                pmem_in_mbs:
                    description:
                        - Pmem size in MBs.
                    returned: on success
                    type: int
                    sample: 56
                operating_system:
                    description:
                        - Operating system.
                    returned: on success
                    type: str
                    sample: operating_system_example
                operating_system_version:
                    description:
                        - Operating system version.
                    returned: on success
                    type: str
                    sample: operating_system_version_example
                host_name:
                    description:
                        - Host name of the VM.
                    returned: on success
                    type: str
                    sample: host_name_example
                power_state:
                    description:
                        - The current power state of the virtual machine.
                    returned: on success
                    type: str
                    sample: power_state_example
                guest_state:
                    description:
                        - Guest state.
                    returned: on success
                    type: str
                    sample: guest_state_example
                is_tpm_enabled:
                    description:
                        - Whether Trusted Platform Module (TPM) is enabled.
                    returned: on success
                    type: bool
                    sample: true
                connected_networks:
                    description:
                        - Number of connected networks.
                    returned: on success
                    type: int
                    sample: 56
                nics_count:
                    description:
                        - Number of network ethernet cards.
                    returned: on success
                    type: int
                    sample: 56
                nics:
                    description:
                        - List of network ethernet cards attached to a virtual machine.
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Provides a label and summary information for the device.
                            returned: on success
                            type: str
                            sample: label_example
                        switch_name:
                            description:
                                - Switch name.
                            returned: on success
                            type: str
                            sample: switch_name_example
                        mac_address:
                            description:
                                - Mac address of the VM.
                            returned: on success
                            type: str
                            sample: mac_address_example
                        mac_address_type:
                            description:
                                - Mac address type.
                            returned: on success
                            type: str
                            sample: mac_address_type_example
                        network_name:
                            description:
                                - Network name.
                            returned: on success
                            type: str
                            sample: network_name_example
                        ip_addresses:
                            description:
                                - List of IP addresses.
                            returned: on success
                            type: list
                            sample: []
                storage_provisioned_in_mbs:
                    description:
                        - Provision storage size in MBs.
                    returned: on success
                    type: int
                    sample: 56
                disks_count:
                    description:
                        - Number of disks.
                    returned: on success
                    type: int
                    sample: 56
                disks:
                    description:
                        - Lists the set of disks belonging to the virtual machine. This list is unordered.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Disk name.
                            returned: on success
                            type: str
                            sample: name_example
                        boot_order:
                            description:
                                - Order of boot volumes.
                            returned: on success
                            type: int
                            sample: 56
                        uuid:
                            description:
                                - Disk UUID for the virtual disk, if available.
                            returned: on success
                            type: str
                            sample: uuid_example
                        uuid_lun:
                            description:
                                - Disk UUID LUN for the virtual disk, if available.
                            returned: on success
                            type: str
                            sample: uuid_lun_example
                        size_in_mbs:
                            description:
                                - The size of the volume in MBs.
                            returned: on success
                            type: int
                            sample: 56
                        location:
                            description:
                                - Location of the boot/data volume.
                            returned: on success
                            type: str
                            sample: location_example
                        persistent_mode:
                            description:
                                - The disk persistent mode.
                            returned: on success
                            type: str
                            sample: persistent_mode_example
                firmware:
                    description:
                        - Information about firmware type for this virtual machine.
                    returned: on success
                    type: str
                    sample: firmware_example
                latency_sensitivity:
                    description:
                        - Latency sensitivity.
                    returned: on success
                    type: str
                    sample: latency_sensitivity_example
                nvdimms:
                    description:
                        - The properties of the NVDIMMs attached to a virtual machine.
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Provides a label and summary information for the device.
                            returned: on success
                            type: str
                            sample: label_example
                        unit_number:
                            description:
                                - The unit number of NVDIMM.
                            returned: on success
                            type: int
                            sample: 56
                        controller_key:
                            description:
                                - Controller key.
                            returned: on success
                            type: int
                            sample: 56
                nvdimm_controller:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Provides a label and summary information for the device.
                            returned: on success
                            type: str
                            sample: label_example
                        bus_number:
                            description:
                                - Bus number.
                            returned: on success
                            type: int
                            sample: 56
                scsi_controller:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Provides a label and summary information for the device.
                            returned: on success
                            type: str
                            sample: label_example
                        unit_number:
                            description:
                                - The unit number of the SCSI controller.
                            returned: on success
                            type: int
                            sample: 56
                        shared_bus:
                            description:
                                - Shared bus.
                            returned: on success
                            type: str
                            sample: shared_bus_example
                hardware_version:
                    description:
                        - Hardware version.
                    returned: on success
                    type: str
                    sample: hardware_version_example
        vm:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hypervisor_vendor:
                    description:
                        - Hypervisor vendor.
                    returned: on success
                    type: str
                    sample: hypervisor_vendor_example
                hypervisor_version:
                    description:
                        - Hypervisor version.
                    returned: on success
                    type: str
                    sample: hypervisor_version_example
                hypervisor_host:
                    description:
                        - Host name/IP address of VM on which the host is running.
                    returned: on success
                    type: str
                    sample: hypervisor_host_example
        vmware_vm:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                cluster:
                    description:
                        - Cluster name.
                    returned: on success
                    type: str
                    sample: cluster_example
                customer_fields:
                    description:
                        - Customer fields.
                    returned: on success
                    type: list
                    sample: []
                customer_tags:
                    description:
                        - Customer defined tags.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The tag name.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The tag description.
                            returned: on success
                            type: str
                            sample: description_example
                instance_uuid:
                    description:
                        - vCenter-specific identifier of the virtual machine.
                    returned: on success
                    type: str
                    sample: instance_uuid_example
                path:
                    description:
                        - Path directory of the asset.
                    returned: on success
                    type: str
                    sample: path_example
                vmware_tools_status:
                    description:
                        - VMware tools status.
                    returned: on success
                    type: str
                    sample: vmware_tools_status_example
                is_disks_uuid_enabled:
                    description:
                        - Whether changed block tracking for this VM's disk is active.
                    returned: on success
                    type: bool
                    sample: true
                is_disks_cbt_enabled:
                    description:
                        - Indicates that change tracking is supported for virtual disks of this virtual machine.
                          However, even if change tracking is supported, it might not be available for all disks of the virtual machine.
                    returned: on success
                    type: bool
                    sample: true
                fault_tolerance_state:
                    description:
                        - Fault tolerance state.
                    returned: on success
                    type: str
                    sample: fault_tolerance_state_example
                fault_tolerance_bandwidth:
                    description:
                        - Fault tolerance bandwidth.
                    returned: on success
                    type: int
                    sample: 56
                fault_tolerance_secondary_latency:
                    description:
                        - Fault tolerance to secondary latency.
                    returned: on success
                    type: int
                    sample: 56
        vmware_v_center:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                vcenter_key:
                    description:
                        - vCenter unique key.
                    returned: on success
                    type: str
                    sample: vcenter_key_example
                vcenter_version:
                    description:
                        - Dot-separated version string.
                    returned: on success
                    type: str
                    sample: vcenter_version_example
                data_center:
                    description:
                        - Data center name.
                    returned: on success
                    type: str
                    sample: data_center_example
    sample: {
        "display_name": "display_name_example",
        "inventory_id": "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "source_key": "source_key_example",
        "external_asset_key": "external_asset_key_example",
        "asset_type": "VMWARE_VM",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "asset_source_ids": [],
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "compute": {
            "primary_ip": "primary_ip_example",
            "dns_name": "dns_name_example",
            "description": "description_example",
            "cores_count": 56,
            "cpu_model": "cpu_model_example",
            "gpu_devices_count": 56,
            "gpu_devices": [{
                "name": "name_example",
                "description": "description_example",
                "cores_count": 56,
                "memory_in_mbs": 56,
                "manufacturer": "manufacturer_example"
            }],
            "threads_per_core_count": 56,
            "memory_in_mbs": 56,
            "is_pmem_enabled": true,
            "pmem_in_mbs": 56,
            "operating_system": "operating_system_example",
            "operating_system_version": "operating_system_version_example",
            "host_name": "host_name_example",
            "power_state": "power_state_example",
            "guest_state": "guest_state_example",
            "is_tpm_enabled": true,
            "connected_networks": 56,
            "nics_count": 56,
            "nics": [{
                "label": "label_example",
                "switch_name": "switch_name_example",
                "mac_address": "mac_address_example",
                "mac_address_type": "mac_address_type_example",
                "network_name": "network_name_example",
                "ip_addresses": []
            }],
            "storage_provisioned_in_mbs": 56,
            "disks_count": 56,
            "disks": [{
                "name": "name_example",
                "boot_order": 56,
                "uuid": "uuid_example",
                "uuid_lun": "uuid_lun_example",
                "size_in_mbs": 56,
                "location": "location_example",
                "persistent_mode": "persistent_mode_example"
            }],
            "firmware": "firmware_example",
            "latency_sensitivity": "latency_sensitivity_example",
            "nvdimms": [{
                "label": "label_example",
                "unit_number": 56,
                "controller_key": 56
            }],
            "nvdimm_controller": {
                "label": "label_example",
                "bus_number": 56
            },
            "scsi_controller": {
                "label": "label_example",
                "unit_number": 56,
                "shared_bus": "shared_bus_example"
            },
            "hardware_version": "hardware_version_example"
        },
        "vm": {
            "hypervisor_vendor": "hypervisor_vendor_example",
            "hypervisor_version": "hypervisor_version_example",
            "hypervisor_host": "hypervisor_host_example"
        },
        "vmware_vm": {
            "cluster": "cluster_example",
            "customer_fields": [],
            "customer_tags": [{
                "name": "name_example",
                "description": "description_example"
            }],
            "instance_uuid": "instance_uuid_example",
            "path": "path_example",
            "vmware_tools_status": "vmware_tools_status_example",
            "is_disks_uuid_enabled": true,
            "is_disks_cbt_enabled": true,
            "fault_tolerance_state": "fault_tolerance_state_example",
            "fault_tolerance_bandwidth": 56,
            "fault_tolerance_secondary_latency": 56
        },
        "vmware_v_center": {
            "vcenter_key": "vcenter_key_example",
            "vcenter_version": "vcenter_version_example",
            "data_center": "data_center_example"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import InventoryClient
    from oci.cloud_bridge.models import CreateAssetDetails
    from oci.cloud_bridge.models import UpdateAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AssetHelperGen, self).get_possible_entity_types() + [
            "ocbinventoryasset",
            "ocbinventoryassets",
            "cloudBridgeocbinventoryasset",
            "cloudBridgeocbinventoryassets",
            "ocbinventoryassetresource",
            "ocbinventoryassetsresource",
            "asset",
            "assets",
            "cloudBridgeasset",
            "cloudBridgeassets",
            "assetresource",
            "assetsresource",
            "cloudbridge",
        ]

    def get_module_resource_id_param(self):
        return "asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("asset_id")

    def get_get_fn(self):
        return self.client.get_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset, asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset, asset_id=self.module.params.get("asset_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            [
                "source_key",
                "external_asset_key",
                "asset_id",
                "display_name",
                "inventory_id",
            ]
            if self._use_name_as_identifier()
            else [
                "source_key",
                "external_asset_key",
                "asset_type",
                "asset_id",
                "display_name",
                "inventory_id",
            ]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_assets, **kwargs)

    def get_create_model_class(self):
        return CreateAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_asset_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                asset_id=self.module.params.get("asset_id"),
                update_asset_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(asset_id=self.module.params.get("asset_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AssetHelperCustom = get_custom_class("AssetHelperCustom")


class ResourceHelper(AssetHelperCustom, AssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            inventory_id=dict(type="str"),
            compartment_id=dict(type="str"),
            source_key=dict(type="str", no_log=True),
            external_asset_key=dict(type="str", no_log=True),
            display_name=dict(aliases=["name"], type="str"),
            asset_type=dict(type="str", choices=["VMWARE_VM", "VM"]),
            asset_source_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            compute=dict(
                type="dict",
                options=dict(
                    primary_ip=dict(type="str"),
                    dns_name=dict(type="str"),
                    description=dict(type="str"),
                    cores_count=dict(type="int"),
                    cpu_model=dict(type="str"),
                    gpu_devices_count=dict(type="int"),
                    gpu_devices=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str"),
                            description=dict(type="str"),
                            cores_count=dict(type="int"),
                            memory_in_mbs=dict(type="int"),
                            manufacturer=dict(type="str"),
                        ),
                    ),
                    threads_per_core_count=dict(type="int"),
                    memory_in_mbs=dict(type="int"),
                    is_pmem_enabled=dict(type="bool"),
                    pmem_in_mbs=dict(type="int"),
                    operating_system=dict(type="str"),
                    operating_system_version=dict(type="str"),
                    host_name=dict(type="str"),
                    power_state=dict(type="str"),
                    guest_state=dict(type="str"),
                    is_tpm_enabled=dict(type="bool"),
                    connected_networks=dict(type="int"),
                    nics_count=dict(type="int"),
                    nics=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            label=dict(type="str"),
                            switch_name=dict(type="str"),
                            mac_address=dict(type="str"),
                            mac_address_type=dict(type="str"),
                            network_name=dict(type="str"),
                            ip_addresses=dict(type="list", elements="str"),
                        ),
                    ),
                    storage_provisioned_in_mbs=dict(type="int"),
                    disks_count=dict(type="int"),
                    disks=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str"),
                            boot_order=dict(type="int"),
                            uuid=dict(type="str"),
                            uuid_lun=dict(type="str"),
                            size_in_mbs=dict(type="int"),
                            location=dict(type="str"),
                            persistent_mode=dict(type="str"),
                        ),
                    ),
                    firmware=dict(type="str"),
                    latency_sensitivity=dict(type="str"),
                    nvdimms=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            label=dict(type="str"),
                            unit_number=dict(type="int"),
                            controller_key=dict(type="int", no_log=True),
                        ),
                    ),
                    nvdimm_controller=dict(
                        type="dict",
                        options=dict(
                            label=dict(type="str"), bus_number=dict(type="int")
                        ),
                    ),
                    scsi_controller=dict(
                        type="dict",
                        options=dict(
                            label=dict(type="str"),
                            unit_number=dict(type="int"),
                            shared_bus=dict(type="str"),
                        ),
                    ),
                    hardware_version=dict(type="str"),
                ),
            ),
            vm=dict(
                type="dict",
                options=dict(
                    hypervisor_vendor=dict(type="str"),
                    hypervisor_version=dict(type="str"),
                    hypervisor_host=dict(type="str"),
                ),
            ),
            vmware_vm=dict(
                type="dict",
                options=dict(
                    cluster=dict(type="str"),
                    customer_fields=dict(type="list", elements="str"),
                    customer_tags=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str"), description=dict(type="str")
                        ),
                    ),
                    instance_uuid=dict(type="str"),
                    path=dict(type="str"),
                    vmware_tools_status=dict(type="str"),
                    is_disks_uuid_enabled=dict(type="bool"),
                    is_disks_cbt_enabled=dict(type="bool"),
                    fault_tolerance_state=dict(type="str"),
                    fault_tolerance_bandwidth=dict(type="int"),
                    fault_tolerance_secondary_latency=dict(type="int"),
                ),
            ),
            vmware_v_center=dict(
                type="dict",
                options=dict(
                    vcenter_key=dict(type="str", no_log=True),
                    vcenter_version=dict(type="str"),
                    data_center=dict(type="str"),
                ),
            ),
            asset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="asset",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
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
