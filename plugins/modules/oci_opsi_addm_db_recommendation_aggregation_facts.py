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
module: oci_opsi_addm_db_recommendation_aggregation_facts
short_description: Fetches details about one or multiple AddmDbRecommendationAggregation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddmDbRecommendationAggregation resources in Oracle Cloud Infrastructure
    - Summarizes ADDM recommendations for the specified databases.
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
            - Optional value filter to match the finding category exactly.
        type: str
    finding_identifier:
        description:
            - Unique finding ID
        type: str
    sql_identifier:
        description:
            - Optional filter to return only resources whose sql id matches the value given. Only considered when
              categoryName is SQL_TUNING.
        type: str
    owner_or_name_contains:
        description:
            - Optional filter to return only resources whose owner or name contains the substring given. The
              match is not case sensitive. Only considered when categoryName is SCHEMA_OBJECT.
        type: str
    name_contains:
        description:
            - Optional filter to return only resources whose name contains the substring given. The
              match is not case sensitive. Only considered when categoryName is DATABASE_CONFIGURATION.
        type: str
    name:
        description:
            - Optional filter to return only resources whose name exactly matches the substring given. The
              match is case sensitive. Only considered when categoryName is DATABASE_CONFIGURATION.
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
            - Field name for sorting the recommendation data
        type: str
        choices:
            - "maxBenefitPercent"
            - "maxBenefitAvgActiveSessions"
            - "frequencyCount"
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
- name: List addm_db_recommendation_aggregations
  oci_opsi_addm_db_recommendation_aggregation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    instance_number: instance_number_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    category_name: category_name_example
    finding_identifier: finding_identifier_example
    sql_identifier: sql_identifier_example
    owner_or_name_contains: owner_or_name_contains_example
    name_contains: name_contains_example
    name: name_example
    sort_order: ASC
    sort_by: maxBenefitPercent
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true

"""

RETURN = """
addm_db_recommendation_aggregations:
    description:
        - List of AddmDbRecommendationAggregation resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database insight.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - Type of recommendation
            returned: on success
            type: str
            sample: type_example
        message:
            description:
                - Recommendation message
            returned: on success
            type: str
            sample: message_example
        requires_db_restart:
            description:
                - "Indicates implementation of the recommended action requires a database restart in order for it
                  to take effect. Possible values \\"Y\\", \\"N\\" and null."
            returned: on success
            type: str
            sample: requires_db_restart_example
        implement_actions:
            description:
                - Actions that can be performed to implement the recommendation (such as 'ALTER PARAMETER',
                  'RUN SQL TUNING ADVISOR')
            returned: on success
            type: list
            sample: []
        rationale:
            description:
                - Recommendation message
            returned: on success
            type: str
            sample: rationale_example
        max_benefit_percent:
            description:
                - Maximum estimated benefit in terms of percentage of total activity
            returned: on success
            type: float
            sample: 1.2
        overall_benefit_percent:
            description:
                - Overall estimated benefit in terms of percentage of total activity
            returned: on success
            type: float
            sample: 1.2
        max_benefit_avg_active_sessions:
            description:
                - Maximum estimated benefit in terms of average active sessions
            returned: on success
            type: float
            sample: 1.2
        frequency_count:
            description:
                - Number of occurrences for this recommendation
            returned: on success
            type: int
            sample: 56
        related_object:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of database parameter
                    returned: on success
                    type: str
                    sample: name_example
                object_id:
                    description:
                        - Object id (from RDBMS)
                    returned: on success
                    type: int
                    sample: 56
                owner:
                    description:
                        - Owner of object
                    returned: on success
                    type: str
                    sample: owner_example
                object_name:
                    description:
                        - Name of object
                    returned: on success
                    type: str
                    sample: object_name_example
                sub_object_name:
                    description:
                        - Subobject name; for example, partition name
                    returned: on success
                    type: str
                    sample: sub_object_name_example
                object_type:
                    description:
                        - Type of the object (such as TABLE, INDEX)
                    returned: on success
                    type: str
                    sample: object_type_example
                type:
                    description:
                        - Type of related object
                    returned: on success
                    type: str
                    sample: SCHEMA_OBJECT
                sql_id:
                    description:
                        - SQL identifier
                    returned: on success
                    type: str
                    sample: "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx"
                sql_text:
                    description:
                        - First 3800 characters of the SQL text
                    returned: on success
                    type: str
                    sample: sql_text_example
                is_sql_text_truncated:
                    description:
                        - SQL identifier
                    returned: on success
                    type: bool
                    sample: true
                sql_command:
                    description:
                        - SQL command name (such as SELECT, INSERT)
                    returned: on success
                    type: str
                    sample: sql_command_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "type_example",
        "message": "message_example",
        "requires_db_restart": "requires_db_restart_example",
        "implement_actions": [],
        "rationale": "rationale_example",
        "max_benefit_percent": 1.2,
        "overall_benefit_percent": 1.2,
        "max_benefit_avg_active_sessions": 1.2,
        "frequency_count": 56,
        "related_object": {
            "name": "name_example",
            "object_id": 56,
            "owner": "owner_example",
            "object_name": "object_name_example",
            "sub_object_name": "sub_object_name_example",
            "object_type": "object_type_example",
            "type": "SCHEMA_OBJECT",
            "sql_id": "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx",
            "sql_text": "sql_text_example",
            "is_sql_text_truncated": true,
            "sql_command": "sql_command_example"
        }
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


class AddmDbRecommendationAggregationFactsHelperGen(OCIResourceFactsHelperBase):
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
            "finding_identifier",
            "sql_identifier",
            "owner_or_name_contains",
            "name_contains",
            "name",
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
            self.client.summarize_addm_db_recommendations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AddmDbRecommendationAggregationFactsHelperCustom = get_custom_class(
    "AddmDbRecommendationAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    AddmDbRecommendationAggregationFactsHelperCustom,
    AddmDbRecommendationAggregationFactsHelperGen,
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
            finding_identifier=dict(type="str"),
            sql_identifier=dict(type="str"),
            owner_or_name_contains=dict(type="str"),
            name_contains=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "maxBenefitPercent",
                    "maxBenefitAvgActiveSessions",
                    "frequencyCount",
                ],
            ),
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
        resource_type="addm_db_recommendation_aggregation",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addm_db_recommendation_aggregations=result)


if __name__ == "__main__":
    main()
