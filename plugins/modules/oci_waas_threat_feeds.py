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
module: oci_waas_threat_feeds
short_description: Manage a ThreatFeeds resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a ThreatFeeds resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    threat_feeds:
        description:
            - A list of threat feeds for which to update the actions.
        type: list
        required: true
        suboptions:
            key:
                description:
                    - The unique key of the object for which the action applies.
                    - This parameter is updatable.
                type: str
                required: true
            action:
                description:
                    - The selected action. If unspecified, defaults to `OFF`.
                    - This parameter is updatable.
                type: str
                choices:
                    - "OFF"
                    - "DETECT"
                    - "BLOCK"
                required: true
    state:
        description:
            - The state of the ThreatFeeds.
            - Use I(state=present) to update an existing a ThreatFeeds.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update threat_feeds
  oci_waas_threat_feeds:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx
    threat_feeds:
    - key: key_example
      action: OFF

"""

RETURN = """
threat_feeds:
    description:
        - Details of the ThreatFeeds resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key of the threat intelligence feed.
            returned: on success
            type: string
            sample: key_example
        name:
            description:
                - The name of the threat intelligence feed.
            returned: on success
            type: string
            sample: name_example
        action:
            description:
                - The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to `OFF`.
            returned: on success
            type: string
            sample: OFF
        description:
            description:
                - The description of the threat intelligence feed.
            returned: on success
            type: string
            sample: description_example
    sample: {
        "key": "key_example",
        "name": "name_example",
        "action": "OFF",
        "description": "description_example"
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
    from oci.waas.models import ThreatFeedAction

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ThreatFeedsHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

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
            self.client.list_threat_feeds, **kwargs
        )

    def get_update_model_class(self):
        return ThreatFeedAction

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_threat_feeds,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                threat_feeds=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ThreatFeedsHelperCustom = get_custom_class("ThreatFeedsHelperCustom")


class ResourceHelper(ThreatFeedsHelperCustom, ThreatFeedsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            threat_feeds=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str", required=True),
                    action=dict(
                        type="str", required=True, choices=["OFF", "DETECT", "BLOCK"]
                    ),
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
        resource_type="threat_feeds",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
