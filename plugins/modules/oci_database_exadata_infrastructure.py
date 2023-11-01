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
module: oci_database_exadata_infrastructure
short_description: Manage an ExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only.
      To create an Exadata Cloud Service infrastructure resource, use the  L(CreateCloudExadataInfrastructure,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudExadataInfrastructure/CreateCloudExadataInfrastructure) operation.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_exadata_infrastructure_actions) module: activate,
      add_storage_capacity, change_compartment, download_exadata_infrastructure_config_file."
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
    display_name:
        description:
            - The user-friendly name for the Exadata infrastructure. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    shape:
        description:
            - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            - Required for create using I(state=present).
        type: str
    storage_count:
        description:
            - The number of storage servers for the Exadata infrastructure.
        type: int
    compute_count:
        description:
            - The number of compute servers for the Exadata infrastructure.
        type: int
    cloud_control_plane_server1:
        description:
            - The IP address for the first control plane server.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    cloud_control_plane_server2:
        description:
            - The IP address for the second control plane server.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    netmask:
        description:
            - The netmask for the control plane network.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    gateway:
        description:
            - The gateway for the control plane network.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    admin_network_cidr:
        description:
            - The CIDR block for the Exadata administration network.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    infini_band_network_cidr:
        description:
            - The CIDR block for the Exadata InfiniBand interconnect.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    corporate_proxy:
        description:
            - The corporate network proxy for access to the control plane network. Oracle recommends using an HTTPS proxy when possible
              for enhanced security.
            - This parameter is updatable.
        type: str
    contacts:
        description:
            - The list of contacts for the Exadata infrastructure.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The name of the Exadata Infrastructure contact.
                type: str
                required: true
            phone_number:
                description:
                    - The phone number for the Exadata Infrastructure contact.
                type: str
            email:
                description:
                    - The email for the Exadata Infrastructure contact.
                type: str
                required: true
            is_primary:
                description:
                    - If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.
                type: bool
                required: true
            is_contact_mos_validated:
                description:
                    - If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure contact
                      is not a valid MOS contact.
                type: bool
    maintenance_window:
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
    additional_storage_count:
        description:
            - The requested number of additional storage servers for the Exadata infrastructure.
            - This parameter is updatable.
        type: int
    is_multi_rack_deployment:
        description:
            - Indicates if deployment is Multi-Rack or not.
            - This parameter is updatable.
        type: bool
    multi_rack_configuration_file:
        description:
            - The base64 encoded Multi-Rack configuration json file.
            - This parameter is updatable.
        type: str
    additional_compute_count:
        description:
            - The requested number of additional compute servers for the Exadata infrastructure.
            - This parameter is updatable.
        type: int
    additional_compute_system_model:
        description:
            - Oracle Exadata System Model specification. The system model determines the amount of compute or storage
              server resources available for use. For more information, please see L(System and Shape Configuration
              Options],https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-
              options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)
            - This parameter is updatable.
        type: str
        choices:
            - "X7"
            - "X8"
            - "X8M"
            - "X9M"
    dns_server:
        description:
            - The list of DNS server IP addresses. Maximum of 3 allowed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    ntp_server:
        description:
            - The list of NTP server IP addresses. Maximum of 3 allowed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    time_zone:
        description:
            - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_cps_offline_report_enabled:
        description:
            - Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status
              themselves and fix problems on their end, saving time and frustration
              for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata
              infrastructure provisioning. You can also disable or enable it at any time
              using the UpdateExadatainfrastructure API.
            - This parameter is updatable.
        type: bool
    network_bonding_mode_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            client_network_bonding_mode:
                description:
                    - The network bonding mode for the Exadata infrastructure.
                type: str
                choices:
                    - "ACTIVE_BACKUP"
                    - "LACP"
            backup_network_bonding_mode:
                description:
                    - The network bonding mode for the Exadata infrastructure.
                type: str
                choices:
                    - "ACTIVE_BACKUP"
                    - "LACP"
            dr_network_bonding_mode:
                description:
                    - The network bonding mode for the Exadata infrastructure.
                type: str
                choices:
                    - "ACTIVE_BACKUP"
                    - "LACP"
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
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExadataInfrastructure.
            - Use I(state=present) to create or update an ExadataInfrastructure.
            - Use I(state=absent) to delete an ExadataInfrastructure.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create exadata_infrastructure
  oci_database_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    shape: shape_example
    cloud_control_plane_server1: cloud_control_plane_server1_example
    cloud_control_plane_server2: cloud_control_plane_server2_example
    netmask: netmask_example
    gateway: gateway_example
    admin_network_cidr: admin_network_cidr_example
    infini_band_network_cidr: infini_band_network_cidr_example
    dns_server: [ "dns_server_example" ]
    ntp_server: [ "ntp_server_example" ]
    time_zone: time_zone_example

    # optional
    storage_count: 56
    compute_count: 56
    corporate_proxy: corporate_proxy_example
    contacts:
    - # required
      name: name_example
      email: email_example
      is_primary: true

      # optional
      phone_number: phone_number_example
      is_contact_mos_validated: true
    maintenance_window:
      # optional
      preference: NO_PREFERENCE
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
    is_multi_rack_deployment: true
    multi_rack_configuration_file: multi_rack_configuration_file_example
    is_cps_offline_report_enabled: true
    network_bonding_mode_details:
      # optional
      client_network_bonding_mode: ACTIVE_BACKUP
      backup_network_bonding_mode: ACTIVE_BACKUP
      dr_network_bonding_mode: ACTIVE_BACKUP
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update exadata_infrastructure
  oci_database_exadata_infrastructure:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    cloud_control_plane_server1: cloud_control_plane_server1_example
    cloud_control_plane_server2: cloud_control_plane_server2_example
    netmask: netmask_example
    gateway: gateway_example
    admin_network_cidr: admin_network_cidr_example
    infini_band_network_cidr: infini_band_network_cidr_example
    corporate_proxy: corporate_proxy_example
    contacts:
    - # required
      name: name_example
      email: email_example
      is_primary: true

      # optional
      phone_number: phone_number_example
      is_contact_mos_validated: true
    maintenance_window:
      # optional
      preference: NO_PREFERENCE
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
    additional_storage_count: 56
    is_multi_rack_deployment: true
    multi_rack_configuration_file: multi_rack_configuration_file_example
    additional_compute_count: 56
    additional_compute_system_model: X7
    dns_server: [ "dns_server_example" ]
    ntp_server: [ "ntp_server_example" ]
    time_zone: time_zone_example
    is_cps_offline_report_enabled: true
    network_bonding_mode_details:
      # optional
      client_network_bonding_mode: ACTIVE_BACKUP
      backup_network_bonding_mode: ACTIVE_BACKUP
      dr_network_bonding_mode: ACTIVE_BACKUP
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    cloud_control_plane_server1: cloud_control_plane_server1_example
    cloud_control_plane_server2: cloud_control_plane_server2_example
    netmask: netmask_example
    gateway: gateway_example
    admin_network_cidr: admin_network_cidr_example
    infini_band_network_cidr: infini_band_network_cidr_example
    corporate_proxy: corporate_proxy_example
    contacts:
    - # required
      name: name_example
      email: email_example
      is_primary: true

      # optional
      phone_number: phone_number_example
      is_contact_mos_validated: true
    maintenance_window:
      # optional
      preference: NO_PREFERENCE
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
    additional_storage_count: 56
    is_multi_rack_deployment: true
    multi_rack_configuration_file: multi_rack_configuration_file_example
    additional_compute_count: 56
    additional_compute_system_model: X7
    dns_server: [ "dns_server_example" ]
    ntp_server: [ "ntp_server_example" ]
    time_zone: time_zone_example
    is_cps_offline_report_enabled: true
    network_bonding_mode_details:
      # optional
      client_network_bonding_mode: ACTIVE_BACKUP
      backup_network_bonding_mode: ACTIVE_BACKUP
      dr_network_bonding_mode: ACTIVE_BACKUP
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete exadata_infrastructure
  oci_database_exadata_infrastructure:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
