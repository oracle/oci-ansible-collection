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
module: oci_opensearch_cluster_actions
short_description: Perform actions on an OpensearchCluster resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OpensearchCluster resource in Oracle Cloud Infrastructure
    - For I(action=backup), backup the opensearch cluster details.
    - For I(action=opensearch_cluster_restore), restore the opensearch cluster details.
    - For I(action=resize_opensearch_cluster_horizontal), resize the opensearch cluster horizontal details.
    - For I(action=resize_opensearch_cluster_vertical), resize the opensearch cluster vertical details.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The name of the cluster backup. Avoid entering confidential information.
            - Required for I(action=backup).
        type: str
        aliases: ["name"]
    opensearch_cluster_backup_id:
        description:
            - The OCID of the cluster backup to restore.
            - Required for I(action=opensearch_cluster_restore).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment where the cluster backup is located.
            - Required for I(action=backup), I(action=opensearch_cluster_restore).
        type: str
    prefix:
        description:
            - The prefix for the indices in the cluster backup.
            - Applicable only for I(action=opensearch_cluster_restore).
        type: str
    master_node_count:
        description:
            - The number of master nodes to configure for the cluster.
            - Applicable only for I(action=resize_opensearch_cluster_horizontal).
        type: int
    data_node_count:
        description:
            - The number of data nodes to configure for the cluster.
            - Applicable only for I(action=resize_opensearch_cluster_horizontal).
        type: int
    opendashboard_node_count:
        description:
            - The number of OpenSearch Dashboard nodes to configure for the cluster.
            - Applicable only for I(action=resize_opensearch_cluster_horizontal).
        type: int
    opensearch_cluster_id:
        description:
            - unique OpensearchCluster identifier
        type: str
        aliases: ["id"]
        required: true
    master_node_host_ocpu_count:
        description:
            - The number of OCPUs to configure for the cluster's master nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    master_node_host_memory_gb:
        description:
            - The amount of memory in GB, to configure for the cluster's master nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    data_node_host_ocpu_count:
        description:
            - The number of OCPUs to configure for the cluster's data nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    data_node_host_memory_gb:
        description:
            - The amount of memory in GB, to configure for the cluster's data nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    data_node_storage_gb:
        description:
            - The amount of storage in GB, to configure per node for the cluster's data nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    opendashboard_node_host_ocpu_count:
        description:
            - The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    opendashboard_node_host_memory_gb:
        description:
            - The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.
            - Applicable only for I(action=resize_opensearch_cluster_vertical).
        type: int
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - Applicable only for I(action=resize_opensearch_cluster_horizontal)I(action=resize_opensearch_cluster_vertical).
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - Applicable only for I(action=resize_opensearch_cluster_horizontal)I(action=resize_opensearch_cluster_vertical).
        type: dict
    action:
        description:
            - The action to perform on the OpensearchCluster.
        type: str
        required: true
        choices:
            - "backup"
            - "opensearch_cluster_restore"
            - "resize_opensearch_cluster_horizontal"
            - "resize_opensearch_cluster_vertical"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action backup on opensearch_cluster
  oci_opensearch_cluster_actions:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: backup

- name: Perform action opensearch_cluster_restore on opensearch_cluster
  oci_opensearch_cluster_actions:
    # required
    opensearch_cluster_backup_id: "ocid1.opensearchclusterbackup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: opensearch_cluster_restore

    # optional
    prefix: prefix_example

- name: Perform action resize_opensearch_cluster_horizontal on opensearch_cluster
  oci_opensearch_cluster_actions:
    # required
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: resize_opensearch_cluster_horizontal

    # optional
    master_node_count: 56
    data_node_count: 56
    opendashboard_node_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Perform action resize_opensearch_cluster_vertical on opensearch_cluster
  oci_opensearch_cluster_actions:
    # required
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: resize_opensearch_cluster_vertical

    # optional
    master_node_host_ocpu_count: 56
    master_node_host_memory_gb: 56
    data_node_host_ocpu_count: 56
    data_node_host_memory_gb: 56
    data_node_storage_gb: 56
    opendashboard_node_host_ocpu_count: 56
    opendashboard_node_host_memory_gb: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

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
        security_mode:
            description:
                - The security mode of the cluster.
            returned: on success
            type: str
            sample: DISABLED
        security_master_user_name:
            description:
                - The name of the master user that are used to manage security config
            returned: on success
            type: str
            sample: security_master_user_name_example
        security_master_user_password_hash:
            description:
                - The password hash of the master user that are used to manage security config
            returned: on success
            type: str
            sample: security_master_user_password_hash_example
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
        "availability_domains": [],
        "security_mode": "DISABLED",
        "security_master_user_name": "security_master_user_name_example",
        "security_master_user_password_hash": "security_master_user_password_hash_example"
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
    from oci.opensearch import OpensearchClusterClient
    from oci.opensearch.models import BackupOpensearchClusterDetails
    from oci.opensearch.models import RestoreOpensearchClusterDetails
    from oci.opensearch.models import ResizeOpensearchClusterHorizontalDetails
    from oci.opensearch.models import ResizeOpensearchClusterVerticalDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        backup
        opensearch_cluster_restore
        resize_opensearch_cluster_horizontal
        resize_opensearch_cluster_vertical
    """

    @staticmethod
    def get_module_resource_id_param():
        return "opensearch_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("opensearch_cluster_id")

    def get_get_fn(self):
        return self.client.get_opensearch_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster,
            opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
        )

    def backup(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BackupOpensearchClusterDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.backup_opensearch_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                backup_opensearch_cluster_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def opensearch_cluster_restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreOpensearchClusterDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.opensearch_cluster_restore,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                restore_opensearch_cluster_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def resize_opensearch_cluster_horizontal(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResizeOpensearchClusterHorizontalDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resize_opensearch_cluster_horizontal,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                resize_opensearch_cluster_horizontal_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def resize_opensearch_cluster_vertical(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResizeOpensearchClusterVerticalDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resize_opensearch_cluster_vertical,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
                resize_opensearch_cluster_vertical_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OpensearchClusterActionsHelperCustom = get_custom_class(
    "OpensearchClusterActionsHelperCustom"
)


class ResourceHelper(
    OpensearchClusterActionsHelperCustom, OpensearchClusterActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            opensearch_cluster_backup_id=dict(type="str"),
            compartment_id=dict(type="str"),
            prefix=dict(type="str"),
            master_node_count=dict(type="int"),
            data_node_count=dict(type="int"),
            opendashboard_node_count=dict(type="int"),
            opensearch_cluster_id=dict(aliases=["id"], type="str", required=True),
            master_node_host_ocpu_count=dict(type="int"),
            master_node_host_memory_gb=dict(type="int"),
            data_node_host_ocpu_count=dict(type="int"),
            data_node_host_memory_gb=dict(type="int"),
            data_node_storage_gb=dict(type="int"),
            opendashboard_node_host_ocpu_count=dict(type="int"),
            opendashboard_node_host_memory_gb=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "backup",
                    "opensearch_cluster_restore",
                    "resize_opensearch_cluster_horizontal",
                    "resize_opensearch_cluster_vertical",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opensearch_cluster",
        service_client_class=OpensearchClusterClient,
        namespace="opensearch",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
