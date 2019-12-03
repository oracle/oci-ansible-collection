#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_ad_facts
short_description: Retrieve details of availability domains in your tenancy for a given region
description:
    - This module retrieves details of all availability domains in your tenancy. By default, the region configured
      in your OCI SDK configuration is used. To retrieve details of all availability domains in your tenancy for a
      different region, use I(region) to specify the region for which availability domains must be retrieved.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment (either the tenancy or another compartment in the tenancy).
        required: true
        aliases: ['id']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all the availability domains in your tenancy (default configured region)
  oci_ad_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'

- name: Get details of all the availability domains in your tenancy for a specified non-default region
  oci_ad_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
    region: 'us-phoenix-1'
"""

RETURN = """
availability_domains:
    description: Information about one or more availability domains in your tenancy
    returned: on success
    type: complex
    contains:
        name:
            description: The name of the Availability Domain.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        compartment_id:
            description: The OCID of the compartment
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq
    sample: {
       "availability_domains": [
            {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
              "name": "IwGV:US-ASHBURN-AD-1"
            },
            {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
              "name": "IwGV:US-ASHBURN-AD-2"
            },
            {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
              "name": "IwGV:US-ASHBURN-AD-3"
            }
          ]
       }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_availability_domains(identity_client, module):
    try:
        cid = module.params["compartment_id"]
        ads = oci_utils.call_with_backoff(
            identity_client.list_availability_domains, compartment_id=cid
        ).data
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    return to_dict(ads)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(compartment_id=dict(type="str", required=True, aliases=["id"]))
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    # oci.identity.identity_client.IdentityClient#list_availability_domains uses the REGION in the config to get ADs
    # for a specific region. So do not automatically redirect all
    # oci.identity.identity_client.IdentityClient#list_availability_domains calls to the Home region while creating the
    # service client
    module.params["do_not_redirect_to_home_region"] = True

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = list_availability_domains(identity_client, module)
    module.exit_json(availability_domains=result)


if __name__ == "__main__":
    main()
