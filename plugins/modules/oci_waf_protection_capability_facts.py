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
module: oci_waf_protection_capability_facts
short_description: Fetches details about one or multiple ProtectionCapability resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProtectionCapability resources in Oracle Cloud Infrastructure
    - Lists of protection capabilities filtered by query parameters.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
        type: str
        required: true
    key:
        description:
            - The unique key of protection capability to filter by.
        type: str
    is_latest_version:
        description:
            - A filter to return only resources that matches given isLatestVersion.
        type: list
        elements: bool
    type:
        description:
            - A filter to return only resources that matches given type.
        type: str
        choices:
            - "REQUEST_PROTECTION_CAPABILITY"
            - "RESPONSE_PROTECTION_CAPABILITY"
    group_tag:
        description:
            - A filter to return only resources that are accociated given group tag.
        type: list
        elements: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for key is descending.
              Default order for type is descending.
              Default order for displayName is ascending.
              If no value is specified key is default.
        type: str
        choices:
            - "key"
            - "type"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List protection_capabilities
  oci_waf_protection_capability_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    key: key_example
    is_latest_version: [ "true" ]
    type: REQUEST_PROTECTION_CAPABILITY
    group_tag: [ "group_tag_example" ]
    display_name: display_name_example
    sort_order: ASC
    sort_by: key

"""

RETURN = """
protection_capabilities:
    description:
        - List of ProtectionCapability resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique key of protection capability.
            returned: on success
            type: str
            sample: key_example
        display_name:
            description:
                - The display name of protection capability.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of protection capability.
            returned: on success
            type: str
            sample: description_example
        version:
            description:
                - The version of protection capability.
            returned: on success
            type: int
            sample: 56
        is_latest_version:
            description:
                - The field that shows if this is the latest version of protection capability.
            returned: on success
            type: bool
            sample: true
        group_tags:
            description:
                - "The list of unique names protection capability group tags that are associated with this capability.
                  Example: [\\"PCI\\", \\"Recommended\\"]"
            returned: on success
            type: list
            sample: []
        type:
            description:
                - The type of protection capability.
                - "* **REQUEST_PROTECTION_CAPABILITY** can only be used in `requestProtection` module of WebAppFirewallPolicy."
                - "* **RESPONSE_PROTECTION_CAPABILITY** can only be used in `responseProtection` module of WebAppFirewallPolicy."
            returned: on success
            type: str
            sample: REQUEST_PROTECTION_CAPABILITY
        collaborative_action_threshold:
            description:
                - The default collaborative action threshold for OCI-managed collaborative protection capability.
                  Collaborative protection capabilities are made of several simple, non-collaborative protection capabilities
                  (referred to as `contributing capabilities` later on) which have weights assigned to them. These weights can
                  be found in the `collaborativeWeights` array.
                  For incoming/outgoing HTTP messages, all contributing capabilities are executed and the sum of all triggered
                  contributing capabilities weights is calculated. Only if this sum is greater than or equal to
                  `collaborativeActionThreshold` is the incoming/outgoing HTTP message marked as malicious.
                - This field is ignored for non-collaborative capabilities.
            returned: on success
            type: int
            sample: 56
        collaborative_weights:
            description:
                - The weights of contributing capabilities.
                  Defines how much each contributing capability contributes towards the action threshold of a collaborative protection capability.
                - This field is ignored for non-collaborative capabilities.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique key of contributing protection capability.
                    returned: on success
                    type: str
                    sample: key_example
                display_name:
                    description:
                        - The display name of contributing protection capability.
                    returned: on success
                    type: str
                    sample: display_name_example
                weight:
                    description:
                        - The weight of contributing protection capability.
                    returned: on success
                    type: int
                    sample: 56
    sample: [{
        "key": "key_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "version": 56,
        "is_latest_version": true,
        "group_tags": [],
        "type": "REQUEST_PROTECTION_CAPABILITY",
        "collaborative_action_threshold": 56,
        "collaborative_weights": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "weight": 56
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
    from oci.waf import WafClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionCapabilityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "key",
            "is_latest_version",
            "type",
            "group_tag",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_protection_capabilities,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProtectionCapabilityFactsHelperCustom = get_custom_class(
    "ProtectionCapabilityFactsHelperCustom"
)


class ResourceFactsHelper(
    ProtectionCapabilityFactsHelperCustom, ProtectionCapabilityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            key=dict(type="str", no_log=True),
            is_latest_version=dict(type="list", elements="bool"),
            type=dict(
                type="str",
                choices=[
                    "REQUEST_PROTECTION_CAPABILITY",
                    "RESPONSE_PROTECTION_CAPABILITY",
                ],
            ),
            group_tag=dict(type="list", elements="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["key", "type", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protection_capability",
        service_client_class=WafClient,
        namespace="waf",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(protection_capabilities=result)


if __name__ == "__main__":
    main()
