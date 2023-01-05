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
module: oci_log_analytics_storage_facts
short_description: Fetches details about a Storage resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Storage resource in Oracle Cloud Infrastructure
    - This API gets the storage configuration of a tenancy
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
- name: Get a specific storage
  oci_log_analytics_storage_facts:
    # required
    namespace_name: namespace_name_example

"""

RETURN = """
storage:
    description:
        - Storage resource
    returned: on success
    type: complex
    contains:
        is_archiving_enabled:
            description:
                - This indicates if old data can be archived for a tenancy
            returned: on success
            type: bool
            sample: true
        archiving_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                active_storage_duration:
                    description:
                        - This is the duration data in active storage before data is archived, as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations.
                          The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).
                    returned: on success
                    type: str
                    sample: active_storage_duration_example
                archival_storage_duration:
                    description:
                        - This is the duration before archived data is deleted from object storage, as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations
                          The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).
                    returned: on success
                    type: str
                    sample: archival_storage_duration_example
    sample: {
        "is_archiving_enabled": true,
        "archiving_configuration": {
            "active_storage_duration": "active_storage_duration_example",
            "archival_storage_duration": "archival_storage_duration_example"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StorageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_storage,
            namespace_name=self.module.params.get("namespace_name"),
        )


StorageFactsHelperCustom = get_custom_class("StorageFactsHelperCustom")


class ResourceFactsHelper(StorageFactsHelperCustom, StorageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(namespace_name=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="storage",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(storage=result)


if __name__ == "__main__":
    main()
