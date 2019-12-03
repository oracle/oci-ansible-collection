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
module: oci_search_resources_facts
short_description: Finds resources in your cloud network
description:
    - This module allows the user to finds resources in your cloud network. Queries any and all compartments in the
      tenancy to find resources that match the specified criteria. Results include resources that you have permission
      to view and can span different resource types. You can also sort results based on a specified resource attribute.
version_added: "2.5"
options:
    type:
        description: The type of SearchDetails, whether FreeText or Structured.
        required: true
        choices: ['FreeText', 'Structured']
    matching_context_type:
        description: The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service
                     will highlight fragments in its response. (See SearchContext in the RETURN section for more
                     information.) The default setting is NONE.
        default: 'NONE'
        required: false
        choices: [ 'NONE', 'HIGHLIGHTS' ]
    query:
        description: The structured query describing which resources to search for. Required when structured search is
                     desired, I(type="Structured").
        required: false
    text:
        description: The text to search for. Required when free text search is desired, I(type="FreeText").
        required: false
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Perform a free-text search
  oci_search_resources_facts:
    type: 'FreeText'
    text: "MyVCN1"
    matching_context_type: "HIGHLIGHTS"

- name: Perform a structured search to find a "user" resource whose display name is "Jane"
  oci_search_resources_facts:
    type: "Structured"
    query: "query user resources where displayName = 'jane'"
"""

RETURN = """
search_resources:
    description: A resource that exists in the user's cloud network.
    returned: On successful operation
    type: complex
    contains:
        resource_type:
            description: The resource type name.
            type: string
            returned: always
        identifier:
            description: The unique identifier for this particular resource, usually an OCID.
            type: string
            returned: always
        compartment_id:
            description: The OCID of the compartment that contains this resource.
            type: string
            returned: always
        time_created:
            description: The time this resource was created.
            type: string
            returned: always
        display_name:
            description: The display name (or name) of this resource, if one exists.
            type: string
            returned: always
        availability_domain:
            description: The availability domain this resource is located in, if applicable.
            type: string
            returned: always
        lifecycle_state:
            description: The lifecycle state of this resource, if applicable.
            type: string
            returned: always
        freeform_tags:
            description: The freeform tags associated with this resource, if any.
            type: string
            returned: always
        defined_tags:
            description: The defined tags associated with this resource, if any.
            type: string
            returned: always
        search_context:
            description: Contains search context, such as highlighting, for found resources.
            type: complex
            returned: always
            contains:
                highlights: Describes what in each field matched the search criteria by showing highlighted values, but
                            only for free text searches or for structured queries that use a MATCHING clause. The list
                            of strings represents fragments of values that matched the query conditions. Highlighted
                            values are wrapped with .. tags. All values are HTML-encoded (except tags).
                type: string
                returned: always
    sample:  [
                {
                  "resourceType": "User",
                  "identifier": "ocid1.user.oc1..examplea..xxxxxEXAMPLExxxxx",
                  "compartmentId": "ocidv1:tenancy:oc1:phx:1457636318783:examp..xxxxxEXAMPLExxxxx",
                  "timeCreated": "2016-12-12T19:31:03.749Z",
                  "displayName": "Jane.Doe",
                  "availabilityDomain": null,
                  "lifecycleState": "ACTIVE",
                  "freeformTags": {},
                  "definedTags": {},
                  "searchContext": {
                    "highlights": {
                      "description": [
                        "<h1>Jane</h1> Doe's account"
                      ]
                    }
                  }
                },
                {
              "resourceType": "Compartment",
              "identifier": "ocid1.compartment.oc1....xxxxxEXAMPLExxxxx",
              "compartmentId": "ocidv1:tenancy:oc1:phx:1457636318783:..xxxxxEXAMPLExxxxx",
              "timeCreated": "2017-01-20T00:18:14.236Z",
              "displayName": "JanesCompartment",
              "availabilityDomain": null,
              "lifecycleState": "ACTIVE",
              "freeformTags": {},
              "definedTags": {},
              "searchContext": {
                "highlights": {
                  "description": [
                    "Compartment for <h1>Jane</h1> Doe to use"
                  ]
                }
              }
            }
        ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.resource_search.resource_search_client import ResourceSearchClient
    from oci.resource_search.models import (
        FreeTextSearchDetails,
        StructuredSearchDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            type=dict(type="str", required=True, choices=["FreeText", "Structured"]),
            matching_context_type=dict(
                type="str",
                required=False,
                choices=["NONE", "HIGHLIGHTS"],
                default="NONE",
            ),
            query=dict(type="str", required=False),
            text=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("type", "FreeText", ["text"]), ("type", "Structured", ["query"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    result = dict(changed=False)

    resource_search_client = oci_utils.create_service_client(
        module, ResourceSearchClient
    )
    matching_context_type = module.params.get("matching_context_type")

    search_details = None
    if module.params["type"] == "FreeText":
        ftsd = FreeTextSearchDetails()
        ftsd.type = "FreeText"
        if matching_context_type is not None:
            ftsd.matching_context_type = matching_context_type
        ftsd.text = module.params["text"]
        search_details = ftsd
    else:
        ssd = StructuredSearchDetails()
        if matching_context_type is not None:
            ssd.type = "Structured"
        ssd.matching_context_type = matching_context_type
        ssd.query = module.params["query"]
        search_details = ssd

    res_coll = oci_utils.call_with_backoff(
        resource_search_client.search_resources, search_details=search_details
    ).data
    result["search_resources"] = oci_utils.to_dict(res_coll.items)
    module.exit_json(**result)


if __name__ == "__main__":
    main()
