#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_network_service_facts
short_description: Fetches details about one or multiple Service resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Service resources in Oracle Cloud Infrastructure
    - Lists the available L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/) objects that you can enable for a
      service gateway in this region.
    - If I(service_id) is specified, the details of a single Service will be returned.
version_added: "2.5"
options:
    service_id:
        description:
            - The service's L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific service.
        type: str
        aliases: ["id"]
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List services
  oci_network_service_facts:

- name: Get a specific service
  oci_network_service_facts:
    service_id: ocid1.service.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
services:
    description:
        - List of Service resources
    returned: on success
    type: complex
    contains:
        cidr_block:
            description:
                - "A string that represents the regional public IP address ranges for the Oracle service or
                  services covered by this `Service` object. Also known as the `Service` object's *service
                  CIDR label*."
                - When you set up a route rule to route traffic to the service gateway, use this value as the
                  rule's destination. See L(Route Table,https://docs.cloud.oracle.com/#/en/iaas/20160918/RouteTable/). Also, when you set up
                  a security list rule to cover traffic with the service gateway, use the `cidrBlock` value
                  as the rule's destination (for an egress rule) or the source (for an ingress rule).
                  See L(Security List,https://docs.cloud.oracle.com/#/en/iaas/20160918/SecurityList/).
                - "Example: `oci-phx-objectstorage`"
            returned: on success
            type: string
            sample: oci-phx-objectstorage
        description:
            description:
                - Description of the Oracle service or services covered by this `Service` object.
                - "Example: `OCI PHX Object Storage`"
            returned: on success
            type: string
            sample: OCI PHX Object Storage
        id:
            description:
                - The `Service` object's L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - Name of the `Service` object. This name can change and is not guaranteed to be unique.
                - "Example: `OCI PHX Object Storage`"
            returned: on success
            type: string
            sample: OCI PHX Object Storage
    sample: [{
        "cidr_block": "oci-phx-objectstorage",
        "description": "OCI PHX Object Storage",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "OCI PHX Object Storage"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "service_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service, service_id=self.module.params.get("service_id"),
        )

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
            self.client.list_services, **optional_kwargs
        )


ServiceFactsHelperCustom = get_custom_class("ServiceFactsHelperCustom")


class ResourceFactsHelper(ServiceFactsHelperCustom, ServiceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(service_id=dict(aliases=["id"], type="str"), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(services=result)


if __name__ == "__main__":
    main()
