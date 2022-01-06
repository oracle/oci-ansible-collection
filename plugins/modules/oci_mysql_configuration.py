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
module: oci_mysql_configuration
short_description: Manage a Configuration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Configuration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - User-provided data about the Configuration.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - The display name of the Configuration.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    shape_name:
        description:
            - The name of the associated Shape.
            - Required for create using I(state=present).
        type: str
    variables:
        description:
            - ""
        type: dict
        suboptions:
            completion_type:
                description:
                    - "(\\"completion_type\\")"
                type: str
                choices:
                    - "NO_CHAIN"
                    - "CHAIN"
                    - "RELEASE"
            default_authentication_plugin:
                description:
                    - "(\\"default_authentication_plugin\\")"
                type: str
                choices:
                    - "mysql_native_password"
                    - "sha256_password"
                    - "caching_sha2_password"
            transaction_isolation:
                description:
                    - "(\\"transaction_isolation\\")"
                type: str
                choices:
                    - "READ-UNCOMMITTED"
                    - "READ-COMMITED"
                    - "READ-COMMITTED"
                    - "REPEATABLE-READ"
                    - "SERIALIZABLE"
            innodb_ft_server_stopword_table:
                description:
                    - "(\\"innodb_ft_server_stopword_table\\")"
                type: str
            mandatory_roles:
                description:
                    - "(\\"mandatory_roles\\")"
                type: str
            autocommit:
                description:
                    - "(\\"autocommit\\")"
                type: bool
            foreign_key_checks:
                description:
                    - "(\\"foreign_key_checks\\")"
                type: bool
            group_replication_consistency:
                description:
                    - "- EVENTUAL:
                          Both RO and RW transactions do not wait for preceding transactions to be applied before executing.
                          A RW transaction does not wait for other members to apply a transaction. This means that a transaction
                          could be externalized on one member before the others. This also means that in the event of a primary failover,
                          the new primary can accept new RO and RW transactions before the previous primary transactions are all applied.
                          RO transactions could result in outdated values, RW transactions could result in a rollback due to conflicts.
                      - BEFORE_ON_PRIMARY_FAILOVER:
                          New RO or RW transactions with a newly elected primary that is applying backlog from the old
                          primary are held (not applied) until any backlog has been applied. This ensures that when a primary failover happens,
                          intentionally or not, clients always see the latest value on the primary. This guarantees consistency, but means that
                          clients must be able to handle the delay in the event that a backlog is being applied. Usually this delay should be minimal,
                          but does depend on the size of the backlog.
                      - BEFORE:
                          A RW transaction waits for all preceding transactions to complete before being applied. A RO transaction waits for all preceding
                          transactions to complete before being executed. This ensures that this transaction reads the latest value by only affecting the
                          latency of the transaction. This reduces the overhead of synchronization on every RW transaction, by ensuring synchronization is
                          used only on RO transactions. This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER.
                      - AFTER:
                          A RW transaction waits until its changes have been applied to all of the other members. This value has no effect on RO transactions.
                          This mode ensures that when a transaction is committed on the local member, any subsequent transaction reads the written value or
                          a more recent value on any group member. Use this mode with a group that is used for predominantly RO operations to ensure that
                          applied RW transactions are applied everywhere once they commit. This could be used by your application to ensure that subsequent
                          reads fetch the latest data which includes the latest writes. This reduces the overhead of synchronization on every RO transaction,
                          by ensuring synchronization is used only on RW transactions. This consistency level also includes the consistency guarantees
                          provided by BEFORE_ON_PRIMARY_FAILOVER.
                      - BEFORE_AND_AFTER:
                          A RW transaction waits for 1) all preceding transactions to complete before being applied and 2) until its changes have been
                          applied on other members. A RO transaction waits for all preceding transactions to complete before execution takes place.
                          This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER."
                type: str
                choices:
                    - "EVENTUAL"
                    - "BEFORE_ON_PRIMARY_FAILOVER"
                    - "BEFORE"
                    - "AFTER"
                    - "BEFORE_AND_AFTER"
            innodb_ft_enable_stopword:
                description:
                    - "(\\"innodb_ft_enable_stopword\\")"
                type: bool
            local_infile:
                description:
                    - "(\\"local_infile\\")"
                type: bool
            mysql_firewall_mode:
                description:
                    - "(\\"mysql_firewall_mode\\")"
                type: bool
            mysqlx_enable_hello_notice:
                description:
                    - "(\\"mysqlx_enable_hello_notice\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: bool
            sql_require_primary_key:
                description:
                    - "(\\"sql_require_primary_key\\")"
                type: bool
            sql_warnings:
                description:
                    - "(\\"sql_warnings\\")"
                type: bool
            binlog_expire_logs_seconds:
                description:
                    - Sets the binary log expiration period in seconds.
                      binlogExpireLogsSeconds corresponds to the MySQL binary logging system variable
                      L(binlog_expire_logs_seconds,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-
                      log.html#sysvar_binlog_expire_logs_seconds).
                type: int
            binlog_row_metadata:
                description:
                    - Configures the amount of table metadata added to the binary log when using row-based logging.
                      binlogRowMetadata corresponds to the MySQL binary logging system variable
                      L(binlog_row_metadata,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_metadata).
                type: str
                choices:
                    - "FULL"
                    - "MINIMAL"
            binlog_row_value_options:
                description:
                    - When set to PARTIAL_JSON, this enables use of a space-efficient binary log format for updates that modify only a small portion of a JSON
                      document.
                      binlogRowValueOptions corresponds to the MySQL binary logging system variable
                      L(binlog_row_value_options,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_value_options).
                type: str
            binlog_transaction_compression:
                description:
                    - Enables compression for transactions that are written to binary log files on this server.
                      binlogTransactionCompression corresponds to the MySQL binary logging system variable
                      L(binlog_transaction_compression,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-
                      log.html#sysvar_binlog_transaction_compression).
                type: bool
            innodb_buffer_pool_size:
                description:
                    - "(\\"innodb_buffer_pool_size\\")"
                type: int
            innodb_ft_result_cache_limit:
                description:
                    - "(\\"innodb_ft_result_cache_limit\\")"
                type: int
            max_connections:
                description:
                    - "(\\"max_connections\\")"
                type: int
            max_prepared_stmt_count:
                description:
                    - "(\\"max_prepared_stmt_count\\")"
                type: int
            connect_timeout:
                description:
                    - "(\\"connect_timeout\\")"
                type: int
            cte_max_recursion_depth:
                description:
                    - "(\\"cte_max_recursion_depth\\")"
                type: int
            generated_random_password_length:
                description:
                    - "(\\"generated_random_password_length\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            information_schema_stats_expiry:
                description:
                    - "(\\"information_schema_stats_expiry\\")"
                type: int
            innodb_buffer_pool_instances:
                description:
                    - "(\\"innodb_buffer_pool_instances\\")"
                type: int
            innodb_ft_max_token_size:
                description:
                    - "(\\"innodb_ft_max_token_size\\")"
                type: int
            innodb_ft_min_token_size:
                description:
                    - "(\\"innodb_ft_min_token_size\\")"
                type: int
            innodb_ft_num_word_optimize:
                description:
                    - "(\\"innodb_ft_num_word_optimize\\")"
                type: int
            innodb_lock_wait_timeout:
                description:
                    - "(\\"innodb_lock_wait_timeout\\")"
                type: int
            innodb_max_purge_lag:
                description:
                    - "(\\"innodb_max_purge_lag\\")"
                type: int
            innodb_max_purge_lag_delay:
                description:
                    - "(\\"innodb_max_purge_lag_delay\\")"
                type: int
            max_execution_time:
                description:
                    - "(\\"max_execution_time\\")"
                type: int
            mysqlx_connect_timeout:
                description:
                    - "(\\"mysqlx_connect_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_document_id_unique_prefix:
                description:
                    - "(\\"mysqlx_document_id_unique_prefix\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_idle_worker_thread_timeout:
                description:
                    - "(\\"mysqlx_idle_worker_thread_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_interactive_timeout:
                description:
                    - "(\\"mysqlx_interactive_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_max_allowed_packet:
                description:
                    - "(\\"mysqlx_max_allowed_packet\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_min_worker_threads:
                description:
                    - "(\\"mysqlx_min_worker_threads\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_read_timeout:
                description:
                    - "(\\"mysqlx_read_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_wait_timeout:
                description:
                    - "(\\"mysqlx_wait_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            mysqlx_write_timeout:
                description:
                    - "(\\"mysqlx_write_timeout\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            parser_max_mem_size:
                description:
                    - "(\\"parser_max_mem_size\\")"
                type: int
            query_alloc_block_size:
                description:
                    - "(\\"query_alloc_block_size\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            query_prealloc_size:
                description:
                    - "(\\"query_prealloc_size\\") DEPRECATED -- variable should not be settable and will be ignored"
                type: int
            sql_mode:
                description:
                    - "(\\"sql_mode\\")"
                type: str
            mysqlx_deflate_default_compression_level:
                description:
                    - "Set the default compression level for the deflate algorithm. (\\"mysqlx_deflate_default_compression_level\\")"
                type: int
            mysqlx_deflate_max_client_compression_level:
                description:
                    - "Limit the upper bound of accepted compression levels for the deflate algorithm. (\\"mysqlx_deflate_max_client_compression_level\\")"
                type: int
            mysqlx_lz4_max_client_compression_level:
                description:
                    - "Limit the upper bound of accepted compression levels for the lz4 algorithm. (\\"mysqlx_lz4_max_client_compression_level\\")"
                type: int
            mysqlx_lz4_default_compression_level:
                description:
                    - "Set the default compression level for the lz4 algorithm. (\\"mysqlx_lz4_default_compression_level\\")"
                type: int
            mysqlx_zstd_max_client_compression_level:
                description:
                    - "Limit the upper bound of accepted compression levels for the zstd algorithm. (\\"mysqlx_zstd_max_client_compression_level\\")"
                type: int
            mysqlx_zstd_default_compression_level:
                description:
                    - "Set the default compression level for the zstd algorithm. (\\"mysqlx_zstd_default_compression_level\\")"
                type: int
            mysql_zstd_default_compression_level:
                description:
                    - "DEPRECATED -- typo of mysqlx_zstd_default_compression_level. variable will be ignored."
                type: int
    parent_configuration_id:
        description:
            - The OCID of the Configuration from which the new Configuration is derived. The values in CreateConfigurationDetails.variables supersede the
              variables of the parent Configuration.
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
            - The OCID of the Configuration.
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
  oci_mysql_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    shape_name: shape_name_example

    # optional
    description: description_example
    display_name: display_name_example
    variables:
      # optional
      completion_type: NO_CHAIN
      default_authentication_plugin: mysql_native_password
      transaction_isolation: READ-UNCOMMITTED
      innodb_ft_server_stopword_table: innodb_ft_server_stopword_table_example
      mandatory_roles: mandatory_roles_example
      autocommit: true
      foreign_key_checks: true
      group_replication_consistency: EVENTUAL
      innodb_ft_enable_stopword: true
      local_infile: true
      mysql_firewall_mode: true
      mysqlx_enable_hello_notice: true
      sql_require_primary_key: true
      sql_warnings: true
      binlog_expire_logs_seconds: 56
      binlog_row_metadata: FULL
      binlog_row_value_options: binlog_row_value_options_example
      binlog_transaction_compression: true
      innodb_buffer_pool_size: 56
      innodb_ft_result_cache_limit: 56
      max_connections: 56
      max_prepared_stmt_count: 56
      connect_timeout: 56
      cte_max_recursion_depth: 56
      generated_random_password_length: 56
      information_schema_stats_expiry: 56
      innodb_buffer_pool_instances: 56
      innodb_ft_max_token_size: 56
      innodb_ft_min_token_size: 56
      innodb_ft_num_word_optimize: 56
      innodb_lock_wait_timeout: 56
      innodb_max_purge_lag: 56
      innodb_max_purge_lag_delay: 56
      max_execution_time: 56
      mysqlx_connect_timeout: 56
      mysqlx_document_id_unique_prefix: 56
      mysqlx_idle_worker_thread_timeout: 56
      mysqlx_interactive_timeout: 56
      mysqlx_max_allowed_packet: 56
      mysqlx_min_worker_threads: 56
      mysqlx_read_timeout: 56
      mysqlx_wait_timeout: 56
      mysqlx_write_timeout: 56
      parser_max_mem_size: 56
      query_alloc_block_size: 56
      query_prealloc_size: 56
      sql_mode: sql_mode_example
      mysqlx_deflate_default_compression_level: 56
      mysqlx_deflate_max_client_compression_level: 56
      mysqlx_lz4_max_client_compression_level: 56
      mysqlx_lz4_default_compression_level: 56
      mysqlx_zstd_max_client_compression_level: 56
      mysqlx_zstd_default_compression_level: 56
      mysql_zstd_default_compression_level: 56
    parent_configuration_id: "ocid1.parentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update configuration
  oci_mysql_configuration:
    # required
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete configuration
  oci_mysql_configuration:
    # required
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The OCID of the Configuration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the Compartment the Configuration exists in.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - User-provided data about the Configuration.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - The display name of the Configuration.
            returned: on success
            type: str
            sample: display_name_example
        shape_name:
            description:
                - The name of the associated Shape.
            returned: on success
            type: str
            sample: shape_name_example
        type:
            description:
                - The Configuration type, DEFAULT or CUSTOM.
            returned: on success
            type: str
            sample: DEFAULT
        time_created:
            description:
                - The date and time the Configuration was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the Configuration was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Configuration.
            returned: on success
            type: str
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
                    type: str
                    sample: NO_CHAIN
                default_authentication_plugin:
                    description:
                        - "(\\"default_authentication_plugin\\")"
                    returned: on success
                    type: str
                    sample: mysql_native_password
                transaction_isolation:
                    description:
                        - "(\\"transaction_isolation\\")"
                    returned: on success
                    type: str
                    sample: READ-UNCOMMITTED
                innodb_ft_server_stopword_table:
                    description:
                        - "(\\"innodb_ft_server_stopword_table\\")"
                    returned: on success
                    type: str
                    sample: innodb_ft_server_stopword_table_example
                mandatory_roles:
                    description:
                        - "(\\"mandatory_roles\\")"
                    returned: on success
                    type: str
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
                group_replication_consistency:
                    description:
                        - "- EVENTUAL:
                              Both RO and RW transactions do not wait for preceding transactions to be applied before executing.
                              A RW transaction does not wait for other members to apply a transaction. This means that a transaction
                              could be externalized on one member before the others. This also means that in the event of a primary failover,
                              the new primary can accept new RO and RW transactions before the previous primary transactions are all applied.
                              RO transactions could result in outdated values, RW transactions could result in a rollback due to conflicts.
                          - BEFORE_ON_PRIMARY_FAILOVER:
                              New RO or RW transactions with a newly elected primary that is applying backlog from the old
                              primary are held (not applied) until any backlog has been applied. This ensures that when a primary failover happens,
                              intentionally or not, clients always see the latest value on the primary. This guarantees consistency, but means that
                              clients must be able to handle the delay in the event that a backlog is being applied. Usually this delay should be minimal,
                              but does depend on the size of the backlog.
                          - BEFORE:
                              A RW transaction waits for all preceding transactions to complete before being applied. A RO transaction waits for all preceding
                              transactions to complete before being executed. This ensures that this transaction reads the latest value by only affecting the
                              latency of the transaction. This reduces the overhead of synchronization on every RW transaction, by ensuring synchronization is
                              used only on RO transactions. This consistency level also includes the consistency guarantees provided by
                              BEFORE_ON_PRIMARY_FAILOVER.
                          - AFTER:
                              A RW transaction waits until its changes have been applied to all of the other members. This value has no effect on RO
                              transactions.
                              This mode ensures that when a transaction is committed on the local member, any subsequent transaction reads the written value or
                              a more recent value on any group member. Use this mode with a group that is used for predominantly RO operations to ensure that
                              applied RW transactions are applied everywhere once they commit. This could be used by your application to ensure that subsequent
                              reads fetch the latest data which includes the latest writes. This reduces the overhead of synchronization on every RO
                              transaction,
                              by ensuring synchronization is used only on RW transactions. This consistency level also includes the consistency guarantees
                              provided by BEFORE_ON_PRIMARY_FAILOVER.
                          - BEFORE_AND_AFTER:
                              A RW transaction waits for 1) all preceding transactions to complete before being applied and 2) until its changes have been
                              applied on other members. A RO transaction waits for all preceding transactions to complete before execution takes place.
                              This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER."
                    returned: on success
                    type: str
                    sample: EVENTUAL
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
                        - Sets the binary log expiration period in seconds.
                          binlogExpireLogsSeconds corresponds to the MySQL binary logging system variable
                          L(binlog_expire_logs_seconds,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-
                          log.html#sysvar_binlog_expire_logs_seconds).
                    returned: on success
                    type: int
                    sample: 56
                binlog_row_metadata:
                    description:
                        - Configures the amount of table metadata added to the binary log when using row-based logging.
                          binlogRowMetadata corresponds to the MySQL binary logging system variable
                          L(binlog_row_metadata,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_metadata).
                    returned: on success
                    type: str
                    sample: FULL
                binlog_row_value_options:
                    description:
                        - When set to PARTIAL_JSON, this enables use of a space-efficient binary log format for updates that modify only a small portion of a
                          JSON document.
                          binlogRowValueOptions corresponds to the MySQL binary logging system variable
                          L(binlog_row_value_options,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-
                          log.html#sysvar_binlog_row_value_options).
                    returned: on success
                    type: str
                    sample: binlog_row_value_options_example
                binlog_transaction_compression:
                    description:
                        - Enables compression for transactions that are written to binary log files on this server.
                          binlogTransactionCompression corresponds to the MySQL binary logging system variable
                          L(binlog_transaction_compression,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-
                          log.html#sysvar_binlog_transaction_compression).
                    returned: on success
                    type: bool
                    sample: true
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
                    type: str
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
            type: str
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
    sample: {
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
            "group_replication_consistency": "EVENTUAL",
            "innodb_ft_enable_stopword": true,
            "local_infile": true,
            "mysql_firewall_mode": true,
            "mysqlx_enable_hello_notice": true,
            "sql_require_primary_key": true,
            "sql_warnings": true,
            "binlog_expire_logs_seconds": 56,
            "binlog_row_metadata": "FULL",
            "binlog_row_value_options": "binlog_row_value_options_example",
            "binlog_transaction_compression": true,
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import WorkRequestsClient
    from oci.mysql import MysqlaasClient
    from oci.mysql.models import CreateConfigurationDetails
    from oci.mysql.models import UpdateConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["configuration_id", "display_name", "shape_name"]

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

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_configuration_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
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


MysqlConfigurationHelperCustom = get_custom_class("MysqlConfigurationHelperCustom")


class ResourceHelper(MysqlConfigurationHelperCustom, MysqlConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            shape_name=dict(type="str"),
            variables=dict(
                type="dict",
                options=dict(
                    completion_type=dict(
                        type="str", choices=["NO_CHAIN", "CHAIN", "RELEASE"]
                    ),
                    default_authentication_plugin=dict(
                        type="str",
                        choices=[
                            "mysql_native_password",
                            "sha256_password",
                            "caching_sha2_password",
                        ],
                    ),
                    transaction_isolation=dict(
                        type="str",
                        choices=[
                            "READ-UNCOMMITTED",
                            "READ-COMMITED",
                            "READ-COMMITTED",
                            "REPEATABLE-READ",
                            "SERIALIZABLE",
                        ],
                    ),
                    innodb_ft_server_stopword_table=dict(type="str"),
                    mandatory_roles=dict(type="str"),
                    autocommit=dict(type="bool"),
                    foreign_key_checks=dict(type="bool", no_log=True),
                    group_replication_consistency=dict(
                        type="str",
                        choices=[
                            "EVENTUAL",
                            "BEFORE_ON_PRIMARY_FAILOVER",
                            "BEFORE",
                            "AFTER",
                            "BEFORE_AND_AFTER",
                        ],
                    ),
                    innodb_ft_enable_stopword=dict(type="bool"),
                    local_infile=dict(type="bool"),
                    mysql_firewall_mode=dict(type="bool"),
                    mysqlx_enable_hello_notice=dict(type="bool"),
                    sql_require_primary_key=dict(type="bool", no_log=True),
                    sql_warnings=dict(type="bool"),
                    binlog_expire_logs_seconds=dict(type="int"),
                    binlog_row_metadata=dict(type="str", choices=["FULL", "MINIMAL"]),
                    binlog_row_value_options=dict(type="str"),
                    binlog_transaction_compression=dict(type="bool"),
                    innodb_buffer_pool_size=dict(type="int"),
                    innodb_ft_result_cache_limit=dict(type="int"),
                    max_connections=dict(type="int"),
                    max_prepared_stmt_count=dict(type="int"),
                    connect_timeout=dict(type="int"),
                    cte_max_recursion_depth=dict(type="int"),
                    generated_random_password_length=dict(type="int", no_log=True),
                    information_schema_stats_expiry=dict(type="int"),
                    innodb_buffer_pool_instances=dict(type="int"),
                    innodb_ft_max_token_size=dict(type="int", no_log=True),
                    innodb_ft_min_token_size=dict(type="int", no_log=True),
                    innodb_ft_num_word_optimize=dict(type="int"),
                    innodb_lock_wait_timeout=dict(type="int"),
                    innodb_max_purge_lag=dict(type="int"),
                    innodb_max_purge_lag_delay=dict(type="int"),
                    max_execution_time=dict(type="int"),
                    mysqlx_connect_timeout=dict(type="int"),
                    mysqlx_document_id_unique_prefix=dict(type="int"),
                    mysqlx_idle_worker_thread_timeout=dict(type="int"),
                    mysqlx_interactive_timeout=dict(type="int"),
                    mysqlx_max_allowed_packet=dict(type="int"),
                    mysqlx_min_worker_threads=dict(type="int"),
                    mysqlx_read_timeout=dict(type="int"),
                    mysqlx_wait_timeout=dict(type="int"),
                    mysqlx_write_timeout=dict(type="int"),
                    parser_max_mem_size=dict(type="int"),
                    query_alloc_block_size=dict(type="int"),
                    query_prealloc_size=dict(type="int"),
                    sql_mode=dict(type="str"),
                    mysqlx_deflate_default_compression_level=dict(type="int"),
                    mysqlx_deflate_max_client_compression_level=dict(type="int"),
                    mysqlx_lz4_max_client_compression_level=dict(type="int"),
                    mysqlx_lz4_default_compression_level=dict(type="int"),
                    mysqlx_zstd_max_client_compression_level=dict(type="int"),
                    mysqlx_zstd_default_compression_level=dict(type="int"),
                    mysql_zstd_default_compression_level=dict(type="int"),
                ),
            ),
            parent_configuration_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration",
        service_client_class=MysqlaasClient,
        namespace="mysql",
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
