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
module: oci_resource_manager_stack_associated_resource_facts
short_description: Fetches details about one or multiple StackAssociatedResource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple StackAssociatedResource resources in Oracle Cloud Infrastructure
    - Gets the list of resources associated with the specified stack.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
        type: str
        required: true
    terraform_resource_type:
        description:
            - A filter to return only specified resource types.
              For more information about resource types supported for the Oracle Cloud Infrastructure L(OCI] provider, see [Oracle Cloud Infrastructure
              Provider,https://registry.terraform.io/providers/oracle/oci/latest/docs).
        type: str
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List stack_associated_resources
  oci_resource_manager_stack_associated_resource_facts:
    # required
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    terraform_resource_type: terraform_resource_type_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
stack_associated_resources:
    description:
        - List of StackAssociatedResource resources
    returned: on success
    type: complex
    contains:
        resource_id:
            description:
                - Unique identifier for the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_name:
            description:
                - Name of the resource.
            returned: on success
            type: str
            sample: resource_name_example
        resource_type:
            description:
                - Resource type. For more information about resource types supported for the Oracle Cloud Infrastructure (OCI) provider, see L(Oracle Cloud
                  Infrastructure Provider,https://registry.terraform.io/providers/oracle/oci/latest/docs).
            returned: on success
            type: str
            sample: resource_type_example
        attributes:
            description:
                - "Resource attribute values. Each value is represented as a key-value pair.
                  Example: `{\\"state\\": \\"AVAILABLE\\"}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - "The date and time when the stack was created.
                  Format is defined by RFC3339.
                  Example: `2022-07-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        region:
            description:
                - "Resource region.
                  For information about regions, see L(Regions and Availability
                  Domains,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
                  Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        resource_address:
            description:
                - Terraform resource address.
            returned: on success
            type: str
            sample: resource_address_example
    sample: [{
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "resource_type": "resource_type_example",
        "attributes": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "region": "us-phoenix-1",
        "resource_address": "resource_address_example"
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


class StackAssociatedResourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "stack_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "terraform_resource_type",
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_stack_associated_resources,
            stack_id=self.module.params.get("stack_id"),
            **optional_kwargs
        )


StackAssociatedResourceFactsHelperCustom = get_custom_class(
    "StackAssociatedResourceFactsHelperCustom"
)


class ResourceFactsHelper(
    StackAssociatedResourceFactsHelperCustom, StackAssociatedResourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stack_id=dict(type="str", required=True),
            terraform_resource_type=dict(type="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stack_associated_resource",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(stack_associated_resources=result)


if __name__ == "__main__":
    main()
