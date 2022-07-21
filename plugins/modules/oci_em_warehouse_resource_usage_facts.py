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
module: oci_em_warehouse_resource_usage_facts
short_description: Fetches details about a ResourceUsage resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ResourceUsage resource in Oracle Cloud Infrastructure
    - Gets a EmWarehouseResourceUsage by identifier
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    em_warehouse_id:
        description:
            - unique EmWarehouse identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific resource_usage
  oci_em_warehouse_resource_usage_facts:
    # required
    em_warehouse_id: "ocid1.emwarehouse.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
resource_usage:
    description:
        - ResourceUsage resource
    returned: on success
    type: complex
    contains:
        operations_insights_warehouse_id:
            description:
                - operations Insights Warehouse Identifier
            returned: on success
            type: str
            sample: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        em_instance_count:
            description:
                - EmInstanceCount
            returned: on success
            type: int
            sample: 56
        targets_count:
            description:
                - EmInstance Target count
            returned: on success
            type: int
            sample: 56
        em_instances:
            description:
                - List of emInstances
            returned: on success
            type: complex
            contains:
                em_id:
                    description:
                        - operations Insights Warehouse Identifier
                    returned: on success
                    type: str
                    sample: "ocid1.em.oc1..xxxxxxEXAMPLExxxxxx"
                targets_count:
                    description:
                        - EmInstance Target count
                    returned: on success
                    type: int
                    sample: 56
                em_host:
                    description:
                        - emHost name
                    returned: on success
                    type: str
                    sample: em_host_example
    sample: {
        "operations_insights_warehouse_id": "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "em_instance_count": 56,
        "targets_count": 56,
        "em_instances": [{
            "em_id": "ocid1.em.oc1..xxxxxxEXAMPLExxxxxx",
            "targets_count": 56,
            "em_host": "em_host_example"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.em_warehouse import EmDataLakeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "em_warehouse_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_em_warehouse_resource_usage,
            em_warehouse_id=self.module.params.get("em_warehouse_id"),
        )


ResourceUsageFactsHelperCustom = get_custom_class("ResourceUsageFactsHelperCustom")


class ResourceFactsHelper(ResourceUsageFactsHelperCustom, ResourceUsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(em_warehouse_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_usage",
        service_client_class=EmDataLakeClient,
        namespace="em_warehouse",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_usage=result)


if __name__ == "__main__":
    main()
