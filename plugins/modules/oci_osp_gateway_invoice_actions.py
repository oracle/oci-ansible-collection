#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_osp_gateway_invoice_actions
short_description: Perform actions on an Invoice resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Invoice resource in Oracle Cloud Infrastructure
    - For I(action=download_pdf_content), returns an invoice in pdf format
    - For I(action=pay), pay an invoice
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
            - Required for I(action=download_pdf_content).
        type: str
    osp_home_region:
        description:
            - The home region's public name of the logged in user.
        type: str
        required: true
    internal_invoice_id:
        description:
            - The identifier of the invoice.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    language_code:
        description:
            - Language code
            - Applicable only for I(action=pay).
        type: str
    return_url:
        description:
            - Callback URL
            - Applicable only for I(action=pay).
        type: str
    email:
        description:
            - User email
            - Required for I(action=pay).
        type: str
    action:
        description:
            - The action to perform on the Invoice.
        type: str
        required: true
        choices:
            - "download_pdf_content"
            - "pay"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action download_pdf_content on invoice
  oci_osp_gateway_invoice_actions:
    # required
    dest: /tmp/myfile
    osp_home_region: us-phoenix-1
    internal_invoice_id: "ocid1.internalinvoice.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: download_pdf_content

- name: Perform action pay on invoice
  oci_osp_gateway_invoice_actions:
    # required
    osp_home_region: us-phoenix-1
    internal_invoice_id: "ocid1.internalinvoice.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    email: email_example
    action: pay

    # optional
    language_code: language_code_example
    return_url: return_url_example

"""

RETURN = """
pay_invoice_receipt:
    description:
        - Details of the Invoice resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        url:
            description:
                - Url of the Payment Service
            returned: on success
            type: str
            sample: url_example
        header_id:
            description:
                - Payment header id
            returned: on success
            type: str
            sample: "ocid1.header.oc1..xxxxxxEXAMPLExxxxxx"
        token:
            description:
                - Token created for Payment Service
            returned: on success
            type: str
            sample: token_example
    sample: {
        "url": "url_example",
        "header_id": "ocid1.header.oc1..xxxxxxEXAMPLExxxxxx",
        "token": "token_example"
    }
"""

from ansible.module_utils._text import to_bytes
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
    from oci.osp_gateway import InvoiceServiceClient
    from oci.osp_gateway.models import PayInvoiceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InvoiceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        download_pdf_content
        pay
    """

    @staticmethod
    def get_module_resource_id_param():
        return "internal_invoice_id"

    def get_module_resource_id(self):
        return self.module.params.get("internal_invoice_id")

    def get_get_fn(self):
        return self.client.get_invoice

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_invoice,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            internal_invoice_id=self.module.params.get("internal_invoice_id"),
        )

    def download_pdf_content(self):
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.download_pdf_content,
            call_fn_args=(),
            call_fn_kwargs=dict(
                osp_home_region=self.module.params.get("osp_home_region"),
                compartment_id=self.module.params.get("compartment_id"),
                internal_invoice_id=self.module.params.get("internal_invoice_id"),
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None

    def pay(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PayInvoiceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.pay_invoice,
            call_fn_args=(),
            call_fn_kwargs=dict(
                osp_home_region=self.module.params.get("osp_home_region"),
                internal_invoice_id=self.module.params.get("internal_invoice_id"),
                compartment_id=self.module.params.get("compartment_id"),
                pay_invoice_details=action_details,
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


InvoiceActionsHelperCustom = get_custom_class("InvoiceActionsHelperCustom")


class ResourceHelper(InvoiceActionsHelperCustom, InvoiceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            dest=dict(type="str"),
            osp_home_region=dict(type="str", required=True),
            internal_invoice_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            language_code=dict(type="str"),
            return_url=dict(type="str"),
            email=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["download_pdf_content", "pay"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="invoice",
        service_client_class=InvoiceServiceClient,
        namespace="osp_gateway",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
