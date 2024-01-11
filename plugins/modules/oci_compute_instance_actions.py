#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_compute_instance_actions
short_description: Perform actions on an Instance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Instance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an instance into a different compartment within the same tenancy. For information about
      moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - When you move an instance to a different compartment, associated resources such as boot volumes and VNICs
      are not moved.
    - "For I(action=instance_action), performs one of the following power actions on the specified instance:"
    - "- **START** - Powers on the instance."
    - "- **STOP** - Powers off the instance."
    - "- **RESET** - Powers off the instance and then powers it back on."
    - "- **SOFTSTOP** - Gracefully shuts down the instance by sending a shutdown command to the operating system.
      After waiting 15 minutes for the OS to shut down, the instance is powered off.
      If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting
      in data corruption. To avoid this, manually shut down the instance using the commands available in the OS before you softstop the
      instance."
    - "- **SOFTRESET** - Gracefully reboots the instance by sending a shutdown command to the operating system.
      After waiting 15 minutes for the OS to shut down, the instance is powered off and
      then powered back on."
    - "- **SENDDIAGNOSTICINTERRUPT** - For advanced users. **Caution: Sending a diagnostic interrupt to a live system can
      cause data corruption or system failure.** Sends a diagnostic interrupt that causes the instance's
      OS to crash and then reboot. Before you send a diagnostic interrupt, you must configure the instance to generate a
      crash dump file when it crashes. The crash dump captures information about the state of the OS at the time of
      the crash. After the OS restarts, you can analyze the crash dump to diagnose the issue. For more information, see
      L(Sending a Diagnostic Interrupt,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm)."
    - "- **DIAGNOSTICREBOOT** - Powers off the instance, rebuilds it, and then powers it back on.
      Before you send a diagnostic reboot, restart the instance's OS, confirm that the instance and networking settings are configured
      correctly, and try other L(troubleshooting steps,https://docs.cloud.oracle.com/iaas/Content/Compute/References/troubleshooting-compute-instances.htm).
      Use diagnostic reboot as a final attempt to troubleshoot an unreachable instance. For virtual machine (VM) instances only.
      For more information, see L(Performing a Diagnostic Reboot,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/diagnostic-reboot.htm)."
    - "- **REBOOTMIGRATE** - Powers off the instance, moves it to new hardware, and then powers it back on. For more information, see
      L(Infrastructure Maintenance,https://docs.cloud.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm)."
    - For more information about managing instance lifecycle states, see
      L(Stopping and Starting an Instance,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the instance to.
            - Required for I(action=change_compartment).
        type: str
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Instance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "stop"
            - "start"
            - "softreset"
            - "reset"
            - "softstop"
            - "senddiagnosticinterrupt"
            - "diagnosticreboot"
            - "rebootmigrate"
    delete_local_storage:
        description:
            - For bare metal instances that have local storage, this must be set to true to verify that the local storage
              will be deleted during the migration.  For instances without, this parameter has no effect.
            - Applicable only for I(action=instance_action).
            - Applicable when action_type is 'rebootMigrate'
        type: bool
    time_scheduled:
        description:
            - If present, this parameter will set (or reset) the scheduled time that the instance will be reboot
              migrated in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).  This will also change
              the `timeMaintenanceRebootDue` field on the instance.
            - If not present, the reboot migration will be triggered immediately.
            - Applicable only for I(action=instance_action).
            - Applicable when action_type is 'rebootMigrate'
        type: str
    action_type:
        description:
            - The type of power action to perform.
            - Required for I(action=instance_action).
        type: str
        choices:
            - "reset"
            - "rebootMigrate"
            - "softreset"
    allow_dense_reboot_migration:
        description:
            - For instances that use a DenseIO shape, the flag denoting whether
              L(reboot migration,https://docs.cloud.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm#reboot)
              is performed for the instance. The default value is `false`.
            - If the instance has a date in the Maintenance reboot field and you do nothing (or set this flag to `false`), the instance
              will be rebuilt at the scheduled maintenance time. The instance will experience 2-6 hours of downtime during the
              maintenance process. The local NVMe-based SSD will be preserved.
            - If you want to minimize downtime and can delete the SSD, you can set this flag to `true` and proactively reboot the
              instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be
              deleted. A short downtime occurs during the migration.
            - "**Caution:** When `true`, the SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding."
            - Applicable only for I(action=instance_action).
            - Applicable when action_type is one of ['softreset', 'reset']
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on instance
  oci_compute_instance_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action stop on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action stop on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action stop on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action start on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action start on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action start on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action softreset on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action softreset on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action softreset on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action reset on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action reset on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action reset on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action softstop on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action softstop on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action softstop on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action senddiagnosticinterrupt on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action senddiagnosticinterrupt on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action senddiagnosticinterrupt on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action diagnosticreboot on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action diagnosticreboot on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action diagnosticreboot on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action rebootmigrate on instance with action_type = reset
  oci_compute_instance_actions:
    # required
    action_type: reset

    # optional
    allow_dense_reboot_migration: true

- name: Perform action rebootmigrate on instance with action_type = rebootMigrate
  oci_compute_instance_actions:
    # required
    action_type: rebootMigrate

    # optional
    delete_local_storage: true
    time_scheduled: time_scheduled_example

- name: Perform action rebootmigrate on instance with action_type = softreset
  oci_compute_instance_actions:
    # required
    action_type: softreset

    # optional
    allow_dense_reboot_migration: true

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
            type: str
            sample: Uocm:PHX-AD-1
        capacity_reservation_id:
            description:
                - The OCID of the compute capacity reservation this instance is launched under.
                  When this field contains an empty string or is null, the instance is not currently in a capacity reservation.
                  For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            returned: on success
            type: str
            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dedicated_vm_host_id:
            description:
                - The OCID of the dedicated virtual machine host that the instance is placed on.
            returned: on success
            type: str
            sample: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
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
                - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality
                  as fields in the `metadata` object.
                - They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata`
                  fields are string/string maps only).
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
                - If you do not specify the fault domain, the system selects one for you.
                - "Example: `FAULT-DOMAIN-1`"
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        image_id:
            description:
                - Deprecated. Use `sourceDetails` instead.
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        ipxe_script:
            description:
                - When a bare metal or virtual machine
                  instance boots, the iPXE firmware that runs on the instance is
                  configured to run an iPXE script to continue the boot process.
                - If you want more control over the boot process, you can provide
                  your own custom iPXE script that will run when the instance boots.
                  Be aware that the same iPXE script will run
                  every time an instance boots, not only after the initial
                  LaunchInstance call.
                - "The default iPXE script connects to the instance's local boot
                  volume over iSCSI and performs a network boot. If you use a custom iPXE
                  script and want to network-boot from the instance's local boot volume
                  over iSCSI the same way as the default iPXE script, use the
                  following iSCSI IP address: 169.254.0.2, and boot volume IQN:
                  iqn.2015-02.oracle.boot."
                - If your instance boot volume attachment type is paravirtualized,
                  the boot volume is attached to the instance through virtio-scsi and no iPXE script is used.
                  If your instance boot volume attachment type is paravirtualized
                  and you use custom iPXE to network boot into your instance,
                  the primary boot volume is attached as a data volume through virtio-scsi drive.
                - For more information about the Bring Your Own Image feature of
                  Oracle Cloud Infrastructure, see
                  L(Bring Your Own Image,https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).
                - For more information about iPXE, see http://ipxe.org.
            returned: on success
            type: str
            sample: ipxe_script_example
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
                          L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/datatypes/LaunchInstanceDetails).
                    returned: on success
                    type: bool
                    sample: true
                is_consistent_volume_naming_enabled:
                    description:
                        - Whether to enable consistent volume naming feature. Defaults to false.
                    returned: on success
                    type: bool
                    sample: true
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
                is_live_migration_preferred:
                    description:
                        - Whether to live migrate supported VM instances to a healthy physical VM host without
                          disrupting running instances during infrastructure maintenance events. If null, Oracle
                          chooses the best option for migrating the VM during infrastructure maintenance events.
                    returned: on success
                    type: bool
                    sample: true
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
                                - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults
                                  to false if not specified.
                            returned: on success
                            type: bool
                            sample: true
        lifecycle_state:
            description:
                - The current state of the instance.
            returned: on success
            type: str
            sample: MOVING
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
            type: str
            sample: us-phoenix-1
        shape:
            description:
                - The shape of the instance. The shape determines the number of CPUs and the amount of memory
                  allocated to the instance. You can enumerate all available shapes by calling
                  L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
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
                          - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance."
                    returned: on success
                    type: str
                    sample: BASELINE_1_8
                processor_description:
                    description:
                        - A short description of the instance's processor (CPU).
                    returned: on success
                    type: str
                    sample: processor_description_example
                networking_bandwidth_in_gbps:
                    description:
                        - The networking bandwidth available to the instance, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
                max_vnic_attachments:
                    description:
                        - The maximum number of VNIC attachments for the instance.
                    returned: on success
                    type: int
                    sample: 56
                gpus:
                    description:
                        - The number of GPUs available to the instance.
                    returned: on success
                    type: int
                    sample: 56
                gpu_description:
                    description:
                        - A short description of the instance's graphics processing unit (GPU).
                        - If the instance does not have any GPUs, this field is `null`.
                    returned: on success
                    type: str
                    sample: gpu_description_example
                local_disks:
                    description:
                        - The number of local disks available to the instance.
                    returned: on success
                    type: int
                    sample: 56
                local_disks_total_size_in_gbs:
                    description:
                        - The aggregate size of all local disks, in gigabytes.
                        - If the instance does not have any local disks, this field is `null`.
                    returned: on success
                    type: float
                    sample: 3.4
                local_disk_description:
                    description:
                        - A short description of the local disks available to this instance.
                        - If the instance does not have any local disks, this field is `null`.
                    returned: on success
                    type: str
                    sample: local_disk_description_example
                vcpus:
                    description:
                        - The total number of VCPUs available to the instance. This can be used instead of OCPUs,
                          in which case the actual number of OCPUs will be calculated based on this value
                          and the actual hardware. This must be a multiple of 2.
                    returned: on success
                    type: int
                    sample: 56
        is_cross_numa_node:
            description:
                - Whether the instance's OCPUs and memory are distributed across multiple NUMA nodes.
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
                        - The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 32,768 GB (32 TB).
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
                        - The OCID of the Vault service key to assign as the master encryption key for the boot volume.
                    returned: on success
                    type: str
                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                boot_volume_vpus_per_gb:
                    description:
                        - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                          representing the Block Volume service's elastic performance options.
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
                instance_source_image_filter_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        compartment_id:
                            description:
                                - The OCID of the compartment containing images to search
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        defined_tags_filter:
                            description:
                                - Filter based on these defined tags. Each key is predefined and scoped to a
                                  namespace. For more information, see L(Resource
                                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                            returned: on success
                            type: dict
                            sample: {}
                        operating_system:
                            description:
                                - The image's operating system.
                                - "Example: `Oracle Linux`"
                            returned: on success
                            type: str
                            sample: operating_system_example
                        operating_system_version:
                            description:
                                - The image's operating system version.
                                - "Example: `7.2`"
                            returned: on success
                            type: str
                            sample: operating_system_version_example
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The date and time the instance was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        agent_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_monitoring_disabled:
                    description:
                        - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the
                          monitoring plugins.
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
                        - Whether Oracle Cloud Agent can run all of the available plugins.
                          This includes the management and monitoring plugins.
                        - For more information about the available plugins, see
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
                                  L(Managing Plugins with Oracle Cloud Agent,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
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
        time_maintenance_reboot_due:
            description:
                - "The date and time the instance is expected to be stopped / started,  in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  After that time if instance hasn't been rebooted, Oracle will reboot the instance within 24 hours of the due time.
                  Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state.
                  Example: `2018-05-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                is_memory_encryption_enabled:
                    description:
                        - Whether the instance is a confidential instance. If this value is `true`, the instance is a confidential instance. The default value
                          is `false`.
                    returned: on success
                    type: bool
                    sample: true
        instance_configuration_id:
            description:
                - The OCID of the Instance Configuration used to source launch details for this instance. Any other fields supplied in the instance launch
                  request override the details stored in the Instance Configuration for this instance launch.
            returned: on success
            type: str
            sample: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "dedicated_vm_host_id": "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
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
        "instance_options": {
            "are_legacy_imds_endpoints_disabled": true
        },
        "availability_config": {
            "is_live_migration_preferred": true,
            "recovery_action": "RESTORE_INSTANCE"
        },
        "preemptible_instance_config": {
            "preemption_action": {
                "type": "TERMINATE",
                "preserve_boot_volume": true
            }
        },
        "lifecycle_state": "MOVING",
        "metadata": {},
        "region": "us-phoenix-1",
        "shape": "shape_example",
        "shape_config": {
            "ocpus": 3.4,
            "memory_in_gbs": 3.4,
            "baseline_ocpu_utilization": "BASELINE_1_8",
            "processor_description": "processor_description_example",
            "networking_bandwidth_in_gbps": 3.4,
            "max_vnic_attachments": 56,
            "gpus": 56,
            "gpu_description": "gpu_description_example",
            "local_disks": 56,
            "local_disks_total_size_in_gbs": 3.4,
            "local_disk_description": "local_disk_description_example",
            "vcpus": 56
        },
        "is_cross_numa_node": true,
        "source_details": {
            "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
            "source_type": "bootVolume",
            "boot_volume_size_in_gbs": 56,
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
            "boot_volume_vpus_per_gb": 56,
            "instance_source_image_filter_details": {
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "defined_tags_filter": {},
                "operating_system": "operating_system_example",
                "operating_system_version": "operating_system_version_example"
            }
        },
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "agent_config": {
            "is_monitoring_disabled": true,
            "is_management_disabled": true,
            "are_all_plugins_disabled": true,
            "plugins_config": [{
                "name": "name_example",
                "desired_state": "ENABLED"
            }]
        },
        "time_maintenance_reboot_due": "2013-10-20T19:20:30+01:00",
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
            "is_measured_boot_enabled": true,
            "is_memory_encryption_enabled": true
        },
        "instance_configuration_id": "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import ChangeInstanceCompartmentDetails
    from oci.core.models import InstancePowerActionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        instance_action
    """

    def __init__(self, *args, **kwargs):
        super(InstanceActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_id")

    def get_get_fn(self):
        return self.client.get_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance, instance_id=self.module.params.get("instance_id"),
        )

    def get_action_fn(self, action):
        action = action.lower()
        if action in [
            "stop",
            "start",
            "softreset",
            "reset",
            "softstop",
            "senddiagnosticinterrupt",
            "diagnosticreboot",
            "rebootmigrate",
        ]:
            self.module.params["action"] = action.upper()
            return getattr(self, "instance_action", None)
        return super(InstanceActionsHelperGen, self).get_action_fn(action)

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_id=self.module.params.get("instance_id"),
                change_instance_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def instance_action(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstancePowerActionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.instance_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_id=self.module.params.get("instance_id"),
                action=self.module.params.get("action"),
                instance_power_action_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


InstanceActionsHelperCustom = get_custom_class("InstanceActionsHelperCustom")


class ResourceHelper(InstanceActionsHelperCustom, InstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            instance_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "stop",
                    "start",
                    "softreset",
                    "reset",
                    "softstop",
                    "senddiagnosticinterrupt",
                    "diagnosticreboot",
                    "rebootmigrate",
                ],
            ),
            delete_local_storage=dict(type="bool"),
            time_scheduled=dict(type="str"),
            action_type=dict(
                type="str", choices=["reset", "rebootMigrate", "softreset"]
            ),
            allow_dense_reboot_migration=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
