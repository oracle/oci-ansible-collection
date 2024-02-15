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
module: oci_compute_cloud_at_customer_ccc_infrastructure
short_description: Manage a CccInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CccInfrastructure resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a Compute Cloud@Customer infrastructure. Once created, Oracle Services
      must connect the rack in the data center to this Oracle Cloud Infrastructure resource.
    - "This resource has the following action operations in the M(oracle.oci.oci_compute_cloud_at_customer_ccc_infrastructure_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with
              the infrastructure.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The name that will be used to display the Compute Cloud@Customer infrastructure
              in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure.
              Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    subnet_id:
        description:
            - Identifier for network subnet that will be used to communicate with Compute Cloud@Customer infrastructure.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    connection_state:
        description:
            - The current connection state of the Compute Cloud@Customer infrastructure. This value
              will default to REJECT if the value is not provided. The only valid value at creation
              time is REJECT.
            - This parameter is updatable.
        type: str
    connection_details:
        description:
            - A message describing the current connection state in more detail.
            - This parameter is updatable.
        type: str
    ccc_upgrade_schedule_id:
        description:
            - Schedule used for upgrades. If no schedule is associated with the infrastructure,
              it can be upgraded at any time.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    ccc_infrastructure_id:
        description:
            - An L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for a
              Compute Cloud@Customer Infrastructure.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CccInfrastructure.
            - Use I(state=present) to create or update a CccInfrastructure.
            - Use I(state=absent) to delete a CccInfrastructure.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ccc_infrastructure
  oci_compute_cloud_at_customer_ccc_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    connection_state: connection_state_example
    connection_details: connection_details_example
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ccc_infrastructure
  oci_compute_cloud_at_customer_ccc_infrastructure:
    # required
    ccc_infrastructure_id: "ocid1.cccinfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    connection_state: connection_state_example
    connection_details: connection_details_example
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ccc_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_cloud_at_customer_ccc_infrastructure:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    connection_state: connection_state_example
    connection_details: connection_details_example
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete ccc_infrastructure
  oci_compute_cloud_at_customer_ccc_infrastructure:
    # required
    ccc_infrastructure_id: "ocid1.cccinfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ccc_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_cloud_at_customer_ccc_infrastructure:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient
    from oci.compute_cloud_at_customer.models import CreateCccInfrastructureDetails
    from oci.compute_cloud_at_customer.models import UpdateCccInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CccInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(CccInfrastructureHelperGen, self).get_possible_entity_types() + [
            "cccinfrastructure",
            "cccinfrastructures",
            "computeCloudAtCustomercccinfrastructure",
            "computeCloudAtCustomercccinfrastructures",
            "cccinfrastructureresource",
            "cccinfrastructuresresource",
            "computecloudatcustomer",
        ]

    def get_module_resource_id_param(self):
        return "ccc_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("ccc_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_ccc_infrastructure

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_infrastructure, ccc_infrastructure_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_infrastructure,
            ccc_infrastructure_id=self.module.params.get("ccc_infrastructure_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "ccc_infrastructure_id",
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
            self.client.list_ccc_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return CreateCccInfrastructureDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ccc_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ccc_infrastructure_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCccInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ccc_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ccc_infrastructure_id=self.module.params.get("ccc_infrastructure_id"),
                update_ccc_infrastructure_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ccc_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ccc_infrastructure_id=self.module.params.get("ccc_infrastructure_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CccInfrastructureHelperCustom = get_custom_class("CccInfrastructureHelperCustom")


class ResourceHelper(CccInfrastructureHelperCustom, CccInfrastructureHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            subnet_id=dict(type="str"),
            connection_state=dict(type="str"),
            connection_details=dict(type="str"),
            ccc_upgrade_schedule_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            ccc_infrastructure_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
