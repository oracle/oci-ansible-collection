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
module: oci_blockchain_platform
short_description: Manage a BlockchainPlatform resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BlockchainPlatform resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Blockchain Platform.
    - "This resource has the following action operations in the M(oracle.oci.oci_blockchain_platform_actions) module: change_compartment, start, stop, upgrade."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Platform Instance Display name, can be renamed
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    platform_role:
        description:
            - "Role of platform - founder or participant"
            - Required for create using I(state=present).
        type: str
    compute_shape:
        description:
            - "Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE"
            - Required for create using I(state=present).
        type: str
    is_byol:
        description:
            - Bring your own license
        type: bool
    platform_version:
        description:
            - Platform version
        type: str
    idcs_access_token:
        description:
            - IDCS access token with Identity Domain Administrator role
            - Required for create using I(state=present).
        type: str
    federated_user_id:
        description:
            - Identifier for a federated user
        type: str
    ca_cert_archive_text:
        description:
            - Base64 encoded text in ASCII character set of a Thirdparty CA Certificates archive file.
              The Archive file is a zip file containing third part CA Certificates,
              the ca key and certificate files used when issuing enrollment certificates
              (ECerts) and transaction certificates (TCerts). The chainfile (if it exists)
              contains the certificate chain which should be trusted for this CA, where
              the 1st in the chain is always the root CA certificate.
              File list in zip file [ca-cert.pem,ca-key.pem,ca-chain.pem(optional)].
        type: str
    description:
        description:
            - Platform Instance Description
            - This parameter is updatable.
        type: str
    storage_size_in_tbs:
        description:
            - Storage size in TBs
            - This parameter is updatable.
        type: float
    replicas:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            proxy_count:
                description:
                    - Number of REST proxy replicas
                    - This parameter is updatable.
                type: int
            ca_count:
                description:
                    - Number of CA replicas
                    - This parameter is updatable.
                type: int
            console_count:
                description:
                    - Number of console replicas
                    - This parameter is updatable.
                type: int
    total_ocpu_capacity:
        description:
            - Number of total OCPUs to allocate
            - This parameter is updatable.
        type: int
    load_balancer_shape:
        description:
            - "Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS."
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
    blockchain_platform_id:
        description:
            - Unique service identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BlockchainPlatform.
            - Use I(state=present) to create or update a BlockchainPlatform.
            - Use I(state=absent) to delete a BlockchainPlatform.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create blockchain_platform
  oci_blockchain_platform:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    platform_role: platform_role_example
    compute_shape: compute_shape_example
    idcs_access_token: idcs_access_token_example

    # optional
    is_byol: true
    platform_version: platform_version_example
    federated_user_id: "ocid1.federateduser.oc1..xxxxxxEXAMPLExxxxxx"
    ca_cert_archive_text: ca_cert_archive_text_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update blockchain_platform
  oci_blockchain_platform:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    storage_size_in_tbs: 3.4
    replicas:
      # optional
      proxy_count: 56
      ca_count: 56
      console_count: 56
    total_ocpu_capacity: 56
    load_balancer_shape: load_balancer_shape_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update blockchain_platform using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockchain_platform:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    storage_size_in_tbs: 3.4
    replicas:
      # optional
      proxy_count: 56
      ca_count: 56
      console_count: 56
    total_ocpu_capacity: 56
    load_balancer_shape: load_balancer_shape_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete blockchain_platform
  oci_blockchain_platform:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete blockchain_platform using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockchain_platform:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
