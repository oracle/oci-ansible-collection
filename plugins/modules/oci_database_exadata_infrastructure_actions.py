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
module: oci_database_exadata_infrastructure_actions
short_description: Perform actions on an ExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(action=activate), activates the specified Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only.
    - For I(action=add_storage_capacity), makes the storage capacity from additional storage servers available for VM Cluster consumption. Applies to Exadata
      Cloud@Customer instances only.
    - For I(action=change_compartment), moves an Exadata infrastructure resource and its dependent resources to another compartment. Applies to Exadata
      Cloud@Customer instances only.
      To move an Exadata Cloud Service infrastructure resource to another compartment, use the
      L(ChangeCloudExadataInfrastructureCompartment,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudExadataInfrastructure/ChangeCloudExadataInfrastructureCompartment) operation.
    - For I(action=download_exadata_infrastructure_config_file), downloads the configuration file for the specified Exadata Cloud@Customer infrastructure.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    activation_file:
        description:
            - "The base 64 encoded contents of the activation zip file. You can use the ansible 'lookup' and 'b64encode' functionality to read a file and base
              64 encode its contents. For example: {{ lookup('file', 'activation.zip') | b64encode }}"
            - Required for I(action=activate).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    config_file_dest:
        description:
            - The destination file path to write the config file to when I(action=download_exadata_infrastructure_config_file). The file will be created if it
              does not exist. If the file already exists, the content will be overwritten. I(config_file_dest) is required if
              I(action=download_exadata_infrastructure_config_file).
            - Required for I(action=download_exadata_infrastructure_config_file).
        type: str
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ExadataInfrastructure.
        type: str
        required: true
        choices:
            - "activate"
            - "add_storage_capacity"
            - "change_compartment"
            - "download_exadata_infrastructure_config_file"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on exadata_infrastructure
  oci_database_exadata_infrastructure_actions:
    # required
    activation_file: activation_file_example
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

- name: Perform action add_storage_capacity on exadata_infrastructure
  oci_database_exadata_infrastructure_actions:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_storage_capacity

- name: Perform action change_compartment on exadata_infrastructure
  oci_database_exadata_infrastructure_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action download_exadata_infrastructure_config_file on exadata_infrastructure
  oci_database_exadata_infrastructure_actions:
    # required
    config_file_dest: /tmp/exadata_config_file.zip
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: download_exadata_infrastructure_config_file

