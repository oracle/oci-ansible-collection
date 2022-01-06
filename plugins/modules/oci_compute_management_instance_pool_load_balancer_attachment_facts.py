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
module: oci_compute_management_instance_pool_load_balancer_attachment_facts
short_description: Fetches details about a InstancePoolLoadBalancerAttachment resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a InstancePoolLoadBalancerAttachment resource in Oracle Cloud Infrastructure
    - Gets information about a load balancer that is attached to the specified instance pool.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
        type: str
        required: true
    instance_pool_load_balancer_attachment_id:
        description:
            - The OCID of the load balancer attachment.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific instance_pool_load_balancer_attachment
  oci_compute_management_instance_pool_load_balancer_attachment_facts:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    instance_pool_load_balancer_attachment_id: "ocid1.instancepoolloadbalancerattachment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
instance_pool_load_balancer_attachment:
    description:
        - InstancePoolLoadBalancerAttachment resource
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool of the load balancer attachment.
            returned: on success
            type: str
            sample: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer attached to the instance pool.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_pool_id": "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx",
        "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
        "backend_set_name": "backend_set_name_example",
        "port": 56,
        "vnic_selection": "vnic_selection_example",
        "lifecycle_state": "ATTACHING"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolLoadBalancerAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "instance_pool_id",
            "instance_pool_load_balancer_attachment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_pool_load_balancer_attachment,
            instance_pool_id=self.module.params.get("instance_pool_id"),
            instance_pool_load_balancer_attachment_id=self.module.params.get(
                "instance_pool_load_balancer_attachment_id"
            ),
        )


InstancePoolLoadBalancerAttachmentFactsHelperCustom = get_custom_class(
    "InstancePoolLoadBalancerAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    InstancePoolLoadBalancerAttachmentFactsHelperCustom,
    InstancePoolLoadBalancerAttachmentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_pool_id=dict(type="str", required=True),
            instance_pool_load_balancer_attachment_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_pool_load_balancer_attachment",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_pool_load_balancer_attachment=result)


if __name__ == "__main__":
    main()
