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
module: oci_functions_function_facts
short_description: Fetches details about one or multiple Function resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Function resources in Oracle Cloud Infrastructure
    - Lists functions for an application.
    - If I(function_id) is specified, the details of a single Function will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    function_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this function.
            - Required to get a specific function.
        type: str
        aliases: ["id"]
    application_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the application to which this function belongs.
            - Required to list multiple functions.
        type: str
    lifecycle_state:
        description:
            - "A filter to return only functions that match the lifecycle state in this parameter.
              Example: `Creating`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only functions with display names that match the display name string. Matching is exact.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - Specifies sort order.
            - "* **ASC:** Ascending sort order.
              * **DESC:** Descending sort order."
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the attribute with which to sort the rules.
            - "Default: `displayName`"
            - "* **timeCreated:** Sorts by timeCreated.
              * **displayName:** Sorts by displayName.
              * **id:** Sorts by id."
        type: str
        choices:
            - "timeCreated"
            - "id"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific function
  oci_functions_function_facts:
    # required
    function_id: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"

- name: List functions
  oci_functions_function_facts:
    # required
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
functions:
    description:
        - List of Function resources
    returned: on success
    type: complex
    contains:
        config:
            description:
                - Function configuration. Overrides application configuration.
                  Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values
                  should be limited to printable unicode characters.
                - "Example: `{\\"MY_FUNCTION_CONFIG\\": \\"ConfVal\\"}`"
                - The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each
                  key and value in UTF-8.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the function. The display name is unique within the application containing the function.
            returned: on success
            type: str
            sample: display_name_example
        application_id:
            description:
                - The OCID of the application the function belongs to.
            returned: on success
            type: str
            sample: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the function.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the function.
            returned: on success
            type: str
            sample: CREATING
        image:
            description:
                - "The qualified name of the Docker image to use in the function, including the image tag.
                  The image should be in the OCI Registry that is in the same region as the function itself.
                  Example: `phx.ocir.io/ten/functions/function:0.0.1`"
            returned: on success
            type: str
            sample: image_example
        image_digest:
            description:
                - "The image digest for the version of the image that will be pulled when invoking this function.
                  If no value is specified, the digest currently associated with the image in the OCI Registry will be used.
                  Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`"
            returned: on success
            type: str
            sample: image_digest_example
        memory_in_mbs:
            description:
                - Maximum usable memory for the function (MiB).
            returned: on success
            type: int
            sample: 56
        timeout_in_seconds:
            description:
                - Timeout for executions of the function. Value in seconds.
            returned: on success
            type: int
            sample: 56
        provisioned_concurrency_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                count:
                    description:
                        - ""
                    returned: on success
                    type: int
                    sample: 56
                strategy:
                    description:
                        - The strategy for provisioned concurrency to be used.
                    returned: on success
                    type: str
                    sample: CONSTANT
        trace_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Define if tracing is enabled for the resource.
                    returned: on success
                    type: bool
                    sample: true
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        invoke_endpoint:
            description:
                - The base https invoke URL to set on a client in order to invoke a function. This URL will never change over the lifetime of the function and
                  can be cached.
            returned: on success
            type: str
            sample: invoke_endpoint_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        time_created:
            description:
                - The time the function was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the function was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "config": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "application_id": "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "image": "image_example",
        "image_digest": "image_digest_example",
        "memory_in_mbs": 56,
        "timeout_in_seconds": 56,
        "provisioned_concurrency_config": {
            "count": 56,
            "strategy": "CONSTANT"
        },
        "trace_config": {
            "is_enabled": true
        },
        "freeform_tags": {'Department': 'Finance'},
        "invoke_endpoint": "invoke_endpoint_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.functions import FunctionsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FunctionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "function_id",
        ]

    def get_required_params_for_list(self):
        return [
            "application_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_function, function_id=self.module.params.get("function_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
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
            self.client.list_functions,
            application_id=self.module.params.get("application_id"),
            **optional_kwargs
        )


FunctionFactsHelperCustom = get_custom_class("FunctionFactsHelperCustom")


class ResourceFactsHelper(FunctionFactsHelperCustom, FunctionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            function_id=dict(aliases=["id"], type="str"),
            application_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "id", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="function",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(functions=result)


if __name__ == "__main__":
    main()
