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
module: oci_object_storage_replication_policy
short_description: Manage a ReplicationPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a ReplicationPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a replication policy for the specified bucket.
version_added: "2.5"
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
    name:
        description:
            - The name of the policy.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    destination_region_name:
        description:
            - "The destination region to replicate to, for example \\"us-ashburn-1\\"."
            - Required for create using I(state=present).
        type: str
    destination_bucket_name:
        description:
            - The bucket to replicate to in the destination region. Replication policy creation does not automatically
              create a destination bucket. Create the destination bucket before creating the policy.
            - Required for create using I(state=present).
        type: str
    replication_id:
        description:
            - The ID of the replication policy.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ReplicationPolicy.
            - Use I(state=present) to create a ReplicationPolicy.
            - Use I(state=absent) to delete a ReplicationPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create replication_policy
  oci_object_storage_replication_policy:
    name: mypolicy
    destination_region_name: us-phoenix-1
    destination_bucket_name: backup
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

- name: Delete replication_policy
  oci_object_storage_replication_policy:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    replication_id: ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete replication_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_object_storage_replication_policy:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    name: mypolicy
    state: absent

"""

RETURN = """
replication_policy:
    description:
        - Details of the ReplicationPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The id of the replication policy.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name of the policy.
            returned: on success
            type: string
            sample: name_example
        destination_region_name:
            description:
                - "The destination region to replicate to, for example \\"us-ashburn-1\\"."
            returned: on success
            type: string
            sample: destination_region_name_example
        destination_bucket_name:
            description:
                - The bucket to replicate to in the destination region. Replication policy creation does not automatically
                  create a destination bucket. Create the destination bucket before creating the policy.
            returned: on success
            type: string
            sample: destination_bucket_name_example
        time_created:
            description:
                - The date when the replication policy was created as per L(RFC 3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_sync:
            description:
                - Changes made to the source bucket before this time has been replicated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        status:
            description:
                - The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue
                  described in the status message, the status will become ACTIVE.
            returned: on success
            type: string
            sample: ACTIVE
        status_message:
            description:
                - A human-readable description of the status.
            returned: on success
            type: string
            sample: status_message_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "destination_region_name": "destination_region_name_example",
        "destination_bucket_name": "destination_bucket_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_sync": "2013-10-20T19:20:30+01:00",
        "status": "ACTIVE",
        "status_message": "status_message_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient
    from oci.object_storage.models import CreateReplicationPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "replication_id"

    def get_module_resource_id(self):
        return self.module.params.get("replication_id")

    def get_get_fn(self):
        return self.client.get_replication_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_policy,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            replication_id=self.module.params.get("replication_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "namespace_name",
            "bucket_name",
        ]

        optional_list_method_params = []

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_replication_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateReplicationPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_replication_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                create_replication_policy_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_replication_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                replication_id=self.module.params.get("replication_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_terminated_states(),
        )


ReplicationPolicyHelperCustom = get_custom_class("ReplicationPolicyHelperCustom")


class ResourceHelper(ReplicationPolicyHelperCustom, ReplicationPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            name=dict(type="str"),
            destination_region_name=dict(type="str"),
            destination_bucket_name=dict(type="str"),
            replication_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="replication_policy",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
