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
module: oci_psql_configuration_actions
short_description: Perform actions on a Configuration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Configuration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a configuration from one compartment to another. When provided, If-Match is checked against ETag values of the
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    configuration_id:
        description:
            - A unique identifier for the configuration.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the configuration will be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Configuration.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on configuration
  oci_psql_configuration_actions:
    # required
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
configuration:
    description:
        - Details of the Configuration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier for the configuration. Immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the configuration. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A description for the configuration.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the configuration.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time that the configuration was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the configuration.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        shape:
            description:
                - "The name of the shape for the configuration.
                  Example: `VM.Standard.E4.Flex`"
            returned: on success
            type: str
            sample: shape_example
        instance_ocpu_count:
            description:
                - CPU core count.
            returned: on success
            type: int
            sample: 56
        instance_memory_size_in_gbs:
            description:
                - Memory size in gigabytes with 1GB increment.
            returned: on success
            type: int
            sample: 56
        db_version:
            description:
                - Version of the PostgreSQL database.
            returned: on success
            type: str
            sample: db_version_example
        configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of ConfigParms object.
                    returned: on success
                    type: complex
                    contains:
                        config_key:
                            description:
                                - The configuration variable name.
                            returned: on success
                            type: str
                            sample: config_key_example
                        default_config_value:
                            description:
                                - Default value for the configuration variable.
                            returned: on success
                            type: str
                            sample: default_config_value_example
                        overriden_config_value:
                            description:
                                - User-selected configuration variable value.
                            returned: on success
                            type: str
                            sample: overriden_config_value_example
                        allowed_values:
                            description:
                                - Range or list of allowed values.
                            returned: on success
                            type: str
                            sample: allowed_values_example
                        is_restart_required:
                            description:
                                - If true, modifying this configuration value will require a restart of the database.
                            returned: on success
                            type: bool
                            sample: true
                        data_type:
                            description:
                                - Data type of the variable.
                            returned: on success
                            type: str
                            sample: data_type_example
                        is_overridable:
                            description:
                                - Whether the value can be overridden or not.
                            returned: on success
                            type: bool
                            sample: true
                        description:
                            description:
                                - Details about the PostgreSQL parameter.
                            returned: on success
                            type: str
                            sample: description_example
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
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "shape": "shape_example",
        "instance_ocpu_count": 56,
        "instance_memory_size_in_gbs": 56,
        "db_version": "db_version_example",
        "configuration_details": {
            "items": [{
                "config_key": "config_key_example",
                "default_config_value": "default_config_value_example",
                "overriden_config_value": "overriden_config_value_example",
                "allowed_values": "allowed_values_example",
                "is_restart_required": true,
                "data_type": "data_type_example",
                "is_overridable": true,
                "description": "description_example"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.psql import PostgresqlClient
    from oci.psql.models import ChangeConfigurationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("configuration_id")

    def get_get_fn(self):
        return self.client.get_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            configuration_id=self.module.params.get("configuration_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeConfigurationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_configuration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_id=self.module.params.get("configuration_id"),
                change_configuration_compartment_details=action_details,
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


PsqlConfigurationActionsHelperCustom = get_custom_class(
    "PsqlConfigurationActionsHelperCustom"
)


class ResourceHelper(
    PsqlConfigurationActionsHelperCustom, PsqlConfigurationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            configuration_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration",
        service_client_class=PostgresqlClient,
        namespace="psql",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
