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
module: oci_object_storage_bucket_actions
short_description: Perform actions on a Bucket resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Bucket resource in Oracle Cloud Infrastructure
    - For I(action=copy_object), creates a request to copy an object within a region or to another region.
    - For I(action=rename_object), rename an object in the given Object Storage namespace.
    - For I(action=restore_objects), restores one or more objects specified by the objectName parameter.
      By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.
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
    source_object_name:
        description:
            - The name of the object to be copied.
            - Required for I(action=copy_object).
    source_object_if_match_e_tag:
        description:
            - The entity tag (ETag) to match against that of the source object. Used to confirm that the source object
              with a given name is the version of that object storing a specified ETag.
            - Applicable only for I(action=copy_object).
    destination_region:
        description:
            - "The destination region the object will be copied to, for example \\"us-ashburn-1\\"."
            - Required for I(action=copy_object).
    destination_namespace:
        description:
            - The destination Object Storage namespace the object will be copied to.
            - Required for I(action=copy_object).
    destination_bucket:
        description:
            - The destination bucket the object will be copied to.
            - Required for I(action=copy_object).
    destination_object_name:
        description:
            - The name of the destination object resulting from the copy operation.
            - Required for I(action=copy_object).
    destination_object_if_match_e_tag:
        description:
            - The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten).
              Used to confirm that the destination object stored under a given name is the version of that object
              storing a specified entity tag.
            - Applicable only for I(action=copy_object).
    destination_object_if_none_match_e_tag:
        description:
            - "The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail
              if the object already exists in the destination bucket."
            - Applicable only for I(action=copy_object).
    destination_object_metadata:
        description:
            - "Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in
              \\"opc-meta-*\\" format. Avoid entering confidential information. Metadata key-value pairs entered
              in this field are assigned to the destination object. If you enter no metadata values, the destination
              object will inherit any existing metadata values associated with the source object."
            - Applicable only for I(action=copy_object).
        type: dict
    source_name:
        description:
            - The name of the source object to be renamed.
            - Required for I(action=rename_object).
    new_name:
        description:
            - The new name of the source object.
            - Required for I(action=rename_object).
    src_obj_if_match_e_tag:
        description:
            - The if-match entity tag (ETag) of the source object.
            - Applicable only for I(action=rename_object).
    new_obj_if_match_e_tag:
        description:
            - The if-match entity tag (ETag) of the new object.
            - Applicable only for I(action=rename_object).
    new_obj_if_none_match_e_tag:
        description:
            - The if-none-match entity tag (ETag) of the new object.
            - Applicable only for I(action=rename_object).
    object_name:
        description:
            - An object that is in an archive storage tier and needs to be restored.
            - Required for I(action=restore_objects).
    hours:
        description:
            - The number of hours for which this object will be restored.
              By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.
            - Applicable only for I(action=restore_objects).
        type: int
    action:
        description:
            - The action to perform on the Bucket.
        required: true
        choices: ["copy_object", "rename_object", "restore_objects"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action copy_object on bucket
  oci_object_storage_bucket_actions:
    source_object_name: backup.tar.gz
    source_object_if_match_e_tag: '*'
    destination_region: uk-london-1
    destination_namespace: ansh8lvru1zp
    destination_bucket: backup
    destination_object_name: backup2.tar.gz
    destination_object_if_match_e_tag: '*'
    destination_object_if_none_match_e_tag: '*'
    destination_object_metadata:
      opc-meta-a: b
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    action: copy_object

- name: Perform action rename_object on bucket
  oci_object_storage_bucket_actions:
    source_name: SourceObjectName
    new_name: TargetObjectName
    src_obj_if_match_e_tag: '*'
    new_obj_if_match_e_tag: '*'
    new_obj_if_none_match_e_tag: '*'
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    action: rename_object

- name: Perform action restore_objects on bucket
  oci_object_storage_bucket_actions:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    object_name: object_name_example
    action: restore_objects

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
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    convert_input_data_to_model_class,
)

try:
    from oci.object_storage import ObjectStorageClient
    from oci.object_storage.models import CopyObjectDetails
    from oci.object_storage.models import RenameObjectDetails
    from oci.object_storage.models import RestoreObjectsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketActionsHelperGen(OCIResourceHelperBase):
    """Supported actions: copy_object, rename_object, restore_objects"""

    @staticmethod
    def get_module_resource_id_param():
        return "bucket_name"

    def get_module_resource_id(self):
        return self.module.params.get("bucket_name")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bucket,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
        )

    def copy_object(self):
        action_details = convert_input_data_to_model_class(
            self.module.params, CopyObjectDetails
        )
        return oci_common_utils.call_with_backoff(
            self.client.copy_object,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            copy_object_details=action_details,
        )

    def rename_object(self):
        action_details = convert_input_data_to_model_class(
            self.module.params, RenameObjectDetails
        )
        return oci_common_utils.call_with_backoff(
            self.client.rename_object,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            rename_object_details=action_details,
        )

    def restore_objects(self):
        action_details = convert_input_data_to_model_class(
            self.module.params, RestoreObjectsDetails
        )
        return oci_common_utils.call_with_backoff(
            self.client.restore_objects,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            restore_objects_details=action_details,
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
            source_object_name=dict(type="str"),
            source_object_if_match_e_tag=dict(type="str"),
            destination_region=dict(type="str"),
            destination_namespace=dict(type="str"),
            destination_bucket=dict(type="str"),
            destination_object_name=dict(type="str"),
            destination_object_if_match_e_tag=dict(type="str"),
            destination_object_if_none_match_e_tag=dict(type="str"),
            destination_object_metadata=dict(type="dict"),
            source_name=dict(type="str"),
            new_name=dict(type="str"),
            src_obj_if_match_e_tag=dict(type="str"),
            new_obj_if_match_e_tag=dict(type="str"),
            new_obj_if_none_match_e_tag=dict(type="str"),
            object_name=dict(type="str"),
            hours=dict(type="int"),
            action=dict(
                type="str",
                required=True,
                choices=["copy_object", "rename_object", "restore_objects"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module, resource_type="bucket", service_client_class=ObjectStorageClient
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
