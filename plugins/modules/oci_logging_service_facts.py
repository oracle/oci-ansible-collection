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
module: oci_logging_service_facts
short_description: Fetches details about one or multiple Service resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Service resources in Oracle Cloud Infrastructure
    - Lists all services that support logging.
version_added: "2.9"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List services
  oci_logging_service_facts:

"""

RETURN = """
services:
    description:
        - List of Service resources
    returned: on success
    type: complex
    contains:
        tenant_id:
            description:
                - Tenant OCID.
            returned: on success
            type: string
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - Apollo project namespace, if any.
            returned: on success
            type: string
            sample: namespace_example
        service_principal_name:
            description:
                - Service ID as set in Service Principal.
            returned: on success
            type: string
            sample: service_principal_name_example
        endpoint:
            description:
                - Service endpoint.
            returned: on success
            type: string
            sample: endpoint_example
        name:
            description:
                - User-friendly service name.
            returned: on success
            type: string
            sample: name_example
        id:
            description:
                - Service ID.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_types:
            description:
                - Type of resource that a service provides.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Resource type name.
                    returned: on success
                    type: string
                    sample: name_example
                categories:
                    description:
                        - Categories for resources.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Category name.
                            returned: on success
                            type: string
                            sample: name_example
                        display_name:
                            description:
                                - Category display name.
                            returned: on success
                            type: string
                            sample: display_name_example
                        parameters:
                            description:
                                - Parameters the category supports.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - Parameter name.
                                    returned: on success
                                    type: string
                                    sample: name_example
                                type:
                                    description:
                                        - Parameter type. One of integer, string, boolean.
                                    returned: on success
                                    type: string
                                    sample: integer
                                pattern:
                                    description:
                                        - Java regex pattern to validate a parameter value.
                                    returned: on success
                                    type: string
                                    sample: pattern_example
    sample: [{
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "service_principal_name": "service_principal_name_example",
        "endpoint": "endpoint_example",
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_types": [{
            "name": "name_example",
            "categories": [{
                "name": "name_example",
                "display_name": "display_name_example",
                "parameters": [{
                    "name": "name_example",
                    "type": "integer",
                    "pattern": "pattern_example"
                }]
            }]
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.logging import LoggingManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_services, **optional_kwargs
        )


ServiceFactsHelperCustom = get_custom_class("ServiceFactsHelperCustom")


class ResourceFactsHelper(ServiceFactsHelperCustom, ServiceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(name=dict(type="str"),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service",
        service_client_class=LoggingManagementClient,
        namespace="logging",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(services=result)


if __name__ == "__main__":
    main()
