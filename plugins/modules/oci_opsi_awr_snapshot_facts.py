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
module: oci_opsi_awr_snapshot_facts
short_description: Fetches details about one or multiple AwrSnapshot resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrSnapshot resources in Oracle Cloud Infrastructure
    - Lists AWR snapshots for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should
      not exceed an elapsed range of 1 day.
      The timeGreaterThanOrEqualTo & timeLessThanOrEqualTo params are optional. If these params are not provided, by default last 1 day snapshots will be
      returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    awr_hub_id:
        description:
            - Unique Awr Hub identifier
        type: str
        required: true
    awr_source_database_identifier:
        description:
            - AWR source database identifier.
        type: str
        required: true
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
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The option to sort the AWR snapshot summary data. Default sort is by timeBegin.
        type: str
        choices:
            - "timeBegin"
            - "snapshotId"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List awr_snapshots
  oci_opsi_awr_snapshot_facts:
    # required
    awr_hub_id: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"
    awr_source_database_identifier: awr_source_database_identifier_example

    # optional
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeBegin

"""

RETURN = """
awr_snapshots:
    description:
        - List of AwrSnapshot resources
    returned: on success
    type: complex
    contains:
        awr_source_database_id:
            description:
                - DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.
            returned: on success
            type: str
            sample: "ocid1.awrsourcedatabase.oc1..xxxxxxEXAMPLExxxxxx"
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
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_snapshot_begin:
            description:
                - The start time of the snapshot.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_snapshot_end:
            description:
                - The end time of the snapshot.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        snapshot_identifier:
            description:
                - The identifier of the snapshot.
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
        "awr_source_database_id": "ocid1.awrsourcedatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_number": 56,
        "time_db_startup": "2013-10-20T19:20:30+01:00",
        "time_snapshot_begin": "2013-10-20T19:20:30+01:00",
        "time_snapshot_end": "2013-10-20T19:20:30+01:00",
        "snapshot_identifier": 56,
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
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AwrSnapshotFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "awr_hub_id",
            "awr_source_database_identifier",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_awr_snapshots,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            awr_source_database_identifier=self.module.params.get(
                "awr_source_database_identifier"
            ),
            **optional_kwargs
        )


AwrSnapshotFactsHelperCustom = get_custom_class("AwrSnapshotFactsHelperCustom")


class ResourceFactsHelper(AwrSnapshotFactsHelperCustom, AwrSnapshotFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            awr_hub_id=dict(type="str", required=True),
            awr_source_database_identifier=dict(type="str", required=True),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeBegin", "snapshotId"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_snapshot",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_snapshots=result)


if __name__ == "__main__":
    main()
