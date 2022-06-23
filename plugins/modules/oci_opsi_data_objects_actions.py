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
module: oci_opsi_data_objects_actions
short_description: Perform actions on an OpsiDataObjects resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OpsiDataObjects resource in Oracle Cloud Infrastructure
    - For I(action=query), queries an OPSI data object with the inputs provided and sends the result set back. Either analysisTimeInterval
      or timeIntervalStart and timeIntervalEnd parameters need to be passed as well.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    data_object_identifier:
        description:
            - Unique OPSI data object identifier.
        type: str
    query:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            query_type:
                description:
                    - Type of Query
                type: str
                choices:
                    - "TEMPLATIZED_QUERY"
                required: true
            select_list:
                description:
                    - List of items to be added into the SELECT clause of the query; items will be added with comma separation.
                type: list
                elements: str
            where_conditions_list:
                description:
                    - "List of items to be added into the WHERE clause of the query; items will be added with AND separation.
                      Item can contain a single condition or multiple conditions.
                      Single condition e.g:  \\"optimizer_mode='mode1'\\"
                      Multiple conditions e.g: (module='module1' OR module='module2')"
                type: list
                elements: str
            group_by_list:
                description:
                    - List of items to be added into the GROUP BY clause of the query; items will be added with comma separation.
                type: list
                elements: str
            having_conditions_list:
                description:
                    - List of items to be added into the HAVING clause of the query; items will be added with AND separation.
                type: list
                elements: str
            order_by_list:
                description:
                    - List of items to be added into the ORDER BY clause of the query; items will be added with comma separation.
                type: list
                elements: str
            time_filters:
                description:
                    - ""
                type: dict
                suboptions:
                    time_period:
                        description:
                            - "Specify time period in ISO 8601 format with respect to current time.
                              Default is last 30 days represented by P30D.
                              If timePeriod is specified, then timeStart and timeEnd will be ignored.
                              Examples: P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months)."
                        type: str
                    time_start:
                        description:
                            - "Start time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z.
                              timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored."
                        type: str
                    time_end:
                        description:
                            - "End time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z.
                              timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored.
                              If timeEnd is not specified, current time is used as timeEnd."
                        type: str
    resource_filters:
        description:
            - ""
        type: dict
        suboptions:
            defined_tag_equals:
                description:
                    - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be considered.
                      Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
                      Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
                      Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
                type: list
                elements: str
            freeform_tag_equals:
                description:
                    - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be considered.
                      The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
                      Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
                type: list
                elements: str
            defined_tag_exists:
                description:
                    - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be considered.
                      Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
                      or \\"{namespace}.true\\".  All inputs are case-insensitive.
                      Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
                      Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
                      Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
                type: list
                elements: str
            freeform_tag_exists:
                description:
                    - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist will be considered.
                      The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
                      Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
                      Multiple values for different tag names are interpreted as \\"AND\\"."
                type: list
                elements: str
            compartment_id_in_subtree:
                description:
                    - A flag to consider all resources within a given compartment and all sub-compartments.
                type: bool
    action:
        description:
            - The action to perform on the OpsiDataObjects.
        type: str
        required: true
        choices:
            - "query"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action query on opsi_data_objects
  oci_opsi_data_objects_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    query:
      # required
      query_type: TEMPLATIZED_QUERY

      # optional
      select_list: [ "select_list_example" ]
      where_conditions_list: [ "where_conditions_list_example" ]
      group_by_list: [ "group_by_list_example" ]
      having_conditions_list: [ "having_conditions_list_example" ]
      order_by_list: [ "order_by_list_example" ]
      time_filters:
        # optional
        time_period: time_period_example
        time_start: time_start_example
        time_end: time_end_example
    action: query

    # optional
    data_object_identifier: data_object_identifier_example
    resource_filters:
      # optional
      defined_tag_equals: [ "defined_tag_equals_example" ]
      freeform_tag_equals: [ "freeform_tag_equals_example" ]
      defined_tag_exists: [ "defined_tag_exists_example" ]
      freeform_tag_exists: [ "freeform_tag_exists_example" ]
      compartment_id_in_subtree: true

