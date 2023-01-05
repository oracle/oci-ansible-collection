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
module: oci_usage_configuration_facts
short_description: Fetches details about a Configuration resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Configuration resource in Oracle Cloud Infrastructure
    - Returns the configurations list for the UI drop-down list.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenant_id:
        description:
            - tenant id
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific configuration
  oci_usage_configuration_facts:
    # required
    tenant_id: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
configuration:
    description:
        - Configuration resource
    returned: on success
    type: complex
    contains:
        items:
            description:
                - The list of available configurations.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The configuration key.
                    returned: on success
                    type: str
                    sample: key_example
                values:
                    description:
                        - The configuration value.
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "items": [{
            "key": "key_example",
            "values": []
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.usage_api import UsageapiClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "tenant_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.request_summarized_configurations,
            tenant_id=self.module.params.get("tenant_id"),
        )


ConfigurationFactsHelperCustom = get_custom_class("ConfigurationFactsHelperCustom")


class ResourceFactsHelper(ConfigurationFactsHelperCustom, ConfigurationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(tenant_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="configuration",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(configuration=result)


if __name__ == "__main__":
    main()
