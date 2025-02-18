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
module: oci_ai_language_evaluation_result_facts
short_description: Fetches details about one or multiple EvaluationResult resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EvaluationResult resources in Oracle Cloud Infrastructure
    - Get a (paginated) list of evaluation results for a given model.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - unique model OCID.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List evaluation_results
  oci_ai_language_evaluation_result_facts:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
evaluation_results:
    description:
        - List of EvaluationResult resources
    returned: on success
    type: complex
    contains:
        model_type:
            description:
                - Model type
            returned: on success
            type: str
            sample: model_type_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "model_type": "model_type_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
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


class AiLanguageEvaluationResultFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "model_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_evaluation_results,
            model_id=self.module.params.get("model_id"),
            **optional_kwargs
        )


AiLanguageEvaluationResultFactsHelperCustom = get_custom_class(
    "AiLanguageEvaluationResultFactsHelperCustom"
)


class ResourceFactsHelper(
    AiLanguageEvaluationResultFactsHelperCustom,
    AiLanguageEvaluationResultFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(model_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="evaluation_result",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(evaluation_results=result)


if __name__ == "__main__":
    main()
