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
module: oci_loadbalancer_hostname_facts
short_description: Fetches details about one or multiple Hostname resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Hostname resources in Oracle Cloud Infrastructure
    - Lists all hostname resources associated with the specified load balancer.
    - If I(name) is specified, the details of a single Hostname will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the hostname resource to retrieve.
            - "Example: `example_hostname_001`"
            - Required to get a specific hostname.
        type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific hostname
  oci_loadbalancer_hostname_facts:
    # required
    name: name_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: List hostnames
  oci_loadbalancer_hostname_facts:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
hostnames:
    description:
        - List of Hostname resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential
                  information.
                - "Example: `example_hostname_001`"
            returned: on success
            type: str
            sample: name_example
        hostname:
            description:
                - A virtual hostname. For more information about virtual hostname string construction, see
                  L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing).
                - "Example: `app.example.com`"
            returned: on success
            type: str
            sample: hostname_example
    sample: [{
        "name": "name_example",
        "hostname": "hostname_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostnameFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_hostname,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            name=self.module.params.get("name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_hostnames,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


HostnameFactsHelperCustom = get_custom_class("HostnameFactsHelperCustom")


class ResourceFactsHelper(HostnameFactsHelperCustom, HostnameFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            name=dict(type="str"),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="hostname",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(hostnames=result)


if __name__ == "__main__":
    main()
