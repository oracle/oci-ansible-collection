#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_kubeconfig
short_description: Create the Kubeconfig YAML for a cluster in OCI container engine for Kubernetes service.
description:
    - This module creates a cluster kubeconfig in OCI Container Engine for Kubernetes Service.
version_added: "2.5"
options:
    cluster_id:
        description: The OCID of the cluster.
        required: true
    create_cluster_kubeconfig_content_details :
        description: The details of the cluster kubeconfig to create.
        required: false
        suboptions:
            expiration:
                description: The desired expiration, in seconds, to use for the kubeconfig token.
                required: false
            token_version:
                description: The version of the kubeconfig token.
                required: false
    dest:
        description: The complete file path of the file to which kubeconfig content should be written.
        required: false
    force:
        description: Whether to force overwrite an existing kubeconfig file.
        required: false
        default: false
        aliases: ['overwrite']
        type: bool
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Create a kubeconfig for a cluster
  oci_kubeconfig:
    cluster_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
    create_cluster_kubeconfig_content_details:
        expiration: 600
    dest: "/usr/local/my_kubeconfig"
"""

RETURN = """
kubeconfig:
    description: kubeconfig content
    returned: always
    type: dict
    sample: {
            kubeconfig: "apiVersion: v1\nclusters:\n- cluster:\n    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJ
            Q0FURS0tLS0tCk1JSURqRENDQW5TZ....."
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle import oci_ce_utils
from ansible.module_utils._text import to_bytes
import os

try:
    from oci.container_engine.container_engine_client import ContainerEngineClient
    from oci.container_engine.models import CreateClusterKubeconfigContentDetails
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def create_kubeconfig(container_engine_client, module):
    result = dict(changed=False)
    kubeconfig_details = CreateClusterKubeconfigContentDetails()
    kubeconfig_param = module.params["create_cluster_kubeconfig_content_details"]
    if kubeconfig_param:
        for attribute in kubeconfig_details.attribute_map.keys():
            if kubeconfig_param.get(attribute, None):
                kubeconfig_details.attribute = kubeconfig_param[attribute]

    # Wait for cluster to be active before attempting to create kubeconfig.
    oci_ce_utils.wait_on_resource(
        container_engine_client,
        module,
        container_engine_client.get_cluster,
        {"cluster_id": module.params["cluster_id"]},
        states=["ACTIVE"],
    )

    result["kubeconfig"] = oci_utils.call_with_backoff(
        container_engine_client.create_kubeconfig,
        cluster_id=module.params["cluster_id"],
        create_cluster_kubeconfig_content_details=kubeconfig_details,
    ).data.content
    if module.params.get("dest"):
        dest = module.params.get("dest")
        if module.params.get("force") or not os.path.isfile(to_bytes(dest)):
            oci_utils.write_to_file(dest, result["kubeconfig"])
            result["changed"] = True

    return result


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cluster_id=dict(type="str", required=True),
            create_cluster_kubeconfig_content_details=dict(type="dict", required=False),
            dest=dict(type="str", required=False),
            force=dict(
                type="bool", required=False, default=False, aliases=["overwrite"]
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("force", True, ["dest"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    try:
        result = create_kubeconfig(container_engine_client, module)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
