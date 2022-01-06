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
module: oci_object_storage_bucket_actions
short_description: Perform actions on a Bucket resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Bucket resource in Oracle Cloud Infrastructure
    - For I(action=make_bucket_writable), stops replication to the destination bucket and removes the replication policy. When the replication
      policy was created, this destination bucket became read-only except for new and changed objects replicated
      automatically from the source bucket. MakeBucketWritable removes the replication policy. This bucket is no
      longer the target for replication and is now writable, allowing users to make changes to bucket contents.
    - For I(action=reencrypt), re-encrypts the unique data encryption key that encrypts each object written to the bucket by using the most recent
      version of the master encryption key assigned to the bucket. (All data encryption keys are encrypted by a master
      encryption key. Master encryption keys are assigned to buckets and managed by Oracle by default, but you can assign
      a key that you created and control through the Oracle Cloud Infrastructure Key Management service.) The kmsKeyId property
      of the bucket determines which master encryption key is assigned to the bucket. If you assigned a different Key Management
      master encryption key to the bucket, you can call this API to re-encrypt all data encryption keys with the newly
      assigned key. Similarly, you might want to re-encrypt all data encryption keys if the assigned key has been rotated to
      a new key version since objects were last added to the bucket. If you call this API and there is no kmsKeyId associated
      with the bucket, the call will fail.
      Calling this API starts a work request task to re-encrypt the data encryption key of all objects in the bucket. Only
      objects created before the time of the API call will be re-encrypted. The call can take a long time, depending on how many
      objects are in the bucket and how big they are. This API returns a work request ID that you can use to retrieve the status
      of the work request task.
      All the versions of objects will be re-encrypted whether versioning is enabled or suspended at the bucket.
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
    action:
        description:
            - The action to perform on the Bucket.
        type: str
        required: true
        choices:
            - "make_bucket_writable"
            - "reencrypt"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action make_bucket_writable on bucket
  oci_object_storage_bucket_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    action: make_bucket_writable

- name: Perform action reencrypt on bucket
  oci_object_storage_bucket_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    action: reencrypt

"""

RETURN = """
bucket:
    description:
        - Details of the Bucket resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        namespace:
            description:
                - The Object Storage namespace in which the bucket resides.
            returned: on success
            type: str
            sample: namespace_example
        name:
            description:
                - "The name of the bucket. Avoid entering confidential information.
                  Example: my-new-bucket1"
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The compartment ID in which the bucket is authorized.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        metadata:
            description:
                - Arbitrary string keys and values for user-defined metadata.
            returned: on success
            type: dict
            sample: {}
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the user who created the bucket.
            returned: on success
            type: str
            sample: created_by_example
        time_created:
            description:
                - The date and time the bucket was created, as described in L(RFC 2616,https://tools.ietf.org/html/rfc2616#section-14.29).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        etag:
            description:
                - The entity tag (ETag) for the bucket.
            returned: on success
            type: str
            sample: etag_example
        public_access_type:
            description:
                - The type of public access enabled on this bucket.
                  A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
                  bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
                  `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the
                  bucket, public access is allowed for the `GetObject` and `HeadObject` operations.
            returned: on success
            type: str
            sample: NoPublicAccess
        storage_tier:
            description:
                - The storage tier type assigned to the bucket. A bucket is set to `Standard` tier by default, which means
                  objects uploaded or copied to the bucket will be in the standard storage tier. When the `Archive` tier type
                  is set explicitly for a bucket, objects uploaded or copied to the bucket will be stored in archive storage.
                  The `storageTier` property is immutable after bucket is created.
            returned: on success
            type: str
            sample: Standard
        object_events_enabled:
            description:
                - Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is
                  set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information
                  about events, see L(Overview of Events,https://docs.cloud.oracle.com/Content/Events/Concepts/eventsoverview.htm).
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        kms_key_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a master encryption key used to call the Key Management
                  service to generate a data encryption key or to encrypt or decrypt a data encryption key.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        object_lifecycle_policy_etag:
            description:
                - The entity tag (ETag) for the live object lifecycle policy on the bucket.
            returned: on success
            type: str
            sample: object_lifecycle_policy_etag_example
        approximate_count:
            description:
                - The approximate number of objects in the bucket. Count statistics are reported periodically. You will see a
                  lag between what is displayed and the actual object count.
            returned: on success
            type: int
            sample: 56
        approximate_size:
            description:
                - The approximate total size in bytes of all objects in the bucket. Size statistics are reported periodically. You will
                  see a lag between what is displayed and the actual size of the bucket.
            returned: on success
            type: int
            sample: 56
        replication_enabled:
            description:
                - Whether or not this bucket is a replication source. By default, `replicationEnabled` is set to `false`. This will
                  be set to 'true' when you create a replication policy for the bucket.
            returned: on success
            type: bool
            sample: true
        is_read_only:
            description:
                - Whether or not this bucket is read only. By default, `isReadOnly` is set to `false`. This will
                  be set to 'true' when this bucket is configured as a destination in a replication policy.
            returned: on success
            type: bool
            sample: true
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the bucket.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        versioning:
            description:
                - The versioning status on the bucket. A bucket is created with versioning `Disabled` by default.
                  For versioning `Enabled`, objects are protected from overwrites and deletes, by maintaining their version history. When versioning is
                  `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted.
            returned: on success
            type: str
            sample: Enabled
        auto_tiering:
            description:
                - The auto tiering status on the bucket. A bucket is created with auto tiering `Disabled` by default.
                  For auto tiering `InfrequentAccess`, objects are transitioned automatically between the 'Standard'
                  and 'InfrequentAccess' tiers based on the access pattern of the objects.
            returned: on success
            type: str
            sample: Disabled
    sample: {
        "namespace": "namespace_example",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "metadata": {},
        "created_by": "created_by_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "public_access_type": "NoPublicAccess",
        "storage_tier": "Standard",
        "object_events_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "object_lifecycle_policy_etag": "object_lifecycle_policy_etag_example",
        "approximate_count": 56,
        "approximate_size": 56,
        "replication_enabled": true,
        "is_read_only": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "versioning": "Enabled",
        "auto_tiering": "Disabled"
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
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        make_bucket_writable
        reencrypt
    """

    @staticmethod
    def get_module_resource_id_param():
        return "bucket_name"

    def get_module_resource_id(self):
        return self.module.params.get("bucket_name")

    def get_get_fn(self):
        return self.client.get_bucket

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bucket,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
        )

    def make_bucket_writable(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.make_bucket_writable,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
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

    def reencrypt(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reencrypt_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BucketActionsHelperCustom = get_custom_class("BucketActionsHelperCustom")


class ResourceHelper(BucketActionsHelperCustom, BucketActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            action=dict(
                type="str", required=True, choices=["make_bucket_writable", "reencrypt"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bucket",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
