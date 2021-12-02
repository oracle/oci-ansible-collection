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
module: oci_loadbalancer_ssl_cipher_suite
short_description: Manage a SslCipherSuite resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SslCipherSuite resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a custom SSL cipher suite.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - A friendly name for the SSL cipher suite. It must be unique and it cannot be changed.
            - "**Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or
                        reserved SSL cipher suite names:"
            - "* oci-default-ssl-cipher-suite-v1
              * oci-modern-ssl-cipher-suite-v1
              * oci-compatible-ssl-cipher-suite-v1
              * oci-wider-compatible-ssl-cipher-suite-v1
              * oci-customized-ssl-cipher-suite"
            - "example: `example_cipher_suite`"
        type: str
        required: true
    ciphers:
        description:
            - A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.
            - "The following ciphers are valid values for this property:"
            - "*  __TLSv1.2 ciphers__"
            - "       \\"AES128-GCM-SHA256\\"
                      \\"AES128-SHA256\\"
                      \\"AES256-GCM-SHA384\\"
                      \\"AES256-SHA256\\"
                      \\"DH-DSS-AES128-GCM-SHA256\\"
                      \\"DH-DSS-AES128-SHA256\\"
                      \\"DH-DSS-AES256-GCM-SHA384\\"
                      \\"DH-DSS-AES256-SHA256\\"
                      \\"DH-RSA-AES128-GCM-SHA256\\"
                      \\"DH-RSA-AES128-SHA256\\"
                      \\"DH-RSA-AES256-GCM-SHA384\\"
                      \\"DH-RSA-AES256-SHA256\\"
                      \\"DHE-DSS-AES128-GCM-SHA256\\"
                      \\"DHE-DSS-AES128-SHA256\\"
                      \\"DHE-DSS-AES256-GCM-SHA384\\"
                      \\"DHE-DSS-AES256-SHA256\\"
                      \\"DHE-RSA-AES128-GCM-SHA256\\"
                      \\"DHE-RSA-AES128-SHA256\\"
                      \\"DHE-RSA-AES256-GCM-SHA384\\"
                      \\"DHE-RSA-AES256-SHA256\\"
                      \\"ECDH-ECDSA-AES128-GCM-SHA256\\"
                      \\"ECDH-ECDSA-AES128-SHA256\\"
                      \\"ECDH-ECDSA-AES256-GCM-SHA384\\"
                      \\"ECDH-ECDSA-AES256-SHA384\\"
                      \\"ECDH-RSA-AES128-GCM-SHA256\\"
                      \\"ECDH-RSA-AES128-SHA256\\"
                      \\"ECDH-RSA-AES256-GCM-SHA384\\"
                      \\"ECDH-RSA-AES256-SHA384\\"
                      \\"ECDHE-ECDSA-AES128-GCM-SHA256\\"
                      \\"ECDHE-ECDSA-AES128-SHA256\\"
                      \\"ECDHE-ECDSA-AES256-GCM-SHA384\\"
                      \\"ECDHE-ECDSA-AES256-SHA384\\"
                      \\"ECDHE-RSA-AES128-GCM-SHA256\\"
                      \\"ECDHE-RSA-AES128-SHA256\\"
                      \\"ECDHE-RSA-AES256-GCM-SHA384\\"
                      \\"ECDHE-RSA-AES256-SHA384\\""
            - "*  __TLSv1 ciphers also supported by TLSv1.2__"
            - "       \\"AES128-SHA\\"
                      \\"AES256-SHA\\"
                      \\"CAMELLIA128-SHA\\"
                      \\"CAMELLIA256-SHA\\"
                      \\"DES-CBC3-SHA\\"
                      \\"DH-DSS-AES128-SHA\\"
                      \\"DH-DSS-AES256-SHA\\"
                      \\"DH-DSS-CAMELLIA128-SHA\\"
                      \\"DH-DSS-CAMELLIA256-SHA\\"
                      \\"DH-DSS-DES-CBC3-SHAv\\"
                      \\"DH-DSS-SEED-SHA\\"
                      \\"DH-RSA-AES128-SHA\\"
                      \\"DH-RSA-AES256-SHA\\"
                      \\"DH-RSA-CAMELLIA128-SHA\\"
                      \\"DH-RSA-CAMELLIA256-SHA\\"
                      \\"DH-RSA-DES-CBC3-SHA\\"
                      \\"DH-RSA-SEED-SHA\\"
                      \\"DHE-DSS-AES128-SHA\\"
                      \\"DHE-DSS-AES256-SHA\\"
                      \\"DHE-DSS-CAMELLIA128-SHA\\"
                      \\"DHE-DSS-CAMELLIA256-SHA\\"
                      \\"DHE-DSS-DES-CBC3-SHA\\"
                      \\"DHE-DSS-SEED-SHA\\"
                      \\"DHE-RSA-AES128-SHA\\"
                      \\"DHE-RSA-AES256-SHA\\"
                      \\"DHE-RSA-CAMELLIA128-SHA\\"
                      \\"DHE-RSA-CAMELLIA256-SHA\\"
                      \\"DHE-RSA-DES-CBC3-SHA\\"
                      \\"DHE-RSA-SEED-SHA\\"
                      \\"ECDH-ECDSA-AES128-SHA\\"
                      \\"ECDH-ECDSA-AES256-SHA\\"
                      \\"ECDH-ECDSA-DES-CBC3-SHA\\"
                      \\"ECDH-ECDSA-RC4-SHA\\"
                      \\"ECDH-RSA-AES128-SHA\\"
                      \\"ECDH-RSA-AES256-SHA\\"
                      \\"ECDH-RSA-DES-CBC3-SHA\\"
                      \\"ECDH-RSA-RC4-SHA\\"
                      \\"ECDHE-ECDSA-AES128-SHA\\"
                      \\"ECDHE-ECDSA-AES256-SHA\\"
                      \\"ECDHE-ECDSA-DES-CBC3-SHA\\"
                      \\"ECDHE-ECDSA-RC4-SHA\\"
                      \\"ECDHE-RSA-AES128-SHA\\"
                      \\"ECDHE-RSA-AES256-SHA\\"
                      \\"ECDHE-RSA-DES-CBC3-SHA\\"
                      \\"ECDHE-RSA-RC4-SHA\\"
                      \\"IDEA-CBC-SHA\\"
                      \\"KRB5-DES-CBC3-MD5\\"
                      \\"KRB5-DES-CBC3-SHA\\"
                      \\"KRB5-IDEA-CBC-MD5\\"
                      \\"KRB5-IDEA-CBC-SHA\\"
                      \\"KRB5-RC4-MD5\\"
                      \\"KRB5-RC4-SHA\\"
                      \\"PSK-3DES-EDE-CBC-SHA\\"
                      \\"PSK-AES128-CBC-SHA\\"
                      \\"PSK-AES256-CBC-SHA\\"
                      \\"PSK-RC4-SHA\\"
                      \\"RC4-MD5\\"
                      \\"RC4-SHA\\"
                      \\"SEED-SHA\\""
            - "example: `[\\"ECDHE-RSA-AES256-GCM-SHA384\\",\\"ECDHE-ECDSA-AES256-GCM-SHA384\\",\\"ECDHE-RSA-AES128-GCM-SHA256\\"]`"
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: list
        elements: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated load balancer.
        type: str
        required: true
    state:
        description:
            - The state of the SslCipherSuite.
            - Use I(state=present) to create or update a SslCipherSuite.
            - Use I(state=absent) to delete a SslCipherSuite.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ssl_cipher_suite
  oci_loadbalancer_ssl_cipher_suite:
    # required
    name: example_cipher_suite
    ciphers: [ "ECDHE-RSA-AES256-GCM-SHA384" ]
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update ssl_cipher_suite
  oci_loadbalancer_ssl_cipher_suite:
    # required
    name: example_cipher_suite
    ciphers: [ "ECDHE-RSA-AES256-GCM-SHA384" ]
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete ssl_cipher_suite
  oci_loadbalancer_ssl_cipher_suite:
    # required
    name: example_cipher_suite
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
ssl_cipher_suite:
    description:
        - Details of the SslCipherSuite resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A friendly name for the SSL cipher suite. It must be unique and it cannot be changed.
                - "**Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or
                            reserved SSL cipher suite names:"
                - "* oci-default-ssl-cipher-suite-v1
                  * oci-modern-ssl-cipher-suite-v1
                  * oci-compatible-ssl-cipher-suite-v1
                  * oci-wider-compatible-ssl-cipher-suite-v1
                  * oci-customized-ssl-cipher-suite"
                - "example: `example_cipher_suite`"
            returned: on success
            type: str
            sample: name_example
        ciphers:
            description:
                - A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.
                - "The following ciphers are valid values for this property:"
                - "*  __TLSv1.2 ciphers__"
                - "       \\"AES128-GCM-SHA256\\"
                          \\"AES128-SHA256\\"
                          \\"AES256-GCM-SHA384\\"
                          \\"AES256-SHA256\\"
                          \\"DH-DSS-AES128-GCM-SHA256\\"
                          \\"DH-DSS-AES128-SHA256\\"
                          \\"DH-DSS-AES256-GCM-SHA384\\"
                          \\"DH-DSS-AES256-SHA256\\"
                          \\"DH-RSA-AES128-GCM-SHA256\\"
                          \\"DH-RSA-AES128-SHA256\\"
                          \\"DH-RSA-AES256-GCM-SHA384\\"
                          \\"DH-RSA-AES256-SHA256\\"
                          \\"DHE-DSS-AES128-GCM-SHA256\\"
                          \\"DHE-DSS-AES128-SHA256\\"
                          \\"DHE-DSS-AES256-GCM-SHA384\\"
                          \\"DHE-DSS-AES256-SHA256\\"
                          \\"DHE-RSA-AES128-GCM-SHA256\\"
                          \\"DHE-RSA-AES128-SHA256\\"
                          \\"DHE-RSA-AES256-GCM-SHA384\\"
                          \\"DHE-RSA-AES256-SHA256\\"
                          \\"ECDH-ECDSA-AES128-GCM-SHA256\\"
                          \\"ECDH-ECDSA-AES128-SHA256\\"
                          \\"ECDH-ECDSA-AES256-GCM-SHA384\\"
                          \\"ECDH-ECDSA-AES256-SHA384\\"
                          \\"ECDH-RSA-AES128-GCM-SHA256\\"
                          \\"ECDH-RSA-AES128-SHA256\\"
                          \\"ECDH-RSA-AES256-GCM-SHA384\\"
                          \\"ECDH-RSA-AES256-SHA384\\"
                          \\"ECDHE-ECDSA-AES128-GCM-SHA256\\"
                          \\"ECDHE-ECDSA-AES128-SHA256\\"
                          \\"ECDHE-ECDSA-AES256-GCM-SHA384\\"
                          \\"ECDHE-ECDSA-AES256-SHA384\\"
                          \\"ECDHE-RSA-AES128-GCM-SHA256\\"
                          \\"ECDHE-RSA-AES128-SHA256\\"
                          \\"ECDHE-RSA-AES256-GCM-SHA384\\"
                          \\"ECDHE-RSA-AES256-SHA384\\""
                - "*  __TLSv1 ciphers also supported by TLSv1.2__"
                - "       \\"AES128-SHA\\"
                          \\"AES256-SHA\\"
                          \\"CAMELLIA128-SHA\\"
                          \\"CAMELLIA256-SHA\\"
                          \\"DES-CBC3-SHA\\"
                          \\"DH-DSS-AES128-SHA\\"
                          \\"DH-DSS-AES256-SHA\\"
                          \\"DH-DSS-CAMELLIA128-SHA\\"
                          \\"DH-DSS-CAMELLIA256-SHA\\"
                          \\"DH-DSS-DES-CBC3-SHAv\\"
                          \\"DH-DSS-SEED-SHA\\"
                          \\"DH-RSA-AES128-SHA\\"
                          \\"DH-RSA-AES256-SHA\\"
                          \\"DH-RSA-CAMELLIA128-SHA\\"
                          \\"DH-RSA-CAMELLIA256-SHA\\"
                          \\"DH-RSA-DES-CBC3-SHA\\"
                          \\"DH-RSA-SEED-SHA\\"
                          \\"DHE-DSS-AES128-SHA\\"
                          \\"DHE-DSS-AES256-SHA\\"
                          \\"DHE-DSS-CAMELLIA128-SHA\\"
                          \\"DHE-DSS-CAMELLIA256-SHA\\"
                          \\"DHE-DSS-DES-CBC3-SHA\\"
                          \\"DHE-DSS-SEED-SHA\\"
                          \\"DHE-RSA-AES128-SHA\\"
                          \\"DHE-RSA-AES256-SHA\\"
                          \\"DHE-RSA-CAMELLIA128-SHA\\"
                          \\"DHE-RSA-CAMELLIA256-SHA\\"
                          \\"DHE-RSA-DES-CBC3-SHA\\"
                          \\"DHE-RSA-SEED-SHA\\"
                          \\"ECDH-ECDSA-AES128-SHA\\"
                          \\"ECDH-ECDSA-AES256-SHA\\"
                          \\"ECDH-ECDSA-DES-CBC3-SHA\\"
                          \\"ECDH-ECDSA-RC4-SHA\\"
                          \\"ECDH-RSA-AES128-SHA\\"
                          \\"ECDH-RSA-AES256-SHA\\"
                          \\"ECDH-RSA-DES-CBC3-SHA\\"
                          \\"ECDH-RSA-RC4-SHA\\"
                          \\"ECDHE-ECDSA-AES128-SHA\\"
                          \\"ECDHE-ECDSA-AES256-SHA\\"
                          \\"ECDHE-ECDSA-DES-CBC3-SHA\\"
                          \\"ECDHE-ECDSA-RC4-SHA\\"
                          \\"ECDHE-RSA-AES128-SHA\\"
                          \\"ECDHE-RSA-AES256-SHA\\"
                          \\"ECDHE-RSA-DES-CBC3-SHA\\"
                          \\"ECDHE-RSA-RC4-SHA\\"
                          \\"IDEA-CBC-SHA\\"
                          \\"KRB5-DES-CBC3-MD5\\"
                          \\"KRB5-DES-CBC3-SHA\\"
                          \\"KRB5-IDEA-CBC-MD5\\"
                          \\"KRB5-IDEA-CBC-SHA\\"
                          \\"KRB5-RC4-MD5\\"
                          \\"KRB5-RC4-SHA\\"
                          \\"PSK-3DES-EDE-CBC-SHA\\"
                          \\"PSK-AES128-CBC-SHA\\"
                          \\"PSK-AES256-CBC-SHA\\"
                          \\"PSK-RC4-SHA\\"
                          \\"RC4-MD5\\"
                          \\"RC4-SHA\\"
                          \\"SEED-SHA\\""
                - "example: `[\\"ECDHE-RSA-AES256-GCM-SHA384\\",\\"ECDHE-ECDSA-AES256-GCM-SHA384\\",\\"ECDHE-RSA-AES128-GCM-SHA256\\"]`"
            returned: on success
            type: list
            sample: []
    sample: {
        "name": "name_example",
        "ciphers": []
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
    from oci.load_balancer.models import CreateSSLCipherSuiteDetails
    from oci.load_balancer.models import UpdateSSLCipherSuiteDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SslCipherSuiteHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_ssl_cipher_suite

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ssl_cipher_suite,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            name=self.module.params.get("name"),
        )

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
            self.client.list_ssl_cipher_suites, **kwargs
        )

    def get_create_model_class(self):
        return CreateSSLCipherSuiteDetails

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
            call_fn=self.client.create_ssl_cipher_suite,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_ssl_cipher_suite_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSSLCipherSuiteDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ssl_cipher_suite,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_ssl_cipher_suite_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ssl_cipher_suite,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


SslCipherSuiteHelperCustom = get_custom_class("SslCipherSuiteHelperCustom")


class ResourceHelper(SslCipherSuiteHelperCustom, SslCipherSuiteHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            ciphers=dict(type="list", elements="str"),
            load_balancer_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ssl_cipher_suite",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
