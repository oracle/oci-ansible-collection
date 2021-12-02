#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_certificates_certificate_authority_bundle_facts
short_description: Fetches details about a CertificateAuthorityBundle resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CertificateAuthorityBundle resource in Oracle Cloud Infrastructure
    - Gets a certificate authority bundle that matches either the specified `stage`, `name`, or `versionNumber` parameter.
      If none of these parameters are provided, the bundle for the certificate authority version marked as `CURRENT` will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA).
        type: str
        aliases: ["id"]
        required: true
    version_number:
        description:
            - The version number of the certificate authority (CA).
        type: int
    certificate_authority_version_name:
        description:
            - The name of the certificate authority (CA). (This might be referred to as the name of the CA version, as every CA consists of at least one
              version.) Names are unique across versions of a given CA.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific certificate_authority_bundle
  oci_certificates_certificate_authority_bundle_facts:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    version_number: 789
    certificate_authority_version_name: certificate_authority_version_name_example
    stage: CURRENT

"""

RETURN = """
certificate_authority_bundle:
    description:
        - CertificateAuthorityBundle resource
    returned: on success
    type: complex
    contains:
        certificate_authority_id:
            description:
                - The OCID of the certificate authority (CA).
            returned: on success
            type: str
            sample: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_authority_name:
            description:
                - The name of the CA.
            returned: on success
            type: str
            sample: certificate_authority_name_example
        serial_number:
            description:
                - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                  Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
            returned: on success
            type: str
            sample: 03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF
        certificate_pem:
            description:
                - The certificate (in PEM format) for this CA version.
            returned: on success
            type: str
            sample: certificate_pem_example
        cert_chain_pem:
            description:
                - The certificate chain (in PEM format) for this CA version.
            returned: on success
            type: str
            sample: cert_chain_pem_example
        version_name:
            description:
                - The name of the CA.
            returned: on success
            type: str
            sample: version_name_example
        time_created:
            description:
                - "A property indicating when the CA was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        version_number:
            description:
                - The version number of the CA.
            returned: on success
            type: int
            sample: 56
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
                    sample: "2019-04-03T21:10:29.600Z"
                time_of_validity_not_after:
                    description:
                        - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                          format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2019-04-03T21:10:29.600Z"
        stages:
            description:
                - A list of rotation states for this CA.
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
    sample: {
        "certificate_authority_id": "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_authority_name": "certificate_authority_name_example",
        "serial_number": "03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF",
        "certificate_pem": "certificate_pem_example",
        "cert_chain_pem": "cert_chain_pem_example",
        "version_name": "version_name_example",
        "time_created": "2019-04-03T21:10:29.600Z",
        "version_number": 56,
        "validity": {
            "time_of_validity_not_before": "2019-04-03T21:10:29.600Z",
            "time_of_validity_not_after": "2019-04-03T21:10:29.600Z"
        },
        "stages": [],
        "revocation_status": {
            "time_revoked": "2013-10-20T19:20:30+01:00",
            "revocation_reason": "UNSPECIFIED"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.certificates import CertificatesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityBundleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "certificate_authority_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "version_number",
            "certificate_authority_version_name",
            "stage",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority_bundle,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
            **optional_kwargs
        )


CertificateAuthorityBundleFactsHelperCustom = get_custom_class(
    "CertificateAuthorityBundleFactsHelperCustom"
)


class ResourceFactsHelper(
    CertificateAuthorityBundleFactsHelperCustom,
    CertificateAuthorityBundleFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_authority_id=dict(aliases=["id"], type="str", required=True),
            version_number=dict(type="int"),
            certificate_authority_version_name=dict(type="str"),
            stage=dict(
                type="str",
                choices=["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate_authority_bundle",
        service_client_class=CertificatesClient,
        namespace="certificates",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(certificate_authority_bundle=result)


if __name__ == "__main__":
    main()
