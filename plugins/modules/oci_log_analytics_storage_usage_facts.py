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
module: oci_log_analytics_storage_usage_facts
short_description: Fetches details about a StorageUsage resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a StorageUsage resource in Oracle Cloud Infrastructure
    - This API gets storage usage information of a tenancy.  Storage usage information includes active, archived or recalled
      data.  The unit of return data is in bytes.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific storage_usage
  oci_log_analytics_storage_usage_facts:
    # required
    namespace_name: namespace_name_example

"""

RETURN = """
storage_usage:
    description:
        - StorageUsage resource
    returned: on success
    type: complex
    contains:
        active_data_size_in_bytes:
            description:
                - This is the number of bytes of active data (non-archived)
            returned: on success
            type: int
            sample: 56
        archived_data_size_in_bytes:
            description:
                - This is the number of bytes of archived data in object storage
            returned: on success
            type: int
            sample: 56
        recalled_archived_data_size_in_bytes:
            description:
                - This is the number of bytes of recalled data from archived in object store
            returned: on success
            type: int
            sample: 56
    sample: {
        "active_data_size_in_bytes": 56,
        "archived_data_size_in_bytes": 56,
        "recalled_archived_data_size_in_bytes": 56
    }
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


class StorageUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_storage_usage,
            namespace_name=self.module.params.get("namespace_name"),
        )


StorageUsageFactsHelperCustom = get_custom_class("StorageUsageFactsHelperCustom")


class ResourceFactsHelper(StorageUsageFactsHelperCustom, StorageUsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(namespace_name=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="storage_usage",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(storage_usage=result)


if __name__ == "__main__":
    main()