"""

RETURN = """
exadata_infrastructure:
    description:
        - Details of the ExadataInfrastructure resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
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
                - The current lifecycle state of the Exadata infrastructure.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: str
            sample: shape_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
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
        max_db_node_storage_in_g_bs:
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
        max_data_storage_in_t_bs:
            description:
                - The total available DATA disk group size.
            returned: on success
            type: float
            sample: 1.2
        rack_serial_number:
            description:
                - The serial number for the Exadata infrastructure.
            returned: on success
            type: str
            sample: rack_serial_number_example
        storage_count:
            description:
                - The number of Exadata storage servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
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
        compute_count:
            description:
                - The number of compute servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        additional_compute_count:
            description:
                - The requested number of additional compute servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        additional_compute_system_model:
            description:
                - Oracle Exadata System Model specification. The system model determines the amount of compute or storage
                  server resources available for use. For more information, please see L(System and Shape Configuration
                  Options],https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-
                  options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)
            returned: on success
            type: str
            sample: X7
        cloud_control_plane_server1:
            description:
                - The IP address for the first control plane server.
            returned: on success
            type: str
            sample: cloud_control_plane_server1_example
        cloud_control_plane_server2:
            description:
                - The IP address for the second control plane server.
            returned: on success
            type: str
            sample: cloud_control_plane_server2_example
        netmask:
            description:
                - The netmask for the control plane network.
            returned: on success
            type: str
            sample: netmask_example
        gateway:
            description:
                - The gateway for the control plane network.
            returned: on success
            type: str
            sample: gateway_example
        admin_network_cidr:
            description:
                - The CIDR block for the Exadata administration network.
            returned: on success
            type: str
            sample: admin_network_cidr_example
        infini_band_network_cidr:
            description:
                - The CIDR block for the Exadata InfiniBand interconnect.
            returned: on success
            type: str
            sample: infini_band_network_cidr_example
        corporate_proxy:
            description:
                - The corporate network proxy for access to the control plane network.
            returned: on success
            type: str
            sample: corporate_proxy_example
        dns_server:
            description:
                - The list of DNS server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        ntp_server:
            description:
                - The list of NTP server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the Exadata infrastructure was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        csi_number:
            description:
                - The CSI Number of the Exadata infrastructure.
            returned: on success
            type: str
            sample: csi_number_example
        contacts:
            description:
                - The list of contacts for the Exadata infrastructure.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: name_example
                phone_number:
                    description:
                        - The phone number for the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: phone_number_example
                email:
                    description:
                        - The email for the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: email_example
                is_primary:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.
                    returned: on success
                    type: bool
                    sample: true
                is_contact_mos_validated:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure
                          contact is not a valid MOS contact.
                    returned: on success
                    type: bool
                    sample: true
        maintenance_slo_status:
            description:
                - A field to capture 'Maintenance SLO Status' for the Exadata infrastructure with values 'OK', 'DEGRADED'. Default is 'OK' when the
                  infrastructure is provisioned.
            returned: on success
            type: str
            sample: OK
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
        storage_server_version:
            description:
                - The software version of the storage servers (cells) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: storage_server_version_example
        db_server_version:
            description:
                - The software version of the database servers (dom0) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: db_server_version_example
        monthly_db_server_version:
            description:
                - The monthly software version of the database servers (dom0) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: monthly_db_server_version_example
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
        is_cps_offline_report_enabled:
            description:
                - Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status
                  themselves and fix problems on their end, saving time and frustration
                  for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata
                  infrastructure provisioning. You can also disable or enable it at any time
                  using the UpdateExadatainfrastructure API.
            returned: on success
            type: bool
            sample: true
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "shape": "shape_example",
        "time_zone": "time_zone_example",
        "cpus_enabled": 56,
        "max_cpu_count": 56,
        "memory_size_in_gbs": 56,
        "max_memory_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "max_db_node_storage_in_g_bs": 56,
        "data_storage_size_in_tbs": 1.2,
        "max_data_storage_in_t_bs": 1.2,
        "rack_serial_number": "rack_serial_number_example",
        "storage_count": 56,
        "additional_storage_count": 56,
        "activated_storage_count": 56,
        "compute_count": 56,
        "additional_compute_count": 56,
        "additional_compute_system_model": "X7",
        "cloud_control_plane_server1": "cloud_control_plane_server1_example",
        "cloud_control_plane_server2": "cloud_control_plane_server2_example",
        "netmask": "netmask_example",
        "gateway": "gateway_example",
        "admin_network_cidr": "admin_network_cidr_example",
        "infini_band_network_cidr": "infini_band_network_cidr_example",
        "corporate_proxy": "corporate_proxy_example",
        "dns_server": [],
        "ntp_server": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "csi_number": "csi_number_example",
        "contacts": [{
            "name": "name_example",
            "phone_number": "phone_number_example",
            "email": "email_example",
            "is_primary": true,
            "is_contact_mos_validated": true
        }],
        "maintenance_slo_status": "OK",
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
        "storage_server_version": "storage_server_version_example",
        "db_server_version": "db_server_version_example",
        "monthly_db_server_version": "monthly_db_server_version_example",
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cps_offline_report_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ActivateExadataInfrastructureDetails
    from oci.database.models import ChangeExadataInfrastructureCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        add_storage_capacity
        change_compartment
        download_exadata_infrastructure_config_file
    """

    def __init__(self, *args, **kwargs):
        super(ExadataInfrastructureActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_exadata_infrastructure

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_infrastructure,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
        )

    def activate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ActivateExadataInfrastructureDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                activate_exadata_infrastructure_details=action_details,
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

    def add_storage_capacity(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_storage_capacity_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
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
            self.module.params, ChangeExadataInfrastructureCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_exadata_infrastructure_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_exadata_infrastructure_compartment_details=action_details,
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
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

    def download_exadata_infrastructure_config_file(self):
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.download_exadata_infrastructure_config_file,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )
        dest = self.module.params.get("config_file_dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


ExadataInfrastructureActionsHelperCustom = get_custom_class(
    "ExadataInfrastructureActionsHelperCustom"
)


class ResourceHelper(
    ExadataInfrastructureActionsHelperCustom, ExadataInfrastructureActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            activation_file=dict(type="str"),
            compartment_id=dict(type="str"),
            config_file_dest=dict(type="str"),
            exadata_infrastructure_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "activate",
                    "add_storage_capacity",
                    "change_compartment",
                    "download_exadata_infrastructure_config_file",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="exadata_infrastructure",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
