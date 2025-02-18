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
module: oci_os_management_hub_managed_instance_actions
short_description: Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
    - For I(action=attach_profile), adds profile to a managed instance. After the profile has been added,
      the instance can be registered as a managed instance.
    - For I(action=attach_software_sources), adds software sources to a managed instance. After the software source has been added,
      then packages from that software source can be installed on the managed instance.
    - For I(action=detach_profile), detaches profile from a managed instance. After the profile has been removed,
      the instance cannot be registered as a managed instance.
    - For I(action=detach_software_sources), removes software sources from a managed instance.
      Packages will no longer be able to be installed from these software sources.
    - For I(action=disable_module_stream), disables a module stream on a managed instance.  After the stream is
      disabled, it is no longer possible to install the profiles that are
      contained by the stream.  All installed profiles must be removed prior
      to disabling a module stream.
    - For I(action=enable_module_stream), enables a module stream on a managed instance.  After the stream is
      enabled, it is possible to install the profiles that are contained
      by the stream.  Enabling a stream that is already enabled will
      succeed.  Attempting to enable a different stream for a module that
      already has a stream enabled results in an error.
    - For I(action=install_module_stream_profile), installs a profile for an module stream.  The stream must be
      enabled before a profile can be installed.  If a module stream
      defines multiple profiles, each one can be installed independently.
    - For I(action=install_packages), installs packages on a managed instance.
    - For I(action=install_windows_updates), installs Windows updates on the specified managed instance.
    - For I(action=manage_module_streams), enables or disables module streams and installs or removes module stream profiles. Once complete, the state of the
      modules, streams, and
      profiles will match the state indicated in the operation. See L(ManageModuleStreamsOnManagedInstanceDetails,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/osmh/latest/datatypes/ManageModuleStreamsOnManagedInstanceDetails)
      for more information. You can preform this operation as a dry run. For a dry run, the service evaluates the operation against the
      current module, stream, and profile state on the managed instance, but does not commit the changes. Instead, the service returns work request log or error
      entries indicating the impact of the operation.
    - For I(action=refresh_software), refreshes the package or Windows update information on a managed instance with the latest data from the software source.
      This does not update packages on the instance. It provides the service with the latest package data.
    - For I(action=remove_module_stream_profile), removes a profile for a module stream that is installed on a managed instance.
      If a module stream is provided, rather than a fully qualified profile, all
      profiles that have been installed for the module stream will be removed.
    - For I(action=remove_packages), removes an installed package from a managed instance.
    - For I(action=switch_module_stream), enables a new stream for a module that already has a stream enabled.
      If any profiles or packages from the original module are installed,
      switching to a new stream will remove the existing packages and
      install their counterparts in the new stream.
    - For I(action=update_packages), updates a package on a managed instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    profile_id:
        description:
            - The profile L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) to attach to the managed instance.
            - Required for I(action=attach_profile).
        type: str
    software_sources:
        description:
            - The list of software source OCIDs to be attached/detached.
            - Required for I(action=attach_software_sources), I(action=detach_software_sources).
        type: list
        elements: str
    windows_update_name:
        description:
            - "The list of Windows update unique identifiers.
              Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
              Example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'"
            - Applicable only for I(action=install_windows_updates).
        type: list
        elements: str
    windows_update_types:
        description:
            - The types of Windows updates to be installed.
            - Applicable only for I(action=install_windows_updates).
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
              operation is committed to the managed instance.  The default is
              false.
            - Applicable only for I(action=manage_module_streams).
        type: bool
    enable:
        description:
            - The set of module streams to enable. If any streams of a module are already enabled, the service switches from the current stream to the new
              stream.
              Once complete, the streams will be in 'ENABLED' status.
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
            - The set of module streams to disable. Any profiles that are installed for the module stream will be removed as part of the operation.
              Once complete, the streams will be in 'DISABLED' status.
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
            - The set of module stream profiles to install. Any packages that are part of the profile are installed on the managed instance.
              Once complete, the profile will be in 'INSTALLED' status. The operation will return an error if you attempt to install a profile from a disabled
              stream, unless enabling the new module stream is included in this operation.
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
            - The set of module stream profiles to remove. Once complete, the profile will be in 'AVAILABLE' status.
              The status of packages within the profile after the operation is complete is defined by the package manager on the managed instance group.
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
    module_name:
        description:
            - The name of a module.
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
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the module stream.
            - Applicable only for I(action=switch_module_stream).
        type: str
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
        type: str
        aliases: ["id"]
        required: true
    package_names:
        description:
            - The list of package names.
            - Required for I(action=install_packages), I(action=remove_packages).
        type: list
        elements: str
    update_types:
        description:
            - The types of updates to be applied.
            - Applicable only for I(action=update_packages).
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
            - Applicable only for I(action=attach_software_sources)I(action=detach_software_sources)I(action=disable_module_stream)I(action=enable_module_stream
              )I(action=install_module_stream_profile)I(action=install_packages)I(action=install_windows_updates)I(action=manage_module_streams)I(action=remove_
              module_stream_profile)I(action=remove_packages)I(action=switch_module_stream)I(action=update_packages).
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
            - The action to perform on the ManagedInstance.
        type: str
        required: true
        choices:
            - "attach_profile"
            - "attach_software_sources"
            - "detach_profile"
            - "detach_software_sources"
            - "disable_module_stream"
            - "enable_module_stream"
            - "install_module_stream_profile"
            - "install_packages"
            - "install_windows_updates"
            - "manage_module_streams"
            - "refresh_software"
            - "remove_module_stream_profile"
            - "remove_packages"
            - "switch_module_stream"
            - "update_packages"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_profile on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_profile

