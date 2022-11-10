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
module: oci_waas_good_bots
short_description: Manage a GoodBots resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a GoodBots resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    good_bots:
        description:
            - ""
        type: list
        elements: dict
        required: true
        suboptions:
            key:
                description:
                    - The unique key for the bot.
                    - This parameter is updatable.
                type: str
                required: true
            name:
                description:
                    - The bot name.
                    - This parameter is updatable.
                type: str
            is_enabled:
                description:
                    - Enables or disables the bot.
                    - This parameter is updatable.
                type: bool
                required: true
            description:
                description:
                    - The description of the bot.
                    - This parameter is updatable.
                type: str
    state:
        description:
            - The state of the GoodBots.
            - Use I(state=present) to update an existing a GoodBots.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update good_bots
  oci_waas_good_bots:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    good_bots:
    - # required
      key: key_example
      is_enabled: true

      # optional
      name: name_example
      description: description_example

"""

RETURN = """
good_bots:
    description:
        - Details of the GoodBots resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key for the bot.
            returned: on success
            type: str
            sample: key_example
        name:
            description:
                - The bot name.
            returned: on success
            type: str
            sample: name_example
        is_enabled:
            description:
                - Enables or disables the bot.
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - The description of the bot.
            returned: on success
            type: str
            sample: description_example
    sample: {
        "key": "key_example",
        "name": "name_example",
        "is_enabled": true,
        "description": "description_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import GoodBot

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GoodBotsHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(GoodBotsHelperGen, self).get_possible_entity_types() + [
            "goodbots",
            "goodbot",
            "waasgoodbots",
            "waasgoodbot",
            "goodbotsresource",
            "goodbotresource",
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
        return oci_common_utils.list_all_resources(self.client.list_good_bots, **kwargs)

    def get_update_model_class(self):
        return GoodBot

    def get_update_model(self):
        if self.module.params.get("good_bots"):
            return [
                oci_common_utils.convert_input_data_to_model_class(
                    resource, self.get_update_model_class()
                )
                for resource in self.module.params["good_bots"]
            ]
        return []

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_good_bots,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                good_bots=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


GoodBotsHelperCustom = get_custom_class("GoodBotsHelperCustom")


class ResourceHelper(GoodBotsHelperCustom, GoodBotsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            good_bots=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    name=dict(type="str"),
                    is_enabled=dict(type="bool", required=True),
                    description=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="good_bots",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