exadata_infrastructure:
    description:
        - Details of the ExadataInfrastructure resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the Exadata infrastructure.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: str
            sample: shape_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
            returned: on success
            type: int
            sample: 56
        max_cpu_count:
            description:
                - The total number of CPU cores available.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_memory_in_gbs:
            description:
                - The total memory available in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_db_node_storage_in_g_bs:
            description:
                - The total local node storage available in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - Size, in terabytes, of the DATA disk group.
            returned: on success
            type: float
            sample: 1.2
        max_data_storage_in_t_bs:
            description:
                - The total available DATA disk group size.
            returned: on success
            type: float
            sample: 1.2
        rack_serial_number:
            description:
                - The serial number for the Exadata infrastructure.
            returned: on success
            type: str
            sample: rack_serial_number_example
        storage_count:
            description:
                - The number of Exadata storage servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        additional_storage_count:
            description:
                - The requested number of additional storage servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        activated_storage_count:
            description:
                - The requested number of additional storage servers activated for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        compute_count:
            description:
                - The number of compute servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        is_multi_rack_deployment:
            description:
                - Indicates if deployment is Multi-Rack or not.
            returned: on success
            type: bool
            sample: true
        multi_rack_configuration_file:
            description:
                - The base64 encoded Multi-Rack configuration json file.
            returned: on success
            type: str
            sample: "null"

        additional_compute_count:
            description:
                - The requested number of additional compute servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        additional_compute_system_model:
            description:
                - Oracle Exadata System Model specification. The system model determines the amount of compute or storage
                  server resources available for use. For more information, please see L(System and Shape Configuration
                  Options],https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-
                  options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)
            returned: on success
            type: str
            sample: X7
        cloud_control_plane_server1:
            description:
                - The IP address for the first control plane server.
            returned: on success
            type: str
            sample: cloud_control_plane_server1_example
        cloud_control_plane_server2:
            description:
                - The IP address for the second control plane server.
            returned: on success
            type: str
            sample: cloud_control_plane_server2_example
        netmask:
            description:
                - The netmask for the control plane network.
            returned: on success
            type: str
            sample: netmask_example
        gateway:
            description:
                - The gateway for the control plane network.
            returned: on success
            type: str
            sample: gateway_example
        admin_network_cidr:
            description:
                - The CIDR block for the Exadata administration network.
            returned: on success
            type: str
            sample: admin_network_cidr_example
        infini_band_network_cidr:
            description:
                - The CIDR block for the Exadata InfiniBand interconnect.
            returned: on success
            type: str
            sample: infini_band_network_cidr_example
        corporate_proxy:
            description:
                - The corporate network proxy for access to the control plane network.
            returned: on success
            type: str
            sample: corporate_proxy_example
        dns_server:
            description:
                - The list of DNS server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        ntp_server:
            description:
                - The list of NTP server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the Exadata infrastructure was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        csi_number:
            description:
                - The CSI Number of the Exadata infrastructure.
            returned: on success
            type: str
            sample: csi_number_example
        contacts:
            description:
                - The list of contacts for the Exadata infrastructure.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: name_example
                phone_number:
                    description:
                        - The phone number for the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: phone_number_example
                email:
                    description:
                        - The email for the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: email_example
                is_primary:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.
                    returned: on success
                    type: bool
                    sample: true
                is_contact_mos_validated:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure
                          contact is not a valid MOS contact.
                    returned: on success
                    type: bool
                    sample: true
        maintenance_slo_status:
            description:
                - A field to capture 'Maintenance SLO Status' for the Exadata infrastructure with values 'OK', 'DEGRADED'. Default is 'OK' when the
                  infrastructure is provisioned.
            returned: on success
            type: str
            sample: OK
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
        storage_server_version:
            description:
                - The software version of the storage servers (cells) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: storage_server_version_example
        db_server_version:
            description:
                - The software version of the database servers (dom0) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: db_server_version_example
        monthly_db_server_version:
            description:
                - The monthly software version of the database servers (dom0) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: monthly_db_server_version_example
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
        is_cps_offline_report_enabled:
            description:
                - Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status
                  themselves and fix problems on their end, saving time and frustration
                  for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata
                  infrastructure provisioning. You can also disable or enable it at any time
                  using the UpdateExadatainfrastructure API.
            returned: on success
            type: bool
            sample: true
        network_bonding_mode_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                client_network_bonding_mode:
                    description:
                        - The network bonding mode for the Exadata infrastructure.
                    returned: on success
                    type: str
                    sample: ACTIVE_BACKUP
                backup_network_bonding_mode:
                    description:
                        - The network bonding mode for the Exadata infrastructure.
                    returned: on success
                    type: str
                    sample: ACTIVE_BACKUP
                dr_network_bonding_mode:
                    description:
                        - The network bonding mode for the Exadata infrastructure.
                    returned: on success
                    type: str
                    sample: ACTIVE_BACKUP
        availability_domain:
            description:
                - The name of the availability domain that the Exadata infrastructure is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "shape": "shape_example",
        "time_zone": "time_zone_example",
        "cpus_enabled": 56,
        "max_cpu_count": 56,
        "memory_size_in_gbs": 56,
        "max_memory_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "max_db_node_storage_in_g_bs": 56,
        "data_storage_size_in_tbs": 1.2,
        "max_data_storage_in_t_bs": 1.2,
        "rack_serial_number": "rack_serial_number_example",
        "storage_count": 56,
        "additional_storage_count": 56,
        "activated_storage_count": 56,
        "compute_count": 56,
        "is_multi_rack_deployment": true,
        "multi_rack_configuration_file": null,
        "additional_compute_count": 56,
        "additional_compute_system_model": "X7",
        "cloud_control_plane_server1": "cloud_control_plane_server1_example",
        "cloud_control_plane_server2": "cloud_control_plane_server2_example",
        "netmask": "netmask_example",
        "gateway": "gateway_example",
        "admin_network_cidr": "admin_network_cidr_example",
        "infini_band_network_cidr": "infini_band_network_cidr_example",
        "corporate_proxy": "corporate_proxy_example",
        "dns_server": [],
        "ntp_server": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "csi_number": "csi_number_example",
        "contacts": [{
            "name": "name_example",
            "phone_number": "phone_number_example",
            "email": "email_example",
            "is_primary": true,
            "is_contact_mos_validated": true
        }],
        "maintenance_slo_status": "OK",
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
        "storage_server_version": "storage_server_version_example",
        "db_server_version": "db_server_version_example",
        "monthly_db_server_version": "monthly_db_server_version_example",
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cps_offline_report_enabled": true,
        "network_bonding_mode_details": {
            "client_network_bonding_mode": "ACTIVE_BACKUP",
            "backup_network_bonding_mode": "ACTIVE_BACKUP",
            "dr_network_bonding_mode": "ACTIVE_BACKUP"
        },
        "availability_domain": "Uocm:PHX-AD-1",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.database.models import CreateExadataInfrastructureDetails
    from oci.database.models import UpdateExadataInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ExadataInfrastructureHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            ExadataInfrastructureHelperGen, self
        ).get_possible_entity_types() + [
            "exadatainfrastructure",
            "exadatainfrastructures",
            "databaseexadatainfrastructure",
            "databaseexadatainfrastructures",
            "exadatainfrastructureresource",
            "exadatainfrastructuresresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_exadata_infrastructure

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_infrastructure,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
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
        optional_list_method_params = ["display_name"]

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
            self.client.list_exadata_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return CreateExadataInfrastructureDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(create_exadata_infrastructure_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExadataInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                update_exadata_infrastructure_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExadataInfrastructureHelperCustom = get_custom_class(
    "ExadataInfrastructureHelperCustom"
)


class ResourceHelper(ExadataInfrastructureHelperCustom, ExadataInfrastructureHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            shape=dict(type="str"),
            storage_count=dict(type="int"),
            compute_count=dict(type="int"),
            cloud_control_plane_server1=dict(type="str"),
            cloud_control_plane_server2=dict(type="str"),
            netmask=dict(type="str"),
            gateway=dict(type="str"),
            admin_network_cidr=dict(type="str"),
            infini_band_network_cidr=dict(type="str"),
            corporate_proxy=dict(type="str"),
            contacts=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    phone_number=dict(type="str"),
                    email=dict(type="str", required=True),
                    is_primary=dict(type="bool", required=True),
                    is_contact_mos_validated=dict(type="bool"),
                ),
            ),
            maintenance_window=dict(
                type="dict",
                options=dict(
                    preference=dict(
                        type="str", choices=["NO_PREFERENCE", "CUSTOM_PREFERENCE"]
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
            additional_storage_count=dict(type="int"),
            is_multi_rack_deployment=dict(type="bool"),
            multi_rack_configuration_file=dict(type="str"),
            additional_compute_count=dict(type="int"),
            additional_compute_system_model=dict(
                type="str", choices=["X7", "X8", "X8M", "X9M"]
            ),
            dns_server=dict(type="list", elements="str"),
            ntp_server=dict(type="list", elements="str"),
            time_zone=dict(type="str"),
            is_cps_offline_report_enabled=dict(type="bool"),
            network_bonding_mode_details=dict(
                type="dict",
                options=dict(
                    client_network_bonding_mode=dict(
                        type="str", choices=["ACTIVE_BACKUP", "LACP"]
                    ),
                    backup_network_bonding_mode=dict(
                        type="str", choices=["ACTIVE_BACKUP", "LACP"]
                    ),
                    dr_network_bonding_mode=dict(
                        type="str", choices=["ACTIVE_BACKUP", "LACP"]
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="exadata_infrastructure",
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
