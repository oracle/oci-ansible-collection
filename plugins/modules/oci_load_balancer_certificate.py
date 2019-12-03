#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_load_balancer_certificate
short_description: Add or remove a SSL certificate from a load balancer in
                   OCI Load Balancing Service
description:
    - Add a SSL certificate to OCI Load Balancer
    - Delete a SSL certificate, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer in which the certificate belongs
        required: true
        aliases: ['id']
    name:
        description: The name of the certificate  to add to the load balancer.
        required: true
    ca_certificate:
        description: The Certificate Authority certificate, or any interim certificate,
                     that you received from your SSL certificate provider. The absolute
                     path of the certificate file should be provided.
        required: false
    passphrase:
        description: A passphrase for encrypted private keys. This is needed only if you
                     created your certificate with a passphrase.
        required: false
    private_key :
        description: The SSL private key for your certificate, in PEM format.The absolute
                     path of the private key file should be provided.
        required: false
    public_certificate:
        description: The public certificate, in PEM format, that you received
                     from your SSL certificate provider. The absolute
                     path of the public certificate file should be provided.
        required: false
    state:
        description: Create or  delete certificate. For I(state=present),
                     if it does not exists, it gets added.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Add a certificate bundle (without passphrase) to a loadbalancer
- name: Add a certificate bundle (without passphrase) to a loadbalancer
  oci_load_balancer_certificate:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_certtificate"
    ca_certificate: "certificate_src/ca_cert.pem"
    private_key: "certificate_src/private_key.pem"
    public_certificate: "certificate_src/cert.pem"
    state: 'present'
# Add a certificate bundle (with a passphrase for encrypted private keys) to a load balancer
- name: Create certificate with Passphrase
  oci_load_balancer_certificate:
    name: "ansible_cert_with_passphrase"
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    ca_certificate: "certificate_src/ca_cert.pem"
    passphrase: "ansible"
    private_key: "certificate_src/private_key_with_passphrase.pem"
    public_certificate: "certificate_src/cert_with_passphrase.pem"
    state: 'present'
# Delete a SSL Certificate from a load balancer
- name: Delete a SSL certificate
  oci_load_balancer_certificate:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_certtificate"
    state: 'absent'
"""

RETURN = """
    certificate:
        description: Attributes of the created certificate.
                     For delete, deleted certificate description will
                     be returned.
        returned: success
        type: complex
        contains:
            certificate_name:
                description: Name of the certificate
                returned: always
                type: string
                sample: ansible_certificate
            ca_certificate:
                description: The Certificate Authority certificate, or any interim certificate,
                             that you received from your SSL certificate provider.
                returned: always
                type: string
                sample: -----BEGIN CERTIFICATE-----
                            MIIDlTCCA
                        -----END CERTIFICATE-----
            public_certificate:
                description: The public certificate, in PEM format, that you received from
                             your SSL certificate provider.
                returned: always
                type: string
                sample: -----BEGIN CERTIFICATE-----
                            MIIDlTCCAn
                        -----END CERTIFICATE-----
        sample: {
                    "ca_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDlTCCAn2gAw\\n-----END CERTIFICATE-----",
                    "certificate_name":"ansible_cert",
                    "public_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDPjCCAiYCCQC5OEUUNtrC\\n-----END CERTIFICATE-----"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils


try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.util import to_dict
    from oci.load_balancer.models import CreateCertificateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_certificate(lb_client, module):
    result = dict(changed=False, certificate="")
    lb_id = module.params.get("load_balancer_id")
    name = module.params.get("name")

    certificate = oci_lb_utils.get_certificate(lb_client, module, lb_id, name)
    create_certificate_details = oci_lb_utils.get_create_certificate_details(
        module, name
    )
    same_certificate = False
    if certificate is not None:
        same_certificate = oci_lb_utils.is_same_certificate(
            create_certificate_details, certificate
        )
        if same_certificate:
            get_logger().info(
                "Certificate %s with same attribute values already available", name
            )
            result["changed"] = False
            result["certificate"] = to_dict(certificate)
        else:
            get_logger().error(
                "Certificate %s with different attribute value already available in load balancer %s",
                name,
                lb_id,
            )
            module.fail_json(
                msg="Certificate "
                + name
                + " with different attribute value already available in "
                "load balancer " + lb_id
            )
    if not same_certificate:
        get_logger().info(
            "Creating certificate %s in the load balancer %s", name, lb_id
        )
        result = oci_lb_utils.create_or_update_lb_resources_and_wait(
            resource_type="certificate",
            function=lb_client.create_certificate,
            kwargs_function={
                "create_certificate_details": create_certificate_details,
                "load_balancer_id": lb_id,
            },
            lb_client=lb_client,
            get_sub_resource_fn=oci_lb_utils.get_certificate,
            kwargs_get={
                "lb_client": lb_client,
                "module": module,
                "lb_id": lb_id,
                "name": name,
            },
            module=module,
        )
        get_logger().info(
            "Successfully created certificate %s in the load balancer %s", name, lb_id
        )

    return result


def delete_certificate(lb_client, module):
    lb_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    get_logger().info("Deleting certificate %s from the load balancer %s", name, lb_id)
    result = oci_lb_utils.delete_lb_resources_and_wait(
        resource_type="certificate",
        function=lb_client.delete_certificate,
        kwargs_function={"certificate_name": name, "load_balancer_id": lb_id},
        lb_client=lb_client,
        get_sub_resource_fn=oci_lb_utils.get_certificate,
        kwargs_get={
            "lb_client": lb_client,
            "module": module,
            "lb_id": lb_id,
            "name": name,
        },
        module=module,
    )
    get_logger().info(
        "Successfully deleted certificate %s from the load balancer %s", name, lb_id
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_certificate")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            ca_certificate=dict(type="str", required=False),
            passphrase=dict(type="str", required=False, no_log=True),
            private_key=dict(type="str", required=False),
            public_certificate=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    state = module.params["state"]

    if state == "present":
        result = oci_utils.check_and_create_resource(
            resource_type="certificate",
            create_fn=create_certificate,
            kwargs_create={"lb_client": lb_client, "module": module},
            list_fn=lb_client.list_certificates,
            kwargs_list={"load_balancer_id": module.params.get("load_balancer_id")},
            module=module,
            model=CreateCertificateDetails(),
        )
    elif state == "absent":
        result = delete_certificate(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
