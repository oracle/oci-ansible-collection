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
module: oci_resource_manager_stack_tf_state_facts
short_description: Fetches details about a StackTfState resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a StackTfState resource in Oracle Cloud Infrastructure
    - Returns the Terraform state for the specified stack.
version_added: "2.9"
author: Oracle (@oracle)
options:
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific stack_tf_state
  oci_resource_manager_stack_tf_state_facts:
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
stack_tf_state:
    description:
        - StackTfState resource
    returned: on success
    type: str
    sample: "sample"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StackTfStateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "stack_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stack_tf_state, stack_id=self.module.params.get("stack_id"),
        )

    def get(self):
        response_data = self.get_resource().data
        return to_text(response_data)


StackTfStateFactsHelperCustom = get_custom_class("StackTfStateFactsHelperCustom")


class ResourceFactsHelper(StackTfStateFactsHelperCustom, StackTfStateFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(stack_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stack_tf_state",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(stack_tf_state=result)


if __name__ == "__main__":
    main()
