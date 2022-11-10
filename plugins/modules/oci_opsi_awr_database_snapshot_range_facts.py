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
module: oci_opsi_awr_database_snapshot_range_facts
short_description: Fetches details about one or multiple AwrDatabaseSnapshotRange resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrDatabaseSnapshotRange resources in Oracle Cloud Infrastructure
    - Summarizes the AWR snapshot ranges that contain continuous snapshots, for the specified AWRHub.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    awr_hub_id:
        description:
            - Unique Awr Hub identifier
        type: str
        required: true
    name:
        description:
            - The optional single value query parameter to filter the entity name.
        type: str
    time_greater_than_or_equal_to:
        description:
            - "The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ,
              example 2020-12-03T19:00:53Z"
        type: str
    time_less_than_or_equal_to:
        description:
            - "The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example
              2020-12-03T19:00:53Z"
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
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List awr_database_snapshot_ranges
  oci_opsi_awr_database_snapshot_range_facts:
    # required
    awr_hub_id: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    sort_by: END_INTERVAL_TIME
    sort_order: ASC

"""

RETURN = """
awr_database_snapshot_ranges:
    description:
        - List of AwrDatabaseSnapshotRange resources
    returned: on success
    type: complex
    contains:
        awr_source_database_identifier:
            description:
                - "The internal ID of the database. The internal ID of the database is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /awrHubs/{awrHubId}/awrDatabases"
            returned: on success
            type: str
            sample: awr_source_database_identifier_example
        db_name:
            description:
                - The name of the database.
            returned: on success
            type: str
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
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_first_snapshot_begin:
            description:
                - The start time of the earliest snapshot.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_latest_snapshot_end:
            description:
                - The end time of the latest snapshot.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        first_snapshot_identifier:
            description:
                - "The ID of the earliest snapshot. The snapshot identifier is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /awrHubs/{awrHubId}/awrDatabaseSnapshots"
            returned: on success
            type: int
            sample: 56
        latest_snapshot_identifier:
            description:
                - "The ID of the latest snapshot. The snapshot identifier is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /awrHubs/{awrHubId}/awrDatabaseSnapshots"
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
        db_version:
            description:
                - The version of the database.
            returned: on success
            type: str
            sample: db_version_example
        snapshot_timezone:
            description:
                - "The time zone of the snapshot. sample -  snapshotTimezone=+0 00:00:00"
            returned: on success
            type: str
            sample: snapshot_timezone_example
    sample: [{
        "awr_source_database_identifier": "awr_source_database_identifier_example",
        "db_name": "db_name_example",
        "instance_list": [],
        "time_db_startup": "2013-10-20T19:20:30+01:00",
        "time_first_snapshot_begin": "2013-10-20T19:20:30+01:00",
        "time_latest_snapshot_end": "2013-10-20T19:20:30+01:00",
        "first_snapshot_identifier": 56,
        "latest_snapshot_identifier": 56,
        "snapshot_count": 56,
        "snapshot_interval_in_min": 56,
        "db_version": "db_version_example",
        "snapshot_timezone": "snapshot_timezone_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AwrDatabaseSnapshotRangeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "awr_hub_id",
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
            self.client.summarize_awr_database_snapshot_ranges,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            **optional_kwargs
        )


AwrDatabaseSnapshotRangeFactsHelperCustom = get_custom_class(
    "AwrDatabaseSnapshotRangeFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDatabaseSnapshotRangeFactsHelperCustom, AwrDatabaseSnapshotRangeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            awr_hub_id=dict(type="str", required=True),
            name=dict(type="str"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            sort_by=dict(type="str", choices=["END_INTERVAL_TIME", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_database_snapshot_range",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_database_snapshot_ranges=result)


if __name__ == "__main__":
    main()
