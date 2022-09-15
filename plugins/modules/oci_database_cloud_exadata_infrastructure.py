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
module: oci_database_cloud_exadata_infrastructure
short_description: Manage a CloudExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CloudExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a cloud Exadata infrastructure resource. This resource is used to create either an L(Exadata Cloud
      Service,https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm) instance or an Autonomous Database on dedicated Exadata infrastructure.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_cloud_exadata_infrastructure_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain where the cloud Exadata infrastructure is located.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    shape:
        description:
            - The shape of the cloud Exadata infrastructure resource.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    maintenance_window:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            preference:
                description:
                    - The maintenance window scheduling preference.
                type: str
                choices:
                    - "NO_PREFERENCE"
                    - "CUSTOM_PREFERENCE"
                required: true
            patching_mode:
                description:
                    - "Cloud Exadata infrastructure node patching method, either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
                    - "*IMPORTANT*: Non-rolling infrastructure patching involves system down time. See L(Oracle-Managed Infrastructure Maintenance
                      Updates,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle) for more information."
                type: str
                choices:
                    - "ROLLING"
                    - "NONROLLING"
            is_custom_action_timeout_enabled:
                description:
                    - If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.
                type: bool
            custom_action_timeout_in_mins:
                description:
                    - Determines the amount of time the system will wait before the start of each database server patching operation.
                      Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).
                type: int
            is_monthly_patching_enabled:
                description:
                    - If true, enables the monthly patching option.
                type: bool
            months:
                description:
                    - Months during the year when maintenance should be performed.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Name of the month of the year.
                        type: str
                        choices:
                            - "JANUARY"
                            - "FEBRUARY"
                            - "MARCH"
                            - "APRIL"
                            - "MAY"
                            - "JUNE"
                            - "JULY"
                            - "AUGUST"
                            - "SEPTEMBER"
                            - "OCTOBER"
                            - "NOVEMBER"
                            - "DECEMBER"
                        required: true
            weeks_of_month:
                description:
                    - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                      duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                      For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                      Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                      Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the
                      week and hours that maintenance will be performed.
                type: list
                elements: int
            days_of_week:
                description:
                    - Days during the week when maintenance should be performed.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Name of the day of the week.
                        type: str
                        choices:
                            - "MONDAY"
                            - "TUESDAY"
                            - "WEDNESDAY"
                            - "THURSDAY"
                            - "FRIDAY"
                            - "SATURDAY"
                            - "SUNDAY"
                        required: true
            hours_of_day:
                description:
                    - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                      - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 -
                        represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC"
                type: list
                elements: int
            lead_time_in_weeks:
                description:
                    - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.
                type: int
    compute_count:
        description:
            - The number of compute servers for the cloud Exadata infrastructure.
            - This parameter is updatable.
        type: int
    storage_count:
        description:
            - The number of storage servers for the cloud Exadata infrastructure.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    customer_contacts:
        description:
            - Customer contacts.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            email:
                description:
                    - The email address used by Oracle to send notifications regarding databases and infrastructure.
                type: str
    cloud_exadata_infrastructure_id:
        description:
            - The cloud Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_delete_vm_clusters:
        description:
            - If `true`, forces the deletion the specified cloud Exadata infrastructure resource as well as all associated VM clusters. If `false`, the cloud
              Exadata infrastructure resource can be deleted only if it has no associated VM clusters. Default value is `false`.
        type: bool
    state:
        description:
            - The state of the CloudExadataInfrastructure.
            - Use I(state=present) to create or update a CloudExadataInfrastructure.
            - Use I(state=absent) to delete a CloudExadataInfrastructure.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create cloud_exadata_infrastructure
  oci_database_cloud_exadata_infrastructure:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example
    display_name: display_name_example

    # optional
    maintenance_window:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      is_monthly_patching_enabled: true
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    compute_count: 56
    storage_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    customer_contacts:
    - # optional
      email: email_example

- name: Update cloud_exadata_infrastructure
  oci_database_cloud_exadata_infrastructure:
    # required
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    maintenance_window:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      is_monthly_patching_enabled: true
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    compute_count: 56
    storage_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    customer_contacts:
    - # optional
      email: email_example

- name: Update cloud_exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_cloud_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    maintenance_window:
      # required
      preference: NO_PREFERENCE

      # optional
      patching_mode: ROLLING
      is_custom_action_timeout_enabled: true
      custom_action_timeout_in_mins: 56
      is_monthly_patching_enabled: true
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    compute_count: 56
    storage_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    customer_contacts:
    - # optional
      email: email_example

- name: Delete cloud_exadata_infrastructure
  oci_database_cloud_exadata_infrastructure:
    # required
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    is_delete_vm_clusters: true

