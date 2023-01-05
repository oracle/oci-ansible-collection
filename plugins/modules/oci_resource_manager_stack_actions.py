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
module: oci_resource_manager_stack_actions
short_description: Perform actions on a Stack resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Stack resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a stack (and its associated jobs) into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=detect_stack_drift), checks drift status for the specified stack.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              into which the Stack should be moved.
            - Required for I(action=change_compartment).
        type: str
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
        type: str
        aliases: ["id"]
        required: true
    resource_addresses:
        description:
            - "The list of resources in the specified stack to detect drift for. Each resource is identified by a resource address,
              which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index.
              For example, the resource address for the fourth Compute instance with the name \\"test_instance\\" is oci_core_instance.test_instanceL(3].
              For more details and examples of resource addresses, see the Terraform documentation at [Resource
              spec,https://www.terraform.io/docs/internals/resource-addressing.html#examples)."
            - Applicable only for I(action=detect_stack_drift).
        type: list
        elements: str
    is_provider_upgrade_required:
        description:
            - Specifies whether or not to upgrade provider versions.
              Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers.
              For more information about this option, see L(Dependency Lock File (terraform.io),https://www.terraform.io/language/files/dependency-lock).
            - Applicable only for I(action=detect_stack_drift).
        type: bool
    action:
        description:
            - The action to perform on the Stack.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "detect_stack_drift"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on stack
  oci_resource_manager_stack_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action detect_stack_drift on stack
  oci_resource_manager_stack_actions:
    # required
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"
    action: detect_stack_drift

    # optional
    resource_addresses: [ "resource_addresses_example" ]
    is_provider_upgrade_required: true

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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the compartment where the stack is
                  located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable name of the stack.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the stack.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The date and time at which the stack was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the stack.
                  For more information about stack lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates).
            returned: on success
            type: str
            sample: CREATING
        config_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to use
                          for creating the stack. The new stack will include definitions for supported
                          resource types in this compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                configuration_source_provider_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Git configuration source.
                    returned: on success
                    type: str
                    sample: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
                repository_url:
                    description:
                        - The URL of the Git repository for the configuration source.
                    returned: on success
                    type: str
                    sample: repository_url_example
                branch_name:
                    description:
                        - The name of the branch in the Git repository for the configuration source.
                    returned: on success
                    type: str
                    sample: branch_name_example
                region:
                    description:
                        - The region to use for creating the stack. The new stack will include definitions for
                          supported resource types in this region.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                namespace:
                    description:
                        - The Object Storage namespace that contains the bucket.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - "The name of the bucket that contains the Terraform configuration files.
                          Maximum file size (applies to each file in the bucket): 100 MB. (In a bucket, a file is an object.)"
                    returned: on success
                    type: str
                    sample: bucket_name_example
                config_source_type:
                    description:
                        - The type of configuration source to use for the Terraform configuration.
                    returned: on success
                    type: str
                    sample: COMPARTMENT_CONFIG_SOURCE
                working_directory:
                    description:
                        - File path to the directory to use for running Terraform.
                          If not specified, the root directory is used.
                          Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders.
                          Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.
                          For more information about required and recommended file structure, see
                          L(File Structure (Terraform Configurations for Resource
                          Manager),https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#filestructure).
                    returned: on success
                    type: str
                    sample: working_directory_example
        custom_terraform_provider:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - "The name of the region that contains the bucket you want.
                          For information about regions, see L(Regions and Availability
                          Domains,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
                          Example: `us-phoenix-1`"
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                namespace:
                    description:
                        - The Object Storage namespace that contains the bucket you want.
                          For information about Object Storage namespaces, see L(Understanding Object Storage
                          Namespaces,https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm).
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - The name of the bucket that contains the binary files for the custom Terraform providers.
                          For information about buckets, see L(Managing Buckets,https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm).
                    returned: on success
                    type: str
                    sample: bucket_name_example
        is_third_party_provider_experience_enabled:
            description:
                - When `true`, the stack sources third-party Terraform providers from
                  L(Terraform Registry,https://registry.terraform.io/browse/providers) and allows
                  L(custom providers,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/resourcemanager/latest/datatypes/CustomTerraformProvider).
                  For more information about stack sourcing of third-party Terraform providers, see
                  L(Third-party Provider
                  Configuration,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers).
            returned: on success
            type: bool
            sample: true
        variables:
            description:
                - "Terraform variables associated with this resource.
                  Maximum number of variables supported is 250.
                  The maximum size of each variable, including both name and value, is 8192 bytes.
                  Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
            returned: on success
            type: dict
            sample: {}
        terraform_version:
            description:
                - "The version of Terraform specified for the stack. Example: `0.12.x`"
            returned: on success
            type: str
            sample: terraform_version_example
        stack_drift_status:
            description:
                - Drift status of the stack.
                  Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.
            returned: on success
            type: str
            sample: NOT_CHECKED
        time_drift_last_checked:
            description:
                - "The date and time when the drift detection was last executed.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "config_source": {
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "services_to_discover": [],
            "configuration_source_provider_id": "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "branch_name": "branch_name_example",
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "config_source_type": "COMPARTMENT_CONFIG_SOURCE",
            "working_directory": "working_directory_example"
        },
        "custom_terraform_provider": {
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example"
        },
        "is_third_party_provider_experience_enabled": true,
        "variables": {},
        "terraform_version": "terraform_version_example",
        "stack_drift_status": "NOT_CHECKED",
        "time_drift_last_checked": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import ChangeStackCompartmentDetails
    from oci.resource_manager.models import DetectStackDriftDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StackActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeStackCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_stack_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stack_id=self.module.params.get("stack_id"),
                change_stack_compartment_details=action_details,
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

    def detect_stack_drift(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetectStackDriftDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detect_stack_drift,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stack_id=self.module.params.get("stack_id"),
                detect_stack_drift_details=action_details,
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


StackActionsHelperCustom = get_custom_class("StackActionsHelperCustom")


class ResourceHelper(StackActionsHelperCustom, StackActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            stack_id=dict(aliases=["id"], type="str", required=True),
            resource_addresses=dict(type="list", elements="str"),
            is_provider_upgrade_required=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "detect_stack_drift"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
