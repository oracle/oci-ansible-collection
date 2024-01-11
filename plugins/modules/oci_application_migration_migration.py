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
module: oci_application_migration_migration
short_description: Manage a Migration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Migration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle
      Cloud
      Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information,
      see L(Manage Migrations,https://docs.cloud.oracle.com/iaas/application-migration/manage_migrations.htm).
    - When you create a migration, provide the required information to let Application Migration access the source environment.
      Application Migration uses this information to access the application in the source environment and discover application artifacts.
    - All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID).
      When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on
      that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.
    - After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state
      will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase,
      Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration.
      When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>.
      Next, you'll need to update the migration to provide configuration values. Before updating the
      migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.
    - To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests
      by using the <code>L(GetWorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/applicationmigration/20191031/WorkRequest/GetWorkRequest)</code>
      REST API operation on the work request or by viewing the status of the work request in
      the console.
    - "This resource has the following action operations in the M(oracle.oci.oci_application_migration_migration_actions) module: change_compartment,
      migrate_application."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the source.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
            - Required for create using I(state=present).
        type: str
    application_name:
        description:
            - Name of the application that you want to migrate from the source environment.
            - Required for create using I(state=present).
        type: str
    pre_created_target_database_type:
        description:
            - The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud
              Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.
        type: str
        choices:
            - "DATABASE_SYSTEM"
            - "NOT_SET"
    display_name:
        description:
            - User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the application that you are migrating.
            - This parameter is updatable.
        type: str
    discovery_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            service_instance_user:
                description:
                    - Application administrator username to access the Oracle Integration Classic instance in the source environment.
                    - Required when type is one of ['OAC', 'PCS', 'OIC', 'ICS']
                type: str
            service_instance_password:
                description:
                    - Password for this user.
                    - Required when type is one of ['OAC', 'PCS', 'OIC', 'ICS']
                type: str
            type:
                description:
                    - The type of application that you want to migrate.
                type: str
                choices:
                    - "OIC"
                    - "PCS"
                    - "ICS"
                    - "OAC"
                    - "JCS"
                    - "SOACS"
                required: true
            weblogic_user:
                description:
                    - WebLogic administrator username for the Oracle Java Cloud Service application in the source environment.
                    - Required when type is one of ['SOACS', 'JCS']
                type: str
            weblogic_password:
                description:
                    - The password of the WebLogic administrator for the Oracle Java Cloud Service application in the source environment.
                    - Required when type is one of ['SOACS', 'JCS']
                type: str
    is_selective_migration:
        description:
            - If set to `true`, Application Migration migrates the application resources selectively depending on the source.
            - This parameter is updatable.
        type: bool
    service_config:
        description:
            - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
              to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
              CreateMigration operation.
            - This parameter is updatable.
        type: dict
        suboptions:
            name:
                description:
                    - The name of the configuration field.
                type: str
            group:
                description:
                    - The name of the group to which this field belongs, if any.
                type: str
            type:
                description:
                    - The type of the configuration field.
                type: str
            value:
                description:
                    - The value of the field.
                type: str
            description:
                description:
                    - Help text to guide the user in setting the configuration value.
                type: str
            resource_list:
                description:
                    - A list of resources associated with a specific configuration object.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The display name of the resource field.
                        type: str
                    group:
                        description:
                            - The name of the group to which this field belongs to.
                        type: str
                    type:
                        description:
                            - The type of the resource field.
                        type: str
                        required: true
                    value:
                        description:
                            - The value of the field.
                        type: str
                        required: true
            is_required:
                description:
                    - Indicates whether or not the field is required (defaults to `true`).
                type: bool
            is_mutable:
                description:
                    - Indicates whether or not the field may be modified (defaults to `true`).
                type: bool
    application_config:
        description:
            - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
              to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
              CreateMigration operation.
            - This parameter is updatable.
        type: dict
        suboptions:
            name:
                description:
                    - The name of the configuration field.
                type: str
            group:
                description:
                    - The name of the group to which this field belongs, if any.
                type: str
            type:
                description:
                    - The type of the configuration field.
                type: str
            value:
                description:
                    - The value of the field.
                type: str
            description:
                description:
                    - Help text to guide the user in setting the configuration value.
                type: str
            resource_list:
                description:
                    - A list of resources associated with a specific configuration object.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The display name of the resource field.
                        type: str
                    group:
                        description:
                            - The name of the group to which this field belongs to.
                        type: str
                    type:
                        description:
                            - The type of the resource field.
                        type: str
                        required: true
                    value:
                        description:
                            - The value of the field.
                        type: str
                        required: true
            is_required:
                description:
                    - Indicates whether or not the field is required (defaults to `true`).
                type: bool
            is_mutable:
                description:
                    - Indicates whether or not the field may be modified (defaults to `true`).
                type: bool
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"Department\\":
              \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"Operations\\":
              {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    migration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the migration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Migration.
            - Use I(state=present) to create or update a Migration.
            - Use I(state=absent) to delete a Migration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create migration
  oci_application_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    application_name: application_name_example
    discovery_details:
      # required
      service_instance_user: service_instance_user_example
      service_instance_password: example-password
      type: OIC

    # optional
    pre_created_target_database_type: DATABASE_SYSTEM
    display_name: display_name_example
    description: description_example
    is_selective_migration: true
    service_config:
      # optional
      name: name_example
      group: group_example
      type: type_example
      value: value_example
      description: description_example
      resource_list:
      - # required
        type: type_example
        value: value_example

        # optional
        name: name_example
        group: group_example
      is_required: true
      is_mutable: true
    application_config:
      # optional
      name: name_example
      group: group_example
      type: type_example
      value: value_example
      description: description_example
      resource_list:
      - # required
        type: type_example
        value: value_example

        # optional
        name: name_example
        group: group_example
      is_required: true
      is_mutable: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update migration
  oci_application_migration_migration:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    discovery_details:
      # required
      service_instance_user: service_instance_user_example
      service_instance_password: example-password
      type: OIC
    is_selective_migration: true
    service_config:
      # optional
      name: name_example
      group: group_example
      type: type_example
      value: value_example
      description: description_example
      resource_list:
      - # required
        type: type_example
        value: value_example

        # optional
        name: name_example
        group: group_example
      is_required: true
      is_mutable: true
    application_config:
      # optional
      name: name_example
      group: group_example
      type: type_example
      value: value_example
      description: description_example
      resource_list:
      - # required
        type: type_example
        value: value_example

        # optional
        name: name_example
        group: group_example
      is_required: true
      is_mutable: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_application_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    discovery_details:
      # required
      service_instance_user: service_instance_user_example
      service_instance_password: example-password
      type: OIC
    is_selective_migration: true
    service_config:
      # optional
      name: name_example
      group: group_example
      type: type_example
      value: value_example
      description: description_example
      resource_list:
      - # required
        type: type_example
        value: value_example

        # optional
        name: name_example
        group: group_example
      is_required: true
      is_mutable: true
    application_config:
      # optional
      name: name_example
      group: group_example
      type: type_example
      value: value_example
      description: description_example
      resource_list:
      - # required
        type: type_example
        value: value_example

        # optional
        name: name_example
        group: group_example
      is_required: true
      is_mutable: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete migration
  oci_application_migration_migration:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_application_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
migration:
    description:
        - Details of the Migration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the migration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the migration.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name of the migration.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the migration.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time at which the migration was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source with which this migration is associated.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        application_name:
            description:
                - Name of the application which is being migrated. This is the name of the application in the source environment.
            returned: on success
            type: str
            sample: application_name_example
        application_type:
            description:
                - The type of application being migrated.
            returned: on success
            type: str
            sample: JCS
        pre_created_target_database_type:
            description:
                - The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud
                  Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance
                  types.
            returned: on success
            type: str
            sample: DATABASE_SYSTEM
        is_selective_migration:
            description:
                - If set to `true`, Application Migration migrates only the application resources that you specify. If set to `false`, Application Migration
                  migrates the entire application. When you migrate the entire application, all the application resources are migrated to the target
                  environment. You can selectively migrate resources only for the Oracle Integration Cloud and Oracle Integration Cloud Service applications.
            returned: on success
            type: bool
            sample: true
        service_config:
            description:
                - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
                  to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
                  CreateMigration operation.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the configuration field.
                    returned: on success
                    type: str
                    sample: name_example
                group:
                    description:
                        - The name of the group to which this field belongs, if any.
                    returned: on success
                    type: str
                    sample: group_example
                type:
                    description:
                        - The type of the configuration field.
                    returned: on success
                    type: str
                    sample: type_example
                value:
                    description:
                        - The value of the field.
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Help text to guide the user in setting the configuration value.
                    returned: on success
                    type: str
                    sample: description_example
                resource_list:
                    description:
                        - A list of resources associated with a specific configuration object.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The display name of the resource field.
                            returned: on success
                            type: str
                            sample: name_example
                        group:
                            description:
                                - The name of the group to which this field belongs to.
                            returned: on success
                            type: str
                            sample: group_example
                        type:
                            description:
                                - The type of the resource field.
                            returned: on success
                            type: str
                            sample: type_example
                        value:
                            description:
                                - The value of the field.
                            returned: on success
                            type: str
                            sample: value_example
                is_required:
                    description:
                        - Indicates whether or not the field is required (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
                is_mutable:
                    description:
                        - Indicates whether or not the field may be modified (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
        application_config:
            description:
                - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
                  to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
                  CreateMigration operation.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the configuration field.
                    returned: on success
                    type: str
                    sample: name_example
                group:
                    description:
                        - The name of the group to which this field belongs, if any.
                    returned: on success
                    type: str
                    sample: group_example
                type:
                    description:
                        - The type of the configuration field.
                    returned: on success
                    type: str
                    sample: type_example
                value:
                    description:
                        - The value of the field.
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Help text to guide the user in setting the configuration value.
                    returned: on success
                    type: str
                    sample: description_example
                resource_list:
                    description:
                        - A list of resources associated with a specific configuration object.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The display name of the resource field.
                            returned: on success
                            type: str
                            sample: name_example
                        group:
                            description:
                                - The name of the group to which this field belongs to.
                            returned: on success
                            type: str
                            sample: group_example
                        type:
                            description:
                                - The type of the resource field.
                            returned: on success
                            type: str
                            sample: type_example
                        value:
                            description:
                                - The value of the field.
                            returned: on success
                            type: str
                            sample: value_example
                is_required:
                    description:
                        - Indicates whether or not the field is required (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
                is_mutable:
                    description:
                        - Indicates whether or not the field may be modified (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
        lifecycle_state:
            description:
                - The current state of the migration.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current lifecycle state of the migration.
            returned: on success
            type: str
            sample: lifecycle_details_example
        migration_state:
            description:
                - The current state of the overall migration process.
            returned: on success
            type: str
            sample: DISCOVERING_APPLICATION
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "application_name": "application_name_example",
        "application_type": "JCS",
        "pre_created_target_database_type": "DATABASE_SYSTEM",
        "is_selective_migration": true,
        "service_config": {
            "name": "name_example",
            "group": "group_example",
            "type": "type_example",
            "value": "value_example",
            "description": "description_example",
            "resource_list": [{
                "name": "name_example",
                "group": "group_example",
                "type": "type_example",
                "value": "value_example"
            }],
            "is_required": true,
            "is_mutable": true
        },
        "application_config": {
            "name": "name_example",
            "group": "group_example",
            "type": "type_example",
            "value": "value_example",
            "description": "description_example",
            "resource_list": [{
                "name": "name_example",
                "group": "group_example",
                "type": "type_example",
                "value": "value_example"
            }],
            "is_required": true,
            "is_mutable": true
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "migration_state": "DISCOVERING_APPLICATION",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.application_migration import ApplicationMigrationClient
    from oci.application_migration.models import CreateMigrationDetails
    from oci.application_migration.models import UpdateMigrationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MigrationHelperGen, self).get_possible_entity_types() + [
            "migration",
            "migrations",
            "applicationMigrationmigration",
            "applicationMigrationmigrations",
            "migrationresource",
            "migrationsresource",
            "applicationmigration",
        ]

    def get_module_resource_id_param(self):
        return "migration_id"

    def get_module_resource_id(self):
        return self.module.params.get("migration_id")

    def get_get_fn(self):
        return self.client.get_migration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration, migration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration,
            migration_id=self.module.params.get("migration_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_migrations, **kwargs
        )

    def get_create_model_class(self):
        return CreateMigrationDetails

    def get_exclude_attributes(self):
        return ["discovery_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_migration_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMigrationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                update_migration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(migration_id=self.module.params.get("migration_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationHelperCustom = get_custom_class("MigrationHelperCustom")


class ResourceHelper(MigrationHelperCustom, MigrationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            source_id=dict(type="str"),
            application_name=dict(type="str"),
            pre_created_target_database_type=dict(
                type="str", choices=["DATABASE_SYSTEM", "NOT_SET"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            discovery_details=dict(
                type="dict",
                options=dict(
                    service_instance_user=dict(type="str"),
                    service_instance_password=dict(type="str", no_log=True),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["OIC", "PCS", "ICS", "OAC", "JCS", "SOACS"],
                    ),
                    weblogic_user=dict(type="str"),
                    weblogic_password=dict(type="str", no_log=True),
                ),
            ),
            is_selective_migration=dict(type="bool"),
            service_config=dict(type="dict"),
            application_config=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            migration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration",
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
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
