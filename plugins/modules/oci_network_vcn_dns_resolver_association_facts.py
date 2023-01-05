#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_network_vcn_dns_resolver_association_facts
short_description: Fetches details about a VcnDnsResolverAssociation resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a VcnDnsResolverAssociation resource in Oracle Cloud Infrastructure
    - Get the associated DNS resolver information with a vcn
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vcn_dns_resolver_association
  oci_network_vcn_dns_resolver_association_facts:
    # required
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
vcn_dns_resolver_association:
    description:
        - VcnDnsResolverAssociation resource
    returned: on success
    type: complex
    contains:
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN in the association.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        dns_resolver_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DNS resolver in the association.
            returned: on success
            type: str
            sample: "ocid1.dnsresolver.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the association.
            returned: on success
            type: str
            sample: PROVISIONING
    sample: {
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "dns_resolver_id": "ocid1.dnsresolver.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VcnDnsResolverAssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "vcn_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vcn_dns_resolver_association,
            vcn_id=self.module.params.get("vcn_id"),
        )


VcnDnsResolverAssociationFactsHelperCustom = get_custom_class(
    "VcnDnsResolverAssociationFactsHelperCustom"
)


class ResourceFactsHelper(
    VcnDnsResolverAssociationFactsHelperCustom, VcnDnsResolverAssociationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(vcn_id=dict(aliases=["id"], type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vcn_dns_resolver_association",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(vcn_dns_resolver_association=result)


if __name__ == "__main__":
    main()
