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
module: oci_dns_resolver_facts
short_description: Fetches details about one or multiple Resolver resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Resolver resources in Oracle Cloud Infrastructure
    - Gets a list of all resolvers within a compartment. The collection can
      be filtered by display name, id, or lifecycle state. It can be sorted
      on creation time or displayName both in ASC or DESC order. Note that
      when no lifecycleState query parameter is provided that the collection
      does not include resolvers in the DELETED lifecycleState to be consistent
      with other operations of the API.
    - If I(resolver_id) is specified, the details of a single Resolver will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    resolver_id:
        description:
            - The OCID of the target resolver.
            - Required to get a specific resolver.
        type: str
        aliases: ["id"]
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - Required to list multiple resolvers.
        type: str
    display_name:
        description:
            - The displayName of a resource.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field by which to sort resolvers.
        type: str
        choices:
            - "displayName"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List resolvers
  oci_dns_resolver_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific resolver
  oci_dns_resolver_facts:
    resolver_id: ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
resolvers:
    description:
        - List of Resolver resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the owning compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        attached_vcn_id:
            description:
                - The OCID of the attached VCN.
            returned: on success
            type: string
            sample: ocid1.attachedvcn.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of the resolver.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        id:
            description:
                - The OCID of the resolver.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - "The date and time the resource was created in \\"YYYY-MM-ddThh:mm:ssZ\\" format
                  with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - "The date and time the resource was last updated in \\"YYYY-MM-ddThh:mm:ssZ\\"
                  format with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: string
            sample: ACTIVE
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: string
            sample: _self_example
        default_view_id:
            description:
                - The OCID of the default view.
            returned: on success
            type: string
            sample: ocid1.defaultview.oc1..xxxxxxEXAMPLExxxxxx
        is_protected:
            description:
                - A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.
            returned: on success
            type: bool
            sample: true
        endpoints:
            description:
                - Read-only array of endpoints for the resolver.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the resolver endpoint. Must be unique within the resolver.
                    returned: on success
                    type: string
                    sample: name_example
                endpoint_type:
                    description:
                        - The type of resolver endpoint. VNIC is currently the only supported type.
                    returned: on success
                    type: string
                    sample: VNIC
                forwarding_address:
                    description:
                        - An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
                          of the subnet and will be assigned by the system if unspecified when isForwarding is true.
                    returned: on success
                    type: string
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
                          subnet and will be assigned by the system if unspecified.
                    returned: on success
                    type: string
                    sample: listening_address_example
                compartment_id:
                    description:
                        - The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under
                          and will be updated if the resolver's compartment is changed.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                time_created:
                    description:
                        - "The date and time the resource was created in \\"YYYY-MM-ddThh:mm:ssZ\\" format
                          with a Z offset, as defined by RFC 3339."
                        - "**Example:** `2016-07-22T17:23:59:60Z`"
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - "The date and time the resource was last updated in \\"YYYY-MM-ddThh:mm:ssZ\\"
                          format with a Z offset, as defined by RFC 3339."
                        - "**Example:** `2016-07-22T17:23:59:60Z`"
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                lifecycle_state:
                    description:
                        - The current state of the resource.
                    returned: on success
                    type: string
                    sample: ACTIVE
                _self:
                    description:
                        - The canonical absolute URL of the resource.
                    returned: on success
                    type: string
                    sample: _self_example
                subnet_id:
                    description:
                        - The OCID of a subnet. Must be part of the VCN that the resolver is attached to.
                    returned: on success
                    type: string
                    sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        attached_views:
            description:
                - The attached views. Views are evaluated in order.
            returned: on success
            type: complex
            contains:
                view_id:
                    description:
                        - The OCID of the view.
                    returned: on success
                    type: string
                    sample: ocid1.view.oc1..xxxxxxEXAMPLExxxxxx
        rules:
            description:
                - Rules for the resolver. Rules are evaluated in order.
            returned: on success
            type: complex
            contains:
                client_address_conditions:
                    description:
                        - A list of CIDR blocks. The query must come from a client within one of the blocks in order for the rule action
                          to apply.
                    returned: on success
                    type: list
                    sample: []
                qname_cover_conditions:
                    description:
                        - A list of domain names. The query must be covered by one of the domains in order for the rule action to apply.
                    returned: on success
                    type: list
                    sample: []
                action:
                    description:
                        - "The action determines the behavior of the rule. If a query matches a supplied condition then the action will
                          apply. If there are no conditions on the rule then all queries are subject to the specified action.
                          * `FORWARD` - Matching requests will be forwarded from the source interface to the destination address."
                    returned: on success
                    type: string
                    sample: FORWARD
                destination_addresses:
                    description:
                        - IP addresses to which queries should be forwarded. Currently limited to a single address.
                    returned: on success
                    type: list
                    sample: []
                source_endpoint_name:
                    description:
                        - Name of an endpoint, that is a sub-resource of the resolver, to use as the forwarding interface. The
                          endpoint must have isForwarding set to true.
                    returned: on success
                    type: string
                    sample: source_endpoint_name_example
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "attached_vcn_id": "ocid1.attachedvcn.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "_self": "_self_example",
        "default_view_id": "ocid1.defaultview.oc1..xxxxxxEXAMPLExxxxxx",
        "is_protected": true,
        "endpoints": [{
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
        }],
        "attached_views": [{
            "view_id": "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "rules": [{
            "client_address_conditions": [],
            "qname_cover_conditions": [],
            "action": "FORWARD",
            "destination_addresses": [],
            "source_endpoint_name": "source_endpoint_name_example"
        }]
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


class ResolverFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "resolver_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
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
            self.client.get_resolver,
            resolver_id=self.module.params.get("resolver_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
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
            self.client.list_resolvers,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ResolverFactsHelperCustom = get_custom_class("ResolverFactsHelperCustom")


class ResourceFactsHelper(ResolverFactsHelperCustom, ResolverFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            resolver_id=dict(aliases=["id"], type="str"),
            if_modified_since=dict(type="str"),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
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
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resolver",
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

    module.exit_json(resolvers=result)


if __name__ == "__main__":
    main()
