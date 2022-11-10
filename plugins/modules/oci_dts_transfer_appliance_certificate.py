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
module: oci_dts_transfer_appliance_certificate
short_description: Manage a TransferApplianceCertificate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a TransferApplianceCertificate resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an X.509 certificate from a public key
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    id:
        description:
            - ID of the Transfer Job
        type: str
        required: true
    transfer_appliance_label:
        description:
            - Label of the Transfer Appliance
        type: str
        required: true
    public_key:
        description:
            - ""
        type: str
    state:
        description:
            - The state of the TransferApplianceCertificate.
            - Use I(state=present) to create a TransferApplianceCertificate.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create transfer_appliance_certificate
  oci_dts_transfer_appliance_certificate:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    transfer_appliance_label: transfer_appliance_label_example

    # optional
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."

"""

RETURN = """
transfer_appliance_certificate:
    description:
        - Details of the TransferApplianceCertificate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        certificate:
            description:
                - ""
            returned: on success
            type: str
            sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    sample: {
        "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
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
    from oci.dts import TransferApplianceClient
    from oci.dts.models import TransferAppliancePublicKey

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferApplianceCertificateHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_possible_entity_types(self):
        return super(
            TransferApplianceCertificateHelperGen, self
        ).get_possible_entity_types() + [
            "transferappliancecertificate",
            "transferappliancecertificates",
            "dtstransferappliancecertificate",
            "dtstransferappliancecertificates",
            "transferappliancecertificateresource",
            "transferappliancecertificatesresource",
            "admincredential",
            "admincredentials",
            "dtsadmincredential",
            "dtsadmincredentials",
            "admincredentialresource",
            "admincredentialsresource",
            "dts",
        ]

    def get_get_fn(self):
        return self.client.get_transfer_appliance_certificate_authority_certificate

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_appliance_certificate_authority_certificate,
            id=self.module.params.get("id"),
            transfer_appliance_label=self.module.params.get("transfer_appliance_label"),
        )

    def get_create_model_class(self):
        return TransferAppliancePublicKey

    def get_exclude_attributes(self):
        return ["public_key"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_transfer_appliance_admin_credentials,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_appliance_label=self.module.params.get(
                    "transfer_appliance_label"
                ),
                admin_public_key=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


TransferApplianceCertificateHelperCustom = get_custom_class(
    "TransferApplianceCertificateHelperCustom"
)


class ResourceHelper(
    TransferApplianceCertificateHelperCustom, TransferApplianceCertificateHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            id=dict(type="str", required=True),
            transfer_appliance_label=dict(type="str", required=True),
            public_key=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transfer_appliance_certificate",
        service_client_class=TransferApplianceClient,
        namespace="dts",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
