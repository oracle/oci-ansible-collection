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
module: oci_data_science_model_actions
short_description: Perform actions on a Model resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Model resource in Oracle Cloud Infrastructure
    - For I(action=activate), activates the model.
    - For I(action=deactivate), deactivates the model.
version_added: "2.9"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Model.
        type: str
        required: true
        choices:
            - "activate"
            - "deactivate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on model
  oci_data_science_model_actions:
    model_id: ocid1.model.oc1..xxxxxxEXAMPLExxxxxx
    action: activate

- name: Perform action deactivate on model
  oci_data_science_model_actions:
    model_id: ocid1.model.oc1..xxxxxxEXAMPLExxxxxx
    action: deactivate

"""

RETURN = """
model:
    description:
        - Details of the Model resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model's compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the project associated with the model.
            returned: on success
            type: string
            sample: ocid1.project.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - A short blurb describing the model.
            returned: on success
            type: string
            sample: description_example
        lifecycle_state:
            description:
                - The state of the model.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - "The date and time the resource was created, in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the user who created the model.
            returned: on success
            type: string
            sample: created_by_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        deactivate
    """

    @staticmethod
    def get_module_resource_id_param():
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def activate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def deactivate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deactivate_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


DataScienceModelActionsHelperCustom = get_custom_class(
    "DataScienceModelActionsHelperCustom"
)


class ResourceHelper(
    DataScienceModelActionsHelperCustom, DataScienceModelActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["activate", "deactivate"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