blockchain_platform:
    description:
        - Details of the BlockchainPlatform resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Platform Instance Display name, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Platform Instance Description
            returned: on success
            type: str
            sample: description_example
        is_byol:
            description:
                - Bring your own license
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the the Platform Instance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Platform Instance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        platform_version:
            description:
                - Platform Version
            returned: on success
            type: str
            sample: platform_version_example
        service_version:
            description:
                - The version of the Platform Instance.
            returned: on success
            type: str
            sample: service_version_example
        platform_role:
            description:
                - "Role of platform - FOUNDER or PARTICIPANT"
            returned: on success
            type: str
            sample: FOUNDER
        compute_shape:
            description:
                - "Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM"
            returned: on success
            type: str
            sample: STANDARD
        platform_shape_type:
            description:
                - "Type of Platform shape - DEFAULT or CUSTOM"
            returned: on success
            type: str
            sample: DEFAULT
        load_balancer_shape:
            description:
                - "Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS."
            returned: on success
            type: str
            sample: LB_100_MBPS
        service_endpoint:
            description:
                - Service endpoint URL, valid post-provisioning
            returned: on success
            type: str
            sample: service_endpoint_example
        lifecycle_state:
            description:
                - The current state of the Platform Instance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        storage_size_in_tbs:
            description:
                - Storage size in TBs
            returned: on success
            type: float
            sample: 1.2
        storage_used_in_t_bs:
            description:
                - Storage used in TBs
            returned: on success
            type: float
            sample: 1.2
        is_multi_ad:
            description:
                - True for multi-AD blockchain plaforms, false for single-AD
            returned: on success
            type: bool
            sample: true
        total_ocpu_capacity:
            description:
                - Number of total OCPUs allocated to the platform cluster
            returned: on success
            type: int
            sample: 56
        component_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                osns:
                    description:
                        - List of OSNs
                    returned: on success
                    type: complex
                    contains:
                        osn_key:
                            description:
                                - OSN identifier
                            returned: on success
                            type: str
                            sample: osn_key_example
                        ad:
                            description:
                                - Availability Domain of OSN
                            returned: on success
                            type: str
                            sample: Uocm:PHX-AD-1
                        ocpu_allocation_param:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpu_allocation_number:
                                    description:
                                        - Number of OCPU allocation
                                    returned: on success
                                    type: float
                                    sample: 3.4
                        lifecycle_state:
                            description:
                                - The current state of the OSN.
                            returned: on success
                            type: str
                            sample: ACTIVE
                peers:
                    description:
                        - List of Peers
                    returned: on success
                    type: complex
                    contains:
                        peer_key:
                            description:
                                - peer identifier
                            returned: on success
                            type: str
                            sample: peer_key_example
                        role:
                            description:
                                - Peer role
                            returned: on success
                            type: str
                            sample: role_example
                        alias:
                            description:
                                - peer alias
                            returned: on success
                            type: str
                            sample: alias_example
                        ocpu_allocation_param:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpu_allocation_number:
                                    description:
                                        - Number of OCPU allocation
                                    returned: on success
                                    type: float
                                    sample: 3.4
                        host:
                            description:
                                - Host on which the Peer exists
                            returned: on success
                            type: str
                            sample: host_example
                        ad:
                            description:
                                - Availability Domain of peer
                            returned: on success
                            type: str
                            sample: Uocm:PHX-AD-1
                        lifecycle_state:
                            description:
                                - The current state of the peer.
                            returned: on success
                            type: str
                            sample: ACTIVE
        replicas:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                proxy_count:
                    description:
                        - Number of REST proxy replicas
                    returned: on success
                    type: int
                    sample: 56
                ca_count:
                    description:
                        - Number of CA replicas
                    returned: on success
                    type: int
                    sample: 56
                console_count:
                    description:
                        - Number of console replicas
                    returned: on success
                    type: int
                    sample: 56
        host_ocpu_utilization_info:
            description:
                - List of OcpuUtilization for all hosts
            returned: on success
            type: complex
            contains:
                host:
                    description:
                        - Host name of VM
                    returned: on success
                    type: str
                    sample: host_example
                ocpu_utilization_number:
                    description:
                        - Number of OCPU utilized
                    returned: on success
                    type: float
                    sample: 3.4
                ocpu_capacity_number:
                    description:
                        - Number of total OCPU capacity on the host
                    returned: on success
                    type: float
                    sample: 3.4
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "is_byol": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "platform_version": "platform_version_example",
        "service_version": "service_version_example",
        "platform_role": "FOUNDER",
        "compute_shape": "STANDARD",
        "platform_shape_type": "DEFAULT",
        "load_balancer_shape": "LB_100_MBPS",
        "service_endpoint": "service_endpoint_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "storage_size_in_tbs": 1.2,
        "storage_used_in_t_bs": 1.2,
        "is_multi_ad": true,
        "total_ocpu_capacity": 56,
        "component_details": {
            "osns": [{
                "osn_key": "osn_key_example",
                "ad": "Uocm:PHX-AD-1",
                "ocpu_allocation_param": {
                    "ocpu_allocation_number": 3.4
                },
                "lifecycle_state": "ACTIVE"
            }],
            "peers": [{
                "peer_key": "peer_key_example",
                "role": "role_example",
                "alias": "alias_example",
                "ocpu_allocation_param": {
                    "ocpu_allocation_number": 3.4
                },
                "host": "host_example",
                "ad": "Uocm:PHX-AD-1",
                "lifecycle_state": "ACTIVE"
            }]
        },
        "replicas": {
            "proxy_count": 56,
            "ca_count": 56,
            "console_count": 56
        },
        "host_ocpu_utilization_info": [{
            "host": "host_example",
            "ocpu_utilization_number": 3.4,
            "ocpu_capacity_number": 3.4
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.blockchain import BlockchainPlatformClient
    from oci.blockchain.models import CreateBlockchainPlatformDetails
    from oci.blockchain.models import UpdateBlockchainPlatformDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BlockchainPlatformHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_default_module_wait_timeout(self):
        return 2400

    def get_possible_entity_types(self):
        return super(BlockchainPlatformHelperGen, self).get_possible_entity_types() + [
            "blockchainplatform",
            "blockchainplatforms",
            "blockchainblockchainplatform",
            "blockchainblockchainplatforms",
            "blockchainplatformresource",
            "blockchainplatformsresource",
            "blockchain",
        ]

    def get_module_resource_id_param(self):
        return "blockchain_platform_id"

    def get_module_resource_id(self):
        return self.module.params.get("blockchain_platform_id")

    def get_get_fn(self):
        return self.client.get_blockchain_platform

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_blockchain_platform,
            blockchain_platform_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_blockchain_platform,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
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
            self.client.list_blockchain_platforms, **kwargs
        )

    def get_create_model_class(self):
        return CreateBlockchainPlatformDetails

    def get_exclude_attributes(self):
        return ["idcs_access_token", "ca_cert_archive_text", "federated_user_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_blockchain_platform,
            call_fn_args=(),
            call_fn_kwargs=dict(create_blockchain_platform_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBlockchainPlatformDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_blockchain_platform,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_blockchain_platform_details=update_details,
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_blockchain_platform,
            call_fn_args=(),
            call_fn_kwargs=dict(
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BlockchainPlatformHelperCustom = get_custom_class("BlockchainPlatformHelperCustom")


class ResourceHelper(BlockchainPlatformHelperCustom, BlockchainPlatformHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            platform_role=dict(type="str"),
            compute_shape=dict(type="str"),
            is_byol=dict(type="bool"),
            platform_version=dict(type="str"),
            idcs_access_token=dict(type="str", no_log=True),
            federated_user_id=dict(type="str"),
            ca_cert_archive_text=dict(type="str"),
            description=dict(type="str"),
            storage_size_in_tbs=dict(type="float"),
            replicas=dict(
                type="dict",
                options=dict(
                    proxy_count=dict(type="int"),
                    ca_count=dict(type="int"),
                    console_count=dict(type="int"),
                ),
            ),
            total_ocpu_capacity=dict(type="int"),
            load_balancer_shape=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            blockchain_platform_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="blockchain_platform",
        service_client_class=BlockchainPlatformClient,
        namespace="blockchain",
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
