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
module: oci_database_vm_cluster_network
short_description: Manage a VmClusterNetwork resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VmClusterNetwork resource in Oracle Cloud Infrastructure
    - For I(state=present), creates the VM cluster network. Applies to Exadata Cloud@Customer instances only.
      To create a cloud VM cluster in an Exadata Cloud Service instance, use the L(CreateCloudVmCluster ,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudVmCluster/CreateCloudVmCluster) operation.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_vm_cluster_network_actions) module: add_dbserver_network,
      remove_dbserver_network."
version_added: "2.9.0"
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
            - The user-friendly name for the Exadata Cloud@Customer VM cluster network. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    scans:
        description:
            - The SCAN details.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            hostname:
                description:
                    - The SCAN hostname.
                type: str
                required: true
            port:
                description:
                    - "**Deprecated.** This field is deprecated. You may use 'scanListenerPortTcp' to specify the port.
                      The SCAN TCPIP port. Default is 1521."
                type: int
            scan_listener_port_tcp:
                description:
                    - The SCAN TCPIP port. Default is 1521.
                type: int
            scan_listener_port_tcp_ssl:
                description:
                    - The SCAN TCPIP SSL port. Default is 2484.
                type: int
            ips:
                description:
                    - The list of SCAN IP addresses. Three addresses should be provided.
                type: list
                elements: str
                required: true
    dns:
        description:
            - The list of DNS server IP addresses. Maximum of 3 allowed.
            - This parameter is updatable.
        type: list
        elements: str
    ntp:
        description:
            - The list of NTP server IP addresses. Maximum of 3 allowed.
            - This parameter is updatable.
        type: list
        elements: str
    vm_networks:
        description:
            - Details of the client and backup networks.
            - Required for create using I(state=present).
            - This parameter is updatable.
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
    dr_scans:
        description:
            - The SCAN details for DR network
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            hostname:
                description:
                    - The Disaster recovery SCAN hostname.
                type: str
                required: true
            scan_listener_port_tcp:
                description:
                    - The Disaster recovery SCAN TCPIP port. Default is 1521.
                type: int
                required: true
            ips:
                description:
                    - The list of Disaster recovery SCAN IP addresses. Three addresses should be provided.
                type: list
                elements: str
                required: true
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
        type: str
        required: true
    vm_cluster_network_id:
        description:
            - The VM cluster network L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VmClusterNetwork.
            - Use I(state=present) to create or update a VmClusterNetwork.
            - Use I(state=absent) to delete a VmClusterNetwork.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vm_cluster_network
  oci_database_vm_cluster_network:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    scans:
    - # required
      hostname: hostname_example
      ips: [ "ips_example" ]

      # optional
      port: 56
      scan_listener_port_tcp: 56
      scan_listener_port_tcp_ssl: 56
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

    # optional
    dns: [ "dns_example" ]
    ntp: [ "ntp_example" ]
    dr_scans:
    - # required
      hostname: hostname_example
      scan_listener_port_tcp: 56
      ips: [ "ips_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update vm_cluster_network
  oci_database_vm_cluster_network:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    scans:
    - # required
      hostname: hostname_example
      ips: [ "ips_example" ]

      # optional
      port: 56
      scan_listener_port_tcp: 56
      scan_listener_port_tcp_ssl: 56
    dns: [ "dns_example" ]
    ntp: [ "ntp_example" ]
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
    dr_scans:
    - # required
      hostname: hostname_example
      scan_listener_port_tcp: 56
      ips: [ "ips_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update vm_cluster_network using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_vm_cluster_network:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    scans:
    - # required
      hostname: hostname_example
      ips: [ "ips_example" ]

      # optional
      port: 56
      scan_listener_port_tcp: 56
      scan_listener_port_tcp_ssl: 56
    dns: [ "dns_example" ]
    ntp: [ "ntp_example" ]
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
    dr_scans:
    - # required
      hostname: hostname_example
      scan_listener_port_tcp: 56
      ips: [ "ips_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete vm_cluster_network
  oci_database_vm_cluster_network:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete vm_cluster_network using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_vm_cluster_network:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import VmClusterNetworkDetails
    from oci.database.models import UpdateVmClusterNetworkDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VmClusterNetworkHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(VmClusterNetworkHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(VmClusterNetworkHelperGen, self).get_possible_entity_types() + [
            "vmclusternetwork",
            "vmclusternetworks",
            "databasevmclusternetwork",
            "databasevmclusternetworks",
            "vmclusternetworkresource",
            "vmclusternetworksresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "vm_cluster_network_id"

    def get_module_resource_id(self):
        return self.module.params.get("vm_cluster_network_id")

    def get_get_fn(self):
        return self.client.get_vm_cluster_network

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster_network,
            vm_cluster_network_id=summary_model.id,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster_network,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "exadata_infrastructure_id",
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
            self.client.list_vm_cluster_networks, **kwargs
        )

    def get_create_model_class(self):
        return VmClusterNetworkDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vm_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateVmClusterNetworkDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vm_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
                update_vm_cluster_network_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vm_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
                vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VmClusterNetworkHelperCustom = get_custom_class("VmClusterNetworkHelperCustom")


class ResourceHelper(VmClusterNetworkHelperCustom, VmClusterNetworkHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            scans=dict(
                type="list",
                elements="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    port=dict(type="int"),
                    scan_listener_port_tcp=dict(type="int"),
                    scan_listener_port_tcp_ssl=dict(type="int"),
                    ips=dict(type="list", elements="str", required=True),
                ),
            ),
            dns=dict(type="list", elements="str"),
            ntp=dict(type="list", elements="str"),
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
            dr_scans=dict(
                type="list",
                elements="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    scan_listener_port_tcp=dict(type="int", required=True),
                    ips=dict(type="list", elements="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            exadata_infrastructure_id=dict(type="str", required=True),
            vm_cluster_network_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
