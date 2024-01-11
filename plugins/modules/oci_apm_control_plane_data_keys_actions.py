#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_apm_control_plane_data_keys_actions
short_description: Perform actions on a DataKeys resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataKeys resource in Oracle Cloud Infrastructure
    - For I(action=generate), generates a set of new Data Keys for the specified APM domain with the specified names and
      types. These will be added to the existing set of Data Keys for the specified APM domain.
    - For I(action=remove), removes the set of specified Data Keys from the specified APM domain. Agents would no longer
      be able to use these data keys to upload to the APM domain once this operation is completed.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    generate_data_keys_list_details:
        description:
            - List of new Data Keys to be generated.
            - Required for I(action=generate).
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.
                type: str
                required: true
            type:
                description:
                    - Type of the Data Key.
                type: str
                choices:
                    - "PRIVATE"
                    - "PUBLIC"
                required: true
    apm_domain_id:
        description:
            - The OCID of the APM domain.
        type: str
        aliases: ["id"]
        required: true
    remove_data_keys_list_details:
        description:
            - List of Data Keys to be removed.
            - Required for I(action=remove).
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.
                type: str
                required: true
    action:
        description:
            - The action to perform on the DataKeys.
        type: str
        required: true
        choices:
            - "generate"
            - "remove"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action generate on data_keys
  oci_apm_control_plane_data_keys_actions:
    # required
    generate_data_keys_list_details:
    - # required
      name: name_example
      type: PRIVATE
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate

- name: Perform action remove on data_keys
  oci_apm_control_plane_data_keys_actions:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    remove_data_keys_list_details:
    - # required
      name: name_example
    action: remove

"""

RETURN = """
data_keys:
    description:
        - Details of the DataKeys resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        value:
            description:
                - Value of the Data Key.
            returned: on success
            type: str
            sample: value_example
        name:
            description:
                - Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - Type of the Data Key.
            returned: on success
            type: str
            sample: PRIVATE
    sample: {
        "value": "value_example",
        "name": "name_example",
        "type": "PRIVATE"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.apm_control_plane import ApmDomainClient
    from oci.apm_control_plane.models import GenerateDataKeyDetails
    from oci.apm_control_plane.models import RemoveDataKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataKeysActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        generate
        remove
    """

    @staticmethod
    def get_module_resource_id_param():
        return "apm_domain_id"

    def get_module_resource_id(self):
        return self.module.params.get("apm_domain_id")

    def generate(self):
        action_details = []
        if self.module.params.get("generate_data_keys_list_details"):
            for action_details_item in self.module.params.get(
                "generate_data_keys_list_details"
            ):
                action_details.append(
                    oci_common_utils.convert_input_data_to_model_class(
                        action_details_item, GenerateDataKeyDetails
                    )
                )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_data_keys,
            call_fn_args=(),
            call_fn_kwargs=dict(
                generate_data_keys_list_details=action_details,
                apm_domain_id=self.module.params.get("apm_domain_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove(self):
        action_details = []
        if self.module.params.get("remove_data_keys_list_details"):
            for action_details_item in self.module.params.get(
                "remove_data_keys_list_details"
            ):
                action_details.append(
                    oci_common_utils.convert_input_data_to_model_class(
                        action_details_item, RemoveDataKeyDetails
                    )
                )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_data_keys,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                remove_data_keys_list_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataKeysActionsHelperCustom = get_custom_class("DataKeysActionsHelperCustom")


class ResourceHelper(DataKeysActionsHelperCustom, DataKeysActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            generate_data_keys_list_details=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    name=dict(type="str", required=True),
                    type=dict(type="str", required=True, choices=["PRIVATE", "PUBLIC"]),
                ),
            ),
            apm_domain_id=dict(aliases=["id"], type="str", required=True),
            remove_data_keys_list_details=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(name=dict(type="str", required=True)),
            ),
            action=dict(type="str", required=True, choices=["generate", "remove"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_keys",
        service_client_class=ApmDomainClient,
        namespace="apm_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
