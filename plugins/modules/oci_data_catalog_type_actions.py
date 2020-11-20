#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_data_catalog_type_actions
short_description: Perform actions on a Type resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Type resource in Oracle Cloud Infrastructure
    - For I(action=associate_custom_property), associate the custom property for the given type
    - For I(action=disassociate_custom_property), remove the custom property for the given type
version_added: "2.9"
author: Oracle (@oracle)
options:
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    type_key:
        description:
            - Unique type key.
        type: str
        required: true
    custom_property_ids:
        description:
            - array of custom property Ids
        type: list
    action:
        description:
            - The action to perform on the Type.
        type: str
        required: true
        choices:
            - "associate_custom_property"
            - "disassociate_custom_property"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action associate_custom_property on type
  oci_data_catalog_type_actions:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    type_key: type_key_example
    action: associate_custom_property

- name: Perform action disassociate_custom_property on type
  oci_data_catalog_type_actions:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    type_key: type_key_example
    action: disassociate_custom_property

"""

RETURN = """
type:
    description:
        - Details of the Type resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique type key that is immutable.
            returned: on success
            type: string
            sample: key_example
        name:
            description:
                - The immutable name of the type.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - Detailed description of the type.
            returned: on success
            type: string
            sample: description_example
        catalog_id:
            description:
                - The data catalog's OCID.
            returned: on success
            type: string
            sample: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
        properties:
            description:
                - |
                  "A map of arrays which defines the type specific properties, both required and optional. The map keys are
                  category names and the values are arrays contiaing all property details. Every property is contained inside
                  of a category. Most types have required properties within the \\"default\\" category.
                  Example:
                  `{
                     \\"properties\\": {
                       \\"default\\": {
                         \\"attributes:\\": [
                           {
                             \\"name\\": \\"host\\",
                             \\"type\\": \\"string\\",
                             \\"isRequired\\": true,
                             \\"isUpdatable\\": false
                           },
                           ...
                         ]
                       }
                     }
                   }`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The current state of the type.
            returned: on success
            type: string
            sample: CREATING
        is_internal:
            description:
                - Indicates whether the type is internal, making it unavailable for use by metadata elements.
            returned: on success
            type: bool
            sample: true
        is_tag:
            description:
                - Indicates whether the type can be used for tagging metadata elements.
            returned: on success
            type: bool
            sample: true
        is_approved:
            description:
                - Indicates whether the type is approved for use as a classifying object.
            returned: on success
            type: bool
            sample: true
        type_category:
            description:
                - Indicates the category this type belongs to. For instance, data assets, connections.
            returned: on success
            type: string
            sample: type_category_example
        external_type_name:
            description:
                - Mapping type equivalence in the external system.
            returned: on success
            type: string
            sample: external_type_name_example
        uri:
            description:
                - URI to the type instance in the API.
            returned: on success
            type: string
            sample: uri_example
        custom_properties:
            description:
                - Custom properties associated with this Type.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique custom property key that is immutable.
                    returned: on success
                    type: string
                    sample: key_example
                display_name:
                    description:
                        - Display name of the custom property
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Description of the custom property
                    returned: on success
                    type: string
                    sample: description_example
                data_type:
                    description:
                        - Data type of the custom property
                    returned: on success
                    type: string
                    sample: TEXT
                namespace_name:
                    description:
                        - Namespace name of the custom property
                    returned: on success
                    type: string
                    sample: namespace_name_example
                is_sortable:
                    description:
                        - If this field allows to sort from UI
                    returned: on success
                    type: bool
                    sample: true
                is_filterable:
                    description:
                        - If this field allows to filter or create facets from UI
                    returned: on success
                    type: bool
                    sample: true
                is_multi_valued:
                    description:
                        - If this field allows multiple values to be set
                    returned: on success
                    type: bool
                    sample: true
                is_hidden:
                    description:
                        - If this field is a hidden field
                    returned: on success
                    type: bool
                    sample: true
                is_editable:
                    description:
                        - If this field is a editable field
                    returned: on success
                    type: bool
                    sample: true
                is_service_defined:
                    description:
                        - If this field is defined by service or by a user
                    returned: on success
                    type: bool
                    sample: true
                is_hidden_in_search:
                    description:
                        - If this field is allowed to pop in search results
                    returned: on success
                    type: bool
                    sample: true
                time_created:
                    description:
                        - "The date and time the custom property was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-03-25T21:10:29.600Z
                lifecycle_state:
                    description:
                        - The current state of the custom property.
                    returned: on success
                    type: string
                    sample: CREATING
                usage_count:
                    description:
                        - Total number of first class objects using this custom property
                    returned: on success
                    type: int
                    sample: 56
                scope:
                    description:
                        - Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to
                    returned: on success
                    type: complex
                    contains:
                        type_id:
                            description:
                                - Unique type key identifier
                            returned: on success
                            type: string
                            sample: ocid1.type.oc1..xxxxxxEXAMPLExxxxxx
                        type_name:
                            description:
                                - Name of the type associated with
                            returned: on success
                            type: string
                            sample: type_name_example
                        count:
                            description:
                                - Number of objects associated with this type
                            returned: on success
                            type: int
                            sample: 56
                allowed_values:
                    description:
                        - Allowed values for the custom property if any
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "key": "key_example",
        "name": "name_example",
        "description": "description_example",
        "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
        "properties": {},
        "lifecycle_state": "CREATING",
        "is_internal": true,
        "is_tag": true,
        "is_approved": true,
        "type_category": "type_category_example",
        "external_type_name": "external_type_name_example",
        "uri": "uri_example",
        "custom_properties": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "data_type": "TEXT",
            "namespace_name": "namespace_name_example",
            "is_sortable": true,
            "is_filterable": true,
            "is_multi_valued": true,
            "is_hidden": true,
            "is_editable": true,
            "is_service_defined": true,
            "is_hidden_in_search": true,
            "time_created": "2019-03-25T21:10:29.600Z",
            "lifecycle_state": "CREATING",
            "usage_count": 56,
            "scope": [{
                "type_id": "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx",
                "type_name": "type_name_example",
                "count": 56
            }],
            "allowed_values": []
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
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import TypeCustomPropertyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogTypeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        associate_custom_property
        disassociate_custom_property
    """

    @staticmethod
    def get_module_resource_id_param():
        return "type_key"

    def get_module_resource_id(self):
        return self.module.params.get("type_key")

    def get_get_fn(self):
        return self.client.get_type

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_type,
            catalog_id=self.module.params.get("catalog_id"),
            type_key=self.module.params.get("type_key"),
        )

    def associate_custom_property(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TypeCustomPropertyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.associate_custom_property,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                type_key=self.module.params.get("type_key"),
                associate_custom_property_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def disassociate_custom_property(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TypeCustomPropertyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disassociate_custom_property,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                type_key=self.module.params.get("type_key"),
                disassociate_custom_property_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


DataCatalogTypeActionsHelperCustom = get_custom_class(
    "DataCatalogTypeActionsHelperCustom"
)


class ResourceHelper(
    DataCatalogTypeActionsHelperCustom, DataCatalogTypeActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            catalog_id=dict(type="str", required=True),
            type_key=dict(type="str", required=True),
            custom_property_ids=dict(type="list"),
            action=dict(
                type="str",
                required=True,
                choices=["associate_custom_property", "disassociate_custom_property"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="type",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
