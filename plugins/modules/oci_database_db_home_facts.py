#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_db_home_facts
short_description: Fetches details about one or multiple DbHome resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbHome resources in Oracle Cloud Infrastructure
    - Lists the Database Homes in the specified DB system and compartment. A Database Home is a directory where Oracle Database software is installed.
    - If I(db_home_id) is specified, the details of a single DbHome will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_home_id:
        description:
            - The Database Home L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_home.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple db_homes.
        type: str
    db_system_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of
              database versions which are supported for the DB system.
        type: str
    vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
        type: str
    backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup. Specify a backupId to list only the DB systems
              or DB homes that support creating a database using this backup in this compartment.
        type: str
    db_version:
        description:
            - A filter to return only DB Homes that match the specified dbVersion.
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
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_home
  oci_database_db_home_facts:
    # required
    db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_homes
  oci_database_db_home_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
    db_version: db_version_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING
    display_name: display_name_example

"""

RETURN = """
db_homes:
    description:
        - List of DbHome resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
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
                - The user-provided name for the Database Home. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        last_patch_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch history. This value is updated as soon as
                  a patch operation is started.
            returned: on success
            type: str
            sample: "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the Database Home.
            returned: on success
            type: str
            sample: PROVISIONING
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
            returned: on success
            type: str
            sample: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        db_version:
            description:
                - The Oracle Database version.
            returned: on success
            type: str
            sample: db_version_example
        db_home_location:
            description:
                - The location of the Oracle Database Home.
            returned: on success
            type: str
            sample: db_home_location_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the Database Home was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        one_off_patches:
            description:
                - List of one-off patches for Database Homes.
            returned: on success
            type: list
            sample: []
        database_software_image_id:
            description:
                - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            returned: on success
            type: str
            sample: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "last_patch_history_entry_id": "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "db_version": "db_version_example",
        "db_home_location": "db_home_location_example",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "one_off_patches": [],
        "database_software_image_id": "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
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


class DbHomeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_home_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_home, db_home_id=self.module.params.get("db_home_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "db_system_id",
            "vm_cluster_id",
            "backup_id",
            "db_version",
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
            self.client.list_db_homes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DbHomeFactsHelperCustom = get_custom_class("DbHomeFactsHelperCustom")


class ResourceFactsHelper(DbHomeFactsHelperCustom, DbHomeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_home_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            db_system_id=dict(type="str"),
            vm_cluster_id=dict(type="str"),
            backup_id=dict(type="str"),
            db_version=dict(type="str"),
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
        resource_type="db_home",
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

    module.exit_json(db_homes=result)


if __name__ == "__main__":
    main()
