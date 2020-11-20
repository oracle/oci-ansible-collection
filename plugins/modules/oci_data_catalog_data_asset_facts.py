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
module: oci_data_catalog_data_asset_facts
short_description: Fetches details about one or multiple DataAsset resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataAsset resources in Oracle Cloud Infrastructure
    - Returns a list of data assets within a data catalog.
    - If I(data_asset_key) is specified, the details of a single DataAsset will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    data_asset_key:
        description:
            - Unique data asset key.
            - Required to get a specific data_asset.
        type: str
    fields:
        description:
            - Specifies the fields to return in a data asset response.
        type: list
        choices:
            - "key"
            - "displayName"
            - "description"
            - "catalogId"
            - "externalKey"
            - "typeKey"
            - "lifecycleState"
            - "timeCreated"
            - "timeUpdated"
            - "createdById"
            - "updatedById"
            - "uri"
            - "properties"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - "A filter to return only resources that match display name pattern given. The match is not case sensitive.
              For Example : /folders?displayNameContains=Cu.*
              The above would match all folders with display name that starts with \\"Cu\\"."
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "MOVING"
    time_created:
        description:
            - Time that the resource was created. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
        type: str
    time_updated:
        description:
            - Time that the resource was updated. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
        type: str
    created_by_id:
        description:
            - OCID of the user who created the resource.
        type: str
    updated_by_id:
        description:
            - OCID of the user who updated the resource.
        type: str
    external_key:
        description:
            - Unique external identifier of this resource in the external source system.
        type: str
    type_key:
        description:
            - The key of the object type.
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List data_assets
  oci_data_catalog_data_asset_facts:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific data_asset
  oci_data_catalog_data_asset_facts:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    data_asset_key: data_asset_key_example

