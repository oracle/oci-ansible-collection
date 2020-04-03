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
module: oci_object_storage_bucket
short_description: Manage a Bucket resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Bucket resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a bucket in the given namespace with a bucket name and optional user-defined metadata. Avoid entering
      confidential information in bucket names.
version_added: "2.5"
options:
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        type: str
        required: true
    name:
        description:
            - "The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, and dashes.
              Bucket names must be unique within an Object Storage namespace. Avoid entering confidential information.
              example: Example: my-new-bucket1"
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The ID of the compartment in which to create the bucket.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    metadata:
        description:
            - Arbitrary string, up to 4KB, of keys and values for user-defined metadata.
        type: dict
    public_access_type:
        description:
            - The type of public access enabled on this bucket.
              A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
              bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
              `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket,
              public access is allowed for the `GetObject` and `HeadObject` operations.
        type: str
        choices:
            - "NoPublicAccess"
            - "ObjectRead"
            - "ObjectReadWithoutList"
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
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    kms_key_id:
        description:
            - The OCID of a KMS key id used to call KMS to generate the data key or decrypt the encrypted data key.
        type: str
    bucket_name:
        description:
            - "The name of the bucket. Avoid entering confidential information.
              Example: `my-new-bucket1`"
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    state:
        description:
            - The state of the Bucket.
            - Use I(state=present) to create a Bucket.
            - Use I(state=absent) to delete a Bucket.
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
- name: Create bucket
  oci_object_storage_bucket:
    namespace_name: namespace_name_example
    name: my-test-1
    compartment_id: ocid.compartment.oc1..exampleuniquecompartmentID

- name: Delete bucket
  oci_object_storage_bucket:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    state: absent

- name: Delete bucket using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_object_storage_bucket:
    namespace_name: namespace_name_example
    name: my-test-1
    compartment_id: ocid.compartment.oc1..exampleuniquecompartmentID
    state: absent

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
                - The Object Storage namespace in which the bucket lives.
            returned: on success
            type: string
            sample: namespace_example
        name:
            description:
                - "The name of the bucket. Avoid entering confidential information.
                  Example: my-new-bucket1"
            returned: on success
            type: string
            sample: name_example
        compartment_id:
            description:
                - The compartment ID in which the bucket is authorized.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        metadata:
            description:
                - Arbitrary string keys and values for user-defined metadata.
            returned: on success
            type: dict
            sample: {}
        created_by:
            description:
                - The OCID of the user who created the bucket.
            returned: on success
            type: string
            sample: created_by_example
        time_created:
            description:
                - The date and time the bucket was created, as described in L(RFC 2616,https://tools.ietf.org/rfc/rfc2616), section 14.29.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        etag:
            description:
                - The entity tag (ETag) for the bucket.
            returned: on success
            type: string
            sample: etag_example
        public_access_type:
            description:
                - The type of public access enabled on this bucket.
                  A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
                  bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
                  `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the
                  bucket, public access is allowed for the `GetObject` and `HeadObject` operations.
            returned: on success
            type: string
            sample: NoPublicAccess
        storage_tier:
            description:
                - The storage tier type assigned to the bucket. A bucket is set to 'Standard' tier by default, which means
                  objects uploaded or copied to the bucket will be in the standard storage tier. When the 'Archive' tier type
                  is set explicitly for a bucket, objects uploaded or copied to the bucket will be stored in archive storage.
                  The 'storageTier' property is immutable after bucket is created.
            returned: on success
            type: string
            sample: Standard
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
                - The OCID of a KMS key id used to call KMS to generate data key or decrypt the encrypted data key.
            returned: on success
            type: string
            sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
        object_lifecycle_policy_etag:
            description:
                - The entity tag (ETag) for the live object lifecycle policy on the bucket.
            returned: on success
            type: string
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
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "object_lifecycle_policy_etag": "object_lifecycle_policy_etag_example",
        "approximate_count": 56,
        "approximate_size": 56
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
    from oci.object_storage.models import CreateBucketDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def list_resources(self):
        required_list_method_params = [
            "namespace_name",
            "compartment_id",
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

        return oci_common_utils.list_all_resources(self.client.list_buckets, **kwargs)

    def get_create_model_class(self):
        return CreateBucketDetails

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
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_terminated_states(),
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
            namespace_name=dict(type="str", required=True),
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            metadata=dict(type="dict"),
            public_access_type=dict(
                type="str",
                choices=["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"],
            ),
            storage_tier=dict(type="str", choices=["Standard", "Archive"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            kms_key_id=dict(type="str"),
            bucket_name=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
