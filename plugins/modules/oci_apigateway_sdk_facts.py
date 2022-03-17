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
module: oci_apigateway_sdk_facts
short_description: Fetches details about one or multiple Sdk resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Sdk resources in Oracle Cloud Infrastructure
    - Returns list of generated SDKs.
    - If I(sdk_id) is specified, the details of a single Sdk will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sdk_id:
        description:
            - The ocid of the SDK.
            - Required to get a specific sdk.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
            - "Example: `ACTIVE` or `DELETED`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "DELETING"
            - "DELETED"
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
    api_id:
        description:
            - The ocid of the API.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sdk
  oci_apigateway_sdk_facts:
    # required
    sdk_id: "ocid1.sdk.oc1..xxxxxxEXAMPLExxxxxx"

- name: List sdks
  oci_apigateway_sdk_facts:

    # optional
    sdk_id: "ocid1.sdk.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated
    api_id: "ocid1.api.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
sdks:
    description:
        - List of Sdk resources
    returned: on success
    type: complex
    contains:
        api_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of API resource
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.api.oc1..xxxxxxEXAMPLExxxxxx"
        artifact_url:
            description:
                - File location for generated SDK.
                - Returned for get operation
            returned: on success
            type: str
            sample: artifact_url_example
        time_artifact_url_expires_at:
            description:
                - Expiry of artifact url.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a
                  resource in a Failed state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        parameters:
            description:
                - "Additional optional configurations passed.
                  The applicable config keys are listed under \\"parameters\\" when \\"/sdkLanguageTypes\\" is called."
                - "Example: `{\\"configName\\": \\"configValue\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: str
            sample: display_name_example
        target_language:
            description:
                - The string representing the target programming language for generating the SDK.
            returned: on success
            type: str
            sample: target_language_example
        lifecycle_state:
            description:
                - "The current state of the SDK.
                  - The SDK will be in CREATING state if the SDK creation is in progress.
                  - The SDK will be in ACTIVE state if create is successful.
                  - The SDK will be in FAILED state if the create, or delete fails.
                  - The SDK will be in DELETING state if the deletion in in progress.
                  - The SDK will be in DELETED state if the delete is successful."
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair
                  with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "api_id": "ocid1.api.oc1..xxxxxxEXAMPLExxxxxx",
        "artifact_url": "artifact_url_example",
        "time_artifact_url_expires_at": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "parameters": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "target_language": "target_language_example",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
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


class ApigatewaySdkFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "sdk_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sdk, sdk_id=self.module.params.get("sdk_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sdk_id",
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "api_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sdks, **optional_kwargs
        )


ApigatewaySdkFactsHelperCustom = get_custom_class("ApigatewaySdkFactsHelperCustom")


class ResourceFactsHelper(ApigatewaySdkFactsHelperCustom, ApigatewaySdkFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sdk_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            api_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sdk",
        service_client_class=ApiGatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sdks=result)


if __name__ == "__main__":
    main()
