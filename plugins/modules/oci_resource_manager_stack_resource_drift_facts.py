#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_resource_manager_stack_resource_drift_facts
short_description: Fetches details about one or multiple StackResourceDrift resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple StackResourceDrift resources in Oracle Cloud Infrastructure
    - Lists drift status details for each resource defined in the specified stack.
      The drift status details for a given resource indicate differences, if any, between the actual state
      and the expected (defined) state for that resource.
version_added: "2.9"
author: Oracle (@oracle)
options:
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
        type: str
        required: true
    resource_drift_status:
        description:
            - "A filter that returns only resources that match the given drift status. The value is case-insensitive.
              Allowable values -
                - NOT_CHECKED
                - MODIFIED
                - IN_SYNC
                - DELETED"
        type: list
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List stack_resource_drifts
  oci_resource_manager_stack_resource_drift_facts:
    stack_id: ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
stack_resource_drifts:
    description:
        - List of StackResourceDrift resources
    returned: on success
    type: complex
    contains:
        stack_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
            returned: on success
            type: string
            sample: ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where the stack is located.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        resource_name:
            description:
                - The name of the resource as defined in the stack.
            returned: on success
            type: string
            sample: resource_name_example
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource provisioned by Terraform.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        resource_type:
            description:
                - "The provider resource type.
                  Must be supported by the L(Oracle Cloud Infrastructure provider,https://www.terraform.io/docs/providers/oci/index.html).
                  Example: `oci_core_instance`"
            returned: on success
            type: string
            sample: oci_core_instance
        resource_drift_status:
            description:
                - The drift status of the resource.
                  A drift status value indicates whether or not the actual state of the resource differs from the expected (defined) state for that resource.
            returned: on success
            type: string
            sample: NOT_CHECKED
        actual_properties:
            description:
                - "Actual values of properties that the stack defines for the indicated resource.
                  Each property and value is provided as a key-value pair.
                  The following example shows actual values for the resource's display name and server type:
                  `{\\"display_name\\": \\"tf-default-dhcp-options-new\\", \\"options.0.server_type\\": \\"VcnLocalPlusInternet\\"}`"
            returned: on success
            type: dict
            sample: {}
        expected_properties:
            description:
                - "Expected values of properties that the stack defines for the indicated resource.
                  Each property and value is provided as a key-value pair.
                  The following example shows expected (defined) values for the resource's display name and server type:
                  `{\\"display_name\\": \\"tf-default-dhcp-options\\", \\"options.0.server_type\\": \\"VcnLocalPlusInternet\\"}`"
            returned: on success
            type: dict
            sample: {}
        time_drift_checked:
            description:
                - "The date and time when the drift detection was executed.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
    sample: [{
        "stack_id": "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "oci_core_instance",
        "resource_drift_status": "NOT_CHECKED",
        "actual_properties": {},
        "expected_properties": {},
        "time_drift_checked": "2020-01-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
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


class StackResourceDriftFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "stack_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "resource_drift_status",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_stack_resource_drift_details,
            stack_id=self.module.params.get("stack_id"),
            **optional_kwargs
        )


StackResourceDriftFactsHelperCustom = get_custom_class(
    "StackResourceDriftFactsHelperCustom"
)


class ResourceFactsHelper(
    StackResourceDriftFactsHelperCustom, StackResourceDriftFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stack_id=dict(type="str", required=True),
            resource_drift_status=dict(type="list"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stack_resource_drift",
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

    module.exit_json(stack_resource_drifts=result)


if __name__ == "__main__":
    main()
