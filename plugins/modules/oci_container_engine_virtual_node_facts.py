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
module: oci_container_engine_virtual_node_facts
short_description: Fetches details about one or multiple VirtualNode resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VirtualNode resources in Oracle Cloud Infrastructure
    - List virtual nodes in a virtual node pool.
    - If I(virtual_node_id) is specified, the details of a single VirtualNode will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_node_id:
        description:
            - The OCID of the virtual node.
            - Required to get a specific virtual_node.
        type: str
        aliases: ["id"]
    virtual_node_pool_id:
        description:
            - The OCID of the virtual node pool.
        type: str
        required: true
    name:
        description:
            - The name to filter on.
        type: str
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "ID"
            - "NAME"
            - "TIME_CREATED"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific virtual_node
  oci_container_engine_virtual_node_facts:
    # required
    virtual_node_id: "ocid1.virtualnode.oc1..xxxxxxEXAMPLExxxxxx"
    virtual_node_pool_id: "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx"

- name: List virtual_nodes
  oci_container_engine_virtual_node_facts:
    # required
    virtual_node_pool_id: "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: ID

"""

RETURN = """
virtual_nodes:
    description:
        - List of VirtualNode resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The ocid of the virtual node.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the virtual node.
            returned: on success
            type: str
            sample: display_name_example
        kubernetes_version:
            description:
                - The version of Kubernetes this virtual node is running.
            returned: on success
            type: str
            sample: kubernetes_version_example
        virtual_node_pool_id:
            description:
                - The ocid of the virtual node pool this virtual node belongs to.
            returned: on success
            type: str
            sample: "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The name of the availability domain in which this virtual node is placed
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The fault domain of this virtual node.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        subnet_id:
            description:
                - The OCID of the subnet in which this Virtual Node is placed.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - NSG Ids applied to virtual node vnic.
            returned: on success
            type: list
            sample: []
        private_ip:
            description:
                - The private IP address of this Virtual Node.
            returned: on success
            type: str
            sample: private_ip_example
        virtual_node_error:
            description:
                - An error that may be associated with the virtual node.
            returned: on success
            type: str
            sample: virtual_node_error_example
        lifecycle_state:
            description:
                - The state of the Virtual Node.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the state of the Virtual Node.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time at which the virtual node was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "kubernetes_version": "kubernetes_version_example",
        "virtual_node_pool_id": "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "FAULT-DOMAIN-1",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "private_ip": "private_ip_example",
        "virtual_node_error": "virtual_node_error_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
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
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualNodeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "virtual_node_pool_id",
            "virtual_node_id",
        ]

    def get_required_params_for_list(self):
        return [
            "virtual_node_pool_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_node,
            virtual_node_pool_id=self.module.params.get("virtual_node_pool_id"),
            virtual_node_id=self.module.params.get("virtual_node_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_virtual_nodes,
            virtual_node_pool_id=self.module.params.get("virtual_node_pool_id"),
            **optional_kwargs
        )


VirtualNodeFactsHelperCustom = get_custom_class("VirtualNodeFactsHelperCustom")


class ResourceFactsHelper(VirtualNodeFactsHelperCustom, VirtualNodeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            virtual_node_id=dict(aliases=["id"], type="str"),
            virtual_node_pool_id=dict(type="str", required=True),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ID", "NAME", "TIME_CREATED"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="virtual_node",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(virtual_nodes=result)


if __name__ == "__main__":
    main()
