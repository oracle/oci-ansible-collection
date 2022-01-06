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
module: oci_database_vm_cluster_network_facts
short_description: Fetches details about one or multiple VmClusterNetwork resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VmClusterNetwork resources in Oracle Cloud Infrastructure
    - Gets a list of the VM cluster networks in the specified compartment. Applies to Exadata Cloud@Customer instances only.
    - If I(vm_cluster_network_id) is specified, the details of a single VmClusterNetwork will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    vm_cluster_network_id:
        description:
            - The VM cluster network L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific vm_cluster_network.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple vm_cluster_networks.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
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
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vm_cluster_network
  oci_database_vm_cluster_network_facts:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vm_cluster_networks
  oci_database_vm_cluster_network_facts:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: CREATING
    display_name: display_name_example

"""

RETURN = """
vm_cluster_networks:
    description:
        - List of VmClusterNetwork resources
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
                        - The SCAN TCPIP port. Default is 1521.
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
                - The current state of the VM cluster network.
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
    sample: [{
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
                "vip": "vip_example"
            }]
        }],
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VmClusterNetworkFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "exadata_infrastructure_id",
            "vm_cluster_network_id",
        ]

    def get_required_params_for_list(self):
        return [
            "exadata_infrastructure_id",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster_network,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vm_cluster_networks,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VmClusterNetworkFactsHelperCustom = get_custom_class(
    "VmClusterNetworkFactsHelperCustom"
)


class ResourceFactsHelper(
    VmClusterNetworkFactsHelperCustom, VmClusterNetworkFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            exadata_infrastructure_id=dict(type="str", required=True),
            vm_cluster_network_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
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
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vm_cluster_network",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vm_cluster_networks=result)


if __name__ == "__main__":
    main()
