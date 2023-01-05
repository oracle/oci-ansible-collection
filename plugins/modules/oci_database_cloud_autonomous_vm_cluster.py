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
module: oci_database_cloud_autonomous_vm_cluster
short_description: Manage a CloudAutonomousVmCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CloudAutonomousVmCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Autonomous Exadata VM cluster in the Oracle cloud. For Exadata Cloud@Customer systems, see
      L(CreateAutonomousVmCluster,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/AutonomousVmCluster/CreateAutonomousVmCluster).
    - "This resource has the following action operations in the M(oracle.oci.oci_database_cloud_autonomous_vm_cluster_actions) module: change_compartment,
      rotate_cloud_autonomous_vm_cluster_ords_certs, rotate_cloud_autonomous_vm_cluster_ssl_certs."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the cloud Autonomous VM Cluster is associated
              with.
            - Required for create using I(state=present).
        type: str
    cloud_exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure.
            - Required for create using I(state=present).
        type: str
    total_container_databases:
        description:
            - The total number of Autonomous Container Databases that can be created.
        type: int
    cpu_core_count_per_node:
        description:
            - The number of OCPU cores to enable per VM cluster node.
        type: int
    memory_per_oracle_compute_unit_in_gbs:
        description:
            - The amount of memory (in GBs) to be enabled per each OCPU core.
        type: int
    autonomous_data_storage_size_in_tbs:
        description:
            - The data disk group size to be allocated for Autonomous Databases, in TBs.
        type: float
    cluster_time_zone:
        description:
            - The time zone to use for the Cloud Autonomous VM cluster. For details, see L(DB System Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
        type: str
    db_servers:
        description:
            - The list of Db server.
        type: list
        elements: str
    description:
        description:
            - User defined description of the cloud Autonomous VM cluster.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    maintenance_window_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            preference:
                description:
                    - The maintenance window scheduling preference.
                type: str
                choices:
                    - "NO_PREFERENCE"
                    - "CUSTOM_PREFERENCE"
                required: true
            patching_mode:
                description:
                    - "Cloud Exadata infrastructure node patching method, either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
                    - "*IMPORTANT*: Non-rolling infrastructure patching involves system down time. See L(Oracle-Managed Infrastructure Maintenance
                      Updates,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle) for more information."
                type: str
                choices:
                    - "ROLLING"
                    - "NONROLLING"
            is_custom_action_timeout_enabled:
                description:
                    - If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.
                type: bool
            custom_action_timeout_in_mins:
                description:
                    - Determines the amount of time the system will wait before the start of each database server patching operation.
                      Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).
                type: int
            is_monthly_patching_enabled:
                description:
                    - If true, enables the monthly patching option.
                type: bool
            months:
                description:
                    - Months during the year when maintenance should be performed.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Name of the month of the year.
                        type: str
                        choices:
                            - "JANUARY"
                            - "FEBRUARY"
                            - "MARCH"
                            - "APRIL"
                            - "MAY"
                            - "JUNE"
                            - "JULY"
                            - "AUGUST"
                            - "SEPTEMBER"
                            - "OCTOBER"
                            - "NOVEMBER"
                            - "DECEMBER"
                        required: true
            weeks_of_month:
                description:
                    - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                      duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                      For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                      Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                      Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the
                      week and hours that maintenance will be performed.
                type: list
                elements: int
            days_of_week:
                description:
                    - Days during the week when maintenance should be performed.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Name of the day of the week.
                        type: str
                        choices:
                            - "MONDAY"
                            - "TUESDAY"
                            - "WEDNESDAY"
                            - "THURSDAY"
                            - "FRIDAY"
                            - "SATURDAY"
                            - "SUNDAY"
                        required: true
            hours_of_day:
                description:
                    - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                      - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 -
                        represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC"
                type: list
                elements: int
            lead_time_in_weeks:
                description:
                    - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.
                type: int
    license_model:
        description:
            - The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-
              premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
              License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
              Note that when provisioning an Autonomous Database on L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
              database/index.html), this attribute must be null because the attribute is already set at the
              Autonomous Exadata Infrastructure level. When using L(shared Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
              database/index.html), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    nsg_ids:
        description:
            - "The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the network security groups (NSGs) to which this
              resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see L(Security
              Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
              **NsgIds restrictions:**
              - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty."
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    cloud_autonomous_vm_cluster_id:
        description:
            - The Cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CloudAutonomousVmCluster.
            - Use I(state=present) to create or update a CloudAutonomousVmCluster.
            - Use I(state=absent) to delete a CloudAutonomousVmCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create cloud_autonomous_vm_cluster
  oci_database_cloud_autonomous_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    total_container_databases: 56
    cpu_core_count_per_node: 56
    memory_per_oracle_compute_unit_in_gbs: 56
    autonomous_data_storage_size_in_tbs: 3.4
    cluster_time_zone: cluster_time_zone_example
    db_servers: [ "db_servers_example" ]
    description: description_example
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      is_monthly_patching_enabled: true
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    license_model: LICENSE_INCLUDED
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update cloud_autonomous_vm_cluster
  oci_database_cloud_autonomous_vm_cluster:
    # required
    cloud_autonomous_vm_cluster_id: "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      is_monthly_patching_enabled: true
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    license_model: LICENSE_INCLUDED
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update cloud_autonomous_vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_cloud_autonomous_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      is_monthly_patching_enabled: true
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    license_model: LICENSE_INCLUDED
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete cloud_autonomous_vm_cluster
  oci_database_cloud_autonomous_vm_cluster:
    # required
    cloud_autonomous_vm_cluster_id: "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete cloud_autonomous_vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_cloud_autonomous_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
cloud_autonomous_vm_cluster:
    description:
        - Details of the CloudAutonomousVmCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - User defined description of the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: description_example
        availability_domain:
            description:
                - The name of the availability domain that the cloud Autonomous VM cluster is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the cloud Autonomous VM Cluster is associated
                  with.
                - "**Subnet Restrictions:**
                  - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and backup subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - "The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the network security groups (NSGs) to which
                  this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see L(Security
                  Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
                  **NsgIds restrictions:**
                  - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty."
            returned: on success
            type: list
            sample: []
        last_update_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance update history. This value is
                  updated when a maintenance update starts.
            returned: on success
            type: str
            sample: "ocid1.lastupdatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: PROVISIONING
        display_name:
            description:
                - The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time that the cloud Autonomous VM cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last date and time that the cloud Autonomous VM cluster was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        cluster_time_zone:
            description:
                - The time zone of the Cloud Autonomous VM Cluster.
            returned: on success
            type: str
            sample: cluster_time_zone_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        hostname:
            description:
                - The hostname for the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: hostname_example
        domain:
            description:
                - The domain name for the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: domain_example
        cloud_exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        shape:
            description:
                - The model name of the Exadata hardware running the cloud Autonomous VM cluster.
            returned: on success
            type: str
            sample: shape_example
        node_count:
            description:
                - The number of database servers in the cloud VM cluster.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - The total data storage allocated, in terabytes (TB).
            returned: on success
            type: float
            sample: 1.2
        data_storage_size_in_gbs:
            description:
                - The total data storage allocated, in gigabytes (GB).
            returned: on success
            type: float
            sample: 1.2
        cpu_core_count:
            description:
                - The number of CPU cores on the cloud Autonomous VM cluster.
            returned: on success
            type: int
            sample: 56
        ocpu_count:
            description:
                - The number of CPU cores on the cloud Autonomous VM cluster. Only 1 decimal place is allowed for the fractional part.
            returned: on success
            type: float
            sample: 3.4
        cpu_core_count_per_node:
            description:
                - The number of OCPU cores enabled per VM cluster node.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        license_model:
            description:
                - The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-
                  premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
                  License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
                  Note that when provisioning an Autonomous Database on L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
                  database/index.html), this attribute must be null because the attribute is already set at the
                  Autonomous Exadata Infrastructure level. When using L(shared Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
                  database/index.html), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        last_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance run.
            returned: on success
            type: str
            sample: "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: str
            sample: "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preference:
                    description:
                        - The maintenance window scheduling preference.
                    returned: on success
                    type: str
                    sample: NO_PREFERENCE
                patching_mode:
                    description:
                        - "Cloud Exadata infrastructure node patching method, either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
                        - "*IMPORTANT*: Non-rolling infrastructure patching involves system down time. See L(Oracle-Managed Infrastructure Maintenance
                          Updates,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle) for more information."
                    returned: on success
                    type: str
                    sample: ROLLING
                is_custom_action_timeout_enabled:
                    description:
                        - If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.
                    returned: on success
                    type: bool
                    sample: true
                custom_action_timeout_in_mins:
                    description:
                        - Determines the amount of time the system will wait before the start of each database server patching operation.
                          Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).
                    returned: on success
                    type: int
                    sample: 56
                is_monthly_patching_enabled:
                    description:
                        - If true, enables the monthly patching option.
                    returned: on success
                    type: bool
                    sample: true
                months:
                    description:
                        - Months during the year when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the month of the year.
                            returned: on success
                            type: str
                            sample: JANUARY
                weeks_of_month:
                    description:
                        - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                          duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                          For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                          Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                          Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of
                          the week and hours that maintenance will be performed.
                    returned: on success
                    type: list
                    sample: []
                days_of_week:
                    description:
                        - Days during the week when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                hours_of_day:
                    description:
                        - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                          - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12
                            - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59
                            UTC"
                    returned: on success
                    type: list
                    sample: []
                lead_time_in_weeks:
                    description:
                        - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to
                          4.
                    returned: on success
                    type: int
                    sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        available_cpus:
            description:
                - CPU cores available for allocation to Autonomous Databases.
            returned: on success
            type: float
            sample: 3.4
        reclaimable_cpus:
            description:
                - CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous
                  Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous
                  Container Database.
            returned: on success
            type: float
            sample: 3.4
        available_container_databases:
            description:
                - The number of Autonomous Container Databases that can be created with the currently available local storage.
            returned: on success
            type: int
            sample: 56
        total_container_databases:
            description:
                - The total number of Autonomous Container Databases that can be created with the allocated local storage.
            returned: on success
            type: int
            sample: 56
        available_autonomous_data_storage_size_in_tbs:
            description:
                - The data disk group size available for Autonomous Databases, in TBs.
            returned: on success
            type: float
            sample: 1.2
        autonomous_data_storage_size_in_tbs:
            description:
                - The data disk group size allocated for Autonomous Databases, in TBs.
            returned: on success
            type: float
            sample: 1.2
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        memory_per_oracle_compute_unit_in_gbs:
            description:
                - The amount of memory (in GBs) enabled per each OCPU core.
            returned: on success
            type: int
            sample: 56
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "last_update_history_entry_id": "ocid1.lastupdatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "cluster_time_zone": "cluster_time_zone_example",
        "lifecycle_details": "lifecycle_details_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "cloud_exadata_infrastructure_id": "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "node_count": 56,
        "data_storage_size_in_tbs": 1.2,
        "data_storage_size_in_gbs": 1.2,
        "cpu_core_count": 56,
        "ocpu_count": 3.4,
        "cpu_core_count_per_node": 56,
        "memory_size_in_gbs": 56,
        "license_model": "LICENSE_INCLUDED",
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "patching_mode": "ROLLING",
            "is_custom_action_timeout_enabled": true,
            "custom_action_timeout_in_mins": 56,
            "is_monthly_patching_enabled": true,
            "months": [{
                "name": "JANUARY"
            }],
            "weeks_of_month": [],
            "days_of_week": [{
                "name": "MONDAY"
            }],
            "hours_of_day": [],
            "lead_time_in_weeks": 56
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "available_cpus": 3.4,
        "reclaimable_cpus": 3.4,
        "available_container_databases": 56,
        "total_container_databases": 56,
        "available_autonomous_data_storage_size_in_tbs": 1.2,
        "autonomous_data_storage_size_in_tbs": 1.2,
        "db_node_storage_size_in_gbs": 56,
        "memory_per_oracle_compute_unit_in_gbs": 56
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateCloudAutonomousVmClusterDetails
    from oci.database.models import UpdateCloudAutonomousVmClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudAutonomousVmClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(CloudAutonomousVmClusterHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            CloudAutonomousVmClusterHelperGen, self
        ).get_possible_entity_types() + [
            "cloudautonomousvmcluster",
            "cloudautonomousvmclusters",
            "databasecloudautonomousvmcluster",
            "databasecloudautonomousvmclusters",
            "cloudautonomousvmclusterresource",
            "cloudautonomousvmclustersresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "cloud_autonomous_vm_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cloud_autonomous_vm_cluster_id")

    def get_get_fn(self):
        return self.client.get_cloud_autonomous_vm_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_autonomous_vm_cluster,
            cloud_autonomous_vm_cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_autonomous_vm_cluster,
            cloud_autonomous_vm_cluster_id=self.module.params.get(
                "cloud_autonomous_vm_cluster_id"
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
        optional_list_method_params = [
            "cloud_exadata_infrastructure_id",
            "display_name",
        ]

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
            self.client.list_cloud_autonomous_vm_clusters, **kwargs
        )

    def get_create_model_class(self):
        return CreateCloudAutonomousVmClusterDetails

    def get_exclude_attributes(self):
        return ["maintenance_window_details", "db_servers"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cloud_autonomous_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_cloud_autonomous_vm_cluster_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateCloudAutonomousVmClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cloud_autonomous_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_autonomous_vm_cluster_id=self.module.params.get(
                    "cloud_autonomous_vm_cluster_id"
                ),
                update_cloud_autonomous_vm_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_cloud_autonomous_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_autonomous_vm_cluster_id=self.module.params.get(
                    "cloud_autonomous_vm_cluster_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CloudAutonomousVmClusterHelperCustom = get_custom_class(
    "CloudAutonomousVmClusterHelperCustom"
)


class ResourceHelper(
    CloudAutonomousVmClusterHelperCustom, CloudAutonomousVmClusterHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            cloud_exadata_infrastructure_id=dict(type="str"),
            total_container_databases=dict(type="int"),
            cpu_core_count_per_node=dict(type="int"),
            memory_per_oracle_compute_unit_in_gbs=dict(type="int"),
            autonomous_data_storage_size_in_tbs=dict(type="float"),
            cluster_time_zone=dict(type="str"),
            db_servers=dict(type="list", elements="str"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            maintenance_window_details=dict(
                type="dict",
                options=dict(
                    preference=dict(
                        type="str",
                        required=True,
                        choices=["NO_PREFERENCE", "CUSTOM_PREFERENCE"],
                    ),
                    patching_mode=dict(type="str", choices=["ROLLING", "NONROLLING"]),
                    is_custom_action_timeout_enabled=dict(type="bool"),
                    custom_action_timeout_in_mins=dict(type="int"),
                    is_monthly_patching_enabled=dict(type="bool"),
                    months=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "JANUARY",
                                    "FEBRUARY",
                                    "MARCH",
                                    "APRIL",
                                    "MAY",
                                    "JUNE",
                                    "JULY",
                                    "AUGUST",
                                    "SEPTEMBER",
                                    "OCTOBER",
                                    "NOVEMBER",
                                    "DECEMBER",
                                ],
                            )
                        ),
                    ),
                    weeks_of_month=dict(type="list", elements="int"),
                    days_of_week=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "MONDAY",
                                    "TUESDAY",
                                    "WEDNESDAY",
                                    "THURSDAY",
                                    "FRIDAY",
                                    "SATURDAY",
                                    "SUNDAY",
                                ],
                            )
                        ),
                    ),
                    hours_of_day=dict(type="list", elements="int"),
                    lead_time_in_weeks=dict(type="int"),
                ),
            ),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            nsg_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            cloud_autonomous_vm_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cloud_autonomous_vm_cluster",
        service_client_class=DatabaseClient,
        namespace="database",
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
