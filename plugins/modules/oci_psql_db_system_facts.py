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
module: oci_psql_db_system_facts
short_description: Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
    - Returns a list of database systems.
    - If I(db_system_id) is specified, the details of a single DbSystem will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - A unique identifier for the database system.
            - Required to get a specific db_system.
        type: str
        aliases: ["id"]
    excluded_fields:
        description:
            - A filter to exclude database configuration when this query parameter is set to OverrideDbConfig.
        type: list
        elements: str
        choices:
            - "dbConfigurationParams"
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources if their `lifecycleState` matches the given `lifecycleState`.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_system
  oci_psql_db_system_facts:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    excluded_fields: [ "dbConfigurationParams" ]

- name: List db_systems
  oci_psql_db_system_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
db_systems:
    description:
        - List of DbSystem resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A description of the database system.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        admin_username:
            description:
                - The database system administrator username.
                - Returned for get operation
            returned: on success
            type: str
            sample: admin_username_example
        instances:
            description:
                - The list of instances, or nodes, in the database system.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - A unique identifier for the database instance node. Immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - A user-friendly display name for the database instance node. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description of the database instance node.
                    returned: on success
                    type: str
                    sample: description_example
                availability_domain:
                    description:
                        - The availability domain in which the database instance node is located.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                lifecycle_state:
                    description:
                        - The current state of the database instance node.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_created:
                    description:
                        - The date and time that the database instance node was created, expressed in
                          L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the database instance node was updated, expressed in
                          L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        storage_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                system_type:
                    description:
                        - Type of the database system.
                    returned: on success
                    type: str
                    sample: OCI_OPTIMIZED_STORAGE
                is_regionally_durable:
                    description:
                        - Specifies if the block volume used for the database system is regional or AD-local.
                          If not specified, it will be set to false.
                          If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                          If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                    returned: on success
                    type: bool
                    sample: true
                availability_domain:
                    description:
                        - Specifies the availability domain of AD-local storage.
                          If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                          If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                iops:
                    description:
                        - Guaranteed input/output storage requests per second (IOPS) available to the database system.
                    returned: on success
                    type: int
                    sample: 56
        network_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer subnet associated with the database
                          system.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                primary_db_endpoint_private_ip:
                    description:
                        - Private IP in customer subnet. The value is optional.
                          If the IP is not provided, the IP will be chosen from the available IP addresses from the specified subnet.
                    returned: on success
                    type: str
                    sample: primary_db_endpoint_private_ip_example
                nsg_ids:
                    description:
                        - List of customer Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated
                          with the database system.
                    returned: on success
                    type: list
                    sample: []
        management_policy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                maintenance_window_start:
                    description:
                        - The start of the maintenance window.
                    returned: on success
                    type: str
                    sample: maintenance_window_start_example
                backup_policy:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        days_of_the_month:
                            description:
                                - Day of the month when the backup should start.
                                  To ensure that the backup runs monthly, the latest day of the month that you can use to schedule a backup is the the 28th day.
                            returned: on success
                            type: list
                            sample: []
                        kind:
                            description:
                                - The kind of backup policy.
                            returned: on success
                            type: str
                            sample: DAILY
                        retention_days:
                            description:
                                - How many days the data should be stored after the database system deletion.
                            returned: on success
                            type: int
                            sample: 56
                        days_of_the_week:
                            description:
                                - The day of the week that the backup starts.
                            returned: on success
                            type: list
                            sample: []
                        backup_start:
                            description:
                                - Hour of the day when the backup starts.
                            returned: on success
                            type: str
                            sample: backup_start_example
        source:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                backup_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system backup.
                    returned: on success
                    type: str
                    sample: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
                is_having_restore_config_overrides:
                    description:
                        - Deprecated. Don't use.
                    returned: on success
                    type: bool
                    sample: true
                source_type:
                    description:
                        - The source descriminator.
                    returned: on success
                    type: str
                    sample: BACKUP
        id:
            description:
                - A unique identifier for the database system. Immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the database system. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the database system.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time that the database system was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that the database system was updated, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the database system.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        system_type:
            description:
                - Type of the database system.
            returned: on success
            type: str
            sample: OCI_OPTIMIZED_STORAGE
        instance_count:
            description:
                - Count of instances, or nodes, in the database system.
            returned: on success
            type: int
            sample: 56
        shape:
            description:
                - "The name of the shape for the database instance.
                  Example: `VM.Standard.E4.Flex`"
            returned: on success
            type: str
            sample: shape_example
        instance_ocpu_count:
            description:
                - The total number of OCPUs available to each database instance node.
            returned: on success
            type: int
            sample: 56
        instance_memory_size_in_gbs:
            description:
                - The total amount of memory available to each database instance node, in gigabytes.
            returned: on success
            type: int
            sample: 56
        db_version:
            description:
                - The major and minor versions of the database system software.
            returned: on success
            type: str
            sample: db_version_example
        config_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration associated with the database system.
            returned: on success
            type: str
            sample: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
    sample: [{
        "description": "description_example",
        "admin_username": "admin_username_example",
        "instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "storage_details": {
            "system_type": "OCI_OPTIMIZED_STORAGE",
            "is_regionally_durable": true,
            "availability_domain": "Uocm:PHX-AD-1",
            "iops": 56
        },
        "network_details": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "primary_db_endpoint_private_ip": "primary_db_endpoint_private_ip_example",
            "nsg_ids": []
        },
        "management_policy": {
            "maintenance_window_start": "maintenance_window_start_example",
            "backup_policy": {
                "days_of_the_month": [],
                "kind": "DAILY",
                "retention_days": 56,
                "days_of_the_week": [],
                "backup_start": "backup_start_example"
            }
        },
        "source": {
            "backup_id": "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx",
            "is_having_restore_config_overrides": true,
            "source_type": "BACKUP"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "system_type": "OCI_OPTIMIZED_STORAGE",
        "instance_count": 56,
        "shape": "shape_example",
        "instance_ocpu_count": 56,
        "instance_memory_size_in_gbs": 56,
        "db_version": "db_version_example",
        "config_id": "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.psql import PostgresqlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlDbSystemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "excluded_fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_systems, **optional_kwargs
        )


PsqlDbSystemFactsHelperCustom = get_custom_class("PsqlDbSystemFactsHelperCustom")


class ResourceFactsHelper(PsqlDbSystemFactsHelperCustom, PsqlDbSystemFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_system_id=dict(aliases=["id"], type="str"),
            excluded_fields=dict(
                type="list", elements="str", choices=["dbConfigurationParams"]
            ),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system",
        service_client_class=PostgresqlClient,
        namespace="psql",
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
