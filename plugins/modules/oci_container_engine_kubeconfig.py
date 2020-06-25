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
module: oci_container_engine_kubeconfig
short_description: Manage a Kubeconfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a Kubeconfig resource in Oracle Cloud Infrastructure
    - For I(state=present), create the Kubeconfig YAML for a cluster.
version_added: "2.9"
author: Oracle (@oracle)
options:
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    token_version:
        description:
            - The version of the kubeconfig token. Supported value 2.0.0
        type: str
    expiration:
        description:
            - Deprecated. This field is no longer used.
        type: int
    state:
        description:
            - The state of the Kubeconfig.
            - Use I(state=present) to create a Kubeconfig.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create kubeconfig
  oci_container_engine_kubeconfig:
    cluster_id: ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
kubeconfig:
    description:
        - Details of the Kubeconfig resource acted upon by the current operation
    returned: on success
    type: str
    sample: "sample"
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
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import CreateClusterKubeconfigContentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KubeconfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return CreateClusterKubeconfigContentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_kubeconfig,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                create_cluster_kubeconfig_content_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )


KubeconfigHelperCustom = get_custom_class("KubeconfigHelperCustom")


class ResourceHelper(KubeconfigHelperCustom, KubeconfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            cluster_id=dict(type="str", required=True),
            token_version=dict(type="str"),
            expiration=dict(type="int"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="kubeconfig",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
