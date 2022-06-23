#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_autonomous_exadata_infrastructure
short_description: Manage an AutonomousExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutonomousExadataInfrastructure resource in Oracle Cloud Infrastructure
    - "For I(state=present), **Deprecated** To create a new Autonomous Database system on dedicated Exadata Infrastructure, use the
      L(CreateCloudExadataInfrastructure,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudExadataInfrastructure/CreateCloudExadataInfrastructure) and
      L(CreateCloudAutonomousVmCluster,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudAutonomousVmCluster/CreateCloudAutonomousVmCluster) operations instead. Note that to create an Autonomous VM
      cluster, you must have an existing Exadata Infrastructure resource to contain the VM cluster."
    - "This resource has the following action operations in the M(oracle.oci.oci_database_autonomous_exadata_infrastructure_actions) module: change_compartment,
      rotate_ords_certs, rotate_ssl_certs."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the Autonomous Exadata Infrastructure
              belongs in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    availability_domain:
        description:
            - The availability domain where the Autonomous Exadata Infrastructure is located.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the Autonomous Exadata Infrastructure is
              associated with.
            - "**Subnet Restrictions:**
              - For Autonomous Exadata Infrastructures, do not use a subnet that overlaps with 192.168.128.0/20"
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and backup subnet.
            - Required for create using I(state=present).
        type: str
    shape:
        description:
            - The shape of the Autonomous Exadata Infrastructure. The shape determines resources allocated to the Autonomous Exadata Infrastructure (CPU cores,
              memory and storage). To get a list of shapes, use the ListDbSystemShapes operation.
            - Required for create using I(state=present).
        type: str
    domain:
        description:
            - A domain name used for the Autonomous Exadata Infrastructure. If the Oracle-provided Internet and VCN
              Resolver is enabled for the specified subnet, the domain name for the subnet is used
              (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
        type: str
    license_model:
        description:
            - The Oracle license model that applies to all the databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    display_name:
        description:
            - The user-friendly name for the Autonomous Exadata Infrastructure. It does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
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
    autonomous_exadata_infrastructure_id:
        description:
            - The Autonomous Exadata Infrastructure  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AutonomousExadataInfrastructure.
            - Use I(state=present) to create or update an AutonomousExadataInfrastructure.
            - Use I(state=absent) to delete an AutonomousExadataInfrastructure.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create autonomous_exadata_infrastructure
  oci_database_autonomous_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example

    # optional
    domain: domain_example
    license_model: LICENSE_INCLUDED
    display_name: display_name_example
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update autonomous_exadata_infrastructure
  oci_database_autonomous_exadata_infrastructure:
    # required
    autonomous_exadata_infrastructure_id: "ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update autonomous_exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete autonomous_exadata_infrastructure
  oci_database_autonomous_exadata_infrastructure:
    # required
    autonomous_exadata_infrastructure_id: "ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete autonomous_exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
autonomous_exadata_infrastructure:
    description:
        - Details of the AutonomousExadataInfrastructure resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: display_name_example
        availability_domain:
            description:
                - The name of the availability domain that the Autonomous Exadata Infrastructure is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        subnet_id:
            description:
                - The OCID of the subnet the Autonomous Exadata Infrastructure is associated with.
                - "**Subnet Restrictions:**
                  - For Autonomous Databases with Autonomous Exadata Infrastructure, do not use a subnet that overlaps with 192.168.128.0/20"
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
        shape:
            description:
                - The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU
                  cores, memory and storage).
            returned: on success
            type: str
            sample: shape_example
        hostname:
            description:
                - The host name for the Autonomous Exadata Infrastructure node.
            returned: on success
            type: str
            sample: hostname_example
        domain:
            description:
                - The domain name for the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: domain_example
        lifecycle_state:
            description:
                - The current lifecycle state of the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: lifecycle_details_example
        license_model:
            description:
                - The Oracle license model that applies to all databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        time_created:
            description:
                - The date and time the Autonomous Exadata Infrastructure was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        scan_dns_name:
            description:
                - The FQDN of the DNS record for the SCAN IP addresses that are associated with the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: scan_dns_name_example
        zone_id:
            description:
                - The OCID of the zone the Autonomous Exadata Infrastructure is associated with.
            returned: on success
            type: str
            sample: "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "shape": "shape_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "license_model": "LICENSE_INCLUDED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "patching_mode": "ROLLING",
            "is_custom_action_timeout_enabled": true,
            "custom_action_timeout_in_mins": 56,
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
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "scan_dns_name": "scan_dns_name_example",
        "zone_id": "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import LaunchAutonomousExadataInfrastructureDetails
    from oci.database.models import UpdateAutonomousExadataInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousExadataInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(AutonomousExadataInfrastructureHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            AutonomousExadataInfrastructureHelperGen, self
        ).get_possible_entity_types() + [
            "autonomousexadatainfrastructure",
            "autonomousexadatainfrastructures",
            "databaseautonomousexadatainfrastructure",
            "databaseautonomousexadatainfrastructures",
            "autonomousexadatainfrastructureresource",
            "autonomousexadatainfrastructuresresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "autonomous_exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_autonomous_exadata_infrastructure

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_exadata_infrastructure,
            autonomous_exadata_infrastructure_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_exadata_infrastructure,
            autonomous_exadata_infrastructure_id=self.module.params.get(
                "autonomous_exadata_infrastructure_id"
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
        optional_list_method_params = ["availability_domain", "display_name"]

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
            self.client.list_autonomous_exadata_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return LaunchAutonomousExadataInfrastructureDetails

    def get_exclude_attributes(self):
        return ["maintenance_window_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.launch_autonomous_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                launch_autonomous_exadata_infrastructure_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutonomousExadataInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_autonomous_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_exadata_infrastructure_id=self.module.params.get(
                    "autonomous_exadata_infrastructure_id"
                ),
                update_autonomous_exadata_infrastructures_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.terminate_autonomous_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_exadata_infrastructure_id=self.module.params.get(
                    "autonomous_exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousExadataInfrastructureHelperCustom = get_custom_class(
    "AutonomousExadataInfrastructureHelperCustom"
)


class ResourceHelper(
    AutonomousExadataInfrastructureHelperCustom,
    AutonomousExadataInfrastructureHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            subnet_id=dict(type="str"),
            shape=dict(type="str"),
            domain=dict(type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
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
            nsg_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            autonomous_exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_exadata_infrastructure",
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
