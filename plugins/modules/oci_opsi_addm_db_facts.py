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
module: oci_opsi_addm_db_facts
short_description: Fetches details about one or multiple AddmDb resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddmDb resources in Oracle Cloud Infrastructure
    - Gets a list of ADDM database information
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
        elements: str
    id:
        description:
            - Optional list of database insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    time_interval_start:
        description:
            - Analysis start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              The minimum allowed value is 2 years prior to the current day.
              timeIntervalStart and timeIntervalEnd parameters are used together.
              If analysisTimeInterval is specified, this parameter is ignored.
        type: str
    time_interval_end:
        description:
            - Analysis end time in UTC in ISO 8601 format(exclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd are used together.
              If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.
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
            - Field name for sorting ADDM database data
        type: str
        choices:
            - "databaseName"
            - "numberOfFindings"
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List addm_dbs
  oci_opsi_addm_db_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: databaseName
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true

"""

RETURN = """
addm_dbs:
    description:
        - List of AddmDb resources
    returned: on success
    type: complex
    contains:
        database_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database insight resource.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                database_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
                    returned: on success
                    type: str
                    sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                database_name:
                    description:
                        - The database name. The database name is unique within the tenancy.
                    returned: on success
                    type: str
                    sample: database_name_example
                database_display_name:
                    description:
                        - The user-friendly name for the database. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: database_display_name_example
                database_type:
                    description:
                        - Operations Insights internal representation of the database type.
                    returned: on success
                    type: str
                    sample: database_type_example
                database_version:
                    description:
                        - The version of the database.
                    returned: on success
                    type: str
                    sample: database_version_example
                instances:
                    description:
                        - Array of hostname and instance name.
                    returned: on success
                    type: complex
                    contains:
                        host_name:
                            description:
                                - The hostname of the database insight resource.
                            returned: on success
                            type: str
                            sample: host_name_example
                        instance_name:
                            description:
                                - The instance name of the database insight resource.
                            returned: on success
                            type: str
                            sample: instance_name_example
                cdb_name:
                    description:
                        - Name of the CDB.Only applies to PDB.
                    returned: on success
                    type: str
                    sample: cdb_name_example
        number_of_findings:
            description:
                - Number of ADDM findings
            returned: on success
            type: int
            sample: 56
        number_of_addm_tasks:
            description:
                - Number of ADDM tasks
            returned: on success
            type: int
            sample: 56
        time_first_snapshot_begin:
            description:
                - The start timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_latest_snapshot_end:
            description:
                - The end timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        snapshot_interval_start:
            description:
                - AWR snapshot id.
            returned: on success
            type: str
            sample: snapshot_interval_start_example
        snapshot_interval_end:
            description:
                - AWR snapshot id.
            returned: on success
            type: str
            sample: snapshot_interval_end_example
        max_overall_impact:
            description:
                - Maximum overall impact in terms of percentage of total activity
            returned: on success
            type: float
            sample: 1.2
        most_frequent_category_name:
            description:
                - Category name
            returned: on success
            type: str
            sample: most_frequent_category_name_example
        most_frequent_category_display_name:
            description:
                - Category display name
            returned: on success
            type: str
            sample: most_frequent_category_display_name_example
    sample: [{
        "database_details": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "database_name": "database_name_example",
            "database_display_name": "database_display_name_example",
            "database_type": "database_type_example",
            "database_version": "database_version_example",
            "instances": [{
                "host_name": "host_name_example",
                "instance_name": "instance_name_example"
            }],
            "cdb_name": "cdb_name_example"
        },
        "number_of_findings": 56,
        "number_of_addm_tasks": 56,
        "time_first_snapshot_begin": "2013-10-20T19:20:30+01:00",
        "time_latest_snapshot_end": "2013-10-20T19:20:30+01:00",
        "snapshot_interval_start": "snapshot_interval_start_example",
        "snapshot_interval_end": "snapshot_interval_end_example",
        "max_overall_impact": 1.2,
        "most_frequent_category_name": "most_frequent_category_name_example",
        "most_frequent_category_display_name": "most_frequent_category_display_name_example"
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


class AddmDbFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_id",
            "id",
            "time_interval_start",
            "time_interval_end",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_addm_dbs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AddmDbFactsHelperCustom = get_custom_class("AddmDbFactsHelperCustom")


class ResourceFactsHelper(AddmDbFactsHelperCustom, AddmDbFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["databaseName", "numberOfFindings"]),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="addm_db",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addm_dbs=result)


if __name__ == "__main__":
    main()
