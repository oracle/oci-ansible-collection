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
module: oci_opsi_awr_database_wait_event_facts
short_description: Fetches details about one or multiple AwrDatabaseWaitEvent resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrDatabaseWaitEvent resources in Oracle Cloud Infrastructure
    - Summarizes the AWR wait event sample data for the specified database in the AWR. The event data is summarized based on the Time dimension for each event.
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
            - "The internal ID of the database. The internal ID of the database is not the
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
              It can be retrieved from the following endpoint:
              /awrHubs/{awrHubId}/awrDatabases"
        type: str
        required: true
    instance_number:
        description:
            - The optional single value query parameter to filter by database instance number.
        type: str
    begin_snapshot_identifier_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to filter on the snapshot ID.
        type: int
    end_snapshot_identifier_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the snapshot Identifier.
        type: int
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
    name:
        description:
            - The optional multiple value query parameter to filter the entity name.
        type: list
        elements: str
    session_type:
        description:
            - The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.
        type: str
        choices:
            - "FOREGROUND"
            - "BACKGROUND"
            - "ALL"
    sort_by:
        description:
            - The option to sort the data within a time period.
        type: str
        choices:
            - "TIME_BEGIN"
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
- name: List awr_database_wait_events
  oci_opsi_awr_database_wait_event_facts:
    # required
    awr_hub_id: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"
    awr_source_database_identifier: awr_source_database_identifier_example

    # optional
    instance_number: instance_number_example
    begin_snapshot_identifier_greater_than_or_equal_to: 56
    end_snapshot_identifier_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    name: [ "name_example" ]
    session_type: FOREGROUND
    sort_by: TIME_BEGIN
    sort_order: ASC

"""

RETURN = """
awr_database_wait_events:
    description:
        - List of AwrDatabaseWaitEvent resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the event.
            returned: on success
            type: str
            sample: name_example
        time_begin:
            description:
                - The begin time of the wait event.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - The end time of the wait event.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        waits_per_sec:
            description:
                - The wait count per second.
            returned: on success
            type: float
            sample: 1.2
        avg_wait_time_per_sec:
            description:
                - The average wait time per second.
            returned: on success
            type: float
            sample: 1.2
        snapshot_identifier:
            description:
                - "The ID of the snapshot. The snapshot identifier is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /awrHubs/{awrHubId}/awrDatabaseSnapshots"
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "time_begin": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "waits_per_sec": 1.2,
        "avg_wait_time_per_sec": 1.2,
        "snapshot_identifier": 56
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


class AwrDatabaseWaitEventFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "awr_hub_id",
            "awr_source_database_identifier",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "instance_number",
            "begin_snapshot_identifier_greater_than_or_equal_to",
            "end_snapshot_identifier_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "name",
            "session_type",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_awr_database_wait_events,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            awr_source_database_identifier=self.module.params.get(
                "awr_source_database_identifier"
            ),
            **optional_kwargs
        )


AwrDatabaseWaitEventFactsHelperCustom = get_custom_class(
    "AwrDatabaseWaitEventFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDatabaseWaitEventFactsHelperCustom, AwrDatabaseWaitEventFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            awr_hub_id=dict(type="str", required=True),
            awr_source_database_identifier=dict(type="str", required=True),
            instance_number=dict(type="str"),
            begin_snapshot_identifier_greater_than_or_equal_to=dict(type="int"),
            end_snapshot_identifier_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            name=dict(type="list", elements="str"),
            session_type=dict(type="str", choices=["FOREGROUND", "BACKGROUND", "ALL"]),
            sort_by=dict(type="str", choices=["TIME_BEGIN", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_database_wait_event",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_database_wait_events=result)


if __name__ == "__main__":
    main()
