#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_ai_language_model_type_info_facts
short_description: Fetches details about a ModelTypeInfo resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ModelTypeInfo resource in Oracle Cloud Infrastructure
    - Gets model capabilities
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_type:
        description:
            - Results like version and model supported info by specifying model type
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific model_type_info
  oci_ai_language_model_type_info_facts:
    # required
    model_type: model_type_example

"""

RETURN = """
model_type_info:
    description:
        - ModelTypeInfo resource
    returned: on success
    type: complex
    contains:
        versions:
            description:
                - Model versions available for this model type
            returned: on success
            type: list
            sample: []
        capabilities:
            description:
                - Model information capabilities related to version
            returned: on success
            type: complex
            contains:
                capability:
                    description:
                        - Model information capabilities related to version
                    returned: on success
                    type: complex
                    contains:
                        details:
                            description:
                                - values
                            returned: on success
                            type: list
                            sample: []
    sample: {
        "versions": [],
        "capabilities": {
            "capability": {
                "details": []
            }
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_language import AIServiceLanguageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageModelTypeInfoFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "model_type",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_type, model_type=self.module.params.get("model_type"),
        )


AiLanguageModelTypeInfoFactsHelperCustom = get_custom_class(
    "AiLanguageModelTypeInfoFactsHelperCustom"
)


class ResourceFactsHelper(
    AiLanguageModelTypeInfoFactsHelperCustom, AiLanguageModelTypeInfoFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(model_type=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="model_type_info",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(model_type_info=result)


if __name__ == "__main__":
    main()
