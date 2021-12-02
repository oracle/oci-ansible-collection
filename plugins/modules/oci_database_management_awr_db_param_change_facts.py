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
module: oci_database_management_awr_db_param_change_facts
short_description: Fetches details about a AwrDbParamChange resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AwrDbParamChange resource in Oracle Cloud Infrastructure
    - "Summarizes the database parameter change history for one database parameter of the specified database in AWR. One change history record contains
      the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range,
      then multiple change history records are created for the same parameter.
      Note that this API only returns information on change history details for one database parameter.
      To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint:
      /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameters"
version_added: "2.9.0"
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
              /managedDatabases/{managedDatabaseId}/awrDbs"
        type: str
        aliases: ["id"]
        required: true
    name:
        description:
            - The required single value query parameter to filter the entity name.
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
            - The option to sort the AWR database parameter change history data.
        type: str
        choices:
            - "IS_CHANGED"
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Descending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific awr_db_param_change
  oci_database_management_awr_db_param_change_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    awr_db_id: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    inst_num: inst_num_example
    begin_sn_id_greater_than_or_equal_to: 56
    end_sn_id_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    container_id: 56
    sort_by: IS_CHANGED
    sort_order: ASC

"""

RETURN = """
awr_db_param_change:
    description:
        - AwrDbParamChange resource
    returned: on success
    type: complex
    contains:
        time_begin:
            description:
                - The start time of the interval.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - The end time of the interval.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        instance_number:
            description:
                - The database instance number.
            returned: on success
            type: int
            sample: 56
        previous_value:
            description:
                - The previous value of the database parameter.
            returned: on success
            type: str
            sample: previous_value_example
        value:
            description:
                - The current value of the database parameter.
            returned: on success
            type: str
            sample: value_example
        snapshot_id:
            description:
                - "The ID of the snapshot with the parameter value changed. The snapshot ID is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots"
            returned: on success
            type: int
            sample: 56
        value_modified:
            description:
                - "Indicates whether the parameter has been modified after instance startup:
                   - MODIFIED - Parameter has been modified with ALTER SESSION
                   - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions' values to be modified)
                   - FALSE - Parameter has not been modified after instance startup"
            returned: on success
            type: str
            sample: value_modified_example
        is_default:
            description:
                - Indicates whether the parameter value in the end snapshot is the default.
            returned: on success
            type: bool
            sample: true
    sample: {
        "time_begin": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "instance_number": 56,
        "previous_value": "previous_value_example",
        "value": "value_example",
        "snapshot_id": 56,
        "value_modified": "value_modified_example",
        "is_default": true
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


class AwrDbParamChangeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "awr_db_id",
            "name",
        ]

    def get_resource(self):
        optional_get_method_params = [
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
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_awr_db_parameter_changes,
            managed_database_id=self.module.params.get("managed_database_id"),
            awr_db_id=self.module.params.get("awr_db_id"),
            name=self.module.params.get("name"),
            **optional_kwargs
        )


AwrDbParamChangeFactsHelperCustom = get_custom_class(
    "AwrDbParamChangeFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDbParamChangeFactsHelperCustom, AwrDbParamChangeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            awr_db_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str", required=True),
            inst_num=dict(type="str"),
            begin_sn_id_greater_than_or_equal_to=dict(type="int"),
            end_sn_id_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            container_id=dict(type="int"),
            sort_by=dict(type="str", choices=["IS_CHANGED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db_param_change",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_db_param_change=result)


if __name__ == "__main__":
    main()
