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
module: oci_usage_custom_table
short_description: Manage a CustomTable resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CustomTable resource in Oracle Cloud Infrastructure
    - For I(state=present), returns the created custom table.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment OCID.
            - Required for create using I(state=present).
        type: str
    saved_report_id:
        description:
            - The associated saved report OCID.
            - Required for create using I(state=present).
        type: str
    saved_custom_table:
        description:
            - ""
            - Required for create using I(state=present), update using I(state=present) with custom_table_id present.
        type: dict
        suboptions:
            display_name:
                description:
                    - The name of the custom table.
                type: str
                aliases: ["name"]
                required: true
            row_group_by:
                description:
                    - "The row groupBy key list.
                      example:
                        `[\\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\", \\"skuPartNumber\\", \\"unit\\",
                          \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\", \\"logicalAd\\",
                          \\"resourceId\\", \\"tenantId\\", \\"tenantName\\"]`"
                type: list
                elements: str
            column_group_by:
                description:
                    - "The column groupBy key list.
                      example:
                        `[\\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\", \\"skuPartNumber\\", \\"unit\\",
                          \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\", \\"logicalAd\\",
                          \\"resourceId\\", \\"tenantId\\", \\"tenantName\\"]`"
                type: list
                elements: str
            group_by_tag:
                description:
                    - "GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only one tag in the list is supported.
                      For example:
                        `[{\\"namespace\\":\\"oracle\\", \\"key\\":\\"createdBy\\"]`"
                type: list
                elements: dict
                suboptions:
                    namespace:
                        description:
                            - The tag namespace.
                        type: str
                    key:
                        description:
                            - The tag key.
                        type: str
                    value:
                        description:
                            - The tag value.
                        type: str
            compartment_depth:
                description:
                    - The compartment depth level.
                type: float
            version:
                description:
                    - The version of the custom table.
                type: float
    custom_table_id:
        description:
            - The custom table unique OCID.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CustomTable.
            - Use I(state=present) to create or update a CustomTable.
            - Use I(state=absent) to delete a CustomTable.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create custom_table
  oci_usage_custom_table:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    saved_report_id: "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx"
    saved_custom_table:
      # required
      display_name: display_name_example

      # optional
      row_group_by: [ "row_group_by_example" ]
      column_group_by: [ "column_group_by_example" ]
      group_by_tag:
      - # optional
        namespace: namespace_example
        key: key_example
        value: value_example
      compartment_depth: 3.4
      version: 3.4

- name: Update custom_table
  oci_usage_custom_table:
    # required
    saved_custom_table:
      # required
      display_name: display_name_example

      # optional
      row_group_by: [ "row_group_by_example" ]
      column_group_by: [ "column_group_by_example" ]
      group_by_tag:
      - # optional
        namespace: namespace_example
        key: key_example
        value: value_example
      compartment_depth: 3.4
      version: 3.4
    custom_table_id: "ocid1.customtable.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete custom_table
  oci_usage_custom_table:
    # required
    custom_table_id: "ocid1.customtable.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
custom_table:
    description:
        - Details of the CustomTable resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The custom table OCID.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        saved_report_id:
            description:
                - The custom table associated saved report OCID.
            returned: on success
            type: str
            sample: "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The custom table compartment OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        saved_custom_table:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The name of the custom table.
                    returned: on success
                    type: str
                    sample: display_name_example
                row_group_by:
                    description:
                        - "The row groupBy key list.
                          example:
                            `[\\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\", \\"skuPartNumber\\", \\"unit\\",
                              \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\", \\"logicalAd\\",
                              \\"resourceId\\", \\"tenantId\\", \\"tenantName\\"]`"
                    returned: on success
                    type: list
                    sample: []
                column_group_by:
                    description:
                        - "The column groupBy key list.
                          example:
                            `[\\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\", \\"skuPartNumber\\", \\"unit\\",
                              \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\", \\"logicalAd\\",
                              \\"resourceId\\", \\"tenantId\\", \\"tenantName\\"]`"
                    returned: on success
                    type: list
                    sample: []
                group_by_tag:
                    description:
                        - "GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only one tag in the list is supported.
                          For example:
                            `[{\\"namespace\\":\\"oracle\\", \\"key\\":\\"createdBy\\"]`"
                    returned: on success
                    type: complex
                    contains:
                        namespace:
                            description:
                                - The tag namespace.
                            returned: on success
                            type: str
                            sample: namespace_example
                        key:
                            description:
                                - The tag key.
                            returned: on success
                            type: str
                            sample: key_example
                        value:
                            description:
                                - The tag value.
                            returned: on success
                            type: str
                            sample: value_example
                compartment_depth:
                    description:
                        - The compartment depth level.
                    returned: on success
                    type: float
                    sample: 10
                version:
                    description:
                        - The version of the custom table.
                    returned: on success
                    type: float
                    sample: 10
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "saved_report_id": "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "saved_custom_table": {
            "display_name": "display_name_example",
            "row_group_by": [],
            "column_group_by": [],
            "group_by_tag": [{
                "namespace": "namespace_example",
                "key": "key_example",
                "value": "value_example"
            }],
            "compartment_depth": 10,
            "version": 10
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.usage_api import UsageapiClient
    from oci.usage_api.models import CreateCustomTableDetails
    from oci.usage_api.models import UpdateCustomTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CustomTableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(CustomTableHelperGen, self).get_possible_entity_types() + [
            "customtable",
            "customtables",
            "usageApicustomtable",
            "usageApicustomtables",
            "customtableresource",
            "customtablesresource",
            "usageapi",
        ]

    def get_module_resource_id_param(self):
        return "custom_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("custom_table_id")

    def get_get_fn(self):
        return self.client.get_custom_table

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_table, custom_table_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_table,
            custom_table_id=self.module.params.get("custom_table_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "saved_report_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_custom_tables, **kwargs
        )

    def get_create_model_class(self):
        return CreateCustomTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_custom_table,
            call_fn_args=(),
            call_fn_kwargs=dict(create_custom_table_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCustomTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_custom_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_custom_table_details=update_details,
                custom_table_id=self.module.params.get("custom_table_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_custom_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                custom_table_id=self.module.params.get("custom_table_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CustomTableHelperCustom = get_custom_class("CustomTableHelperCustom")


class ResourceHelper(CustomTableHelperCustom, CustomTableHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            saved_report_id=dict(type="str"),
            saved_custom_table=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str", required=True),
                    row_group_by=dict(type="list", elements="str"),
                    column_group_by=dict(type="list", elements="str"),
                    group_by_tag=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace=dict(type="str"),
                            key=dict(type="str", no_log=True),
                            value=dict(type="str"),
                        ),
                    ),
                    compartment_depth=dict(type="float"),
                    version=dict(type="float"),
                ),
            ),
            custom_table_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="custom_table",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
