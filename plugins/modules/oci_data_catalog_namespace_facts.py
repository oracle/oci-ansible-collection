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
module: oci_data_catalog_namespace_facts
short_description: Fetches details about one or multiple Namespace resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Namespace resources in Oracle Cloud Infrastructure
    - Returns a list of namespaces within a data catalog.
    - If I(namespace_id) is specified, the details of a single Namespace will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_id:
        description:
            - Unique namespace identifier.
            - Required to get a specific namespace.
        type: str
        aliases: ["id"]
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - "A filter to return only resources that match display name pattern given. The match is not case sensitive.
              For Example : /folders?displayNameContains=Cu.*
              The above would match all folders with display name that starts with \\"Cu\\" or has the pattern \\"Cu\\" anywhere in between."
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
    fields:
        description:
            - Specifies the fields to return in a namespace response.
        type: list
        elements: str
        choices:
            - "key"
            - "displayName"
            - "description"
            - "lifecycleState"
            - "timeCreated"
            - "timeUpdated"
            - "createdById"
            - "updatedById"
            - "properties"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific namespace
  oci_data_catalog_namespace_facts:
    # required
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fields: [ "key" ]

- name: List namespaces
  oci_data_catalog_namespace_facts:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    lifecycle_state: CREATING
    time_created: 2013-10-20T19:20:30+01:00
    time_updated: 2013-10-20T19:20:30+01:00
    created_by_id: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
    updated_by_id: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC
    fields: [ "key" ]

"""

RETURN = """
namespaces:
    description:
        - List of Namespace resources
    returned: on success
    type: complex
    contains:
        time_updated:
            description:
                - The last time that any change was made to the namespace. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by_id:
            description:
                - OCID of the user who created the namespace.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_id:
            description:
                - OCID of the user who last modified the namespace.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        key:
            description:
                - Unique namespace key that is immutable.
            returned: on success
            type: str
            sample: key_example
        display_name:
            description:
                - Name of the Namespace
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for the namespace
            returned: on success
            type: str
            sample: description_example
        is_service_defined:
            description:
                - If this field is defined by service or by a user
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the namespace.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - "The date and time the namespace was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
        "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx",
        "key": "key_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "is_service_defined": true,
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class DataCatalogNamespaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "catalog_id",
            "namespace_id",
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
            self.client.get_namespace,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
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
            "sort_by",
            "sort_order",
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_namespaces,
            catalog_id=self.module.params.get("catalog_id"),
            **optional_kwargs
        )


DataCatalogNamespaceFactsHelperCustom = get_custom_class(
    "DataCatalogNamespaceFactsHelperCustom"
)


class ResourceFactsHelper(
    DataCatalogNamespaceFactsHelperCustom, DataCatalogNamespaceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_id=dict(aliases=["id"], type="str"),
            catalog_id=dict(type="str", required=True),
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
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            fields=dict(
                type="list",
                elements="str",
                choices=[
                    "key",
                    "displayName",
                    "description",
                    "lifecycleState",
                    "timeCreated",
                    "timeUpdated",
                    "createdById",
                    "updatedById",
                    "properties",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="namespace",
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

    module.exit_json(namespaces=result)


if __name__ == "__main__":
    main()
