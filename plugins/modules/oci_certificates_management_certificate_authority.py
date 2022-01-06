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
module: oci_certificates_management_certificate_authority
short_description: Manage a CertificateAuthority resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a CertificateAuthority resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new certificate authority (CA) according to the details of the request.
    - "This resource has the following action operations in the M(oracle.oci.oci_certificates_management_certificate_authority_actions) module:
      cancel_certificate_authority_deletion, change_compartment, schedule_certificate_authority_deletion."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include
              uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - A brief description of the CA.
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The compartment in which you want to create the CA.
            - Required for create using I(state=present).
        type: str
    certificate_authority_rules:
        description:
            - A list of rules that control how the CA is used and managed.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            rule_type:
                description:
                    - The type of rule, whether a renewal rule regarding when to renew the CA or an issuance expiry rule that governs how long the certificates
                      and CAs issued by the CA are valid. (For internal use only) An internal issuance rule defines the number and type of certificates that the
                      CA can issue.
                type: str
                choices:
                    - "CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE"
                required: true
            leaf_certificate_max_validity_duration:
                description:
                    - A property indicating the maximum validity duration, in days, of leaf certificates issued by this CA.
                      Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                type: str
            certificate_authority_max_validity_duration:
                description:
                    - A property indicating the maximum validity duration, in days, of subordinate CA's issued by this CA.
                      Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                type: str
    certificate_authority_config:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            config_type:
                description:
                    - The origin of the CA.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ROOT_CA_GENERATED_INTERNALLY"
                    - "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"
                required: true
            version_name:
                description:
                    - The name of the CA version. When the value is not null, a name is unique across versions of a given CA.
                    - This parameter is updatable.
                type: str
            validity:
                description:
                    - ""
                type: dict
                suboptions:
                    time_of_validity_not_before:
                        description:
                            - "The date on which the certificate validity period begins, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                              format.
                              Example: `2019-04-03T21:10:29.600Z`"
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    time_of_validity_not_after:
                        description:
                            - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                              format.
                              Example: `2019-04-03T21:10:29.600Z`"
                            - Required when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                        required: true
            signing_algorithm:
                description:
                    - The algorithm used to sign public key certificates that the CA issues.
                type: str
                choices:
                    - "SHA256_WITH_RSA"
                    - "SHA384_WITH_RSA"
                    - "SHA512_WITH_RSA"
                    - "SHA256_WITH_ECDSA"
                    - "SHA384_WITH_ECDSA"
                    - "SHA512_WITH_ECDSA"
            subject:
                description:
                    - ""
                type: dict
                suboptions:
                    common_name:
                        description:
                            - Common name or fully-qualified domain name (RDN CN).
                            - Required when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                        required: true
                    country:
                        description:
                            - Country name (RDN C).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    domain_component:
                        description:
                            - Domain component (RDN DC).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    distinguished_name_qualifier:
                        description:
                            - Distinguished name qualifier(RDN DNQ).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    generation_qualifier:
                        description:
                            - Personal generational qualifier (for example, Sr., Jr. 3rd, or IV).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    given_name:
                        description:
                            - Personal given name (RDN G or GN).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    initials:
                        description:
                            - Personal initials.
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    locality_name:
                        description:
                            - Locality (RDN L).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    organization:
                        description:
                            - Organization (RDN O).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    organizational_unit:
                        description:
                            - Organizational unit (RDN OU).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    pseudonym:
                        description:
                            - Subject pseudonym.
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    serial_number:
                        description:
                            - Unique subject identifier, which is not the same as the certificate serial number (RDN SERIALNUMBER).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    state_or_province_name:
                        description:
                            - State or province name (RDN ST or S).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    street:
                        description:
                            - Street address (RDN STREET).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    surname:
                        description:
                            - Personal surname (RDN SN).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    title:
                        description:
                            - Title (RDN T or TITLE).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
                    user_id:
                        description:
                            - User ID (RDN UID).
                            - Applicable when config_type is 'ROOT_CA_GENERATED_INTERNALLY'
                        type: str
            issuer_certificate_authority_id:
                description:
                    - The OCID of the private CA.
                    - Required when config_type is 'SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA'
                type: str
            stage:
                description:
                    - The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version
                      that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example,
                      you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.
                    - This parameter is updatable.
                type: str
                choices:
                    - "CURRENT"
                    - "PENDING"
    certificate_revocation_list_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            object_storage_config:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    object_storage_namespace:
                        description:
                            - The tenancy of the bucket where the CRL is stored.
                        type: str
                    object_storage_bucket_name:
                        description:
                            - The name of the bucket where the CRL is stored.
                        type: str
                        required: true
                    object_storage_object_name_format:
                        description:
                            - The object name in the bucket where the CRL is stored, expressed using a format where the version number of the issuing CA is
                              inserted as part of the Object Storage object name wherever you include a pair of curly braces. This versioning scheme helps avoid
                              collisions when new CA versions are created. For example, myCrlFileIssuedFromCAVersion{}.crl becomes
                              myCrlFileIssuedFromCAVersion2.crl for CA version 2.
                        type: str
                        required: true
            custom_formatted_urls:
                description:
                    - Optional CRL access points, expressed using a format where the version number of the issuing CA is inserted wherever you include a pair of
                      curly braces. This versioning scheme helps avoid collisions when new CA versions are created. For example,
                      myCrlFileIssuedFromCAVersion{}.crl becomes myCrlFileIssuedFromCAVersion2.crl for CA version 2.
                type: list
                elements: str
    kms_key_id:
        description:
            - The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    current_version_number:
        description:
            - Makes this version the current version. This property cannot be updated in combination with any other properties.
            - This parameter is updatable.
        type: int
    state:
        description:
            - The state of the CertificateAuthority.
            - Use I(state=present) to create or update a CertificateAuthority.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create certificate_authority
  oci_certificates_management_certificate_authority:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_authority_config:
      # required
      config_type: ROOT_CA_GENERATED_INTERNALLY
      subject:
        # required
        common_name: common_name_example

        # optional
        country: country_example
        domain_component: domain_component_example
        distinguished_name_qualifier: distinguished_name_qualifier_example
        generation_qualifier: generation_qualifier_example
        given_name: given_name_example
        initials: initials_example
        locality_name: locality_name_example
        organization: organization_example
        organizational_unit: organizational_unit_example
        pseudonym: pseudonym_example
        serial_number: serial_number_example
        state_or_province_name: state_or_province_name_example
        street: street_example
        surname: surname_example
        title: title_example
        user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
      version_name: version_name_example
      validity:
        # required
        time_of_validity_not_after: time_of_validity_not_after_example

        # optional
        time_of_validity_not_before: time_of_validity_not_before_example
      signing_algorithm: SHA256_WITH_RSA
      stage: CURRENT
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    certificate_authority_rules:
    - # required
      rule_type: CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE

      # optional
      leaf_certificate_max_validity_duration: leaf_certificate_max_validity_duration_example
      certificate_authority_max_validity_duration: certificate_authority_max_validity_duration_example
    certificate_revocation_list_details:
      # required
      object_storage_config:
        # required
        object_storage_bucket_name: object_storage_bucket_name_example
        object_storage_object_name_format: object_storage_object_name_format_example

        # optional
        object_storage_namespace: object_storage_namespace_example

        # optional
      custom_formatted_urls: [ "custom_formatted_urls_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update certificate_authority
  oci_certificates_management_certificate_authority:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    certificate_authority_rules:
    - # required
      rule_type: CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE

      # optional
      leaf_certificate_max_validity_duration: leaf_certificate_max_validity_duration_example
      certificate_authority_max_validity_duration: certificate_authority_max_validity_duration_example
    certificate_authority_config:
      # required
      config_type: ROOT_CA_GENERATED_INTERNALLY
      subject:
        # required
        common_name: common_name_example

        # optional
        country: country_example
        domain_component: domain_component_example
        distinguished_name_qualifier: distinguished_name_qualifier_example
        generation_qualifier: generation_qualifier_example
        given_name: given_name_example
        initials: initials_example
        locality_name: locality_name_example
        organization: organization_example
        organizational_unit: organizational_unit_example
        pseudonym: pseudonym_example
        serial_number: serial_number_example
        state_or_province_name: state_or_province_name_example
        street: street_example
        surname: surname_example
        title: title_example
        user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
      version_name: version_name_example
      validity:
        # required
        time_of_validity_not_after: time_of_validity_not_after_example

        # optional
        time_of_validity_not_before: time_of_validity_not_before_example
      signing_algorithm: SHA256_WITH_RSA
      stage: CURRENT
    certificate_revocation_list_details:
      # required
      object_storage_config:
        # required
        object_storage_bucket_name: object_storage_bucket_name_example
        object_storage_object_name_format: object_storage_object_name_format_example

        # optional
        object_storage_namespace: object_storage_namespace_example

        # optional
      custom_formatted_urls: [ "custom_formatted_urls_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    current_version_number: 56

- name: Update certificate_authority using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_certificates_management_certificate_authority:
    # required
    name: name_example

    # optional
    description: description_example
    certificate_authority_rules:
    - # required
      rule_type: CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE

      # optional
      leaf_certificate_max_validity_duration: leaf_certificate_max_validity_duration_example
      certificate_authority_max_validity_duration: certificate_authority_max_validity_duration_example
    certificate_authority_config:
      # required
      config_type: ROOT_CA_GENERATED_INTERNALLY
      subject:
        # required
        common_name: common_name_example

        # optional
        country: country_example
        domain_component: domain_component_example
        distinguished_name_qualifier: distinguished_name_qualifier_example
        generation_qualifier: generation_qualifier_example
        given_name: given_name_example
        initials: initials_example
        locality_name: locality_name_example
        organization: organization_example
        organizational_unit: organizational_unit_example
        pseudonym: pseudonym_example
        serial_number: serial_number_example
        state_or_province_name: state_or_province_name_example
        street: street_example
        surname: surname_example
        title: title_example
        user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
      version_name: version_name_example
      validity:
        # required
        time_of_validity_not_after: time_of_validity_not_after_example

        # optional
        time_of_validity_not_before: time_of_validity_not_before_example
      signing_algorithm: SHA256_WITH_RSA
      stage: CURRENT
    certificate_revocation_list_details:
      # required
      object_storage_config:
        # required
        object_storage_bucket_name: object_storage_bucket_name_example
        object_storage_object_name_format: object_storage_object_name_format_example

        # optional
        object_storage_namespace: object_storage_namespace_example

        # optional
      custom_formatted_urls: [ "custom_formatted_urls_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    current_version_number: 56

"""

RETURN = """
certificate_authority:
    description:
        - Details of the CertificateAuthority resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the CA.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        issuer_certificate_authority_id:
            description:
                - The OCID of the parent CA that issued this CA. If this is the root CA, then this value is null.
            returned: on success
            type: str
            sample: "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include
                  uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - A brief description of the CA.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "A property indicating when the CA was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the CA version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        kms_key_id:
            description:
                - The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the certificate authority.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current CA lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        compartment_id:
            description:
                - The OCID of the compartment under which the CA is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_authority_rules:
            description:
                - An optional list of rules that control how the CA is used and managed.
            returned: on success
            type: complex
            contains:
                rule_type:
                    description:
                        - The type of rule, whether a renewal rule regarding when to renew the CA or an issuance expiry rule that governs how long the
                          certificates and CAs issued by the CA are valid. (For internal use only) An internal issuance rule defines the number and type of
                          certificates that the CA can issue.
                    returned: on success
                    type: str
                    sample: CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE
                leaf_certificate_max_validity_duration:
                    description:
                        - A property indicating the maximum validity duration, in days, of leaf certificates issued by this CA.
                          Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                    returned: on success
                    type: str
                    sample: leaf_certificate_max_validity_duration_example
                certificate_authority_max_validity_duration:
                    description:
                        - A property indicating the maximum validity duration, in days, of subordinate CA's issued by this CA.
                          Expressed in L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format.
                    returned: on success
                    type: str
                    sample: certificate_authority_max_validity_duration_example
        current_version:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_authority_id:
                    description:
                        - The OCID of the CA.
                    returned: on success
                    type: str
                    sample: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
                issuer_ca_version_number:
                    description:
                        - The version number of the issuing CA.
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
                time_created:
                    description:
                        - "A optional property indicating when the CA version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                          timestamp format.
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
                time_of_deletion:
                    description:
                        - "An optional property indicating when to delete the CA version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                          format.
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
                - The origin of the CA.
            returned: on success
            type: str
            sample: ROOT_CA_GENERATED_INTERNALLY
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
        signing_algorithm:
            description:
                - The algorithm used to sign public key certificates that the CA issues.
            returned: on success
            type: str
            sample: SHA256_WITH_RSA
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "issuer_certificate_authority_id": "ocid1.issuercertificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_authority_rules": [{
            "rule_type": "CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE",
            "leaf_certificate_max_validity_duration": "leaf_certificate_max_validity_duration_example",
            "certificate_authority_max_validity_duration": "certificate_authority_max_validity_duration_example"
        }],
        "current_version": {
            "certificate_authority_id": "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
            "issuer_ca_version_number": 56,
            "serial_number": "serial_number_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "version_number": 56,
            "version_name": "version_name_example",
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
        "config_type": "ROOT_CA_GENERATED_INTERNALLY",
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
        "signing_algorithm": "SHA256_WITH_RSA",
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
    from oci.certificates_management.models import CreateCertificateAuthorityDetails
    from oci.certificates_management.models import UpdateCertificateAuthorityDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_module_resource_id_param(self):
        return "certificate_authority_id"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_authority_id")

    def get_get_fn(self):
        return self.client.get_certificate_authority

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "certificate_authority_id",
        ]

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
            self.client.list_certificate_authorities, **kwargs
        )

    def get_create_model_class(self):
        return CreateCertificateAuthorityDetails

    def get_exclude_attributes(self):
        return ["certificate_authority_config"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_certificate_authority,
            call_fn_args=(),
            call_fn_kwargs=dict(create_certificate_authority_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCertificateAuthorityDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_certificate_authority,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
                update_certificate_authority_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


CertificateAuthorityHelperCustom = get_custom_class("CertificateAuthorityHelperCustom")


class ResourceHelper(CertificateAuthorityHelperCustom, CertificateAuthorityHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            certificate_authority_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    rule_type=dict(
                        type="str",
                        required=True,
                        choices=["CERTIFICATE_AUTHORITY_ISSUANCE_EXPIRY_RULE"],
                    ),
                    leaf_certificate_max_validity_duration=dict(type="str"),
                    certificate_authority_max_validity_duration=dict(type="str"),
                ),
            ),
            certificate_authority_config=dict(
                type="dict",
                options=dict(
                    config_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ROOT_CA_GENERATED_INTERNALLY",
                            "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA",
                        ],
                    ),
                    version_name=dict(type="str"),
                    validity=dict(
                        type="dict",
                        options=dict(
                            time_of_validity_not_before=dict(type="str"),
                            time_of_validity_not_after=dict(type="str", required=True),
                        ),
                    ),
                    signing_algorithm=dict(
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
                    issuer_certificate_authority_id=dict(type="str"),
                    stage=dict(type="str", choices=["CURRENT", "PENDING"]),
                ),
            ),
            certificate_revocation_list_details=dict(
                type="dict",
                options=dict(
                    object_storage_config=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            object_storage_namespace=dict(type="str"),
                            object_storage_bucket_name=dict(type="str", required=True),
                            object_storage_object_name_format=dict(
                                type="str", required=True
                            ),
                        ),
                    ),
                    custom_formatted_urls=dict(type="list", elements="str"),
                ),
            ),
            kms_key_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            certificate_authority_id=dict(aliases=["id"], type="str"),
            current_version_number=dict(type="int"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="certificate_authority",
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
