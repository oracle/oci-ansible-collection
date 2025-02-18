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
module: oci_psql_backup_facts
short_description: Fetches details about one or multiple Backup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Backup resources in Oracle Cloud Infrastructure
    - Returns a list of backups.
    - If I(backup_id) is specified, the details of a single Backup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    time_started:
        description:
            - The start date for getting backups. An L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) formatted datetime string.
        type: str
    time_ended:
        description:
            - The end date for getting backups. An L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) formatted datetime string.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources if their `lifecycleState` matches the given `lifecycleState`.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    backup_id:
        description:
            - A unique identifier for the backup.
            - Required to get a specific backup.
        type: str
        aliases: ["id"]
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
- name: Get a specific backup
  oci_psql_backup_facts:
    # required
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"

- name: List backups
  oci_psql_backup_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    time_started: 2013-10-20T19:20:30+01:00
    time_ended: 2013-10-20T19:20:30+01:00
    lifecycle_state: CREATING
    display_name: display_name_example
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
backups:
    description:
        - List of Backup resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A description for the backup.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        db_system_details:
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
                    sample: system_type_example
                db_version:
                    description:
                        - The major and minor versions of the database system software.
                    returned: on success
                    type: str
                    sample: db_version_example
        last_accepted_request_token:
            description:
                - lastAcceptedRequestToken from MP.
                - Returned for get operation
            returned: on success
            type: str
            sample: last_accepted_request_token_example
        last_completed_request_token:
            description:
                - lastCompletedRequestToken from MP.
                - Returned for get operation
            returned: on success
            type: str
            sample: last_completed_request_token_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the backup. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the backup.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the backup was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the backup was updated, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the backup.
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
        source_type:
            description:
                - Specifies whether the backup was created manually, or by a management policy.
            returned: on success
            type: str
            sample: SCHEDULED
        backup_size:
            description:
                - The size of the backup, in gigabytes.
            returned: on success
            type: int
            sample: 56
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup's source database system.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        retention_period:
            description:
                - Backup retention period in days.
            returned: on success
            type: int
            sample: 56
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
        "db_system_details": {
            "system_type": "system_type_example",
            "db_version": "db_version_example"
        },
        "last_accepted_request_token": "last_accepted_request_token_example",
        "last_completed_request_token": "last_completed_request_token_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "source_type": "SCHEDULED",
        "backup_size": 56,
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "retention_period": 56,
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


class PsqlBackupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "backup_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup, backup_id=self.module.params.get("backup_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "time_started",
            "time_ended",
            "lifecycle_state",
            "display_name",
            "backup_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_backups, **optional_kwargs
        )


PsqlBackupFactsHelperCustom = get_custom_class("PsqlBackupFactsHelperCustom")


class ResourceFactsHelper(PsqlBackupFactsHelperCustom, PsqlBackupFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            time_started=dict(type="str"),
            time_ended=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            backup_id=dict(aliases=["id"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backup",
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

    module.exit_json(backups=result)


if __name__ == "__main__":
    main()
