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
module: oci_audit_configuration_facts
short_description: Fetches details about a Configuration resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Configuration resource in Oracle Cloud Infrastructure
    - Get the configuration
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - ID of the root compartment (tenancy)
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific configuration
  oci_audit_configuration_facts:
    compartment_id: ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
configuration:
    description:
        - Configuration resource
    returned: on success
    type: complex
    contains:
        retention_period_days:
            description:
                - The retention period setting, specified in days. The minimum is 90, the maximum 365.
                - "Example: `90`"
            returned: on success
            type: int
            sample: 90
    sample: {
        "retention_period_days": 90
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.audit import AuditClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )


ConfigurationFactsHelperCustom = get_custom_class("ConfigurationFactsHelperCustom")


class ResourceFactsHelper(ConfigurationFactsHelperCustom, ConfigurationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="configuration",
        service_client_class=AuditClient,
        namespace="audit",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(configuration=result)


if __name__ == "__main__":
    main()
