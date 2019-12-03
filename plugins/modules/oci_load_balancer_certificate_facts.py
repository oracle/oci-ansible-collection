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
module: oci_load_balancer_certificate_facts
short_description: Fetch details of all certificates associated with a load balancer
description:
    - Fetch details of all certificates or details of a particular certificate that is associated with a load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer to which the certificate belongs.
        required: true
        aliases: ['id']
    name:
        description: The name of the certificate wose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of all certificates of a load balancer
- name: List all Load Balancer certificates
  oci_load_balancer_certificate_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

#Fetch details of a specific certificate of a load balancer
- name: List a specific certificate
  oci_load_balancer_certificate_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
      name: 'ansible_certificate'
"""

RETURN = """
    certificate:
        description: Attributes of the created certificates.
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
        sample: [{
                    "ca_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDlTCCAn2gAw\\n-----END CERTIFICATE-----",
                    "certificate_name":"ansible_cert_one",
                    "public_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDPjCCAiYCCQC5OEUUNtrC\\n-----END CERTIFICATE-----"
                },
                {
                    "ca_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDlTCCAn2gAw\\n-----END CERTIFICATE-----",
                    "certificate_name":"ansible_cert_two",
                    "public_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDPjCCAiYCCQC5OEUUNtrC\\n-----END CERTIFICATE-----"
                }]
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_load_balancer_certificates(lb_client, module):
    result = dict(certificates="")
    name = module.params.get("name")
    load_balancer_id = module.params["load_balancer_id"]
    existing_certificates = []
    try:
        if name is None or not name:
            get_logger().debug(
                "Listing all certificates under load balancer %s", load_balancer_id
            )
            existing_certificates = oci_utils.list_all_resources(
                lb_client.list_certificates, load_balancer_id=load_balancer_id
            )
        else:
            get_logger().debug(
                "Listing certificate %s on load balancer %s", name, load_balancer_id
            )
            response = oci_utils.call_with_backoff(
                lb_client.list_certificates, load_balancer_id=load_balancer_id
            )
            certificates = response.data
            for certificate in certificates:
                if certificate.certificate_name == name:
                    existing_certificates = [certificate]
                    break
    except ServiceError as ex:
        get_logger().error("Unable to list Backend Sets due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["certificates"] = to_dict(existing_certificates)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_certificate_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            name=dict(type="str", required=False),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_certificates(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
