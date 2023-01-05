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
module: oci_database_management_awr_db_param_facts
short_description: Fetches details about a AwrDbParam resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AwrDbParam resource in Oracle Cloud Infrastructure
    - "Summarizes the database parameter history for the specified database in AWR. This includes the list of database
      parameters, with information on whether the parameter values were modified within the query time range. Note that
      each database parameter is only listed once. Depending on the optional query parameters, the returned summary gets all the database parameters, which
      include:"
    - "- Each parameter whose value was changed during the time range:  (valueChanged =\\"Y\\")
      - Each parameter whose value was unchanged during the time range:  (valueChanged =\\"N\\")
      - Each parameter whose value was changed at the system level during the time range: (valueChanged =\\"Y\\"  and valueModified = \\"SYSTEM_MOD\\")
      - Each parameter whose value was unchanged during the time range, however, the value is not the default value: (valueChanged =\\"N\\" and  valueDefault =
        \\"FALSE\\")"
    - "Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database
      parameter value change history for a specific parameter, use the following API endpoint:
      /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameterChanges"
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
    name:
        description:
            - The optional multiple value query parameter to filter the entity name.
        type: list
        elements: str
    name_contains:
        description:
            - The optional contains query parameter to filter the entity name by any part of the name.
        type: str
    value_changed:
        description:
            - The optional query parameter to filter database parameters whose values were changed.
        type: str
        choices:
            - "Y"
            - "N"
    value_default:
        description:
            - The optional query parameter to filter the database parameters that had the default value in the last snapshot.
        type: str
        choices:
            - "TRUE"
            - "FALSE"
    value_modified:
        description:
            - The optional query parameter to filter the database parameters that had a modified value in the last snapshot.
        type: str
        choices:
            - "MODIFIED"
            - "SYSTEM_MOD"
            - "FALSE"
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
- name: Get a specific awr_db_param
  oci_database_management_awr_db_param_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    awr_db_id: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    inst_num: inst_num_example
    begin_sn_id_greater_than_or_equal_to: 56
    end_sn_id_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    container_id: 56
    name: [ "name_example" ]
    name_contains: name_contains_example
    value_changed: Y
    value_default: TRUE
    value_modified: MODIFIED
    sort_by: IS_CHANGED
    sort_order: ASC

"""

RETURN = """
awr_db_param:
    description:
        - AwrDbParam resource
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the parameter.
            returned: on success
            type: str
            sample: name_example
        instance_number:
            description:
                - The database instance number.
            returned: on success
            type: int
            sample: 56
        begin_value:
            description:
                - The parameter value when the period began.
            returned: on success
            type: str
            sample: begin_value_example
        end_value:
            description:
                - The parameter value when the period ended.
            returned: on success
            type: str
            sample: end_value_example
        is_changed:
            description:
                - Indicates whether the parameter value changed within the period.
            returned: on success
            type: bool
            sample: true
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
        "name": "name_example",
        "instance_number": 56,
        "begin_value": "begin_value_example",
        "end_value": "end_value_example",
        "is_changed": true,
        "value_modified": "value_modified_example",
        "is_default": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AwrDbParamFactsHelperGen(OCIResourceFactsHelperBase):
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
            "container_id",
            "name",
            "name_contains",
            "value_changed",
            "value_default",
            "value_modified",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_awr_db_parameters,
            managed_database_id=self.module.params.get("managed_database_id"),
            awr_db_id=self.module.params.get("awr_db_id"),
            **optional_kwargs
        )


AwrDbParamFactsHelperCustom = get_custom_class("AwrDbParamFactsHelperCustom")


class ResourceFactsHelper(AwrDbParamFactsHelperCustom, AwrDbParamFactsHelperGen):
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
            container_id=dict(type="int"),
            name=dict(type="list", elements="str"),
            name_contains=dict(type="str"),
            value_changed=dict(type="str", choices=["Y", "N"]),
            value_default=dict(type="str", choices=["TRUE", "FALSE"]),
            value_modified=dict(
                type="str", choices=["MODIFIED", "SYSTEM_MOD", "FALSE"]
            ),
            sort_by=dict(type="str", choices=["IS_CHANGED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db_param",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_db_param=result)


if __name__ == "__main__":
    main()
