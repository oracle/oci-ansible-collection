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
module: oci_database_vm_cluster_network_actions
short_description: Perform actions on a VmClusterNetwork resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VmClusterNetwork resource in Oracle Cloud Infrastructure
    - For I(action=download_validation_report), downloads the network validation report file for the specified VM cluster network. Applies to Exadata
      Cloud@Customer instances only.
    - For I(action=download_vm_cluster_network_config_file), downloads the configuration file for the specified VM cluster network. Applies to Exadata
      Cloud@Customer instances only.
    - For I(action=resize), adds or removes Db server network nodes to extend or shrink the existing VM cluster network. Applies to Exadata
      Cloud@Customer instances only.
    - For I(action=validate), validates the specified VM cluster network. Applies to Exadata Cloud@Customer instances only.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    validation_report_dest:
        description:
            - The destination file path to write the report to when I(action=download_validation_report). The file will be created if it does not exist. If the
              file already exists, the content will be overwritten. I(validation_report_dest) is required if I(action=download_validation_report).
            - Required for I(action=download_validation_report).
        type: str
    config_file_dest:
        description:
            - The destination file path to write the config file to when I(action=download_vm_cluster_network_config_file). The file will be created if it does
              not exist. If the file already exists, the content will be overwritten. I(config_file_dest) is required if
              I(action=download_vm_cluster_network_config_file).
            - Required for I(action=download_vm_cluster_network_config_file).
        type: str
    action:
        description:
            - The action to perform on the VmClusterNetwork.
        type: str
        required: true
        choices:
            - "download_validation_report"
            - "download_vm_cluster_network_config_file"
            - "add_dbserver_network"
            - "remove_dbserver_network"
            - "validate"
    vm_networks:
        description:
            - Details of the client and backup networks.
            - Required for I(action=resize).
        type: list
        elements: dict
        suboptions:
            vlan_id:
                description:
                    - The network VLAN ID.
                type: str
            network_type:
                description:
                    - The network type.
                type: str
                choices:
                    - "CLIENT"
                    - "BACKUP"
                    - "DISASTER_RECOVERY"
                required: true
            netmask:
                description:
                    - The network netmask.
                type: str
            gateway:
                description:
                    - The network gateway.
                type: str
            domain_name:
                description:
                    - The network domain name.
                type: str
            nodes:
                description:
                    - The list of node details.
                type: list
                elements: dict
                required: true
                suboptions:
                    hostname:
                        description:
                            - The node host name.
                        type: str
                        required: true
                    ip:
                        description:
                            - The node IP address.
                        type: str
                        required: true
                    vip_hostname:
                        description:
                            - The node virtual IP (VIP) host name.
                        type: str
                    vip:
                        description:
                            - The node virtual IP (VIP) address.
                        type: str
                    lifecycle_state:
                        description:
                            - "The current state of the VM cluster network nodes.
                              CREATING - The resource is being created
                              REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
                              VALIDATING - The resource is being validated and not available to use.
                              VALIDATED - The resource is validated and is available for consumption by VM cluster.
                              VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
                              UPDATING - The resource is being updated and not available to use.
                              ALLOCATED - The resource is currently being used by VM cluster.
                              TERMINATING - The resource is being deleted and not available to use.
                              TERMINATED - The resource is deleted and unavailable.
                              FAILED - The resource is in a failed state due to validation or other errors."
                        type: str
                        choices:
                            - "CREATING"
                            - "REQUIRES_VALIDATION"
                            - "VALIDATING"
                            - "VALIDATED"
                            - "VALIDATION_FAILED"
                            - "UPDATING"
                            - "ALLOCATED"
                            - "TERMINATING"
                            - "TERMINATED"
                            - "FAILED"
                    db_server_id:
                        description:
                            - The Db server associated with the node.
                        type: str
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    vm_cluster_network_id:
        description:
            - The VM cluster network L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action download_validation_report on vm_cluster_network
  oci_database_vm_cluster_network_actions:
    # required
    validation_report_dest: /tmp/exadata_validation_report
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
    action: download_validation_report

- name: Perform action download_vm_cluster_network_config_file on vm_cluster_network
  oci_database_vm_cluster_network_actions:
    # required
    config_file_dest: /tmp/exadata_config_file.zip
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
    action: download_vm_cluster_network_config_file

