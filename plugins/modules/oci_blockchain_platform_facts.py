#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_blockchain_platform_facts
short_description: Fetches details about one or multiple BlockchainPlatform resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BlockchainPlatform resources in Oracle Cloud Infrastructure
    - Returns a list Blockchain Platform Instances in a compartment
    - If I(blockchain_platform_id) is specified, the details of a single BlockchainPlatform will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    blockchain_platform_id:
        description:
            - Unique service identifier.
            - Required to get a specific blockchain_platform.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple blockchain_platforms.
        type: str
    display_name:
        description:
            - "A user-friendly name. Does not have to be unique, and it's changeable.
              Example: `My new resource`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.
              The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "SCALING"
            - "INACTIVE"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List blockchain_platforms
  oci_blockchain_platform_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific blockchain_platform
  oci_blockchain_platform_facts:
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
blockchain_platforms:
    description:
        - List of BlockchainPlatform resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - unique identifier that is immutable on creation
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        platform_shape_type:
            description:
                - "Type of Platform shape - DEFAULT or CUSTOM"
            returned: on success
            type: string
            sample: DEFAULT
        load_balancer_shape:
            description:
                - "Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS."
            returned: on success
            type: string
            sample: LB_100_MBPS
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.blockchain import BlockchainPlatformClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BlockchainPlatformFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "blockchain_platform_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_blockchain_platform,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_blockchain_platforms,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BlockchainPlatformFactsHelperCustom = get_custom_class(
    "BlockchainPlatformFactsHelperCustom"
)


class ResourceFactsHelper(
    BlockchainPlatformFactsHelperCustom, BlockchainPlatformFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            blockchain_platform_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "SCALING",
                    "INACTIVE",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="blockchain_platform",
        service_client_class=BlockchainPlatformClient,
        namespace="blockchain",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(blockchain_platforms=result)


if __name__ == "__main__":
    main()
