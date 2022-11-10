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
module: oci_compute_management_cluster_network_facts
short_description: Fetches details about one or multiple ClusterNetwork resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ClusterNetwork resources in Oracle Cloud Infrastructure
    - Lists the cluster networks in the specified compartment.
    - If I(cluster_network_id) is specified, the details of a single ClusterNetwork will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cluster_network_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.
            - Required to get a specific cluster_network.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple cluster_networks.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle
              state. The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "SCALING"
            - "STARTING"
            - "STOPPING"
            - "TERMINATING"
            - "STOPPED"
            - "TERMINATED"
            - "RUNNING"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cluster_network
  oci_compute_management_cluster_network_facts:
    # required
    cluster_network_id: "ocid1.clusternetwork.oc1..xxxxxxEXAMPLExxxxxx"

- name: List cluster_networks
  oci_compute_management_cluster_network_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING

"""

RETURN = """
cluster_networks:
    description:
        - List of ClusterNetwork resources
    returned: on success
    type: complex
    contains:
        placement_configuration:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                availability_domain:
                    description:
                        - The availability domain to place instances.
                        - "Example: `Uocm:PHX-AD-1`"
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                primary_subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet to place
                          instances.
                    returned: on success
                    type: str
                    sample: "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx"
                secondary_vnic_subnets:
                    description:
                        - The set of secondary VNIC data for instances in the pool.
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - The display name of the VNIC. This is also use to match against the instance configuration defined
                                  secondary VNIC.
                            returned: on success
                            type: str
                            sample: display_name_example
                        subnet_id:
                            description:
                                - The subnet L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the cluster network.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        instance_pools:
            description:
                - The instance pools in the cluster network.
                - Each cluster network can have one instance pool.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the instance
                          pool.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                defined_tags:
                    description:
                        - Defined tags for this resource. Each key is predefined and scoped to a
                          namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                freeform_tags:
                    description:
                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                          predefined name, type, or namespace. For more information, see L(Resource
                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                instance_configuration_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration associated
                          with the instance pool.
                    returned: on success
                    type: str
                    sample: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the instance pool.
                    returned: on success
                    type: str
                    sample: PROVISIONING
                placement_configurations:
                    description:
                        - The placement configurations for the instance pool.
                    returned: on success
                    type: complex
                    contains:
                        availability_domain:
                            description:
                                - The availability domain to place instances.
                                - "Example: `Uocm:PHX-AD-1`"
                            returned: on success
                            type: str
                            sample: Uocm:PHX-AD-1
                        primary_subnet_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet to place
                                  instances.
                            returned: on success
                            type: str
                            sample: "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx"
                        fault_domains:
                            description:
                                - The fault domains to place instances.
                                - If you don't provide any values, the system makes a best effort to distribute
                                  instances across all fault domains based on capacity.
                                - To distribute the instances evenly across selected fault domains, provide a
                                  set of fault domains. For example, you might want instances to be evenly
                                  distributed if your applications require high availability.
                                - To get a list of fault domains, use the
                                  L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation
                                  in the Identity and Access Management Service API.
                                - "Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`"
                            returned: on success
                            type: list
                            sample: []
                        secondary_vnic_subnets:
                            description:
                                - The set of secondary VNIC data for instances in the pool.
                            returned: on success
                            type: complex
                            contains:
                                display_name:
                                    description:
                                        - The display name of the VNIC. This is also use to match against the instance configuration defined
                                          secondary VNIC.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                subnet_id:
                                    description:
                                        - The subnet L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                size:
                    description:
                        - The number of instances that should be in the instance pool.
                    returned: on success
                    type: int
                    sample: 56
                time_created:
                    description:
                        - "The date and time the instance pool was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                load_balancers:
                    description:
                        - The load balancers attached to the instance pool.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer attachment.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        instance_pool_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool of the load
                                  balancer attachment.
                            returned: on success
                            type: str
                            sample: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
                        load_balancer_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer attached to the
                                  instance pool.
                            returned: on success
                            type: str
                            sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                        backend_set_name:
                            description:
                                - The name of the backend set on the load balancer.
                            returned: on success
                            type: str
                            sample: backend_set_name_example
                        port:
                            description:
                                - The port value used for the backends.
                            returned: on success
                            type: int
                            sample: 56
                        vnic_selection:
                            description:
                                - "Indicates which VNIC on each instance in the instance pool should be used to associate with the load balancer.
                                  Possible values are \\"PrimaryVnic\\" or the displayName of one of the secondary VNICs on the instance configuration
                                  that is associated with the instance pool."
                            returned: on success
                            type: str
                            sample: vnic_selection_example
                        lifecycle_state:
                            description:
                                - The status of the interaction between the instance pool and the load balancer.
                            returned: on success
                            type: str
                            sample: ATTACHING
                availability_domains:
                    description:
                        - The availability domains for the instance pool.
                    returned: on success
                    type: list
                    sample: []
        lifecycle_state:
            description:
                - The current state of the cluster network.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the resource was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "placement_configuration": {
            "availability_domain": "Uocm:PHX-AD-1",
            "primary_subnet_id": "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx",
            "secondary_vnic_subnets": [{
                "display_name": "display_name_example",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "instance_pools": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "display_name": "display_name_example",
            "freeform_tags": {'Department': 'Finance'},
            "instance_configuration_id": "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "PROVISIONING",
            "placement_configurations": [{
                "availability_domain": "Uocm:PHX-AD-1",
                "primary_subnet_id": "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx",
                "fault_domains": [],
                "secondary_vnic_subnets": [{
                    "display_name": "display_name_example",
                    "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            }],
            "size": 56,
            "time_created": "2013-10-20T19:20:30+01:00",
            "load_balancers": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "instance_pool_id": "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx",
                "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
                "backend_set_name": "backend_set_name_example",
                "port": 56,
                "vnic_selection": "vnic_selection_example",
                "lifecycle_state": "ATTACHING"
            }],
            "availability_domains": []
        }],
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterNetworkFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cluster_network_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster_network,
            cluster_network_id=self.module.params.get("cluster_network_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cluster_networks,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ClusterNetworkFactsHelperCustom = get_custom_class("ClusterNetworkFactsHelperCustom")


class ResourceFactsHelper(
    ClusterNetworkFactsHelperCustom, ClusterNetworkFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cluster_network_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "SCALING",
                    "STARTING",
                    "STOPPING",
                    "TERMINATING",
                    "STOPPED",
                    "TERMINATED",
                    "RUNNING",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cluster_network",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cluster_networks=result)


if __name__ == "__main__":
    main()
