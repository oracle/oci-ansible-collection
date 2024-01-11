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
module: oci_recovery_protected_database_facts
short_description: Fetches details about one or multiple ProtectedDatabase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProtectedDatabase resources in Oracle Cloud Infrastructure
    - Lists the protected databases based on the specified parameters.
    - If I(protected_database_id) is specified, the details of a single ProtectedDatabase will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    protected_database_id:
        description:
            - The protected database OCID.
            - Required to get a specific protected_database.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment OCID.
            - Required to list multiple protected_databases.
        type: str
    lifecycle_state:
        description:
            - A filter to return only the resources that match the specified lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire 'displayname' given.
        type: str
        aliases: ["name"]
    protection_policy_id:
        description:
            - The protection policy OCID.
        type: str
    recovery_service_subnet_id:
        description:
            - The recovery service subnet OCID.
        type: str
    sort_order:
        description:
            - "The sort order to use, either ascending (ASC) or descending (DESC).
              Allowed values are:
                - ASC
                - DESC"
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If you do not specify a value, then TIMECREATED is used as the default sort order.
              Allowed values are:
                - TIMECREATED
                - DISPLAYNAME"
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific protected_database
  oci_recovery_protected_database_facts:
    # required
    protected_database_id: "ocid1.protecteddatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List protected_databases
  oci_recovery_protected_database_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    recovery_service_subnet_id: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
protected_databases:
    description:
        - List of ProtectedDatabase resources
    returned: on success
    type: complex
    contains:
        database_size_in_gbs:
            description:
                - The size of the database in GBs, in gigabytes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        change_rate:
            description:
                - The percentage of data changes that exist in the database between successive incremental backups.
                - Returned for get operation
            returned: on success
            type: float
            sample: 1.2
        compression_ratio:
            description:
                - The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.
                - Returned for get operation
            returned: on success
            type: float
            sample: 1.2
        is_redo_logs_shipped:
            description:
                - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected
                  database to Recovery Service.
                  Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.
                  For this to be effective, additional
                  configuration is needed on client side.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        id:
            description:
                - The OCID of the protected database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The protected database name. You can change the displayName. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the protected database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_unique_name:
            description:
                - The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.
            returned: on success
            type: str
            sample: db_unique_name_example
        vpc_user_name:
            description:
                - The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.
            returned: on success
            type: str
            sample: vpc_user_name_example
        database_size:
            description:
                - "The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater
                  than 5TB."
            returned: on success
            type: str
            sample: XS
        protection_policy_id:
            description:
                - The OCID of the protection policy associated with the protected database.
            returned: on success
            type: str
            sample: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        recovery_service_subnets:
            description:
                - List of recovery service subnet resources associated with the protected database.
            returned: on success
            type: complex
            contains:
                recovery_service_subnet_id:
                    description:
                        - Recovery Service Subnet Identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the Recovery Service Subnet.
                    returned: on success
                    type: str
                    sample: CREATING
        database_id:
            description:
                - The OCID of the protected database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Protected Database.
            returned: on success
            type: str
            sample: CREATING
        health:
            description:
                - "Indicates the protection status of the database. Allowed values are:
                   - HEALTHY
                   - WARNING
                   - ALERT"
                - "A 'HEALTHY' status indicates that Recovery Service can ensure database recovery to any point in time within the entire recovery window. The
                  potential data loss exposure since the last backup is:
                   - Less than 10 seconds, if Real-time data protection is enabled
                   - Less than 70 minutes if Real-time data protection is disabled"
                - "A 'WARNING' status indicates that Recovery Service can ensure database recovery within the current recovery window - 1 day. The potential
                  data loss exposure since the last backup is:
                   - Greater than 10 seconds, if Real-time data protection is enabled
                   - Greater than 60 minutes, if if Real-time data protection is disabled"
                - An 'ALERT' status indicates that Recovery Service cannot recover the database within the current recovery window.
            returned: on success
            type: str
            sample: PROTECTED
        lifecycle_details:
            description:
                - Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable
                  information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        health_details:
            description:
                - A message describing the current health of the protected database.
            returned: on success
            type: str
            sample: health_details_example
        is_read_only_resource:
            description:
                - Indicates whether the protected database is created by Recovery Service or created manually.
                  Set to <b>TRUE</b> for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set
                  Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource.
                  Set to <b>FALSE</b> for a user-defined protected database.
            returned: on success
            type: bool
            sample: true
        metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_space_used_in_gbs:
                    description:
                        - Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.
                    returned: on success
                    type: float
                    sample: 3.4
                backup_space_estimate_in_gbs:
                    description:
                        - The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the
                          protected database.
                    returned: on success
                    type: float
                    sample: 3.4
                unprotected_window_in_seconds:
                    description:
                        - This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is
                          available.
                          This is the time we received the last backup or last redo-log shipped.
                    returned: on success
                    type: float
                    sample: 3.4
                db_size_in_gbs:
                    description:
                        - The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the
                          catalog, and does not include archive logs.
                    returned: on success
                    type: float
                    sample: 3.4
                is_redo_logs_enabled:
                    description:
                        - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the
                          protected database to Recovery Service.
                          Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log
                          backups.
                    returned: on success
                    type: bool
                    sample: true
                retention_period_in_days:
                    description:
                        - The maximum number of days to retain backups for a protected database.
                    returned: on success
                    type: float
                    sample: 3.4
                current_retention_period_in_seconds:
                    description:
                        - Number of seconds backups are currently retained for this database.
                    returned: on success
                    type: float
                    sample: 3.4
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "database_size_in_gbs": 56,
        "change_rate": 1.2,
        "compression_ratio": 1.2,
        "is_redo_logs_shipped": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_unique_name": "db_unique_name_example",
        "vpc_user_name": "vpc_user_name_example",
        "database_size": "XS",
        "protection_policy_id": "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "recovery_service_subnets": [{
            "recovery_service_subnet_id": "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING"
        }],
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "health": "PROTECTED",
        "lifecycle_details": "lifecycle_details_example",
        "health_details": "health_details_example",
        "is_read_only_resource": true,
        "metrics": {
            "backup_space_used_in_gbs": 3.4,
            "backup_space_estimate_in_gbs": 3.4,
            "unprotected_window_in_seconds": 3.4,
            "db_size_in_gbs": 3.4,
            "is_redo_logs_enabled": true,
            "retention_period_in_days": 3.4,
            "current_retention_period_in_seconds": 3.4
        },
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
    from oci.recovery import DatabaseRecoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectedDatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "protected_database_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protected_database,
            protected_database_id=self.module.params.get("protected_database_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "protection_policy_id",
            "recovery_service_subnet_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_protected_databases,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProtectedDatabaseFactsHelperCustom = get_custom_class(
    "ProtectedDatabaseFactsHelperCustom"
)


class ResourceFactsHelper(
    ProtectedDatabaseFactsHelperCustom, ProtectedDatabaseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            protected_database_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            protection_policy_id=dict(type="str"),
            recovery_service_subnet_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protected_database",
        service_client_class=DatabaseRecoveryClient,
        namespace="recovery",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(protected_databases=result)


if __name__ == "__main__":
    main()
