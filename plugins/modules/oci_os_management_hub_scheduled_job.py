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
module: oci_os_management_hub_scheduled_job
short_description: Manage a ScheduledJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ScheduledJob resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new scheduled job.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_scheduled_job_actions) module: change_compartment,
      run_scheduled_job_now."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the scheduled job.
            - Required for create using I(state=present).
        type: str
    locations:
        description:
            - The list of locations this scheduled job should operate on for a job targeting on compartments. (Empty list means apply to all locations). This
              can only be set when managedCompartmentIds is not empty.
        type: list
        elements: str
    managed_instance_ids:
        description:
            - The managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
              A scheduled job can only operate on one type of target, therefore you must supply either this or
              managedInstanceGroupIds, or managedCompartmentIds, or lifecycleStageIds.
        type: list
        elements: str
    managed_instance_group_ids:
        description:
            - The managed instance group L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates
              on.
              A scheduled job can only operate on one type of target, therefore you must supply either this or managedInstanceIds,
              or managedCompartmentIds, or lifecycleStageIds.
        type: list
        elements: str
    managed_compartment_ids:
        description:
            - The compartment L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
              To apply the job to all compartments in the tenancy, set this to the tenancy OCID (root compartment) and set
              isSubcompartmentIncluded to true. A scheduled job can only operate on one type of target, therefore you must
              supply either this or managedInstanceIds, or managedInstanceGroupIds, or lifecycleStageIds.
        type: list
        elements: str
    lifecycle_stage_ids:
        description:
            - The lifecycle stage L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
              A scheduled job can only operate on one type of target, therefore you must supply either this or managedInstanceIds,
              or managedInstanceGroupIds, or managedCompartmentIds.
        type: list
        elements: str
    is_subcompartment_included:
        description:
            - Indicates whether to apply the scheduled job to all compartments in the tenancy when managedCompartmentIds specifies
              the tenancy L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) (root compartment).
        type: bool
    is_managed_by_autonomous_linux:
        description:
            - Indicates whether this scheduled job is managed by the Autonomous Linux service.
        type: bool
    display_name:
        description:
            - User-friendly name for the scheduled job. Does not have to be unique and you can change the name later. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-specified description of the scheduled job. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    schedule_type:
        description:
            - The type of scheduling frequency for the scheduled job.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "ONETIME"
            - "RECURRING"
    time_next_execution:
        description:
            - The desired time of the next execution of this scheduled job (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    recurring_rule:
        description:
            - The frequency schedule for a recurring scheduled job.
            - This parameter is updatable.
        type: str
    operations:
        description:
            - "The list of operations this scheduled job needs to perform.
              A scheduled job supports only one operation type, unless it is one of the following:
              * UPDATE_PACKAGES
              * UPDATE_ALL
              * UPDATE_SECURITY
              * UPDATE_BUGFIX
              * UPDATE_ENHANCEMENT
              * UPDATE_OTHER
              * UPDATE_KSPLICE_USERSPACE
              * UPDATE_KSPLICE_KERNEL"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            operation_type:
                description:
                    - The type of operation this scheduled job performs.
                type: str
                choices:
                    - "INSTALL_PACKAGES"
                    - "UPDATE_PACKAGES"
                    - "REMOVE_PACKAGES"
                    - "UPDATE_ALL"
                    - "UPDATE_SECURITY"
                    - "UPDATE_BUGFIX"
                    - "UPDATE_ENHANCEMENT"
                    - "UPDATE_OTHER"
                    - "UPDATE_KSPLICE_USERSPACE"
                    - "UPDATE_KSPLICE_KERNEL"
                    - "MANAGE_MODULE_STREAMS"
                    - "SWITCH_MODULE_STREAM"
                    - "ATTACH_SOFTWARE_SOURCES"
                    - "DETACH_SOFTWARE_SOURCES"
                    - "SYNC_MANAGEMENT_STATION_MIRROR"
                    - "PROMOTE_LIFECYCLE"
                    - "INSTALL_WINDOWS_UPDATES"
                    - "INSTALL_ALL_WINDOWS_UPDATES"
                    - "INSTALL_SECURITY_WINDOWS_UPDATES"
                    - "INSTALL_BUGFIX_WINDOWS_UPDATES"
                    - "INSTALL_ENHANCEMENT_WINDOWS_UPDATES"
                    - "INSTALL_OTHER_WINDOWS_UPDATES"
                required: true
            package_names:
                description:
                    - The names of the target packages. This parameter only applies when the scheduled job is for installing, updating, or removing packages.
                type: list
                elements: str
            windows_update_names:
                description:
                    - "Unique identifier for the Windows update. This parameter only applies if the scheduled job is for installing Windows updates.
                      Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
                      For example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'."
                type: list
                elements: str
            manage_module_streams_details:
                description:
                    - ""
                type: dict
                suboptions:
                    enable:
                        description:
                            - The set of module streams to enable.
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
                                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                      contains the module stream.
                                type: str
                    disable:
                        description:
                            - The set of module streams to disable.
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
                                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                      contains the module stream.
                                type: str
                    install:
                        description:
                            - The set of module stream profiles to install.
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
                                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                      contains the module stream.
                                type: str
                    remove:
                        description:
                            - The set of module stream profiles to remove.
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
                                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                      contains the module stream.
                                type: str
            switch_module_streams_details:
                description:
                    - ""
                type: dict
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
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the
                              module stream.
                        type: str
            software_source_ids:
                description:
                    - The software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
                      This parameter only applies when the scheduled job is for attaching or detaching software sources.
                type: list
                elements: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    retry_intervals:
        description:
            - The amount of time in minutes to wait until retrying the scheduled job. If set, the service will automatically
              retry a failed scheduled job after the interval. For example, you could set the interval to [2,5,10]. If the
              initial execution of the job fails, the service waits 2 minutes and then retries. If that fails, the service
              waits 5 minutes and then retries. If that fails, the service waits 10 minutes and then retries.
            - This parameter is updatable.
        type: list
        elements: int
    scheduled_job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ScheduledJob.
            - Use I(state=present) to create or update a ScheduledJob.
            - Use I(state=absent) to delete a ScheduledJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create scheduled_job
  oci_os_management_hub_scheduled_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    schedule_type: ONETIME
    time_next_execution: time_next_execution_example
    operations:
    - # required
      operation_type: INSTALL_PACKAGES

      # optional
      package_names: [ "package_names_example" ]
      windows_update_names: [ "windows_update_names_example" ]
      manage_module_streams_details:
        # optional
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
      switch_module_streams_details:
        # required
        module_name: module_name_example
        stream_name: stream_name_example

        # optional
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
      software_source_ids: [ "software_source_ids_example" ]

    # optional
    locations: [ "locations_example" ]
    managed_instance_ids: [ "managed_instance_ids_example" ]
    managed_instance_group_ids: [ "managed_instance_group_ids_example" ]
    managed_compartment_ids: [ "managed_compartment_ids_example" ]
    lifecycle_stage_ids: [ "lifecycle_stage_ids_example" ]
    is_subcompartment_included: true
    is_managed_by_autonomous_linux: true
    display_name: display_name_example
    description: description_example
    recurring_rule: recurring_rule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    retry_intervals: [ "retry_intervals_example" ]

- name: Update scheduled_job
  oci_os_management_hub_scheduled_job:
    # required
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    schedule_type: ONETIME
    time_next_execution: time_next_execution_example
    recurring_rule: recurring_rule_example
    operations:
    - # required
      operation_type: INSTALL_PACKAGES

      # optional
      package_names: [ "package_names_example" ]
      windows_update_names: [ "windows_update_names_example" ]
      manage_module_streams_details:
        # optional
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
      switch_module_streams_details:
        # required
        module_name: module_name_example
        stream_name: stream_name_example

        # optional
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
      software_source_ids: [ "software_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    retry_intervals: [ "retry_intervals_example" ]

- name: Update scheduled_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_scheduled_job:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    schedule_type: ONETIME
    time_next_execution: time_next_execution_example
    recurring_rule: recurring_rule_example
    operations:
    - # required
      operation_type: INSTALL_PACKAGES

      # optional
      package_names: [ "package_names_example" ]
      windows_update_names: [ "windows_update_names_example" ]
      manage_module_streams_details:
        # optional
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
      switch_module_streams_details:
        # required
        module_name: module_name_example
        stream_name: stream_name_example

        # optional
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
      software_source_ids: [ "software_source_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    retry_intervals: [ "retry_intervals_example" ]

- name: Delete scheduled_job
  oci_os_management_hub_scheduled_job:
    # required
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete scheduled_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_scheduled_job:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
scheduled_job:
    description:
        - Details of the ScheduledJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name for the scheduled job.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the scheduled job.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - User-specified description for the scheduled job.
            returned: on success
            type: str
            sample: description_example
        schedule_type:
            description:
                - The type of scheduling frequency for the job.
            returned: on success
            type: str
            sample: ONETIME
        locations:
            description:
                - The list of locations this scheduled job should operate on for a job targeting on compartments. (Empty list means apply to all locations).
                  This can only be set when managedCompartmentIds is not empty.
            returned: on success
            type: list
            sample: []
        time_next_execution:
            description:
                - The time of the next execution of this scheduled job (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_execution:
            description:
                - The time of the last execution of this scheduled job (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        recurring_rule:
            description:
                - The frequency schedule for a recurring scheduled job.
            returned: on success
            type: str
            sample: recurring_rule_example
        managed_instance_ids:
            description:
                - The managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
                  A scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with
                  managedInstanceGroupIds, managedCompartmentIds, and lifecycleStageIds.
            returned: on success
            type: list
            sample: []
        managed_instance_group_ids:
            description:
                - The managed instance group L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job
                  operates on. A scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with managedInstanceIds,
                  managedCompartmentIds, and lifecycleStageIds.
            returned: on success
            type: list
            sample: []
        managed_compartment_ids:
            description:
                - The compartment L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on. A
                  scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with managedInstanceIds,
                  managedInstanceGroupIds, and lifecycleStageIds.
            returned: on success
            type: list
            sample: []
        lifecycle_stage_ids:
            description:
                - The lifecycle stage L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
                  A scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with
                  managedInstanceIds, managedInstanceGroupIds, and managedCompartmentIds.
            returned: on success
            type: list
            sample: []
        is_subcompartment_included:
            description:
                - Indicates whether to apply the scheduled job to all compartments in the tenancy when managedCompartmentIds specifies the tenancy
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) (root compartment).
            returned: on success
            type: bool
            sample: true
        operations:
            description:
                - "The list of operations this scheduled job needs to perform.
                  A scheduled job supports only one operation type, unless it is one of the following:
                  * UPDATE_PACKAGES
                  * UPDATE_ALL
                  * UPDATE_SECURITY
                  * UPDATE_BUGFIX
                  * UPDATE_ENHANCEMENT
                  * UPDATE_OTHER
                  * UPDATE_KSPLICE_USERSPACE
                  * UPDATE_KSPLICE_KERNEL"
            returned: on success
            type: complex
            contains:
                operation_type:
                    description:
                        - The type of operation this scheduled job performs.
                    returned: on success
                    type: str
                    sample: INSTALL_PACKAGES
                package_names:
                    description:
                        - The names of the target packages. This parameter only applies when the scheduled job is for installing, updating, or removing
                          packages.
                    returned: on success
                    type: list
                    sample: []
                windows_update_names:
                    description:
                        - "Unique identifier for the Windows update. This parameter only applies if the scheduled job is for installing Windows updates.
                          Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
                          For example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'."
                    returned: on success
                    type: list
                    sample: []
                manage_module_streams_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        enable:
                            description:
                                - The set of module streams to enable.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                        disable:
                            description:
                                - The set of module streams to disable.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                        install:
                            description:
                                - The set of module stream profiles to install.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                profile_name:
                                    description:
                                        - The name of a profile of the specified module stream.
                                    returned: on success
                                    type: str
                                    sample: profile_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                        remove:
                            description:
                                - The set of module stream profiles to remove.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                profile_name:
                                    description:
                                        - The name of a profile of the specified module stream.
                                    returned: on success
                                    type: str
                                    sample: profile_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                switch_module_streams_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        module_name:
                            description:
                                - The name of a module.
                            returned: on success
                            type: str
                            sample: module_name_example
                        stream_name:
                            description:
                                - The name of a stream of the specified module.
                            returned: on success
                            type: str
                            sample: stream_name_example
                        software_source_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains
                                  the module stream.
                            returned: on success
                            type: str
                            sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                software_source_ids:
                    description:
                        - The software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
                          This parameter only applies when the scheduled job is for attaching or detaching software sources.
                    returned: on success
                    type: list
                    sample: []
        work_request_ids:
            description:
                - The list of work request L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with this scheduled
                  job.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time this scheduled job was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this scheduled job was updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the scheduled job.
            returned: on success
            type: str
            sample: CREATING
        is_managed_by_autonomous_linux:
            description:
                - Indicates whether this scheduled job is managed by the Autonomous Linux service.
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
        is_restricted:
            description:
                - Indicates if the schedule job has restricted update and deletion capabilities. For restricted scheduled jobs,
                  you can update only the timeNextExecution, recurringRule, and tags.
            returned: on success
            type: bool
            sample: true
        retry_intervals:
            description:
                - The amount of time in minutes to wait until retrying the scheduled job. If set, the service will automatically retry
                  a failed scheduled job after the interval. For example, you could set the interval to [2,5,10]. If the initial
                  execution of the job fails, the service waits 2 minutes and then retries. If that fails, the service waits 5 minutes
                  and then retries. If that fails, the service waits 10 minutes and then retries.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "schedule_type": "ONETIME",
        "locations": [],
        "time_next_execution": "2013-10-20T19:20:30+01:00",
        "time_last_execution": "2013-10-20T19:20:30+01:00",
        "recurring_rule": "recurring_rule_example",
        "managed_instance_ids": [],
        "managed_instance_group_ids": [],
        "managed_compartment_ids": [],
        "lifecycle_stage_ids": [],
        "is_subcompartment_included": true,
        "operations": [{
            "operation_type": "INSTALL_PACKAGES",
            "package_names": [],
            "windows_update_names": [],
            "manage_module_streams_details": {
                "enable": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "disable": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "install": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "profile_name": "profile_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "remove": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "profile_name": "profile_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            },
            "switch_module_streams_details": {
                "module_name": "module_name_example",
                "stream_name": "stream_name_example",
                "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "software_source_ids": []
        }],
        "work_request_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_managed_by_autonomous_linux": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "is_restricted": true,
        "retry_intervals": []
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
    from oci.os_management_hub import ScheduledJobClient
    from oci.os_management_hub.models import CreateScheduledJobDetails
    from oci.os_management_hub.models import UpdateScheduledJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubScheduledJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            OsManagementHubScheduledJobHelperGen, self
        ).get_possible_entity_types() + [
            "scheduledjob",
            "scheduledjobs",
            "osManagementHubscheduledjob",
            "osManagementHubscheduledjobs",
            "scheduledjobresource",
            "scheduledjobsresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "scheduled_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("scheduled_job_id")

    def get_get_fn(self):
        return self.client.get_scheduled_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_job, scheduled_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_job,
            scheduled_job_id=self.module.params.get("scheduled_job_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["compartment_id", "display_name", "is_managed_by_autonomous_linux"]
            if self._use_name_as_identifier()
            else [
                "compartment_id",
                "display_name",
                "schedule_type",
                "is_managed_by_autonomous_linux",
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
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateScheduledJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_scheduled_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_scheduled_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateScheduledJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_scheduled_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
                update_scheduled_job_details=update_details,
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
            call_fn=self.client.delete_scheduled_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


OsManagementHubScheduledJobHelperCustom = get_custom_class(
    "OsManagementHubScheduledJobHelperCustom"
)


class ResourceHelper(
    OsManagementHubScheduledJobHelperCustom, OsManagementHubScheduledJobHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            locations=dict(type="list", elements="str"),
            managed_instance_ids=dict(type="list", elements="str"),
            managed_instance_group_ids=dict(type="list", elements="str"),
            managed_compartment_ids=dict(type="list", elements="str"),
            lifecycle_stage_ids=dict(type="list", elements="str"),
            is_subcompartment_included=dict(type="bool"),
            is_managed_by_autonomous_linux=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            schedule_type=dict(type="str", choices=["ONETIME", "RECURRING"]),
            time_next_execution=dict(type="str"),
            recurring_rule=dict(type="str"),
            operations=dict(
                type="list",
                elements="dict",
                options=dict(
                    operation_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "INSTALL_PACKAGES",
                            "UPDATE_PACKAGES",
                            "REMOVE_PACKAGES",
                            "UPDATE_ALL",
                            "UPDATE_SECURITY",
                            "UPDATE_BUGFIX",
                            "UPDATE_ENHANCEMENT",
                            "UPDATE_OTHER",
                            "UPDATE_KSPLICE_USERSPACE",
                            "UPDATE_KSPLICE_KERNEL",
                            "MANAGE_MODULE_STREAMS",
                            "SWITCH_MODULE_STREAM",
                            "ATTACH_SOFTWARE_SOURCES",
                            "DETACH_SOFTWARE_SOURCES",
                            "SYNC_MANAGEMENT_STATION_MIRROR",
                            "PROMOTE_LIFECYCLE",
                            "INSTALL_WINDOWS_UPDATES",
                            "INSTALL_ALL_WINDOWS_UPDATES",
                            "INSTALL_SECURITY_WINDOWS_UPDATES",
                            "INSTALL_BUGFIX_WINDOWS_UPDATES",
                            "INSTALL_ENHANCEMENT_WINDOWS_UPDATES",
                            "INSTALL_OTHER_WINDOWS_UPDATES",
                        ],
                    ),
                    package_names=dict(type="list", elements="str"),
                    windows_update_names=dict(type="list", elements="str"),
                    manage_module_streams_details=dict(
                        type="dict",
                        options=dict(
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
                        ),
                    ),
                    switch_module_streams_details=dict(
                        type="dict",
                        options=dict(
                            module_name=dict(type="str", required=True),
                            stream_name=dict(type="str", required=True),
                            software_source_id=dict(type="str"),
                        ),
                    ),
                    software_source_ids=dict(type="list", elements="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            retry_intervals=dict(type="list", elements="int"),
            scheduled_job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="scheduled_job",
        service_client_class=ScheduledJobClient,
        namespace="os_management_hub",
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
