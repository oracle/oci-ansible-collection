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
module: oci_cloud_bridge_asset_facts
short_description: Fetches details about one or multiple Asset resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Asset resources in Oracle Cloud Infrastructure
    - Returns a list of assets.
    - If I(asset_id) is specified, the details of a single Asset will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple assets.
        type: str
    lifecycle_state:
        description:
            - A filter to return only assets whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    source_key:
        description:
            - Source key from where the assets originate.
        type: str
    external_asset_key:
        description:
            - External asset key.
        type: str
    asset_type:
        description:
            - The type of asset.
        type: str
        choices:
            - "VMWARE_VM"
            - "VM"
    asset_id:
        description:
            - Unique asset identifier.
            - Required to get a specific asset.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "displayName"
    inventory_id:
        description:
            - Unique Inventory identifier.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific asset
  oci_cloud_bridge_asset_facts:
    # required
    asset_id: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"

- name: List assets
  oci_cloud_bridge_asset_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    source_key: source_key_example
    external_asset_key: external_asset_key_example
    asset_type: VMWARE_VM
    asset_id: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated
    inventory_id: "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
assets:
    description:
        - List of Asset resources
    returned: on success
    type: complex
    contains:
        compute:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
    sample: [{
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
        },
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
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import InventoryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "asset_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset, asset_id=self.module.params.get("asset_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "source_key",
            "external_asset_key",
            "asset_type",
            "asset_id",
            "display_name",
            "sort_order",
            "sort_by",
            "inventory_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_assets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AssetFactsHelperCustom = get_custom_class("AssetFactsHelperCustom")


class ResourceFactsHelper(AssetFactsHelperCustom, AssetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            source_key=dict(type="str", no_log=True),
            external_asset_key=dict(type="str", no_log=True),
            asset_type=dict(type="str", choices=["VMWARE_VM", "VM"]),
            asset_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "displayName"]
            ),
            inventory_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="asset",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(assets=result)


if __name__ == "__main__":
    main()
