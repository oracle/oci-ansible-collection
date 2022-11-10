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
module: oci_service_manager_proxy_service_environment_facts
short_description: Fetches details about one or multiple ServiceEnvironment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ServiceEnvironment resources in Oracle Cloud Infrastructure
    - List the details of Software as a Service (SaaS) environments provisioned by Service Manager.
      Information includes the service instance endpoints and service definition details.
    - If I(service_environment_id) is specified, the details of a single ServiceEnvironment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the compartment.
        type: str
        required: true
    service_environment_id:
        description:
            - The unique identifier associated with the service environment.
            - "**Note:** Not an L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)."
            - Required to get a specific service_environment.
        type: str
        aliases: ["id"]
    service_environment_type:
        description:
            - "The environment's service definition type.
              For example, \\"RGBUOROMS\\" is the service definition type for \\"Oracle Retail Order Management Cloud Service\\"."
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. ID is default ordered as ascending.
        type: str
        choices:
            - "ID"
    sort_order:
        description:
            - The sort order to use, either `ASC` or `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - The display name of the resource.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific service_environment
  oci_service_manager_proxy_service_environment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    service_environment_id: "ocid1.serviceenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List service_environments
  oci_service_manager_proxy_service_environment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    service_environment_id: "ocid1.serviceenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    service_environment_type: service_environment_type_example
    sort_by: ID
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
service_environments:
    description:
        - List of ServiceEnvironment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unqiue identifier for the entitlement related to the environment.
                - "**Note:** Not an L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)."
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_id:
            description:
                - The unique subscription ID associated with the service environment ID.
                - "**Note:** Not an L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)."
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - Status of the entitlement registration for the service.
            returned: on success
            type: str
            sample: INITIALIZED
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        service_definition:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - "The service definition type. For example, a service definition type \\"RGBUOROMS\\"
                          would be for the service \\"Oracle Retail Order Management Cloud Service\\"."
                    returned: on success
                    type: str
                    sample: type_example
                display_name:
                    description:
                        - "Display name of the service. For example, \\"Oracle Retail Order Management Cloud Service\\"."
                    returned: on success
                    type: str
                    sample: display_name_example
                short_display_name:
                    description:
                        - "Short display name of the service. For example, \\"Retail Order Management\\"."
                    returned: on success
                    type: str
                    sample: short_display_name_example
        console_url:
            description:
                - The URL for the console.
            returned: on success
            type: str
            sample: console_url_example
        service_environment_endpoints:
            description:
                - Array of service environment end points.
            returned: on success
            type: complex
            contains:
                environment_type:
                    description:
                        - Service environment endpoint type.
                    returned: on success
                    type: str
                    sample: INSTANCE_URL_PROD
                url:
                    description:
                        - Service environment instance URL.
                    returned: on success
                    type: str
                    sample: url_example
                description:
                    description:
                        - Description of the environment link
                    returned: on success
                    type: str
                    sample: description_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                - Returned for list operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"CostCenter\\": \\"42\\"}`"
                - Returned for list operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "INITIALIZED",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "service_definition": {
            "type": "type_example",
            "display_name": "display_name_example",
            "short_display_name": "short_display_name_example"
        },
        "console_url": "console_url_example",
        "service_environment_endpoints": [{
            "environment_type": "INSTANCE_URL_PROD",
            "url": "url_example",
            "description": "description_example"
        }],
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.service_manager_proxy import ServiceManagerProxyClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceEnvironmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "service_environment_id",
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_environment,
            service_environment_id=self.module.params.get("service_environment_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "service_environment_id",
            "service_environment_type",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_service_environments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ServiceEnvironmentFactsHelperCustom = get_custom_class(
    "ServiceEnvironmentFactsHelperCustom"
)


class ResourceFactsHelper(
    ServiceEnvironmentFactsHelperCustom, ServiceEnvironmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            service_environment_id=dict(aliases=["id"], type="str"),
            service_environment_type=dict(type="str"),
            sort_by=dict(type="str", choices=["ID"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service_environment",
        service_client_class=ServiceManagerProxyClient,
        namespace="service_manager_proxy",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(service_environments=result)


if __name__ == "__main__":
    main()
