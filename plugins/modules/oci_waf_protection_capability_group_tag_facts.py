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
module: oci_waf_protection_capability_group_tag_facts
short_description: Fetches details about one or multiple ProtectionCapabilityGroupTag resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProtectionCapabilityGroupTag resources in Oracle Cloud Infrastructure
    - Lists of available group tags filtered by query parameters.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
        type: str
        required: true
    type:
        description:
            - A filter to return only resources that matches given type.
        type: str
        choices:
            - "REQUEST_PROTECTION_CAPABILITY"
            - "RESPONSE_PROTECTION_CAPABILITY"
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
              Default order for name is ascending.
              If no value is specified name is default.
        type: str
        choices:
            - "name"
    name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List protection_capability_group_tags
  oci_waf_protection_capability_group_tag_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    type: REQUEST_PROTECTION_CAPABILITY
    sort_order: ASC
    sort_by: name
    name: name_example

"""

RETURN = """
protection_capability_group_tags:
    description:
        - List of ProtectionCapabilityGroupTag resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Unique name of protection capability group tag.
            returned: on success
            type: str
            sample: name_example
    sample: [{
        "name": "name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waf import WafClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionCapabilityGroupTagFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "type",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_protection_capability_group_tags,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProtectionCapabilityGroupTagFactsHelperCustom = get_custom_class(
    "ProtectionCapabilityGroupTagFactsHelperCustom"
)


class ResourceFactsHelper(
    ProtectionCapabilityGroupTagFactsHelperCustom,
    ProtectionCapabilityGroupTagFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            type=dict(
                type="str",
                choices=[
                    "REQUEST_PROTECTION_CAPABILITY",
                    "RESPONSE_PROTECTION_CAPABILITY",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protection_capability_group_tag",
        service_client_class=WafClient,
        namespace="waf",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(protection_capability_group_tags=result)


if __name__ == "__main__":
    main()
