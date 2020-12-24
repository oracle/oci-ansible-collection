#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_blockchain_platform_actions
short_description: Perform actions on a BlockchainPlatform resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BlockchainPlatform resource in Oracle Cloud Infrastructure
    - For I(action=start), start a Blockchain Platform
    - For I(action=stop), stop a Blockchain Platform
version_added: "2.9"
author: Oracle (@oracle)
options:
    blockchain_platform_id:
        description:
            - Unique service identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the BlockchainPlatform.
        type: str
        required: true
        choices:
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action start on blockchain_platform
  oci_blockchain_platform_actions:
    blockchain_platform_id: ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx
    action: start

- name: Perform action stop on blockchain_platform
  oci_blockchain_platform_actions:
    blockchain_platform_id: ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx
    action: stop

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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Platform Instance Display name, can be renamed
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        description:
            description:
                - Platform Instance Description
            returned: on success
            type: string
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
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the Platform Instance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        service_version:
            description:
                - The version of the Platform Instance.
            returned: on success
            type: string
            sample: service_version_example
        platform_role:
            description:
                - "Role of platform - FOUNDER or PARTICIPANT"
            returned: on success
            type: string
            sample: FOUNDER
        compute_shape:
            description:
                - "Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM"
            returned: on success
            type: string
            sample: STANDARD
        service_endpoint:
            description:
                - Service endpoint URL, valid post-provisioning
            returned: on success
            type: string
            sample: service_endpoint_example
        lifecycle_state:
            description:
                - The current state of the Platform Instance.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
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
                            type: string
                            sample: osn_key_example
                        ad:
                            description:
                                - Availability Domain of OSN
                            returned: on success
                            type: string
                            sample: ad_example
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
                            type: string
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
                            type: string
                            sample: peer_key_example
                        role:
                            description:
                                - Peer role
                            returned: on success
                            type: string
                            sample: role_example
                        alias:
                            description:
                                - peer alias
                            returned: on success
                            type: string
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
                            type: string
                            sample: host_example
                        ad:
                            description:
                                - Availability Domain of peer
                            returned: on success
                            type: string
                            sample: ad_example
                        lifecycle_state:
                            description:
                                - The current state of the peer.
                            returned: on success
                            type: string
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
                    type: string
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
        "service_version": "service_version_example",
        "platform_role": "FOUNDER",
        "compute_shape": "STANDARD",
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
                "ad": "ad_example",
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
                "ad": "ad_example",
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.blockchain import BlockchainPlatformClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BlockchainPlatformActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "blockchain_platform_id"

    def get_module_resource_id(self):
        return self.module.params.get("blockchain_platform_id")

    def get_get_fn(self):
        return self.client.get_blockchain_platform

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_blockchain_platform,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_blockchain_platform,
            call_fn_args=(),
            call_fn_kwargs=dict(
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
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

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_blockchain_platform,
            call_fn_args=(),
            call_fn_kwargs=dict(
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
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


BlockchainPlatformActionsHelperCustom = get_custom_class(
    "BlockchainPlatformActionsHelperCustom"
)


class ResourceHelper(
    BlockchainPlatformActionsHelperCustom, BlockchainPlatformActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            blockchain_platform_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["start", "stop"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
