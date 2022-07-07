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
module: oci_database_autonomous_vm_cluster_facts
short_description: Fetches details about one or multiple AutonomousVmCluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousVmCluster resources in Oracle Cloud Infrastructure
    - Gets a list of Exadata Cloud@Customer Autonomous VM clusters in the specified compartment. To list Autonomous VM Clusters in the Oracle Cloud, see
      L(ListCloudAutonomousVmClusters,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/CloudAutonomousVmCluster/ListCloudAutonomousVmClusters).
    - If I(autonomous_vm_cluster_id) is specified, the details of a single AutonomousVmCluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_vm_cluster_id:
        description:
            - The autonomous VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific autonomous_vm_cluster.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple autonomous_vm_clusters.
        type: str
    exadata_infrastructure_id:
        description:
            - If provided, filters the results for the given Exadata Infrastructure.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
            - "MAINTENANCE_IN_PROGRESS"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_vm_cluster
  oci_database_autonomous_vm_cluster_facts:
    # required
    autonomous_vm_cluster_id: "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List autonomous_vm_clusters
  oci_database_autonomous_vm_cluster_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING
    display_name: display_name_example

"""

RETURN = """
autonomous_vm_clusters:
    description:
        - List of AutonomousVmCluster resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous VM cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time that the Autonomous VM cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Autonomous VM cluster.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_zone:
            description:
                - The time zone to use for the Autonomous VM cluster. For details, see L(DB System Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        vm_cluster_network_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster network.
            returned: on success
            type: str
            sample: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
        is_local_backup_enabled:
            description:
                - If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata
                  storage is not available in the Autonomous VM cluster.
            returned: on success
            type: bool
            sample: true
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
            returned: on success
            type: int
            sample: 56
        ocpus_enabled:
            description:
                - The number of enabled OCPU cores.
            returned: on success
            type: float
            sample: 3.4
        available_cpus:
            description:
                - The numnber of CPU cores available.
            returned: on success
            type: int
            sample: 56
        total_container_databases:
            description:
                - The total number of Autonomous Container Databases that can be created.
            returned: on success
            type: int
            sample: 56
        memory_per_oracle_compute_unit_in_gbs:
            description:
                - The amount of memory (in GBs) enabled per each OCPU core.
            returned: on success
            type: int
            sample: 56
        cpu_core_count_per_node:
            description:
                - The number of OCPU cores enabled per VM cluster node.
            returned: on success
            type: int
            sample: 56
        autonomous_data_storage_size_in_tbs:
            description:
                - The data disk group size allocated for Autonomous Databases, in TBs.
            returned: on success
            type: float
            sample: 1.2
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
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - The total data storage allocated in TBs
            returned: on success
            type: float
            sample: 1.2
        data_storage_size_in_gbs:
            description:
                - The total data storage allocated in GBs.
            returned: on success
            type: float
            sample: 1.2
        available_data_storage_size_in_tbs:
            description:
                - "**Deprecated.** Use `availableAutonomousDataStorageSizeInTBs` for Autonomous Databases' data storage availability in TBs."
            returned: on success
            type: float
            sample: 1.2
        license_model:
            description:
                - The Oracle license model that applies to the Autonomous VM cluster. The default is LICENSE_INCLUDED.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
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
        reclaimable_cpus:
            description:
                - CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous
                  Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous
                  Container Database.
            returned: on success
            type: int
            sample: 56
        available_container_databases:
            description:
                - The number of Autonomous Container Databases that can be created with the currently available local storage.
            returned: on success
            type: int
            sample: 56
        available_autonomous_data_storage_size_in_tbs:
            description:
                - The data disk group size available for Autonomous Databases, in TBs.
            returned: on success
            type: float
            sample: 1.2
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_zone": "time_zone_example",
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_cluster_network_id": "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx",
        "is_local_backup_enabled": true,
        "cpus_enabled": 56,
        "ocpus_enabled": 3.4,
        "available_cpus": 56,
        "total_container_databases": 56,
        "memory_per_oracle_compute_unit_in_gbs": 56,
        "cpu_core_count_per_node": 56,
        "autonomous_data_storage_size_in_tbs": 1.2,
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
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "data_storage_size_in_tbs": 1.2,
        "data_storage_size_in_gbs": 1.2,
        "available_data_storage_size_in_tbs": 1.2,
        "license_model": "LICENSE_INCLUDED",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "reclaimable_cpus": 56,
        "available_container_databases": 56,
        "available_autonomous_data_storage_size_in_tbs": 1.2
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousVmClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "autonomous_vm_cluster_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_vm_cluster,
            autonomous_vm_cluster_id=self.module.params.get("autonomous_vm_cluster_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "exadata_infrastructure_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_vm_clusters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutonomousVmClusterFactsHelperCustom = get_custom_class(
    "AutonomousVmClusterFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousVmClusterFactsHelperCustom, AutonomousVmClusterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_vm_cluster_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            exadata_infrastructure_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                    "MAINTENANCE_IN_PROGRESS",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_vm_cluster",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_vm_clusters=result)


if __name__ == "__main__":
    main()
