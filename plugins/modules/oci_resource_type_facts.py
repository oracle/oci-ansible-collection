#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_resource_type_facts
short_description: Retrieves facts of types of resource that you can find with a search or query
description:
    - This module allows the user to retrieve facts of all resource types or a specific resource type that you can
      find with a search or query.
version_added: "2.5"
options:
    name:
        description: The name of the resource type. Required if you want details of a specific resource type. If I(name)
                     is unspecified, details of all resource types that are supported is returned.
        required: false
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get facts about all resource types that you can find with a search or query
  oci_resource_type_facts:

- name: Get details of the Vcn resource type
  oci_resource_type_facts:
    name: "Vcn"
"""

RETURN = """
resource_types:
    description: A type of resource that you can find with a search or query.
    returned: On successful operation
    type: complex
    contains:
        name:
            description: The unique name of the resource type, which matches the value returned as part of the
                         ResourceSummary object.
            type: string
            returned: always
        fields:
            description: List of all the fields and their value type that are indexed for querying.
            type: complex
            returned: always
            contains:
                field_type:
                    description: The type of the field, which dictates what semantics and query constraints you can use
                                 when searching or querying.
                    type: string
                    returned: always
                field_name:
                    description: The name of the field to use when constructing the query. Field names are present for
                                 all types except OBJECT.
                    type: string
                    returned: always
                is_array:
                    description: Indicates this field is actually an array of the specified field type.
                    type: bool
                    returned: always
                object_properties:
                    description: If the field type is OBJECT, then this property will provide all the individual
                                 properties on the object that can be queried.
                    type: same as fields
                    returned: if the field type is OBJECT
    sample:  [{
                fields: [{
                    "fieldName": "freeformTags",
                    "fieldType": "OBJECT",
                    "isArray": true,
                    "objectProperties": [
                      {
                        "fieldName": "freeformTags.value",
                        "fieldType": "STRING",
                        "isArray": false,
                        "objectProperties": null
                      },
                      {
                        "fieldName": "freeformTags.key",
                        "fieldType": "STRING",
                        "isArray": false,
                        "objectProperties": null
                      }
                    ]
                  },
                  {
                    "fieldName": "displayName",
                    "fieldType": "STRING",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "definedTags",
                    "fieldType": "OBJECT",
                    "isArray": true,
                    "objectProperties": [
                      {
                        "fieldName": "definedTags.key",
                        "fieldType": "STRING",
                        "isArray": false,
                        "objectProperties": null
                      },
                      {
                        "fieldName": "definedTags.namespace",
                        "fieldType": "STRING",
                        "isArray": false,
                        "objectProperties": null
                      },
                      {
                        "fieldName": "definedTags.value",
                        "fieldType": "STRING",
                        "isArray": false,
                        "objectProperties": null
                      }
                    ]
                  },
                  {
                    "fieldName": "lifecycleState",
                    "fieldType": "STRING",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "compartmentId",
                    "fieldType": "IDENTIFIER",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "availabilityDomain",
                    "fieldType": "STRING",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "timeLastIndexed",
                    "fieldType": "DATETIME",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "timeCreated",
                    "fieldType": "DATETIME",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "identifier",
                    "fieldType": "IDENTIFIER",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "cidrBlock",
                    "fieldType": "STRING",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "dnsLabel",
                    "fieldType": "STRING",
                    "isArray": false,
                    "objectProperties": null
                  },
                  {
                    "fieldName": "vcnDomainName",
                    "fieldType": "STRING",
                    "isArray": false,
                    "objectProperties": null
                  }
                ],
                "name": "Vcn"
              }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.resource_search.resource_search_client import ResourceSearchClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(name=dict(type="str", required=False)))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    result = dict(changed=False)

    resource_search_client = oci_utils.create_service_client(
        module, ResourceSearchClient
    )
    name = module.params.get("name")
    res_coll = None
    if name is not None:
        res_coll = [
            oci_utils.call_with_backoff(
                resource_search_client.get_resource_type, name=name
            ).data
        ]
    else:
        res_coll = oci_utils.call_with_backoff(
            resource_search_client.list_resource_types
        ).data
    result["resource_types"] = oci_utils.to_dict(res_coll)
    module.exit_json(**result)


if __name__ == "__main__":
    main()
