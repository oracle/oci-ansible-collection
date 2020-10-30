#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_database_db_system_facts
short_description: Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
    - Lists the DB systems in the specified compartment. You can specify a `backupId` to list only the DB systems that support creating a database using this
      backup in this compartment.
    - If I(db_system_id) is specified, the details of a single DbSystem will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_system.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple db_systems.
        type: str
    backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup. Specify a backupId to list only the DB systems
              or DB homes that support creating a database using this backup in this compartment.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
            - "**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted."
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
            - "MIGRATED"
            - "MAINTENANCE_IN_PROGRESS"
    availability_domain:
        description:
            - A filter to return only resources that match the given availability domain exactly.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List db_systems
  oci_database_db_system_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific db_system
  oci_database_db_system_facts:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
db_systems:
    description:
        - List of DbSystem resources
    returned: on success
    type: complex
    contains:
        iorm_config_cache:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                lifecycle_state:
                    description:
                        - The current state of IORM configuration for the Exadata DB system.
                    returned: on success
                    type: string
                    sample: BOOTSTRAPPING
                lifecycle_details:
                    description:
                        - Additional information about the current `lifecycleState`.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
                objective:
                    description:
                        - The current value for the IORM objective.
                          The default is `AUTO`.
                    returned: on success
                    type: string
                    sample: LOW_LATENCY
                db_plans:
                    description:
                        - An array of IORM settings for all the database in
                          the Exadata DB system.
                    returned: on success
                    type: complex
                    contains:
                        db_name:
                            description:
                                - The database name. For the default `DbPlan`, the `dbName` is `default`.
                            returned: on success
                            type: string
                            sample: db_name_example
                        share:
                            description:
                                - The relative priority of this database.
                            returned: on success
                            type: int
                            sample: 56
                        flash_cache_limit:
                            description:
                                - The flash cache limit for this database. This value is internally configured based on the share value assigned to the
                                  database.
                            returned: on success
                            type: string
                            sample: flash_cache_limit_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name for the DB system. The name does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        availability_domain:
            description:
                - The name of the availability domain that the DB system is located in.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        fault_domains:
            description:
                - List of the Fault Domains in which this DB system is provisioned.
            returned: on success
            type: list
            sample: []
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the DB system is associated with.
                - "**Subnet Restrictions:**
                  - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
                  - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and backup subnet.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        backup_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup network subnet the DB system is associated
                  with. Applicable only to Exadata DB systems.
                - "**Subnet Restriction:** See the subnet restrictions information for **subnetId**."
            returned: on success
            type: string
            sample: ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx
        nsg_ids:
            description:
                - "A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this
                  resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about
                  NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
                  **NsgIds restrictions:**
                  - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty."
            returned: on success
            type: list
            sample: []
        backup_network_nsg_ids:
            description:
                - A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the
                  backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For
                  more information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm). Applicable only
                  to Exadata systems.
            returned: on success
            type: list
            sample: []
        shape:
            description:
                - "The shape of the DB system. The shape determines resources to allocate to the DB system.
                  - For virtual machine shapes, the number of CPU cores and memory
                  - For bare metal and Exadata shapes, the number of CPU cores, storage, and memory"
            returned: on success
            type: string
            sample: shape_example
        db_system_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                storage_management:
                    description:
                        - "The storage option used in DB system.
                          ASM - Automatic storage management
                          LVM - Logical Volume management"
                    returned: on success
                    type: string
                    sample: ASM
        ssh_public_keys:
            description:
                - The public key portion of one or more key pairs used for SSH access to the DB system.
            returned: on success
            type: list
            sample: [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ]
        time_zone:
            description:
                - The time zone of the DB system. For details, see L(DB System Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: string
            sample: time_zone_example
        hostname:
            description:
                - The hostname for the DB system.
            returned: on success
            type: string
            sample: hostname_example
        domain:
            description:
                - The domain name for the DB system.
            returned: on success
            type: string
            sample: domain_example
        version:
            description:
                - The Oracle Database version of the DB system.
            returned: on success
            type: string
            sample: version_example
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the DB system.
            returned: on success
            type: int
            sample: 56
        cluster_name:
            description:
                - The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may
                  contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.
            returned: on success
            type: string
            sample: cluster_name_example
        data_storage_percentage:
            description:
                - The percentage assigned to DATA storage (user data and database files).
                  The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40
                  and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        database_edition:
            description:
                - The Oracle Database edition that applies to all the databases on the DB system.
            returned: on success
            type: string
            sample: STANDARD_EDITION
        last_patch_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch history. This value is updated as soon as
                  a patch operation starts.
            returned: on success
            type: string
            sample: ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx
        listener_port:
            description:
                - The port number configured for the listener on the DB system.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the DB system.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the DB system was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        disk_redundancy:
            description:
                - The type of redundancy configured for the DB system.
                  NORMAL is 2-way redundancy.
                  HIGH is 3-way redundancy.
            returned: on success
            type: string
            sample: HIGH
        sparse_diskgroup:
            description:
                - True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.
            returned: on success
            type: bool
            sample: true
        scan_ip_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Single Client Access Name (SCAN) IP addresses
                  associated with the DB system.
                  SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
                  Oracle Clusterware directs the requests to the appropriate nodes in the cluster.
                - "**Note:** For a single-node DB system, this list is empty."
            returned: on success
            type: list
            sample: []
        vip_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual IP (VIP) addresses associated with the DB
                  system.
                  The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to
                  enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.
                - "**Note:** For a single-node DB system, this list is empty."
            returned: on success
            type: list
            sample: []
        scan_dns_record_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DNS record for the SCAN IP addresses that are
                  associated with the DB system.
            returned: on success
            type: string
            sample: ocid1.scandnsrecord.oc1..xxxxxxEXAMPLExxxxxx
        data_storage_size_in_gbs:
            description:
                - The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        reco_storage_size_in_gb:
            description:
                - The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        node_count:
            description:
                - The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.
            returned: on success
            type: int
            sample: 56
        license_model:
            description:
                - The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.
            returned: on success
            type: string
            sample: LICENSE_INCLUDED
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
                    type: string
                    sample: NO_PREFERENCE
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
                            type: string
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
                            type: string
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
            type: string
            sample: ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: string
            sample: ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx
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
        source_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: string
            sample: ocid1.sourcedbsystem.oc1..xxxxxxEXAMPLExxxxxx
        point_in_time_data_disk_clone_timestamp:
            description:
                - The point in time for a cloned database system when the data disks were cloned from the source database system, as described in L(RFC
                  3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "iorm_config_cache": {
            "lifecycle_state": "BOOTSTRAPPING",
            "lifecycle_details": "lifecycle_details_example",
            "objective": "LOW_LATENCY",
            "db_plans": [{
                "db_name": "db_name_example",
                "share": 56,
                "flash_cache_limit": "flash_cache_limit_example"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domains": [],
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_subnet_id": "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "backup_network_nsg_ids": [],
        "shape": "shape_example",
        "db_system_options": {
            "storage_management": "ASM"
        },
        "ssh_public_keys": [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ],
        "time_zone": "time_zone_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "version": "version_example",
        "cpu_core_count": 56,
        "cluster_name": "cluster_name_example",
        "data_storage_percentage": 56,
        "database_edition": "STANDARD_EDITION",
        "last_patch_history_entry_id": "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "listener_port": 56,
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "disk_redundancy": "HIGH",
        "sparse_diskgroup": true,
        "scan_ip_ids": [],
        "vip_ids": [],
        "scan_dns_record_id": "ocid1.scandnsrecord.oc1..xxxxxxEXAMPLExxxxxx",
        "data_storage_size_in_gbs": 56,
        "reco_storage_size_in_gb": 56,
        "node_count": 56,
        "license_model": "LICENSE_INCLUDED",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
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
        "source_db_system_id": "ocid1.sourcedbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "point_in_time_data_disk_clone_timestamp": "2013-10-20T19:20:30+01:00"
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


class DbSystemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "backup_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_systems,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DbSystemFactsHelperCustom = get_custom_class("DbSystemFactsHelperCustom")


class ResourceFactsHelper(DbSystemFactsHelperCustom, DbSystemFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_system_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            backup_id=dict(type="str"),
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
                    "MIGRATED",
                    "MAINTENANCE_IN_PROGRESS",
                ],
            ),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system",
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

    module.exit_json(db_systems=result)


if __name__ == "__main__":
    main()
