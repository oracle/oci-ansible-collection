#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
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
module: oci_tag_namespace_facts
short_description: Retrieve details of tag namespaces for a specified compartment or tenancy in OCI
description:
    - This module retrieves details of tag namespaces of a specified tenancy or compartment in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment whose tag namespaces must be retrieved. To get the tag namespaces of
                     the tenancy, provide the tenancy's root compartment OCID as the I(compartment_id)
        required: false
    tag_namespace_id:
        description: The OCID of a tag namespace for which details must be retrieved. Required when facts about a
                     specific tag namespace needs to be obtained.
        required: false
        aliases: ['id']
    include_subcompartments:
        description: An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments.
                     If this parameter is not specified, only the tag namespaces defined in the specified compartment
                     are retrieved.
        required: false
        type: bool
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get details of all the tag namespaces of the specified user
  oci_tag_namespace_facts:
    compartment_id: "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx"

- name: Get details of a specific tag namespace
  oci_tag_namespace_facts:
    id: "ocid1.namespace.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
tag_namespaces:
    description: Information about one or more tag namespaces in the specified user
    returned: on success
    type: complex
    contains:
        id:
            description: The OCID of the tag namespace.
            returned: always
            type: string
            sample: ocid1.tagnamespace.oc1..xxxxxEXAMPLExxxxx
        compartment_id:
            description: The OCID of the compartment that contains the tag namespace.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        name:
            description: The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and
                         cannot be changed.
            returned: always
            type: string
            sample: BillingTags
        description:
            description: The description that was assigned to the tag namespace.
            returned: always
            type: string
            sample: "This namespace contains tags that will be used in billing."
        time_created:
            description: Date and time the tag namespace object was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        is_retired:
            description: Whether the tag namespace is retired.
            returned: always
            type: string
            sample: yes
    sample: {
        "tag_namespaces": [
            {
                'name': 'BillingTags',
                'defined_tags': {},
                'description': "This namespace contains tags that will be used in billing.",
                'id': 'ocid1.tagnamespace.oc1..xxxxxEXAMPLExxxxx',
                'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx',
                'freeform_tags': {},
                'is_retired': False,
                'time_created': '2018-01-15T17:36:10.388000+00:00'
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


def list_tag_namespaces(identity_client, compartment_id, tag_namespace_id, module):
    try:
        if tag_namespace_id:
            tag_ns = oci_utils.call_with_backoff(
                identity_client.get_tag_namespace, tag_namespace_id=tag_namespace_id
            ).data
            return to_dict([tag_ns])

        optional_list_method_params = ["include_subcompartments", "name"]
        optional_kwargs = dict(
            (param, module.params[param])
            for param in optional_list_method_params
            if module.params.get(param) is not None
        )
        return to_dict(
            oci_utils.list_all_resources(
                identity_client.list_tag_namespaces,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            tag_namespace_id=dict(type="str", required=False, aliases=["id"]),
            include_subcompartments=dict(type="bool", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    compartment_id = module.params.get("compartment_id")
    tagns_id = module.params.get("tag_namespace_id", None)
    result = list_tag_namespaces(identity_client, compartment_id, tagns_id, module)

    module.exit_json(tag_namespaces=result)


if __name__ == "__main__":
    main()
