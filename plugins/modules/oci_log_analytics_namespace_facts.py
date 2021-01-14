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
module: oci_log_analytics_namespace_facts
short_description: Fetches details about one or multiple Namespace resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Namespace resources in Oracle Cloud Infrastructure
    - List Namespaces.
    - If I(namespace_name) is specified, the details of a single Namespace will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Log Analytics namespace used for the request.
            - Required to get a specific namespace.
        type: str
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple namespaces.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List namespaces
  oci_log_analytics_namespace_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific namespace
  oci_log_analytics_namespace_facts:
    namespace_name: namespace_name_example

"""

RETURN = """
namespaces:
    description:
        - List of Namespace resources
    returned: on success
    type: complex
    contains:
        namespace_name:
            description:
                - namespace name
            returned: on success
            type: string
            sample: namespace_name_example
        compartment_id:
            description:
                - Tenancy ID
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        is_onboarded:
            description:
                - if tenancy is onboarded to logging analytics
            returned: on success
            type: bool
            sample: true
    sample: [{
        "namespace_name": "namespace_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_onboarded": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace,
            namespace_name=self.module.params.get("namespace_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_namespaces,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NamespaceFactsHelperCustom = get_custom_class("NamespaceFactsHelperCustom")


class ResourceFactsHelper(NamespaceFactsHelperCustom, NamespaceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(namespace_name=dict(type="str"), compartment_id=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="namespace",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(namespaces=result)


if __name__ == "__main__":
    main()
