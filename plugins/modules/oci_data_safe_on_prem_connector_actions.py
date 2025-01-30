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
module: oci_data_safe_on_prem_connector_actions
short_description: Perform actions on an OnPremConnector resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OnPremConnector resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified on-premises connector into a different compartment.
    - For I(action=generate_on_prem_connector_configuration), creates and downloads the configuration of the specified on-premises connector.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the new compartment where you want to move the on-premises connector.
            - Required for I(action=change_compartment).
        type: str
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
            - Required for I(action=generate_on_prem_connector_configuration).
        type: str
    password:
        description:
            - The password to encrypt the keys inside the wallet included as part of the configuration. The password must be between 12 and 30 characters long
              and must contain atleast 1 uppercase, 1 lowercase, 1 numeric, and 1 special character.
            - Required for I(action=generate_on_prem_connector_configuration).
        type: str
    on_prem_connector_id:
        description:
            - The OCID of the on-premises connector.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the OnPremConnector.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "generate_on_prem_connector_configuration"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on on_prem_connector
  oci_data_safe_on_prem_connector_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    on_prem_connector_id: "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action generate_on_prem_connector_configuration on on_prem_connector
  oci_data_safe_on_prem_connector_actions:
    # required
    dest: /tmp/myfile
    password: example-password
    on_prem_connector_id: "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate_on_prem_connector_configuration

"""

RETURN = """
on_prem_connector:
    description:
        - Details of the OnPremConnector resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the on-premises connector.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the on-premises connector.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the on-premises connector.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description of the on-premises connector.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the on-premises connector was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the on-premises connector.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current state of the on-premises connector.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        available_version:
            description:
                - Latest available version of the on-premises connector.
            returned: on success
            type: str
            sample: available_version_example
        created_version:
            description:
                - Created version of the on-premises connector.
            returned: on success
            type: str
            sample: created_version_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "available_version": "available_version_example",
        "created_version": "created_version_example"
    }
"""

from ansible.module_utils._text import to_bytes
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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import ChangeOnPremConnectorCompartmentDetails
    from oci.data_safe.models import GenerateOnPremConnectorConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeOnPremConnectorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOnPremConnectorCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_on_prem_connector_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                on_prem_connector_id=self.module.params.get("on_prem_connector_id"),
                change_on_prem_connector_compartment_details=action_details,
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

    def generate_on_prem_connector_configuration(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateOnPremConnectorConfigurationDetails
        )
        response = oci_wait_utils.call_and_wait(
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


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
            compartment_id=dict(type="str"),
            dest=dict(type="str"),
            password=dict(type="str", no_log=True),
            on_prem_connector_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "generate_on_prem_connector_configuration",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
