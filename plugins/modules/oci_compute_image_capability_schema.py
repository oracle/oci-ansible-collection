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
module: oci_compute_image_capability_schema
short_description: Manage a ComputeImageCapabilitySchema resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ComputeImageCapabilitySchema resource in Oracle Cloud Infrastructure
    - For I(state=present), creates compute image capability schema.
    - "This resource has the following action operations in the M(oci_compute_image_capability_schema_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the resource.
            - Required for create using I(state=present).
        type: str
    compute_global_image_capability_schema_version_name:
        description:
            - The name of the compute global image capability schema version
            - Required for create using I(state=present).
        type: str
    image_id:
        description:
            - The ocid of the image
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name for the compute image capability schema
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    schema_data:
        description:
            - The map of each capability name to its ImageCapabilitySchemaDescriptor.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            descriptor_type:
                description:
                    - The image capability schema descriptor type for the capability
                type: str
                choices:
                    - "enumstring"
                    - "enuminteger"
                    - "boolean"
                required: true
            source:
                description:
                    - ""
                type: str
                choices:
                    - "GLOBAL"
                    - "IMAGE"
                required: true
            enum_string_values:
                description:
                    - the list of values for the enum
                    - Required when descriptor_type is 'enumstring'
                type: list
                elements: str
            enum_string_default_value:
                description:
                    - the default value
                    - Applicable when descriptor_type is 'enumstring'
                type: str
            enum_integer_values:
                description:
                    - the list of values for the enum
                    - Required when descriptor_type is 'enuminteger'
                type: list
                elements: int
            enum_integer_default_value:
                description:
                    - the default value
                    - Applicable when descriptor_type is 'enuminteger'
                type: int
            boolean_default_value:
                description:
                    - the default value
                    - Applicable when descriptor_type is 'boolean'
                type: bool
    compute_image_capability_schema_id:
        description:
            - The id of the compute image capability schema or the image ocid
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ComputeImageCapabilitySchema.
            - Use I(state=present) to create or update a ComputeImageCapabilitySchema.
            - Use I(state=absent) to delete a ComputeImageCapabilitySchema.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create compute_image_capability_schema
  oci_compute_image_capability_schema:
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    compute_global_image_capability_schema_version_name: "2c0xx226-xxx-xxxx-xxxx-193cc17xx90b"
    schema_data:
      Compute.LaunchMode:
        descriptor_type: "enumstring"
        source: "IMAGE"
        enum_string_values:
        - "EMULATED"
        - "PARAVIRTUALIZED"
        - "CUSTOM"
        enum_string_default_value: "PARAVIRTUALIZED"

- name: Update compute_image_capability_schema using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_image_capability_schema:
    compute_image_capability_schema_id: "ocid1.computeimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
    schema_data:
      Storage.ConsistentVolumeNaming:
        descriptor_type: "boolean"
        source: "IMAGE"
        enum_string_default_value: true

- name: Update compute_image_capability_schema
  oci_compute_image_capability_schema:
    compute_image_capability_schema_id: "ocid1.computeimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete compute_image_capability_schema
  oci_compute_image_capability_schema:
    compute_image_capability_schema_id: "ocid1.computeimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete compute_image_capability_schema using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_image_capability_schema:
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient
    from oci.core.models import CreateComputeImageCapabilitySchemaDetails
    from oci.core.models import UpdateComputeImageCapabilitySchemaDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputeImageCapabilitySchemaHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "image_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_compute_image_capability_schemas, **kwargs
        )

    def get_create_model_class(self):
        return CreateComputeImageCapabilitySchemaDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_compute_image_capability_schema,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_compute_image_capability_schema_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateComputeImageCapabilitySchemaDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_compute_image_capability_schema,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compute_image_capability_schema_id=self.module.params.get(
                    "compute_image_capability_schema_id"
                ),
                update_compute_image_capability_schema_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_compute_image_capability_schema,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compute_image_capability_schema_id=self.module.params.get(
                    "compute_image_capability_schema_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ComputeImageCapabilitySchemaHelperCustom = get_custom_class(
    "ComputeImageCapabilitySchemaHelperCustom"
)


class ResourceHelper(
    ComputeImageCapabilitySchemaHelperCustom, ComputeImageCapabilitySchemaHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            compute_global_image_capability_schema_version_name=dict(type="str"),
            image_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            defined_tags=dict(type="dict"),
            schema_data=dict(type="dict"),
            compute_image_capability_schema_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
