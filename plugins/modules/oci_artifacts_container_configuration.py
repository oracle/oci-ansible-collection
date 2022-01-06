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
module: oci_artifacts_container_configuration
short_description: Manage a ContainerConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a ContainerConfiguration resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    is_repository_created_on_first_push:
        description:
            - Whether to create a new container repository when a container is pushed to a new repository path.
              Repositories created in this way belong to the root compartment.
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the ContainerConfiguration.
            - Use I(state=present) to update an existing a ContainerConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update container_configuration
  oci_artifacts_container_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_repository_created_on_first_push: true

"""

RETURN = """
container_configuration:
    description:
        - Details of the ContainerConfiguration resource acted upon by the current operation
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
            type: str
            sample: namespace_example
    sample: {
        "is_repository_created_on_first_push": true,
        "namespace": "namespace_example"
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
    from oci.artifacts import ArtifactsClient
    from oci.artifacts.models import UpdateContainerConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_get_fn(self):
        return self.client.get_container_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_update_model_class(self):
        return UpdateContainerConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_container_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                update_container_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


ContainerConfigurationHelperCustom = get_custom_class(
    "ContainerConfigurationHelperCustom"
)


class ResourceHelper(
    ContainerConfigurationHelperCustom, ContainerConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            is_repository_created_on_first_push=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="container_configuration",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
