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
module: oci_database_exadata_infrastructure
short_description: Manage an ExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only.
      To create an Exadata Cloud Service infrastructure resource, use the  L(CreateCloudExadataInfrastructure,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudExadataInfrastructure/CreateCloudExadataInfrastructure) operation.
    - "This resource has the following action operations in the M(oci_exadata_infrastructure_actions) module: activate,
      download_exadata_infrastructure_config_file."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly name for the Exadata infrastructure. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    shape:
        description:
            - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            - Required for create using I(state=present).
        type: str
    time_zone:
        description:
            - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    cloud_control_plane_server1:
        description:
            - The IP address for the first control plane server.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    cloud_control_plane_server2:
        description:
            - The IP address for the second control plane server.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    netmask:
        description:
            - The netmask for the control plane network.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    gateway:
        description:
            - The gateway for the control plane network.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    admin_network_cidr:
        description:
            - The CIDR block for the Exadata administration network.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    infini_band_network_cidr:
        description:
            - The CIDR block for the Exadata InfiniBand interconnect.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    corporate_proxy:
        description:
            - The corporate network proxy for access to the control plane network. Oracle recommends using an HTTPS proxy when possible
              for enhanced security.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    contacts:
        description:
            - The list of contacts for the Exadata infrastructure.
            - This parameter is updatable.
        type: list
        suboptions:
            name:
                description:
                    - The name of the Exadata Infrastructure contact.
                type: str
                required: true
            phone_number:
                description:
                    - The phone number for the Exadata Infrastructure contact.
                type: str
            email:
                description:
                    - The email for the Exadata Infrastructure contact.
                type: str
                required: true
            is_primary:
                description:
                    - If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.
                type: bool
                required: true
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
            months:
                description:
                    - Months during the year when maintenance should be performed.
                type: list
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
            days_of_week:
                description:
                    - Days during the week when maintenance should be performed.
                type: list
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
            lead_time_in_weeks:
                description:
                    - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.
                type: int
    dns_server:
        description:
            - The list of DNS server IP addresses. Maximum of 3 allowed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
    ntp_server:
        description:
            - The list of NTP server IP addresses. Maximum of 3 allowed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
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
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExadataInfrastructure.
            - Use I(state=present) to create or update an ExadataInfrastructure.
            - Use I(state=absent) to delete an ExadataInfrastructure.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create exadata_infrastructure
  oci_database_exadata_infrastructure:
    compartment_id: "ocid1.tenancy.oc1.unique_ID"
    display_name: "tstExaInfra"
    shape: "Exadata.Full2.336"
    time_zone: "PST"
    cloud_control_plane_server1: "192.168.19.1"
    cloud_control_plane_server2: "192.168.19.2"
    netmask: "255.255.0.0"
    gateway: "192.168.20.1"
    admin_network_cidr: "192.168.19.2/16"
    infini_band_network_cidr: "10.172.19.1/24"
    corporate_proxy: "192.168.20.1"
    dns_server:
    - "192.168.10.10"
    ntp_server:
    - "192.168.10.20"

- name: Update exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_exadata_infrastructure:
    admin_network_cidr: "192.168.19.1/16"
    infini_band_network_cidr: "10.172.19.2/24"

- name: Update exadata_infrastructure
  oci_database_exadata_infrastructure:
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete exadata_infrastructure
  oci_database_exadata_infrastructure:
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_exadata_infrastructure:
    compartment_id: ocid1.tenancy.oc1.unique_ID
    display_name: tstExaInfra
    state: absent

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
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the Exadata infrastructure.
            returned: on success
            type: string
            sample: CREATING
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: string
            sample: shape_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: string
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
        cloud_control_plane_server1:
            description:
                - The IP address for the first control plane server.
            returned: on success
            type: string
            sample: cloud_control_plane_server1_example
        cloud_control_plane_server2:
            description:
                - The IP address for the second control plane server.
            returned: on success
            type: string
            sample: cloud_control_plane_server2_example
        netmask:
            description:
                - The netmask for the control plane network.
            returned: on success
            type: string
            sample: netmask_example
        gateway:
            description:
                - The gateway for the control plane network.
            returned: on success
            type: string
            sample: gateway_example
        admin_network_cidr:
            description:
                - The CIDR block for the Exadata administration network.
            returned: on success
            type: string
            sample: admin_network_cidr_example
        infini_band_network_cidr:
            description:
                - The CIDR block for the Exadata InfiniBand interconnect.
            returned: on success
            type: string
            sample: infini_band_network_cidr_example
        corporate_proxy:
            description:
                - The corporate network proxy for access to the control plane network.
            returned: on success
            type: string
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
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        csi_number:
            description:
                - The CSI Number of the Exadata infrastructure.
            returned: on success
            type: string
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
                    type: string
                    sample: name_example
                phone_number:
                    description:
                        - The phone number for the Exadata Infrastructure contact.
                    returned: on success
                    type: string
                    sample: phone_number_example
                email:
                    description:
                        - The email for the Exadata Infrastructure contact.
                    returned: on success
                    type: string
                    sample: email_example
                is_primary:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.
                    returned: on success
                    type: bool
                    sample: true
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
                    type: string
                    sample: NO_PREFERENCE
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
                            type: string
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
                            type: string
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
            "is_primary": true
        }],
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
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
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.database.models import CreateExadataInfrastructureDetails
    from oci.database.models import UpdateExadataInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ExadataInfrastructureHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
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
            self.client.list_exadata_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return CreateExadataInfrastructureDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(create_exadata_infrastructure_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExadataInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                update_exadata_infrastructure_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExadataInfrastructureHelperCustom = get_custom_class(
    "ExadataInfrastructureHelperCustom"
)


class ResourceHelper(ExadataInfrastructureHelperCustom, ExadataInfrastructureHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            shape=dict(type="str"),
            time_zone=dict(type="str"),
            cloud_control_plane_server1=dict(type="str"),
            cloud_control_plane_server2=dict(type="str"),
            netmask=dict(type="str"),
            gateway=dict(type="str"),
            admin_network_cidr=dict(type="str"),
            infini_band_network_cidr=dict(type="str"),
            corporate_proxy=dict(type="str"),
            contacts=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    phone_number=dict(type="str"),
                    email=dict(type="str", required=True),
                    is_primary=dict(type="bool", required=True),
                ),
            ),
            maintenance_window=dict(
                type="dict",
                options=dict(
                    preference=dict(
                        type="str",
                        required=True,
                        choices=["NO_PREFERENCE", "CUSTOM_PREFERENCE"],
                    ),
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
                    weeks_of_month=dict(type="list"),
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
                    hours_of_day=dict(type="list"),
                    lead_time_in_weeks=dict(type="int"),
                ),
            ),
            dns_server=dict(type="list"),
            ntp_server=dict(type="list"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="exadata_infrastructure",
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
