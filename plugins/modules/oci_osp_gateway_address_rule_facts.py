#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_osp_gateway_address_rule_facts
short_description: Fetches details about a AddressRule resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AddressRule resource in Oracle Cloud Infrastructure
    - Get the address rule for the compartment based on the country code
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    osp_home_region:
        description:
            - The home region's public name of the logged in user.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    country_code:
        description:
            - Country code for the address rule in ISO-3166-1 2-letter format.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific address_rule
  oci_osp_gateway_address_rule_facts:
    # required
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    country_code: country_code_example

"""

RETURN = """
address_rule:
    description:
        - AddressRule resource
    returned: on success
    type: complex
    contains:
        country_code:
            description:
                - Country code for the address rule in ISO-3166-1 2-letter format
            returned: on success
            type: str
            sample: country_code_example
        address:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                third_party_validation:
                    description:
                        - Third party validation.
                    returned: on success
                    type: str
                    sample: OPTIONAL
                fields:
                    description:
                        - Address type rule fields
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The field name
                            returned: on success
                            type: str
                            sample: name_example
                        is_required:
                            description:
                                - The given field is requeired or not
                            returned: on success
                            type: bool
                            sample: true
                        format:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - Regex format specification
                                    returned: on success
                                    type: str
                                    sample: value_example
                                example:
                                    description:
                                        - Example of the desired format that matches the regex
                                    returned: on success
                                    type: str
                                    sample: example_example
                        label:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - Language token of the required label
                                    returned: on success
                                    type: str
                                    sample: value_example
                                example:
                                    description:
                                        - "English translation of the label (for reference only - translation is not provided)"
                                    returned: on success
                                    type: str
                                    sample: example_example
                        language:
                            description:
                                - "Locale code (rfc4646 format) of a forced language (e.g.: jp addresses require jp always)"
                            returned: on success
                            type: str
                            sample: language_example
        contact:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                fields:
                    description:
                        - Contact type rule fields
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The field name
                            returned: on success
                            type: str
                            sample: name_example
                        is_required:
                            description:
                                - The given field is requeired or not
                            returned: on success
                            type: bool
                            sample: true
                        format:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - Regex format specification
                                    returned: on success
                                    type: str
                                    sample: value_example
                                example:
                                    description:
                                        - Example of the desired format that matches the regex
                                    returned: on success
                                    type: str
                                    sample: example_example
                        label:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - Language token of the required label
                                    returned: on success
                                    type: str
                                    sample: value_example
                                example:
                                    description:
                                        - "English translation of the label (for reference only - translation is not provided)"
                                    returned: on success
                                    type: str
                                    sample: example_example
                        language:
                            description:
                                - "Locale code (rfc4646 format) of a forced language (e.g.: jp addresses require jp always)"
                            returned: on success
                            type: str
                            sample: language_example
        tax:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                fields:
                    description:
                        - Tax type rule fields
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The field name
                            returned: on success
                            type: str
                            sample: name_example
                        is_required:
                            description:
                                - The given field is requeired or not
                            returned: on success
                            type: bool
                            sample: true
                        format:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - Regex format specification
                                    returned: on success
                                    type: str
                                    sample: value_example
                                example:
                                    description:
                                        - Example of the desired format that matches the regex
                                    returned: on success
                                    type: str
                                    sample: example_example
                        label:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - Language token of the required label
                                    returned: on success
                                    type: str
                                    sample: value_example
                                example:
                                    description:
                                        - "English translation of the label (for reference only - translation is not provided)"
                                    returned: on success
                                    type: str
                                    sample: example_example
                        language:
                            description:
                                - "Locale code (rfc4646 format) of a forced language (e.g.: jp addresses require jp always)"
                            returned: on success
                            type: str
                            sample: language_example
    sample: {
        "country_code": "country_code_example",
        "address": {
            "third_party_validation": "OPTIONAL",
            "fields": [{
                "name": "name_example",
                "is_required": true,
                "format": {
                    "value": "value_example",
                    "example": "example_example"
                },
                "label": {
                    "value": "value_example",
                    "example": "example_example"
                },
                "language": "language_example"
            }]
        },
        "contact": {
            "fields": [{
                "name": "name_example",
                "is_required": true,
                "format": {
                    "value": "value_example",
                    "example": "example_example"
                },
                "label": {
                    "value": "value_example",
                    "example": "example_example"
                },
                "language": "language_example"
            }]
        },
        "tax": {
            "fields": [{
                "name": "name_example",
                "is_required": true,
                "format": {
                    "value": "value_example",
                    "example": "example_example"
                },
                "label": {
                    "value": "value_example",
                    "example": "example_example"
                },
                "language": "language_example"
            }]
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osp_gateway import AddressRuleServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddressRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "osp_home_region",
            "compartment_id",
            "country_code",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_address_rule,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            country_code=self.module.params.get("country_code"),
        )


AddressRuleFactsHelperCustom = get_custom_class("AddressRuleFactsHelperCustom")


class ResourceFactsHelper(AddressRuleFactsHelperCustom, AddressRuleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            country_code=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="address_rule",
        service_client_class=AddressRuleServiceClient,
        namespace="osp_gateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(address_rule=result)


if __name__ == "__main__":
    main()
