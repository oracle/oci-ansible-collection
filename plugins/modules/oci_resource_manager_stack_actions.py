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
module: oci_resource_manager_stack_actions
short_description: Perform actions on a Stack resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Stack resource in Oracle Cloud Infrastructure
    - For I(action=detect_stack_drift), checks drift status for the specified stack.
version_added: "2.9"
author: Oracle (@oracle)
options:
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Stack.
        type: str
        required: true
        choices:
            - "detect_stack_drift"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action detect_stack_drift on stack
  oci_resource_manager_stack_actions:
    stack_id: ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx
    action: detect_stack_drift

"""

RETURN = """
stack:
    description:
        - Details of the Stack resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the stack.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the compartment where the stack is
                  located.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Human-readable name of the stack.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Description of the stack.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - "The date and time at which the stack was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The current lifecycle state of the stack.
                  For more information about stack lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#StackStates).
            returned: on success
            type: string
            sample: CREATING
        config_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                config_source_type:
                    description:
                        - The type of configuration source to use for the Terraform configuration.
                    returned: on success
                    type: string
                    sample: ZIP_UPLOAD
                working_directory:
                    description:
                        - File path to the directory to use for running Terraform.
                          If not specified, the root directory is used.
                          This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.
                    returned: on success
                    type: string
                    sample: working_directory_example
                configuration_source_provider_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Git configuration source.
                    returned: on success
                    type: string
                    sample: ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx
                repository_url:
                    description:
                        - The URL of the Git repository for the configuration source.
                    returned: on success
                    type: string
                    sample: repository_url_example
                branch_name:
                    description:
                        - The name of the branch in the Git repository for the configuration source.
                    returned: on success
                    type: string
                    sample: branch_name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to use
                          for creating the stack. The new stack will include definitions for supported
                          resource types in this compartment.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                region:
                    description:
                        - The region to use for creating the stack. The new stack will include definitions for
                          supported resource types in this region.
                    returned: on success
                    type: string
                    sample: region_example
                services_to_discover:
                    description:
                        - "Filter for L(services to use with Resource
                          Discovery,https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).
                          For example, \\"database\\" limits resource discovery to resource types within the Database service.
                          The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level
                          otherwise).
                          If not specified, then all services at the scope of the given compartment OCID are used."
                    returned: on success
                    type: list
                    sample: []
        variables:
            description:
                - "Terraform variables associated with this resource.
                  Maximum number of variables supported is 250.
                  The maximum size of each variable, including both name and value, is 4096 bytes.
                  Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
            returned: on success
            type: dict
            sample: {}
        terraform_version:
            description:
                - "The version of Terraform specified for the stack. Example: `0.12.x`"
            returned: on success
            type: string
            sample: 0.12.x
        stack_drift_status:
            description:
                - Drift status of the stack.
                  Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.
            returned: on success
            type: string
            sample: NOT_CHECKED
        time_drift_last_checked:
            description:
                - "The date and time when the drift detection was last executed.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
        freeform_tags:
            description:
                - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2020-01-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "config_source": {
            "config_source_type": "ZIP_UPLOAD",
            "working_directory": "working_directory_example",
            "configuration_source_provider_id": "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "branch_name": "branch_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "region": "region_example",
            "services_to_discover": []
        },
        "variables": {},
        "terraform_version": "0.12.x",
        "stack_drift_status": "NOT_CHECKED",
        "time_drift_last_checked": "2020-01-25T21:10:29.600Z",
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
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StackActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        detect_stack_drift
    """

    @staticmethod
    def get_module_resource_id_param():
        return "stack_id"

    def get_module_resource_id(self):
        return self.module.params.get("stack_id")

    def get_get_fn(self):
        return self.client.get_stack

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stack, stack_id=self.module.params.get("stack_id"),
        )

    def detect_stack_drift(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detect_stack_drift,
            call_fn_args=(),
            call_fn_kwargs=dict(stack_id=self.module.params.get("stack_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


StackActionsHelperCustom = get_custom_class("StackActionsHelperCustom")


class ResourceHelper(StackActionsHelperCustom, StackActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            stack_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["detect_stack_drift"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stack",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
