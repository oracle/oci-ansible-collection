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
module: oci_resource_manager_configuration_source_provider_actions
short_description: Perform actions on a ConfigurationSourceProvider resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ConfigurationSourceProvider resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a configuration source provider into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    configuration_source_provider_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration source provider.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              to move the configuration source provider to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ConfigurationSourceProvider.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on configuration_source_provider
  oci_resource_manager_configuration_source_provider_actions:
    # required
    configuration_source_provider_id: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
configuration_source_provider:
    description:
        - Details of the ConfigurationSourceProvider resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration source provider.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where the configuration source
                  provider is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable display name for the configuration source provider.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the configuration source provider.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The date and time when the configuration source provider was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the configuration source provider.
                  For more information about configuration source provider lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__CSPStates).
            returned: on success
            type: str
            sample: ACTIVE
        config_source_provider_type:
            description:
                - The type of configuration source provider.
                  The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
                  The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.
            returned: on success
            type: str
            sample: GITLAB_ACCESS_TOKEN
        private_server_config_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                private_endpoint_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a private endpoint associated with the
                          configuration source provider.
                    returned: on success
                    type: str
                    sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a certificate associated with the
                          configuration source provider.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        api_endpoint:
            description:
                - "The GitHub service endpoint.
                  Example: `https://github.com/`"
            returned: on success
            type: str
            sample: api_endpoint_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "config_source_provider_type": "GITLAB_ACCESS_TOKEN",
        "private_server_config_details": {
            "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "api_endpoint": "api_endpoint_example"
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
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import (
        ChangeConfigurationSourceProviderCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationSourceProviderActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "configuration_source_provider_id"

    def get_module_resource_id(self):
        return self.module.params.get("configuration_source_provider_id")

    def get_get_fn(self):
        return self.client.get_configuration_source_provider

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration_source_provider,
            configuration_source_provider_id=self.module.params.get(
                "configuration_source_provider_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeConfigurationSourceProviderCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_configuration_source_provider_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_source_provider_id=self.module.params.get(
                    "configuration_source_provider_id"
                ),
                change_configuration_source_provider_compartment_details=action_details,
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


ConfigurationSourceProviderActionsHelperCustom = get_custom_class(
    "ConfigurationSourceProviderActionsHelperCustom"
)


class ResourceHelper(
    ConfigurationSourceProviderActionsHelperCustom,
    ConfigurationSourceProviderActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            configuration_source_provider_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration_source_provider",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
