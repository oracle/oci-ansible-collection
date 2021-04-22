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
module: oci_waas_certificate_actions
short_description: Perform actions on a WaasCertificate resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a WaasCertificate resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves certificate into a different compartment. When provided, If-Match is checked against ETag values of the
      certificate.
      For information about moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    certificate_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SSL certificate used in the WAAS policy. This number is
              generated when the certificate is added to the policy.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
              For information about moving resources between compartments, see L(Moving Resources to a Different
              Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
        type: str
        required: true
    action:
        description:
            - The action to perform on the WaasCertificate.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on waas_certificate
  oci_waas_certificate_actions:
    compartment_id: "ocid1.compartment.oc1.."
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

"""

RETURN = """
waas_certificate:
    description:
        - Details of the WaasCertificate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the certificate.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the certificate's compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the certificate.
            returned: on success
            type: string
            sample: display_name_example
        issued_by:
            description:
                - ""
            returned: on success
            type: string
            sample: issued_by_example
        subject_name:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                country:
                    description:
                        - ISO 3166-1 alpha-2 code of the country where the organization is located. For a list of codes, see L(ISO's
                          website,https://www.iso.org/obp/ui/#search/code/).
                    returned: on success
                    type: string
                    sample: country_example
                state_province:
                    description:
                        - The province where the organization is located.
                    returned: on success
                    type: string
                    sample: state_province_example
                locality:
                    description:
                        - The city in which the organization is located.
                    returned: on success
                    type: string
                    sample: locality_example
                organization:
                    description:
                        - The organization name.
                    returned: on success
                    type: string
                    sample: organization_example
                organizational_unit:
                    description:
                        - The field to differentiate between divisions within an organization.
                    returned: on success
                    type: string
                    sample: organizational_unit_example
                common_name:
                    description:
                        - The fully qualified domain name used for DNS lookups of the server.
                    returned: on success
                    type: string
                    sample: common_name_example
                email_address:
                    description:
                        - The email address of the server's administrator.
                    returned: on success
                    type: string
                    sample: email_address_example
        issuer_name:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                country:
                    description:
                        - ISO 3166-1 alpha-2 code of the country where the organization is located. For a list of codes, see L(ISO's
                          website,https://www.iso.org/obp/ui/#search/code/).
                    returned: on success
                    type: string
                    sample: country_example
                state_province:
                    description:
                        - The province where the organization is located.
                    returned: on success
                    type: string
                    sample: state_province_example
                locality:
                    description:
                        - The city in which the organization is located.
                    returned: on success
                    type: string
                    sample: locality_example
                organization:
                    description:
                        - The organization name.
                    returned: on success
                    type: string
                    sample: organization_example
                organizational_unit:
                    description:
                        - The field to differentiate between divisions within an organization.
                    returned: on success
                    type: string
                    sample: organizational_unit_example
                common_name:
                    description:
                        - The Certificate Authority (CA) name.
                    returned: on success
                    type: string
                    sample: common_name_example
                email_address:
                    description:
                        - The email address of the server's administrator.
                    returned: on success
                    type: string
                    sample: email_address_example
        serial_number:
            description:
                - A unique, positive integer assigned by the Certificate Authority (CA). The issuer name and serial number identify a unique certificate.
            returned: on success
            type: string
            sample: serial_number_example
        version:
            description:
                - The version of the encoded certificate.
            returned: on success
            type: int
            sample: 56
        signature_algorithm:
            description:
                - The identifier for the cryptographic algorithm used by the Certificate Authority (CA) to sign this certificate.
            returned: on success
            type: string
            sample: signature_algorithm_example
        time_not_valid_before:
            description:
                - The date and time the certificate will become valid, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        time_not_valid_after:
            description:
                - The date and time the certificate will expire, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        public_key_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                algorithm:
                    description:
                        - The algorithm identifier and parameters for the public key.
                    returned: on success
                    type: string
                    sample: algorithm_example
                exponent:
                    description:
                        - The private key exponent.
                    returned: on success
                    type: int
                    sample: 56
                key_size:
                    description:
                        - The number of bits in a key used by a cryptographic algorithm.
                    returned: on success
                    type: int
                    sample: 56
        extensions:
            description:
                - Additional attributes associated with users or public keys for managing relationships between Certificate Authorities.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The certificate extension name.
                    returned: on success
                    type: string
                    sample: name_example
                is_critical:
                    description:
                        - The critical flag of the extension. Critical extensions must be processed, non-critical extensions can be ignored.
                    returned: on success
                    type: bool
                    sample: true
                value:
                    description:
                        - The certificate extension value.
                    returned: on success
                    type: string
                    sample: value_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - The current lifecycle state of the SSL certificate.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the certificate was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        is_trust_verification_disabled:
            description:
                - This indicates whether trust verification was disabled during the creation of SSL certificate.
                  If `true` SSL certificate trust verification was disabled and this SSL certificate is most likely self-signed.
            returned: on success
            type: bool
            sample: true
        certificate_data:
            description:
                - The data of the SSL certificate.
            returned: on success
            type: string
            sample: certificate_data_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "issued_by": "issued_by_example",
        "subject_name": {
            "country": "country_example",
            "state_province": "state_province_example",
            "locality": "locality_example",
            "organization": "organization_example",
            "organizational_unit": "organizational_unit_example",
            "common_name": "common_name_example",
            "email_address": "email_address_example"
        },
        "issuer_name": {
            "country": "country_example",
            "state_province": "state_province_example",
            "locality": "locality_example",
            "organization": "organization_example",
            "organizational_unit": "organizational_unit_example",
            "common_name": "common_name_example",
            "email_address": "email_address_example"
        },
        "serial_number": "serial_number_example",
        "version": 56,
        "signature_algorithm": "signature_algorithm_example",
        "time_not_valid_before": "2018-11-16T21:10:29Z",
        "time_not_valid_after": "2018-11-16T21:10:29Z",
        "public_key_info": {
            "algorithm": "algorithm_example",
            "exponent": 56,
            "key_size": 56
        },
        "extensions": [{
            "name": "name_example",
            "is_critical": true,
            "value": "value_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_state": "CREATING",
        "time_created": "2018-11-16T21:10:29Z",
        "is_trust_verification_disabled": true,
        "certificate_data": "certificate_data_example"
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
    from oci.waas import WaasClient
    from oci.waas.models import ChangeCertificateCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasCertificateActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "certificate_id"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_id")

    def get_get_fn(self):
        return self.client.get_certificate

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            certificate_id=self.module.params.get("certificate_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCertificateCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_certificate_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_id=self.module.params.get("certificate_id"),
                change_certificate_compartment_details=action_details,
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


WaasCertificateActionsHelperCustom = get_custom_class(
    "WaasCertificateActionsHelperCustom"
)


class ResourceHelper(
    WaasCertificateActionsHelperCustom, WaasCertificateActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            certificate_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="waas_certificate",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