- name: Delete cloud_exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_cloud_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
cloud_exadata_infrastructure:
    description:
        - Details of the CloudExadataInfrastructure resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the cloud Exadata infrastructure resource.
            returned: on success
            type: str
            sample: PROVISIONING
        display_name:
            description:
                - The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        shape:
            description:
                - The model name of the cloud Exadata infrastructure resource.
            returned: on success
            type: str
            sample: shape_example
        availability_domain:
            description:
                - The name of the availability domain that the cloud Exadata infrastructure resource is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compute_count:
            description:
                - The number of compute servers for the cloud Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        storage_count:
            description:
                - The number of storage servers for the cloud Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        total_storage_size_in_gbs:
            description:
                - The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).
            returned: on success
            type: int
            sample: 56
        available_storage_size_in_gbs:
            description:
                - The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the cloud Exadata infrastructure resource was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preference:
                    description:
                        - The maintenance window scheduling preference.
                    returned: on success
                    type: str
                    sample: NO_PREFERENCE
                patching_mode:
                    description:
                        - "Cloud Exadata infrastructure node patching method, either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
                        - "*IMPORTANT*: Non-rolling infrastructure patching involves system down time. See L(Oracle-Managed Infrastructure Maintenance
                          Updates,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle) for more information."
                    returned: on success
                    type: str
                    sample: ROLLING
                is_custom_action_timeout_enabled:
                    description:
                        - If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.
                    returned: on success
                    type: bool
                    sample: true
                custom_action_timeout_in_mins:
                    description:
                        - Determines the amount of time the system will wait before the start of each database server patching operation.
                          Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).
                    returned: on success
                    type: int
                    sample: 56
                is_monthly_patching_enabled:
                    description:
                        - If true, enables the monthly patching option.
                    returned: on success
                    type: bool
                    sample: true
                months:
                    description:
                        - Months during the year when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the month of the year.
                            returned: on success
                            type: str
                            sample: JANUARY
                weeks_of_month:
                    description:
                        - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                          duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                          For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                          Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                          Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of
                          the week and hours that maintenance will be performed.
                    returned: on success
                    type: list
                    sample: []
                days_of_week:
                    description:
                        - Days during the week when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                hours_of_day:
                    description:
                        - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                          - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12
                            - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59
                            UTC"
                    returned: on success
                    type: list
                    sample: []
                lead_time_in_weeks:
                    description:
                        - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to
                          4.
                    returned: on success
                    type: int
                    sample: 56
        last_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance run.
            returned: on success
            type: str
            sample: "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: str
            sample: "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        customer_contacts:
            description:
                - The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource.
                  Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system
                  hardware, and other information needed by administrators.
                  Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.
            returned: on success
            type: complex
            contains:
                email:
                    description:
                        - The email address used by Oracle to send notifications regarding databases and infrastructure.
                    returned: on success
                    type: str
                    sample: email_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "display_name": "display_name_example",
        "shape": "shape_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "compute_count": 56,
        "storage_count": 56,
        "total_storage_size_in_gbs": 56,
        "available_storage_size_in_gbs": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "patching_mode": "ROLLING",
            "is_custom_action_timeout_enabled": true,
            "custom_action_timeout_in_mins": 56,
            "is_monthly_patching_enabled": true,
            "months": [{
                "name": "JANUARY"
            }],
            "weeks_of_month": [],
            "days_of_week": [{
                "name": "MONDAY"
            }],
            "hours_of_day": [],
            "lead_time_in_weeks": 56
        },
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "customer_contacts": [{
            "email": "email_example"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateCloudExadataInfrastructureDetails
    from oci.database.models import UpdateCloudExadataInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudExadataInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(CloudExadataInfrastructureHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            CloudExadataInfrastructureHelperGen, self
        ).get_possible_entity_types() + [
            "cloudexadatainfrastructure",
            "cloudexadatainfrastructures",
            "databasecloudexadatainfrastructure",
            "databasecloudexadatainfrastructures",
            "cloudexadatainfrastructureresource",
            "cloudexadatainfrastructuresresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "cloud_exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("cloud_exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_cloud_exadata_infrastructure

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_exadata_infrastructure,
            cloud_exadata_infrastructure_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_exadata_infrastructure,
            cloud_exadata_infrastructure_id=self.module.params.get(
                "cloud_exadata_infrastructure_id"
            ),
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
            self.client.list_cloud_exadata_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return CreateCloudExadataInfrastructureDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cloud_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_cloud_exadata_infrastructure_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateCloudExadataInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cloud_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_exadata_infrastructure_id=self.module.params.get(
                    "cloud_exadata_infrastructure_id"
                ),
                update_cloud_exadata_infrastructure_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_cloud_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_exadata_infrastructure_id=self.module.params.get(
                    "cloud_exadata_infrastructure_id"
                ),
                is_delete_vm_clusters=self.module.params.get("is_delete_vm_clusters"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CloudExadataInfrastructureHelperCustom = get_custom_class(
    "CloudExadataInfrastructureHelperCustom"
)


class ResourceHelper(
    CloudExadataInfrastructureHelperCustom, CloudExadataInfrastructureHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            shape=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            maintenance_window=dict(
                type="dict",
                options=dict(
                    preference=dict(
                        type="str",
                        required=True,
                        choices=["NO_PREFERENCE", "CUSTOM_PREFERENCE"],
                    ),
                    patching_mode=dict(type="str", choices=["ROLLING", "NONROLLING"]),
                    is_custom_action_timeout_enabled=dict(type="bool"),
                    custom_action_timeout_in_mins=dict(type="int"),
                    is_monthly_patching_enabled=dict(type="bool"),
                    months=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "JANUARY",
                                    "FEBRUARY",
                                    "MARCH",
                                    "APRIL",
                                    "MAY",
                                    "JUNE",
                                    "JULY",
                                    "AUGUST",
                                    "SEPTEMBER",
                                    "OCTOBER",
                                    "NOVEMBER",
                                    "DECEMBER",
                                ],
                            )
                        ),
                    ),
                    weeks_of_month=dict(type="list", elements="int"),
                    days_of_week=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "MONDAY",
                                    "TUESDAY",
                                    "WEDNESDAY",
                                    "THURSDAY",
                                    "FRIDAY",
                                    "SATURDAY",
                                    "SUNDAY",
                                ],
                            )
                        ),
                    ),
                    hours_of_day=dict(type="list", elements="int"),
                    lead_time_in_weeks=dict(type="int"),
                ),
            ),
            compute_count=dict(type="int"),
            storage_count=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            customer_contacts=dict(
                type="list", elements="dict", options=dict(email=dict(type="str"))
            ),
            cloud_exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            is_delete_vm_clusters=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cloud_exadata_infrastructure",
        service_client_class=DatabaseClient,
        namespace="database",
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
