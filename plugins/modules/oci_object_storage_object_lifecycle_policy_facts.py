#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_object_storage_object_lifecycle_policy_facts
short_description: Fetches details about one or multiple ObjectLifecyclePolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ObjectLifecyclePolicy resources in Oracle Cloud Infrastructure
    - Gets the object lifecycle policy for the bucket.
version_added: "2.9"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific object_lifecycle_policy
  oci_object_storage_object_lifecycle_policy_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

"""

RETURN = """
object_lifecycle_policies:
    description:
        - List of ObjectLifecyclePolicy resources
    returned: on success
    type: complex
    contains:
        time_created:
            description:
                - The date and time the object lifecycle policy was created, as described in
                  L(RFC 3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        items:
            description:
                - The live lifecycle policy on the bucket.
                - For an example of this value, see the
                  L(PutObjectLifecyclePolicy API
                  documentation,https://docs.cloud.oracle.com/iaas/api/#/en/objectstorage/20160918/ObjectLifecyclePolicy/PutObjectLifecyclePolicy).
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the lifecycle rule to be applied.
                    returned: on success
                    type: string
                    sample: name_example
                target:
                    description:
                        - ""
                    returned: on success
                    type: string
                    sample: target_example
                action:
                    description:
                        - The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects into the
                          L(Archive Storage tier,https://docs.cloud.oracle.com/Content/Archive/Concepts/archivestorageoverview.htm). Rules using the action
                          'DELETE' permanently delete objects from buckets. Rules using 'ABORT' abort the uncommitted multipart-uploads
                          and permanently delete their parts from buckets. 'ARCHIVE', 'DELETE' and 'ABORT' are the only three supported
                          actions at this time.
                    returned: on success
                    type: string
                    sample: action_example
                time_amount:
                    description:
                        - Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the
                          timeUnit parameter, and is calculated in relation to each object's Last-Modified time.
                    returned: on success
                    type: int
                    sample: 56
                time_unit:
                    description:
                        - The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC.
                          Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.
                    returned: on success
                    type: string
                    sample: DAYS
                is_enabled:
                    description:
                        - A Boolean that determines whether this rule is currently enabled.
                    returned: on success
                    type: bool
                    sample: true
                object_name_filter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        inclusion_prefixes:
                            description:
                                - An array of object name prefixes that the rule will apply to. An empty array means to include all objects.
                            returned: on success
                            type: list
                            sample: []
                        inclusion_patterns:
                            description:
                                - An array of glob patterns to match the object names to include. An empty array includes all objects in the
                                  bucket. Exclusion patterns take precedence over inclusion patterns.
                                  A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other
                                  than the special pattern characters described below, matches itself.
                                      Glob patterns must be between 1 and 1024 characters.
                                - "   The special pattern characters have the following meanings:"
                                - "   \\\\           Escapes the following character
                                      *           Matches any string of characters.
                                      ?           Matches any single character .
                                      [...]       Matches a group of characters. A group of characters can be:
                                                      A set of characters, for example: [Zafg9@]. This matches any character in the brackets.
                                                      A range of characters, for example: [a-z]. This matches any character in the range.
                                                          [a-f] is equivalent to [abcdef].
                                                          For character ranges only the CHARACTER-CHARACTER pattern is supported.
                                                              [ab-yz] is not valid
                                                              [a-mn-z] is not valid
                                                          Character ranges can not start with ^ or :
                                                          To include a '-' in the range, make it the first or last character."
                            returned: on success
                            type: list
                            sample: []
                        exclusion_patterns:
                            description:
                                - An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion
                                  patterns take precedence over inclusion patterns.
                                  A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other
                                  than the special pattern characters described below, matches itself.
                                      Glob patterns must be between 1 and 1024 characters.
                                - "   The special pattern characters have the following meanings:"
                                - "   \\\\           Escapes the following character
                                      *           Matches any string of characters.
                                      ?           Matches any single character .
                                      [...]       Matches a group of characters. A group of characters can be:
                                                      A set of characters, for example: [Zafg9@]. This matches any character in the brackets.
                                                      A range of characters, for example: [a-z]. This matches any character in the range.
                                                          [a-f] is equivalent to [abcdef].
                                                          For character ranges only the CHARACTER-CHARACTER pattern is supported.
                                                              [ab-yz] is not valid
                                                              [a-mn-z] is not valid
                                                          Character ranges can not start with ^ or :
                                                          To include a '-' in the range, make it the first or last character."
                            returned: on success
                            type: list
                            sample: []
    sample: [{
        "time_created": "2013-10-20T19:20:30+01:00",
        "items": [{
            "name": "name_example",
            "target": "target_example",
            "action": "action_example",
            "time_amount": 56,
            "time_unit": "DAYS",
            "is_enabled": true,
            "object_name_filter": {
                "inclusion_prefixes": [],
                "inclusion_patterns": [],
                "exclusion_patterns": []
            }
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
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectLifecyclePolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_object_lifecycle_policy,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
        )


ObjectLifecyclePolicyFactsHelperCustom = get_custom_class(
    "ObjectLifecyclePolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    ObjectLifecyclePolicyFactsHelperCustom, ObjectLifecyclePolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="object_lifecycle_policy",
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

    module.exit_json(object_lifecycle_policies=result)


if __name__ == "__main__":
    main()
