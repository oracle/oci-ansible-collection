#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_tag_facts
short_description: Retrieve details of tag key definitions for a specified tag namespace in OCI
description:
    - This module retrieves details of all tag key definitions of a specified tag namespace, or a specific tag key
      definition in OCI.
version_added: "2.5"
options:
    tag_namespace_id:
        description: The OCID of the tag namespace whose tag definitions must be retrieved
        required: true
    tag_name:
        description: The name of the tag, whose details must be retrieved
        required: false
        aliases: ['name']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all the tag key definitions of the specified tag namespace
  oci_tag_facts:
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxEXAMPLExxxxx"

- name: Get details of a specific tag key definition
  oci_tag_facts:
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxEXAMPLExxxxx"
    name: "CostCenter"
"""

RETURN = """
tags:
    description: Information about one or more tag key definitions
    returned: on success
    type: complex
    contains:
        id:
            description: The OCID of the tag key definition.
            returned: always
            type: string
            sample: ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx
        compartment_id:
            description: The OCID of the compartment that contains the tag definition.
            returned: always
            type: string
            sample: null
        name:
            description: The name of the tag. The name must be unique across all tags in the namespace and can't be
                         changed.
            returned: always
            type: string
            sample: "CostCenter"
        description:
            description: The description that was assigned to the tag key definition.
            returned: always
            type: string
            sample: "This tag will show the cost center that will be used for billing of resources."
        time_created:
            description: Date and time the Tag key definition object was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        is_retired:
            description: Whether the tag key definition is retired.
            returned: always
            type: string
            sample: yes
    sample: {
        "tags": [
            {
                "compartment_id": null,
                "defined_tags": {},
                "description": "This tag will show the cost center that will be used for billing of resources.",
                "freeform_tags": {},
                "id": "ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx",
                "is_retired": false,
                "name": "CostCenter",
                "time_created": "2018-01-16T04:55:22.600000+00:00"
            }
        ]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_tags(identity_client, tag_namespace_id, tag_name, module):
    try:
        if tag_name is not None:
            tag = oci_utils.call_with_backoff(
                identity_client.get_tag,
                tag_namespace_id=tag_namespace_id,
                tag_name=tag_name,
            ).data
            return to_dict([tag])

        return to_dict(
            oci_utils.call_with_backoff(
                identity_client.list_tags, tag_namespace_id=tag_namespace_id
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tag_namespace_id=dict(type="str", required=True),
            tag_name=dict(type="str", required=False, aliases=["name"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    tag_namespace_id = module.params.get("tag_namespace_id")
    tag_name = module.params.get("tag_name", None)
    result = list_tags(identity_client, tag_namespace_id, tag_name, module)

    module.exit_json(tags=result)


if __name__ == "__main__":
    main()
