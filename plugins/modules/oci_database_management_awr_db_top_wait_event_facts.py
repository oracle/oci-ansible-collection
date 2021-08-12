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
module: oci_database_management_awr_db_top_wait_event_facts
short_description: Fetches details about a AwrDbTopWaitEvent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AwrDbTopWaitEvent resource in Oracle Cloud Infrastructure
    - Summarizes the AWR top wait events.
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
        aliases: ["id"]
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
    session_type:
        description:
            - The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.
        type: str
        choices:
            - "FOREGROUND"
            - "BACKGROUND"
            - "ALL"
    container_id:
        description:
            - "The optional query parameter to filter the database container by an exact ID value.
              Note that the database container ID can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges"
        type: int
    top_n:
        description:
            - The optional query parameter to filter the number of top categories to be returned.
        type: int
    sort_by:
        description:
            - The option to sort the AWR top event summary data.
        type: str
        choices:
            - "WAITS_PERSEC"
            - "AVG_WAIT_TIME_PERSEC"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Descending order is the the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific awr_db_top_wait_event
  oci_database_management_awr_db_top_wait_event_facts:
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    awr_db_id: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
awr_db_top_wait_event:
    description:
        - AwrDbTopWaitEvent resource
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the event.
            returned: on success
            type: string
            sample: name_example
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
    sample: {
        "name": "name_example",
        "waits_per_sec": 1.2,
        "avg_wait_time_per_sec": 1.2
    }
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


class AwrDbTopWaitEventFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "awr_db_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "session_type",
            "container_id",
            "top_n",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_awr_db_top_wait_events,
            managed_database_id=self.module.params.get("managed_database_id"),
            awr_db_id=self.module.params.get("awr_db_id"),
            **optional_kwargs
        )


AwrDbTopWaitEventFactsHelperCustom = get_custom_class(
    "AwrDbTopWaitEventFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDbTopWaitEventFactsHelperCustom, AwrDbTopWaitEventFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            awr_db_id=dict(aliases=["id"], type="str", required=True),
            inst_num=dict(type="str"),
            begin_sn_id_greater_than_or_equal_to=dict(type="int"),
            end_sn_id_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            session_type=dict(type="str", choices=["FOREGROUND", "BACKGROUND", "ALL"]),
            container_id=dict(type="int"),
            top_n=dict(type="int"),
            sort_by=dict(type="str", choices=["WAITS_PERSEC", "AVG_WAIT_TIME_PERSEC"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db_top_wait_event",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_db_top_wait_event=result)


if __name__ == "__main__":
    main()
