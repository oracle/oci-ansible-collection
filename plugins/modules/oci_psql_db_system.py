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
module: oci_psql_db_system
short_description: Manage a DbSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update, patch and delete a DbSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new database system.
    - "This resource has the following action operations in the M(oracle.oci.oci_psql_db_system_actions) module: change_compartment, failover,
      reset_master_user_password, restart_db_instance_in, restore."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the database system.
            - Required for create using I(state=present).
        type: str
    system_type:
        description:
            - Type of the database system.
        type: str
    db_version:
        description:
            - Version of database system software.
            - Required for create using I(state=present).
        type: str
    config_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration associated with the database system.
        type: str
    shape:
        description:
            - "The name of the shape for the database instance node. Use the /shapes API for accepted shapes.
              Example: `VM.Standard.E4.Flex`"
            - Required for create using I(state=present).
        type: str
    instance_ocpu_count:
        description:
            - The total number of OCPUs available to each database instance node.
        type: int
    instance_memory_size_in_gbs:
        description:
            - The total amount of memory available to each database instance node, in gigabytes.
        type: int
    instance_count:
        description:
            - Count of database instances nodes to be created in the database system.
        type: int
    instances_details:
        description:
            - Details of database instances nodes to be created. This parameter is optional.
              If specified, its size must match `instanceCount`.
        type: list
        elements: dict
        suboptions:
            display_name:
                description:
                    - Display name of the database instance node. Avoid entering confidential information.
                type: str
                aliases: ["name"]
            description:
                description:
                    - A user-provided description of the database instance node.
                type: str
            private_ip:
                description:
                    - Private IP in customer subnet that will be assigned to the database instance node. This value is optional.
                      If the IP is not provided, the IP will be chosen from the available IP addresses in the specified subnet.
                type: str
    credentials:
        description:
            - ""
        type: dict
        suboptions:
            username:
                description:
                    - The database system administrator username.
                type: str
                required: true
            password_details:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    password:
                        description:
                            - The database system password.
                            - Required when password_type is 'PLAIN_TEXT'
                        type: str
                    password_type:
                        description:
                            - The password type.
                        type: str
                        choices:
                            - "PLAIN_TEXT"
                            - "VAULT_SECRET"
                        required: true
                    secret_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret where the password is stored.
                            - Required when password_type is 'VAULT_SECRET'
                        type: str
                    secret_version:
                        description:
                            - The secret version of the stored password.
                            - Required when password_type is 'VAULT_SECRET'
                        type: str
    network_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer subnet associated with the database
                      system.
                type: str
                required: true
            primary_db_endpoint_private_ip:
                description:
                    - Private IP in customer subnet. The value is optional.
                      If the IP is not provided, the IP will be chosen from the available IP addresses from the specified subnet.
                type: str
            nsg_ids:
                description:
                    - List of customer Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with
                      the database system.
                type: list
                elements: str
    source:
        description:
            - ""
        type: dict
        suboptions:
            backup_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system backup.
                    - Required when source_type is 'BACKUP'
                type: str
            is_having_restore_config_overrides:
                description:
                    - Deprecated. Don't use.
                    - Applicable when source_type is 'BACKUP'
                type: bool
            source_type:
                description:
                    - The source descriminator.
                type: str
                choices:
                    - "BACKUP"
                    - "NONE"
                required: true
    display_name:
        description:
            - A user-friendly display name for the database system. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A user-provided description of a database system.
            - This parameter is updatable.
        type: str
    db_configuration_params:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            apply_config:
                description:
                    - Whether a configuration update requires a restart of the database instance or a reload of the configuration.
                      Some configuration changes require a restart of database instances to be applied.
                    - This parameter is updatable.
                type: str
                choices:
                    - "RESTART"
                    - "RELOAD"
            config_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration.
                    - This parameter is updatable.
                type: str
                required: true
    management_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            maintenance_window_start:
                description:
                    - The start of the maintenance window.
                type: str
            backup_policy:
                description:
                    - ""
                type: dict
                suboptions:
                    days_of_the_week:
                        description:
                            - The day of the week that the backup starts.
                            - Required when kind is 'WEEKLY'
                        type: list
                        elements: str
                        choices:
                            - "SUNDAY"
                            - "MONDAY"
                            - "TUESDAY"
                            - "WEDNESDAY"
                            - "THURSDAY"
                            - "FRIDAY"
                            - "SATURDAY"
                    kind:
                        description:
                            - The kind of backup policy.
                        type: str
                        choices:
                            - "DAILY"
                            - "WEEKLY"
                            - "NONE"
                            - "MONTHLY"
                        required: true
                    retention_days:
                        description:
                            - How many days the data should be stored after the database system deletion.
                        type: int
                    backup_start:
                        description:
                            - Hour of the day when the backup starts.
                            - Required when kind is one of ['WEEKLY', 'DAILY', 'MONTHLY']
                        type: str
                    days_of_the_month:
                        description:
                            - Day of the month when the backup should start.
                              To ensure that the backup runs monthly, the latest day of the month that you can use to schedule a backup is the the 28th day.
                            - Required when kind is 'MONTHLY'
                        type: list
                        elements: int
    storage_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            system_type:
                description:
                    - Type of the database system.
                type: str
                choices:
                    - "OCI_OPTIMIZED_STORAGE"
            is_regionally_durable:
                description:
                    - Specifies if the block volume used for the database system is regional or AD-local.
                      If not specified, it will be set to false.
                      If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                      If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                type: bool
            availability_domain:
                description:
                    - Specifies the availability domain of AD-local storage.
                      If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                      If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                type: str
            iops:
                description:
                    - Guaranteed input/output storage requests per second (IOPS) available to the database system.
                    - This parameter is updatable.
                type: int
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
    items:
        description:
            - List of patch instructions.
        type: list
        elements: dict
        suboptions:
            _from:
                description:
                    - The selection that is to be moved, with the same format and semantics as `selection`.
                    - Required when operation is 'MOVE'
                type: str
            selected_item:
                description:
                    - A selection to be evaluated against the array for identifying a particular reference item within it, with the same format and semantics as
                      `selection`.
                    - Applicable when operation is 'INSERT'
                type: str
            position:
                description:
                    - "Where to insert the value in an array, relative to the first item in the selection.
                      If there is no such item, then \\"BEFORE\\" specifies insertion at the first position in an array and \\"AFTER\\" specifies insertion at
                      the last position.
                      If the first item in the selection is not the child of an array, then this field has no effect."
                    - Applicable when operation is one of ['MOVE', 'INSERT']
                type: str
                choices:
                    - "AT"
                    - "BEFORE"
                    - "AFTER"
            operation:
                description:
                    - ""
                type: str
                choices:
                    - "MOVE"
                    - "REMOVE"
                    - "REPLACE"
                    - "INSERT"
                    - "REQUIRE"
                    - "MERGE"
                    - "PROHIBIT"
                required: true
            selection:
                description:
                    - The set of values to which the operation applies as a L(JMESPath expression,https://jmespath.org/specification.html) for evaluation
                      against the context resource.
                      An operation fails if the selection yields an exception, except as otherwise specified.
                      Note that comparisons involving non-primitive values (objects or arrays) are not supported and will always evaluate to false.
                type: str
                required: true
            value:
                description:
                    - A value to be added into the target.
                    - Applicable when operation is one of ['MERGE', 'PROHIBIT', 'REQUIRE']
                    - Required when operation is one of ['INSERT', 'REPLACE']
                type: dict
    db_system_id:
        description:
            - A unique identifier for the database system.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DbSystem.
            - Use I(state=present) to create or update a DbSystem.
            - Use I(state=absent) to delete a DbSystem.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create db_system
  oci_psql_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    db_version: db_version_example
    shape: shape_example
    network_details:
      # required
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      primary_db_endpoint_private_ip: primary_db_endpoint_private_ip_example
      nsg_ids: [ "nsg_ids_example" ]
    display_name: display_name_example
    storage_details:
      # required
      system_type: OCI_OPTIMIZED_STORAGE
      is_regionally_durable: true

      # optional
      availability_domain: Uocm:PHX-AD-1
      iops: 56

    # optional
    system_type: system_type_example
    config_id: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"
    instance_ocpu_count: 56
    instance_memory_size_in_gbs: 56
    instance_count: 56
    instances_details:
    - # optional
      display_name: display_name_example
      description: description_example
      private_ip: private_ip_example
    credentials:
      # required
      username: username_example
      password_details:
        # required
        password: example-password
        password_type: PLAIN_TEXT
    source:
      # required
      backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
      source_type: BACKUP

      # optional
      is_having_restore_config_overrides: true
    description: description_example
    management_policy:
      # optional
      maintenance_window_start: maintenance_window_start_example
      backup_policy:
        # required
        kind: DAILY
        backup_start: backup_start_example

        # optional
        retention_days: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update db_system
  oci_psql_db_system:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    db_configuration_params:
      # required
      config_id: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      apply_config: RESTART
    management_policy:
      # optional
      maintenance_window_start: maintenance_window_start_example
      backup_policy:
        # required
        kind: DAILY
        backup_start: backup_start_example

        # optional
        retention_days: 56
    storage_details:
      # required
      system_type: OCI_OPTIMIZED_STORAGE
      is_regionally_durable: true

      # optional
      availability_domain: Uocm:PHX-AD-1
      iops: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_psql_db_system:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    db_configuration_params:
      # required
      config_id: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      apply_config: RESTART
    management_policy:
      # optional
      maintenance_window_start: maintenance_window_start_example
      backup_policy:
        # required
        kind: DAILY
        backup_start: backup_start_example

        # optional
        retention_days: 56
    storage_details:
      # required
      system_type: OCI_OPTIMIZED_STORAGE
      is_regionally_durable: true

      # optional
      availability_domain: Uocm:PHX-AD-1
      iops: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete db_system
  oci_psql_db_system:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_psql_db_system:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
db_system:
    description:
        - Details of the DbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier for the database system. Immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the database system. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A description of the database system.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the database system.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time that the database system was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that the database system was updated, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the database system.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        admin_username:
            description:
                - The database system administrator username.
            returned: on success
            type: str
            sample: admin_username_example
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
        system_type:
            description:
                - Type of the database system.
            returned: on success
            type: str
            sample: OCI_OPTIMIZED_STORAGE
        db_version:
            description:
                - The major and minor versions of the database system software.
            returned: on success
            type: str
            sample: db_version_example
        config_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration associated with the database system.
            returned: on success
            type: str
            sample: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"
        shape:
            description:
                - "The name of the shape for the database instance.
                  Example: `VM.Standard.E4.Flex`"
            returned: on success
            type: str
            sample: shape_example
        instance_ocpu_count:
            description:
                - The total number of OCPUs available to each database instance node.
            returned: on success
            type: int
            sample: 56
        instance_memory_size_in_gbs:
            description:
                - The total amount of memory available to each database instance node, in gigabytes.
            returned: on success
            type: int
            sample: 56
        instance_count:
            description:
                - Count of instances, or nodes, in the database system.
            returned: on success
            type: int
            sample: 56
        instances:
            description:
                - The list of instances, or nodes, in the database system.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - A unique identifier for the database instance node. Immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - A user-friendly display name for the database instance node. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description of the database instance node.
                    returned: on success
                    type: str
                    sample: description_example
                availability_domain:
                    description:
                        - The availability domain in which the database instance node is located.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                lifecycle_state:
                    description:
                        - The current state of the database instance node.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_created:
                    description:
                        - The date and time that the database instance node was created, expressed in
                          L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the database instance node was updated, expressed in
                          L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        storage_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                system_type:
                    description:
                        - Type of the database system.
                    returned: on success
                    type: str
                    sample: OCI_OPTIMIZED_STORAGE
                is_regionally_durable:
                    description:
                        - Specifies if the block volume used for the database system is regional or AD-local.
                          If not specified, it will be set to false.
                          If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                          If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                    returned: on success
                    type: bool
                    sample: true
                availability_domain:
                    description:
                        - Specifies the availability domain of AD-local storage.
                          If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                          If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                iops:
                    description:
                        - Guaranteed input/output storage requests per second (IOPS) available to the database system.
                    returned: on success
                    type: int
                    sample: 56
        network_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer subnet associated with the database
                          system.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                primary_db_endpoint_private_ip:
                    description:
                        - Private IP in customer subnet. The value is optional.
                          If the IP is not provided, the IP will be chosen from the available IP addresses from the specified subnet.
                    returned: on success
                    type: str
                    sample: primary_db_endpoint_private_ip_example
                nsg_ids:
                    description:
                        - List of customer Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated
                          with the database system.
                    returned: on success
                    type: list
                    sample: []
        management_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                maintenance_window_start:
                    description:
                        - The start of the maintenance window.
                    returned: on success
                    type: str
                    sample: maintenance_window_start_example
                backup_policy:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        days_of_the_month:
                            description:
                                - Day of the month when the backup should start.
                                  To ensure that the backup runs monthly, the latest day of the month that you can use to schedule a backup is the the 28th day.
                            returned: on success
                            type: list
                            sample: []
                        kind:
                            description:
                                - The kind of backup policy.
                            returned: on success
                            type: str
                            sample: DAILY
                        retention_days:
                            description:
                                - How many days the data should be stored after the database system deletion.
                            returned: on success
                            type: int
                            sample: 56
                        days_of_the_week:
                            description:
                                - The day of the week that the backup starts.
                            returned: on success
                            type: list
                            sample: []
                        backup_start:
                            description:
                                - Hour of the day when the backup starts.
                            returned: on success
                            type: str
                            sample: backup_start_example
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system backup.
                    returned: on success
                    type: str
                    sample: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
                is_having_restore_config_overrides:
                    description:
                        - Deprecated. Don't use.
                    returned: on success
                    type: bool
                    sample: true
                source_type:
                    description:
                        - The source descriminator.
                    returned: on success
                    type: str
                    sample: BACKUP
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "admin_username": "admin_username_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "system_type": "OCI_OPTIMIZED_STORAGE",
        "db_version": "db_version_example",
        "config_id": "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "instance_ocpu_count": 56,
        "instance_memory_size_in_gbs": 56,
        "instance_count": 56,
        "instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "storage_details": {
            "system_type": "OCI_OPTIMIZED_STORAGE",
            "is_regionally_durable": true,
            "availability_domain": "Uocm:PHX-AD-1",
            "iops": 56
        },
        "network_details": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "primary_db_endpoint_private_ip": "primary_db_endpoint_private_ip_example",
            "nsg_ids": []
        },
        "management_policy": {
            "maintenance_window_start": "maintenance_window_start_example",
            "backup_policy": {
                "days_of_the_month": [],
                "kind": "DAILY",
                "retention_days": 56,
                "days_of_the_week": [],
                "backup_start": "backup_start_example"
            }
        },
        "source": {
            "backup_id": "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx",
            "is_having_restore_config_overrides": true,
            "source_type": "BACKUP"
        }
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
    from oci.psql.models import CreateDbSystemDetails
    from oci.psql.models import UpdateDbSystemDetails
    from oci.psql.models import PatchDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlDbSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, patch, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PsqlDbSystemHelperGen, self).get_possible_entity_types() + [
            "dbsystem",
            "dbsystems",
            "psqldbsystem",
            "psqldbsystems",
            "dbsystemresource",
            "dbsystemsresource",
            "psql",
        ]

    def get_module_resource_id_param(self):
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_db_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_db_systems, **kwargs
        )

    def get_create_model_class(self):
        return CreateDbSystemDetails

    def get_exclude_attributes(self):
        return ["instances_details", "credentials"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(create_db_system_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDbSystemDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                update_db_system_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_patch_model_class(self):
        return PatchDbSystemDetails

    def patch_resource(self):
        patch_details = self.get_patch_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.patch_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                patch_db_system_details=patch_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.PATCH_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PsqlDbSystemHelperCustom = get_custom_class("PsqlDbSystemHelperCustom")


class ResourceHelper(PsqlDbSystemHelperCustom, PsqlDbSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            system_type=dict(type="str"),
            db_version=dict(type="str"),
            config_id=dict(type="str"),
            shape=dict(type="str"),
            instance_ocpu_count=dict(type="int"),
            instance_memory_size_in_gbs=dict(type="int"),
            instance_count=dict(type="int"),
            instances_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    description=dict(type="str"),
                    private_ip=dict(type="str"),
                ),
            ),
            credentials=dict(
                type="dict",
                options=dict(
                    username=dict(type="str", required=True),
                    password_details=dict(
                        type="dict",
                        required=True,
                        no_log=False,
                        options=dict(
                            password=dict(type="str", no_log=True),
                            password_type=dict(
                                type="str",
                                required=True,
                                choices=["PLAIN_TEXT", "VAULT_SECRET"],
                            ),
                            secret_id=dict(type="str"),
                            secret_version=dict(type="str", no_log=True),
                        ),
                    ),
                ),
            ),
            network_details=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str", required=True),
                    primary_db_endpoint_private_ip=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                ),
            ),
            source=dict(
                type="dict",
                options=dict(
                    backup_id=dict(type="str"),
                    is_having_restore_config_overrides=dict(type="bool"),
                    source_type=dict(
                        type="str", required=True, choices=["BACKUP", "NONE"]
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            db_configuration_params=dict(
                type="dict",
                options=dict(
                    apply_config=dict(type="str", choices=["RESTART", "RELOAD"]),
                    config_id=dict(type="str", required=True),
                ),
            ),
            management_policy=dict(
                type="dict",
                options=dict(
                    maintenance_window_start=dict(type="str"),
                    backup_policy=dict(
                        type="dict",
                        options=dict(
                            days_of_the_week=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "SUNDAY",
                                    "MONDAY",
                                    "TUESDAY",
                                    "WEDNESDAY",
                                    "THURSDAY",
                                    "FRIDAY",
                                    "SATURDAY",
                                ],
                            ),
                            kind=dict(
                                type="str",
                                required=True,
                                choices=["DAILY", "WEEKLY", "NONE", "MONTHLY"],
                            ),
                            retention_days=dict(type="int"),
                            backup_start=dict(type="str"),
                            days_of_the_month=dict(type="list", elements="int"),
                        ),
                    ),
                ),
            ),
            storage_details=dict(
                type="dict",
                options=dict(
                    system_type=dict(type="str", choices=["OCI_OPTIMIZED_STORAGE"]),
                    is_regionally_durable=dict(type="bool"),
                    availability_domain=dict(type="str"),
                    iops=dict(type="int"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    _from=dict(type="str"),
                    selected_item=dict(type="str"),
                    position=dict(type="str", choices=["AT", "BEFORE", "AFTER"]),
                    operation=dict(
                        type="str",
                        required=True,
                        choices=[
                            "MOVE",
                            "REMOVE",
                            "REPLACE",
                            "INSERT",
                            "REQUIRE",
                            "MERGE",
                            "PROHIBIT",
                        ],
                    ),
                    selection=dict(type="str", required=True),
                    value=dict(type="dict"),
                ),
            ),
            db_system_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system",
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
    elif resource_helper.is_patch_using_name():
        result = resource_helper.patch_using_name()
    elif resource_helper.is_patch():
        result = resource_helper.patch()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
