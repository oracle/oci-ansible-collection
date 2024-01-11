#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_container_engine_credential_rotation_status_facts
short_description: Fetches details about a CredentialRotationStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CredentialRotationStatus resource in Oracle Cloud Infrastructure
    - Get cluster credential rotation status.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific credential_rotation_status
  oci_container_engine_credential_rotation_status_facts:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
credential_rotation_status:
    description:
        - CredentialRotationStatus resource
    returned: on success
    type: complex
    contains:
        time_auto_completion_scheduled:
            description:
                - The time by which retirement of old credentials should start.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        status:
            description:
                - "Credential rotation status of a kubernetes cluster
                  IN_PROGRESS: Issuing new credentials to kubernetes cluster control plane and worker nodes or retiring old credentials from kubernetes cluster
                  control plane and worker nodes.
                  WAITING: Waiting for customer to invoke the complete rotation action or the automcatic complete rotation action.
                  COMPLETED: New credentials are functional on kuberentes cluster."
            returned: on success
            type: str
            sample: IN_PROGRESS
        status_details:
            description:
                - "Details of a kuberenetes cluster credential rotation status:
                  ISSUING_NEW_CREDENTIALS: Credential rotation is in progress. Starting to issue new credentials to kubernetes cluster control plane and worker
                  nodes.
                  NEW_CREDENTIALS_ISSUED: New credentials are added. At this stage cluster has both old and new credentials and is awaiting old credentials
                  retirement.
                  RETIRING_OLD_CREDENTIALS: Retirement of old credentials is in progress. Starting to remove old credentials from kubernetes cluster control
                  plane and worker nodes.
                  COMPLETED: Credential rotation is complete. Old credentials are retired."
            returned: on success
            type: str
            sample: ISSUING_NEW_CREDENTIALS
    sample: {
        "time_auto_completion_scheduled": "2013-10-20T19:20:30+01:00",
        "status": "IN_PROGRESS",
        "status_details": "ISSUING_NEW_CREDENTIALS"
    }
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


class CredentialRotationStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_credential_rotation_status,
            cluster_id=self.module.params.get("cluster_id"),
        )


CredentialRotationStatusFactsHelperCustom = get_custom_class(
    "CredentialRotationStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    CredentialRotationStatusFactsHelperCustom, CredentialRotationStatusFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(cluster_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="credential_rotation_status",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(credential_rotation_status=result)


if __name__ == "__main__":
    main()
