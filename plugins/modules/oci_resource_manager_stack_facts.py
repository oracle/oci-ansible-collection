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
module: oci_resource_manager_stack_facts
short_description: Fetches details about one or multiple Stack resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Stack resources in Oracle Cloud Infrastructure
    - "Lists stacks according to the specified filter.
      - If called using the compartment ID, returns all stacks in the specified compartment.
      - If called using the stack ID, returns the specified stack. (See also L(GetStack,https://docs.cloud.oracle.com/en-
        us/iaas/api/#/en/resourcemanager/latest/Stack/GetStack).)"
    - If I(stack_id) is specified, the details of a single Stack will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
            - Required to get a specific stack.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
    lifecycle_state:
        description:
            - A filter that returns only those resources that match the specified
              lifecycle state. The state value is case-insensitive.
              For more information about stack lifecycle states, see
              L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates).
            - "Allowable values:
              - CREATING
              - ACTIVE
              - DELETING
              - DELETED
              - FAILED"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list a resource by name.
              Requires `sortBy` set to `DISPLAYNAME`.
              Alternatively, when you know the resource OCID, use the related Get operation.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to use when sorting returned resources.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific stack
  oci_resource_manager_stack_facts:
    # required
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"

- name: List stacks
  oci_resource_manager_stack_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
stacks:
    description:
        - List of Stack resources
    returned: on success
    type: complex
    contains:
        config_source:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                workspace_id:
                    description:
                        - The id of the workspace in Bitbucket Cloud for the configuration source
                    returned: on success
                    type: str
                    sample: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"
                clone_url:
                    description:
                        - The clone URL of Bitbucket Server configuration source.
                    returned: on success
                    type: str
                    sample: clone_url_example
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
                project_id:
                    description:
                        - Unique identifier for a Bitbucket Server project.
                    returned: on success
                    type: str
                    sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
                repository_id:
                    description:
                        - Bitbucket Server repository identifier, usually identified as <repository>.git.
                    returned: on success
                    type: str
                    sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                configuration_source_provider_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Bitbucket Cloud configuration source.
                    returned: on success
                    type: str
                    sample: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
                repository_url:
                    description:
                        - The URL of the Bitbucket Cloud repository for the configuration source.
                    returned: on success
                    type: str
                    sample: repository_url_example
                branch_name:
                    description:
                        - The name of the branch in the Bitbucket Cloud repository for the configuration source.
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
                    sample: BITBUCKET_CLOUD_CONFIG_SOURCE
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
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        variables:
            description:
                - "Terraform variables associated with this resource.
                  Maximum number of variables supported is 250.
                  The maximum size of each variable, including both name and value, is 8192 bytes.
                  Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        stack_drift_status:
            description:
                - Drift status of the stack.
                  Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.
                - Returned for get operation
            returned: on success
            type: str
            sample: NOT_CHECKED
        time_drift_last_checked:
            description:
                - "The date and time when the drift detection was last executed.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        terraform_version:
            description:
                - "The version of Terraform specified for the stack. Example: `0.12.x`"
            returned: on success
            type: str
            sample: terraform_version_example
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
    sample: [{
        "config_source": {
            "workspace_id": "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx",
            "clone_url": "clone_url_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "services_to_discover": [],
            "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
            "configuration_source_provider_id": "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "branch_name": "branch_name_example",
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "config_source_type": "BITBUCKET_CLOUD_CONFIG_SOURCE",
            "working_directory": "working_directory_example"
        },
        "custom_terraform_provider": {
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example"
        },
        "is_third_party_provider_experience_enabled": true,
        "variables": {},
        "stack_drift_status": "NOT_CHECKED",
        "time_drift_last_checked": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "terraform_version": "terraform_version_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StackFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "stack_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stack, stack_id=self.module.params.get("stack_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_stacks, **optional_kwargs
        )


StackFactsHelperCustom = get_custom_class("StackFactsHelperCustom")


class ResourceFactsHelper(StackFactsHelperCustom, StackFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stack_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stack",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(stacks=result)


if __name__ == "__main__":
    main()
