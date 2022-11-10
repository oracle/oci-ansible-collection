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
module: oci_identity_standard_tag_namespace_template_facts
short_description: Fetches details about one or multiple StandardTagNamespaceTemplate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple StandardTagNamespaceTemplate resources in Oracle Cloud Infrastructure
    - Lists available standard tag namespaces that users can create.
    - If I(standard_tag_namespace_name) is specified, the details of a single StandardTagNamespaceTemplate will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    standard_tag_namespace_name:
        description:
            - The name of the standard tag namespace tempate that is requested
            - Required to get a specific standard_tag_namespace_template.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific standard_tag_namespace_template
  oci_identity_standard_tag_namespace_template_facts:
    # required
    standard_tag_namespace_name: standard_tag_namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List standard_tag_namespace_templates
  oci_identity_standard_tag_namespace_template_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
standard_tag_namespace_templates:
    description:
        - List of StandardTagNamespaceTemplate resources
    returned: on success
    type: complex
    contains:
        tag_definition_templates:
            description:
                - The template of the tag definition. This object includes necessary details to create the provided standard tag definition.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                description:
                    description:
                        - The default description of the tag namespace that users can use to create the tag definition
                    returned: on success
                    type: str
                    sample: description_example
                tag_definition_name:
                    description:
                        - The name of this standard tag definition
                    returned: on success
                    type: str
                    sample: tag_definition_name_example
                type:
                    description:
                        - The type of tag definition. Enum or string.
                    returned: on success
                    type: str
                    sample: ENUM
                possible_values:
                    description:
                        - List of possible values. An optional parameter that will be present if the type of definition is enum.
                    returned: on success
                    type: list
                    sample: []
                is_cost_tracking:
                    description:
                        - Is the tag a cost tracking tag. Default will be false as cost tracking tags have been deprecated
                    returned: on success
                    type: bool
                    sample: true
                enum_mutability:
                    description:
                        - The mutability of the possible values list for enum tags. This will default to IMMUTABLE for string value tags
                    returned: on success
                    type: str
                    sample: IMMUTABLE
        description:
            description:
                - The default description of the tag namespace that users can use to create the tag namespace
            returned: on success
            type: str
            sample: description_example
        standard_tag_namespace_name:
            description:
                - The reserved name of this standard tag namespace
            returned: on success
            type: str
            sample: standard_tag_namespace_name_example
        status:
            description:
                - The status of the standard tag namespace
            returned: on success
            type: str
            sample: status_example
    sample: [{
        "tag_definition_templates": [{
            "description": "description_example",
            "tag_definition_name": "tag_definition_name_example",
            "type": "ENUM",
            "possible_values": [],
            "is_cost_tracking": true,
            "enum_mutability": "IMMUTABLE"
        }],
        "description": "description_example",
        "standard_tag_namespace_name": "standard_tag_namespace_name_example",
        "status": "status_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StandardTagNamespaceTemplateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "standard_tag_namespace_name",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_standard_tag_template,
            compartment_id=self.module.params.get("compartment_id"),
            standard_tag_namespace_name=self.module.params.get(
                "standard_tag_namespace_name"
            ),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_standard_tag_namespaces,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


StandardTagNamespaceTemplateFactsHelperCustom = get_custom_class(
    "StandardTagNamespaceTemplateFactsHelperCustom"
)


class ResourceFactsHelper(
    StandardTagNamespaceTemplateFactsHelperCustom,
    StandardTagNamespaceTemplateFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            standard_tag_namespace_name=dict(type="str"),
            compartment_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="standard_tag_namespace_template",
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

    module.exit_json(standard_tag_namespace_templates=result)


if __name__ == "__main__":
    main()
