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
module: oci_network_load_balancer_listener_protocols_facts
short_description: Fetches details about one or multiple ListenerProtocols resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ListenerProtocols resources in Oracle Cloud Infrastructure
    - This API has been deprecated so it won't return the updated list of supported protocls.
      Lists all supported traffic protocols.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sort_order:
        description:
            - The sort order to use, either 'asc' (ascending) or 'desc' (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
              The default order for displayName is ascending. If no value is specified, then timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List listener_protocols
  oci_network_load_balancer_listener_protocols_facts:

    # optional
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
listener_protocols:
    description:
        - List of ListenerProtocols resources
    returned: on success
    type: complex
    contains:
        items:
            description:
                - Array of NetworkLoadBalancersProtocolSummary objects.
            returned: on success
            type: list
            sample: []
    sample: [{
        "items": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.network_load_balancer import NetworkLoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerListenerProtocolsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_load_balancers_protocols, **optional_kwargs
        )


NetworkLoadBalancerListenerProtocolsFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerListenerProtocolsFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerListenerProtocolsFactsHelperCustom,
    NetworkLoadBalancerListenerProtocolsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="listener_protocols",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(listener_protocols=result)


if __name__ == "__main__":
    main()
