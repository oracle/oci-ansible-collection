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
module: oci_waas_http_redirect_facts
short_description: Fetches details about one or multiple HttpRedirect resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HttpRedirect resources in Oracle Cloud Infrastructure
    - Gets a list of HTTP Redirects.
    - If I(http_redirect_id) is specified, the details of a single HttpRedirect will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    http_redirect_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect.
            - Required to get a specific http_redirect.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the
              compartment is created.
            - Required to list multiple http_redirects.
        type: str
    sort_order:
        description:
            - The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort the results of the List query.
        type: str
        choices:
            - "id"
            - "domain"
            - "target"
            - "displayName"
    display_name:
        description:
            - Filter redirects using a display name.
        type: list
        elements: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter redirects using a list of lifecycle states.
        type: list
        elements: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
    time_created_greater_than_or_equal_to:
        description:
            - A filter that matches redirects created on or after the specified date and time.
        type: str
    time_created_less_than:
        description:
            - A filter that matches redirects created before the specified date-time. Default to 1 day before now.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific http_redirect
  oci_waas_http_redirect_facts:
    # required
    http_redirect_id: "ocid1.httpredirect.oc1..xxxxxxEXAMPLExxxxxx"

- name: List http_redirects
  oci_waas_http_redirect_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: id
    display_name: [ "display_name_example" ]
    lifecycle_state: [ "CREATING" ]
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00

"""

RETURN = """
http_redirects:
    description:
        - List of HttpRedirect resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        domain:
            description:
                - The domain from which traffic will be redirected.
            returned: on success
            type: str
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
                    type: str
                    sample: HTTP
                host:
                    description:
                        - The host portion of the redirect.
                    returned: on success
                    type: str
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
                    type: str
                    sample: path_example
                query:
                    description:
                        - "The query component of the target URL (e.g., \\"?redirected\\" in \\"https://target.example.com/path/to/resource?redirected\\"),
                          which can be empty, static, or request-copying. Use of \\\\ is not permitted except to escape a following \\\\, {, or }. An empty
                          value results in a redirection target URL with no query component. A static value must begin with a leading \\"?\\", optionally
                          followed by other query characters. A request-copying value must exactly match \\"{query}\\", and will be replaced with the query
                          component of the request URL (including a leading \\"?\\" if and only if the request URL includes a query component)."
                    returned: on success
                    type: str
                    sample: query_example
        response_code:
            description:
                - The response code returned for the redirect to the client. For more information, see L(RFC
                  7231,https://tools.ietf.org/html/rfc7231#section-6.4).
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current lifecycle state of the HTTP Redirect.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the policy was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
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
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import RedirectClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpRedirectFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "http_redirect_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_http_redirect,
            http_redirect_id=self.module.params.get("http_redirect_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_http_redirects,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


HttpRedirectFactsHelperCustom = get_custom_class("HttpRedirectFactsHelperCustom")


class ResourceFactsHelper(HttpRedirectFactsHelperCustom, HttpRedirectFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            http_redirect_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "domain", "target", "displayName"]),
            display_name=dict(aliases=["name"], type="list", elements="str"),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                ],
            ),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="http_redirect",
        service_client_class=RedirectClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(http_redirects=result)


if __name__ == "__main__":
    main()
