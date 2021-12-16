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
module: oci_certificates_management_certificate_authority_actions
short_description: Perform actions on a CertificateAuthority resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CertificateAuthority resource in Oracle Cloud Infrastructure
    - For I(action=cancel_certificate_authority_deletion), cancels the scheduled deletion of the specified certificate authority (CA).
    - For I(action=change_compartment), moves a certificate authority (CA) to a different compartment within the same tenancy. For information about
      moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      When provided, If-Match is checked against the ETag values of the source.
    - For I(action=schedule_certificate_authority_deletion), schedules the deletion of the specified certificate authority (CA). This sets the lifecycle state
      of the CA to `PENDING_DELETION` and then deletes it after the specified retention period ends. If needed, you can determine the status of the deletion by
      using `GetCertificateAuthority`.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA).
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the CA should move.
            - Required for I(action=change_compartment).
        type: str
    time_of_deletion:
        description:
            - "An optional property indicating when to delete the CA, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
              Example: `2019-04-03T21:10:29.600Z`"
            - Applicable only for I(action=schedule_certificate_authority_deletion).
        type: str
    action:
        description:
            - The action to perform on the CertificateAuthority.
        type: str
        required: true
        choices:
            - "cancel_certificate_authority_deletion"
            - "change_compartment"
            - "schedule_certificate_authority_deletion"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel_certificate_authority_deletion on certificate_authority
  oci_certificates_management_certificate_authority_actions:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel_certificate_authority_deletion

- name: Perform action change_compartment on certificate_authority
  oci_certificates_management_certificate_authority_actions:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action schedule_certificate_authority_deletion on certificate_authority
  oci_certificates_management_certificate_authority_actions:
    # required
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    action: schedule_certificate_authority_deletion

    # optional
    time_of_deletion: time_of_deletion_example

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.certificates_management import CertificatesManagementClient
    from oci.certificates_management.models import (
        ChangeCertificateAuthorityCompartmentDetails,
    )
    from oci.certificates_management.models import (
        ScheduleCertificateAuthorityDeletionDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_certificate_authority_deletion
        change_compartment
        schedule_certificate_authority_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def cancel_certificate_authority_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_certificate_authority_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCertificateAuthorityCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_certificate_authority_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
                change_certificate_authority_compartment_details=action_details,
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

    def schedule_certificate_authority_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleCertificateAuthorityDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_certificate_authority_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
                schedule_certificate_authority_deletion_details=action_details,
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


CertificateAuthorityActionsHelperCustom = get_custom_class(
    "CertificateAuthorityActionsHelperCustom"
)


class ResourceHelper(
    CertificateAuthorityActionsHelperCustom, CertificateAuthorityActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            certificate_authority_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            time_of_deletion=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_certificate_authority_deletion",
                    "change_compartment",
                    "schedule_certificate_authority_deletion",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