"""

RETURN = """
opsi_data_object:
    description:
        - Details of the OpsiDataObjects resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        identifier:
            description:
                - Unique identifier of OPSI data object.
            returned: on success
            type: str
            sample: identifier_example
        data_object_type:
            description:
                - Type of OPSI data object.
            returned: on success
            type: str
            sample: DATABASE_INSIGHTS_DATA_OBJECT
        display_name:
            description:
                - User-friendly name of OPSI data object.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of OPSI data object.
            returned: on success
            type: str
            sample: description_example
        columns_metadata:
            description:
                - Metadata of columns in a data object.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the column.
                    returned: on success
                    type: str
                    sample: name_example
                category:
                    description:
                        - Category of the column.
                    returned: on success
                    type: str
                    sample: DIMENSION
                data_type_name:
                    description:
                        - Type of a data object column.
                    returned: on success
                    type: str
                    sample: NUMBER
                display_name:
                    description:
                        - Display name of the column.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description of the column.
                    returned: on success
                    type: str
                    sample: description_example
                group_name:
                    description:
                        - Group name of the column.
                    returned: on success
                    type: str
                    sample: group_name_example
                unit_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        numerator:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                unit_category:
                                    description:
                                        - Category of the column's unit.
                                    returned: on success
                                    type: str
                                    sample: DATA_SIZE
                                display_name:
                                    description:
                                        - Display name of the column's unit.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                        denominator:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                unit_category:
                                    description:
                                        - Category of the column's unit.
                                    returned: on success
                                    type: str
                                    sample: DATA_SIZE
                                display_name:
                                    description:
                                        - Display name of the column's unit.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                        unit_category:
                            description:
                                - Category of the column's unit.
                            returned: on success
                            type: str
                            sample: DATA_SIZE
                        display_name:
                            description:
                                - Display name of the column's unit.
                            returned: on success
                            type: str
                            sample: display_name_example
                        unit:
                            description:
                                - Core unit.
                            returned: on success
                            type: str
                            sample: CORE
    sample: {
        "identifier": "identifier_example",
        "data_object_type": "DATABASE_INSIGHTS_DATA_OBJECT",
        "display_name": "display_name_example",
        "description": "description_example",
        "columns_metadata": [{
            "name": "name_example",
            "category": "DIMENSION",
            "data_type_name": "NUMBER",
            "display_name": "display_name_example",
            "description": "description_example",
            "group_name": "group_name_example",
            "unit_details": {
                "numerator": {
                    "unit_category": "DATA_SIZE",
                    "display_name": "display_name_example"
                },
                "denominator": {
                    "unit_category": "DATA_SIZE",
                    "display_name": "display_name_example"
                },
                "unit_category": "DATA_SIZE",
                "display_name": "display_name_example",
                "unit": "CORE"
            }
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import QueryOpsiDataObjectDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpsiDataObjectsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        query
    """

    def get_get_fn(self):
        return self.client.get_opsi_data_object

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opsi_data_object,
            compartment_id=self.module.params.get("compartment_id"),
            opsi_data_object_identifier=self.module.params.get(
                "opsi_data_object_identifier"
            ),
        )

    def query(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, QueryOpsiDataObjectDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.query_opsi_data_object_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                query_opsi_data_object_data_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


OpsiDataObjectsActionsHelperCustom = get_custom_class(
    "OpsiDataObjectsActionsHelperCustom"
)


class ResourceHelper(
    OpsiDataObjectsActionsHelperCustom, OpsiDataObjectsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            data_object_identifier=dict(type="str"),
            query=dict(
                type="dict",
                required=True,
                options=dict(
                    query_type=dict(
                        type="str", required=True, choices=["TEMPLATIZED_QUERY"]
                    ),
                    select_list=dict(type="list", elements="str"),
                    where_conditions_list=dict(type="list", elements="str"),
                    group_by_list=dict(type="list", elements="str"),
                    having_conditions_list=dict(type="list", elements="str"),
                    order_by_list=dict(type="list", elements="str"),
                    time_filters=dict(
                        type="dict",
                        options=dict(
                            time_period=dict(type="str"),
                            time_start=dict(type="str"),
                            time_end=dict(type="str"),
                        ),
                    ),
                ),
            ),
            resource_filters=dict(
                type="dict",
                options=dict(
                    defined_tag_equals=dict(type="list", elements="str"),
                    freeform_tag_equals=dict(type="list", elements="str"),
                    defined_tag_exists=dict(type="list", elements="str"),
                    freeform_tag_exists=dict(type="list", elements="str"),
                    compartment_id_in_subtree=dict(type="bool"),
                ),
            ),
            action=dict(type="str", required=True, choices=["query"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opsi_data_objects",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
