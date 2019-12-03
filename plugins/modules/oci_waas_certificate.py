#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

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
short_description: Manage WAAS certificates in OCI
description:
    - This module allows the user to create, delete and update WAAS certificates in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment in which to create the SSL certificate.
        type: str
    display_name:
        description: A user-friendly name for the SSL certificate. The name can be changed and does not need to be
                     unique.
        type: str
    certificate_data:
        description: The data of the SSL certificate.
        type: str
    private_key_data:
        description: The private key data of the SSL certificate.
        type: str
    is_trust_verification_disabled:
        description: The is_trust_verification_disabled of this certificate. Set to true if the SSL certificate
                     is self-signed.
        type: bool
    certificate_id:
        description: The OCID of the SSL certificate used in the WAAS policy. Required when deleting a WAAS certificate
                     with I(state=absent) or updating a WAAS certificate with I(state=present). This option is mutually
                     exclusive with I(compartment_id).
        type: str
    state:
        description: Create or update a WAAS certificate with I(state=present). Use I(state=absent) to delete a
                     WAAS certificate.
        default: present
        choices: ['present', 'absent']
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a waas certificate
  oci_waas_certificate:
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx"
    display_name: "test_waas_certificate"
    certificate_data: "{{ lookup('file', '/path/to/cert/file') }}"
    private_key_data: "{{ lookup('file', '/path/to/private/key') }}"
    is_trust_verification_disabled: True

- name: Update display name of the waas certificate
  oci_waas_certificate:
    certificate_id: "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx"
    display_name: "updated_test_waas_certificate"

- name: Delete a waas certificate
  oci_waas_certificate:
    certificate_id: "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx"
    state: absent
"""

RETURN = """
waas_certificate:
    description: Information about the WAAS certificate.
    returned: on successful create and update operation
    type: complex
    contains:
        compartment_id:
            description: The OCID of the certificate's compartment.
            returned: success
            type: str
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: A key-value pair with a defined schema that restricts the values of tags. These predefined keys
                         are scoped to namespaces.
            returned: success
            type: str
            sample: {"example_namespace": {"example_key": "example_value"}}
        display_name:
            description: The user-friendly name of the certificate.
            returned: success
            type: str
            sample: testcertificate
        extensions:
            description: The extensions of this Certificate.
            returned: success
            type: list
            sample: [
                {
                    "is_critical": null,
                    "name": "subjectKeyIdentifier",
                    "value": "A6:B2:56:XX:XX:XX:XX:XX:XX:XX:XX:9F:E1:98:2E:8C:F6"
                },
                {
                    "is_critical": null,
                    "name": "authorityKeyIdentifier",
                    "value": "keyid:A6:B2:56:XX:XX:XX:XX:XX:XX:XX:XX:9F:E1:98:2E:8C:F6"
                },
                {
                    "is_critical": true,
                    "name": "basicConstraints",
                    "value": "CA:TRUE"
                }
            ]
        freeform_tags:
            description: A simple key-value pair without any defined schema.
            returned: success
            type: complex
            sample: {"example_freeform_key": "example_freeform_value"}
        id:
            description: The OCID of the certificate.
            returned: success
            type: str
            sample: ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx
        issued_by:
            description: The issued_by of this Certificate.
            returned: success
            type: str
            sample: testissuer
        issuer_name:
            description: The issuer_name of this Certificate.
            returned: success
            type: complex
            sample: {
                "common_name": "testcommonname",
                "country": "AU",
                "email_address": "test.email@address.com",
                "locality": "testlocality",
                "organization": "testorg",
                "organizational_unit": "testorgunit",
                "state_province": "teststate"
            }
        lifecycle_state:
            description: The current lifecycle state of the SSL certificate.
            returned: success
            type: str
            sample: ACTIVE
        public_key_info:
            description: The public_key_info of this Certificate.
            returned: success
            type: complex
            sample: {
                "algorithm": "RSA",
                "exponent": 65537,
                "key_size": 2048
            }
        serial_number:
            description: The serial_number of this Certificate.
            returned: success
            type: str
            sample: 100000000000710
        signature_algorithm:
            description: The signature_algorithm of this Certificate.
            returned: success
            type: str
            sample: SHA-1
        subject_name:
            description: The subject_name of this Certificate.
            returned: success
            type: complex
            sample: {
                "common_name": "testcommonname",
                "country": "AU",
                "email_address": "test.email@address.com",
                "locality": "testlocality",
                "organization": "testorg",
                "organizational_unit": "testorgunit",
                "state_province": "teststate"
            }
        time_created:
            description: The date and time the certificate was created, expressed in RFC 3339 timestamp format.
            returned: success
            type: str
            sample: 2019-04-02T17:12:42.454000+00:00
        time_not_valid_after:
            description: The date and time the certificate will expire, expressed in RFC 3339 timestamp format.
            returned: success
            type: str
            sample: 2020-04-01T15:29:38+00:00
        time_not_valid_before:
            description: The time_not_valid_before of this Certificate.
            returned: success
            type: str
            sample: 2019-04-02T15:29:38+00:00
        version:
            description: The version of this Certificate.
            returned: success
            type: int
            sample: 2
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {"example_namespace": {"example_key": "example_value"}},
            "display_name": "testcertificate",
            "extensions": [
                {
                    "is_critical": null,
                    "name": "subjectKeyIdentifier",
                    "value": "A6:B2:56:XX:XX:XX:XX:XX:XX:XX:XX:9F:E1:98:2E:8C:F6"
                },
                {
                    "is_critical": null,
                    "name": "authorityKeyIdentifier",
                    "value": "keyid:A6:B2:56:XX:XX:XX:XX:XX:XX:XX:XX:9F:E1:98:2E:8C:F6"
                },
                {
                    "is_critical": true,
                    "name": "basicConstraints",
                    "value": "CA:TRUE"
                }
            ],
            "freeform_tags": {"example_freeform_key": "example_freeform_value"},
            "id": "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx",
            "issued_by": "testissuer",
            "issuer_name": {
                "common_name": "testcommonname",
                "country": "AU",
                "email_address": "test.email@address.com",
                "locality": "testlocality",
                "organization": "testorg",
                "organizational_unit": "testorgunit",
                "state_province": "teststate"
            },
            "lifecycle_state": "ACTIVE",
            "public_key_info": {
                "algorithm": "RSA",
                "exponent": 65537,
                "key_size": 2048
            },
            "serial_number": "100000000000710",
            "signature_algorithm": null,
            "subject_name": {
                "common_name": "testcommonname",
                "country": "AU",
                "email_address": "test.email@address.com",
                "locality": "testlocality",
                "organization": "testorg",
                "organizational_unit": "testorgunit",
                "state_province": "teststate"
            },
            "time_created": "2019-04-13T21:51:09.088000+00:00",
            "time_not_valid_after": "2020-04-01T15:29:38+00:00",
            "time_not_valid_before": "2019-04-02T15:29:38+00:00",
            "version": 2
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_waas_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.waas.models import CreateCertificateDetails
    from oci.waas.models import UpdateCertificateDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_TYPE = "waas_certificate"


