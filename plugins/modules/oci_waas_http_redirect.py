#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_waas_http_redirect
short_description: Manage a HttpRedirect resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a HttpRedirect resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new HTTP Redirect on the WAF edge.
    - "This resource has the following action operations in the M(oracle.oci.oci_waas_http_redirect_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirects compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    domain:
        description:
            - The domain from which traffic will be redirected.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    target:
        description:
            - The redirect target object including all the redirect data.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            protocol:
                description:
                    - The protocol used for the target, http or https.
                type: str
                choices:
                    - "HTTP"
                    - "HTTPS"
                required: true
            host:
                description:
                    - The host portion of the redirect.
                type: str
                required: true
            port:
                description:
                    - Port number of the target destination of the redirect, default to match protocol
                type: int
            path:
                description:
                    - "The path component of the target URL (e.g., \\"/path/to/resource\\" in \\"https://target.example.com/path/to/resource?redirected\\"),
                      which can be empty, static, or request-copying, or request-prefixing. Use of \\\\ is not permitted except to escape a following \\\\, {,
                      or }. An empty value is treated the same as static \\"/\\". A static value must begin with a leading \\"/\\", optionally followed by other
                      path characters. A request-copying value must exactly match \\"{path}\\", and will be replaced with the path component of the request URL
                      (including its initial \\"/\\"). A request-prefixing value must start with \\"/\\" and end with a non-escaped \\"{path}\\", which will be
                      replaced with the path component of the request URL (including its initial \\"/\\"). Only one such replacement token is allowed."
                type: str
                required: true
            query:
                description:
                    - "The query component of the target URL (e.g., \\"?redirected\\" in \\"https://target.example.com/path/to/resource?redirected\\"), which
                      can be empty, static, or request-copying. Use of \\\\ is not permitted except to escape a following \\\\, {, or }. An empty value results
                      in a redirection target URL with no query component. A static value must begin with a leading \\"?\\", optionally followed by other query
                      characters. A request-copying value must exactly match \\"{query}\\", and will be replaced with the query component of the request URL
                      (including a leading \\"?\\" if and only if the request URL includes a query component)."
                type: str
                required: true
    response_code:
        description:
            - The response code returned for the redirect to the client. For more information, see L(RFC 7231,https://tools.ietf.org/html/rfc7231#section-6.4).
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    http_redirect_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the HTTP Redirect.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the HttpRedirect.
            - Use I(state=present) to create or update a HttpRedirect.
            - Use I(state=absent) to delete a HttpRedirect.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create http_redirect
  oci_waas_http_redirect:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    domain: domain_example
    target:
      # required
      protocol: HTTP
      host: host_example
      path: path_example
      query: query_example

      # optional
      port: 56

    # optional
    display_name: display_name_example
    response_code: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update http_redirect
  oci_waas_http_redirect:
    # required
    http_redirect_id: "ocid1.httpredirect.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    target:
      # required
      protocol: HTTP
      host: host_example
      path: path_example
      query: query_example

      # optional
      port: 56
    response_code: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update http_redirect using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_http_redirect:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    target:
      # required
      protocol: HTTP
      host: host_example
      path: path_example
      query: query_example

      # optional
      port: 56
    response_code: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete http_redirect
  oci_waas_http_redirect:
    # required
    http_redirect_id: "ocid1.httpredirect.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete http_redirect using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_http_redirect:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
        time_created:
            description:
                - The date and time the policy was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the HTTP Redirect.
            returned: on success
            type: str
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.waas import RedirectClient
    from oci.waas.models import CreateHttpRedirectDetails
    from oci.waas.models import UpdateHttpRedirectDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpRedirectHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(HttpRedirectHelperGen, self).get_possible_entity_types() + [
            "httpredirect",
            "httpredirects",
            "waashttpredirect",
            "waashttpredirects",
            "httpredirectresource",
            "httpredirectsresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "http_redirect_id"

    def get_module_resource_id(self):
        return self.module.params.get("http_redirect_id")

    def get_get_fn(self):
        return self.client.get_http_redirect

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_http_redirect, http_redirect_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_http_redirect,
            http_redirect_id=self.module.params.get("http_redirect_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
            self.client.list_http_redirects, **kwargs
        )

    def get_create_model_class(self):
        return CreateHttpRedirectDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_http_redirect,
            call_fn_args=(),
            call_fn_kwargs=dict(create_http_redirect_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateHttpRedirectDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_http_redirect,
            call_fn_args=(),
            call_fn_kwargs=dict(
                http_redirect_id=self.module.params.get("http_redirect_id"),
                update_http_redirect_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_http_redirect,
            call_fn_args=(),
            call_fn_kwargs=dict(
                http_redirect_id=self.module.params.get("http_redirect_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


HttpRedirectHelperCustom = get_custom_class("HttpRedirectHelperCustom")


class ResourceHelper(HttpRedirectHelperCustom, HttpRedirectHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            target=dict(
                type="dict",
                options=dict(
                    protocol=dict(type="str", required=True, choices=["HTTP", "HTTPS"]),
                    host=dict(type="str", required=True),
                    port=dict(type="int"),
                    path=dict(type="str", required=True),
                    query=dict(type="str", required=True),
                ),
            ),
            response_code=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            http_redirect_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="http_redirect",
        service_client_class=RedirectClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
