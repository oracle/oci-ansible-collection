#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_data_safe_on_prem_connector_actions
short_description: Perform actions on an OnPremConnector resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OnPremConnector resource in Oracle Cloud Infrastructure
    - For I(action=generate_on_prem_connector_configuration), creates and downloads the configuration of the specified on-premises connector.
version_added: "2.9"
author: Oracle (@oracle)
options:
    password:
        description:
            - The password to encrypt the keys inside the wallet included as part of the configuration. The password must be between 12 and 30 characters long
              and must contain atleast 1 uppercase, 1 lowercase, 1 numeric, and 1 special character.
        type: str
        required: true
    on_prem_connector_id:
        description:
            - The OCID of the on-premises connector.
        type: str
        aliases: ["id"]
        required: true
    dest:
        description:
            - The destination file path to write the configuration file to when I(action=generate_on_prem_connector_configuration). The file will be created if
              it does not exist. If the file already exists, the content will be overwritten. I(dest) is required if
              I(action=generate_on_prem_connector_configuration).
        type: str
        required: true
    action:
        description:
            - The action to perform on the OnPremConnector.
        type: str
        required: true
        choices:
            - "generate_on_prem_connector_configuration"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action generate_on_prem_connector_configuration on on_prem_connector
  oci_data_safe_on_prem_connector_actions:
    password: password_example
    on_prem_connector_id: ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx
    dest: /tmp/on_prem_connector_config_file.zip
    action: generate_on_prem_connector_configuration

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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import GenerateOnPremConnectorConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeOnPremConnectorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        generate_on_prem_connector_configuration
    """

    @staticmethod
    def get_module_resource_id_param():
        return "on_prem_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("on_prem_connector_id")

    def get_get_fn(self):
        return self.client.get_on_prem_connector

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_on_prem_connector,
            on_prem_connector_id=self.module.params.get("on_prem_connector_id"),
        )

    def generate_on_prem_connector_configuration(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateOnPremConnectorConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_on_prem_connector_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                generate_on_prem_connector_configuration_details=action_details,
                on_prem_connector_id=self.module.params.get("on_prem_connector_id"),
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


DataSafeOnPremConnectorActionsHelperCustom = get_custom_class(
    "DataSafeOnPremConnectorActionsHelperCustom"
)


class ResourceHelper(
    DataSafeOnPremConnectorActionsHelperCustom, DataSafeOnPremConnectorActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            password=dict(type="str", required=True, no_log=True),
            on_prem_connector_id=dict(aliases=["id"], type="str", required=True),
            dest=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["generate_on_prem_connector_configuration"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="on_prem_connector",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