- name: Perform action add_dbserver_network on vm_cluster_network
  oci_database_vm_cluster_network_actions:
    # required
    action: ADD_DBSERVER_NETWORK
    vm_networks:
    - # required
      network_type: CLIENT
      nodes:
      - # required
        hostname: hostname_example
        ip: ip_example

        # optional
        vip_hostname: vip_hostname_example
        vip: vip_example
        lifecycle_state: CREATING
        db_server_id: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      vlan_id: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
      netmask: netmask_example
      gateway: gateway_example
      domain_name: domain_name_example
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action remove_dbserver_network on vm_cluster_network
  oci_database_vm_cluster_network_actions:
    # required
    action: ADD_DBSERVER_NETWORK
    vm_networks:
    - # required
      network_type: CLIENT
      nodes:
      - # required
        hostname: hostname_example
        ip: ip_example

        # optional
        vip_hostname: vip_hostname_example
        vip: vip_example
        lifecycle_state: CREATING
        db_server_id: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      vlan_id: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
      netmask: netmask_example
      gateway: gateway_example
      domain_name: domain_name_example
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action validate on vm_cluster_network
  oci_database_vm_cluster_network_actions:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
    action: validate

"""

RETURN = """
vm_cluster_network:
    description:
        - Details of the VmClusterNetwork resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster network.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated VM Cluster.
            returned: on success
            type: str
            sample: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the VM cluster network. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        scans:
            description:
                - The SCAN details.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The SCAN hostname.
                    returned: on success
                    type: str
                    sample: hostname_example
                port:
                    description:
                        - "**Deprecated.** This field is deprecated. You may use 'scanListenerPortTcp' to specify the port.
                          The SCAN TCPIP port. Default is 1521."
                    returned: on success
                    type: int
                    sample: 56
                scan_listener_port_tcp:
                    description:
                        - The SCAN TCPIP port. Default is 1521.
                    returned: on success
                    type: int
                    sample: 56
                scan_listener_port_tcp_ssl:
                    description:
                        - The SCAN TCPIP SSL port. Default is 2484.
                    returned: on success
                    type: int
                    sample: 56
                ips:
                    description:
                        - The list of SCAN IP addresses. Three addresses should be provided.
                    returned: on success
                    type: list
                    sample: []
        dns:
            description:
                - The list of DNS server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        ntp:
            description:
                - The list of NTP server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        vm_networks:
            description:
                - Details of the client and backup networks.
            returned: on success
            type: complex
            contains:
                vlan_id:
                    description:
                        - The network VLAN ID.
                    returned: on success
                    type: str
                    sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                network_type:
                    description:
                        - The network type.
                    returned: on success
                    type: str
                    sample: CLIENT
                netmask:
                    description:
                        - The network netmask.
                    returned: on success
                    type: str
                    sample: netmask_example
                gateway:
                    description:
                        - The network gateway.
                    returned: on success
                    type: str
                    sample: gateway_example
                domain_name:
                    description:
                        - The network domain name.
                    returned: on success
                    type: str
                    sample: domain_name_example
                nodes:
                    description:
                        - The list of node details.
                    returned: on success
                    type: complex
                    contains:
                        hostname:
                            description:
                                - The node host name.
                            returned: on success
                            type: str
                            sample: hostname_example
                        ip:
                            description:
                                - The node IP address.
                            returned: on success
                            type: str
                            sample: ip_example
                        vip_hostname:
                            description:
                                - The node virtual IP (VIP) host name.
                            returned: on success
                            type: str
                            sample: vip_hostname_example
                        vip:
                            description:
                                - The node virtual IP (VIP) address.
                            returned: on success
                            type: str
                            sample: vip_example
                        lifecycle_state:
                            description:
                                - "The current state of the VM cluster network nodes.
                                  CREATING - The resource is being created
                                  REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
                                  VALIDATING - The resource is being validated and not available to use.
                                  VALIDATED - The resource is validated and is available for consumption by VM cluster.
                                  VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
                                  UPDATING - The resource is being updated and not available to use.
                                  ALLOCATED - The resource is currently being used by VM cluster.
                                  TERMINATING - The resource is being deleted and not available to use.
                                  TERMINATED - The resource is deleted and unavailable.
                                  FAILED - The resource is in a failed state due to validation or other errors."
                            returned: on success
                            type: str
                            sample: CREATING
                        db_server_id:
                            description:
                                - The Db server associated with the node.
                            returned: on success
                            type: str
                            sample: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
        dr_scans:
            description:
                - The SCAN details for DR network
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The Disaster recovery SCAN hostname.
                    returned: on success
                    type: str
                    sample: hostname_example
                scan_listener_port_tcp:
                    description:
                        - The Disaster recovery SCAN TCPIP port. Default is 1521.
                    returned: on success
                    type: int
                    sample: 56
                ips:
                    description:
                        - The list of Disaster recovery SCAN IP addresses. Three addresses should be provided.
                    returned: on success
                    type: list
                    sample: []
        lifecycle_state:
            description:
                - "The current state of the VM cluster network.
                  CREATING - The resource is being created
                  REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
                  VALIDATING - The resource is being validated and not available to use.
                  VALIDATED - The resource is validated and is available for consumption by VM cluster.
                  VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
                  UPDATING - The resource is being updated and not available to use.
                  ALLOCATED - The resource is is currently being used by VM cluster.
                  TERMINATING - The resource is being deleted and not available to use.
                  TERMINATED - The resource is deleted and unavailable.
                  FAILED - The resource is in a failed state due to validation or other errors.
                  NEEDS_ATTENTION - The resource is in needs attention state as some of it's child nodes are not validated
                                    and unusable by VM cluster."
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time when the VM cluster network was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
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
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "scans": [{
            "hostname": "hostname_example",
            "port": 56,
            "scan_listener_port_tcp": 56,
            "scan_listener_port_tcp_ssl": 56,
            "ips": []
        }],
        "dns": [],
        "ntp": [],
        "vm_networks": [{
            "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
            "network_type": "CLIENT",
            "netmask": "netmask_example",
            "gateway": "gateway_example",
            "domain_name": "domain_name_example",
            "nodes": [{
                "hostname": "hostname_example",
                "ip": "ip_example",
                "vip_hostname": "vip_hostname_example",
                "vip": "vip_example",
                "lifecycle_state": "CREATING",
                "db_server_id": "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }],
        "dr_scans": [{
            "hostname": "hostname_example",
            "scan_listener_port_tcp": 56,
            "ips": []
        }],
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.database.models import ResizeVmClusterNetworkDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VmClusterNetworkActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        download_validation_report
        download_vm_cluster_network_config_file
        resize
        validate
    """

    def __init__(self, *args, **kwargs):
        super(VmClusterNetworkActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "vm_cluster_network_id"

    def get_module_resource_id(self):
        return self.module.params.get("vm_cluster_network_id")

    def get_get_fn(self):
        return self.client.get_vm_cluster_network

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster_network,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
        )

    def get_action_fn(self, action):
        action = action.lower()
        if action in [
            "add_dbserver_network",
            "remove_dbserver_network",
        ]:
            self.module.params["action"] = action.upper()
            return getattr(self, "resize", None)
        return super(VmClusterNetworkActionsHelperGen, self).get_action_fn(action)

    def download_validation_report(self):
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.download_validation_report,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
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
        dest = self.module.params.get("validation_report_dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None

    def download_vm_cluster_network_config_file(self):
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.download_vm_cluster_network_config_file,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
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

    def resize(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResizeVmClusterNetworkDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resize_vm_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
                resize_vm_cluster_network_details=action_details,
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

    def validate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_vm_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
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


VmClusterNetworkActionsHelperCustom = get_custom_class(
    "VmClusterNetworkActionsHelperCustom"
)


class ResourceHelper(
    VmClusterNetworkActionsHelperCustom, VmClusterNetworkActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            validation_report_dest=dict(type="str"),
            config_file_dest=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "download_validation_report",
                    "download_vm_cluster_network_config_file",
                    "add_dbserver_network",
                    "remove_dbserver_network",
                    "validate",
                ],
            ),
            vm_networks=dict(
                type="list",
                elements="dict",
                options=dict(
                    vlan_id=dict(type="str"),
                    network_type=dict(
                        type="str",
                        required=True,
                        choices=["CLIENT", "BACKUP", "DISASTER_RECOVERY"],
                    ),
                    netmask=dict(type="str"),
                    gateway=dict(type="str"),
                    domain_name=dict(type="str"),
                    nodes=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            hostname=dict(type="str", required=True),
                            ip=dict(type="str", required=True),
                            vip_hostname=dict(type="str"),
                            vip=dict(type="str"),
                            lifecycle_state=dict(
                                type="str",
                                choices=[
                                    "CREATING",
                                    "REQUIRES_VALIDATION",
                                    "VALIDATING",
                                    "VALIDATED",
                                    "VALIDATION_FAILED",
                                    "UPDATING",
                                    "ALLOCATED",
                                    "TERMINATING",
                                    "TERMINATED",
                                    "FAILED",
                                ],
                            ),
                            db_server_id=dict(type="str"),
                        ),
                    ),
                ),
            ),
            exadata_infrastructure_id=dict(type="str", required=True),
            vm_cluster_network_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vm_cluster_network",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
