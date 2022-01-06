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
module: oci_log_analytics_unprocessed_data_bucket_actions
short_description: Perform actions on an UnprocessedDataBucket resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an UnprocessedDataBucket resource in Oracle Cloud Infrastructure
    - For I(action=set), this API configures a bucket to store unprocessed payloads.
      While processing there could be reasons a payload cannot be processed (mismatched structure, corrupted archive format, etc),
      if configured the payload would be uploaded to the bucket for verification.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    bucket_name:
        description:
            - Name of the Object Storage bucket.
        type: str
        required: true
    is_enabled:
        description:
            - The enabled flag used for filtering.  Only items with the specified enabled value
              will be returned.
        type: bool
    action:
        description:
            - The action to perform on the UnprocessedDataBucket.
        type: str
        required: true
        choices:
            - "set"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action set on unprocessed_data_bucket
  oci_log_analytics_unprocessed_data_bucket_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    action: set

    # optional
    is_enabled: true

"""

RETURN = """
unprocessed_data_bucket:
    description:
        - Details of the UnprocessedDataBucket resource acted upon by the current operation
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UnprocessedDataBucketActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        set
    """

    @staticmethod
    def get_module_resource_id_param():
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def get_get_fn(self):
        return self.client.get_unprocessed_data_bucket

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_unprocessed_data_bucket,
            namespace_name=self.module.params.get("namespace_name"),
        )

    def set(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.set_unprocessed_data_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                is_enabled=self.module.params.get("is_enabled"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


UnprocessedDataBucketActionsHelperCustom = get_custom_class(
    "UnprocessedDataBucketActionsHelperCustom"
)


class ResourceHelper(
    UnprocessedDataBucketActionsHelperCustom, UnprocessedDataBucketActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            is_enabled=dict(type="bool"),
            action=dict(type="str", required=True, choices=["set"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="unprocessed_data_bucket",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
