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
module: oci_waas_captchas
short_description: Manage a Captchas resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Captchas resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    captchas:
        description:
            - A list of CAPTCHA details.
        type: list
        elements: dict
        required: true
        suboptions:
            url:
                description:
                    - The unique URL path at which to show the CAPTCHA challenge.
                    - This parameter is updatable.
                type: str
                required: true
            session_expiration_in_seconds:
                description:
                    - The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.
                    - This parameter is updatable.
                type: int
                required: true
            title:
                description:
                    - The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`
                    - This parameter is updatable.
                type: str
                required: true
            header_text:
                description:
                    - The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number of
                      attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the text from
                      the image below.'
                    - This parameter is updatable.
                type: str
            footer_text:
                description:
                    - The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as they are
                      shown in the image above.'
                    - This parameter is updatable.
                type: str
            failure_message:
                description:
                    - The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`
                    - This parameter is updatable.
                type: str
                required: true
            submit_label:
                description:
                    - The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.
                    - This parameter is updatable.
                type: str
                required: true
    state:
        description:
            - The state of the Captchas.
            - Use I(state=present) to update an existing a Captchas.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update captchas
  oci_waas_captchas:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    captchas:
    - # required
      url: url_example
      session_expiration_in_seconds: 56
      title: title_example
      failure_message: failure_message_example
      submit_label: submit_label_example

      # optional
      header_text: header_text_example
      footer_text: footer_text_example

"""

RETURN = """
captchas:
    description:
        - Details of the Captchas resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        url:
            description:
                - The unique URL path at which to show the CAPTCHA challenge.
            returned: on success
            type: str
            sample: url_example
        session_expiration_in_seconds:
            description:
                - The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.
            returned: on success
            type: int
            sample: 56
        title:
            description:
                - The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`
            returned: on success
            type: str
            sample: title_example
        header_text:
            description:
                - The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number of attempts
                  to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the text from the image
                  below.'
            returned: on success
            type: str
            sample: header_text_example
        footer_text:
            description:
                - The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as they are shown
                  in the image above.'
            returned: on success
            type: str
            sample: footer_text_example
        failure_message:
            description:
                - The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`
            returned: on success
            type: str
            sample: failure_message_example
        submit_label:
            description:
                - The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.
            returned: on success
            type: str
            sample: submit_label_example
    sample: {
        "url": "url_example",
        "session_expiration_in_seconds": 56,
        "title": "title_example",
        "header_text": "header_text_example",
        "footer_text": "footer_text_example",
        "failure_message": "failure_message_example",
        "submit_label": "submit_label_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import Captcha

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CaptchasHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(CaptchasHelperGen, self).get_possible_entity_types() + [
            "captchas",
            "captcha",
            "waascaptchas",
            "waascaptcha",
            "captchasresource",
            "captcharesource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "waas_policy_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_captchas, **kwargs)

    def get_update_model_class(self):
        return Captcha

    def get_update_model(self):
        if self.module.params.get("captchas"):
            return [
                oci_common_utils.convert_input_data_to_model_class(
                    resource, self.get_update_model_class()
                )
                for resource in self.module.params["captchas"]
            ]
        return []

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_captchas,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                captchas=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CaptchasHelperCustom = get_custom_class("CaptchasHelperCustom")


class ResourceHelper(CaptchasHelperCustom, CaptchasHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            captchas=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    url=dict(type="str", required=True),
                    session_expiration_in_seconds=dict(type="int", required=True),
                    title=dict(type="str", required=True),
                    header_text=dict(type="str"),
                    footer_text=dict(type="str"),
                    failure_message=dict(type="str", required=True),
                    submit_label=dict(type="str", required=True),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="captchas",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
