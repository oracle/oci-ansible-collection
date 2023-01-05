#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_apigateway_sdk_language_type_facts
short_description: Fetches details about one or multiple SdkLanguageType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SdkLanguageType resources in Oracle Cloud Infrastructure
    - Lists programming languages in which SDK can be generated.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ocid of the compartment in which to list resources.
        type: str
        required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for `timeCreated` is descending. Default order for
              `displayName` is ascending. The `displayName` sort order is case
              sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List sdk_language_types
  oci_apigateway_sdk_language_type_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
sdk_language_types:
    description:
        - List of SdkLanguageType resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of the programming language.
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Display name of the target programming language.
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - Version string of the programming language defined in name.
            returned: on success
            type: str
            sample: version_example
        description:
            description:
                - Additional details.
            returned: on success
            type: str
            sample: description_example
        parameters:
            description:
                - List of optional configurations that can be used while generating SDK for the given target language.
            returned: on success
            type: complex
            contains:
                param_name:
                    description:
                        - Name of the parameter.
                    returned: on success
                    type: str
                    sample: param_name_example
                display_name:
                    description:
                        - Display name of the parameter.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description for the parameter.
                    returned: on success
                    type: str
                    sample: description_example
                is_required:
                    description:
                        - Information on whether the parameter is required or not.
                    returned: on success
                    type: bool
                    sample: true
                max_size:
                    description:
                        - Maximum size as input value for this parameter.
                    returned: on success
                    type: float
                    sample: 10
                input_type:
                    description:
                        - "The input type for this param.
                          - Input type is ENUM when only specific list of input strings are allowed.
                          - Input type is EMAIL when input type is an email ID.
                          - Input type is URI when input type is an URI.
                          - Input type is STRING in all other cases."
                    returned: on success
                    type: str
                    sample: ENUM
                allowed_values:
                    description:
                        - "List of allowed input values.
                          Example: `[{\\"name\\": \\"name1\\", \\"description\\": \\"description1\\"}, ...]`"
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the allowed value.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - Description for the allowed value.
                            returned: on success
                            type: str
                            sample: description_example
    sample: [{
        "name": "name_example",
        "display_name": "display_name_example",
        "version": "version_example",
        "description": "description_example",
        "parameters": [{
            "param_name": "param_name_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "is_required": true,
            "max_size": 10,
            "input_type": "ENUM",
            "allowed_values": [{
                "name": "name_example",
                "description": "description_example"
            }]
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import ApiGatewayClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewaySdkLanguageTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
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
            self.client.list_sdk_language_types,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApigatewaySdkLanguageTypeFactsHelperCustom = get_custom_class(
    "ApigatewaySdkLanguageTypeFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewaySdkLanguageTypeFactsHelperCustom, ApigatewaySdkLanguageTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            display_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sdk_language_type",
        service_client_class=ApiGatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sdk_language_types=result)


if __name__ == "__main__":
    main()
