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
module: oci_database_management_database_parameter_facts
short_description: Fetches details about one or multiple DatabaseParameter resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseParameter resources in Oracle Cloud Infrastructure
    - Gets the list of database parameters for the specified Managed Database. The parameters are listed in alphabetical order, along with their current values.
version_added: "2.9"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    source:
        description:
            - The source used to list database parameters. `CURRENT` is used to get the
              database parameters that are currently in effect for the database
              instance. `SPFILE` is used to list parameters from the server parameter
              file. Default is `CURRENT`.
        type: str
        choices:
            - "CURRENT"
            - "SPFILE"
    name:
        description:
            - A filter to return all parameters that have the text given in their names.
        type: str
    is_allowed_values_included:
        description:
            - When true, results include a list of valid values for parameters (if applicable).
        type: bool
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The
              default sort order for `NAME` is ascending and it is case-sensitive.
        type: str
        choices:
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List database_parameters
  oci_database_management_database_parameter_facts:
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
database_parameters:
    description:
        - List of DatabaseParameter resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The parameter name.
            returned: on success
            type: string
            sample: name_example
        type:
            description:
                - The parameter type.
            returned: on success
            type: string
            sample: BOOLEAN
        value:
            description:
                - The parameter value.
            returned: on success
            type: string
            sample: value_example
        display_value:
            description:
                - The parameter value in a user-friendly format. For example, if the `value` property shows the value 262144 for a big integer parameter, then
                  the `displayValue` property will show the value 256K.
            returned: on success
            type: string
            sample: display_value_example
        number:
            description:
                - The parameter number.
            returned: on success
            type: float
            sample: 10
        is_default:
            description:
                - Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`).
            returned: on success
            type: bool
            sample: true
        is_session_modifiable:
            description:
                - Indicates whether the parameter can be changed with `ALTER SESSION` (`TRUE`) or not (`FALSE`)
            returned: on success
            type: bool
            sample: true
        is_system_modifiable:
            description:
                - "Indicates whether the parameter can be changed with `ALTER SYSTEM` and when the change takes effect:
                  - IMMEDIATE: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change
                    takes effect immediately.
                  - DEFERRED: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes
                    effect in subsequent sessions.
                  - FALSE: Parameter cannot be changed with `ALTER SYSTEM` unless a server parameter file was used to start the instance. The change takes
                    effect in subsequent instances."
            returned: on success
            type: string
            sample: IMMEDIATE
        is_pdb_modifiable:
            description:
                - Indicates whether the parameter can be modified on a per-PDB basis (`TRUE`) or not (`FALSE`). In a non-CDB, the value of this property is
                  `null`.
            returned: on success
            type: bool
            sample: true
        is_instance_modifiable:
            description:
                - For parameters that can be changed with `ALTER SYSTEM`, indicates whether the value of the parameter can be different for every instance
                  (`TRUE`) or whether the parameter must have the same value for all Real Application Clusters instances (`FALSE`). For other parameters, this
                  is always `FALSE`.
            returned: on success
            type: bool
            sample: true
        is_modified:
            description:
                - Indicates how the parameter was modified. If an `ALTER SYSTEM` was performed, the value will be `MODIFIED`.
            returned: on success
            type: string
            sample: MODIFIED
        is_adjusted:
            description:
                - Indicates whether Oracle adjusted the input value to a more suitable value.
            returned: on success
            type: bool
            sample: true
        is_deprecated:
            description:
                - Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`).
            returned: on success
            type: bool
            sample: true
        is_basic:
            description:
                - Indicates whether the parameter is a basic parameter (`TRUE`) or not (`FALSE`).
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - The description of the parameter.
            returned: on success
            type: string
            sample: description_example
        ordinal:
            description:
                - The position (ordinal number) of the parameter value. Useful only for parameters whose values are lists of strings.
            returned: on success
            type: float
            sample: 10
        update_comment:
            description:
                - The comments associated with the most recent update.
            returned: on success
            type: string
            sample: update_comment_example
        container_id:
            description:
                - "The ID of the database container to which the data pertains.
                  Possible values include:
                  - `0`: This value is used for data that pertain to the entire CDB. This value is also used for data in non-CDBs.
                  - `1`: This value is used for data that pertain to only the root container.
                  - `n`: Where n is the applicable container ID for the data."
            returned: on success
            type: float
            sample: 10
        category:
            description:
                - The parameter category.
            returned: on success
            type: string
            sample: category_example
        constraint:
            description:
                - Applicable in case of Oracle Real Application Clusters (Oracle RAC) databases.
                  A `UNIQUE` parameter is one which is unique to each Oracle Real Application
                  Clusters (Oracle RAC) instance. For example, the parameter `INSTANCE_NUMBER`
                  must have different values in each instance. An `IDENTICAL` parameter must
                  have the same value for every instance. For example, the parameter
                  `DB_BLOCK_SIZE` must have the same value in all instances.
            returned: on success
            type: string
            sample: UNIQUE
        sid:
            description:
                - The database instance SID for which the parameter is defined.
            returned: on success
            type: string
            sample: sid_example
        is_specified:
            description:
                - Indicates whether the parameter was specified in the server parameter file (`TRUE`) or not (`FALSE`). Applicable only when the parameter
                  source is `SPFILE`.
            returned: on success
            type: bool
            sample: true
        allowed_values:
            description:
                - A list of allowed values for this parameter.
            returned: on success
            type: complex
            contains:
                ordinal:
                    description:
                        - The ordinal number in the list (1-based).
                    returned: on success
                    type: float
                    sample: 10
                value:
                    description:
                        - The parameter value at ordinal.
                    returned: on success
                    type: string
                    sample: value_example
                is_default:
                    description:
                        - Indicates whether the given ordinal value is the default value for the parameter.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "name": "name_example",
        "type": "BOOLEAN",
        "value": "value_example",
        "display_value": "display_value_example",
        "number": 10,
        "is_default": true,
        "is_session_modifiable": true,
        "is_system_modifiable": "IMMEDIATE",
        "is_pdb_modifiable": true,
        "is_instance_modifiable": true,
        "is_modified": "MODIFIED",
        "is_adjusted": true,
        "is_deprecated": true,
        "is_basic": true,
        "description": "description_example",
        "ordinal": 10,
        "update_comment": "update_comment_example",
        "container_id": 10,
        "category": "category_example",
        "constraint": "UNIQUE",
        "sid": "sid_example",
        "is_specified": true,
        "allowed_values": [{
            "ordinal": 10,
            "value": "value_example",
            "is_default": true
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseParameterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "source",
            "name",
            "is_allowed_values_included",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_parameters,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


DatabaseParameterFactsHelperCustom = get_custom_class(
    "DatabaseParameterFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseParameterFactsHelperCustom, DatabaseParameterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            source=dict(type="str", choices=["CURRENT", "SPFILE"]),
            name=dict(type="str"),
            is_allowed_values_included=dict(type="bool"),
            sort_by=dict(type="str", choices=["NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_parameter",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_parameters=result)


if __name__ == "__main__":
    main()
