#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_object_storage_object_lifecycle_policy
short_description: Manage an ObjectLifecyclePolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete an ObjectLifecyclePolicy resource in Oracle Cloud Infrastructure
version_added: "2.5"
options:
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        required: true
    bucket_name:
        description:
            - "The name of the bucket. Avoid entering confidential information.
              Example: `my-new-bucket1`"
        required: true
    items:
        description:
            - The bucket's set of lifecycle policy rules.
        type: list
        suboptions:
            name:
                description:
                    - The name of the lifecycle rule to be applied.
                required: true
            action:
                description:
                    - The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects into the
                      L(Archive Storage tier,https://docs.cloud.oracle.com/Content/Archive/Concepts/archivestorageoverview.htm). Rules using the action
                      'DELETE' permanently delete objects from buckets. 'ARCHIVE' and 'DELETE' are the only two supported
                      actions at this time.
                required: true
            time_amount:
                description:
                    - Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the
                      timeUnit parameter, and is calculated in relation to each object's Last-Modified time.
                required: true
            time_unit:
                description:
                    - The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC.
                      Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.
                choices:
                    - "DAYS"
                    - "YEARS"
                required: true
            is_enabled:
                description:
                    - A boolean that determines whether this rule is currently enabled.
                type: bool
                required: true
            object_name_filter:
                description:
                    - A filter limiting object names that the rule will apply to.
                suboptions:
                    inclusion_prefixes:
                        description:
                            - An array of object name prefixes that the rule will apply to. An empty array means to include all objects.
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
    state:
        description:
            - The state of the ObjectLifecyclePolicy.
            - Use I(state=present) to update an existing an ObjectLifecyclePolicy.
            - Use I(state=absent) to delete an ObjectLifecyclePolicy.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Update object_lifecycle_policy from x-example
  oci_object_storage_object_lifecycle_policy:
      namespace_name: namespace_name_example
      bucket_name: my-new-bucket1
      items:
          - name: sampleRule
            action: ARCHIVE
            time_amount: 3
            time_unit: DAYS
            is_enabled: false
            object_name_filter:
                inclusion_prefixes: [ "samplePrefix" ]
                inclusion_patterns: [ "*.txt" ]
                exclusion_patterns: [ "*.pdf" ]

- name: Delete object_lifecycle_policy
  oci_object_storage_object_lifecycle_policy:
      namespace_name: namespace_name_example
      bucket_name: my-new-bucket1
      state: absent

"""

RETURN = """
object_lifecycle_policy:
    description:
        - Details of the ObjectLifecyclePolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        time_created:
            description:
                - The date and time the object lifecycle policy was created, as described in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
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
                action:
                    description:
                        - The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects into the
                          L(Archive Storage tier,https://docs.cloud.oracle.com/Content/Archive/Concepts/archivestorageoverview.htm). Rules using the action
                          'DELETE' permanently delete objects from buckets. 'ARCHIVE' and 'DELETE' are the only two supported
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
                        - A boolean that determines whether this rule is currently enabled.
                    returned: on success
                    type: bool
                    sample: true
                object_name_filter:
                    description:
                        - A filter limiting object names that the rule will apply to.
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
    sample: {
        "time_created": "2013-10-20T19:20:30+01:00",
        "items": [{
            "name": "name_example",
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient
    from oci.object_storage.models import PutObjectLifecyclePolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectLifecyclePolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "bucket_name"

    def get_module_resource_id(self):
        return self.module.params.get("bucket_name")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_object_lifecycle_policy,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
        )

    def get_update_model_class(self):
        return PutObjectLifecyclePolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.put_object_lifecycle_policy,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            put_object_lifecycle_policy_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_object_lifecycle_policy,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
        )


ObjectLifecyclePolicyHelperCustom = get_custom_class(
    "ObjectLifecyclePolicyHelperCustom"
)


class ResourceHelper(ObjectLifecyclePolicyHelperCustom, ObjectLifecyclePolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    action=dict(type="str", required=True),
                    time_amount=dict(type="int", required=True),
                    time_unit=dict(
                        type="str", required=True, choices=["DAYS", "YEARS"]
                    ),
                    is_enabled=dict(type="bool", required=True),
                    object_name_filter=dict(
                        type="dict",
                        options=dict(
                            inclusion_prefixes=dict(type="list"),
                            inclusion_patterns=dict(type="list"),
                            exclusion_patterns=dict(type="list"),
                        ),
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="object_lifecycle_policy",
        service_client_class=ObjectStorageClient,
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
