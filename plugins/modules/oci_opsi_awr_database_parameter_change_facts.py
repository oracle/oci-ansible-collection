#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_opsi_awr_database_parameter_change_facts
short_description: Fetches details about one or multiple AwrDatabaseParameterChange resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AwrDatabaseParameterChange resources in Oracle Cloud Infrastructure
    - "Summarizes the database parameter change history for one database parameter of the specified database in AWR. One change history record contains
      the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range,
      then multiple change history records are created for the same parameter.
      Note that this API only returns information on change history details for one database parameter.
      To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint:
      /awrHubs/{awrHubId}/awrDbParameters?awrSourceDatabaseIdentifier={awrSourceDbId}"
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
    name:
        description:
            - The required single value query parameter to filter the entity name.
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
- name: List awr_database_parameter_changes
  oci_opsi_awr_database_parameter_change_facts:
    # required
    awr_hub_id: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"
    awr_source_database_identifier: awr_source_database_identifier_example
    name: name_example

    # optional
    instance_number: instance_number_example
    begin_snapshot_identifier_greater_than_or_equal_to: 56
    end_snapshot_identifier_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    sort_by: IS_CHANGED
    sort_order: ASC

"""

RETURN = """
awr_database_parameter_changes:
    description:
        - List of AwrDatabaseParameterChange resources
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
        snapshot_identifier:
            description:
                - "The ID of the snapshot with the parameter value changed. The snapshot identifier is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  It can be retrieved from the following endpoint:
                  /awrHubs/{awrHubId}/awrDatabaseSnapshots"
            returned: on success
            type: int
            sample: 56
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
        "time_begin": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "instance_number": 56,
        "previous_value": "previous_value_example",
        "value": "value_example",
        "snapshot_identifier": 56,
        "value_modified": "value_modified_example",
        "is_default": true
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


class AwrDatabaseParameterChangeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "awr_hub_id",
            "awr_source_database_identifier",
            "name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "instance_number",
            "begin_snapshot_identifier_greater_than_or_equal_to",
            "end_snapshot_identifier_less_than_or_equal_to",
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
            self.client.summarize_awr_database_parameter_changes,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            awr_source_database_identifier=self.module.params.get(
                "awr_source_database_identifier"
            ),
            name=self.module.params.get("name"),
            **optional_kwargs
        )


AwrDatabaseParameterChangeFactsHelperCustom = get_custom_class(
    "AwrDatabaseParameterChangeFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDatabaseParameterChangeFactsHelperCustom,
    AwrDatabaseParameterChangeFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            awr_hub_id=dict(type="str", required=True),
            awr_source_database_identifier=dict(type="str", required=True),
            name=dict(type="str", required=True),
            instance_number=dict(type="str"),
            begin_snapshot_identifier_greater_than_or_equal_to=dict(type="int"),
            end_snapshot_identifier_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            sort_by=dict(type="str", choices=["IS_CHANGED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_database_parameter_change",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_database_parameter_changes=result)


if __name__ == "__main__":
    main()