- name: Perform action attach_software_sources on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    software_sources: [ "software_sources_example" ]
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_software_sources

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action detach_profile on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_profile

- name: Perform action detach_software_sources on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    software_sources: [ "software_sources_example" ]
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_software_sources

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action disable_module_stream on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    module_name: module_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_module_stream

    # optional
    stream_name: stream_name_example
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action enable_module_stream on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    module_name: module_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_module_stream

    # optional
    stream_name: stream_name_example
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action install_module_stream_profile on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    module_name: module_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_module_stream_profile

    # optional
    profile_name: profile_name_example
    stream_name: stream_name_example
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action install_packages on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    package_names: [ "package_names_example" ]
    action: install_packages

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action install_windows_updates on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_windows_updates

    # optional
    windows_update_name: [ "windows_update_name_example" ]
    windows_update_types: [ "SECURITY" ]
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action manage_module_streams on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
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

- name: Perform action refresh_software on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: refresh_software

- name: Perform action remove_module_stream_profile on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    module_name: module_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_module_stream_profile

    # optional
    profile_name: profile_name_example
    stream_name: stream_name_example
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action remove_packages on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    package_names: [ "package_names_example" ]
    action: remove_packages

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action switch_module_stream on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    module_name: module_name_example
    stream_name: stream_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: switch_module_stream

    # optional
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

- name: Perform action update_packages on managed_instance
  oci_os_management_hub_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: update_packages

    # optional
    package_names: [ "package_names_example" ]
    update_types: [ "SECURITY" ]
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

