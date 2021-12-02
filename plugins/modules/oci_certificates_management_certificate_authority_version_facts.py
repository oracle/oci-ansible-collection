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
module: oci_certificates_management_certificate_authority_version_facts
short_description: Fetches details about one or multiple CertificateAuthorityVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CertificateAuthorityVersion resources in Oracle Cloud Infrastructure
    - Lists all versions for the specified certificate authority (CA).
      Optionally, you can use the parameter `FilterByVersionNumberQueryParam` to limit the results to a single item that matches the specified version number.
    - If I(certificate_authority_version_number) is specified, the details of a single CertificateAuthorityVersion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA).
        type: str
        required: true
    certificate_authority_version_number:
        description:
            - The version number of the certificate authority (CA).
            - Required to get a specific certificate_authority_version.
        type: int
    version_number:
        description:
            - A filter that returns only resources that match the specified version number. The default value is 0, which means that this filter is not applied.
        type: int
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default order for 'VERSION_NUMBER' is ascending.
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
- name: Get a specific certificate_authority_version
  oci_certificates_management_certificate_authority_version_facts:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_authority_version_number: 789

- name: List certificate_authority_versions
  oci_certificates_management_certificate_authority_version_facts:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    version_number: 789
    sort_by: VERSION_NUMBER
    sort_order: ASC

"""

RETURN = """
certificate_authority_versions:
    description:
        - List of CertificateAuthorityVersion resources
    returned: on success
    type: complex
    contains:
        certificate_authority_id:
            description:
                - The OCID of the CA.
            returned: on success
            type: str
            sample: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        serial_number:
            description:
                - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                  Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
            returned: on success
            type: str
            sample: 03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF
        time_created:
            description:
                - "A optional property indicating when the CA version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        version_number:
            description:
                - The version number of this CA.
            returned: on success
            type: int
            sample: 56
        issuer_ca_version_number:
            description:
                - The version number of the issuing CA.
            returned: on success
            type: int
            sample: 56
        version_name:
            description:
                - The name of the CA version. When the value is not null, a name is unique across versions for a given CA.
            returned: on success
            type: str
            sample: version_name_example
        subject_alternative_names:
            description:
                - A list of subject alternative names. A subject alternative name specifies the domain names, including subdomains, and IP addresses covered by
                  the certificates issued by this CA.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The subject alternative name type. Currently only DNS domain or host names and IP addresses are supported.
                    returned: on success
                    type: str
                    sample: DNS
                value:
                    description:
                        - The subject alternative name.
                    returned: on success
                    type: str
                    sample: value_example
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the CA version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
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
                time_of_revocation:
                    description:
                        - "The time when the entity was revoked, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2019-04-03T21:10:29.600Z"
                revocation_reason:
                    description:
                        - The reason the certificate or certificate authority (CA) was revoked.
                    returned: on success
                    type: str
                    sample: UNSPECIFIED
    sample: [{
        "certificate_authority_id": "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "serial_number": "03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF",
        "time_created": "2019-04-03T21:10:29.600Z",
        "version_number": 56,
        "issuer_ca_version_number": 56,
        "version_name": "version_name_example",
        "subject_alternative_names": [{
            "type": "DNS",
            "value": "value_example"
        }],
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "validity": {
            "time_of_validity_not_before": "2019-04-03T21:10:29.600Z",
            "time_of_validity_not_after": "2019-04-03T21:10:29.600Z"
        },
        "stages": [],
        "revocation_status": {
            "time_of_revocation": "2019-04-03T21:10:29.600Z",
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
    from oci.certificates_management import CertificatesManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "certificate_authority_id",
            "certificate_authority_version_number",
        ]

    def get_required_params_for_list(self):
        return [
            "certificate_authority_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority_version,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
            certificate_authority_version_number=self.module.params.get(
                "certificate_authority_version_number"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "version_number",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificate_authority_versions,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
            **optional_kwargs
        )


CertificateAuthorityVersionFactsHelperCustom = get_custom_class(
    "CertificateAuthorityVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    CertificateAuthorityVersionFactsHelperCustom,
    CertificateAuthorityVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_authority_id=dict(type="str", required=True),
            certificate_authority_version_number=dict(type="int"),
            version_number=dict(type="int"),
            sort_by=dict(type="str", choices=["VERSION_NUMBER"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate_authority_version",
        service_client_class=CertificatesManagementClient,
        namespace="certificates_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(certificate_authority_versions=result)


if __name__ == "__main__":
    main()
