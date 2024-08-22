#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_golden_gate_certificate_facts
short_description: Fetches details about one or multiple Certificate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Certificate resources in Oracle Cloud Infrastructure
    - Returns a list of certificates from truststore.
    - If I(certificate_key) is specified, the details of a single Certificate will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_key:
        description:
            - A unique certificate identifier.
            - Required to get a specific certificate.
        type: str
    deployment_id:
        description:
            - A unique Deployment identifier.
        type: str
        required: true
    lifecycle_state:
        description:
            - A filter to return only connections having the 'lifecycleState' given.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific certificate
  oci_golden_gate_certificate_facts:
    # required
    certificate_key: certificate_key_example
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List certificates
  oci_golden_gate_certificate_facts:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
certificates:
    description:
        - List of Certificate resources
    returned: on success
    type: complex
    contains:
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_content:
            description:
                - The base64 encoded content of the PEM file containing the SSL certificate.
                - Returned for get operation
            returned: on success
            type: str
            sample: certificate_content_example
        issuer:
            description:
                - The Certificate issuer.
                - Returned for get operation
            returned: on success
            type: str
            sample: issuer_example
        md5_hash:
            description:
                - The Certificate md5Hash.
                - Returned for get operation
            returned: on success
            type: str
            sample: md5_hash_example
        public_key:
            description:
                - The Certificate public key.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
        public_key_algorithm:
            description:
                - The Certificate public key algorithm.
                - Returned for get operation
            returned: on success
            type: str
            sample: public_key_algorithm_example
        public_key_size:
            description:
                - The Certificate public key size.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        serial:
            description:
                - The Certificate serial.
                - Returned for get operation
            returned: on success
            type: str
            sample: serial_example
        time_valid_from:
            description:
                - The time the certificate is valid from. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The Certificate version.
                - Returned for get operation
            returned: on success
            type: str
            sample: version_example
        sha1_hash:
            description:
                - The Certificate sha1 hash.
                - Returned for get operation
            returned: on success
            type: str
            sample: sha1_hash_example
        authority_key_id:
            description:
                - The Certificate authority key id.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.authoritykey.oc1..xxxxxxEXAMPLExxxxxx"
        is_ca:
            description:
                - Indicates if the certificate is ca.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        subject_key_id:
            description:
                - The Certificate subject key id.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subjectkey.oc1..xxxxxxEXAMPLExxxxxx"
        key:
            description:
                - The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
                  It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.
            returned: on success
            type: str
            sample: key_example
        lifecycle_state:
            description:
                - Possible certificate lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        subject:
            description:
                - The Certificate subject.
            returned: on success
            type: str
            sample: subject_example
        is_self_signed:
            description:
                - Indicates if the certificate is self signed.
            returned: on success
            type: bool
            sample: true
        time_valid_to:
            description:
                - The time the certificate is valid to. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_content": "certificate_content_example",
        "issuer": "issuer_example",
        "md5_hash": "md5_hash_example",
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...",
        "public_key_algorithm": "public_key_algorithm_example",
        "public_key_size": 56,
        "serial": "serial_example",
        "time_valid_from": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "sha1_hash": "sha1_hash_example",
        "authority_key_id": "ocid1.authoritykey.oc1..xxxxxxEXAMPLExxxxxx",
        "is_ca": true,
        "subject_key_id": "ocid1.subjectkey.oc1..xxxxxxEXAMPLExxxxxx",
        "key": "key_example",
        "lifecycle_state": "CREATING",
        "subject": "subject_example",
        "is_self_signed": true,
        "time_valid_to": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deployment_id",
            "certificate_key",
        ]

    def get_required_params_for_list(self):
        return [
            "deployment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            deployment_id=self.module.params.get("deployment_id"),
            certificate_key=self.module.params.get("certificate_key"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificates,
            deployment_id=self.module.params.get("deployment_id"),
            **optional_kwargs
        )


CertificateFactsHelperCustom = get_custom_class("CertificateFactsHelperCustom")


class ResourceFactsHelper(CertificateFactsHelperCustom, CertificateFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_key=dict(type="str", no_log=True),
            deployment_id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
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
