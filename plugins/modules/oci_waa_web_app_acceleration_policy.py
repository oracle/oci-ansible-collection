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
module: oci_waa_web_app_acceleration_policy
short_description: Manage a WebAppAccelerationPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a WebAppAccelerationPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new WebAppAccelerationPolicy.
    - "This resource has the following action operations in the M(oracle.oci.oci_waa_web_app_acceleration_policy_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - WebAppAccelerationPolicy display name, can be renamed.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    response_caching_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
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
                type: bool
    response_compression_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            gzip_compression:
                description:
                    - ""
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - "When true, support for gzip compression is enabled. HTTP responses will be compressed with gzip only if the
                              client indicates support for gzip via the \\"Accept-Encoding: gzip\\" request header."
                            - When false, support for gzip compression is disabled and HTTP responses will not be compressed with gzip
                              even if the client indicates support for gzip.
                        type: bool
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    system_tags:
        description:
            - "Usage of system tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            - This parameter is updatable.
        type: dict
    web_app_acceleration_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppAccelerationPolicy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the WebAppAccelerationPolicy.
            - Use I(state=present) to create or update a WebAppAccelerationPolicy.
            - Use I(state=absent) to delete a WebAppAccelerationPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create web_app_acceleration_policy
  oci_waa_web_app_acceleration_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    response_caching_policy:
      # optional
      is_response_header_based_caching_enabled: true
    response_compression_policy:
      # optional
      gzip_compression:
        # optional
        is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update web_app_acceleration_policy
  oci_waa_web_app_acceleration_policy:
    # required
    web_app_acceleration_policy_id: "ocid1.webappaccelerationpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    response_caching_policy:
      # optional
      is_response_header_based_caching_enabled: true
    response_compression_policy:
      # optional
      gzip_compression:
        # optional
        is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update web_app_acceleration_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waa_web_app_acceleration_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    response_caching_policy:
      # optional
      is_response_header_based_caching_enabled: true
    response_compression_policy:
      # optional
      gzip_compression:
        # optional
        is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Delete web_app_acceleration_policy
  oci_waa_web_app_acceleration_policy:
    # required
    web_app_acceleration_policy_id: "ocid1.webappaccelerationpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete web_app_acceleration_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waa_web_app_acceleration_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waa import WorkRequestClient
    from oci.waa import WaaClient
    from oci.waa.models import CreateWebAppAccelerationPolicyDetails
    from oci.waa.models import UpdateWebAppAccelerationPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppAccelerationPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(
            WebAppAccelerationPolicyHelperGen, self
        ).get_possible_entity_types() + [
            "webappaccelerationpolicy",
            "webappaccelerationpolicies",
            "waawebappaccelerationpolicy",
            "waawebappaccelerationpolicies",
            "webappaccelerationpolicyresource",
            "webappaccelerationpoliciesresource",
            "waa",
        ]

    def get_module_resource_id_param(self):
        return "web_app_acceleration_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("web_app_acceleration_policy_id")

    def get_get_fn(self):
        return self.client.get_web_app_acceleration_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_acceleration_policy,
            web_app_acceleration_policy_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_acceleration_policy,
            web_app_acceleration_policy_id=self.module.params.get(
                "web_app_acceleration_policy_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
        return oci_common_utils.list_all_resources(
            self.client.list_web_app_acceleration_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateWebAppAccelerationPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_web_app_acceleration_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_web_app_acceleration_policy_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateWebAppAccelerationPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_web_app_acceleration_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_policy_id=self.module.params.get(
                    "web_app_acceleration_policy_id"
                ),
                update_web_app_acceleration_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_web_app_acceleration_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_policy_id=self.module.params.get(
                    "web_app_acceleration_policy_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WebAppAccelerationPolicyHelperCustom = get_custom_class(
    "WebAppAccelerationPolicyHelperCustom"
)


class ResourceHelper(
    WebAppAccelerationPolicyHelperCustom, WebAppAccelerationPolicyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            response_caching_policy=dict(
                type="dict",
                options=dict(
                    is_response_header_based_caching_enabled=dict(type="bool")
                ),
            ),
            response_compression_policy=dict(
                type="dict",
                options=dict(
                    gzip_compression=dict(
                        type="dict", options=dict(is_enabled=dict(type="bool"))
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            web_app_acceleration_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
