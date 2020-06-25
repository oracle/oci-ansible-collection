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
module: oci_identity_tag_namespace_facts
short_description: Fetches details about one or multiple TagNamespace resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TagNamespace resources in Oracle Cloud Infrastructure
    - Lists the tag namespaces in the specified compartment.
    - If I(tag_namespace_id) is specified, the details of a single TagNamespace will be returned.
version_added: "2.5"
options:
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
            - Required to get a specific tag_namespace.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple tag_namespaces.
        type: str
    include_subcompartments:
        description:
            - An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments. If this
              parameter is not specified, only the tag namespaces defined in the specified compartment are retrieved.
        type: bool
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List tag_namespaces
  oci_identity_tag_namespace_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific tag_namespace
  oci_identity_tag_namespace_facts:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
tag_namespaces:
    description:
        - List of TagNamespace resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the tag namespace.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment that contains the tag namespace.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the tag namespace.
            returned: on success
            type: string
            sample: description_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_retired:
            description:
                - Whether the tag namespace is retired.
                  See L(Retiring Key Definitions and Namespace
                  Definitions,https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a
                  tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - "Date and time the tagNamespace was created, in the format defined by RFC3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_retired": true,
        "lifecycle_state": "ACTIVE",
        "time_created": "2016-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagNamespaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "tag_namespace_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag_namespace,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "include_subcompartments",
            "lifecycle_state",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tag_namespaces,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TagNamespaceFactsHelperCustom = get_custom_class("TagNamespaceFactsHelperCustom")


class ResourceFactsHelper(TagNamespaceFactsHelperCustom, TagNamespaceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tag_namespace_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            include_subcompartments=dict(type="bool"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "INACTIVE", "DELETING", "DELETED"]
            ),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tag_namespace",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tag_namespaces=result)


if __name__ == "__main__":
    main()
