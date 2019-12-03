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
module: oci_waas_certificate_facts
short_description: Retrieve details about WAAS certificates.
description:
    - This module retrieves information of a specific WAAS certificate or lists all the WAAS certificates in the given
      compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        type: str
    certificate_id:
        description: The OCID of the SSL certificate used in the WAAS policy. Required to get information of a specific
                     certificate.
        type: str
    id:
        description: Filter certificates using a list of certificates OCIDs.
        type: list
    display_name:
        description: Filter certificates using a list of display names.
        type: list
    lifecycle_state:
        description: Filter certificates using a list of lifecycle states.
        type: list
        choices:
        - "CREATING"
        - "ACTIVE"
        - "FAILED"
        - "UPDATING"
        - "DELETING"
        - "DELETED"
    time_created_greater_than_or_equal_to:
        description: A filter that matches certificates created on or after the specified date-time.
        type: str
    time_created_less_than:
        description: A filter that matches certificates created before the specified date-time.
        type: str
    sort_by:
        description: The value by which certificate summaries are sorted in a paginated 'List' call.
                     If unspecified, defaults to timeCreated.
        type: str
        choices: ["id", "compartmentId", "displayName", "notValidAfter", "timeCreated"]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_sort_order_option ]
"""

EXAMPLES = """
- name: Get all the waas certificates in a compartment
  oci_waas_certificate_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get a specific waas certificate using its OCID
  oci_waas_certificate_facts:
    certificate_id: ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx

- name: Get waas certificate having the specified display name
  oci_waas_certificate_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name: examplewaascertificate

- name: Get waas certificates in a compartment with given display names
  oci_waas_certificate_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name:
        - examplewaascertificate1
        - examplewaascertificate2

- name: Filter waas certificates in a compartment using display_name, lifecycle_state and sort the results
  oci_waas_certificate_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name:
        - examplewaascertificate1
        - examplewaascertificate2
    lifecycle_state:
        - ACTIVE
    sort_by: timeCreated
    sort_order: DESC
"""

RETURN = """
waas_certificates:
    description: List of waas certificates
    returned: on success
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
            sample: [{"is_critical": null, "name": "subjectKeyIdentifier", "value": "A6:B2:56:1X:1X:1X:1X:8C:F6"}]
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
    sample: [
                {
                    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "defined_tags": null,
                    "display_name": "test waas certificate",
                    "extensions": null,
                    "freeform_tags": null,
                    "id": "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx",
                    "issued_by": "Ansible",
                    "issuer_name": {
                        "common_name": "testcommonname",
                        "country": "IN",
                        "email_address": null,
                        "locality": "Bangalore",
                        "organization": "Ansible",
                        "organizational_unit": null,
                        "state_province": "KA"
                    },
                    "lifecycle_state": "ACTIVE",
                    "public_key_info": {
                        "algorithm": "RSA",
                        "exponent": 65537,
                        "key_size": 2048
                    },
                    "serial_number": "9917593779878295042",
                    "signature_algorithm": null,
                    "subject_name": {
                        "common_name": "testcommonname",
                        "country": "IN",
                        "email_address": null,
                        "locality": "Bangalore",
                        "organization": "Ansible",
                        "organizational_unit": null,
                        "state_province": "KA"
                    },
                    "time_created": "2019-04-10T10:05:35.634000+00:00",
                    "time_not_valid_after": "2024-04-08T08:09:17+00:00",
                    "time_not_valid_before": "2019-04-10T08:09:17+00:00",
                    "version": null
                }
            ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def list_certificates(waas_client, module):
    if not module.params.get("compartment_id"):
        module.fail_json(msg="compartment_id required to list certificates.")
    optional_list_method_params = [
        "sort_by",
        "sort_order",
        "id",
        "display_name",
        "lifecycle_state",
        "time_created_greater_than_or_equal_to",
        "time_created_less_than",
    ]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_certificate, certificate_id=certificate.id
            ).data
            for certificate in oci_utils.list_all_resources(
                waas_client.list_certificates,
                compartment_id=module.params["compartment_id"],
                **optional_kwargs
            )
        ]
    )


def get_certificate(waas_client, module):
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_certificate,
                certificate_id=module.params["certificate_id"],
            ).data
        ]
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec(
        filter_by_display_name=False,
        supports_sort=True,
        sort_by_choices=[
            "id",
            "compartmentId",
            "displayName",
            "notValidAfter",
            "timeCreated",
        ],
    )
    module_args.update(
        dict(
            certificate_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="list"),
            id=dict(type="list"),
            lifecycle_state=dict(
                type="list",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                ],
            ),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["certificate_id", "compartment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    waas_client = oci_utils.create_service_client(module, WaasClient)

    try:
        if module.params["certificate_id"]:
            result = get_certificate(waas_client, module)
        elif module.params["compartment_id"]:
            result = list_certificates(waas_client, module)
        else:
            module.fail_json(
                msg="Specify a compartment_id to get all the certificates in the compartment or certificate_id "
                "to retrieve a specific certificate."
            )
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(waas_certificates=result)


if __name__ == "__main__":
    main()
