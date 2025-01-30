#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_os_management_hub_managed_instance_group_actions
short_description: Perform actions on a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
    - For I(action=attach_managed_instances), adds managed instances to the specified managed instance group. After adding instances to the group, any operation
      applied to the group will be applied to all instances in the group.
    - For I(action=attach_software_sources), attaches software sources to the specified managed instance group. The software sources must be compatible with the
      type of instances in the group.
    - For I(action=change_compartment), moves the specified managed instance group to a different compartment within the same tenancy. For information about
      moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=detach_managed_instances), removes a managed instance from the specified managed instance group.
    - For I(action=detach_software_sources), detaches the specified software sources from a managed instance group.
    - For I(action=disable_module_stream), disables a module stream on a managed instance group. After the stream is disabled, you can no longer install the
      profiles contained by the stream.  Before removing the stream, you must remove all installed profiles for the stream by using the
      L(RemoveModuleStreamProfileFromManagedInstanceGroup,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/osmh/latest//ManagedInstanceGroup/RemoveModuleStreamProfileFromManagedInstanceGroup) operation.
    - For I(action=enable_module_stream), enables a module stream on a managed instance group.  After the stream is enabled, you can install a module stream
      profile. Enabling a stream that is already enabled will succeed.  Enabling a different stream for a module that already has a stream enabled results in an
      error. Instead, use the L(SwitchModuleStreamOnManagedInstanceGroup,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/SwitchModuleStreamOnManagedInstanceGroup) operation.
    - For I(action=install_module_stream_profile), installs a profile for an enabled module stream. If a module stream defines multiple profiles, you can
      install each one independently.
    - For I(action=install_packages), installs the specified packages on each managed instance in a managed instance group. The package must be compatible with
      the instances in the group.
    - For I(action=install_windows_updates), installs Windows updates on each managed instance in the managed instance group.
    - For I(action=manage_module_streams), enables or disables module streams and installs or removes module stream profiles. Once complete, the state of the
      modules, streams, and profiles will match the state indicated in the operation. See
      L(ManageModuleStreamsOnManagedInstanceGroupDetails,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/osmh/latest/datatypes/ManageModuleStreamsOnManagedInstanceGroupDetails) for more information.
      You can preform this operation as a dry run. For a dry run, the service evaluates the operation against the current module, stream, and profile state on
      the managed instance, but does not commit the changes. Instead, the service returns work request log or error entries indicating the impact of the
      operation.
    - For I(action=remove_module_stream_profile), removes a profile for a module stream that is installed on a managed instance group. Providing the module
      stream name (without specifying a profile name) removes all profiles that have been installed for the module stream.
    - For I(action=remove_packages), removes the specified packages from each managed instance in a managed instance group.
    - For I(action=switch_module_stream), enables a new stream for a module that already has a stream enabled.
      If any profiles or packages from the original module are installed,
      switching to a new stream will remove the existing packages and
      install their counterparts in the new stream.
    - For I(action=update_all_packages), updates all packages on each managed instance in the specified managed instance group.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the group to.
            - Required for I(action=change_compartment).
        type: str
    managed_instances:
        description:
            - List of managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) to attach to the group.
            - Required for I(action=attach_managed_instances), I(action=detach_managed_instances).
        type: list
        elements: str
    software_sources:
        description:
            - List of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) to attach to the group.
            - Required for I(action=attach_software_sources), I(action=detach_software_sources).
        type: list
        elements: str
    windows_update_types:
        description:
            - The type of Windows updates to be applied.
            - Required for I(action=install_windows_updates).
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "ALL"
    is_dry_run:
        description:
            - Indicates if this operation is a dry run or if the operation
              should be committed.  If set to true, the result of the operation
              will be evaluated but not committed.  If set to false, the
              operation is committed to the managed instance(s).  The default is
              false.
            - Applicable only for I(action=manage_module_streams).
        type: bool
    enable:
        description:
            - The set of module streams to enable.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module.
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module.
                type: str
                required: true
            software_source_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the module
                      stream.
                type: str
    disable:
        description:
            - The set of module streams to disable.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module.
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module.
                type: str
                required: true
            software_source_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the module
                      stream.
                type: str
    install:
        description:
            - The set of module stream profiles to install.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module.
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module.
                type: str
                required: true
            profile_name:
                description:
                    - The name of a profile of the specified module stream.
                type: str
                required: true
            software_source_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the module
                      stream.
                type: str
    remove:
        description:
            - The set of module stream profiles to remove.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module.
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module.
                type: str
                required: true
            profile_name:
                description:
                    - The name of a profile of the specified module stream.
                type: str
                required: true
            software_source_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the module
                      stream.
                type: str
    profile_name:
        description:
            - The name of a profile of the specified module stream.
            - Applicable only for I(action=install_module_stream_profile)I(action=remove_module_stream_profile).
        type: str
    package_names:
        description:
            - The list of package names.
            - Required for I(action=install_packages), I(action=remove_packages).
        type: list
        elements: str
    module_name:
        description:
            - The name of the module.
            - Required for I(action=disable_module_stream), I(action=enable_module_stream), I(action=install_module_stream_profile),
              I(action=remove_module_stream_profile), I(action=switch_module_stream).
        type: str
    stream_name:
        description:
            - The name of a stream of the specified module.
            - Required for I(action=switch_module_stream).
        type: str
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that provides the module stream
            - Applicable only for I(action=disable_module_stream)I(action=enable_module_stream)I(action=install_module_stream_profile)I(action=remove_module_str
              eam_profile)I(action=switch_module_stream).
        type: str
    managed_instance_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        type: str
        aliases: ["id"]
        required: true
    update_types:
        description:
            - The type of updates to be applied.
            - Applicable only for I(action=update_all_packages).
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "KSPLICE_KERNEL"
            - "KSPLICE_USERSPACE"
            - "ALL"
    work_request_details:
        description:
            - ""
            - Applicable only for I(action=attach_managed_instances)I(action=attach_software_sources)I(action=detach_software_sources)I(action=disable_module_st
              ream)I(action=enable_module_stream)I(action=install_module_stream_profile)I(action=install_packages)I(action=install_windows_updates)I(action=mana
              ge_module_streams)I(action=remove_module_stream_profile)I(action=remove_packages)I(action=switch_module_stream)I(action=update_all_packages).
        type: dict
        suboptions:
            display_name:
                description:
                    - A user-friendly name for the job. The name does not have to be unique. Avoid entering confidential information.
                type: str
                aliases: ["name"]
            description:
                description:
                    - User-specified information about the job. Avoid entering confidential information.
                type: str
    action:
        description:
            - The action to perform on the ManagedInstanceGroup.
        type: str
        required: true
        choices:
            - "attach_managed_instances"
            - "attach_software_sources"
            - "change_compartment"
            - "detach_managed_instances"
            - "detach_software_sources"
            - "disable_module_stream"
            - "enable_module_stream"
            - "install_module_stream_profile"
            - "install_packages"
            - "install_windows_updates"
            - "manage_module_streams"
            - "remove_module_stream_profile"
            - "remove_packages"
            - "switch_module_stream"
            - "update_all_packages"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_managed_instances on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    managed_instances: [ "managed_instances_example" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_managed_instances

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action attach_software_sources on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    software_sources: [ "software_sources_example" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_software_sources

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action change_compartment on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action detach_managed_instances on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    managed_instances: [ "managed_instances_example" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_managed_instances

- name: Perform action detach_software_sources on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    software_sources: [ "software_sources_example" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_software_sources

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action disable_module_stream on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    module_name: module_name_example
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_module_stream

    # optional
    stream_name: stream_name_example
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action enable_module_stream on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    module_name: module_name_example
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_module_stream

    # optional
    stream_name: stream_name_example
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action install_module_stream_profile on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    module_name: module_name_example
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_module_stream_profile

    # optional
    profile_name: profile_name_example
    stream_name: stream_name_example
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action install_packages on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    package_names: [ "package_names_example" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_packages

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action install_windows_updates on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    windows_update_types: [ "SECURITY" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_windows_updates

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action manage_module_streams on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: manage_module_streams

    # optional
    is_dry_run: true
    enable:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example

      # optional
      software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    disable:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example

      # optional
      software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    install:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example
      profile_name: profile_name_example

      # optional
      software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    remove:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example
      profile_name: profile_name_example

      # optional
      software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action remove_module_stream_profile on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    module_name: module_name_example
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_module_stream_profile

    # optional
    profile_name: profile_name_example
    stream_name: stream_name_example
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action remove_packages on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    package_names: [ "package_names_example" ]
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_packages

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action switch_module_stream on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    module_name: module_name_example
    stream_name: stream_name_example
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: switch_module_stream

    # optional
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action update_all_packages on managed_instance_group
  oci_os_management_hub_managed_instance_group_actions:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: update_all_packages

    # optional
    update_types: [ "SECURITY" ]
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

"""

RETURN = """
managed_instance_group:
    description:
        - Details of the ManagedInstanceGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the managed instance
                  group.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the managed instance group.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified information about the managed instance group.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The time the managed instance group was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_modified:
            description:
                - The time the managed instance group was last modified (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the managed instance group.
            returned: on success
            type: str
            sample: CREATING
        os_family:
            description:
                - The operating system type of the instances in the managed instance group.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        arch_type:
            description:
                - The CPU architecture of the instances in the managed instance group.
            returned: on success
            type: str
            sample: X86_64
        vendor_name:
            description:
                - The vendor of the operating system used by the managed instances in the group.
            returned: on success
            type: str
            sample: ORACLE
        software_source_ids:
            description:
                - The list of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that the managed instance
                  group will use.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        software_sources:
            description:
                - The list of software sources that the managed instance group will use.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        managed_instance_ids:
            description:
                - The list of managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) attached to the managed
                  instance group.
            returned: on success
            type: list
            sample: []
        managed_instance_count:
            description:
                - The number of managed instances in the group.
            returned: on success
            type: int
            sample: 56
        location:
            description:
                - The location of managed instances attached to the group.
            returned: on success
            type: str
            sample: ON_PREMISE
        pending_job_count:
            description:
                - The number of scheduled jobs pending against the managed instance group.
            returned: on success
            type: int
            sample: 56
        notification_topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Oracle Notifications service (ONS) topic. ONS
                  is the channel used to send notifications to the customer.
            returned: on success
            type: str
            sample: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_data_collection_authorized:
                    description:
                        - Indicates whether Autonomous Linux will collect crash files. This setting can be changed by the user.
                    returned: on success
                    type: bool
                    sample: true
                scheduled_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the restricted scheduled job associated
                          with this instance. This value cannot be deleted by the user.
                    returned: on success
                    type: str
                    sample: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        is_managed_by_autonomous_linux:
            description:
                - Indicates whether the Autonomous Linux service manages the group.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_modified": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "vendor_name": "ORACLE",
        "software_source_ids": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "managed_instance_ids": [],
        "managed_instance_count": 56,
        "location": "ON_PREMISE",
        "pending_job_count": 56,
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_settings": {
            "is_data_collection_authorized": true,
            "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_managed_by_autonomous_linux": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import ManagedInstanceGroupClient
    from oci.os_management_hub.models import (
        AttachManagedInstancesToManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        AttachSoftwareSourcesToManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        ChangeManagedInstanceGroupCompartmentDetails,
    )
    from oci.os_management_hub.models import (
        DetachManagedInstancesFromManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        DetachSoftwareSourcesFromManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        DisableModuleStreamOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        EnableModuleStreamOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        InstallModuleStreamProfileOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        InstallPackagesOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        InstallWindowsUpdatesOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        ManageModuleStreamsOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        RemoveModuleStreamProfileFromManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        RemovePackagesFromManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        SwitchModuleStreamOnManagedInstanceGroupDetails,
    )
    from oci.os_management_hub.models import (
        UpdateAllPackagesOnManagedInstanceGroupDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubManagedInstanceGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_managed_instances
        attach_software_sources
        change_compartment
        detach_managed_instances
        detach_software_sources
        disable_module_stream
        enable_module_stream
        install_module_stream_profile
        install_packages
        install_windows_updates
        manage_module_streams
        remove_module_stream_profile
        remove_packages
        switch_module_stream
        update_all_packages
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "managed_instance_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_group_id")

    def get_get_fn(self):
        return self.client.get_managed_instance_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance_group,
            managed_instance_group_id=self.module.params.get(
                "managed_instance_group_id"
            ),
        )

    def attach_managed_instances(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachManagedInstancesToManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_managed_instances_to_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                attach_managed_instances_to_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def attach_software_sources(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachSoftwareSourcesToManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_software_sources_to_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                attach_software_sources_to_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeManagedInstanceGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_managed_instance_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                change_managed_instance_group_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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

    def detach_managed_instances(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachManagedInstancesFromManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_managed_instances_from_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                detach_managed_instances_from_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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

    def detach_software_sources(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachSoftwareSourcesFromManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_software_sources_from_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                detach_software_sources_from_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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

    def disable_module_stream(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisableModuleStreamOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_module_stream_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                disable_module_stream_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_module_stream(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableModuleStreamOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_module_stream_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                enable_module_stream_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_module_stream_profile(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallModuleStreamProfileOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_module_stream_profile_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                install_module_stream_profile_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallPackagesOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_packages_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                install_packages_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_windows_updates(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallWindowsUpdatesOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_windows_updates_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                install_windows_updates_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def manage_module_streams(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ManageModuleStreamsOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.manage_module_streams_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                manage_module_streams_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_module_stream_profile(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveModuleStreamProfileFromManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_module_stream_profile_from_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                remove_module_stream_profile_from_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemovePackagesFromManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_packages_from_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                remove_packages_from_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def switch_module_stream(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SwitchModuleStreamOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switch_module_stream_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                switch_module_stream_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def update_all_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateAllPackagesOnManagedInstanceGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_all_packages_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                update_all_packages_on_managed_instance_group_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OsManagementHubManagedInstanceGroupActionsHelperCustom = get_custom_class(
    "OsManagementHubManagedInstanceGroupActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubManagedInstanceGroupActionsHelperCustom,
    OsManagementHubManagedInstanceGroupActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            managed_instances=dict(type="list", elements="str"),
            software_sources=dict(type="list", elements="str"),
            windows_update_types=dict(
                type="list",
                elements="str",
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", "ALL"],
            ),
            is_dry_run=dict(type="bool"),
            enable=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    software_source_id=dict(type="str"),
                ),
            ),
            disable=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    software_source_id=dict(type="str"),
                ),
            ),
            install=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    profile_name=dict(type="str", required=True),
                    software_source_id=dict(type="str"),
                ),
            ),
            remove=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    profile_name=dict(type="str", required=True),
                    software_source_id=dict(type="str"),
                ),
            ),
            profile_name=dict(type="str"),
            package_names=dict(type="list", elements="str"),
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            software_source_id=dict(type="str"),
            managed_instance_group_id=dict(aliases=["id"], type="str", required=True),
            update_types=dict(
                type="list",
                elements="str",
                choices=[
                    "SECURITY",
                    "BUGFIX",
                    "ENHANCEMENT",
                    "OTHER",
                    "KSPLICE_KERNEL",
                    "KSPLICE_USERSPACE",
                    "ALL",
                ],
            ),
            work_request_details=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    description=dict(type="str"),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_managed_instances",
                    "attach_software_sources",
                    "change_compartment",
                    "detach_managed_instances",
                    "detach_software_sources",
                    "disable_module_stream",
                    "enable_module_stream",
                    "install_module_stream_profile",
                    "install_packages",
                    "install_windows_updates",
                    "manage_module_streams",
                    "remove_module_stream_profile",
                    "remove_packages",
                    "switch_module_stream",
                    "update_all_packages",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance_group",
        service_client_class=ManagedInstanceGroupClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
