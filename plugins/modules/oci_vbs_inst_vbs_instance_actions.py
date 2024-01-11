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
module: oci_vbs_inst_vbs_instance_actions
short_description: Perform actions on a VbsInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VbsInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a VbsInstance resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vbs_instance_id:
        description:
            - unique VbsInstance identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the VbsInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on vbs_instance
  oci_vbs_inst_vbs_instance_actions:
    # required
    vbs_instance_id: "ocid1.vbsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
vbs_instance:
    description:
        - Details of the VbsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Service instance name (unique identifier)
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Service instance display name
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment of the service instance
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_resource_usage_agreement_granted:
            description:
                - Whether the VBS service instance owner explicitly approved VBS to create and use resources in the customer tenancy
            returned: on success
            type: bool
            sample: true
        resource_compartment_id:
            description:
                - Compartment where VBS may create additional resources for the service instance
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        vbs_access_url:
            description:
                - Public web URL for accessing the VBS service instance
            returned: on success
            type: str
            sample: vbs_access_url_example
        time_created:
            description:
                - The time the the VbsInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the VbsInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the VbsInstance.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_resource_usage_agreement_granted": true,
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vbs_access_url": "vbs_access_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.vbs_inst import VbsInstanceClient
    from oci.vbs_inst.models import ChangeVbsInstanceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VbsInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "vbs_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("vbs_instance_id")

    def get_get_fn(self):
        return self.client.get_vbs_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vbs_instance,
            vbs_instance_id=self.module.params.get("vbs_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVbsInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_vbs_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vbs_instance_id=self.module.params.get("vbs_instance_id"),
                change_vbs_instance_compartment_details=action_details,
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


VbsInstanceActionsHelperCustom = get_custom_class("VbsInstanceActionsHelperCustom")


class ResourceHelper(VbsInstanceActionsHelperCustom, VbsInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            vbs_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vbs_instance",
        service_client_class=VbsInstanceClient,
        namespace="vbs_inst",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
