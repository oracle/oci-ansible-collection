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
module: oci_waas_captchas_facts
short_description: Fetches details about one or multiple Captchas resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Captchas resources in Oracle Cloud Infrastructure
    - Gets the list of currently configured CAPTCHA challenges in the Web
      Application Firewall configuration of a WAAS policy.
    - The order of the CAPTCHA challenges is important. The URL for each
      CAPTCHA will be checked in the order they are created.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List captchas
  oci_waas_captchas_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
captchas:
    description:
        - List of Captchas resources
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
    sample: [{
        "url": "url_example",
        "session_expiration_in_seconds": 56,
        "title": "title_example",
        "header_text": "header_text_example",
        "footer_text": "footer_text_example",
        "failure_message": "failure_message_example",
        "submit_label": "submit_label_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CaptchasFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_captchas,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


CaptchasFactsHelperCustom = get_custom_class("CaptchasFactsHelperCustom")


class ResourceFactsHelper(CaptchasFactsHelperCustom, CaptchasFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(waas_policy_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="captchas",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(captchas=result)


if __name__ == "__main__":
    main()
