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
module: oci_waas_certificate_facts
short_description: Fetches details about one or multiple WaasCertificate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WaasCertificate resources in Oracle Cloud Infrastructure
    - Gets a list of SSL certificates that can be used in a WAAS policy.
    - If I(certificate_id) is specified, the details of a single WaasCertificate will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    certificate_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SSL certificate used in the WAAS policy. This number is
              generated when the certificate is added to the policy.
            - Required to get a specific waas_certificate.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the
              compartment is created.
            - Required to list multiple waas_certificates.
        type: str
    sort_by:
        description:
            - The value by which certificate summaries are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.
        type: str
        choices:
            - "id"
            - "compartmentId"
            - "displayName"
            - "notValidAfter"
            - "timeCreated"
    sort_order:
        description:
            - The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - Filter certificates using a list of display names.
        type: list
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter certificates using a list of lifecycle states.
        type: list
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
    time_created_greater_than_or_equal_to:
        description:
            - A filter that matches certificates created on or after the specified date-time.
        type: str
    time_created_less_than:
        description:
            - A filter that matches certificates created before the specified date-time.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List waas_certificates
  oci_waas_certificate_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific waas_certificate
  oci_waas_certificate_facts:
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
waas_certificates:
    description:
        - List of WaasCertificate resources
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
    sample: [{
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
        "time_created": "2018-11-16T21:10:29Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasCertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "certificate_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            certificate_id=self.module.params.get("certificate_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificates,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


WaasCertificateFactsHelperCustom = get_custom_class("WaasCertificateFactsHelperCustom")


class ResourceFactsHelper(
    WaasCertificateFactsHelperCustom, WaasCertificateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=[
                    "id",
                    "compartmentId",
                    "displayName",
                    "notValidAfter",
                    "timeCreated",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="list"),
            lifecycle_state=dict(
                type="list",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                ],
            ),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waas_certificate",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waas_certificates=result)


if __name__ == "__main__":
    main()
