#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple configurations.
        type: str
    configuration_id:
        description:
            - The OCID of the Configuration.
            - Required to get a specific configuration.
        type: str
        aliases: ["id"]
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
        elements: str
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
- name: Get a specific configuration
  oci_mysql_configuration_facts:
    # required
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List configurations
  oci_mysql_configuration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    type: [ "DEFAULT" ]
    display_name: display_name_example
    shape_name: shape_name_example
    sort_by: displayName
    sort_order: ASC

"""

RETURN = """
configurations:
    description:
        - List of Configuration resources
    returned: on success
    type: complex
    contains:
        init_variables:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                lower_case_table_names:
                    description:
                        - Represents the MySQL server system variable lower_case_table_names (https://dev.mysql.com/doc/refman/8.0/en/server-system-
                          variables.html#sysvar_lower_case_table_names).
                        - lowerCaseTableNames controls case-sensitivity of tables and schema names and how they are stored in the DB System.
                        - "Valid values are:
                            - CASE_SENSITIVE - (default) Table and schema name comparisons are case-sensitive and stored as specified.
                              (lower_case_table_names=0)
                            - CASE_INSENSITIVE_LOWERCASE - Table and schema name comparisons are not case-sensitive and stored in lowercase.
                              (lower_case_table_names=1)"
                    returned: on success
                    type: str
                    sample: CASE_SENSITIVE
        variables:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                completion_type:
                    description:
                        - "(\\"completion_type\\")"
                    returned: on success
                    type: str
                    sample: NO_CHAIN
                big_tables:
                    description:
                        - If enabled, the server stores all temporary tables on disk rather than in memory.
                        - bigTables corresponds to the MySQL server variable L(big_tables,https://dev.mysql.com/doc/refman/en/server-system-
                          variables.html#sysvar_big_tables).
                    returned: on success
                    type: bool
                    sample: true
                connection_memory_chunk_size:
                    description:
                        - Set the chunking size for updates to the global memory usage counter Global_connection_memory.
                        - connectionMemoryChunkSize corresponds to the MySQL system variable
                          L(connection_memory_chunk_size,https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_chunk_size).
                    returned: on success
                    type: int
                    sample: 56
                connection_memory_limit:
                    description:
                        - Set the maximum amount of memory that can be used by a single user connection.
                        - connectionMemoryLimit corresponds to the MySQL system variable L(connection_memory_limit,https://dev.mysql.com/doc/refman/en/server-
                          system-variables.html#sysvar_connection_memory_limit).
                    returned: on success
                    type: int
                    sample: 56
                default_authentication_plugin:
                    description:
                        - "(\\"default_authentication_plugin\\")"
                    returned: on success
                    type: str
                    sample: mysql_native_password
                global_connection_memory_limit:
                    description:
                        - Set the total amount of memory that can be used by all user connections.
                        - globalConnectionMemoryLimit corresponds to the MySQL system variable
                          L(global_connection_memory_limit,https://dev.mysql.com/doc/refman/en/server-system-
                          variables.html#sysvar_global_connection_memory_limit).
                    returned: on success
                    type: int
                    sample: 56
                global_connection_memory_tracking:
                    description:
                        - Determines whether the MySQL server calculates Global_connection_memory.
                        - globalConnectionMemoryTracking corresponds to the MySQL system variable
                          L(global_connection_memory_tracking,https://dev.mysql.com/doc/refman/en/server-system-
                          variables.html#sysvar_global_connection_memory_tracking).
                    returned: on success
                    type: bool
                    sample: true
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
                innodb_log_writer_threads:
                    description:
                        - Enables dedicated log writer threads for writing redo log records from the log buffer to the system buffers and flushing the system
                          buffers to the redo log files.
                        - "This is the MySQL variable \\"innodb_log_writer_threads\\". For more information, please see the L(MySQL
                          documentation,https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_writer_threads)"
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
                        - The size (in bytes) of the buffer pool, that is, the memory area where InnoDB caches table and index data.
                        - innodbBufferPoolSize corresponds to the MySQL server system variable
                          L(innodb_buffer_pool_size,https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size).
                        - The default and maximum values depend on the amount of RAM provisioned by the shape.
                          See L(Default User Variables,https://docs.cloud.oracle.com/mysql-database/doc/configuring-db-
                          system.html#GUID-B5504C19-F6F4-4DAB-8506-189A4E8F4A6A).
                    returned: on success
                    type: int
                    sample: 56
                innodb_ft_result_cache_limit:
                    description:
                        - "(\\"innodb_ft_result_cache_limit\\")"
                    returned: on success
                    type: int
                    sample: 56
                max_binlog_cache_size:
                    description:
                        - Sets the size of the transaction cache.
                        - maxBinlogCacheSize corresponds to the MySQL server system variable
                          L(max_binlog_cache_size,https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_max_binlog_cache_size).
                    returned: on success
                    type: int
                    sample: 56
                max_connect_errors:
                    description:
                        - "(\\"max_connect_errors\\")"
                    returned: on success
                    type: int
                    sample: 56
                max_heap_table_size:
                    description:
                        - This variable sets the maximum size to which user-created MEMORY tables are permitted to grow.
                        - maxHeapTableSize corresponds to the MySQL system variable
                          L(max_heap_table_size,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_heap_table_size)
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
                        - The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake.
                        - connectTimeout corresponds to the MySQL system variable
                          L(connect_timeout,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_connect_timeout)
                        - "Increasing the connect_timeout value might help if clients frequently encounter errors of the form
                          \\"Lost connection to MySQL server at 'XXX', system error: errno\\"."
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
                innodb_buffer_pool_dump_pct:
                    description:
                        - Specifies the percentage of the most recently used pages for each buffer pool to read out and dump.
                        - innodbBufferPoolDumpPct corresponds to the MySQL InnoDB system variable
                          L(innodb_buffer_pool_dump_pct,https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_dump_pct).
                        - The range is 1 to 100. The default value is 25.
                        - For example, if there are 4 buffer pools with 100 pages each, and innodb_buffer_pool_dump_pct is set to 25,
                          the 25 most recently used pages from each buffer pool are dumped.
                    returned: on success
                    type: int
                    sample: 56
                innodb_buffer_pool_instances:
                    description:
                        - "(\\"innodb_buffer_pool_instances\\")"
                    returned: on success
                    type: int
                    sample: 56
                innodb_ddl_buffer_size:
                    description:
                        - innodbDdlBufferSize corresponds to the MySQL system variable L(innodb_ddl_buffer_size],https://dev.mysql.com/doc/refman/8.0/en/innodb-
                          parameters.html#sysvar_innodb_ddl_buffer_size)
                    returned: on success
                    type: int
                    sample: 56
                innodb_ddl_threads:
                    description:
                        - innodbDdlThreads corresponds to the MySQL system variable L(innodb_ddl_threads],https://dev.mysql.com/doc/refman/8.0/en/innodb-
                          parameters.html#sysvar_innodb_ddl_threads)
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
                        - The desired maximum purge lag in terms of transactions.
                        - InnoDB maintains a list of transactions that have index records delete-marked by UPDATE or DELETE operations. The length of the list
                          is the purge lag.
                        - If this value is exceeded, a delay is imposed on INSERT, UPDATE, and DELETE operations to allow time for purge to catch up.
                        - The default value is 0, which means there is no maximum purge lag and no delay.
                        - innodbMaxPurgeLag corresponds to the MySQL server system variable
                          L(innodb_max_purge_lag,https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag).
                    returned: on success
                    type: int
                    sample: 56
                innodb_max_purge_lag_delay:
                    description:
                        - The maximum delay in microseconds for the delay imposed when the innodb_max_purge_lag threshold is exceeded.
                        - The specified innodb_max_purge_lag_delay value is an upper limit on the delay period.
                        - innodbMaxPurgeLagDelay corresponds to the MySQL server system variable
                          L(innodb_max_purge_lag_delay,https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag_delay).
                    returned: on success
                    type: int
                    sample: 56
                interactive_timeout:
                    description:
                        - The number of seconds the server waits for activity on an interactive connection before closing it.
                        - interactiveTimeout corresponds to the MySQL system variable.
                          L(interactive_timeout,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_interactive_timeout)
                    returned: on success
                    type: int
                    sample: 56
                innodb_stats_persistent_sample_pages:
                    description:
                        - The number of index pages to sample when estimating cardinality and other statistics for an indexed column,
                          such as those calculated by ANALYZE TABLE.
                        - innodbStatsPersistentSamplePages corresponds to the MySQL InnoDB system variable
                          L(innodb_stats_persistent_sample_pages,https://dev.mysql.com/doc/refman/8.0/en/innodb-
                          parameters.html#sysvar_innodb_stats_persistent_sample_pages)
                        - innodb_stats_persistent_sample_pages only applies when innodb_stats_persistent is enabled for a table;
                          when innodb_stats_persistent is disabled, innodb_stats_transient_sample_pages applies instead.
                    returned: on success
                    type: int
                    sample: 56
                innodb_stats_transient_sample_pages:
                    description:
                        - The number of index pages to sample when estimating cardinality and other statistics for an indexed column,
                          such as those calculated by L(ANALYZE TABLE,https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html).
                        - innodbStatsTransientSamplePages corresponds to the MySQL InnoDB system variable
                          L(innodb_stats_transient_sample_pages,https://dev.mysql.com/doc/refman/8.0/en/innodb-
                          parameters.html#sysvar_innodb_stats_transient_sample_pages)
                        - innodb_stats_transient_sample_pages only applies when innodb_stats_persistent is disabled for a table;
                          when innodb_stats_persistent is enabled, innodb_stats_persistent_sample_pages applies instead.
                        - innodb_stats_persistent is ON by default and cannot be changed. It is possible to override it using the
                          STATS_PERSISTENT clause of the L(CREATE TABLE,https://dev.mysql.com/doc/refman/8.0/en/create-table.html) and
                          L(ALTER TABLE,https://dev.mysql.com/doc/refman/8.0/en/alter-table.html) statements.
                    returned: on success
                    type: int
                    sample: 56
                max_allowed_packet:
                    description:
                        - The maximum size of one packet or any generated/intermediate string.
                        - "This is the mysql variable \\"max_allowed_packet\\"."
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
                        - The number of seconds X Plugin waits for the first packet to be received from newly connected clients.
                        - mysqlxConnectTimeout corresponds to the MySQL X Plugin system variable
                          L(mysqlx_connect_timeout,https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_connect_timeout)
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
                        - The number of seconds to wait for interactive clients to timeout.
                        - mysqlxInteractiveTimeout corresponds to the MySQL X Plugin system variable.
                          L(mysqlx_interactive_timeout,https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-
                          variables.html#sysvar_mysqlx_interactive_timeout)
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_max_allowed_packet:
                    description:
                        - The maximum size of network packets that can be received by X Plugin.
                        - "This is the mysql variable \\"mysqlx_max_allowed_packet\\"."
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
                        - The number of seconds that X Plugin waits for blocking read operations to complete. After this time, if the
                          read operation is not successful, X Plugin closes the connection and returns a warning notice with the error
                          code ER_IO_READ_ERROR to the client application.
                        - mysqlxReadTimeout corresponds to the MySQL X Plugin system variable
                          L(mysqlx_read_timeout,https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_read_timeout)
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_wait_timeout:
                    description:
                        - The number of seconds that X Plugin waits for activity on a connection.
                        - mysqlxWaitTimeout corresponds to the MySQL X Plugin system variable.
                          L(mysqlx_wait_timeout,https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_wait_timeout)
                    returned: on success
                    type: int
                    sample: 56
                mysqlx_write_timeout:
                    description:
                        - The number of seconds that X Plugin waits for blocking write operations to complete. After this time, if the
                          write operation is not successful, X Plugin closes the connection.
                        - mysqlxReadmysqlxWriteTimeoutTimeout corresponds to the MySQL X Plugin system variable
                          L(mysqlx_write_timeout,https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_write_timeout)
                    returned: on success
                    type: int
                    sample: 56
                net_read_timeout:
                    description:
                        - The number of seconds to wait for more data from a connection before aborting the read.
                        - netReadTimeout corresponds to the MySQL system variable
                          L(net_read_timeout,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_read_timeout)
                    returned: on success
                    type: int
                    sample: 56
                net_write_timeout:
                    description:
                        - The number of seconds to wait for a block to be written to a connection before aborting the write.
                        - netWriteTimeout corresponds to the MySQL system variable
                          L(net_write_timeout,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_write_timeout)
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
                regexp_time_limit:
                    description:
                        - regexpTimeLimit corresponds to the MySQL system variable L(regexp_time_limit],https://dev.mysql.com/doc/refman/8.0/en/server-system-
                          variables.html#sysvar_regexp_time_limit)
                    returned: on success
                    type: int
                    sample: 56
                sql_mode:
                    description:
                        - "(\\"sql_mode\\")"
                    returned: on success
                    type: str
                    sample: sql_mode_example
                tmp_table_size:
                    description:
                        - The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.
                        - tmp_table_size corresponds to the MySQL system variable
                          L(tmp_table_size,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size)
                    returned: on success
                    type: int
                    sample: 56
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
                sort_buffer_size:
                    description:
                        - Each session that must perform a sort allocates a buffer of this size.
                        - sortBufferSize corresponds to the MySQL system variable L(sort_buffer_size,https://dev.mysql.com/doc/refman/en/server-system-
                          variables.html#sysvar_sort_buffer_size)
                    returned: on success
                    type: int
                    sample: 56
                wait_timeout:
                    description:
                        - The number of seconds the server waits for activity on a noninteractive connection before closing it.
                        - waitTimeout corresponds to the MySQL system variable.
                          L(wait_timeout,https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout)
                    returned: on success
                    type: int
                    sample: 56
                thread_pool_dedicated_listeners:
                    description:
                        - Controls whether the thread pool uses dedicated listener threads. If enabled, a listener thread in each thread group is dedicated to
                          the task of listening
                          for network events from clients, ensuring that the maximum number of query worker threads is no more than the value specified by
                          threadPoolMaxTransactionsLimit.
                          threadPoolDedicatedListeners corresponds to the MySQL Database Service-specific system variable thread_pool_dedicated_listeners.
                    returned: on success
                    type: bool
                    sample: true
                thread_pool_max_transactions_limit:
                    description:
                        - Limits the maximum number of open transactions to the defined value. The default value is 0, which enforces no limit.
                          threadPoolMaxTransactionsLimit corresponds to the MySQL Database Service-specific system variable thread_pool_max_transactions_limit.
                    returned: on success
                    type: int
                    sample: 56
                time_zone:
                    description:
                        - Initializes the time zone for each client that connects.
                        - "This corresponds to the MySQL System Variable \\"time_zone\\"."
                        - "The values can be given in one of the following formats, none of which are case-sensitive:"
                        - "- As a string indicating an offset from UTC of the form [H]H:MM, prefixed with a + or -, such as '+10:00', '-6:00', or '+05:30'. The
                          permitted range is '-13:59' to '+14:00', inclusive.
                          - As a named time zone, as defined by the \\"IANA Time Zone database\\", such as 'Europe/Helsinki', 'US/Eastern', 'MET', or 'UTC'."
                    returned: on success
                    type: str
                    sample: time_zone_example
        parent_configuration_id:
            description:
                - "The OCID of the Configuration from which this Configuration is
                  \\"derived\\". This is entirely a metadata relationship. There is no
                  relation between the values in this Configuration and its parent."
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.parentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
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
        lifecycle_state:
            description:
                - The current state of the Configuration.
            returned: on success
            type: str
            sample: ACTIVE
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
        "init_variables": {
            "lower_case_table_names": "CASE_SENSITIVE"
        },
        "variables": {
            "completion_type": "NO_CHAIN",
            "big_tables": true,
            "connection_memory_chunk_size": 56,
            "connection_memory_limit": 56,
            "default_authentication_plugin": "mysql_native_password",
            "global_connection_memory_limit": 56,
            "global_connection_memory_tracking": true,
            "transaction_isolation": "READ-UNCOMMITTED",
            "innodb_ft_server_stopword_table": "innodb_ft_server_stopword_table_example",
            "mandatory_roles": "mandatory_roles_example",
            "autocommit": true,
            "foreign_key_checks": true,
            "group_replication_consistency": "EVENTUAL",
            "innodb_ft_enable_stopword": true,
            "innodb_log_writer_threads": true,
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
            "max_binlog_cache_size": 56,
            "max_connect_errors": 56,
            "max_heap_table_size": 56,
            "max_connections": 56,
            "max_prepared_stmt_count": 56,
            "connect_timeout": 56,
            "cte_max_recursion_depth": 56,
            "generated_random_password_length": 56,
            "information_schema_stats_expiry": 56,
            "innodb_buffer_pool_dump_pct": 56,
            "innodb_buffer_pool_instances": 56,
            "innodb_ddl_buffer_size": 56,
            "innodb_ddl_threads": 56,
            "innodb_ft_max_token_size": 56,
            "innodb_ft_min_token_size": 56,
            "innodb_ft_num_word_optimize": 56,
            "innodb_lock_wait_timeout": 56,
            "innodb_max_purge_lag": 56,
            "innodb_max_purge_lag_delay": 56,
            "interactive_timeout": 56,
            "innodb_stats_persistent_sample_pages": 56,
            "innodb_stats_transient_sample_pages": 56,
            "max_allowed_packet": 56,
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
            "net_read_timeout": 56,
            "net_write_timeout": 56,
            "parser_max_mem_size": 56,
            "query_alloc_block_size": 56,
            "query_prealloc_size": 56,
            "regexp_time_limit": 56,
            "sql_mode": "sql_mode_example",
            "tmp_table_size": 56,
            "mysqlx_deflate_default_compression_level": 56,
            "mysqlx_deflate_max_client_compression_level": 56,
            "mysqlx_lz4_max_client_compression_level": 56,
            "mysqlx_lz4_default_compression_level": 56,
            "mysqlx_zstd_max_client_compression_level": 56,
            "mysqlx_zstd_default_compression_level": 56,
            "mysql_zstd_default_compression_level": 56,
            "sort_buffer_size": 56,
            "wait_timeout": 56,
            "thread_pool_dedicated_listeners": true,
            "thread_pool_max_transactions_limit": 56,
            "time_zone": "time_zone_example"
        },
        "parent_configuration_id": "ocid1.parentconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "shape_name": "shape_name_example",
        "type": "DEFAULT",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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
            compartment_id=dict(type="str"),
            configuration_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            type=dict(type="list", elements="str", choices=["DEFAULT", "CUSTOM"]),
            display_name=dict(aliases=["name"], type="str"),
            shape_name=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=["displayName", "shapeName", "timeCreated", "timeUpdated"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

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