"""

RETURN = """
data_assets:
    description:
        - List of DataAsset resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique data asset key that is immutable.
            returned: on success
            type: string
            sample: key_example
        display_name:
            description:
                - A user-friendly display name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Detailed description of the data asset.
            returned: on success
            type: string
            sample: description_example
        catalog_id:
            description:
                - The data catalog's OCID.
            returned: on success
            type: string
            sample: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
        external_key:
            description:
                - External URI that can be used to reference the object. Format will differ based on the type of object.
            returned: on success
            type: string
            sample: external_key_example
        type_key:
            description:
                - The key of the object type. Type key's can be found via the '/types' endpoint.
            returned: on success
            type: string
            sample: type_key_example
        lifecycle_state:
            description:
                - The current state of the data asset.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - "The date and time the data asset was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-03-25T21:10:29.600Z
        time_updated:
            description:
                - The last time that any change was made to the data asset. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        created_by_id:
            description:
                - OCID of the user who created the data asset.
            returned: on success
            type: string
            sample: ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx
        updated_by_id:
            description:
                - OCID of the user who last modified the data asset.
            returned: on success
            type: string
            sample: ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx
        uri:
            description:
                - URI to the data asset instance in the API.
            returned: on success
            type: string
            sample: uri_example
        custom_property_members:
            description:
                - The list of customized properties along with the values for this object
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique Identifier of the attribute which is ID
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
                value:
                    description:
                        - The custom property value
                    returned: on success
                    type: string
                    sample: value_example
                data_type:
                    description:
                        - The data type of the custom property
                    returned: on success
                    type: string
                    sample: TEXT
                namespace_name:
                    description:
                        - Namespace name of the custom property
                    returned: on success
                    type: string
                    sample: namespace_name_example
                namespace_key:
                    description:
                        - Unique namespace key that is immutable
                    returned: on success
                    type: string
                    sample: namespace_key_example
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
                is_list_type:
                    description:
                        - Is this property allowed to have list of values
                    returned: on success
                    type: bool
                    sample: true
                allowed_values:
                    description:
                        - Allowed values for the custom property if any
                    returned: on success
                    type: list
                    sample: []
        data_selector_patterns:
            description:
                - The list of data selector patterns used in the harvest for this data asset to derive logical entities.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique pattern key that is immutable.
                    returned: on success
                    type: string
                    sample: key_example
                display_name:
                    description:
                        - A user-friendly display name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Detailed description of the pattern.
                    returned: on success
                    type: string
                    sample: description_example
                catalog_id:
                    description:
                        - The data catalog's OCID.
                    returned: on success
                    type: string
                    sample: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
                time_created:
                    description:
                        - "The date and time the pattern was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-03-25T21:10:29.600Z
                expression:
                    description:
                        - The expression used in the pattern that may include qualifiers.
                    returned: on success
                    type: string
                    sample: expression_example
                lifecycle_state:
                    description:
                        - State of the pattern.
                    returned: on success
                    type: string
                    sample: CREATING
        properties:
            description:
                - "A map of maps that contains the properties which are specific to the asset type. Each data asset type
                  definition defines it's set of required and optional properties. The map keys are category names and the
                  values are maps of property name to property value. Every property is contained inside of a category. Most
                  data assets have required properties within the \\"default\\" category.
                  Example: `{\\"properties\\": { \\"default\\": { \\"host\\": \\"host1\\", \\"port\\": \\"1521\\", \\"database\\": \\"orcl\\"}}}`"
            returned: on success
            type: dict
            sample: {}
        count:
            description:
                - Total number of items returned.
            returned: on success
            type: int
            sample: 56
        items:
            description:
                - Collection of data asset summaries.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique data asset key that is immutable.
                    returned: on success
                    type: string
                    sample: key_example
                display_name:
                    description:
                        - A user-friendly display name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Detailed description of the data asset.
                    returned: on success
                    type: string
                    sample: description_example
                catalog_id:
                    description:
                        - The data catalog's OCID.
                    returned: on success
                    type: string
                    sample: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
                external_key:
                    description:
                        - External URI that can be used to reference the object. Format will differ based on the type of object.
                    returned: on success
                    type: string
                    sample: external_key_example
                uri:
                    description:
                        - URI to the data asset instance in the API.
                    returned: on success
                    type: string
                    sample: uri_example
                time_created:
                    description:
                        - "The date and time the data asset was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-03-25T21:10:29.600Z
                type_key:
                    description:
                        - The key of the object type. Type keys's can be found via the '/types' endpoint.
                    returned: on success
                    type: string
                    sample: type_key_example
                lifecycle_state:
                    description:
                        - State of the data asset.
                    returned: on success
                    type: string
                    sample: CREATING
    sample: [{
        "key": "key_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
        "external_key": "external_key_example",
        "type_key": "type_key_example",
        "lifecycle_state": "CREATING",
        "time_created": "2019-03-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
        "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx",
        "uri": "uri_example",
        "custom_property_members": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "value": "value_example",
            "data_type": "TEXT",
            "namespace_name": "namespace_name_example",
            "namespace_key": "namespace_key_example",
            "is_multi_valued": true,
            "is_hidden": true,
            "is_editable": true,
            "is_list_type": true,
            "allowed_values": []
        }],
        "data_selector_patterns": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
            "time_created": "2019-03-25T21:10:29.600Z",
            "expression": "expression_example",
            "lifecycle_state": "CREATING"
        }],
        "properties": {},
        "count": 56,
        "items": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
            "external_key": "external_key_example",
            "uri": "uri_example",
            "time_created": "2019-03-25T21:10:29.600Z",
            "type_key": "type_key_example",
            "lifecycle_state": "CREATING"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_catalog import DataCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogDataAssetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "catalog_id",
            "data_asset_key",
        ]

    def get_required_params_for_list(self):
        return [
            "catalog_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset,
            catalog_id=self.module.params.get("catalog_id"),
            data_asset_key=self.module.params.get("data_asset_key"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "lifecycle_state",
            "time_created",
            "time_updated",
            "created_by_id",
            "updated_by_id",
            "external_key",
            "type_key",
            "fields",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_data_assets,
            catalog_id=self.module.params.get("catalog_id"),
            **optional_kwargs
        )


DataCatalogDataAssetFactsHelperCustom = get_custom_class(
    "DataCatalogDataAssetFactsHelperCustom"
)


class ResourceFactsHelper(
    DataCatalogDataAssetFactsHelperCustom, DataCatalogDataAssetFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            catalog_id=dict(type="str", required=True),
            data_asset_key=dict(type="str"),
            fields=dict(
                type="list",
                choices=[
                    "key",
                    "displayName",
                    "description",
                    "catalogId",
                    "externalKey",
                    "typeKey",
                    "lifecycleState",
                    "timeCreated",
                    "timeUpdated",
                    "createdById",
                    "updatedById",
                    "uri",
                    "properties",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "MOVING",
                ],
            ),
            time_created=dict(type="str"),
            time_updated=dict(type="str"),
            created_by_id=dict(type="str"),
            updated_by_id=dict(type="str"),
            external_key=dict(type="str"),
            type_key=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_asset",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(data_assets=result)


if __name__ == "__main__":
    main()
