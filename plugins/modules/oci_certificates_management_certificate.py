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
module: oci_certificates_management_certificate
short_description: Manage a Certificate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Certificate resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new certificate according to the details of the request.
    - "This resource has the following action operations in the M(oracle.oci.oci_certificates_management_certificate_actions) module:
      cancel_certificate_deletion, change_compartment, schedule_certificate_deletion."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are
              uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment where you want to create the certificate.
            - Required for create using I(state=present).
        type: str
    certificate_id:
        description:
            - The OCID of the certificate.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    description:
        description:
            - A brief description of the certificate. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    current_version_number:
        description:
            - Makes this version the current version. This property cannot be updated in combination with any other properties.
            - This parameter is updatable.
        type: int
    certificate_config:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            certificate_profile_type:
                description:
                    - The name of the profile used to create the certificate, which depends on the type of certificate you need.
                    - Required when config_type is 'ISSUED_BY_INTERNAL_CA'
                type: str
                choices:
                    - "TLS_SERVER_OR_CLIENT"
                    - "TLS_SERVER"
                    - "TLS_CLIENT"
                    - "TLS_CODE_SIGN"
            issuer_certificate_authority_id:
                description:
                    - The OCID of the private CA.
                    - Required when config_type is one of ['ISSUED_BY_INTERNAL_CA', 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA']
                type: str
            subject:
                description:
                    - ""
                    - Required when config_type is 'ISSUED_BY_INTERNAL_CA'
                type: dict
                suboptions:
                    common_name:
                        description:
                            - Common name or fully-qualified domain name (RDN CN).
                            - Required when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                        required: true
                    country:
                        description:
                            - Country name (RDN C).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    domain_component:
                        description:
                            - Domain component (RDN DC).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    distinguished_name_qualifier:
                        description:
                            - Distinguished name qualifier(RDN DNQ).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    generation_qualifier:
                        description:
                            - Personal generational qualifier (for example, Sr., Jr. 3rd, or IV).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    given_name:
                        description:
                            - Personal given name (RDN G or GN).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    initials:
                        description:
                            - Personal initials.
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    locality_name:
                        description:
                            - Locality (RDN L).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    organization:
                        description:
                            - Organization (RDN O).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    organizational_unit:
                        description:
                            - Organizational unit (RDN OU).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    pseudonym:
                        description:
                            - Subject pseudonym.
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    serial_number:
                        description:
                            - Unique subject identifier, which is not the same as the certificate serial number (RDN SERIALNUMBER).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    state_or_province_name:
                        description:
                            - State or province name (RDN ST or S).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    street:
                        description:
                            - Street address (RDN STREET).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    surname:
                        description:
                            - Personal surname (RDN SN).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    title:
                        description:
                            - Title (RDN T or TITLE).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                    user_id:
                        description:
                            - User ID (RDN UID).
                            - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
            subject_alternative_names:
                description:
                    - A list of subject alternative names.
                    - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - The subject alternative name type. Currently only DNS domain or host names and IP addresses are supported.
                            - Required when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                        choices:
                            - "DNS"
                            - "IP"
                        required: true
                    value:
                        description:
                            - The subject alternative name.
                            - Required when config_type is 'ISSUED_BY_INTERNAL_CA'
                        type: str
                        required: true
            key_algorithm:
                description:
                    - The algorithm to use to create key pairs.
                    - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                type: str
                choices:
                    - "RSA2048"
                    - "RSA4096"
                    - "ECDSA_P256"
                    - "ECDSA_P384"
            signature_algorithm:
                description:
                    - The algorithm to use to sign the public key certificate.
                    - Applicable when config_type is 'ISSUED_BY_INTERNAL_CA'
                type: str
                choices:
                    - "SHA256_WITH_RSA"
                    - "SHA384_WITH_RSA"
                    - "SHA512_WITH_RSA"
                    - "SHA256_WITH_ECDSA"
                    - "SHA384_WITH_ECDSA"
                    - "SHA512_WITH_ECDSA"
            cert_chain_pem:
                description:
                    - The certificate chain (in PEM format) for the imported certificate.
                    - This parameter is updatable.
                    - Required when config_type is 'IMPORTED'
                type: str
            private_key_pem:
                description:
                    - The private key (in PEM format) for the imported certificate.
                    - This parameter is updatable.
                    - Required when config_type is 'IMPORTED'
                type: str
            certificate_pem:
                description:
                    - The certificate (in PEM format) for the imported certificate.
                    - This parameter is updatable.
                    - Required when config_type is 'IMPORTED'
                type: str
            private_key_pem_passphrase:
                description:
                    - An optional passphrase for the private key.
                    - This parameter is updatable.
                    - Applicable when config_type is 'IMPORTED'
                type: str
            config_type:
                description:
                    - The origin of the certificate.
                    - This parameter is updatable.
                type: str
                choices:
                    - "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA"
                    - "ISSUED_BY_INTERNAL_CA"
                    - "IMPORTED"
                required: true
            version_name:
                description:
                    - A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.
                    - This parameter is updatable.
                type: str
            stage:
                description:
                    - The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version
                      that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example,
                      you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.
                    - This parameter is updatable.
                type: str
                choices:
                    - "CURRENT"
                    - "PENDING"
            csr_pem:
                description:
                    - The certificate signing request (in PEM format).
                    - This parameter is updatable.
                    - Required when config_type is 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA'
                type: str
            validity:
                description:
                    - ""
                    - Applicable when config_type is one of ['ISSUED_BY_INTERNAL_CA', 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA']
                type: dict
                suboptions:
                    time_of_validity_not_before:
                        description:
                            - "The date on which the certificate validity period begins, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                              format.
                              Example: `2019-04-03T21:10:29.600Z`"
                            - Applicable when config_type is 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA'
                        type: str
                    time_of_validity_not_after:
                        description:
                            - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                              format.
                              Example: `2019-04-03T21:10:29.600Z`"
                            - Required when config_type is 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA'
                        type: str
                        required: true
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    certificate_rules:
        description:
            - An optional list of rules that control how the certificate is used and managed.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            rule_type:
                description:
                    - The type of rule.
                type: str
                choices:
                    - "CERTIFICATE_RENEWAL_RULE"
                required: true
            renewal_interval:
                description:
                    - A property specifying how often, in days, a certificate should be renewed.
                      Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                type: str
                required: true
            advance_renewal_period:
                description:
                    - A property specifying the period of time, in days, before the certificate's targeted renewal that the process should occur.
                      Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                type: str
                required: true
    state:
        description:
            - The state of the Certificate.
            - Use I(state=present) to create or update a Certificate.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create certificate
  oci_certificates_management_certificate:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_config:
      # required
      issuer_certificate_authority_id: "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
      config_type: MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA
      csr_pem: csr_pem_example

      # optional
      version_name: version_name_example
      stage: CURRENT
      validity:
        # required
        time_of_validity_not_after: time_of_validity_not_after_example

        # optional
        time_of_validity_not_before: time_of_validity_not_before_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    certificate_rules:
    - # required
      rule_type: CERTIFICATE_RENEWAL_RULE
      renewal_interval: renewal_interval_example
      advance_renewal_period: advance_renewal_period_example

- name: Update certificate
  oci_certificates_management_certificate:
    # required
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    current_version_number: 56
    certificate_config:
      # required
      issuer_certificate_authority_id: "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
      config_type: MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA
      csr_pem: csr_pem_example

      # optional
      version_name: version_name_example
      stage: CURRENT
      validity:
        # required
        time_of_validity_not_after: time_of_validity_not_after_example

        # optional
        time_of_validity_not_before: time_of_validity_not_before_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    certificate_rules:
    - # required
      rule_type: CERTIFICATE_RENEWAL_RULE
      renewal_interval: renewal_interval_example
      advance_renewal_period: advance_renewal_period_example

- name: Update certificate using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_certificates_management_certificate:
    # required
    name: name_example

    # optional
    description: description_example
    current_version_number: 56
    certificate_config:
      # required
      issuer_certificate_authority_id: "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
      config_type: MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA
      csr_pem: csr_pem_example

      # optional
      version_name: version_name_example
      stage: CURRENT
      validity:
        # required
        time_of_validity_not_after: time_of_validity_not_after_example

        # optional
        time_of_validity_not_before: time_of_validity_not_before_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    certificate_rules:
    - # required
      rule_type: CERTIFICATE_RENEWAL_RULE
      renewal_interval: renewal_interval_example
      advance_renewal_period: advance_renewal_period_example

"""

RETURN = """
certificate:
    description:
        - Details of the Certificate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the certificate.
            returned: on success
            type: str
            sample: lifecycle_details_example
        compartment_id:
            description:
                - The OCID of the compartment where you want to create the certificate.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        current_version:
            description:
                - ""
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
        certificate_revocation_list_details:
            description:
                - ""
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "issuer_certificate_authority_id": "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "certificate_rules": [{
            "rule_type": "CERTIFICATE_RENEWAL_RULE",
            "renewal_interval": "renewal_interval_example",
            "advance_renewal_period": "advance_renewal_period_example"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
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
        "certificate_revocation_list_details": {
            "object_storage_config": {
                "object_storage_namespace": "object_storage_namespace_example",
                "object_storage_bucket_name": "object_storage_bucket_name_example",
                "object_storage_object_name_format": "object_storage_object_name_format_example"
            },
            "custom_formatted_urls": []
        },
        "config_type": "ISSUED_BY_INTERNAL_CA",
        "key_algorithm": "RSA2048",
        "signature_algorithm": "SHA256_WITH_RSA",
        "certificate_profile_type": "TLS_SERVER_OR_CLIENT",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.certificates_management import CertificatesManagementClient
    from oci.certificates_management.models import CreateCertificateDetails
    from oci.certificates_management.models import UpdateCertificateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(CertificateHelperGen, self).get_possible_entity_types() + [
            "certificate",
            "certificates",
            "certificatesManagementcertificate",
            "certificatesManagementcertificates",
            "certificateresource",
            "certificatesresource",
            "certificatesmanagement",
        ]

    def get_module_resource_id_param(self):
        return "certificate_id"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_id")

    def get_get_fn(self):
        return self.client.get_certificate

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate, certificate_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            certificate_id=self.module.params.get("certificate_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "name", "certificate_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_certificates, **kwargs
        )

    def get_create_model_class(self):
        return CreateCertificateDetails

    def get_exclude_attributes(self):
        return ["certificate_config"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(create_certificate_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCertificateDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_id=self.module.params.get("certificate_id"),
                update_certificate_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


CertificateHelperCustom = get_custom_class("CertificateHelperCustom")


class ResourceHelper(CertificateHelperCustom, CertificateHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            certificate_id=dict(aliases=["id"], type="str"),
            description=dict(type="str"),
            current_version_number=dict(type="int"),
            certificate_config=dict(
                type="dict",
                options=dict(
                    certificate_profile_type=dict(
                        type="str",
                        choices=[
                            "TLS_SERVER_OR_CLIENT",
                            "TLS_SERVER",
                            "TLS_CLIENT",
                            "TLS_CODE_SIGN",
                        ],
                    ),
                    issuer_certificate_authority_id=dict(type="str"),
                    subject=dict(
                        type="dict",
                        options=dict(
                            common_name=dict(type="str", required=True),
                            country=dict(type="str"),
                            domain_component=dict(type="str"),
                            distinguished_name_qualifier=dict(type="str"),
                            generation_qualifier=dict(type="str"),
                            given_name=dict(type="str"),
                            initials=dict(type="str"),
                            locality_name=dict(type="str"),
                            organization=dict(type="str"),
                            organizational_unit=dict(type="str"),
                            pseudonym=dict(type="str"),
                            serial_number=dict(type="str"),
                            state_or_province_name=dict(type="str"),
                            street=dict(type="str"),
                            surname=dict(type="str"),
                            title=dict(type="str"),
                            user_id=dict(type="str"),
                        ),
                    ),
                    subject_alternative_names=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(type="str", required=True, choices=["DNS", "IP"]),
                            value=dict(type="str", required=True),
                        ),
                    ),
                    key_algorithm=dict(
                        type="str",
                        choices=["RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"],
                    ),
                    signature_algorithm=dict(
                        type="str",
                        choices=[
                            "SHA256_WITH_RSA",
                            "SHA384_WITH_RSA",
                            "SHA512_WITH_RSA",
                            "SHA256_WITH_ECDSA",
                            "SHA384_WITH_ECDSA",
                            "SHA512_WITH_ECDSA",
                        ],
                    ),
                    cert_chain_pem=dict(type="str"),
                    private_key_pem=dict(type="str", no_log=True),
                    certificate_pem=dict(type="str"),
                    private_key_pem_passphrase=dict(type="str", no_log=True),
                    config_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA",
                            "ISSUED_BY_INTERNAL_CA",
                            "IMPORTED",
                        ],
                    ),
                    version_name=dict(type="str"),
                    stage=dict(type="str", choices=["CURRENT", "PENDING"]),
                    csr_pem=dict(type="str"),
                    validity=dict(
                        type="dict",
                        options=dict(
                            time_of_validity_not_before=dict(type="str"),
                            time_of_validity_not_after=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            certificate_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    rule_type=dict(
                        type="str", required=True, choices=["CERTIFICATE_RENEWAL_RULE"]
                    ),
                    renewal_interval=dict(type="str", required=True),
                    advance_renewal_period=dict(type="str", required=True),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="certificate",
        service_client_class=CertificatesManagementClient,
        namespace="certificates_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
