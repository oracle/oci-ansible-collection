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
module: oci_opsi_data_objects_facts
short_description: Fetches details about one or multiple OpsiDataObjects resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OpsiDataObjects resources in Oracle Cloud Infrastructure
    - Gets a list of OPSI data objects based on the query parameters specified. CompartmentId id query parameter must be specified.
    - If I(opsi_data_object_identifier) is specified, the details of a single OpsiDataObjects will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opsi_data_object_identifier:
        description:
            - Unique OPSI data object identifier.
            - Required to get a specific opsi_data_objects.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    data_object_type:
        description:
            - OPSI data object types.
        type: list
        elements: str
        choices:
            - "DATABASE_INSIGHTS_DATA_OBJECT"
            - "HOST_INSIGHTS_DATA_OBJECT"
            - "EXADATA_INSIGHTS_DATA_OBJECT"
    display_name:
        description:
            - A filter to return only resources that match the entire display name.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - OPSI data object list sort options.
        type: str
        choices:
            - "displayName"
            - "dataObjectType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific opsi_data_objects
  oci_opsi_data_objects_facts:
    # required
    opsi_data_object_identifier: opsi_data_object_identifier_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List opsi_data_objects
  oci_opsi_data_objects_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    data_object_type: [ "DATABASE_INSIGHTS_DATA_OBJECT" ]
    display_name: display_name_example
    sort_order: ASC
    sort_by: displayName

"""

RETURN = """
opsi_data_objects:
    description:
        - List of OpsiDataObjects resources
    returned: on success
    type: complex
    contains:
        columns_metadata:
            description:
                - Metadata of columns in a data object.
                - Returned for get operation
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
    sample: [{
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
        }],
        "identifier": "identifier_example",
        "data_object_type": "DATABASE_INSIGHTS_DATA_OBJECT",
        "display_name": "display_name_example",
        "description": "description_example"
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


class OpsiDataObjectsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "opsi_data_object_identifier",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opsi_data_object,
            compartment_id=self.module.params.get("compartment_id"),
            opsi_data_object_identifier=self.module.params.get(
                "opsi_data_object_identifier"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "data_object_type",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_opsi_data_objects,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OpsiDataObjectsFactsHelperCustom = get_custom_class("OpsiDataObjectsFactsHelperCustom")


class ResourceFactsHelper(
    OpsiDataObjectsFactsHelperCustom, OpsiDataObjectsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            opsi_data_object_identifier=dict(type="str"),
            compartment_id=dict(type="str", required=True),
            data_object_type=dict(
                type="list",
                elements="str",
                choices=[
                    "DATABASE_INSIGHTS_DATA_OBJECT",
                    "HOST_INSIGHTS_DATA_OBJECT",
                    "EXADATA_INSIGHTS_DATA_OBJECT",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "dataObjectType"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="opsi_data_objects",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(opsi_data_objects=result)


if __name__ == "__main__":
    main()
