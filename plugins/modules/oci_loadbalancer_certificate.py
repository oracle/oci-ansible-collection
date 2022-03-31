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
module: oci_loadbalancer_certificate
short_description: Manage a Certificate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Certificate resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an asynchronous request to add an SSL certificate bundle.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    passphrase:
        description:
            - A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.
        type: str
    private_key:
        description:
            - The SSL private key for your certificate, in PEM format.
            - "Example:"
            - "   -----BEGIN RSA PRIVATE KEY-----
                  jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK
                  tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb
                  +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16
                  /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ
                  ...
                  -----END RSA PRIVATE KEY-----"
        type: str
    public_certificate:
        description:
            - The public certificate, in PEM format, that you received from your SSL certificate provider.
            - "Example:"
            - "   -----BEGIN CERTIFICATE-----
                  MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbM..QswCQYDVQQGEwJKU
                  A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxE..TAPBgNVBAoTCEZyY
                  MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWB..gNVBAMTD0ZyYW5rN
                  YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmc..mFuazRkZC5jb20wH
                  ...
                  -----END CERTIFICATE-----"
        type: str
    ca_certificate:
        description:
            - The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.
            - "Example:"
            - "   -----BEGIN CERTIFICATE-----
                  MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
                  EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
                  VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
                  aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
                  ...
                  -----END CERTIFICATE-----"
        type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer on which to add the certificate bundle.
        type: str
        aliases: ["id"]
        required: true
    certificate_name:
        description:
            - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
              Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
              Certificate bundle names cannot contain spaces. Avoid entering confidential information.
            - "Example: `example_certificate_bundle`"
        type: str
        aliases: ["name"]
        required: true
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
  oci_loadbalancer_certificate:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_name: certificate_name_example

    # optional
    passphrase: passphrase_example
    private_key: private_key_example
    public_certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    ca_certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"

- name: Delete certificate
  oci_loadbalancer_certificate:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_name: certificate_name_example
    state: absent

"""

RETURN = """
certificate:
    description:
        - Details of the Certificate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        certificate_name:
            description:
                - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                  Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                  Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                - "Example: `example_certificate_bundle`"
            returned: on success
            type: str
            sample: certificate_name_example
        public_certificate:
            description:
                - The public certificate, in PEM format, that you received from your SSL certificate provider.
                - "Example:"
                - "   -----BEGIN CERTIFICATE-----
                      MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
                      A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
                      MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
                      YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
                      ...
                      -----END CERTIFICATE-----"
            returned: on success
            type: str
            sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        ca_certificate:
            description:
                - The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.
                - "Example:"
                - "   -----BEGIN CERTIFICATE-----
                      MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
                      EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
                      VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
                      aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
                      ...
                      -----END CERTIFICATE-----"
            returned: on success
            type: str
            sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    sample: {
        "certificate_name": "certificate_name_example",
        "public_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----",
        "ca_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
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
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreateCertificateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateHelperGen(OCIResourceHelperBase):
    """Supported operations: create, list and delete"""

    def get_possible_entity_types(self):
        return super(CertificateHelperGen, self).get_possible_entity_types() + [
            "certificate",
            "certificates",
            "loadBalancercertificate",
            "loadBalancercertificates",
            "certificateresource",
            "certificatesresource",
            "loadbalancer",
        ]

    def get_module_resource_id_param(self):
        return "certificate_name"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_name")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.certificate_name:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "load_balancer_id",
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

    def get_exclude_attributes(self):
        return ["passphrase", "private_key"]

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_certificate_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
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
                load_balancer_id=self.module.params.get("load_balancer_id"),
                certificate_name=self.module.params.get("certificate_name"),
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
            passphrase=dict(type="str", no_log=True),
            private_key=dict(type="str", no_log=True),
            public_certificate=dict(type="str"),
            ca_certificate=dict(type="str"),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            certificate_name=dict(aliases=["name"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="certificate",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
