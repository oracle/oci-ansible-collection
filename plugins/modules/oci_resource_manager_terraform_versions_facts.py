#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_resource_manager_terraform_versions_facts
short_description: Fetches details about one or multiple TerraformVersions resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TerraformVersions resources in Oracle Cloud Infrastructure
    - Returns a list of supported Terraform versions for use with stacks.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List terraform_versions
  oci_resource_manager_terraform_versions_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
terraform_versions:
    description:
        - List of TerraformVersions resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - "A supported Terraform version. Example: `0.12.x`"
            returned: on success
            type: str
            sample: name_example
        is_default:
            description:
                - Indicates whether this Terraform version is used by default in L(CreateStack,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack).
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "is_default": true
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


class TerraformVersionsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_terraform_versions, **optional_kwargs
        )


TerraformVersionsFactsHelperCustom = get_custom_class(
    "TerraformVersionsFactsHelperCustom"
)


class ResourceFactsHelper(
    TerraformVersionsFactsHelperCustom, TerraformVersionsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str"), name=dict(type="str"),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="terraform_versions",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(terraform_versions=result)


if __name__ == "__main__":
    main()
