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
module: oci_compute_cloud_at_customer_ccc_infrastructure_facts
short_description: Fetches details about one or multiple CccInfrastructure resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CccInfrastructure resources in Oracle Cloud Infrastructure
    - Returns a list of Compute Cloud@Customer infrastructures.
    - If I(ccc_infrastructure_id) is specified, the details of a single CccInfrastructure will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to
              list resources.
        type: str
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and
              sub-compartments in the tenancy are returned. Depends on the 'accessLevel' setting.
        type: bool
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no
              partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    lifecycle_state:
        description:
            - A filter used to return only resources that match the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return only resources whose display name contains the substring.
        type: str
    ccc_infrastructure_id:
        description:
            - An L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for a
              Compute Cloud@Customer Infrastructure.
            - Required to get a specific ccc_infrastructure.
        type: str
        aliases: ["id"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ccc_infrastructure
  oci_compute_cloud_at_customer_ccc_infrastructure_facts:
    # required
    ccc_infrastructure_id: "ocid1.cccinfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

- name: List ccc_infrastructures
  oci_compute_cloud_at_customer_ccc_infrastructure_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    lifecycle_state: ACTIVE
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    ccc_infrastructure_id: "ocid1.cccinfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
ccc_infrastructures:
    description:
        - List of CccInfrastructure resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure.
                  Avoid entering confidential information.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        connection_details:
            description:
                - A message describing the current connection state in more detail.
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_details_example
        ccc_upgrade_schedule_id:
            description:
                - Schedule used for upgrades. If no schedule is associated with the infrastructure,
                  it can be updated at any time.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_fingerprint:
            description:
                - Fingerprint of a Compute Cloud@Customer infrastructure in a data center generated
                  during the initial connection to this resource. The fingerprint should be verified
                  by the administrator when changing the connectionState from REQUEST to READY.
                - Returned for get operation
            returned: on success
            type: str
            sample: provisioning_fingerprint_example
        provisioning_pin:
            description:
                - Code that is required for service personnel to connect a
                  Compute Cloud@Customer infrastructure in a data center to this resource.
                  This code will only be available when the connectionState is REJECT (usually
                  at create time of the Compute Cloud@Customer infrastructure).
                - Returned for get operation
            returned: on success
            type: str
            sample: provisioning_pin_example
        time_updated:
            description:
                - Compute Cloud@Customer infrastructure updated date and time, using an RFC3339 formatted
                  datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current lifecycle state in more detail.
                  For example, this can be used to provide actionable information for a resource that is in
                  a Failed state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        infrastructure_inventory:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
        time_created:
            description:
                - Compute Cloud@Customer infrastructure creation date and time, using an RFC3339 formatted
                  datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        connection_state:
            description:
                - The current connection state of the infrastructure. A user can only update
                  it from REQUEST to READY or from any state back to REJECT. The system automatically
                  handles the REJECT to REQUEST, READY to CONNECTED, or CONNECTED to DISCONNECTED transitions.
            returned: on success
            type: str
            sample: REJECT
        lifecycle_state:
            description:
                - The current state of the Compute Cloud@Customer infrastructure.
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: [{
        "description": "description_example",
        "connection_details": "connection_details_example",
        "ccc_upgrade_schedule_id": "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "provisioning_fingerprint": "provisioning_fingerprint_example",
        "provisioning_pin": "provisioning_pin_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "short_name": "short_name_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "connection_state": "REJECT",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CccInfrastructureFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "ccc_infrastructure_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_infrastructure,
            ccc_infrastructure_id=self.module.params.get("ccc_infrastructure_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "compartment_id_in_subtree",
            "access_level",
            "lifecycle_state",
            "display_name",
            "display_name_contains",
            "ccc_infrastructure_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ccc_infrastructures, **optional_kwargs
        )


CccInfrastructureFactsHelperCustom = get_custom_class(
    "CccInfrastructureFactsHelperCustom"
)


class ResourceFactsHelper(
    CccInfrastructureFactsHelperCustom, CccInfrastructureFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            ccc_infrastructure_id=dict(aliases=["id"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ccc_infrastructure",
        service_client_class=ComputeCloudAtCustomerClient,
        namespace="compute_cloud_at_customer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(ccc_infrastructures=result)


if __name__ == "__main__":
    main()