"""

RETURN = """
managed_instance:
    description:
        - Details of the ManagedInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name for the managed instance.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified description for the managed instance.
            returned: on success
            type: str
            sample: description_example
        tenancy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy that the managed instance resides in.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the managed instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        location:
            description:
                - The location of the managed instance.
            returned: on success
            type: str
            sample: ON_PREMISE
        time_last_checkin:
            description:
                - Time that the instance last checked in with the service (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_boot:
            description:
                - Time that the instance last booted (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        os_name:
            description:
                - Operating system name.
            returned: on success
            type: str
            sample: os_name_example
        os_version:
            description:
                - Operating system version.
            returned: on success
            type: str
            sample: os_version_example
        os_kernel_version:
            description:
                - Operating system kernel version.
            returned: on success
            type: str
            sample: os_kernel_version_example
        ksplice_effective_kernel_version:
            description:
                - The ksplice effective kernel version.
            returned: on success
            type: str
            sample: ksplice_effective_kernel_version_example
        architecture:
            description:
                - The CPU architecture type of the managed instance.
            returned: on success
            type: str
            sample: X86_64
        os_family:
            description:
                - The operating system type of the managed instance.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        status:
            description:
                - Current status of the managed instance.
            returned: on success
            type: str
            sample: NORMAL
        profile:
            description:
                - The profile that was used to register this instance with the service.
            returned: on success
            type: str
            sample: profile_example
        is_management_station:
            description:
                - Indicates whether this managed instance is acting as an on-premises management station.
            returned: on success
            type: bool
            sample: true
        primary_management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
                  primary management station.
            returned: on success
            type: str
            sample: "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
        secondary_management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
                  secondary managment station.
            returned: on success
            type: str
            sample: "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
        software_sources:
            description:
                - The list of software sources currently attached to the managed instance.
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
        managed_instance_group:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_environment:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_stage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        is_reboot_required:
            description:
                - Indicates whether a reboot is required to complete installation of updates.
            returned: on success
            type: bool
            sample: true
        installed_packages:
            description:
                - Number of packages installed on the instance.
            returned: on success
            type: int
            sample: 56
        installed_windows_updates:
            description:
                - Number of Windows updates installed on the instance.
            returned: on success
            type: int
            sample: 56
        updates_available:
            description:
                - Number of updates available for installation.
            returned: on success
            type: int
            sample: 56
        security_updates_available:
            description:
                - Number of security type updates available for installation.
            returned: on success
            type: int
            sample: 56
        bug_updates_available:
            description:
                - Number of bug fix type updates available for installation.
            returned: on success
            type: int
            sample: 56
        enhancement_updates_available:
            description:
                - Number of enhancement type updates available for installation.
            returned: on success
            type: int
            sample: 56
        other_updates_available:
            description:
                - Number of non-classified (other) updates available for installation.
            returned: on success
            type: int
            sample: 56
        scheduled_job_count:
            description:
                - Number of scheduled jobs associated with this instance.
            returned: on success
            type: int
            sample: 56
        work_request_count:
            description:
                - Number of work requests associated with this instance.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the instance was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the instance was last updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                - Indicates whether the Autonomous Linux service manages the instance.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "location": "ON_PREMISE",
        "time_last_checkin": "2013-10-20T19:20:30+01:00",
        "time_last_boot": "2013-10-20T19:20:30+01:00",
        "os_name": "os_name_example",
        "os_version": "os_version_example",
        "os_kernel_version": "os_kernel_version_example",
        "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
        "architecture": "X86_64",
        "os_family": "ORACLE_LINUX_9",
        "status": "NORMAL",
        "profile": "profile_example",
        "is_management_station": true,
        "primary_management_station_id": "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "secondary_management_station_id": "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "managed_instance_group": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "lifecycle_environment": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "lifecycle_stage": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "is_reboot_required": true,
        "installed_packages": 56,
        "installed_windows_updates": 56,
        "updates_available": 56,
        "security_updates_available": 56,
        "bug_updates_available": 56,
        "enhancement_updates_available": 56,
        "other_updates_available": 56,
        "scheduled_job_count": 56,
        "work_request_count": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_settings": {
            "is_data_collection_authorized": true,
            "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_managed_by_autonomous_linux": true
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
    from oci.os_management_hub import ManagedInstanceClient
    from oci.os_management_hub.models import AttachProfileToManagedInstanceDetails
    from oci.os_management_hub.models import (
        AttachSoftwareSourcesToManagedInstanceDetails,
    )
    from oci.os_management_hub.models import (
        DetachSoftwareSourcesFromManagedInstanceDetails,
    )
    from oci.os_management_hub.models import DisableModuleStreamOnManagedInstanceDetails
    from oci.os_management_hub.models import EnableModuleStreamOnManagedInstanceDetails
    from oci.os_management_hub.models import (
        InstallModuleStreamProfileOnManagedInstanceDetails,
    )
    from oci.os_management_hub.models import InstallPackagesOnManagedInstanceDetails
    from oci.os_management_hub.models import (
        InstallWindowsUpdatesOnManagedInstanceDetails,
    )
    from oci.os_management_hub.models import ManageModuleStreamsOnManagedInstanceDetails
    from oci.os_management_hub.models import (
        RemoveModuleStreamProfileFromManagedInstanceDetails,
    )
    from oci.os_management_hub.models import RemovePackagesFromManagedInstanceDetails
    from oci.os_management_hub.models import SwitchModuleStreamOnManagedInstanceDetails
    from oci.os_management_hub.models import UpdatePackagesOnManagedInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubManagedInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_profile
        attach_software_sources
        detach_profile
        detach_software_sources
        disable_module_stream
        enable_module_stream
        install_module_stream_profile
        install_packages
        install_windows_updates
        manage_module_streams
        refresh_software
        remove_module_stream_profile
        remove_packages
        switch_module_stream
        update_packages
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "managed_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_id")

    def get_get_fn(self):
        return self.client.get_managed_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def attach_profile(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachProfileToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_profile_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_profile_to_managed_instance_details=action_details,
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

    def attach_software_sources(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachSoftwareSourcesToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_software_sources_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_software_sources_to_managed_instance_details=action_details,
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

    def detach_profile(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_profile_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
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
            self.module.params, DetachSoftwareSourcesFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_software_sources_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_software_sources_from_managed_instance_details=action_details,
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

    def disable_module_stream(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisableModuleStreamOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                disable_module_stream_on_managed_instance_details=action_details,
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
            self.module.params, EnableModuleStreamOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                enable_module_stream_on_managed_instance_details=action_details,
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
            self.module.params, InstallModuleStreamProfileOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_module_stream_profile_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                install_module_stream_profile_on_managed_instance_details=action_details,
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
            self.module.params, InstallPackagesOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_packages_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                install_packages_on_managed_instance_details=action_details,
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
            self.module.params, InstallWindowsUpdatesOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_windows_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                install_windows_updates_on_managed_instance_details=action_details,
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
            self.module.params, ManageModuleStreamsOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.manage_module_streams_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                manage_module_streams_on_managed_instance_details=action_details,
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

    def refresh_software(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_software_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
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
            self.module.params, RemoveModuleStreamProfileFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_module_stream_profile_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                remove_module_stream_profile_from_managed_instance_details=action_details,
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
            self.module.params, RemovePackagesFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_packages_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                remove_packages_from_managed_instance_details=action_details,
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
            self.module.params, SwitchModuleStreamOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switch_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                switch_module_stream_on_managed_instance_details=action_details,
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

    def update_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdatePackagesOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_packages_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_packages_on_managed_instance_details=action_details,
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


OsManagementHubManagedInstanceActionsHelperCustom = get_custom_class(
    "OsManagementHubManagedInstanceActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubManagedInstanceActionsHelperCustom,
    OsManagementHubManagedInstanceActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            profile_id=dict(type="str"),
            software_sources=dict(type="list", elements="str"),
            windows_update_name=dict(type="list", elements="str"),
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
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            software_source_id=dict(type="str"),
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            package_names=dict(type="list", elements="str"),
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
                    "attach_profile",
                    "attach_software_sources",
                    "detach_profile",
                    "detach_software_sources",
                    "disable_module_stream",
                    "enable_module_stream",
                    "install_module_stream_profile",
                    "install_packages",
                    "install_windows_updates",
                    "manage_module_streams",
                    "refresh_software",
                    "remove_module_stream_profile",
                    "remove_packages",
                    "switch_module_stream",
                    "update_packages",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
