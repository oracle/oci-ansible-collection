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
module: oci_opensearch_cluster
short_description: Manage an OpensearchCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OpensearchCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new OpensearchCluster.
    - "This resource has the following action operations in the M(oracle.oci.oci_opensearch_cluster_actions) module: backup, opensearch_cluster_restore,
      resize_opensearch_cluster_horizontal, resize_opensearch_cluster_vertical."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to create the cluster in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    master_node_count:
        description:
            - The number of master nodes to configure for the cluster.
            - Required for create using I(state=present).
        type: int
    master_node_host_type:
        description:
            - The instance type for the cluster's master nodes.
            - Required for create using I(state=present).
        type: str
        choices:
            - "FLEX"
            - "BM"
    master_node_host_bare_metal_shape:
        description:
            - The bare metal shape for the cluster's master nodes.
        type: str
    master_node_host_ocpu_count:
        description:
            - The number of OCPUs to configure for the cluser's master nodes.
            - Required for create using I(state=present).
        type: int
    master_node_host_memory_gb:
        description:
            - The amount of memory in GB, to configure per node for the cluster's master nodes.
            - Required for create using I(state=present).
        type: int
    data_node_count:
        description:
            - The number of data nodes to configure for the cluster.
            - Required for create using I(state=present).
        type: int
    data_node_host_type:
        description:
            - TThe instance type for the cluster's data nodes.
            - Required for create using I(state=present).
        type: str
        choices:
            - "FLEX"
            - "BM"
    data_node_host_bare_metal_shape:
        description:
            - The bare metal shape for the cluster's data nodes.
        type: str
    data_node_host_ocpu_count:
        description:
            - The number of OCPUs to configure for the cluster's data nodes.
            - Required for create using I(state=present).
        type: int
    data_node_host_memory_gb:
        description:
            - The amount of memory in GB, to configure per node for the cluster's data nodes.
            - Required for create using I(state=present).
        type: int
    data_node_storage_gb:
        description:
            - The amount of storage in GB, to configure per node for the cluster's data nodes.
            - Required for create using I(state=present).
        type: int
    opendashboard_node_count:
        description:
            - The number of OpenSearch Dashboard nodes to configure for the cluster.
            - Required for create using I(state=present).
        type: int
    opendashboard_node_host_ocpu_count:
        description:
            - The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.
            - Required for create using I(state=present).
        type: int
    opendashboard_node_host_memory_gb:
        description:
            - The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.
            - Required for create using I(state=present).
        type: int
    vcn_id:
        description:
            - The OCID of the cluster's VCN.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The OCID of the cluster's subnet.
            - Required for create using I(state=present).
        type: str
    vcn_compartment_id:
        description:
            - The OCID for the compartment where the cluster's VCN is located.
            - Required for create using I(state=present).
        type: str
    subnet_compartment_id:
        description:
            - The OCID for the compartment where the cluster's subnet is located.
            - Required for create using I(state=present).
        type: str
    system_tags:
        description:
            - "Usage of system tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
        type: dict
    display_name:
        description:
            - The name of the cluster. Avoid entering confidential information.
            - Required for create using I(state=present), update using I(state=present) with opensearch_cluster_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    software_version:
        description:
            - The version of the software the cluster is running.
            - Required for create using I(state=present).
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
    opensearch_cluster_id:
        description:
            - unique OpensearchCluster identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OpensearchCluster.
            - Use I(state=present) to create or update an OpensearchCluster.
            - Use I(state=absent) to delete an OpensearchCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create opensearch_cluster
  oci_opensearch_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    master_node_count: 56
    master_node_host_type: FLEX
    master_node_host_ocpu_count: 56
    master_node_host_memory_gb: 56
    data_node_count: 56
    data_node_host_type: FLEX
    data_node_host_ocpu_count: 56
    data_node_host_memory_gb: 56
    data_node_storage_gb: 56
    opendashboard_node_count: 56
    opendashboard_node_host_ocpu_count: 56
    opendashboard_node_host_memory_gb: 56
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_compartment_id: "ocid1.vcncompartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_compartment_id: "ocid1.subnetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    software_version: software_version_example

    # optional
    master_node_host_bare_metal_shape: master_node_host_bare_metal_shape_example
    data_node_host_bare_metal_shape: data_node_host_bare_metal_shape_example
    system_tags: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update opensearch_cluster
  oci_opensearch_cluster:
    # required
    display_name: display_name_example
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    software_version: software_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update opensearch_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opensearch_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    software_version: software_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete opensearch_cluster
  oci_opensearch_cluster:
    # required
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete opensearch_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opensearch_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
opensearch_cluster:
    description:
        - Details of the OpensearchCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the cluster. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the cluster is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the cluster.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - The amount of time in milliseconds since the cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The amount of time in milliseconds since the cluster was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_deleted:
            description:
                - The amount of time in milliseconds since the cluster was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the cluster.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        software_version:
            description:
                - The software version the cluster is running.
            returned: on success
            type: str
            sample: software_version_example
        total_storage_gb:
            description:
                - The size in GB of the cluster's total storage.
            returned: on success
            type: int
            sample: 56
        opensearch_fqdn:
            description:
                - The fully qualified domain name (FQDN) for the cluster's API endpoint.
            returned: on success
            type: str
            sample: opensearch_fqdn_example
        opensearch_private_ip:
            description:
                - The cluster's private IP address.
            returned: on success
            type: str
            sample: opensearch_private_ip_example
        opendashboard_fqdn:
            description:
                - The fully qualified domain name (FQDN) for the cluster's OpenSearch Dashboard API endpoint.
            returned: on success
            type: str
            sample: opendashboard_fqdn_example
        opendashboard_private_ip:
            description:
                - The private IP address for the cluster's OpenSearch Dashboard.
            returned: on success
            type: str
            sample: opendashboard_private_ip_example
        master_node_count:
            description:
                - The number of master nodes configured for the cluster.
            returned: on success
            type: int
            sample: 56
        master_node_host_type:
            description:
                - The instance type for the cluster's master nodes.
            returned: on success
            type: str
            sample: FLEX
        master_node_host_bare_metal_shape:
            description:
                - The bare metal shape for the cluster's master nodes.
            returned: on success
            type: str
            sample: master_node_host_bare_metal_shape_example
        master_node_host_ocpu_count:
            description:
                - The number of OCPUs configured for cluster's master nodes.
            returned: on success
            type: int
            sample: 56
        master_node_host_memory_gb:
            description:
                - The amount of memory in GB, for the cluster's master nodes.
            returned: on success
            type: int
            sample: 56
        data_node_count:
            description:
                - The number of data nodes configured for the cluster.
            returned: on success
            type: int
            sample: 56
        data_node_host_type:
            description:
                - The instance type for the cluster's data nodes.
            returned: on success
            type: str
            sample: FLEX
        data_node_host_bare_metal_shape:
            description:
                - The bare metal shape for the cluster's data nodes.
            returned: on success
            type: str
            sample: data_node_host_bare_metal_shape_example
        data_node_host_ocpu_count:
            description:
                - The number of OCPUs configured for the cluster's data nodes.
            returned: on success
            type: int
            sample: 56
        data_node_host_memory_gb:
            description:
                - The amount of memory in GB, for the cluster's data nodes.
            returned: on success
            type: int
            sample: 56
        data_node_storage_gb:
            description:
                - The amount of storage in GB, to configure per node for the cluster's data nodes.
            returned: on success
            type: int
            sample: 56
        opendashboard_node_count:
            description:
                - The number of OpenSearch Dashboard nodes configured for the cluster.
            returned: on success
            type: int
            sample: 56
        opendashboard_node_host_ocpu_count:
            description:
                - The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.
            returned: on success
            type: int
            sample: 56
        opendashboard_node_host_memory_gb:
            description:
                - The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.
            returned: on success
            type: int
            sample: 56
        vcn_id:
            description:
                - The OCID of the cluster's VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the cluster's subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_compartment_id:
            description:
                - The OCID for the compartment where the cluster's VCN is located.
            returned: on success
            type: str
            sample: "ocid1.vcncompartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_compartment_id:
            description:
                - The OCID for the compartment where the cluster's subnet is located.
            returned: on success
            type: str
            sample: "ocid1.subnetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        fqdn:
            description:
                - The fully qualified domain name (FQDN) for the cluster's API endpoint.
            returned: on success
            type: str
            sample: fqdn_example
        availability_domains:
            description:
                - The availability domains to distribute the cluser nodes across.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_deleted": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "software_version": "software_version_example",
        "total_storage_gb": 56,
        "opensearch_fqdn": "opensearch_fqdn_example",
        "opensearch_private_ip": "opensearch_private_ip_example",
        "opendashboard_fqdn": "opendashboard_fqdn_example",
        "opendashboard_private_ip": "opendashboard_private_ip_example",
        "master_node_count": 56,
        "master_node_host_type": "FLEX",
        "master_node_host_bare_metal_shape": "master_node_host_bare_metal_shape_example",
        "master_node_host_ocpu_count": 56,
        "master_node_host_memory_gb": 56,
        "data_node_count": 56,
        "data_node_host_type": "FLEX",
        "data_node_host_bare_metal_shape": "data_node_host_bare_metal_shape_example",
        "data_node_host_ocpu_count": 56,
        "data_node_host_memory_gb": 56,
        "data_node_storage_gb": 56,
        "opendashboard_node_count": 56,
        "opendashboard_node_host_ocpu_count": 56,
        "opendashboard_node_host_memory_gb": 56,
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_compartment_id": "ocid1.vcncompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_compartment_id": "ocid1.subnetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "fqdn": "fqdn_example",
        "availability_domains": []
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
    from oci.opensearch import OpensearchClusterClient
    from oci.opensearch.models import CreateOpensearchClusterDetails
    from oci.opensearch.models import UpdateOpensearchClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(OpensearchClusterHelperGen, self).get_possible_entity_types() + [
            "opensearchcluster",
            "opensearchclusters",
            "opensearchopensearchcluster",
            "opensearchopensearchclusters",
            "opensearchclusterresource",
            "opensearchclustersresource",
            "opensearch",
        ]

    def get_module_resource_id_param(self):
        return "opensearch_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("opensearch_cluster_id")

    def get_get_fn(self):
        return self.client.get_opensearch_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster, opensearch_cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster,
            opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
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
            self.client.list_opensearch_clusters, **kwargs
        )

    def get_create_model_class(self):
        return CreateOpensearchClusterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_opensearch_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_opensearch_cluster_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOpensearchClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_opensearch_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                update_opensearch_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_opensearch_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OpensearchClusterHelperCustom = get_custom_class("OpensearchClusterHelperCustom")


class ResourceHelper(OpensearchClusterHelperCustom, OpensearchClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            master_node_count=dict(type="int"),
            master_node_host_type=dict(type="str", choices=["FLEX", "BM"]),
            master_node_host_bare_metal_shape=dict(type="str"),
            master_node_host_ocpu_count=dict(type="int"),
            master_node_host_memory_gb=dict(type="int"),
            data_node_count=dict(type="int"),
            data_node_host_type=dict(type="str", choices=["FLEX", "BM"]),
            data_node_host_bare_metal_shape=dict(type="str"),
            data_node_host_ocpu_count=dict(type="int"),
            data_node_host_memory_gb=dict(type="int"),
            data_node_storage_gb=dict(type="int"),
            opendashboard_node_count=dict(type="int"),
            opendashboard_node_host_ocpu_count=dict(type="int"),
            opendashboard_node_host_memory_gb=dict(type="int"),
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            vcn_compartment_id=dict(type="str"),
            subnet_compartment_id=dict(type="str"),
            system_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            software_version=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            opensearch_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opensearch_cluster",
        service_client_class=OpensearchClusterClient,
        namespace="opensearch",
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
