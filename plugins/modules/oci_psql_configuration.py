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
module: oci_psql_configuration
short_description: Manage a Configuration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Configuration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new configuration.
    - "This resource has the following action operations in the M(oracle.oci.oci_psql_configuration_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the configuration.
            - Required for create using I(state=present).
        type: str
    shape:
        description:
            - "The name of the shape for the configuration.
              Example: `VM.Standard.E4.Flex`"
            - Required for create using I(state=present).
        type: str
    db_version:
        description:
            - Version of the PostgreSQL database.
            - Required for create using I(state=present).
        type: str
    instance_ocpu_count:
        description:
            - CPU core count.
            - Required for create using I(state=present).
        type: int
    instance_memory_size_in_gbs:
        description:
            - Memory size in gigabytes with 1GB increment.
            - Required for create using I(state=present).
        type: int
    db_configuration_overrides:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            items:
                description:
                    - List of configuration overridden values.
                type: list
                elements: dict
                required: true
                suboptions:
                    config_key:
                        description:
                            - Configuration variable name.
                        type: str
                        required: true
                    overriden_config_value:
                        description:
                            - User-selected variable value.
                        type: str
                        required: true
    system_tags:
        description:
            - "System tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly display name for the configuration. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Details about the configuration set.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    configuration_id:
        description:
            - A unique identifier for the configuration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Configuration.
            - Use I(state=present) to create or update a Configuration.
            - Use I(state=absent) to delete a Configuration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create configuration
  oci_psql_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example
    db_version: db_version_example
    instance_ocpu_count: 56
    instance_memory_size_in_gbs: 56
    db_configuration_overrides:
      # required
      items:
      - # required
        config_key: config_key_example
        overriden_config_value: overriden_config_value_example
    display_name: display_name_example

    # optional
    system_tags: null
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update configuration
  oci_psql_configuration:
    # required
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_psql_configuration:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete configuration
  oci_psql_configuration:
    # required
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_psql_configuration:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.psql import PostgresqlClient
    from oci.psql.models import CreateConfigurationDetails
    from oci.psql.models import UpdateConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PsqlConfigurationHelperGen, self).get_possible_entity_types() + [
            "postgresqlconfiguration",
            "postgresqlconfigurations",
            "psqlpostgresqlconfiguration",
            "psqlpostgresqlconfigurations",
            "postgresqlconfigurationresource",
            "postgresqlconfigurationsresource",
            "configuration",
            "configurations",
            "psqlconfiguration",
            "psqlconfigurations",
            "configurationresource",
            "configurationsresource",
            "psql",
        ]

    def get_module_resource_id_param(self):
        return "configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("configuration_id")

    def get_get_fn(self):
        return self.client.get_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration, configuration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            configuration_id=self.module.params.get("configuration_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "db_version",
            "shape",
            "configuration_id",
        ]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateConfigurationDetails

    def get_exclude_attributes(self):
        return ["db_configuration_overrides"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_configuration_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_id=self.module.params.get("configuration_id"),
                update_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_id=self.module.params.get("configuration_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PsqlConfigurationHelperCustom = get_custom_class("PsqlConfigurationHelperCustom")


class ResourceHelper(PsqlConfigurationHelperCustom, PsqlConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            shape=dict(type="str"),
            db_version=dict(type="str"),
            instance_ocpu_count=dict(type="int"),
            instance_memory_size_in_gbs=dict(type="int"),
            db_configuration_overrides=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            config_key=dict(type="str", required=True, no_log=True),
                            overriden_config_value=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            system_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
