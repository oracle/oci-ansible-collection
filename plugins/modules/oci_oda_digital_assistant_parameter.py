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
module: oci_oda_digital_assistant_parameter
short_description: Manage a DigitalAssistantParameter resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a DigitalAssistantParameter resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    digital_assistant_id:
        description:
            - Unique Digital Assistant identifier.
        type: str
        required: true
    parameter_name:
        description:
            - The name of a Digital Assistant Parameter.  This is unique with the Digital Assistant.
        type: str
        required: true
    value:
        description:
            - The current value.  The value will be interpreted based on the `type`.
        type: str
        required: true
    state:
        description:
            - The state of the DigitalAssistantParameter.
            - Use I(state=present) to update an existing a DigitalAssistantParameter.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update digital_assistant_parameter
  oci_oda_digital_assistant_parameter:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    digital_assistant_id: "ocid1.digitalassistant.oc1..xxxxxxEXAMPLExxxxxx"
    parameter_name: parameter_name_example
    value: value_example

"""

RETURN = """
digital_assistant_parameter:
    description:
        - Details of the DigitalAssistantParameter resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The Parameter name.  This must be unique within the parent resource.
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - The display name for the Parameter.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A description of the Parameter.
            returned: on success
            type: str
            sample: description_example
        type:
            description:
                - The value type.
            returned: on success
            type: str
            sample: STRING
        value:
            description:
                - The current value.  The value will be interpreted based on the `type`.
            returned: on success
            type: str
            sample: value_example
        lifecycle_state:
            description:
                - The Parameter's current state.
            returned: on success
            type: str
            sample: CREATING
    sample: {
        "name": "name_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "type": "STRING",
        "value": "value_example",
        "lifecycle_state": "CREATING"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import ManagementClient
    from oci.oda.models import UpdateDigitalAssistantParameterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DigitalAssistantParameterHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(
            DigitalAssistantParameterHelperGen, self
        ).get_possible_entity_types() + [
            "digitalassistantparameter",
            "digitalassistantparameters",
            "odadigitalassistantparameter",
            "odadigitalassistantparameters",
            "digitalassistantparameterresource",
            "digitalassistantparametersresource",
            "parameter",
            "parameters",
            "odaparameter",
            "odaparameters",
            "parameterresource",
            "parametersresource",
            "oda",
        ]

    def get_module_resource_id_param(self):
        return "parameter_name"

    def get_module_resource_id(self):
        return self.module.params.get("parameter_name")

    def get_get_fn(self):
        return self.client.get_digital_assistant_parameter

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_digital_assistant_parameter,
            parameter_name=summary_model.name,
            digital_assistant_id=self.module.params.get("digital_assistant_id"),
            oda_instance_id=self.module.params.get("oda_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_digital_assistant_parameter,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            digital_assistant_id=self.module.params.get("digital_assistant_id"),
            parameter_name=self.module.params.get("parameter_name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "oda_instance_id",
            "digital_assistant_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_digital_assistant_parameters, **kwargs
        )

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return UpdateDigitalAssistantParameterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_digital_assistant_parameter,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                digital_assistant_id=self.module.params.get("digital_assistant_id"),
                parameter_name=self.module.params.get("parameter_name"),
                update_digital_assistant_parameter_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


DigitalAssistantParameterHelperCustom = get_custom_class(
    "DigitalAssistantParameterHelperCustom"
)


class ResourceHelper(
    DigitalAssistantParameterHelperCustom, DigitalAssistantParameterHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            oda_instance_id=dict(type="str", required=True),
            digital_assistant_id=dict(type="str", required=True),
            parameter_name=dict(type="str", required=True),
            value=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="digital_assistant_parameter",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
