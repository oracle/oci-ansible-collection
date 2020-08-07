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
module: oci_network_internet_gateway
short_description: Manage an InternetGateway resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an InternetGateway resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new internet gateway for the specified VCN. For more information, see
      L(Access to the Internet,https://docs.cloud.oracle.com/Content/Network/Tasks/managingIGs.htm).
    - For the purposes of access control, you must provide the OCID of the compartment where you want the Internet
      Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or
      other Networking Service components. If you're not sure which compartment to use, put the Internet
      Gateway in the same compartment with the VCN. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It
      does not have to be unique, and you can change it. Avoid entering confidential information."
    - For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in
      the subnet's route table (for example, 0.0.0.0/0 > internet gateway). See
      L(UpdateRouteTable,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/RouteTable/UpdateRouteTable).
    - You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no
      traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later
      use L(UpdateInternetGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/InternetGateway/UpdateInternetGateway) to easily
      disable/enable
      the gateway without changing the route rule.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to contain the internet gateway.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    is_enabled:
        description:
            - Whether the gateway is enabled upon creation.
            - Required for create using I(state=present).
        type: bool
    vcn_id:
        description:
            - The OCID of the VCN the internet gateway is attached to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    ig_id:
        description:
            - The OCID of the internet gateway.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the InternetGateway.
            - Use I(state=present) to create or update an InternetGateway.
            - Use I(state=absent) to delete an InternetGateway.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create internet_gateway
  oci_network_internet_gateway:
    display_name: MyInternetGateway
    compartment_id: ocid1.compartment.oc1..aaaaaaaayzfqeibduyox6iib3olcmdar3ugly4fmameq4h7lcdlihrvur7xq
    vcn_id: ocid1.vcn.oc1.phx.aaaaaaaamzvcg26irmlpkcmdzs33fb43lv2ej4lxshrdgpzvxsmb7zn427ma
    is_enabled: true

- name: Update internet_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_internet_gateway:
    compartment_id: ocid1.compartment.oc1..aaaaaaaayzfqeibduyox6iib3olcmdar3ugly4fmameq4h7lcdlihrvur7xq
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyInternetGateway
    freeform_tags: {'Department': 'Finance'}
    is_enabled: true
    vcn_id: ocid1.vcn.oc1.phx.aaaaaaaamzvcg26irmlpkcmdzs33fb43lv2ej4lxshrdgpzvxsmb7zn427ma

- name: Update internet_gateway
  oci_network_internet_gateway:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyInternetGateway
    ig_id: ocid1.ig.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete internet_gateway
  oci_network_internet_gateway:
    ig_id: ocid1.ig.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete internet_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_internet_gateway:
    compartment_id: ocid1.compartment.oc1..aaaaaaaayzfqeibduyox6iib3olcmdar3ugly4fmameq4h7lcdlihrvur7xq
    display_name: MyInternetGateway
    vcn_id: ocid1.vcn.oc1.phx.aaaaaaaamzvcg26irmlpkcmdzs33fb43lv2ej4lxshrdgpzvxsmb7zn427ma
    state: absent

"""

RETURN = """
internet_gateway:
    description:
        - Details of the InternetGateway resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the internet gateway.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The internet gateway's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        is_enabled:
            description:
                - Whether the gateway is enabled. When the gateway is disabled, traffic is not
                  routed to/from the Internet, regardless of route rules.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The internet gateway's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the internet gateway was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the internet gateway belongs to.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "lifecycle_state": "PROVISIONING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateInternetGatewayDetails
    from oci.core.models import UpdateInternetGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InternetGatewayHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "ig_id"

    def get_module_resource_id(self):
        return self.module.params.get("ig_id")

    def get_get_fn(self):
        return self.client.get_internet_gateway

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_internet_gateway, ig_id=self.module.params.get("ig_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "vcn_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_internet_gateways, **kwargs
        )

    def get_create_model_class(self):
        return CreateInternetGatewayDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_internet_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(create_internet_gateway_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateInternetGatewayDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_internet_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ig_id=self.module.params.get("ig_id"),
                update_internet_gateway_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_internet_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(ig_id=self.module.params.get("ig_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


InternetGatewayHelperCustom = get_custom_class("InternetGatewayHelperCustom")


class ResourceHelper(InternetGatewayHelperCustom, InternetGatewayHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            is_enabled=dict(type="bool"),
            vcn_id=dict(type="str"),
            ig_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="internet_gateway",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
