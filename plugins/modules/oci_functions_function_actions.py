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
module: oci_functions_function_actions
short_description: Perform actions on a Function resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Function resource in Oracle Cloud Infrastructure
    - For I(action=invoke), invokes a function
version_added: "2.9"
author: Oracle (@oracle)
options:
    function_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this function.
        type: str
        aliases: ["id"]
        required: true
    invoke_function_body:
        description:
            - "The body of the function invocation.
              Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this
              limit."
        type: str
    fn_intent:
        description:
            - An optional intent header that indicates to the FDK the way the event should be interpreted. E.g. 'httprequest', 'cloudevent'.
        type: str
        choices:
            - "httprequest"
            - "cloudevent"
    fn_invoke_type:
        description:
            - Indicates whether the functions platform should execute the request directly and return the result ('sync') or
              whether the platform should enqueue the request for later processing and acknowledge that it has been processed ('detached').
        type: str
        choices:
            - "detached"
            - "sync"
    dest:
        description:
            - The destination file path to write the output of I(action=invoke). The file will be created if it does not exist. If the file already exists, the
              content will be overwritten.
        type: str
    action:
        description:
            - The action to perform on the Function.
        type: str
        required: true
        choices:
            - "invoke"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action invoke on function
  oci_functions_function_actions:
    function_id: ocid1.function.oc1..xxxxxxEXAMPLExxxxxx
    action: invoke

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.functions import FunctionsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FunctionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        invoke
    """

    @staticmethod
    def get_module_resource_id_param():
        return "function_id"

    def get_module_resource_id(self):
        return self.module.params.get("function_id")

    def get_get_fn(self):
        return self.client.get_function

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_function, function_id=self.module.params.get("function_id"),
        )

    def invoke(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.invoke_function,
            call_fn_args=(),
            call_fn_kwargs=dict(
                function_id=self.module.params.get("function_id"),
                invoke_function_body=self.module.params.get("invoke_function_body"),
                fn_intent=self.module.params.get("fn_intent"),
                fn_invoke_type=self.module.params.get("fn_invoke_type"),
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


FunctionActionsHelperCustom = get_custom_class("FunctionActionsHelperCustom")


class ResourceHelper(FunctionActionsHelperCustom, FunctionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            function_id=dict(aliases=["id"], type="str", required=True),
            invoke_function_body=dict(type="str"),
            fn_intent=dict(type="str", choices=["httprequest", "cloudevent"]),
            fn_invoke_type=dict(type="str", choices=["detached", "sync"]),
            dest=dict(type="str"),
            action=dict(type="str", required=True, choices=["invoke"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
