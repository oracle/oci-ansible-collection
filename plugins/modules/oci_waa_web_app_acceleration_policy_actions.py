#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_waa_web_app_acceleration_policy_actions
short_description: Perform actions on a WebAppAccelerationPolicy resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a WebAppAccelerationPolicy resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a WebAppAccelerationfPolicy resource from one compartment to another.
      When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    web_app_acceleration_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppAccelerationPolicy.
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
            - The action to perform on the WebAppAccelerationPolicy.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on web_app_acceleration_policy
  oci_waa_web_app_acceleration_policy_actions:
    # required
    web_app_acceleration_policy_id: "ocid1.webappaccelerationpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
web_app_acceleration_policy:
    description:
        - Details of the WebAppAccelerationPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppAccelerationPolicy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - WebAppAccelerationPolicy display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the WebAppAccelerationPolicy was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the WebAppAccelerationPolicy was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the WebAppAccelerationPolicy.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in FAILED state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        response_caching_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_response_header_based_caching_enabled:
                    description:
                        - When false, responses will not be cached by the backend based on response headers.
                        - When true, responses that contain one of the supported cache control headers will be cached according to the
                          values specified in the cache control headers.
                        - "The \\"X-Accel-Expires\\" header field sets caching time of a response in seconds. The zero value disables
                          caching for a response. If the value starts with the @ prefix, it sets an absolute time in seconds since
                          Epoch, up to which the response may be cached."
                        - "If the header does not include the \\"X-Accel-Expires\\" field, parameters of caching may be set in the header
                          fields \\"Expires\\" or \\"Cache-Control\\"."
                        - "If the header includes the \\"Set-Cookie\\" field, such a response will not be cached."
                        - "If the header includes the \\"Vary\\" field with the special value \\"*\\", such a response will not be cached. If the
                          header includes the \\"Vary\\" field with another value, such a response will be cached taking into account the
                          corresponding request header fields."
                    returned: on success
                    type: bool
                    sample: true
        response_compression_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                gzip_compression:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - "When true, support for gzip compression is enabled. HTTP responses will be compressed with gzip only if the
                                  client indicates support for gzip via the \\"Accept-Encoding: gzip\\" request header."
                                - When false, support for gzip compression is disabled and HTTP responses will not be compressed with gzip
                                  even if the client indicates support for gzip.
                            returned: on success
                            type: bool
                            sample: true
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
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "response_caching_policy": {
            "is_response_header_based_caching_enabled": true
        },
        "response_compression_policy": {
            "gzip_compression": {
                "is_enabled": true
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.waa import WorkRequestClient
    from oci.waa import WaaClient
    from oci.waa.models import ChangeWebAppAccelerationPolicyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppAccelerationPolicyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "web_app_acceleration_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("web_app_acceleration_policy_id")

    def get_get_fn(self):
        return self.client.get_web_app_acceleration_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_acceleration_policy,
            web_app_acceleration_policy_id=self.module.params.get(
                "web_app_acceleration_policy_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeWebAppAccelerationPolicyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_web_app_acceleration_policy_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_policy_id=self.module.params.get(
                    "web_app_acceleration_policy_id"
                ),
                change_web_app_acceleration_policy_compartment_details=action_details,
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


WebAppAccelerationPolicyActionsHelperCustom = get_custom_class(
    "WebAppAccelerationPolicyActionsHelperCustom"
)


class ResourceHelper(
    WebAppAccelerationPolicyActionsHelperCustom,
    WebAppAccelerationPolicyActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            web_app_acceleration_policy_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="web_app_acceleration_policy",
        service_client_class=WaaClient,
        namespace="waa",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
