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
module: oci_waas_http_redirect_actions
short_description: Perform actions on a HttpRedirect resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a HttpRedirect resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves HTTP Redirect into a different compartment. When provided, If-Match is checked against ETag values of the WAAS
      policy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    http_redirect_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the HttpRedirect.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on http_redirect
  oci_waas_http_redirect_actions:
    http_redirect_id: "ocid1.httpredirect.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
http_redirect:
    description:
        - Details of the HttpRedirect resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect's compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        domain:
            description:
                - The domain from which traffic will be redirected.
            returned: on success
            type: string
            sample: domain_example
        target:
            description:
                - The redirect target object including all the redirect data.
            returned: on success
            type: complex
            contains:
                protocol:
                    description:
                        - The protocol used for the target, http or https.
                    returned: on success
                    type: string
                    sample: HTTP
                host:
                    description:
                        - The host portion of the redirect.
                    returned: on success
                    type: string
                    sample: host_example
                port:
                    description:
                        - Port number of the target destination of the redirect, default to match protocol
                    returned: on success
                    type: int
                    sample: 56
                path:
                    description:
                        - "The path component of the target URL (e.g., \\"/path/to/resource\\" in \\"https://target.example.com/path/to/resource?redirected\\"),
                          which can be empty, static, or request-copying, or request-prefixing. Use of \\\\ is not permitted except to escape a following \\\\,
                          {, or }. An empty value is treated the same as static \\"/\\". A static value must begin with a leading \\"/\\", optionally followed
                          by other path characters. A request-copying value must exactly match \\"{path}\\", and will be replaced with the path component of the
                          request URL (including its initial \\"/\\"). A request-prefixing value must start with \\"/\\" and end with a non-escaped
                          \\"{path}\\", which will be replaced with the path component of the request URL (including its initial \\"/\\"). Only one such
                          replacement token is allowed."
                    returned: on success
                    type: string
                    sample: path_example
                query:
                    description:
                        - "The query component of the target URL (e.g., \\"?redirected\\" in \\"https://target.example.com/path/to/resource?redirected\\"),
                          which can be empty, static, or request-copying. Use of \\\\ is not permitted except to escape a following \\\\, {, or }. An empty
                          value results in a redirection target URL with no query component. A static value must begin with a leading \\"?\\", optionally
                          followed by other query characters. A request-copying value must exactly match \\"{query}\\", and will be replaced with the query
                          component of the request URL (including a leading \\"?\\" if and only if the request URL includes a query component)."
                    returned: on success
                    type: string
                    sample: query_example
        response_code:
            description:
                - The response code returned for the redirect to the client. For more information, see L(RFC
                  7231,https://tools.ietf.org/html/rfc7231#section-6.4).
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the policy was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        lifecycle_state:
            description:
                - The current lifecycle state of the HTTP Redirect.
            returned: on success
            type: string
            sample: CREATING
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "domain": "domain_example",
        "target": {
            "protocol": "HTTP",
            "host": "host_example",
            "port": 56,
            "path": "path_example",
            "query": "query_example"
        },
        "response_code": 56,
        "time_created": "2018-11-16T21:10:29Z",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import RedirectClient
    from oci.waas.models import ChangeHttpRedirectCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpRedirectActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "http_redirect_id"

    def get_module_resource_id(self):
        return self.module.params.get("http_redirect_id")

    def get_get_fn(self):
        return self.client.get_http_redirect

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_http_redirect,
            http_redirect_id=self.module.params.get("http_redirect_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeHttpRedirectCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_http_redirect_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                http_redirect_id=self.module.params.get("http_redirect_id"),
                change_http_redirect_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


HttpRedirectActionsHelperCustom = get_custom_class("HttpRedirectActionsHelperCustom")


class ResourceHelper(HttpRedirectActionsHelperCustom, HttpRedirectActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            http_redirect_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="http_redirect",
        service_client_class=RedirectClient,
        namespace="waas",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
