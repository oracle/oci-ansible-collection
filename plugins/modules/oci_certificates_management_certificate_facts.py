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
module: oci_certificates_management_certificate_facts
short_description: Fetches details about one or multiple Certificate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Certificate resources in Oracle Cloud Infrastructure
    - Lists all certificates that match the query parameters.
      Optionally, you can use the parameter `FilterByCertificateIdQueryParam` to limit the result set to a single item that matches the specified certificate.
    - If I(certificate_id) is specified, the details of a single Certificate will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter that returns only resources that match the given compartment OCID.
        type: str
    lifecycle_state:
        description:
            - A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "SCHEDULING_DELETION"
            - "PENDING_DELETION"
            - "CANCELLING_DELETION"
            - "FAILED"
    name:
        description:
            - A filter that returns only resources that match the specified name.
        type: str
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default
              order for `EXPIRATIONDATE` and 'TIMECREATED' is descending. The default order for `NAME`
              is ascending.
        type: str
        choices:
            - "NAME"
            - "EXPIRATIONDATE"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    issuer_certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.
        type: str
    certificate_id:
        description:
            - The OCID of the certificate.
            - Required to get a specific certificate.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific certificate
  oci_certificates_management_certificate_facts:
    # required
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"

- name: List certificates
  oci_certificates_management_certificate_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    name: name_example
    sort_by: NAME
    sort_order: ASC
    issuer_certificate_authority_id: "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
