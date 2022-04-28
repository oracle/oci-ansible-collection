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
module: oci_identity_fault_domain_facts
short_description: Fetches details about one or multiple FaultDomain resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FaultDomain resources in Oracle Cloud Infrastructure
    - Lists the Fault Domains in your tenancy. Specify the OCID of either the tenancy or another
      of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment).
      See L(Where to Get the Tenancy's OCID and User's OCID,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#five).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
        type: str
        required: true
    availability_domain:
        description:
            - The name of the availabilityDomain.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List fault_domains
  oci_identity_fault_domain_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

"""

RETURN = """
fault_domains:
    description:
        - List of FaultDomain resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the Fault Domain.
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The OCID of the Fault Domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment. Currently only tenancy (root) compartment can be provided.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The name of the availabilityDomain where the Fault Domain belongs.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
    sample: [{
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FaultDomainFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "availability_domain",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_fault_domains,
            compartment_id=self.module.params.get("compartment_id"),
            availability_domain=self.module.params.get("availability_domain"),
            **optional_kwargs
        )


FaultDomainFactsHelperCustom = get_custom_class("FaultDomainFactsHelperCustom")


class ResourceFactsHelper(FaultDomainFactsHelperCustom, FaultDomainFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    module.params["do_not_redirect_to_home_region"] = True

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fault_domain",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(fault_domains=result)


if __name__ == "__main__":
    main()
