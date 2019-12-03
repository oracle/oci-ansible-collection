#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_fault_domain_facts
short_description: Retrieve details of fault domains in your tenancy
description:
    - This module retrieves details of all fault domains in your tenancy. Specify the OCID of either the tenancy
      or another of your compartments as the value for the compartment ID (remember that the tenancy is simply
      the root compartment).
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment (either the tenancy or another compartment in the tenancy).
        required: true
    availability_domain:
        description: The name of the availibility domain.
        required: true
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get details of all the fault domains in AD1 in your tenancy
  oci_fault_domain_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
    availability_domain: "IwGV:US-ASHBURN-AD-2"
"""

RETURN = """
fault_domains:
    description: Information about one or more fault domains in your tenancy
    returned: on success
    type: complex
    contains:
        name:
            description: The name of the Fault Domain.
            returned: always
            type: string
            sample: FAULT-DOMAIN-1
        compartment_id:
            description: The OCID of the compartment.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq
        availability_domain:
            description: The name of the availabilityDomain where the Fault Domain belongs.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-2
        id:
            description: The OCID of the Fault Domain.
            returned: always
            type: string
            sample: ocid1.faultdomain.oc1..xxxxxEXAMPLExxxxx..4dnw3a
    sample: {
       "fault_domains": [
            {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
              "id": "ocid1.faultdomain.oc1..xxxxxEXAMPLExxxxx..4dnw3a",
              "availability_domain": "IwGV:US-ASHBURN-AD-2",
              "name": "FAULT-DOMAIN-1"
            },
            {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
              "id": "ocid1.faultdomain.oc1..xxxxxEXAMPLExxxxx..3dsdaa",
              "availability_domain": "IwGV:US-ASHBURN-AD-2",
              "name": "FAULT-DOMAIN-2"
            },
            {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
              "id": "ocid1.faultdomain.oc1..xxxxxEXAMPLExxxxx..6ttdaa",
              "availability_domain": "IwGV:US-ASHBURN-AD-2",
              "name": "FAULT-DOMAIN-3"
            }
          ]
       }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_fault_domains(identity_client, module):
    try:
        cid = module.params["compartment_id"]
        ad = module.params["availability_domain"]
        name = module.params["name"]
        fault_domains = oci_utils.list_all_resources(
            identity_client.list_fault_domains,
            compartment_id=cid,
            availability_domain=ad,
            name=name,
        )
    except AttributeError as ae:
        # list_fault_domains is not available
        module.fail_json(
            msg="Exception: {0}. OCI Python SDK 2.0.1 or above is required to use "
            "`oci_fault_domain_facts`. The local SDK version is {1}".format(
                str(ae), oci.__version__
            )
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    return to_dict(fault_domains)


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type=str, required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    # oci.identity.identity_client.IdentityClient#list_fault_domains uses the REGION in the config to get fault domains
    # for a specific region and ad. So do not automatically redirect all
    # oci.identity.identity_client.IdentityClient#list_fault_domains calls to the Home region while creating the
    # service client
    module.params["do_not_redirect_to_home_region"] = True

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = list_fault_domains(identity_client, module)
    module.exit_json(fault_domains=result)


if __name__ == "__main__":
    main()
