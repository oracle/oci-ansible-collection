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
module: oci_certificates_certificate_authority_bundle_version_facts
short_description: Fetches details about one or multiple CertificateAuthorityBundleVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CertificateAuthorityBundleVersion resources in Oracle Cloud Infrastructure
    - Lists all certificate authority bundle versions for the specified certificate authority.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA).
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default
              order for `VERSION_NUMBER` is ascending.
        type: str
        choices:
            - "VERSION_NUMBER"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List certificate_authority_bundle_versions
  oci_certificates_certificate_authority_bundle_version_facts:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: VERSION_NUMBER
    sort_order: ASC

"""

RETURN = """
certificate_authority_bundle_versions:
    description:
        - List of CertificateAuthorityBundleVersion resources
    returned: on success
    type: complex
    contains:
        certificate_authority_id:
            description:
                - The OCID of the certificate authority (CA).
            returned: on success
            type: str
            sample: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        serial_number:
            description:
                - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                  Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
            returned: on success
            type: str
            sample: serial_number_example
        time_created:
            description:
                - "An optional property indicating when the CA version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version_number:
            description:
                - The version number of the CA.
            returned: on success
            type: int
            sample: 56
        version_name:
            description:
                - The name of the CA version. When this value is not null, the name is unique across CA versions for a given CA.
            returned: on success
            type: str
            sample: version_name_example
        certificate_authority_name:
            description:
                - The name of the CA.
            returned: on success
            type: str
            sample: certificate_authority_name_example
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the CA version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
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
        stages:
            description:
                - A list of rotation states for this CA version.
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
    sample: [{
        "certificate_authority_id": "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "serial_number": "serial_number_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version_number": 56,
        "version_name": "version_name_example",
        "certificate_authority_name": "certificate_authority_name_example",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "validity": {
            "time_of_validity_not_before": "2013-10-20T19:20:30+01:00",
            "time_of_validity_not_after": "2013-10-20T19:20:30+01:00"
        },
        "stages": [],
        "revocation_status": {
            "time_revoked": "2013-10-20T19:20:30+01:00",
            "revocation_reason": "UNSPECIFIED"
        }
    }]
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


class CertificateAuthorityBundleVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "certificate_authority_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificate_authority_bundle_versions,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
            **optional_kwargs
        )


CertificateAuthorityBundleVersionFactsHelperCustom = get_custom_class(
    "CertificateAuthorityBundleVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    CertificateAuthorityBundleVersionFactsHelperCustom,
    CertificateAuthorityBundleVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_authority_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["VERSION_NUMBER"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate_authority_bundle_version",
        service_client_class=CertificatesClient,
        namespace="certificates",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(certificate_authority_bundle_versions=result)


if __name__ == "__main__":
    main()