certificates:
    description:
        - List of Certificate resources
    returned: on success
    type: complex
    contains:
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the certificate.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        current_version:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                certificate_id:
                    description:
                        - The OCID of the certificate.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                serial_number:
                    description:
                        - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                          Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
                    returned: on success
                    type: str
                    sample: serial_number_example
                time_created:
                    description:
                        - "A optional property indicating the time when the certificate version was created, expressed in L(RFC
                          3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                version_number:
                    description:
                        - The version number of the certificate.
                    returned: on success
                    type: int
                    sample: 56
                issuer_ca_version_number:
                    description:
                        - The version number of the issuing certificate authority (CA).
                    returned: on success
                    type: int
                    sample: 56
                version_name:
                    description:
                        - The name of the certificate version. When the value is not null, a name is unique across versions of a given certificate.
                    returned: on success
                    type: str
                    sample: version_name_example
                subject_alternative_names:
                    description:
                        - A list of subject alternative names.
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
                        - "An optional property indicating when to delete the certificate version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
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
                                - "The date on which the certificate validity period begins, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                                  timestamp format.
                                  Example: `2019-04-03T21:10:29.600Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_of_validity_not_after:
                            description:
                                - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                                  timestamp format.
                                  Example: `2019-04-03T21:10:29.600Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                stages:
                    description:
                        - A list of rotation states for this certificate version.
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
                            sample: "2013-10-20T19:20:30+01:00"
                        revocation_reason:
                            description:
                                - The reason the certificate or certificate authority (CA) was revoked.
                            returned: on success
                            type: str
                            sample: UNSPECIFIED
        certificate_revocation_list_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                object_storage_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        object_storage_namespace:
                            description:
                                - The tenancy of the bucket where the CRL is stored.
                            returned: on success
                            type: str
                            sample: object_storage_namespace_example
                        object_storage_bucket_name:
                            description:
                                - The name of the bucket where the CRL is stored.
                            returned: on success
                            type: str
                            sample: object_storage_bucket_name_example
                        object_storage_object_name_format:
                            description:
                                - The object name in the bucket where the CRL is stored, expressed using a format where the version number of the issuing CA is
                                  inserted as part of the Object Storage object name wherever you include a pair of curly braces. This versioning scheme helps
                                  avoid collisions when new CA versions are created. For example, myCrlFileIssuedFromCAVersion{}.crl becomes
                                  myCrlFileIssuedFromCAVersion2.crl for CA version 2.
                            returned: on success
                            type: str
                            sample: object_storage_object_name_format_example
                custom_formatted_urls:
                    description:
                        - Optional CRL access points, expressed using a format where the version number of the issuing CA is inserted wherever you include a
                          pair of curly braces. This versioning scheme helps avoid collisions when new CA versions are created. For example,
                          myCrlFileIssuedFromCAVersion{}.crl becomes myCrlFileIssuedFromCAVersion2.crl for CA version 2.
                    returned: on success
                    type: list
                    sample: []
        id:
            description:
                - The OCID of the certificate.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        issuer_certificate_authority_id:
            description:
                - The OCID of the certificate authority (CA) that issued the certificate.
            returned: on success
            type: str
            sample: "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are
                  uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - A brief description of the certificate. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "A property indicating when the certificate was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the certificate version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the certificate.
            returned: on success
            type: str
            sample: CREATING
        compartment_id:
            description:
                - The OCID of the compartment where you want to create the certificate.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_rules:
            description:
                - A list of rules that control how the certificate is used and managed.
            returned: on success
            type: complex
            contains:
                rule_type:
                    description:
                        - The type of rule.
                    returned: on success
                    type: str
                    sample: CERTIFICATE_RENEWAL_RULE
                renewal_interval:
                    description:
                        - A property specifying how often, in days, a certificate should be renewed.
                          Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                    returned: on success
                    type: str
                    sample: renewal_interval_example
                advance_renewal_period:
                    description:
                        - A property specifying the period of time, in days, before the certificate's targeted renewal that the process should occur.
                          Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                    returned: on success
                    type: str
                    sample: advance_renewal_period_example
        current_version_summary:
            description:
                - ""
                - Returned for list operation
            returned: on success
            type: complex
            contains:
                certificate_id:
                    description:
                        - The OCID of the certificate.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                serial_number:
                    description:
                        - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                          Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
                    returned: on success
                    type: str
                    sample: serial_number_example
                time_created:
                    description:
                        - "A optional property indicating the time when the certificate version was created, expressed in L(RFC
                          3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                version_number:
                    description:
                        - The version number of the certificate.
                    returned: on success
                    type: int
                    sample: 56
                issuer_ca_version_number:
                    description:
                        - The version number of the issuing certificate authority (CA).
                    returned: on success
                    type: int
                    sample: 56
                version_name:
                    description:
                        - The name of the certificate version. When the value is not null, a name is unique across versions of a given certificate.
                    returned: on success
                    type: str
                    sample: version_name_example
                subject_alternative_names:
                    description:
                        - A list of subject alternative names.
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
                        - "An optional property indicating when to delete the certificate version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
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
                                - "The date on which the certificate validity period begins, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                                  timestamp format.
                                  Example: `2019-04-03T21:10:29.600Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_of_validity_not_after:
                            description:
                                - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                                  timestamp format.
                                  Example: `2019-04-03T21:10:29.600Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                stages:
                    description:
                        - A list of rotation states for this certificate version.
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
                            sample: "2013-10-20T19:20:30+01:00"
                        revocation_reason:
                            description:
                                - The reason the certificate or certificate authority (CA) was revoked.
                            returned: on success
                            type: str
                            sample: UNSPECIFIED
        subject:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                common_name:
                    description:
                        - Common name or fully-qualified domain name (RDN CN).
                    returned: on success
                    type: str
                    sample: common_name_example
                country:
                    description:
                        - Country name (RDN C).
                    returned: on success
                    type: str
                    sample: country_example
                domain_component:
                    description:
                        - Domain component (RDN DC).
                    returned: on success
                    type: str
                    sample: domain_component_example
                distinguished_name_qualifier:
                    description:
                        - Distinguished name qualifier(RDN DNQ).
                    returned: on success
                    type: str
                    sample: distinguished_name_qualifier_example
                generation_qualifier:
                    description:
                        - Personal generational qualifier (for example, Sr., Jr. 3rd, or IV).
                    returned: on success
                    type: str
                    sample: generation_qualifier_example
                given_name:
                    description:
                        - Personal given name (RDN G or GN).
                    returned: on success
                    type: str
                    sample: given_name_example
                initials:
                    description:
                        - Personal initials.
                    returned: on success
                    type: str
                    sample: initials_example
                locality_name:
                    description:
                        - Locality (RDN L).
                    returned: on success
                    type: str
                    sample: locality_name_example
                organization:
                    description:
                        - Organization (RDN O).
                    returned: on success
                    type: str
                    sample: organization_example
                organizational_unit:
                    description:
                        - Organizational unit (RDN OU).
                    returned: on success
                    type: str
                    sample: organizational_unit_example
                pseudonym:
                    description:
                        - Subject pseudonym.
                    returned: on success
                    type: str
                    sample: pseudonym_example
                serial_number:
                    description:
                        - Unique subject identifier, which is not the same as the certificate serial number (RDN SERIALNUMBER).
                    returned: on success
                    type: str
                    sample: serial_number_example
                state_or_province_name:
                    description:
                        - State or province name (RDN ST or S).
                    returned: on success
                    type: str
                    sample: state_or_province_name_example
                street:
                    description:
                        - Street address (RDN STREET).
                    returned: on success
                    type: str
                    sample: street_example
                surname:
                    description:
                        - Personal surname (RDN SN).
                    returned: on success
                    type: str
                    sample: surname_example
                title:
                    description:
                        - Title (RDN T or TITLE).
                    returned: on success
                    type: str
                    sample: title_example
                user_id:
                    description:
                        - User ID (RDN UID).
                    returned: on success
                    type: str
                    sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        config_type:
            description:
                - The origin of the certificate.
            returned: on success
            type: str
            sample: ISSUED_BY_INTERNAL_CA
        key_algorithm:
            description:
                - The algorithm used to create key pairs.
            returned: on success
            type: str
            sample: RSA2048
        signature_algorithm:
            description:
                - The algorithm used to sign the public key certificate.
            returned: on success
            type: str
            sample: SHA256_WITH_RSA
        certificate_profile_type:
            description:
                - The name of the profile used to create the certificate, which depends on the type of certificate you need.
            returned: on success
            type: str
            sample: TLS_SERVER_OR_CLIENT
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "lifecycle_details": "lifecycle_details_example",
        "current_version": {
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
            "serial_number": "serial_number_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "version_number": 56,
            "issuer_ca_version_number": 56,
            "version_name": "version_name_example",
            "subject_alternative_names": [{
                "type": "DNS",
                "value": "value_example"
            }],
            "time_of_deletion": "2013-10-20T19:20:30+01:00",
            "validity": {
                "time_of_validity_not_before": "2013-10-20T19:20:30+01:00",
                "time_of_validity_not_after": "2013-10-20T19:20:30+01:00"
            },
            "stages": [],
            "revocation_status": {
                "time_of_revocation": "2013-10-20T19:20:30+01:00",
                "revocation_reason": "UNSPECIFIED"
            }
        },
        "certificate_revocation_list_details": {
            "object_storage_config": {
                "object_storage_namespace": "object_storage_namespace_example",
                "object_storage_bucket_name": "object_storage_bucket_name_example",
                "object_storage_object_name_format": "object_storage_object_name_format_example"
            },
            "custom_formatted_urls": []
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "issuer_certificate_authority_id": "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_rules": [{
            "rule_type": "CERTIFICATE_RENEWAL_RULE",
            "renewal_interval": "renewal_interval_example",
            "advance_renewal_period": "advance_renewal_period_example"
        }],
        "current_version_summary": {
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
            "serial_number": "serial_number_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "version_number": 56,
            "issuer_ca_version_number": 56,
            "version_name": "version_name_example",
            "subject_alternative_names": [{
                "type": "DNS",
                "value": "value_example"
            }],
            "time_of_deletion": "2013-10-20T19:20:30+01:00",
            "validity": {
                "time_of_validity_not_before": "2013-10-20T19:20:30+01:00",
                "time_of_validity_not_after": "2013-10-20T19:20:30+01:00"
            },
            "stages": [],
            "revocation_status": {
                "time_of_revocation": "2013-10-20T19:20:30+01:00",
                "revocation_reason": "UNSPECIFIED"
            }
        },
        "subject": {
            "common_name": "common_name_example",
            "country": "country_example",
            "domain_component": "domain_component_example",
            "distinguished_name_qualifier": "distinguished_name_qualifier_example",
            "generation_qualifier": "generation_qualifier_example",
            "given_name": "given_name_example",
            "initials": "initials_example",
            "locality_name": "locality_name_example",
            "organization": "organization_example",
            "organizational_unit": "organizational_unit_example",
            "pseudonym": "pseudonym_example",
            "serial_number": "serial_number_example",
            "state_or_province_name": "state_or_province_name_example",
            "street": "street_example",
            "surname": "surname_example",
            "title": "title_example",
            "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "config_type": "ISSUED_BY_INTERNAL_CA",
        "key_algorithm": "RSA2048",
        "signature_algorithm": "SHA256_WITH_RSA",
        "certificate_profile_type": "TLS_SERVER_OR_CLIENT",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.certificates_management import CertificatesManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "certificate_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            certificate_id=self.module.params.get("certificate_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "name",
            "sort_by",
            "sort_order",
            "issuer_certificate_authority_id",
            "certificate_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificates, **optional_kwargs
        )


CertificateFactsHelperCustom = get_custom_class("CertificateFactsHelperCustom")


class ResourceFactsHelper(CertificateFactsHelperCustom, CertificateFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "SCHEDULING_DELETION",
                    "PENDING_DELETION",
                    "CANCELLING_DELETION",
                    "FAILED",
                ],
            ),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME", "EXPIRATIONDATE", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            issuer_certificate_authority_id=dict(type="str"),
            certificate_id=dict(aliases=["id"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate",
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

    module.exit_json(certificates=result)


if __name__ == "__main__":
    main()
