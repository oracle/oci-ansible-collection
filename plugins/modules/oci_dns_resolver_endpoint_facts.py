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
module: oci_dns_resolver_endpoint_facts
short_description: Fetches details about one or multiple ResolverEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResolverEndpoint resources in Oracle Cloud Infrastructure
    - Gets a list of all endpoints within a resolver. The collection can be filtered by name or lifecycle state.
      It can be sorted on creation time or name both in ASC or DESC order. Note that when no lifecycleState
      query parameter is provided, the collection does not include resolver endpoints in the DELETED
      lifecycle state to be consistent with other operations of the API.
    - If I(resolver_endpoint_name) is specified, the details of a single ResolverEndpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resolver_endpoint_name:
        description:
            - The name of the target resolver endpoint.
            - Required to get a specific resolver_endpoint.
        type: str
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    resolver_id:
        description:
            - The OCID of the target resolver.
        type: str
        required: true
    name:
        description:
            - The name of a resource.
        type: str
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field by which to sort resolver endpoints.
        type: str
        choices:
            - "name"
            - "timeCreated"
    lifecycle_state:
        description:
            - The state of a resource.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETED"
            - "DELETING"
            - "FAILED"
            - "UPDATING"
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
- name: Get a specific resolver_endpoint
  oci_dns_resolver_endpoint_facts:
    # required
    resolver_endpoint_name: resolver_endpoint_name_example
    resolver_id: "ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    if_modified_since: if_modified_since_example
    scope: GLOBAL

- name: List resolver_endpoints
  oci_dns_resolver_endpoint_facts:
    # required
    resolver_id: "ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: name
    lifecycle_state: ACTIVE
    scope: GLOBAL

"""

RETURN = """
resolver_endpoints:
    description:
        - List of ResolverEndpoint resources
    returned: on success
    type: complex
    contains:
        nsg_ids:
            description:
                - An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
                  resolver endpoint is a part of.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        name:
            description:
                - The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.
            returned: on success
            type: str
            sample: name_example
        endpoint_type:
            description:
                - The type of resolver endpoint. VNIC is currently the only supported type.
            returned: on success
            type: str
            sample: VNIC
        forwarding_address:
            description:
                - An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
                  of the subnet and will be assigned by the system if unspecified when isForwarding is true.
            returned: on success
            type: str
            sample: forwarding_address_example
        is_forwarding:
            description:
                - A Boolean flag indicating whether or not the resolver endpoint is for forwarding.
            returned: on success
            type: bool
            sample: true
        is_listening:
            description:
                - A Boolean flag indicating whether or not the resolver endpoint is for listening.
            returned: on success
            type: bool
            sample: true
        listening_address:
            description:
                - An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the
                  subnet and will be assigned by the system if unspecified when isListening is true.
            returned: on success
            type: str
            sample: listening_address_example
        compartment_id:
            description:
                - The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under
                  and will be updated if the resolver's compartment is changed.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created in \\"YYYY-MM-ddThh:mm:ssZ\\" format
                  with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was last updated in \\"YYYY-MM-ddThh:mm:ssZ\\"
                  format with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: str
            sample: ACTIVE
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: str
            sample: _self_example
        subnet_id:
            description:
                - The OCID of a subnet. Must be part of the VCN that the resolver is attached to.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "nsg_ids": [],
        "name": "name_example",
        "endpoint_type": "VNIC",
        "forwarding_address": "forwarding_address_example",
        "is_forwarding": true,
        "is_listening": true,
        "listening_address": "listening_address_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "_self": "_self_example",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResolverEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "resolver_id",
            "resolver_endpoint_name",
        ]

    def get_required_params_for_list(self):
        return [
            "resolver_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver_endpoint,
            resolver_id=self.module.params.get("resolver_id"),
            resolver_endpoint_name=self.module.params.get("resolver_endpoint_name"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_resolver_endpoints,
            resolver_id=self.module.params.get("resolver_id"),
            **optional_kwargs
        )


ResolverEndpointFactsHelperCustom = get_custom_class(
    "ResolverEndpointFactsHelperCustom"
)


class ResourceFactsHelper(
    ResolverEndpointFactsHelperCustom, ResolverEndpointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            resolver_endpoint_name=dict(type="str"),
            if_modified_since=dict(type="str"),
            resolver_id=dict(type="str", required=True),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name", "timeCreated"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "DELETED",
                    "DELETING",
                    "FAILED",
                    "UPDATING",
                ],
            ),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resolver_endpoint",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resolver_endpoints=result)


if __name__ == "__main__":
    main()
