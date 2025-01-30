#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_log_analytics_unprocessed_data_bucket_facts
short_description: Fetches details about a UnprocessedDataBucket resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a UnprocessedDataBucket resource in Oracle Cloud Infrastructure
    - This API retrieves details of the configured bucket that stores unprocessed payloads.
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
- name: Get a specific unprocessed_data_bucket
  oci_log_analytics_unprocessed_data_bucket_facts:
    # required
    namespace_name: namespace_name_example

"""

RETURN = """
unprocessed_data_bucket:
    description:
        - UnprocessedDataBucket resource
    returned: on success
    type: complex
    contains:
        namespace:
            description:
                - Object Storage namespace.
            returned: on success
            type: str
            sample: namespace_example
        bucket_name:
            description:
                - Name of the Object Storage bucket.
            returned: on success
            type: str
            sample: bucket_name_example
        is_enabled:
            description:
                - Flag that specifies if this configuration is enabled or not.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time when this record is created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The latest time when this record is updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "namespace": "namespace_example",
        "bucket_name": "bucket_name_example",
        "is_enabled": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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


class UnprocessedDataBucketFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_unprocessed_data_bucket,
            namespace_name=self.module.params.get("namespace_name"),
        )


UnprocessedDataBucketFactsHelperCustom = get_custom_class(
    "UnprocessedDataBucketFactsHelperCustom"
)


class ResourceFactsHelper(
    UnprocessedDataBucketFactsHelperCustom, UnprocessedDataBucketFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(namespace_name=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="unprocessed_data_bucket",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(unprocessed_data_bucket=result)


if __name__ == "__main__":
    main()
