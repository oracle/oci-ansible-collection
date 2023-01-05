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
module: oci_object_storage_bucket
short_description: Manage a Bucket resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Bucket resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a bucket in the given namespace with a bucket name and optional user-defined metadata. Avoid entering
      confidential information in bucket names.
    - "This resource has the following action operations in the M(oracle.oci.oci_object_storage_bucket_actions) module: make_bucket_writable, reencrypt."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    storage_tier:
        description:
            - The type of storage tier of this bucket.
              A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier.
              When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier'
              property is immutable after bucket is created.
        type: str
        choices:
            - "Standard"
            - "Archive"
    compartment_id:
        description:
            - The ID of the compartment in which to create the bucket.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    metadata:
        description:
            - Arbitrary string, up to 4KB, of keys and values for user-defined metadata.
            - This parameter is updatable.
        type: dict
    public_access_type:
        description:
            - The type of public access enabled on this bucket.
              A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
              bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
              `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket,
              public access is allowed for the `GetObject` and `HeadObject` operations.
            - This parameter is updatable.
        type: str
        choices:
            - "NoPublicAccess"
            - "ObjectRead"
            - "ObjectReadWithoutList"
    object_events_enabled:
        description:
            - Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is
              set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information
              about events, see L(Overview of Events,https://docs.cloud.oracle.com/Content/Events/Concepts/eventsoverview.htm).
            - This parameter is updatable.
        type: bool
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    kms_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a master encryption key used to call the Key
              Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.
            - This parameter is updatable.
        type: str
    versioning:
        description:
            - Set the versioning status on the bucket. By default, a bucket is created with versioning `Disabled`. Use this option to enable versioning during
              bucket creation. Objects in a version enabled bucket are protected from overwrites and deletions. Previous versions of the same object will be
              available in the bucket.
            - This parameter is updatable.
        type: str
        choices:
            - "Enabled"
            - "Disabled"
            - "Suspended"
    auto_tiering:
        description:
            - Set the auto tiering status on the bucket. By default, a bucket is created with auto tiering `Disabled`.
              Use this option to enable auto tiering during bucket creation. Objects in a bucket with auto tiering set to
              `InfrequentAccess` are transitioned automatically between the 'Standard' and 'InfrequentAccess'
              tiers based on the access pattern of the objects.
            - This parameter is updatable.
        type: str
    force:
        description:
            - Force delete a bucket along with all the objects contained in it. Use with (state=absent).
        type: bool
        default: "false"
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        type: str
        required: true
    name:
        description:
            - "The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
              Bucket names must be unique within an Object Storage namespace. Avoid entering confidential information.
              example: Example: my-new-bucket1"
        type: str
        required: true
    state:
        description:
            - The state of the Bucket.
            - Use I(state=present) to create or update a Bucket.
            - Use I(state=absent) to delete a Bucket.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create bucket
  oci_object_storage_bucket:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example
    name: name_example

    # optional
    storage_tier: Standard
    metadata: null
    public_access_type: NoPublicAccess
    object_events_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    versioning: Enabled
    auto_tiering: auto_tiering_example

- name: Update bucket
  oci_object_storage_bucket:
    # required
    namespace_name: namespace_name_example
    name: name_example

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    metadata: null
    public_access_type: NoPublicAccess
    object_events_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    versioning: Enabled
    auto_tiering: auto_tiering_example

- name: Delete bucket
  oci_object_storage_bucket:
    # required
    namespace_name: namespace_name_example
    name: name_example
    state: absent

    # optional
    force: false

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
    from oci.object_storage.models import CreateBucketDetails
    from oci.object_storage.models import UpdateBucketDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BucketHelperGen, self).get_possible_entity_types() + [
            "bucket",
            "buckets",
            "objectStoragebucket",
            "objectStoragebuckets",
            "bucketresource",
            "bucketsresource",
            "b",
            "bs",
            "objectStorageb",
            "objectStoragebs",
            "bresource",
            "bsresource",
            "objectstorage",
        ]

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_bucket

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bucket,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "compartment_id",
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
        return oci_common_utils.list_all_resources(self.client.list_buckets, **kwargs)

    def get_create_model_class(self):
        return CreateBucketDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                create_bucket_details=create_details,
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
        return UpdateBucketDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("name"),
                update_bucket_details=update_details,
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
            call_fn=self.client.delete_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


BucketHelperCustom = get_custom_class("BucketHelperCustom")


class ResourceHelper(BucketHelperCustom, BucketHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            storage_tier=dict(type="str", choices=["Standard", "Archive"]),
            compartment_id=dict(type="str"),
            metadata=dict(type="dict"),
            public_access_type=dict(
                type="str",
                choices=["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"],
            ),
            object_events_enabled=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            kms_key_id=dict(type="str"),
            versioning=dict(type="str", choices=["Enabled", "Disabled", "Suspended"]),
            auto_tiering=dict(type="str"),
            force=dict(type="bool", default="false"),
            namespace_name=dict(type="str", required=True),
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bucket",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
