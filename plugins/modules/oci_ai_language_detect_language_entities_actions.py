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
module: oci_ai_language_detect_language_entities_actions
short_description: Perform actions on a DetectLanguageEntities resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetectLanguageEntities resource in Oracle Cloud Infrastructure
    - For I(action=detect_language_entities), make a detect call to enitiy pre-deployed model
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    text:
        description:
            - Document text for detect entities.
        type: str
        required: true
    model_version:
        description:
            - Named Entity Recognition model versions. By default user will get output from V2.1 implementation.
        type: str
        choices:
            - "V2.1"
            - "V1.1"
    is_pii:
        description:
            - If this parameter is set to true, you only get PII (Personally identifiable information) entities
              like PhoneNumber, Email, Person, and so on. Default value is false.
        type: bool
    action:
        description:
            - The action to perform on the DetectLanguageEntities.
        type: str
        required: true
        choices:
            - "detect_language_entities"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action detect_language_entities on detect_language_entities
  oci_ai_language_detect_language_entities_actions:
    # required
    text: text_example
    action: detect_language_entities

    # optional
    model_version: V2.1
    is_pii: true

"""

RETURN = """
detect_language_entities_result:
    description:
        - Details of the DetectLanguageEntities resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        entities:
            description:
                - List of detected entities.
            returned: on success
            type: complex
            contains:
                offset:
                    description:
                        - The number of Unicode code points preceding this entity in the submitted text.
                    returned: on success
                    type: int
                    sample: 56
                length:
                    description:
                        - Length of entity text
                    returned: on success
                    type: int
                    sample: 56
                text:
                    description:
                        - Entity text like name of person, location, and so on.
                    returned: on success
                    type: str
                    sample: text_example
                type:
                    description:
                        - Type of entity text like PER, LOC, GPE and NOPE.
                    returned: on success
                    type: str
                    sample: type_example
                is_pii:
                    description:
                        - This flag is to indicate if it is PII entity or not.
                    returned: on success
                    type: bool
                    sample: true
                score:
                    description:
                        - "Score or confidence of extracted entity type.
                          Example: `0.9999856066867399`"
                    returned: on success
                    type: float
                    sample: 1.2
    sample: {
        "entities": [{
            "offset": 56,
            "length": 56,
            "text": "text_example",
            "type": "type_example",
            "is_pii": true,
            "score": 1.2
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.ai_language import AIServiceLanguageClient
    from oci.ai_language.models import DetectLanguageEntitiesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectLanguageEntitiesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        detect_language_entities
    """

    def detect_language_entities(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetectLanguageEntitiesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detect_language_entities,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detect_language_entities_details=action_details,
                model_version=self.module.params.get("model_version"),
                is_pii=self.module.params.get("is_pii"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DetectLanguageEntitiesActionsHelperCustom = get_custom_class(
    "DetectLanguageEntitiesActionsHelperCustom"
)


class ResourceHelper(
    DetectLanguageEntitiesActionsHelperCustom, DetectLanguageEntitiesActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            text=dict(type="str", required=True),
            model_version=dict(type="str", choices=["V2.1", "V1.1"]),
            is_pii=dict(type="bool"),
            action=dict(
                type="str", required=True, choices=["detect_language_entities"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detect_language_entities",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
