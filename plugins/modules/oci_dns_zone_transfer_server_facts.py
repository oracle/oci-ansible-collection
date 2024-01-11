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
module: oci_dns_zone_transfer_server_facts
short_description: Fetches details about one or multiple ZoneTransferServer resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ZoneTransferServer resources in Oracle Cloud Infrastructure
    - Gets a list of IP addresses of OCI nameservers for inbound and outbound transfer of zones in the specified
      compartment (which must be the root compartment of a tenancy) that transfer zone data with external master or
      downstream nameservers.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
        type: str
        required: true
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List zone_transfer_servers
  oci_dns_zone_transfer_server_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    scope: GLOBAL

"""

RETURN = """
zone_transfer_servers:
    description:
        - List of ZoneTransferServer resources
    returned: on success
    type: complex
    contains:
        address:
            description:
                - The server's IP address (IPv4 or IPv6).
            returned: on success
            type: str
            sample: address_example
        port:
            description:
                - The server's port.
            returned: on success
            type: int
            sample: 56
        is_transfer_source:
            description:
                - A Boolean flag indicating whether or not the server is a zone data transfer source.
            returned: on success
            type: bool
            sample: true
        is_transfer_destination:
            description:
                - A Boolean flag indicating whether or not the server is a zone data transfer destination.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "address": "address_example",
        "port": 56,
        "is_transfer_source": true,
        "is_transfer_destination": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ZoneTransferServerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_zone_transfer_servers,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ZoneTransferServerFactsHelperCustom = get_custom_class(
    "ZoneTransferServerFactsHelperCustom"
)


class ResourceFactsHelper(
    ZoneTransferServerFactsHelperCustom, ZoneTransferServerFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="zone_transfer_server",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(zone_transfer_servers=result)


if __name__ == "__main__":
    main()
