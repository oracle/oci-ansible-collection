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
module: oci_apigateway_api_validations_facts
short_description: Fetches details about a ApiValidations resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ApiValidations resource in Oracle Cloud Infrastructure
    - Gets the API validation results.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    api_id:
        description:
            - The ocid of the API.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific api_validations
  oci_apigateway_api_validations_facts:
    api_id: "ocid1.api.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
api_validations:
    description:
        - ApiValidations resource
    returned: on success
    type: complex
    contains:
        validations:
            description:
                - API validation results.
            returned: on success
            type: complex
            contains:
                details:
                    description:
                        - Details of validation.
                    returned: on success
                    type: complex
                    contains:
                        msg:
                            description:
                                - Description of the warning/error.
                            returned: on success
                            type: str
                            sample: msg_example
                        severity:
                            description:
                                - Severity of the issue.
                            returned: on success
                            type: str
                            sample: INFO
                        src:
                            description:
                                - Position of the issue in the specification file (line, column).
                            returned: on success
                            type: list
                            sample: []
                name:
                    description:
                        - Name of the validation.
                    returned: on success
                    type: str
                    sample: name_example
                result:
                    description:
                        - Result of the validation.
                    returned: on success
                    type: str
                    sample: ERROR
    sample: {
        "validations": [{
            "details": [{
                "msg": "msg_example",
                "severity": "INFO",
                "src": []
            }],
            "name": "name_example",
            "result": "ERROR"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apigateway import ApiGatewayClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayApiValidationsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "api_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_api_validations, api_id=self.module.params.get("api_id"),
        )


ApigatewayApiValidationsFactsHelperCustom = get_custom_class(
    "ApigatewayApiValidationsFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayApiValidationsFactsHelperCustom, ApigatewayApiValidationsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(api_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="api_validations",
        service_client_class=ApiGatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(api_validations=result)


if __name__ == "__main__":
    main()
