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
        "properties": {},
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
