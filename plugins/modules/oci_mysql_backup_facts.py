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
module: oci_mysql_backup_facts
short_description: Fetches details about one or multiple Backup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Backup resources in Oracle Cloud Infrastructure
    - Get a list of DB System backups.
    - If I(backup_id) is specified, the details of a single Backup will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    backup_id:
        description:
            - The OCID of the Backup
            - Required to get a specific backup.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple backups.
        type: str
    lifecycle_state:
        description:
            - Backup Lifecycle State
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    display_name:
        description:
            - A filter to return only the resource matching the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use (ASC or DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List backups
  oci_mysql_backup_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific backup
  oci_mysql_backup_facts:
    backup_id: ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
backups:
    description:
        - List of Backup resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the backup itself
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-supplied display name for the backup.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - A user-supplied description for the backup.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The time the backup record was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time at which the backup was updated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The state of the backup.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        backup_type:
            description:
                - The type of backup.
            returned: on success
            type: string
            sample: FULL
        creation_type:
            description:
                - If the backup was created automatically, or by a manual request.
            returned: on success
            type: string
            sample: MANUAL
        db_system_id:
            description:
                - The OCID of the DB System the backup is associated with.
            returned: on success
            type: string
            sample: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
        backup_size_in_gbs:
            description:
                - The size of the backup in base-2 (IEC) gibibytes. (GiB).
            returned: on success
            type: int
            sample: 56
        retention_in_days:
            description:
                - Number of days to retain this backup.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_gbs:
            description:
                - Initial size of the data volume in GiBs.
            returned: on success
            type: int
            sample: 56
        mysql_version:
            description:
                - The MySQL server version of the DB System used for backup.
            returned: on success
            type: string
            sample: mysql_version_example
        shape_name:
            description:
                - The shape of the DB System used for backup.
            returned: on success
            type: string
            sample: shape_name_example
        freeform_tags:
            description:
                - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "backup_type": "FULL",
        "creation_type": "MANUAL",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_size_in_gbs": 56,
        "retention_in_days": 56,
        "data_storage_size_in_gbs": 56,
        "mysql_version": "mysql_version_example",
        "shape_name": "shape_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import DbBackupsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlBackupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "backup_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup, backup_id=self.module.params.get("backup_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "backup_id",
            "lifecycle_state",
            "db_system_id",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_backups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlBackupFactsHelperCustom = get_custom_class("MysqlBackupFactsHelperCustom")


class ResourceFactsHelper(MysqlBackupFactsHelperCustom, MysqlBackupFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            db_system_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "displayName"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backup",
        service_client_class=DbBackupsClient,
        namespace="mysql",
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