def create_certificate(waas_client, module):
    create_certificate_details = CreateCertificateDetails()
    for attr in create_certificate_details.attribute_map.keys():
        if attr in module.params:
            setattr(create_certificate_details, attr, module.params[attr])
    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_TYPE,
        create_fn=waas_client.create_certificate,
        kwargs_create={"create_certificate_details": create_certificate_details},
        client=waas_client,
        get_fn=waas_client.get_certificate,
        get_param="certificate_id",
        module=module,
    )
    return result


def update_certificate(waas_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type=RESOURCE_TYPE,
        client=waas_client,
        get_fn=waas_client.get_certificate,
        kwargs_get={"certificate_id": module.params["certificate_id"]},
        update_fn=waas_client.update_certificate,
        primitive_params_update=["certificate_id"],
        kwargs_non_primitive_update={
            UpdateCertificateDetails: "update_certificate_details"
        },
        module=module,
        update_attributes=UpdateCertificateDetails().attribute_map.keys(),
    )
    return result


def delete_certificate(waas_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_TYPE,
        client=waas_client,
        get_fn=waas_client.get_certificate,
        kwargs_get={"certificate_id": module.params["certificate_id"]},
        delete_fn=waas_client.delete_certificate,
        kwargs_delete={"certificate_id": module.params["certificate_id"]},
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            certificate_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False),
            certificate_data=dict(type="str", required=False),
            private_key_data=dict(type="str", required=False, no_log=True),
            is_trust_verification_disabled=dict(type="bool", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("compartment_id", "certificate_id")],
    )

    waas_client = oci_utils.create_service_client(module, WaasClient)
    exclude_attributes = {}
    state = module.params["state"]
    certificate_id = module.params.get("certificate_id")

    if state == "absent":
        if not certificate_id:
            module.fail_json(
                msg="Specify certificate_id with state as 'absent' to delete the certificate."
            )
        result = delete_certificate(waas_client, module)

    else:
        if certificate_id:
            result = update_certificate(waas_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type=RESOURCE_TYPE,
                create_fn=create_certificate,
                kwargs_create={"waas_client": waas_client, "module": module},
                list_fn=waas_client.list_certificates,
                kwargs_list={"compartment_id": module.params["compartment_id"]},
                module=module,
                model=CreateCertificateDetails(),
                exclude_attributes=exclude_attributes,
                get_resource_from_summary_fn=oci_waas_utils.get_waas_certificate_from_summary_resource,
                get_resource_from_summary_fn_kwargs={"waas_client": waas_client},
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
