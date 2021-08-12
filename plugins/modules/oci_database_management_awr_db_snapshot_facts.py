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
module: oci_database_management_awr_db_snapshot_facts
short_description: Fetches details about one or multiple AwrDbSnapshot resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrDbSnapshot resources in Oracle Cloud Infrastructure
    - Lists AWR snapshots for the specified database in the AWR.
version_added: "2.9"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    awr_db_id:
        description:
            - "The parameter to filter the database by internal ID.
              Note that the internal ID of the database can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbs:"
        type: str
        required: true
    inst_num:
        description:
            - The optional single value query parameter to filter the database instance number.
        type: str
    begin_sn_id_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to filter on the snapshot ID.
        type: int
    end_sn_id_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the snapshot ID.
        type: int
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to query parameter to filter the timestamp.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the timestamp.
        type: str
    container_id:
        description:
            - "The optional query parameter to filter the database container by an exact ID value.
              Note that the database container ID can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges"
        type: int
    sort_by:
        description:
            - The option to sort the AWR snapshot summary data.
        type: str
        choices:
            - "TIME_BEGIN"
            - "SNAPSHOT_ID"
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
- name: List awr_db_snapshots
  oci_database_management_awr_db_snapshot_facts:
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    awr_db_id: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
awr_db_snapshots:
    description:
        - List of AwrDbSnapshot resources
    returned: on success
    type: complex
    contains:
        awr_db_id:
            description:
                - "Internal ID of the database. The internal ID of the database is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbs"
            returned: on success
            type: string
            sample: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"
        instance_number:
            description:
                - The database instance number.
            returned: on success
            type: int
            sample: 56
        time_db_startup:
            description:
                - The timestamp of the database startup.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_begin:
            description:
                - The start time of the snapshot.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_end:
            description:
                - The end time of the snapshot.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        snapshot_id:
            description:
                - "The ID of the snapshot. The snapshot ID is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots"
            returned: on success
            type: int
            sample: 56
        error_count:
            description:
                - The total number of errors.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "awr_db_id": "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_number": 56,
        "time_db_startup": "2013-10-20T19:20:30+01:00",
        "time_begin": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "snapshot_id": 56,
        "error_count": 56
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


class AwrDbSnapshotFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "awr_db_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "container_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_awr_db_snapshots,
            managed_database_id=self.module.params.get("managed_database_id"),
            awr_db_id=self.module.params.get("awr_db_id"),
            **optional_kwargs
        )


AwrDbSnapshotFactsHelperCustom = get_custom_class("AwrDbSnapshotFactsHelperCustom")


class ResourceFactsHelper(AwrDbSnapshotFactsHelperCustom, AwrDbSnapshotFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            awr_db_id=dict(type="str", required=True),
            inst_num=dict(type="str"),
            begin_sn_id_greater_than_or_equal_to=dict(type="int"),
            end_sn_id_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            container_id=dict(type="int"),
            sort_by=dict(type="str", choices=["TIME_BEGIN", "SNAPSHOT_ID"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db_snapshot",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_db_snapshots=result)


if __name__ == "__main__":
    main()
