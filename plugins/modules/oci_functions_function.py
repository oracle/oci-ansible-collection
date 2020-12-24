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
module: oci_functions_function
short_description: Manage a Function resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Function resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new function.
    - "This resource has the following action operations in the M(oci_function_actions) module: invoke."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The display name of the function. The display name must be unique within the application containing the function. Avoid entering confidential
              information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    application_id:
        description:
            - The OCID of the application this function belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    image:
        description:
            - "The qualified name of the Docker image to use in the function, including the image tag.
              The image should be in the OCI Registry that is in the same region as the function itself.
              Example: `phx.ocir.io/ten/functions/function:0.0.1`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    image_digest:
        description:
            - "The image digest for the version of the image that will be pulled when invoking this function.
              If no value is specified, the digest currently associated with the image in the OCI Registry will be used.
              Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`"
            - This parameter is updatable.
        type: str
    memory_in_mbs:
        description:
            - Maximum usable memory for the function (MiB).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    config:
        description:
            - Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values.
              Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values
              should be limited to printable unicode characters.
            - "Example: `{\\"MY_FUNCTION_CONFIG\\": \\"ConfVal\\"}`"
            - The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key
              and value in UTF-8.
            - This parameter is updatable.
        type: dict
    timeout_in_seconds:
        description:
            - Timeout for executions of the function. Value in seconds.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    function_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this function.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Function.
            - Use I(state=present) to create or update a Function.
            - Use I(state=absent) to delete a Function.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create function
  oci_functions_function:
    application_id: application_OCID
    display_name: Example Function
    image: phx.ocir.io/example-namespace/example-repo/example-image:0.0.1
    memory_in_mbs: 128

- name: Update function using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_functions_function:
    image: phx.ocir.io/ten/functions/function:0.0.1
    image_digest: sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7
    memory_in_mbs: 56
    timeout_in_seconds: 56
    display_name: myfunction
    config:
      EXAMPLE_KEY: example-value

- name: Update function
  oci_functions_function:
    function_id: ocid1.function.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete function
  oci_functions_function:
    function_id: ocid1.function.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete function using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_functions_function:
    display_name: Example Function
    application_id: application_OCID
    state: absent

"""

RETURN = """
function:
    description:
        - Details of the Function resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of the function. The display name is unique within the application containing the function.
            returned: on success
            type: string
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the function.
            returned: on success
            type: string
            sample: CREATING
        application_id:
            description:
                - The OCID of the application the function belongs to.
            returned: on success
            type: string
            sample: ocid1.application.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment that contains the function.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        image:
            description:
                - "The qualified name of the Docker image to use in the function, including the image tag.
                  The image should be in the OCI Registry that is in the same region as the function itself.
                  Example: `phx.ocir.io/ten/functions/function:0.0.1`"
            returned: on success
            type: string
            sample: phx.ocir.io/ten/functions/function:0.0.1
        image_digest:
            description:
                - "The image digest for the version of the image that will be pulled when invoking this function.
                  If no value is specified, the digest currently associated with the image in the OCI Registry will be used.
                  Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`"
            returned: on success
            type: string
            sample: sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7
        memory_in_mbs:
            description:
                - Maximum usable memory for the function (MiB).
            returned: on success
            type: int
            sample: 56
        config:
            description:
                - Function configuration. Overrides application configuration.
                  Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values
                  should be limited to printable unicode characters.
                - "Example: `{\\"MY_FUNCTION_CONFIG\\": \\"ConfVal\\"}`"
                - The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each
                  key and value in UTF-8.
            returned: on success
            type: dict
            sample: {}
        timeout_in_seconds:
            description:
                - Timeout for executions of the function. Value in seconds.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        invoke_endpoint:
            description:
                - The base https invoke URL to set on a client in order to invoke a function. This URL will never change over the lifetime of the function and
                  can be cached.
            returned: on success
            type: string
            sample: invoke_endpoint_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        time_created:
            description:
                - The time the function was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2018-09-12T22:47:12.613Z
        time_updated:
            description:
                - The time the function was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2018-09-12T22:47:12.613Z
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "application_id": "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "image": "phx.ocir.io/ten/functions/function:0.0.1",
        "image_digest": "sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7",
        "memory_in_mbs": 56,
        "config": {},
        "timeout_in_seconds": 56,
        "freeform_tags": {'Department': 'Finance'},
        "invoke_endpoint": "invoke_endpoint_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "time_created": "2018-09-12T22:47:12.613Z",
        "time_updated": "2018-09-12T22:47:12.613Z"
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
    from oci.functions import FunctionsManagementClient
    from oci.functions.models import CreateFunctionDetails
    from oci.functions.models import UpdateFunctionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FunctionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "function_id"

    def get_module_resource_id(self):
        return self.module.params.get("function_id")

    def get_get_fn(self):
        return self.client.get_function

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_function, function_id=self.module.params.get("function_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "application_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_functions, **kwargs)

    def get_create_model_class(self):
        return CreateFunctionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_function,
            call_fn_args=(),
            call_fn_kwargs=dict(create_function_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateFunctionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_function,
            call_fn_args=(),
            call_fn_kwargs=dict(
                function_id=self.module.params.get("function_id"),
                update_function_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_function,
            call_fn_args=(),
            call_fn_kwargs=dict(function_id=self.module.params.get("function_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


FunctionHelperCustom = get_custom_class("FunctionHelperCustom")


class ResourceHelper(FunctionHelperCustom, FunctionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            application_id=dict(type="str"),
            image=dict(type="str"),
            image_digest=dict(type="str"),
            memory_in_mbs=dict(type="int"),
            config=dict(type="dict"),
            timeout_in_seconds=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            function_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="function",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
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
