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
module: oci_waas_certificate
short_description: Manage a WaasCertificate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a WaasCertificate resource in Oracle Cloud Infrastructure
    - For I(state=present), allows an SSL certificate to be added to a WAAS policy. The Web Application Firewall terminates SSL connections to inspect requests
      in runtime, and then re-encrypts requests before sending them to the origin for fulfillment.
    - For more information, see L(WAF Settings,https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafsettings.htm).
    - "This resource has the following action operations in the M(oci_waas_certificate_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to create the SSL certificate.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    certificate_data:
        description:
            - The data of the SSL certificate.
            - "**Note:** Many SSL certificate providers require an intermediate certificate chain to ensure a trusted status.
              If your SSL certificate requires an intermediate certificate chain, please append the intermediate certificate
              key in the `certificateData` field after the leaf certificate issued by the SSL certificate provider. If you
              are unsure if your certificate requires an intermediate certificate chain, see your certificate
              provider's documentation."
            - The example below shows an intermediate certificate appended to a leaf certificate.
            - Required for create using I(state=present).
        type: str
    private_key_data:
        description:
            - The private key of the SSL certificate.
            - Required for create using I(state=present).
        type: str
    is_trust_verification_disabled:
        description:
            - Set to `true` if the SSL certificate is self-signed.
        type: bool
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    certificate_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SSL certificate used in the WAAS policy. This number is
              generated when the certificate is added to the policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the WaasCertificate.
            - Use I(state=present) to create or update a WaasCertificate.
            - Use I(state=absent) to delete a WaasCertificate.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create waas_certificate
  oci_waas_certificate:
    compartment_id: "ocid1.compartment.oc1.."
    certificate_data: "-----BEGIN CERTIFICATE-----this-is-not-the-secret-----END CERTIFICATE-----"
    private_key_data: "-----BEGIN PRIVATE KEY-----this-is-not-the-secret-----END PRIVATE KEY-----"

- name: Update waas_certificate using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_certificate:
    compartment_id: "ocid1.compartment.oc1.."
    display_name: example.com Certificate
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update waas_certificate
  oci_waas_certificate:
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete waas_certificate
  oci_waas_certificate:
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete waas_certificate using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_certificate:
    compartment_id: "ocid1.compartment.oc1.."
    display_name: example.com Certificate
    state: absent

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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the certificate's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the certificate.
            returned: on success
            type: str
            sample: display_name_example
        issued_by:
            description:
                - ""
            returned: on success
            type: str
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
                    type: str
                    sample: country_example
                state_province:
                    description:
                        - The province where the organization is located.
                    returned: on success
                    type: str
                    sample: state_province_example
                locality:
                    description:
                        - The city in which the organization is located.
                    returned: on success
                    type: str
                    sample: locality_example
                organization:
                    description:
                        - The organization name.
                    returned: on success
                    type: str
                    sample: organization_example
                organizational_unit:
                    description:
                        - The field to differentiate between divisions within an organization.
                    returned: on success
                    type: str
                    sample: organizational_unit_example
                common_name:
                    description:
                        - The fully qualified domain name used for DNS lookups of the server.
                    returned: on success
                    type: str
                    sample: common_name_example
                email_address:
                    description:
                        - The email address of the server's administrator.
                    returned: on success
                    type: str
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
                    type: str
                    sample: country_example
                state_province:
                    description:
                        - The province where the organization is located.
                    returned: on success
                    type: str
                    sample: state_province_example
                locality:
                    description:
                        - The city in which the organization is located.
                    returned: on success
                    type: str
                    sample: locality_example
                organization:
                    description:
                        - The organization name.
                    returned: on success
                    type: str
                    sample: organization_example
                organizational_unit:
                    description:
                        - The field to differentiate between divisions within an organization.
                    returned: on success
                    type: str
                    sample: organizational_unit_example
                common_name:
                    description:
                        - The Certificate Authority (CA) name.
                    returned: on success
                    type: str
                    sample: common_name_example
                email_address:
                    description:
                        - The email address of the server's administrator.
                    returned: on success
                    type: str
                    sample: email_address_example
        serial_number:
            description:
                - A unique, positive integer assigned by the Certificate Authority (CA). The issuer name and serial number identify a unique certificate.
            returned: on success
            type: str
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
            type: str
            sample: signature_algorithm_example
        time_not_valid_before:
            description:
                - The date and time the certificate will become valid, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2018-11-16T21:10:29Z"
        time_not_valid_after:
            description:
                - The date and time the certificate will expire, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2018-11-16T21:10:29Z"
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
                    type: str
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
                    type: str
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
                    type: str
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
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the certificate was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2018-11-16T21:10:29Z"
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
            type: str
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import CreateCertificateDetails
    from oci.waas.models import UpdateCertificateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasCertificateHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
        return ["private_key_data"]

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

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_id=self.module.params.get("certificate_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


WaasCertificateHelperCustom = get_custom_class("WaasCertificateHelperCustom")


class ResourceHelper(WaasCertificateHelperCustom, WaasCertificateHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            certificate_data=dict(type="str"),
            private_key_data=dict(type="str", no_log=True),
            is_trust_verification_disabled=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            certificate_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
