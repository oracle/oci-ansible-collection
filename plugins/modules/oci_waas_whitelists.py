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
module: oci_waas_whitelists
short_description: Manage a Whitelists resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Whitelists resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    whitelists:
        description:
            - ""
        type: list
        elements: dict
        required: true
        suboptions:
            name:
                description:
                    - The unique name of the whitelist.
                    - This parameter is updatable.
                type: str
                required: true
            addresses:
                description:
                    - A set of IP addresses or CIDR notations to include in the whitelist.
                    - This parameter is updatable.
                type: list
                elements: str
            address_lists:
                description:
                    - A list of L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of IP address lists to include in the whitelist.
                    - This parameter is updatable.
                type: list
                elements: str
    state:
        description:
            - The state of the Whitelists.
            - Use I(state=present) to update an existing a Whitelists.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update whitelists
  oci_waas_whitelists:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    whitelists:
    - # required
      name: name_example

      # optional
      addresses: [ "addresses_example" ]
      address_lists: [ "address_lists_example" ]

"""

RETURN = """
whitelists:
    description:
        - Details of the Whitelists resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name of the whitelist.
            returned: on success
            type: str
            sample: name_example
        addresses:
            description:
                - A set of IP addresses or CIDR notations to include in the whitelist.
            returned: on success
            type: list
            sample: []
        address_lists:
            description:
                - A list of L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of IP address lists to include in the whitelist.
            returned: on success
            type: list
            sample: []
    sample: {
        "name": "name_example",
        "addresses": [],
        "address_lists": []
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
    from oci.waas import WaasClient
    from oci.waas.models import Whitelist

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WhitelistsHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

    def get_possible_entity_types(self):
        return super(WhitelistsHelperGen, self).get_possible_entity_types() + [
            "whitelists",
            "whitelist",
            "waaswhitelists",
            "waaswhitelist",
            "whitelistsresource",
            "whitelistresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "waas_policy_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_whitelists, **kwargs
        )

    def get_update_model_class(self):
        return Whitelist

    def get_update_model(self):
        if self.module.params.get("whitelists"):
            return [
                oci_common_utils.convert_input_data_to_model_class(
                    resource, self.get_update_model_class()
                )
                for resource in self.module.params["whitelists"]
            ]
        return []

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_whitelists,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                whitelists=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WhitelistsHelperCustom = get_custom_class("WhitelistsHelperCustom")


class ResourceHelper(WhitelistsHelperCustom, WhitelistsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            whitelists=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    name=dict(type="str", required=True),
                    addresses=dict(type="list", elements="str"),
                    address_lists=dict(type="list", elements="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="whitelists",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
