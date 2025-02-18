#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_golden_gate_certificate
short_description: Manage a Certificate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Certificate resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new certificate to truststore.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    key:
        description:
            - The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
              It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.
            - Required for create using I(state=present).
        type: str
    certificate_content:
        description:
            - The base64 encoded content of the PEM file containing the SSL certificate.
            - Required for create using I(state=present).
        type: str
    deployment_id:
        description:
            - A unique Deployment identifier.
        type: str
        required: true
    certificate_key:
        description:
            - A unique certificate identifier.
            - Required for delete using I(state=absent).
        type: str
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
        type: bool
    state:
        description:
            - The state of the Certificate.
            - Use I(state=present) to create a Certificate.
            - Use I(state=absent) to delete a Certificate.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create certificate
  oci_golden_gate_certificate:
    # required
    key: key_example
    certificate_content: certificate_content_example
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_lock_override: true

- name: Delete certificate
  oci_golden_gate_certificate:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_key: certificate_key_example
    state: absent

    # optional
    is_lock_override: true

"""

RETURN = """
certificate:
    description:
        - Details of the Certificate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
                  It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.
            returned: on success
            type: str
            sample: key_example
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_content:
            description:
                - The base64 encoded content of the PEM file containing the SSL certificate.
            returned: on success
            type: str
            sample: certificate_content_example
        issuer:
            description:
                - The Certificate issuer.
            returned: on success
            type: str
            sample: issuer_example
        is_self_signed:
            description:
                - Indicates if the certificate is self signed.
            returned: on success
            type: bool
            sample: true
        md5_hash:
            description:
                - The Certificate md5Hash.
            returned: on success
            type: str
            sample: md5_hash_example
        public_key:
            description:
                - The Certificate public key.
            returned: on success
            type: str
            sample: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
        public_key_algorithm:
            description:
                - The Certificate public key algorithm.
            returned: on success
            type: str
            sample: public_key_algorithm_example
        public_key_size:
            description:
                - The Certificate public key size.
            returned: on success
            type: int
            sample: 56
        serial:
            description:
                - The Certificate serial.
            returned: on success
            type: str
            sample: serial_example
        subject:
            description:
                - The Certificate subject.
            returned: on success
            type: str
            sample: subject_example
        time_valid_from:
            description:
                - The time the certificate is valid from. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_valid_to:
            description:
                - The time the certificate is valid to. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The Certificate version.
            returned: on success
            type: str
            sample: version_example
        sha1_hash:
            description:
                - The Certificate sha1 hash.
            returned: on success
            type: str
            sample: sha1_hash_example
        authority_key_id:
            description:
                - The Certificate authority key id.
            returned: on success
            type: str
            sample: "ocid1.authoritykey.oc1..xxxxxxEXAMPLExxxxxx"
        is_ca:
            description:
                - Indicates if the certificate is ca.
            returned: on success
            type: bool
            sample: true
        subject_key_id:
            description:
                - The Certificate subject key id.
            returned: on success
            type: str
            sample: "ocid1.subjectkey.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Possible certificate lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "key": "key_example",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_content": "certificate_content_example",
        "issuer": "issuer_example",
        "is_self_signed": true,
        "md5_hash": "md5_hash_example",
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...",
        "public_key_algorithm": "public_key_algorithm_example",
        "public_key_size": 56,
        "serial": "serial_example",
        "subject": "subject_example",
        "time_valid_from": "2013-10-20T19:20:30+01:00",
        "time_valid_to": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "sha1_hash": "sha1_hash_example",
        "authority_key_id": "ocid1.authoritykey.oc1..xxxxxxEXAMPLExxxxxx",
        "is_ca": true,
        "subject_key_id": "ocid1.subjectkey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateCertificateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(CertificateHelperGen, self).get_possible_entity_types() + [
            "goldengatedeployment",
            "goldengatedeployments",
            "goldenGategoldengatedeployment",
            "goldenGategoldengatedeployments",
            "goldengatedeploymentresource",
            "goldengatedeploymentsresource",
            "certificate",
            "certificates",
            "goldenGatecertificate",
            "goldenGatecertificates",
            "certificateresource",
            "certificatesresource",
            "goldengate",
        ]

    def get_module_resource_id_param(self):
        return "certificate_key"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_key")

    def get_get_fn(self):
        return self.client.get_certificate

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            certificate_key=summary_model.key,
            deployment_id=self.module.params.get("deployment_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            deployment_id=self.module.params.get("deployment_id"),
            certificate_key=self.module.params.get("certificate_key"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "deployment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_certificates, **kwargs
        )

    def get_create_model_class(self):
        return CreateCertificateDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_certificate_details=create_details,
                deployment_id=self.module.params.get("deployment_id"),
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                certificate_key=self.module.params.get("certificate_key"),
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
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
            key=dict(type="str", no_log=True),
            certificate_content=dict(type="str"),
            deployment_id=dict(type="str", required=True),
            certificate_key=dict(type="str", no_log=True),
            is_lock_override=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="certificate",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
