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
module: oci_mysql_configuration_facts
short_description: Fetches details about one or multiple Configuration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Configuration resources in Oracle Cloud Infrastructure
    - Lists the Configurations available when creating a DB System.
    - This may include DEFAULT configurations per Shape and CUSTOM configurations.
    - "The default sort order is a multi-part sort by:
        - shapeName, ascending
        - DEFAULT-before-CUSTOM
        - displayName ascending"
    - If I(configuration_id) is specified, the details of a single Configuration will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    configuration_id:
        description:
            - The OCID of the Configuration.
            - Required to get a specific configuration.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple configurations.
        type: str
    lifecycle_state:
        description:
            - Configuration Lifecycle State
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    type:
        description:
            - The requested Configuration types.
        type: list
        choices:
            - "DEFAULT"
            - "CUSTOM"
    display_name:
        description:
            - A filter to return only the resource matching the given display name exactly.
        type: str
        aliases: ["name"]
    shape_name:
        description:
            - The requested Shape name.
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as
              ascending.
        type: str
        choices:
            - "displayName"
            - "shapeName"
            - "timeCreated"
            - "timeUpdated"
    sort_order:
        description:
            - The sort order to use (ASC or DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List configurations
  oci_mysql_configuration_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific configuration
  oci_mysql_configuration_facts:
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
configurations:
    description:
        - List of Configuration resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Configuration.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the Compartment the Configuration exists in.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - User-provided data about the Configuration.
            returned: on success
            type: string
            sample: description_example
        display_name:
            description:
                - The display name of the Configuration.
            returned: on success
            type: string
            sample: display_name_example
        shape_name:
            description:
                - The name of the associated Shape.
            returned: on success
            type: string
            sample: shape_name_example
        type:
            description:
                - The Configuration type, DEFAULT or CUSTOM.
            returned: on success
            type: string
            sample: DEFAULT
        time_created:
            description:
                - The date and time the Configuration was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The date and time the Configuration was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the Configuration.
            returned: on success
            type: string
            sample: ACTIVE
        variables:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                completion_type:
                    description:
                        - "(\\"completion_type\\")"
                    returned: on success
                    type: string
                    sample: NO_CHAIN
                default_authentication_plugin:
                    description:
                        - "(\\"default_authentication_plugin\\")"
                    returned: on success
                    type: string
                    sample: mysql_native_password
                transaction_isolation:
                    description:
                        - "(\\"transaction_isolation\\")"
                    returned: on success
                    type: string
                    sample: READ-UNCOMMITTED
                innodb_ft_server_stopword_table:
                    description:
                        - "(\\"innodb_ft_server_stopword_table\\")"
                    returned: on success
                    type: string
                    sample: innodb_ft_server_stopword_table_example
                mandatory_roles:
                    description:
                        - "(\\"mandatory_roles\\")"
                    returned: on success
                    type: string
                    sample: mandatory_roles_example
                autocommit:
                    description:
                        - "(\\"autocommit\\")"
                    returned: on success
                    type: bool
                    sample: true
                foreign_key_checks:
                    description:
                        - "(\\"foreign_key_checks\\")"
                    returned: on success
                    type: bool
                    sample: true
                innodb_ft_enable_stopword:
                    description:
                        - "(\\"innodb_ft_enable_stopword\\")"
                    returned: on success
                    type: bool
                    sample: true
                local_infile:
                    description:
                        - "(\\"local_infile\\")"
                    returned: on success
                    type: bool
                    sample: true
                mysql_firewall_mode:
                    description:
                        - "(\\"mysql_firewall_mode\\")"
                    returned: on success
                    type: bool
                    sample: true
                mysqlx_enable_hello_notice:
                    description:
                        - "(\\"mysqlx_enable_hello_notice\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: bool
                    sample: true
                sql_require_primary_key:
                    description:
                        - "(\\"sql_require_primary_key\\")"
                    returned: on success
                    type: bool
                    sample: true
                sql_warnings:
                    description:
                        - "(\\"sql_warnings\\")"
                    returned: on success
                    type: bool
                    sample: true
                binlog_expire_logs_seconds:
                    description:
                        - "(\\"binlog_expire_logs_seconds\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                innodb_buffer_pool_size:
                    description:
                        - "(\\"innodb_buffer_pool_size\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_ft_result_cache_limit:
                    description:
                        - "(\\"innodb_ft_result_cache_limit\\")"
                    returned: on success
                    type: int
                    sample: 56
                max_connections:
                    description:
                        - "(\\"max_connections\\")"
                    returned: on success
                    type: int
                    sample: 56
                max_prepared_stmt_count:
                    description:
                        - "(\\"max_prepared_stmt_count\\")"
                    returned: on success
                    type: int
                    sample: 56
                connect_timeout:
                    description:
                        - "(\\"connect_timeout\\")"
                    returned: on success
                    type: int
                    sample: 56
                cte_max_recursion_depth:
                    description:
                        - "(\\"cte_max_recursion_depth\\")"
                    returned: on success
                    type: int
                    sample: 56
                generated_random_password_length:
                    description:
                        - "(\\"generated_random_password_length\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                information_schema_stats_expiry:
                    description:
                        - "(\\"information_schema_stats_expiry\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_buffer_pool_instances:
                    description:
                        - "(\\"innodb_buffer_pool_instances\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_ft_max_token_size:
                    description:
                        - "(\\"innodb_ft_max_token_size\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_ft_min_token_size:
                    description:
                        - "(\\"innodb_ft_min_token_size\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_ft_num_word_optimize:
                    description:
                        - "(\\"innodb_ft_num_word_optimize\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_lock_wait_timeout:
                    description:
                        - "(\\"innodb_lock_wait_timeout\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_max_purge_lag:
                    description:
                        - "(\\"innodb_max_purge_lag\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_max_purge_lag_delay:
                    description:
                        - "(\\"innodb_max_purge_lag_delay\\")"
                    returned: on success
                    type: int
                    sample: 56
                max_execution_time:
                    description:
                        - "(\\"max_execution_time\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_connect_timeout:
                    description:
                        - "(\\"mysqlx_connect_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_document_id_unique_prefix:
                    description:
                        - "(\\"mysqlx_document_id_unique_prefix\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_idle_worker_thread_timeout:
                    description:
                        - "(\\"mysqlx_idle_worker_thread_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_interactive_timeout:
                    description:
                        - "(\\"mysqlx_interactive_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_max_allowed_packet:
                    description:
                        - "(\\"mysqlx_max_allowed_packet\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_min_worker_threads:
                    description:
                        - "(\\"mysqlx_min_worker_threads\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_read_timeout:
                    description:
                        - "(\\"mysqlx_read_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_wait_timeout:
                    description:
                        - "(\\"mysqlx_wait_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_write_timeout:
                    description:
                        - "(\\"mysqlx_write_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                parser_max_mem_size:
                    description:
                        - "(\\"parser_max_mem_size\\")"
                    returned: on success
                    type: int
                    sample: 56
                query_alloc_block_size:
                    description:
                        - "(\\"query_alloc_block_size\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                query_prealloc_size:
                    description:
                        - "(\\"query_prealloc_size\\") DEPRECATED -- variable should not be settable and will be ignored"
                    returned: on success
                    type: int
                    sample: 56
                sql_mode:
                    description:
                        - "(\\"sql_mode\\")"
                    returned: on success
                    type: string
                    sample: sql_mode_example
                mysqlx_deflate_default_compression_level:
                    description:
                        - "Set the default compression level for the deflate algorithm. (\\"mysqlx_deflate_default_compression_level\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_deflate_max_client_compression_level:
                    description:
                        - "Limit the upper bound of accepted compression levels for the deflate algorithm. (\\"mysqlx_deflate_max_client_compression_level\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_lz4_max_client_compression_level:
                    description:
                        - "Limit the upper bound of accepted compression levels for the lz4 algorithm. (\\"mysqlx_lz4_max_client_compression_level\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_lz4_default_compression_level:
                    description:
                        - "Set the default compression level for the lz4 algorithm. (\\"mysqlx_lz4_default_compression_level\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_zstd_max_client_compression_level:
                    description:
                        - "Limit the upper bound of accepted compression levels for the zstd algorithm. (\\"mysqlx_zstd_max_client_compression_level\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_zstd_default_compression_level:
                    description:
                        - "Set the default compression level for the zstd algorithm. (\\"mysqlx_zstd_default_compression_level\\")"
                    returned: on success
                    type: int
                    sample: 56
                mysql_zstd_default_compression_level:
                    description:
                        - "DEPRECATED -- typo of mysqlx_zstd_default_compression_level. variable will be ignored."
                    returned: on success
                    type: int
                    sample: 56
        parent_configuration_id:
            description:
                - "The OCID of the Configuration from which this Configuration is
                  \\"derived\\". This is entirely a metadata relationship. There is no
                  relation between the values in this Configuration and its parent."
            returned: on success
            type: string
            sample: "ocid1.parentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "shape_name": "shape_name_example",
        "type": "DEFAULT",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "variables": {
            "completion_type": "NO_CHAIN",
            "default_authentication_plugin": "mysql_native_password",
            "transaction_isolation": "READ-UNCOMMITTED",
            "innodb_ft_server_stopword_table": "innodb_ft_server_stopword_table_example",
            "mandatory_roles": "mandatory_roles_example",
            "autocommit": true,
            "foreign_key_checks": true,
            "innodb_ft_enable_stopword": true,
            "local_infile": true,
            "mysql_firewall_mode": true,
            "mysqlx_enable_hello_notice": true,
            "sql_require_primary_key": true,
            "sql_warnings": true,
            "binlog_expire_logs_seconds": 56,
            "innodb_buffer_pool_size": 56,
            "innodb_ft_result_cache_limit": 56,
            "max_connections": 56,
            "max_prepared_stmt_count": 56,
            "connect_timeout": 56,
            "cte_max_recursion_depth": 56,
            "generated_random_password_length": 56,
            "information_schema_stats_expiry": 56,
            "innodb_buffer_pool_instances": 56,
            "innodb_ft_max_token_size": 56,
            "innodb_ft_min_token_size": 56,
            "innodb_ft_num_word_optimize": 56,
            "innodb_lock_wait_timeout": 56,
            "innodb_max_purge_lag": 56,
            "innodb_max_purge_lag_delay": 56,
            "max_execution_time": 56,
            "mysqlx_connect_timeout": 56,
            "mysqlx_document_id_unique_prefix": 56,
            "mysqlx_idle_worker_thread_timeout": 56,
            "mysqlx_interactive_timeout": 56,
            "mysqlx_max_allowed_packet": 56,
            "mysqlx_min_worker_threads": 56,
            "mysqlx_read_timeout": 56,
            "mysqlx_wait_timeout": 56,
            "mysqlx_write_timeout": 56,
            "parser_max_mem_size": 56,
            "query_alloc_block_size": 56,
            "query_prealloc_size": 56,
            "sql_mode": "sql_mode_example",
            "mysqlx_deflate_default_compression_level": 56,
            "mysqlx_deflate_max_client_compression_level": 56,
            "mysqlx_lz4_max_client_compression_level": 56,
            "mysqlx_lz4_default_compression_level": 56,
            "mysqlx_zstd_max_client_compression_level": 56,
            "mysqlx_zstd_default_compression_level": 56,
            "mysql_zstd_default_compression_level": 56
        },
        "parent_configuration_id": "ocid1.parentconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import MysqlaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "configuration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            configuration_id=self.module.params.get("configuration_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "configuration_id",
            "lifecycle_state",
            "type",
            "display_name",
            "shape_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_configurations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlConfigurationFactsHelperCustom = get_custom_class(
    "MysqlConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    MysqlConfigurationFactsHelperCustom, MysqlConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            type=dict(type="list", choices=["DEFAULT", "CUSTOM"]),
            display_name=dict(aliases=["name"], type="str"),
            shape_name=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=["displayName", "shapeName", "timeCreated", "timeUpdated"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="configuration",
        service_client_class=MysqlaasClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(configurations=result)


if __name__ == "__main__":
    main()
