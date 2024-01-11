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
module: oci_opsi_addm_db_parameter_aggregation_facts
short_description: Fetches details about one or multiple AddmDbParameterAggregation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddmDbParameterAggregation resources in Oracle Cloud Infrastructure
    - Summarizes database parameter history information for the specified databases. Return a list of parameters
      with information on whether the parameter values were changed or not within the specified
      time period. The response does not include the individual parameter changes within the time
      period.
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
    instance_number:
        description:
            - The optional single value query parameter to filter by database instance number.
        type: str
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
    category_name:
        description:
            - "Optional value filter to match the parameter category exactly. Note the list of possible
              category names can be retrieved from the following endpoint:
              /databases/{databaseId}/addmDbParameterCategories."
        type: str
    name_or_value_contains:
        description:
            - Optional filter to return only resources whose name or value contains the substring given. The
              match is not case sensitive.
        type: str
    is_changed:
        description:
            - "Optional filter to return only parameters whose value changed in the specified time period.
              Valid values include: TRUE, FALSE"
        type: str
        choices:
            - "true"
            - "false"
    is_default:
        description:
            - "Optional filter to return only parameters whose end value was set to the default value (TRUE)
              or was specified in the parameter file (FALSE). Valid values include: TRUE, FALSE"
        type: str
        choices:
            - "true"
            - "false"
    has_recommendations:
        description:
            - "Optional filter to return only parameters which have recommendations in the specified time period.
              Valid values include: TRUE, FALSE"
        type: str
        choices:
            - "true"
            - "false"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Field name for sorting the database parameter data
        type: str
        choices:
            - "isChanged"
            - "name"
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List addm_db_parameter_aggregations
  oci_opsi_addm_db_parameter_aggregation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    instance_number: instance_number_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    category_name: category_name_example
    name_or_value_contains: name_or_value_contains_example
    is_changed: true
    is_default: true
    has_recommendations: true
    sort_order: ASC
    sort_by: isChanged
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true

"""

RETURN = """
addm_db_parameter_aggregations:
    description:
        - List of AddmDbParameterAggregation resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database insight.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Name of  parameter
            returned: on success
            type: str
            sample: name_example
        inst_num:
            description:
                - Number of database instance
            returned: on success
            type: int
            sample: 56
        default_value:
            description:
                - Parameter default value
            returned: on success
            type: str
            sample: default_value_example
        begin_value:
            description:
                - Parameter value when time period began
            returned: on success
            type: str
            sample: begin_value_example
        end_value:
            description:
                - Parameter value when time period ended
            returned: on success
            type: str
            sample: end_value_example
        is_changed:
            description:
                - Indicates whether the parameter's value changed during the selected time range (TRUE) or
                  did not change during the selected time range (FALSE)
            returned: on success
            type: bool
            sample: true
        is_default:
            description:
                - Indicates whether the parameter's end value was set to the default value (TRUE) or was
                  specified in the parameter file (FALSE)
            returned: on success
            type: bool
            sample: true
        value_modified:
            description:
                - "Indicates whether the parameter has been modified after instance starup
                  MODIFIED - Parameter has been modified with ALTER SESSION
                  SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM
                  FALSE - Parameter has not been modified after instance starup"
            returned: on success
            type: str
            sample: value_modified_example
        is_high_impact:
            description:
                - Indicates whether the parameter is a high impact parameter (TRUE) or not (FALSE)
            returned: on success
            type: bool
            sample: true
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "inst_num": 56,
        "default_value": "default_value_example",
        "begin_value": "begin_value_example",
        "end_value": "end_value_example",
        "is_changed": true,
        "is_default": true,
        "value_modified": "value_modified_example",
        "is_high_impact": true
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


class AddmDbParameterAggregationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_id",
            "id",
            "instance_number",
            "time_interval_start",
            "time_interval_end",
            "category_name",
            "name_or_value_contains",
            "is_changed",
            "is_default",
            "has_recommendations",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_addm_db_parameters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AddmDbParameterAggregationFactsHelperCustom = get_custom_class(
    "AddmDbParameterAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    AddmDbParameterAggregationFactsHelperCustom,
    AddmDbParameterAggregationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            instance_number=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            category_name=dict(type="str"),
            name_or_value_contains=dict(type="str"),
            is_changed=dict(type="str", choices=["true", "false"]),
            is_default=dict(type="str", choices=["true", "false"]),
            has_recommendations=dict(type="str", choices=["true", "false"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["isChanged", "name"]),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="addm_db_parameter_aggregation",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addm_db_parameter_aggregations=result)


if __name__ == "__main__":
    main()
