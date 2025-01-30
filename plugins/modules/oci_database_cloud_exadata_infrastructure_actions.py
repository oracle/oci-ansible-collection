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
module: oci_database_cloud_exadata_infrastructure_actions
short_description: Perform actions on a CloudExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CloudExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(action=add_storage_capacity), makes the storage capacity from additional storage servers available for Cloud VM Cluster consumption. Applies to
      Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.
    - For I(action=change_compartment), moves a cloud Exadata infrastructure resource and its dependent resources to another compartment. Applies to Exadata
      Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.For more information about moving resources to a different
      compartment, see L(Moving Database Resources to a Different
      Compartment,https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for I(action=change_compartment).
        type: str
    cloud_exadata_infrastructure_id:
        description:
            - The cloud Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the CloudExadataInfrastructure.
        type: str
        required: true
        choices:
            - "add_storage_capacity"
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_storage_capacity on cloud_exadata_infrastructure
  oci_database_cloud_exadata_infrastructure_actions:
    # required
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_storage_capacity

- name: Perform action change_compartment on cloud_exadata_infrastructure
  oci_database_cloud_exadata_infrastructure_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
        cpu_count:
            description:
                - The total number of CPU cores allocated.
            returned: on success
            type: int
            sample: 56
        max_cpu_count:
            description:
                - The total number of CPU cores available.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_memory_in_gbs:
            description:
                - The total memory available in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_db_node_storage_in_gbs:
            description:
                - The total local node storage available in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - Size, in terabytes, of the DATA disk group.
            returned: on success
            type: float
            sample: 1.2
        max_data_storage_in_tbs:
            description:
                - The total available DATA disk group size.
            returned: on success
            type: float
            sample: 1.2
        additional_storage_count:
            description:
                - The requested number of additional storage servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        activated_storage_count:
            description:
                - The requested number of additional storage servers activated for the Exadata infrastructure.
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
        storage_server_version:
            description:
                - "The software version of the storage servers (cells) in the cloud Exadata infrastructure.
                  Example: 20.1.15"
            returned: on success
            type: str
            sample: storage_server_version_example
        db_server_version:
            description:
                - "The software version of the database servers (dom0) in the cloud Exadata infrastructure.
                  Example: 20.1.15"
            returned: on success
            type: str
            sample: db_server_version_example
        monthly_storage_server_version:
            description:
                - "The monthly software version of the storage servers (cells) in the cloud Exadata infrastructure.
                  Example: 20.1.15"
            returned: on success
            type: str
            sample: monthly_storage_server_version_example
        monthly_db_server_version:
            description:
                - "The monthly software version of the database servers (dom0) in the cloud Exadata infrastructure.
                  Example: 20.1.15"
            returned: on success
            type: str
            sample: monthly_db_server_version_example
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
        "cpu_count": 56,
        "max_cpu_count": 56,
        "memory_size_in_gbs": 56,
        "max_memory_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "max_db_node_storage_in_gbs": 56,
        "data_storage_size_in_tbs": 1.2,
        "max_data_storage_in_tbs": 1.2,
        "additional_storage_count": 56,
        "activated_storage_count": 56,
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
        }],
        "storage_server_version": "storage_server_version_example",
        "db_server_version": "db_server_version_example",
        "monthly_storage_server_version": "monthly_storage_server_version_example",
        "monthly_db_server_version": "monthly_db_server_version_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCloudExadataInfrastructureCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudExadataInfrastructureActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_storage_capacity
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(CloudExadataInfrastructureActionsHelperGen, self).__init__(
            *args, **kwargs
        )
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "cloud_exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("cloud_exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_cloud_exadata_infrastructure

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_exadata_infrastructure,
            cloud_exadata_infrastructure_id=self.module.params.get(
                "cloud_exadata_infrastructure_id"
            ),
        )

    def add_storage_capacity(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_storage_capacity_cloud_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_exadata_infrastructure_id=self.module.params.get(
                    "cloud_exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCloudExadataInfrastructureCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_cloud_exadata_infrastructure_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_cloud_exadata_infrastructure_compartment_details=action_details,
                cloud_exadata_infrastructure_id=self.module.params.get(
                    "cloud_exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CloudExadataInfrastructureActionsHelperCustom = get_custom_class(
    "CloudExadataInfrastructureActionsHelperCustom"
)


class ResourceHelper(
    CloudExadataInfrastructureActionsHelperCustom,
    CloudExadataInfrastructureActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cloud_exadata_infrastructure_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=["add_storage_capacity", "change_compartment"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cloud_exadata_infrastructure",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
