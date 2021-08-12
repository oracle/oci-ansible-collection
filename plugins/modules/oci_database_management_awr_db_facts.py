#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_management_awr_db_facts
short_description: Fetches details about one or multiple AwrDb resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrDb resources in Oracle Cloud Infrastructure
    - Gets the list of databases and their snapshot summary details available in the AWR of the specified Managed Database.
version_added: "2.9"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    name:
        description:
            - The optional single value query parameter to filter the entity name.
        type: str
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to query parameter to filter the timestamp.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the timestamp.
        type: str
    sort_by:
        description:
            - The option to sort the AWR summary data.
        type: str
        choices:
            - "END_INTERVAL_TIME"
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Descending order is the the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List awr_dbs
  oci_database_management_awr_db_facts:
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
awr_dbs:
    description:
        - List of AwrDb resources
    returned: on success
    type: complex
    contains:
        awr_db_id:
            description:
                - "The internal ID of the database. The internal ID of the database is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbs"
            returned: on success
            type: string
            sample: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"
        db_name:
            description:
                - The name of the database.
            returned: on success
            type: string
            sample: db_name_example
        instance_list:
            description:
                - The database instance numbers.
            returned: on success
            type: list
            sample: []
        time_db_startup:
            description:
                - The timestamp of the database startup.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_first_snapshot_begin:
            description:
                - The start time of the earliest snapshot.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_latest_snapshot_end:
            description:
                - The end time of the latest snapshot.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        first_snapshot_id:
            description:
                - "The ID of the earliest snapshot. The snapshot ID is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots"
            returned: on success
            type: int
            sample: 56
        latest_snapshot_id:
            description:
                - "The ID of the latest snapshot. The snapshot ID is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots"
            returned: on success
            type: int
            sample: 56
        snapshot_count:
            description:
                - The total number of snapshots.
            returned: on success
            type: int
            sample: 56
        snapshot_interval_in_min:
            description:
                - The interval time between snapshots (in minutes).
            returned: on success
            type: int
            sample: 56
        container_id:
            description:
                - "ID of the database container. The database container ID is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges"
            returned: on success
            type: int
            sample: 56
        db_version:
            description:
                - The version of the database.
            returned: on success
            type: string
            sample: db_version_example
        snapshot_timezone:
            description:
                - The time zone of the snapshot.
            returned: on success
            type: string
            sample: snapshot_timezone_example
    sample: [{
        "awr_db_id": "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx",
        "db_name": "db_name_example",
        "instance_list": [],
        "time_db_startup": "2013-10-20T19:20:30+01:00",
        "time_first_snapshot_begin": "2013-10-20T19:20:30+01:00",
        "time_latest_snapshot_end": "2013-10-20T19:20:30+01:00",
        "first_snapshot_id": 56,
        "latest_snapshot_id": 56,
        "snapshot_count": 56,
        "snapshot_interval_in_min": 56,
        "container_id": 56,
        "db_version": "db_version_example",
        "snapshot_timezone": "snapshot_timezone_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AwrDbFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_awr_dbs,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


AwrDbFactsHelperCustom = get_custom_class("AwrDbFactsHelperCustom")


class ResourceFactsHelper(AwrDbFactsHelperCustom, AwrDbFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            name=dict(type="str"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            sort_by=dict(type="str", choices=["END_INTERVAL_TIME", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_dbs=result)


if __name__ == "__main__":
    main()
