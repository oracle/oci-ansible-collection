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
module: oci_certificates_certificate_bundle_facts
short_description: Fetches details about a CertificateBundle resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CertificateBundle resource in Oracle Cloud Infrastructure
    - Gets a certificate bundle that matches either the specified `stage`, `versionName`, or `versionNumber` parameter.
      If none of these parameters are provided, the bundle for the certificate version marked as `CURRENT` will be returned.
    - By default, the private key is not included in the query result, and a CertificateBundlePublicOnly is returned.
      If the private key is needed, use the CertificateBundleTypeQueryParam parameter to get a CertificateBundleWithPrivateKey response.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_id:
        description:
            - The OCID of the certificate.
        type: str
        aliases: ["id"]
        required: true
    version_number:
        description:
            - The version number of the certificate. The default value is 0, which means that this query parameter is ignored.
        type: int
    certificate_version_name:
        description:
            - The name of the certificate. (This might be referred to as the name of the certificate version, as every certificate consists of at least one
              version.) Names are unique across versions of a given certificate.
        type: str
    stage:
        description:
            - The rotation state of the certificate version.
        type: str
        choices:
            - "CURRENT"
            - "PENDING"
            - "LATEST"
            - "PREVIOUS"
            - "DEPRECATED"
    certificate_bundle_type:
        description:
            - The type of certificate bundle. By default, the private key fields are not returned. When querying for certificate bundles, to return results with
              certificate contents, the private key in PEM format, and the private key passphrase, specify the value of this parameter as
              `CERTIFICATE_CONTENT_WITH_PRIVATE_KEY`.
        type: str
        choices:
            - "CERTIFICATE_CONTENT_PUBLIC_ONLY"
            - "CERTIFICATE_CONTENT_WITH_PRIVATE_KEY"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific certificate_bundle
  oci_certificates_certificate_bundle_facts:
    # required
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    version_number: 56
    certificate_version_name: certificate_version_name_example
    stage: CURRENT
    certificate_bundle_type: CERTIFICATE_CONTENT_PUBLIC_ONLY

"""

RETURN = """
certificate_bundle:
    description:
        - CertificateBundle resource
    returned: on success
    type: complex
    contains:
        certificate_bundle_type:
            description:
                - The type of certificate bundle, which indicates whether the private key fields are included.
            returned: on success
            type: str
            sample: CERTIFICATE_CONTENT_PUBLIC_ONLY
        certificate_id:
            description:
                - The OCID of the certificate.
            returned: on success
            type: str
            sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_name:
            description:
                - The name of the certificate.
            returned: on success
            type: str
            sample: certificate_name_example
        version_number:
            description:
                - The version number of the certificate.
            returned: on success
            type: int
            sample: 56
        serial_number:
            description:
                - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                  Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
            returned: on success
            type: str
            sample: serial_number_example
        certificate_pem:
            description:
                - The certificate in PEM format.
            returned: on success
            type: str
            sample: certificate_pem_example
        cert_chain_pem:
            description:
                - The certificate chain (in PEM format) for the certificate bundle.
            returned: on success
            type: str
            sample: cert_chain_pem_example
        time_created:
            description:
                - "An optional property indicating when the certificate version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        validity:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_of_validity_not_before:
                    description:
                        - "The date on which the certificate validity period begins, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                          format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_of_validity_not_after:
                    description:
                        - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                          format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        version_name:
            description:
                - The name of the certificate version.
            returned: on success
            type: str
            sample: version_name_example
        stages:
            description:
                - A list of rotation states for the certificate bundle.
            returned: on success
            type: list
            sample: []
        revocation_status:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_revoked:
                    description:
                        - The time when the certificate or CA was revoked.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                revocation_reason:
                    description:
                        - The reason that the certificate or CA was revoked.
                    returned: on success
                    type: str
                    sample: UNSPECIFIED
        private_key_pem:
            description:
                - The private key (in PEM format) for the certificate.
            returned: on success
            type: str
            sample: private_key_pem_example
        private_key_pem_passphrase:
            description:
                - An optional passphrase for the private key.
            returned: on success
            type: str
            sample: private_key_pem_passphrase_example
    sample: {
        "certificate_bundle_type": "CERTIFICATE_CONTENT_PUBLIC_ONLY",
        "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_name": "certificate_name_example",
        "version_number": 56,
        "serial_number": "serial_number_example",
        "certificate_pem": "certificate_pem_example",
        "cert_chain_pem": "cert_chain_pem_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "validity": {
            "time_of_validity_not_before": "2013-10-20T19:20:30+01:00",
            "time_of_validity_not_after": "2013-10-20T19:20:30+01:00"
        },
        "version_name": "version_name_example",
        "stages": [],
        "revocation_status": {
            "time_revoked": "2013-10-20T19:20:30+01:00",
            "revocation_reason": "UNSPECIFIED"
        },
        "private_key_pem": "private_key_pem_example",
        "private_key_pem_passphrase": "private_key_pem_passphrase_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.certificates import CertificatesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateBundleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "certificate_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "version_number",
            "certificate_version_name",
            "stage",
            "certificate_bundle_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_bundle,
            certificate_id=self.module.params.get("certificate_id"),
            **optional_kwargs
        )


CertificateBundleFactsHelperCustom = get_custom_class(
    "CertificateBundleFactsHelperCustom"
)


class ResourceFactsHelper(
    CertificateBundleFactsHelperCustom, CertificateBundleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_id=dict(aliases=["id"], type="str", required=True),
            version_number=dict(type="int"),
            certificate_version_name=dict(type="str"),
            stage=dict(
                type="str",
                choices=["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"],
            ),
            certificate_bundle_type=dict(
                type="str",
                choices=[
                    "CERTIFICATE_CONTENT_PUBLIC_ONLY",
                    "CERTIFICATE_CONTENT_WITH_PRIVATE_KEY",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate_bundle",
        service_client_class=CertificatesClient,
        namespace="certificates",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(certificate_bundle=result)


if __name__ == "__main__":
    main()
