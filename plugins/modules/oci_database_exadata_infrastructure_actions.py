#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
    - For I(action=activate), activates the specified Exadata infrastructure.
    - For I(action=download_exadata_infrastructure_config_file), downloads the configuration file for the specified Exadata infrastructure.
version_added: "2.9"
author: Oracle (@oracle)
options:
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    activation_file:
        description:
            - "The base 64 encoded contents of the activation zip file. You can use the ansible 'lookup' and 'b64encode' functionality to read a file and base
              64 encode its contents. For example: {{ lookup('file', 'activation.zip') | b64encode }}"
            - Required for I(action=activate).
        type: str
    config_file_dest:
        description:
            - The destination file path to write the config file to when I(action=download_exadata_infrastructure_config_file). The file will be created if it
              does not exist. If the file already exists, the content will be overwritten. I(config_file_dest) is required if
              I(action=download_exadata_infrastructure_config_file).
        type: str
    action:
        description:
            - The action to perform on the ExadataInfrastructure.
        type: str
        required: true
        choices:
            - "activate"
            - "download_exadata_infrastructure_config_file"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on exadata_infrastructure
  oci_database_exadata_infrastructure_actions:
    exadata_infrastructure_id: ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx
    action: activate

- name: Perform action download_exadata_infrastructure_config_file on exadata_infrastructure
  oci_database_exadata_infrastructure_actions:
    exadata_infrastructure_id: ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current lifecycle state of the Exadata infrastructure.
            returned: on success
            type: string
            sample: CREATING
        display_name:
            description:
                - The user-friendly name for the Exadata infrastructure. The name does not need to be unique.
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ActivateExadataInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
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

    def download_exadata_infrastructure_config_file(self):
        return oci_wait_utils.call_and_wait(
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
            exadata_infrastructure_id=dict(aliases=["id"], type="str", required=True),
            activation_file=dict(type="str"),
            config_file_dest=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["activate", "download_exadata_infrastructure_config_file"],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
