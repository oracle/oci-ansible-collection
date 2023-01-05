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
module: oci_database_autonomous_database_backup_facts
short_description: Fetches details about one or multiple AutonomousDatabaseBackup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousDatabaseBackup resources in Oracle Cloud Infrastructure
    - Gets a list of Autonomous Database backups based on either the `autonomousDatabaseId` or `compartmentId` specified as a query parameter.
    - If I(autonomous_database_backup_id) is specified, the details of a single AutonomousDatabaseBackup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_database_backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.
            - Required to get a specific autonomous_database_backup.
        type: str
        aliases: ["id"]
    autonomous_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
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
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_database_backup
  oci_database_autonomous_database_backup_facts:
    # required
    autonomous_database_backup_id: "ocid1.autonomousdatabasebackup.oc1..xxxxxxEXAMPLExxxxxx"

- name: List autonomous_database_backups
  oci_database_autonomous_database_backup_facts:

    # optional
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: CREATING
    display_name: display_name_example

"""

RETURN = """
autonomous_database_backups:
    description:
        - List of AutonomousDatabaseBackup resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the backup. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - The type of backup.
            returned: on success
            type: str
            sample: INCREMENTAL
        is_automatic:
            description:
                - Indicates whether the backup is user-initiated or automatic.
            returned: on success
            type: bool
            sample: true
        time_started:
            description:
                - The date and time the backup started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time the backup completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        database_size_in_tbs:
            description:
                - The size of the database in terabytes at the time the backup was taken.
            returned: on success
            type: float
            sample: 10
        lifecycle_state:
            description:
                - The current state of the backup.
            returned: on success
            type: str
            sample: CREATING
        is_restorable:
            description:
                - Indicates whether the backup can be used to restore the associated Autonomous Database.
            returned: on success
            type: bool
            sample: true
        key_store_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the key store.
            returned: on success
            type: str
            sample: "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx"
        key_store_wallet_name:
            description:
                - The wallet name for Oracle Key Vault.
            returned: on success
            type: str
            sample: key_store_wallet_name_example
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        vault_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                  L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id:
            description:
                - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                  versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
            returned: on success
            type: str
            sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_database_id": "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "INCREMENTAL",
        "is_automatic": true,
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "database_size_in_tbs": 10,
        "lifecycle_state": "CREATING",
        "is_restorable": true,
        "key_store_id": "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx",
        "key_store_wallet_name": "key_store_wallet_name_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseBackupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "autonomous_database_backup_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database_backup,
            autonomous_database_backup_id=self.module.params.get(
                "autonomous_database_backup_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "autonomous_database_id",
            "compartment_id",
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
            self.client.list_autonomous_database_backups, **optional_kwargs
        )


AutonomousDatabaseBackupFactsHelperCustom = get_custom_class(
    "AutonomousDatabaseBackupFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDatabaseBackupFactsHelperCustom, AutonomousDatabaseBackupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_database_backup_id=dict(aliases=["id"], type="str"),
            autonomous_database_id=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_database_backup",
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

    module.exit_json(autonomous_database_backups=result)


if __name__ == "__main__":
    main()
