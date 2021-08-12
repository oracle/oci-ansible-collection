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
module: oci_artifacts_container_configuration_facts
short_description: Fetches details about a ContainerConfiguration resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ContainerConfiguration resource in Oracle Cloud Infrastructure
    - Get container configuration.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific container_configuration
  oci_artifacts_container_configuration_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
container_configuration:
    description:
        - ContainerConfiguration resource
    returned: on success
    type: complex
    contains:
        is_repository_created_on_first_push:
            description:
                - Whether to create a new container repository when a container is pushed to a new repository path.
                  Repositories created in this way belong to the root compartment.
            returned: on success
            type: bool
            sample: true
        namespace:
            description:
                - The tenancy namespace used in the container repository path.
            returned: on success
            type: string
            sample: namespace_example
    sample: {
        "is_repository_created_on_first_push": true,
        "namespace": "namespace_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.artifacts import ArtifactsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )


ContainerConfigurationFactsHelperCustom = get_custom_class(
    "ContainerConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    ContainerConfigurationFactsHelperCustom, ContainerConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="container_configuration",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(container_configuration=result)


if __name__ == "__main__":
    main()
