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
module: oci_opsi_awr_database_parameter_facts
short_description: Fetches details about one or multiple AwrDatabaseParameter resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrDatabaseParameter resources in Oracle Cloud Infrastructure
    - "Summarizes the database parameter history for the specified database in AWR. This includes the list of database
      parameters, with information on whether the parameter values were modified within the query time range. Note that
      each database parameter is only listed once. Depending on the optional query parameters, the returned summary gets all the database parameters, which
      include:"
    - "Queryparam (valueChanged =\\"Y\\") - Each parameter whose value was changed during the time range, \\"isChanged : true\\" in response for the DB params.
      Queryparam (valueChanged =\\"N\\") - Each parameter whose value was unchanged during the time range, \\"isChanged : false\\" in response for the DB
      params.
      Queryparam (valueChanged =\\"Y\\"  and valueModified = \\"SYSTEM_MOD\\") - Each parameter whose value was changed at the system level during the time
      range, \\"isChanged : true\\" & \\"valueModified : SYSTEM_MOD\\" in response for the DB params.
      Queryparam (valueChanged =\\"N\\" and  valueDefault = \\"FALSE\\") - Each parameter whose value was unchanged during the time range, however, the value is
      not the default value, \\"isChanged : true\\" & \\"isDefault : false\\" in response for the DB params."
    - "Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database
      parameter value change history for a specific parameter, use the following API endpoint:
      /awrHubs/{awrHubId}/awrDbParameterChanges?awrSourceDatabaseIdentifier={awrSourceDbId}"
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
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List awr_database_parameters
  oci_opsi_awr_database_parameter_facts:
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
    name_contains: name_contains_example
    value_changed: Y
    value_default: TRUE
    value_modified: MODIFIED
    sort_by: IS_CHANGED
    sort_order: ASC

"""

RETURN = """
awr_database_parameters:
    description:
        - List of AwrDatabaseParameter resources
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
                   - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions values to be modified)
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
    sample: [{
        "name": "name_example",
        "instance_number": 56,
        "begin_value": "begin_value_example",
        "end_value": "end_value_example",
        "is_changed": true,
        "value_modified": "value_modified_example",
        "is_default": true
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


class AwrDatabaseParameterFactsHelperGen(OCIResourceFactsHelperBase):
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
            "name_contains",
            "value_changed",
            "value_default",
            "value_modified",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_awr_database_parameters,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            awr_source_database_identifier=self.module.params.get(
                "awr_source_database_identifier"
            ),
            **optional_kwargs
        )


AwrDatabaseParameterFactsHelperCustom = get_custom_class(
    "AwrDatabaseParameterFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDatabaseParameterFactsHelperCustom, AwrDatabaseParameterFactsHelperGen
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

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_database_parameter",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_database_parameters=result)


if __name__ == "__main__":
    main()
