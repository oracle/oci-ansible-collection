#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_dns_resolver_actions
short_description: Perform actions on a Resolver resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Resolver resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resolver into a different compartment along with its protected default view and any endpoints.
      Zones in the default view are not moved. Requires a `PRIVATE` scope query parameter.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resolver_id:
        description:
            - The OCID of the target resolver.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resolver, along with
              its protected default view and resolver endpoints, should be moved.
        type: str
        required: true
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    action:
        description:
            - The action to perform on the Resolver.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on resolver
  oci_dns_resolver_actions:
    resolver_id: "ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
resolver:
    description:
        - Details of the Resolver resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the owning compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        attached_vcn_id:
            description:
                - The OCID of the attached VCN.
            returned: on success
            type: str
            sample: "ocid1.attachedvcn.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the resolver.
            returned: on success
            type: str
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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        default_view_id:
            description:
                - The OCID of the default view.
            returned: on success
            type: str
            sample: "ocid1.defaultview.oc1..xxxxxxEXAMPLExxxxxx"
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
                    type: str
                    sample: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"
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
                        - "The action determines the behavior of the rule. If a query matches a supplied condition, the action will
                          apply. If there are no conditions on the rule, all queries are subject to the specified action.
                          * `FORWARD` - Matching requests will be forwarded from the source interface to the destination address."
                    returned: on success
                    type: str
                    sample: FORWARD
                destination_addresses:
                    description:
                        - IP addresses to which queries should be forwarded. Currently limited to a single address.
                    returned: on success
                    type: list
                    sample: []
                source_endpoint_name:
                    description:
                        - Case-insensitive name of an endpoint, that is a sub-resource of the resolver, to use as the forwarding
                          interface. The endpoint must have isForwarding set to true.
                    returned: on success
                    type: str
                    sample: source_endpoint_name_example
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient
    from oci.dns.models import ChangeResolverCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResolverActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "resolver_id"

    def get_module_resource_id(self):
        return self.module.params.get("resolver_id")

    def get_get_fn(self):
        return self.client.get_resolver

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver, resolver_id=self.module.params.get("resolver_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeResolverCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_resolver_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resolver_id=self.module.params.get("resolver_id"),
                change_resolver_compartment_details=action_details,
                scope=self.module.params.get("scope"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ResolverActionsHelperCustom = get_custom_class("ResolverActionsHelperCustom")


class ResourceHelper(ResolverActionsHelperCustom, ResolverActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            resolver_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="resolver",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
