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
module: oci_compute_cloud_at_customer_ccc_infrastructure_actions
short_description: Perform actions on a CccInfrastructure resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CccInfrastructure resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Compute Cloud@Customer infrastructure resource from one compartment to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ccc_infrastructure_id:
        description:
            - An L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for a
              Compute Cloud@Customer Infrastructure.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the CccInfrastructure.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on ccc_infrastructure
  oci_compute_cloud_at_customer_ccc_infrastructure_actions:
    # required
    ccc_infrastructure_id: "ocid1.cccinfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
ccc_infrastructure:
    description:
        - Details of the CccInfrastructure resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Compute Cloud@Customer infrastructure L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
                  This cannot be changed once created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        short_name:
            description:
                - The Compute Cloud@Customer infrastructure short name.
                  This cannot be changed once created. The
                  short name is used to refer to the infrastructure in several contexts and is unique.
            returned: on success
            type: str
            sample: short_name_example
        display_name:
            description:
                - The name that will be used to display the Compute Cloud@Customer infrastructure
                  in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The infrastructure compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the network subnet that is
                  used to communicate with Compute Cloud@Customer infrastructure.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        connection_state:
            description:
                - The current connection state of the infrastructure. A user can only update
                  it from REQUEST to READY or from any state back to REJECT. The system automatically
                  handles the REJECT to REQUEST, READY to CONNECTED, or CONNECTED to DISCONNECTED transitions.
            returned: on success
            type: str
            sample: REJECT
        connection_details:
            description:
                - A message describing the current connection state in more detail.
            returned: on success
            type: str
            sample: connection_details_example
        ccc_upgrade_schedule_id:
            description:
                - Schedule used for upgrades. If no schedule is associated with the infrastructure,
                  it can be updated at any time.
            returned: on success
            type: str
            sample: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_fingerprint:
            description:
                - Fingerprint of a Compute Cloud@Customer infrastructure in a data center generated
                  during the initial connection to this resource. The fingerprint should be verified
                  by the administrator when changing the connectionState from REQUEST to READY.
            returned: on success
            type: str
            sample: provisioning_fingerprint_example
        provisioning_pin:
            description:
                - Code that is required for service personnel to connect a
                  Compute Cloud@Customer infrastructure in a data center to this resource.
                  This code will only be available when the connectionState is REJECT (usually
                  at create time of the Compute Cloud@Customer infrastructure).
            returned: on success
            type: str
            sample: provisioning_pin_example
        time_created:
            description:
                - Compute Cloud@Customer infrastructure creation date and time, using an RFC3339 formatted
                  datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Compute Cloud@Customer infrastructure updated date and time, using an RFC3339 formatted
                  datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Compute Cloud@Customer infrastructure.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current lifecycle state in more detail.
                  For example, this can be used to provide actionable information for a resource that is in
                  a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        infrastructure_inventory:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                serial_number:
                    description:
                        - The serial number of the Compute Cloud@Customer infrastructure rack.
                    returned: on success
                    type: str
                    sample: serial_number_example
                management_node_count:
                    description:
                        - The number of management nodes that are available and in active use
                          on the Compute Cloud@Customer infrastructure rack.
                    returned: on success
                    type: int
                    sample: 56
                compute_node_count:
                    description:
                        - The number of compute nodes that are available and usable
                          on the Compute Cloud@Customer infrastructure rack. There is no distinction
                          of compute node type in this information.
                    returned: on success
                    type: int
                    sample: 56
                capacity_storage_tray_count:
                    description:
                        - The number of storage trays in the Compute Cloud@Customer infrastructure rack that are designated for capacity storage.
                    returned: on success
                    type: int
                    sample: 56
                performance_storage_tray_count:
                    description:
                        - The number of storage trays in the Compute Cloud@Customer infrastructure rack that are designated for performance storage.
                    returned: on success
                    type: int
                    sample: 56
        infrastructure_network_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                management_nodes:
                    description:
                        - Information about the management nodes that are provisioned in the Compute Cloud@Customer
                          infrastructure.
                    returned: on success
                    type: complex
                    contains:
                        ip:
                            description:
                                - Address of the management node.
                            returned: on success
                            type: str
                            sample: ip_example
                        hostname:
                            description:
                                - Hostname for interface to the management node.
                            returned: on success
                            type: str
                            sample: hostname_example
                uplink_port_speed_in_gbps:
                    description:
                        - Uplink port speed defined in gigabytes per second.
                          All uplink ports must have identical speed.
                    returned: on success
                    type: int
                    sample: 56
                uplink_port_count:
                    description:
                        - Number of uplink ports per spine switch. Connectivity is identical on both spine switches.
                          For example, if input is two 100 gigabyte ports; then port-1 and port-2 on both spines will be configured.
                    returned: on success
                    type: int
                    sample: 56
                uplink_vlan_mtu:
                    description:
                        - The virtual local area network (VLAN) maximum transmission unit (MTU) size
                          for the uplink ports.
                    returned: on success
                    type: int
                    sample: 56
                uplink_netmask:
                    description:
                        - Netmask of the subnet that the Compute Cloud@Customer infrastructure is
                          connected to.
                    returned: on success
                    type: str
                    sample: uplink_netmask_example
                uplink_port_forward_error_correction:
                    description:
                        - The port forward error correction (FEC) setting for the uplink port on the
                          Compute Cloud@Customer infrastructure.
                    returned: on success
                    type: str
                    sample: AUTO
                uplink_domain:
                    description:
                        - Domain name to be used as the base domain for the internal network and by
                          public facing services.
                    returned: on success
                    type: str
                    sample: uplink_domain_example
                uplink_gateway_ip:
                    description:
                        - Uplink gateway in the datacenter network that the Compute Cloud@Customer
                          connects to.
                    returned: on success
                    type: str
                    sample: uplink_gateway_ip_example
                spine_ips:
                    description:
                        - Addresses of the network spine switches.
                    returned: on success
                    type: list
                    sample: []
                spine_vip:
                    description:
                        - The spine switch public virtual IP (VIP). Traffic routed to the
                          Compute Cloud@Customer infrastructure and
                          and virtual cloud networks (VCNs) should have this address as next hop.
                    returned: on success
                    type: str
                    sample: spine_vip_example
                mgmt_vip_hostname:
                    description:
                        - The hostname corresponding to the virtual IP (VIP) address of the management nodes.
                    returned: on success
                    type: str
                    sample: mgmt_vip_hostname_example
                mgmt_vip_ip:
                    description:
                        - The IP address used as the virtual IP (VIP) address of the management nodes.
                    returned: on success
                    type: str
                    sample: mgmt_vip_ip_example
                dns_ips:
                    description:
                        - The domain name system (DNS) addresses that the Compute Cloud@Customer infrastructure
                          uses for the data center network.
                    returned: on success
                    type: list
                    sample: []
                infrastructure_routing_static:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        uplink_vlan:
                            description:
                                - The virtual local area network (VLAN) identifier used to connect to the uplink
                                  (only access mode is supported).
                            returned: on success
                            type: int
                            sample: 56
                        uplink_hsrp_group:
                            description:
                                - The uplink Hot Standby Router Protocol (HSRP) group value for the switch in the
                                  Compute Cloud@Customer infrastructure.
                            returned: on success
                            type: int
                            sample: 56
                infrastructure_routing_dynamic:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        peer_information:
                            description:
                                - The list of peer devices in the dynamic routing configuration.
                            returned: on success
                            type: complex
                            contains:
                                asn:
                                    description:
                                        - The Autonomous System Number (ASN) of the peer network.
                                    returned: on success
                                    type: int
                                    sample: 56
                                ip:
                                    description:
                                        - Neighbor Border Gateway Protocal (BGP) IP address.
                                          The IP address usually refers to the customer data center router.
                                    returned: on success
                                    type: str
                                    sample: ip_example
                        oracle_asn:
                            description:
                                - The Oracle Autonomous System Number (ASN) to control routing and exchange information
                                  within the dynamic routing configuration.
                            returned: on success
                            type: int
                            sample: 56
                        bgp_topology:
                            description:
                                - The topology in use for the Border Gateway Protocol (BGP) configuration.
                            returned: on success
                            type: str
                            sample: TRIANGLE
        upgrade_information:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                current_version:
                    description:
                        - The current version of software installed on the Compute Cloud@Customer infrastructure.
                    returned: on success
                    type: str
                    sample: current_version_example
                time_of_scheduled_upgrade:
                    description:
                        - Compute Cloud@Customer infrastructure next upgrade time. The rack might have performance
                          impacts during this time.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                scheduled_upgrade_duration:
                    description:
                        - Expected duration of Compute Cloud@Customer infrastructure scheduled upgrade. The actual
                          upgrade time might be longer or shorter than this duration depending on rack activity, this
                          is only an estimate.
                    returned: on success
                    type: str
                    sample: scheduled_upgrade_duration_example
                is_active:
                    description:
                        - Indication that the Compute Cloud@Customer infrastructure is in the process of
                          an upgrade or an upgrade activity (such as preloading upgrade images).
                    returned: on success
                    type: bool
                    sample: true
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "short_name": "short_name_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_state": "REJECT",
        "connection_details": "connection_details_example",
        "ccc_upgrade_schedule_id": "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "provisioning_fingerprint": "provisioning_fingerprint_example",
        "provisioning_pin": "provisioning_pin_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "infrastructure_inventory": {
            "serial_number": "serial_number_example",
            "management_node_count": 56,
            "compute_node_count": 56,
            "capacity_storage_tray_count": 56,
            "performance_storage_tray_count": 56
        },
        "infrastructure_network_configuration": {
            "management_nodes": [{
                "ip": "ip_example",
                "hostname": "hostname_example"
            }],
            "uplink_port_speed_in_gbps": 56,
            "uplink_port_count": 56,
            "uplink_vlan_mtu": 56,
            "uplink_netmask": "uplink_netmask_example",
            "uplink_port_forward_error_correction": "AUTO",
            "uplink_domain": "uplink_domain_example",
            "uplink_gateway_ip": "uplink_gateway_ip_example",
            "spine_ips": [],
            "spine_vip": "spine_vip_example",
            "mgmt_vip_hostname": "mgmt_vip_hostname_example",
            "mgmt_vip_ip": "mgmt_vip_ip_example",
            "dns_ips": [],
            "infrastructure_routing_static": {
                "uplink_vlan": 56,
                "uplink_hsrp_group": 56
            },
            "infrastructure_routing_dynamic": {
                "peer_information": [{
                    "asn": 56,
                    "ip": "ip_example"
                }],
                "oracle_asn": 56,
                "bgp_topology": "TRIANGLE"
            }
        },
        "upgrade_information": {
            "current_version": "current_version_example",
            "time_of_scheduled_upgrade": "2013-10-20T19:20:30+01:00",
            "scheduled_upgrade_duration": "scheduled_upgrade_duration_example",
            "is_active": true
        },
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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient
    from oci.compute_cloud_at_customer.models import (
        ChangeCccInfrastructureCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CccInfrastructureActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "ccc_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("ccc_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_ccc_infrastructure

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_infrastructure,
            ccc_infrastructure_id=self.module.params.get("ccc_infrastructure_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCccInfrastructureCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_ccc_infrastructure_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ccc_infrastructure_id=self.module.params.get("ccc_infrastructure_id"),
                change_ccc_infrastructure_compartment_details=action_details,
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


CccInfrastructureActionsHelperCustom = get_custom_class(
    "CccInfrastructureActionsHelperCustom"
)


class ResourceHelper(
    CccInfrastructureActionsHelperCustom, CccInfrastructureActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            ccc_infrastructure_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ccc_infrastructure",
        service_client_class=ComputeCloudAtCustomerClient,
        namespace="compute_cloud_at_customer",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
