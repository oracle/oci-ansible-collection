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
module: oci_psql_default_configuration_facts
short_description: Fetches details about one or multiple DefaultConfiguration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DefaultConfiguration resources in Oracle Cloud Infrastructure
    - Returns a list of default configurations.
    - If I(default_configuration_id) is specified, the details of a single DefaultConfiguration will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    default_configuration_id:
        description:
            - A unique identifier for the configuration.
            - Required to get a specific default_configuration.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - A filter to return only resources if their `lifecycleState` matches the given `lifecycleState`.
        type: str
        choices:
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    db_version:
        description:
            - Verison of the PostgreSQL database, such as 14.9.
        type: str
    shape:
        description:
            - "The name of the shape for the configuration.
              Example: `VM.Standard.E4.Flex`"
        type: str
    configuration_id:
        description:
            - A unique identifier for the configuration.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific default_configuration
  oci_psql_default_configuration_facts:
    # required
    default_configuration_id: "ocid1.defaultconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List default_configurations
  oci_psql_default_configuration_facts:

    # optional
    lifecycle_state: ACTIVE
    display_name: display_name_example
    db_version: db_version_example
    shape: shape_example
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
default_configurations:
    description:
        - List of DefaultConfiguration resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A description for the configuration.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        configuration_details:
            description:
                - ""
                - Returned for get operation
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
                                - Default value for the variable.
                            returned: on success
                            type: str
                            sample: default_config_value_example
                        allowed_values:
                            description:
                                - Range or list of allowed values.
                            returned: on success
                            type: str
                            sample: allowed_values_example
                        is_restart_required:
                            description:
                                - If true, modifying this configuration value will require a restart.
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
                                - Details about the PostgreSQL variable.
                            returned: on success
                            type: str
                            sample: description_example
        id:
            description:
                - A unique identifier for the configuration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the configuration.
            returned: on success
            type: str
            sample: display_name_example
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
        db_version:
            description:
                - Version of the PostgreSQL database.
            returned: on success
            type: str
            sample: db_version_example
        instance_ocpu_count:
            description:
                - CPU core count. Minimum value is 1.
            returned: on success
            type: int
            sample: 56
        instance_memory_size_in_gbs:
            description:
                - Memory size in gigabytes with 1GB increment.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "description": "description_example",
        "configuration_details": {
            "items": [{
                "config_key": "config_key_example",
                "default_config_value": "default_config_value_example",
                "allowed_values": "allowed_values_example",
                "is_restart_required": true,
                "data_type": "data_type_example",
                "is_overridable": true,
                "description": "description_example"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "shape": "shape_example",
        "db_version": "db_version_example",
        "instance_ocpu_count": 56,
        "instance_memory_size_in_gbs": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.psql import PostgresqlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlDefaultConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "default_configuration_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_default_configuration,
            default_configuration_id=self.module.params.get("default_configuration_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "db_version",
            "shape",
            "configuration_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_default_configurations, **optional_kwargs
        )


PsqlDefaultConfigurationFactsHelperCustom = get_custom_class(
    "PsqlDefaultConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    PsqlDefaultConfigurationFactsHelperCustom, PsqlDefaultConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            default_configuration_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "DELETING", "DELETED", "FAILED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            db_version=dict(type="str"),
            shape=dict(type="str"),
            configuration_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="default_configuration",
        service_client_class=PostgresqlClient,
        namespace="psql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(default_configurations=result)


if __name__ == "__main__":
    main()
