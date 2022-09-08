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
module: oci_operator_access_control_interaction_facts
short_description: Fetches details about one or multiple Interaction resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Interaction resources in Oracle Cloud Infrastructure
    - Lists the MoreInformation interaction between customer and operators.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_request_id:
        description:
            - unique AccessRequest identifier
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List interactions
  oci_operator_access_control_interaction_facts:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
interactions:
    description:
        - List of Interaction resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The uniqueId of the message.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - customer or operator id who is part of this conversation.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        user_name:
            description:
                - customer or operator Name who is part of this conversation.
            returned: on success
            type: str
            sample: user_name_example
        message:
            description:
                - contains the information exchanged between operator and customer.
            returned: on success
            type: str
            sample: message_example
        user_type:
            description:
                - Whether the userConversation is an operator or customer.
            returned: on success
            type: str
            sample: user_type_example
        time_of_conversation:
            description:
                - "Time when the conversation happened in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format. Example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "user_name": "user_name_example",
        "message": "message_example",
        "user_type": "user_type_example",
        "time_of_conversation": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.operator_access_control import AccessRequestsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InteractionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "access_request_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_interactions,
            access_request_id=self.module.params.get("access_request_id"),
            **optional_kwargs
        )


InteractionFactsHelperCustom = get_custom_class("InteractionFactsHelperCustom")


class ResourceFactsHelper(InteractionFactsHelperCustom, InteractionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(access_request_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="interaction",
        service_client_class=AccessRequestsClient,
        namespace="operator_access_control",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(interactions=result)


if __name__ == "__main__":
    main()
