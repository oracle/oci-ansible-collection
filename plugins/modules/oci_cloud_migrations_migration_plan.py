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
module: oci_cloud_migrations_migration_plan
short_description: Manage a MigrationPlan resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MigrationPlan resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a migration plan.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_migrations_migration_plan_actions) module: change_compartment, execute,
      import_migration_plan, refresh."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment identifier
            - Required for create using I(state=present).
        type: str
    migration_id:
        description:
            - The OCID of the associated migration.
            - Required for create using I(state=present).
        type: str
    source_migration_plan_id:
        description:
            - Source migraiton plan ID to be cloned.
        type: str
    display_name:
        description:
            - Migration plan identifier
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    strategies:
        description:
            - List of strategies for the resources to be migrated.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            percentile:
                description:
                    - Percentile value
                    - Required when strategy_type is 'PERCENTILE'
                type: str
                choices:
                    - "P50"
                    - "P90"
                    - "P95"
                    - "P99"
            metric_type:
                description:
                    - The current state of the migration plan.
                    - Applicable when strategy_type is one of ['AVERAGE', 'PEAK']
                type: str
                choices:
                    - "AUTO"
                    - "HISTORICAL"
                    - "RUNTIME"
            metric_time_window:
                description:
                    - The current state of the migration plan.
                    - Applicable when strategy_type is one of ['AVERAGE', 'PEAK', 'PERCENTILE']
                type: str
                choices:
                    - "1d"
                    - "7d"
                    - "30d"
            resource_type:
                description:
                    - The type of resource.
                type: str
                choices:
                    - "CPU"
                    - "MEMORY"
                    - "ALL"
                required: true
            strategy_type:
                description:
                    - The type of strategy used for migration.
                type: str
                choices:
                    - "PEAK"
                    - "PERCENTILE"
                    - "AVERAGE"
                    - "AS_IS"
                required: true
            adjustment_multiplier:
                description:
                    - The real resource usage is multiplied to this number before making any recommendation.
                type: float
    target_environments:
        description:
            - List of target environments.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            target_compartment_id:
                description:
                    - Target compartment identifier
                type: str
            target_environment_type:
                description:
                    - The type of target environment.
                type: str
                choices:
                    - "VM_TARGET_ENV"
                required: true
            availability_domain:
                description:
                    - Availability Domain of the VM configuration.
                type: str
            fault_domain:
                description:
                    - Fault domain of the VM configuration.
                type: str
            vcn:
                description:
                    - OCID of the VM configuration VCN.
                type: str
                required: true
            subnet:
                description:
                    - OCID of the VM configuration subnet.
                type: str
                required: true
            dedicated_vm_host:
                description:
                    - OCID of the dedicated VM configuration host.
                type: str
            ms_license:
                description:
                    - Microsoft license for the VM configuration.
                type: str
            preferred_shape_type:
                description:
                    - Preferred VM shape type provided by the customer.
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    migration_plan_id:
        description:
            - Unique migration plan identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MigrationPlan.
            - Use I(state=present) to create or update a MigrationPlan.
            - Use I(state=absent) to delete a MigrationPlan.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create migration_plan
  oci_cloud_migrations_migration_plan:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    source_migration_plan_id: "ocid1.sourcemigrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    strategies:
    - # required
      resource_type: CPU
      strategy_type: PEAK

      # optional
      metric_type: AUTO
      metric_time_window: 1d
      adjustment_multiplier: 3.4
    target_environments:
    - # required
      target_environment_type: VM_TARGET_ENV
      vcn: vcn_example
      subnet: subnet_example

      # optional
      target_compartment_id: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
      availability_domain: Uocm:PHX-AD-1
      fault_domain: FAULT-DOMAIN-1
      dedicated_vm_host: dedicated_vm_host_example
      ms_license: ms_license_example
      preferred_shape_type: preferred_shape_type_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update migration_plan
  oci_cloud_migrations_migration_plan:
    # required
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    strategies:
    - # required
      resource_type: CPU
      strategy_type: PEAK

      # optional
      metric_type: AUTO
      metric_time_window: 1d
      adjustment_multiplier: 3.4
    target_environments:
    - # required
      target_environment_type: VM_TARGET_ENV
      vcn: vcn_example
      subnet: subnet_example

      # optional
      target_compartment_id: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
      availability_domain: Uocm:PHX-AD-1
      fault_domain: FAULT-DOMAIN-1
      dedicated_vm_host: dedicated_vm_host_example
      ms_license: ms_license_example
      preferred_shape_type: preferred_shape_type_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update migration_plan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_migrations_migration_plan:
    # required
    display_name: display_name_example

    # optional
    strategies:
    - # required
      resource_type: CPU
      strategy_type: PEAK

      # optional
      metric_type: AUTO
      metric_time_window: 1d
      adjustment_multiplier: 3.4
    target_environments:
    - # required
      target_environment_type: VM_TARGET_ENV
      vcn: vcn_example
      subnet: subnet_example

      # optional
      target_compartment_id: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
      availability_domain: Uocm:PHX-AD-1
      fault_domain: FAULT-DOMAIN-1
      dedicated_vm_host: dedicated_vm_host_example
      ms_license: ms_license_example
      preferred_shape_type: preferred_shape_type_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete migration_plan
  oci_cloud_migrations_migration_plan:
    # required
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete migration_plan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_migrations_migration_plan:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
migration_plan:
    description:
        - Details of the MigrationPlan resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique Oracle ID (OCID) that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the migration plan.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The time when the migration plan was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the migration plan was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the migration plan.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        migration_id:
            description:
                - The OCID of the associated migration.
            returned: on success
            type: str
            sample: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
        strategies:
            description:
                - List of strategies for the resources to be migrated.
            returned: on success
            type: complex
            contains:
                metric_type:
                    description:
                        - The current state of the migration plan.
                    returned: on success
                    type: str
                    sample: AUTO
                resource_type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: str
                    sample: CPU
                strategy_type:
                    description:
                        - The type of strategy used for migration.
                    returned: on success
                    type: str
                    sample: AS_IS
                percentile:
                    description:
                        - Percentile value
                    returned: on success
                    type: str
                    sample: P50
                adjustment_multiplier:
                    description:
                        - The real resource usage is multiplied to this number before making any recommendation.
                    returned: on success
                    type: float
                    sample: 3.4
                metric_time_window:
                    description:
                        - The current state of the migration plan.
                    returned: on success
                    type: str
                    sample: 1d
        migration_plan_stats:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                total_estimated_cost:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        compute:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpu_per_hour:
                                    description:
                                        - OCPU per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                ocpu_per_hour_by_subscription:
                                    description:
                                        - OCPU per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                memory_gb_per_hour:
                                    description:
                                        - Gigabyte per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                memory_gb_per_hour_by_subscription:
                                    description:
                                        - Gigabyte per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                gpu_per_hour:
                                    description:
                                        - GPU per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                gpu_per_hour_by_subscription:
                                    description:
                                        - GPU per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_per_hour:
                                    description:
                                        - Total per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_per_hour_by_subscription:
                                    description:
                                        - Total usage per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                ocpu_count:
                                    description:
                                        - Total number of OCPUs
                                    returned: on success
                                    type: float
                                    sample: 10
                                memory_amount_gb:
                                    description:
                                        - Total usage of memory
                                    returned: on success
                                    type: float
                                    sample: 10
                                gpu_count:
                                    description:
                                        - Total number of GPU
                                    returned: on success
                                    type: float
                                    sample: 10
                        storage:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                volumes:
                                    description:
                                        - Volume estimation
                                    returned: on success
                                    type: complex
                                    contains:
                                        capacity_gb:
                                            description:
                                                - Gigabyte storage capacity
                                            returned: on success
                                            type: float
                                            sample: 10
                                        description:
                                            description:
                                                - Volume description
                                            returned: on success
                                            type: str
                                            sample: description_example
                                        total_gb_per_month:
                                            description:
                                                - Gigabyte storage capacity per month.
                                            returned: on success
                                            type: float
                                            sample: 10
                                        total_gb_per_month_by_subscription:
                                            description:
                                                - Gigabyte storage capacity per month by subscription
                                            returned: on success
                                            type: float
                                            sample: 10
                                total_gb_per_month:
                                    description:
                                        - Gigabyte storage capacity per month.
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_gb_per_month_by_subscription:
                                    description:
                                        - Gigabyte storage capacity per month by subscription.
                                    returned: on success
                                    type: float
                                    sample: 10
                        os_image:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                total_per_hour:
                                    description:
                                        - Total price per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_per_hour_by_subscription:
                                    description:
                                        - Total price per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                        currency_code:
                            description:
                                - Currency code in the ISO format.
                            returned: on success
                            type: str
                            sample: currency_code_example
                        total_estimation_per_month:
                            description:
                                - Total estimation per month
                            returned: on success
                            type: float
                            sample: 10
                        total_estimation_per_month_by_subscription:
                            description:
                                - Total estimation per month by subscription.
                            returned: on success
                            type: float
                            sample: 10
                        subscription_id:
                            description:
                                - Subscription ID
                            returned: on success
                            type: str
                            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
                time_updated:
                    description:
                        - The time when the migration plan was calculated. An RFC3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                vm_count:
                    description:
                        - The total count of VMs in migration
                    returned: on success
                    type: int
                    sample: 56
        calculated_limits:
            description:
                - "Limits of the resources that are needed for migration. Example: {\\"BlockVolume\\": 2, \\"VCN\\": 1}"
            returned: on success
            type: dict
            sample: {}
        target_environments:
            description:
                - List of target environments.
            returned: on success
            type: complex
            contains:
                target_compartment_id:
                    description:
                        - Target compartment identifier
                    returned: on success
                    type: str
                    sample: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
                target_environment_type:
                    description:
                        - The type of target environment.
                    returned: on success
                    type: str
                    sample: VM_TARGET_ENV
                availability_domain:
                    description:
                        - Availability Domain of the VM configuration.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - Fault domain of the VM configuration.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                vcn:
                    description:
                        - OCID of the VM configuration VCN.
                    returned: on success
                    type: str
                    sample: vcn_example
                subnet:
                    description:
                        - OCID of the VM configuration subnet.
                    returned: on success
                    type: str
                    sample: subnet_example
                dedicated_vm_host:
                    description:
                        - OCID of the dedicated VM configuration host.
                    returned: on success
                    type: str
                    sample: dedicated_vm_host_example
                ms_license:
                    description:
                        - Microsoft license for the VM configuration.
                    returned: on success
                    type: str
                    sample: ms_license_example
                preferred_shape_type:
                    description:
                        - Preferred VM shape type provided by the customer.
                    returned: on success
                    type: str
                    sample: preferred_shape_type_example
        reference_to_rms_stack:
            description:
                - OCID of the referenced ORM job.
            returned: on success
            type: str
            sample: reference_to_rms_stack_example
        source_migration_plan_id:
            description:
                - Source migraiton plan ID to be cloned.
            returned: on success
            type: str
            sample: "ocid1.sourcemigrationplan.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "migration_id": "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx",
        "strategies": [{
            "metric_type": "AUTO",
            "resource_type": "CPU",
            "strategy_type": "AS_IS",
            "percentile": "P50",
            "adjustment_multiplier": 3.4,
            "metric_time_window": "1d"
        }],
        "migration_plan_stats": {
            "total_estimated_cost": {
                "compute": {
                    "ocpu_per_hour": 10,
                    "ocpu_per_hour_by_subscription": 10,
                    "memory_gb_per_hour": 10,
                    "memory_gb_per_hour_by_subscription": 10,
                    "gpu_per_hour": 10,
                    "gpu_per_hour_by_subscription": 10,
                    "total_per_hour": 10,
                    "total_per_hour_by_subscription": 10,
                    "ocpu_count": 10,
                    "memory_amount_gb": 10,
                    "gpu_count": 10
                },
                "storage": {
                    "volumes": [{
                        "capacity_gb": 10,
                        "description": "description_example",
                        "total_gb_per_month": 10,
                        "total_gb_per_month_by_subscription": 10
                    }],
                    "total_gb_per_month": 10,
                    "total_gb_per_month_by_subscription": 10
                },
                "os_image": {
                    "total_per_hour": 10,
                    "total_per_hour_by_subscription": 10
                },
                "currency_code": "currency_code_example",
                "total_estimation_per_month": 10,
                "total_estimation_per_month_by_subscription": 10,
                "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "time_updated": "2013-10-20T19:20:30+01:00",
            "vm_count": 56
        },
        "calculated_limits": {},
        "target_environments": [{
            "target_compartment_id": "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "target_environment_type": "VM_TARGET_ENV",
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1",
            "vcn": "vcn_example",
            "subnet": "subnet_example",
            "dedicated_vm_host": "dedicated_vm_host_example",
            "ms_license": "ms_license_example",
            "preferred_shape_type": "preferred_shape_type_example"
        }],
        "reference_to_rms_stack": "reference_to_rms_stack_example",
        "source_migration_plan_id": "ocid1.sourcemigrationplan.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.cloud_migrations import MigrationClient
    from oci.cloud_migrations.models import CreateMigrationPlanDetails
    from oci.cloud_migrations.models import UpdateMigrationPlanDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationPlanHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MigrationPlanHelperGen, self).get_possible_entity_types() + [
            "ocmmigrationplan",
            "ocmmigrationplans",
            "cloudMigrationsocmmigrationplan",
            "cloudMigrationsocmmigrationplans",
            "ocmmigrationplanresource",
            "ocmmigrationplansresource",
            "migrationplan",
            "migrationplans",
            "cloudMigrationsmigrationplan",
            "cloudMigrationsmigrationplans",
            "migrationplanresource",
            "migrationplansresource",
            "cloudmigrations",
        ]

    def get_module_resource_id_param(self):
        return "migration_plan_id"

    def get_module_resource_id(self):
        return self.module.params.get("migration_plan_id")

    def get_get_fn(self):
        return self.client.get_migration_plan

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration_plan, migration_plan_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration_plan,
            migration_plan_id=self.module.params.get("migration_plan_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "migration_id",
            "display_name",
            "migration_plan_id",
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
            self.client.list_migration_plans, **kwargs
        )

    def get_create_model_class(self):
        return CreateMigrationPlanDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_migration_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(create_migration_plan_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMigrationPlanDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_migration_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_plan_id=self.module.params.get("migration_plan_id"),
                update_migration_plan_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_migration_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_plan_id=self.module.params.get("migration_plan_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationPlanHelperCustom = get_custom_class("MigrationPlanHelperCustom")


class ResourceHelper(MigrationPlanHelperCustom, MigrationPlanHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            migration_id=dict(type="str"),
            source_migration_plan_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            strategies=dict(
                type="list",
                elements="dict",
                options=dict(
                    percentile=dict(type="str", choices=["P50", "P90", "P95", "P99"]),
                    metric_type=dict(
                        type="str", choices=["AUTO", "HISTORICAL", "RUNTIME"]
                    ),
                    metric_time_window=dict(type="str", choices=["1d", "7d", "30d"]),
                    resource_type=dict(
                        type="str", required=True, choices=["CPU", "MEMORY", "ALL"]
                    ),
                    strategy_type=dict(
                        type="str",
                        required=True,
                        choices=["PEAK", "PERCENTILE", "AVERAGE", "AS_IS"],
                    ),
                    adjustment_multiplier=dict(type="float"),
                ),
            ),
            target_environments=dict(
                type="list",
                elements="dict",
                options=dict(
                    target_compartment_id=dict(type="str"),
                    target_environment_type=dict(
                        type="str", required=True, choices=["VM_TARGET_ENV"]
                    ),
                    availability_domain=dict(type="str"),
                    fault_domain=dict(type="str"),
                    vcn=dict(type="str", required=True),
                    subnet=dict(type="str", required=True),
                    dedicated_vm_host=dict(type="str"),
                    ms_license=dict(type="str"),
                    preferred_shape_type=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            migration_plan_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration_plan",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
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
