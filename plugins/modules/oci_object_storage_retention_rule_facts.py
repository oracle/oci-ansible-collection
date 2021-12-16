#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_object_storage_retention_rule_facts
short_description: Fetches details about one or multiple RetentionRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RetentionRule resources in Oracle Cloud Infrastructure
    - List the retention rules for a bucket. The retention rules are sorted based on creation time,
      with the most recently created retention rule returned first.
    - If I(retention_rule_id) is specified, the details of a single RetentionRule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        type: str
        required: true
    bucket_name:
        description:
            - "The name of the bucket. Avoid entering confidential information.
              Example: `my-new-bucket1`"
        type: str
        required: true
    retention_rule_id:
        description:
            - The ID of the retention rule.
            - Required to get a specific retention_rule.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific retention_rule
  oci_object_storage_retention_rule_facts:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    retention_rule_id: "ocid1.retentionrule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List retention_rules
  oci_object_storage_retention_rule_facts:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example

"""

RETURN = """
retention_rules:
    description:
        - List of RetentionRule resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier for the retention rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User specified name for the retention rule.
            returned: on success
            type: str
            sample: display_name_example
        duration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_amount:
                    description:
                        - The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation
                          to each object's Last-Modified timestamp.
                    returned: on success
                    type: int
                    sample: 56
                time_unit:
                    description:
                        - The unit that should be used to interpret timeAmount.
                    returned: on success
                    type: str
                    sample: YEARS
        etag:
            description:
                - The entity tag (ETag) for the retention rule.
            returned: on success
            type: str
            sample: etag_example
        time_rule_locked:
            description:
                - The date and time as per L(RFC 3339,https://tools.ietf.org/html/rfc3339) after which this rule becomes locked.
                  and can only be deleted by deleting the bucket.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time that the retention rule was created as per L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_modified:
            description:
                - The date and time that the retention rule was modified as per L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "duration": {
            "time_amount": 56,
            "time_unit": "YEARS"
        },
        "etag": "etag_example",
        "time_rule_locked": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_modified": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RetentionRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "bucket_name",
            "retention_rule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_retention_rule,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            retention_rule_id=self.module.params.get("retention_rule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_retention_rules,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )


RetentionRuleFactsHelperCustom = get_custom_class("RetentionRuleFactsHelperCustom")


class ResourceFactsHelper(RetentionRuleFactsHelperCustom, RetentionRuleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            retention_rule_id=dict(aliases=["id"], type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="retention_rule",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(retention_rules=result)


if __name__ == "__main__":
    main()
