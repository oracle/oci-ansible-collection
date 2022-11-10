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
module: oci_object_storage_retention_rule
short_description: Manage a RetentionRule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RetentionRule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new retention rule in the specified bucket. The new rule will take effect typically within 30 seconds.
      Note that a maximum of 100 rules are supported on a bucket.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-specified name for the retention rule. Names can be helpful in identifying retention rules.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    duration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            time_amount:
                description:
                    - The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation
                      to each object's Last-Modified timestamp.
                type: int
                required: true
            time_unit:
                description:
                    - The unit that should be used to interpret timeAmount.
                type: str
                choices:
                    - "YEARS"
                    - "DAYS"
                required: true
    time_rule_locked:
        description:
            - The date and time as per L(RFC 3339,https://tools.ietf.org/html/rfc3339) after which this rule is locked
              and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are
              allowed and no other properties can be changed. This property cannot be updated for rules that are in a
              locked state. Specifying it when a duration is not specified is considered an error.
            - This parameter is updatable.
        type: str
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
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RetentionRule.
            - Use I(state=present) to create or update a RetentionRule.
            - Use I(state=absent) to delete a RetentionRule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create retention_rule
  oci_object_storage_retention_rule:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example

    # optional
    display_name: display_name_example
    duration:
      # required
      time_amount: 56
      time_unit: YEARS
    time_rule_locked: time_rule_locked_example

- name: Update retention_rule
  oci_object_storage_retention_rule:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    retention_rule_id: "ocid1.retentionrule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    duration:
      # required
      time_amount: 56
      time_unit: YEARS
    time_rule_locked: time_rule_locked_example

- name: Update retention_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_object_storage_retention_rule:
    # required
    display_name: display_name_example
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example

    # optional
    duration:
      # required
      time_amount: 56
      time_unit: YEARS
    time_rule_locked: time_rule_locked_example

- name: Delete retention_rule
  oci_object_storage_retention_rule:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    retention_rule_id: "ocid1.retentionrule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete retention_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_object_storage_retention_rule:
    # required
    display_name: display_name_example
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    state: absent

"""

RETURN = """
retention_rule:
    description:
        - Details of the RetentionRule resource acted upon by the current operation
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
    sample: {
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.object_storage import ObjectStorageClient
    from oci.object_storage.models import CreateRetentionRuleDetails
    from oci.object_storage.models import UpdateRetentionRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RetentionRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RetentionRuleHelperGen, self).get_possible_entity_types() + [
            "retentionrule",
            "retentionrules",
            "objectStorageretentionrule",
            "objectStorageretentionrules",
            "retentionruleresource",
            "retentionrulesresource",
            "objectstorage",
        ]

    def get_module_resource_id_param(self):
        return "retention_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("retention_rule_id")

    def get_get_fn(self):
        return self.client.get_retention_rule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_retention_rule,
            retention_rule_id=summary_model.id,
            bucket_name=self.module.params.get("bucket_name"),
            namespace_name=self.module.params.get("namespace_name"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_retention_rule,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            retention_rule_id=self.module.params.get("retention_rule_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "bucket_name",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_retention_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateRetentionRuleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_retention_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                create_retention_rule_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRetentionRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_retention_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                retention_rule_id=self.module.params.get("retention_rule_id"),
                update_retention_rule_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_retention_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                retention_rule_id=self.module.params.get("retention_rule_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RetentionRuleHelperCustom = get_custom_class("RetentionRuleHelperCustom")


class ResourceHelper(RetentionRuleHelperCustom, RetentionRuleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            duration=dict(
                type="dict",
                options=dict(
                    time_amount=dict(type="int", required=True),
                    time_unit=dict(
                        type="str", required=True, choices=["YEARS", "DAYS"]
                    ),
                ),
            ),
            time_rule_locked=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            retention_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="retention_rule",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
