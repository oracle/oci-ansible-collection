#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_dns_resolver_endpoint
short_description: Manage a ResolverEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ResolverEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new resolver endpoint. Requires a `PRIVATE` scope query parameter.
version_added: "2.9"
author: Oracle (@oracle)
options:
    resolver_id:
        description:
            - The OCID of the target resolver.
        type: str
        required: true
    name:
        description:
            - The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.
        type: str
        required: true
    endpoint_type:
        description:
            - The type of resolver endpoint. VNIC is currently the only supported type.
            - This parameter is updatable.
        type: str
        choices:
            - "VNIC"
        default: "VNIC"
    forwarding_address:
        description:
            - An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
              of the subnet and will be assigned by the system if unspecified when isForwarding is true.
        type: str
    is_forwarding:
        description:
            - A Boolean flag indicating whether or not the resolver endpoint is for forwarding.
            - Required for create using I(state=present).
        type: bool
    is_listening:
        description:
            - A Boolean flag indicating whether or not the resolver endpoint is for listening.
            - Required for create using I(state=present).
        type: bool
    listening_address:
        description:
            - An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the
              subnet and will be assigned by the system if unspecified when isListening is true.
        type: str
    subnet_id:
        description:
            - The OCID of a subnet. Must be part of the VCN that the resolver is attached to.
            - Required for create using I(state=present).
        type: str
    nsg_ids:
        description:
            - An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
              resolver endpoint is a part of.
            - This parameter is updatable.
        type: list
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
            - This parameter is updatable.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    if_unmodified_since:
        description:
            - The `If-Unmodified-Since` header field makes the request method
              conditional on the selected representation's last modification date being
              earlier than or equal to the date provided in the field-value.  This
              field accomplishes the same purpose as If-Match for cases where the user
              agent does not have an entity-tag for the representation.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the ResolverEndpoint.
            - Use I(state=present) to create or update a ResolverEndpoint.
            - Use I(state=absent) to delete a ResolverEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create resolver_endpoint
  oci_dns_resolver_endpoint:
    resolver_id: "ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    is_forwarding: true
    is_listening: true
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update resolver_endpoint
  oci_dns_resolver_endpoint:
    resolver_id: "ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

- name: Delete resolver_endpoint
  oci_dns_resolver_endpoint:
    resolver_id: "ocid1.resolver.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
resolver_endpoint:
    description:
        - Details of the ResolverEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.
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
                  subnet and will be assigned by the system if unspecified when isListening is true.
            returned: on success
            type: string
            sample: listening_address_example
        compartment_id:
            description:
                - The OCID of the owning compartment. This will match the resolver that the resolver endpoint is under
                  and will be updated if the resolver's compartment is changed.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
                  resolver endpoint is a part of.
            returned: on success
            type: list
            sample: []
    sample: {
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
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": []
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient
    from oci.dns.models import CreateResolverEndpointDetails
    from oci.dns.models import UpdateResolverEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResolverEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_resolver_endpoint

    def get_resource(self):
        optional_params = [
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver_endpoint,
            resolver_id=self.module.params.get("resolver_id"),
            resolver_endpoint_name=self.module.params.get("name"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "resolver_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "scope"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_resolver_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreateResolverEndpointDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        optional_enum_params = [
            "scope",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_resolver_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resolver_id=self.module.params.get("resolver_id"),
                create_resolver_endpoint_details=create_details,
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateResolverEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        optional_enum_params = [
            "scope",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_resolver_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resolver_id=self.module.params.get("resolver_id"),
                resolver_endpoint_name=self.module.params.get("name"),
                update_resolver_endpoint_details=update_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        optional_enum_params = [
            "scope",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_resolver_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resolver_id=self.module.params.get("resolver_id"),
                resolver_endpoint_name=self.module.params.get("name"),
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ResolverEndpointHelperCustom = get_custom_class("ResolverEndpointHelperCustom")


class ResourceHelper(ResolverEndpointHelperCustom, ResolverEndpointHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            resolver_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            endpoint_type=dict(type="str", default="VNIC", choices=["VNIC"]),
            forwarding_address=dict(type="str"),
            is_forwarding=dict(type="bool"),
            is_listening=dict(type="bool"),
            listening_address=dict(type="str"),
            subnet_id=dict(type="str"),
            nsg_ids=dict(type="list"),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            if_unmodified_since=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="resolver_endpoint",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
