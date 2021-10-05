#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_compute_image_capability_schema_actions
short_description: Perform actions on a ComputeImageCapabilitySchema resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ComputeImageCapabilitySchema resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a compute image capability schema into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
              L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compute_image_capability_schema_id:
        description:
            - The id of the compute image capability schema or the image ocid
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to
              move the instance configuration to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ComputeImageCapabilitySchema.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on compute_image_capability_schema
  oci_compute_image_capability_schema_actions:
    compute_image_capability_schema_id: "ocid1.computeimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
compute_image_capability_schema:
    description:
        - Details of the ComputeImageCapabilitySchema resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The id of the compute global image capability schema version
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compute_global_image_capability_schema_id:
            description:
                - The ocid of the compute global image capability schema
            returned: on success
            type: str
            sample: "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
        compute_global_image_capability_schema_version_name:
            description:
                - The name of the compute global image capability schema version
            returned: on success
            type: str
            sample: compute_global_image_capability_schema_version_name_example
        image_id:
            description:
                - The OCID of the image associated with this compute image capability schema
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the compute global image capability schema
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        schema_data:
            description:
                - The map of each capability name to its ImageCapabilityDescriptor.
            returned: on success
            type: complex
            contains:
                descriptor_type:
                    description:
                        - The image capability schema descriptor type for the capability
                    returned: on success
                    type: str
                    sample: boolean
                source:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: GLOBAL
                boolean_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: bool
                    sample: true
                enum_integer_values:
                    description:
                        - the list of values for the enum
                    returned: on success
                    type: list
                    sample: []
                enum_integer_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: int
                    sample: 56
                enum_string_values:
                    description:
                        - the list of values for the enum
                    returned: on success
                    type: list
                    sample: []
                enum_string_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: str
                    sample: default_value_example
        time_created:
            description:
                - The date and time the compute image capability schema was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_global_image_capability_schema_id": "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_global_image_capability_schema_version_name": "compute_global_image_capability_schema_version_name_example",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "schema_data": {
            "descriptor_type": "boolean",
            "source": "GLOBAL",
            "boolean_default_value": true,
            "enum_integer_values": [],
            "enum_integer_default_value": 56,
            "enum_string_values": [],
            "enum_string_default_value": "default_value_example"
        },
        "time_created": "2016-08-25T21:10:29.600Z"
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
    from oci.core import ComputeClient
    from oci.core.models import ChangeComputeImageCapabilitySchemaCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputeImageCapabilitySchemaActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "compute_image_capability_schema_id"

    def get_module_resource_id(self):
        return self.module.params.get("compute_image_capability_schema_id")

    def get_get_fn(self):
        return self.client.get_compute_image_capability_schema

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_compute_image_capability_schema,
            compute_image_capability_schema_id=self.module.params.get(
                "compute_image_capability_schema_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeComputeImageCapabilitySchemaCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_compute_image_capability_schema_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compute_image_capability_schema_id=self.module.params.get(
                    "compute_image_capability_schema_id"
                ),
                change_compute_image_capability_schema_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ComputeImageCapabilitySchemaActionsHelperCustom = get_custom_class(
    "ComputeImageCapabilitySchemaActionsHelperCustom"
)


class ResourceHelper(
    ComputeImageCapabilitySchemaActionsHelperCustom,
    ComputeImageCapabilitySchemaActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compute_image_capability_schema_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="compute_image_capability_schema",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
