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
module: oci_compute_management_cluster_network
short_description: Manage a ClusterNetwork resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ClusterNetwork resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a cluster network. For more information about cluster networks, see
      L(Managing Cluster Networks,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_compute_management_cluster_network_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              containing the cluster network.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    instance_pools:
        description:
            - The data to create the instance pools in the cluster network.
            - Each cluster network can have one instance pool.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a
                      namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    - This parameter is updatable.
                type: dict
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                    - This parameter is updatable.
                type: str
                aliases: ["name"]
            freeform_tags:
                description:
                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                      predefined name, type, or namespace. For more information, see L(Resource
                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    - This parameter is updatable.
                type: dict
            instance_configuration_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration
                      associated with the instance pool.
                    - This parameter is updatable.
                type: str
            size:
                description:
                    - The number of instances that should be in the instance pool.
                    - This parameter is updatable.
                type: int
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
                    - This parameter is updatable.
                type: str
    placement_configuration:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            availability_domain:
                description:
                    - The availability domain to place instances.
                    - "Example: `Uocm:PHX-AD-1`"
                type: str
                required: true
            primary_subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet to place
                      instances.
                type: str
                required: true
            secondary_vnic_subnets:
                description:
                    - The set of secondary VNIC data for instances in the pool.
                type: list
                elements: dict
                suboptions:
                    display_name:
                        description:
                            - The display name of the VNIC. This is also use to match against the instance configuration defined
                              secondary VNIC.
                        type: str
                        aliases: ["name"]
                    subnet_id:
                        description:
                            - The subnet L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.
                        type: str
                        required: true
    cluster_network_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ClusterNetwork.
            - Use I(state=present) to create or update a ClusterNetwork.
            - Use I(state=absent) to delete a ClusterNetwork.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create cluster_network
  oci_compute_management_cluster_network:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    instance_pools:
    - # optional
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      instance_configuration_id: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
      size: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    placement_configuration:
      # required
      availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      secondary_vnic_subnets:
      - # required
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update cluster_network
  oci_compute_management_cluster_network:
    # required
    cluster_network_id: "ocid1.clusternetwork.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    instance_pools:
    - # optional
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      instance_configuration_id: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
      size: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update cluster_network using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_management_cluster_network:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    instance_pools:
    - # optional
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      instance_configuration_id: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
      size: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete cluster_network
  oci_compute_management_cluster_network:
    # required
    cluster_network_id: "ocid1.clusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete cluster_network using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_management_cluster_network:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
cluster_network:
    description:
        - Details of the ClusterNetwork resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        placement_configuration:
            description:
                - ""
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
    sample: {
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
            }]
        }],
        "placement_configuration": {
            "availability_domain": "Uocm:PHX-AD-1",
            "primary_subnet_id": "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx",
            "secondary_vnic_subnets": [{
                "display_name": "display_name_example",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.core import ComputeManagementClient
    from oci.core.models import CreateClusterNetworkDetails
    from oci.core.models import UpdateClusterNetworkDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterNetworkHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ClusterNetworkHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(ClusterNetworkHelperGen, self).get_possible_entity_types() + [
            "clusternetwork",
            "clusternetworks",
            "coreclusternetwork",
            "coreclusternetworks",
            "clusternetworkresource",
            "clusternetworksresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "cluster_network_id"

    def get_module_resource_id(self):
        return self.module.params.get("cluster_network_id")

    def get_get_fn(self):
        return self.client.get_cluster_network

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster_network, cluster_network_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster_network,
            cluster_network_id=self.module.params.get("cluster_network_id"),
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
            self.client.list_cluster_networks, **kwargs
        )

    def get_create_model_class(self):
        return CreateClusterNetworkDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(create_cluster_network_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateClusterNetworkDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_network_id=self.module.params.get("cluster_network_id"),
                update_cluster_network_details=update_details,
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
            call_fn=self.client.terminate_cluster_network,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_network_id=self.module.params.get("cluster_network_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ClusterNetworkHelperCustom = get_custom_class("ClusterNetworkHelperCustom")


class ResourceHelper(ClusterNetworkHelperCustom, ClusterNetworkHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            instance_pools=dict(
                type="list",
                elements="dict",
                options=dict(
                    defined_tags=dict(type="dict"),
                    display_name=dict(aliases=["name"], type="str"),
                    freeform_tags=dict(type="dict"),
                    instance_configuration_id=dict(type="str"),
                    size=dict(type="int"),
                    id=dict(type="str"),
                ),
            ),
            placement_configuration=dict(
                type="dict",
                options=dict(
                    availability_domain=dict(type="str", required=True),
                    primary_subnet_id=dict(type="str", required=True),
                    secondary_vnic_subnets=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            display_name=dict(aliases=["name"], type="str"),
                            subnet_id=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            cluster_network_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cluster_network",
        service_client_class=ComputeManagementClient,
        namespace="core",
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
