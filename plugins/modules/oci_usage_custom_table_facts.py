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
module: oci_usage_custom_table_facts
short_description: Fetches details about one or multiple CustomTable resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CustomTable resources in Oracle Cloud Infrastructure
    - Returns the saved custom table list.
    - If I(custom_table_id) is specified, the details of a single CustomTable will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    custom_table_id:
        description:
            - The custom table unique OCID.
            - Required to get a specific custom_table.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment ID in which to list resources.
            - Required to list multiple custom_tables.
        type: str
    saved_report_id:
        description:
            - The saved report ID in which to list resources.
            - Required to list multiple custom_tables.
        type: str
    sort_by:
        description:
            - The field to sort by. If not specified, the default is displayName.
        type: str
        choices:
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List custom_tables
  oci_usage_custom_table_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    saved_report_id: "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific custom_table
  oci_usage_custom_table_facts:
    custom_table_id: "ocid1.customtable.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
custom_tables:
    description:
        - List of CustomTable resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.usage_api import UsageapiClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CustomTableFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "custom_table_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "saved_report_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_table,
            custom_table_id=self.module.params.get("custom_table_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_custom_tables,
            compartment_id=self.module.params.get("compartment_id"),
            saved_report_id=self.module.params.get("saved_report_id"),
            **optional_kwargs
        )


CustomTableFactsHelperCustom = get_custom_class("CustomTableFactsHelperCustom")


class ResourceFactsHelper(CustomTableFactsHelperCustom, CustomTableFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            custom_table_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            saved_report_id=dict(type="str"),
            sort_by=dict(type="str", choices=["displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="custom_table",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(custom_tables=result)


if __name__ == "__main__":
    main()
