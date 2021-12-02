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
module: oci_object_storage_object_actions
short_description: Perform actions on an Object resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Object resource in Oracle Cloud Infrastructure
    - For I(action=copy), creates a request to copy an object within a region or to another region.
    - "For I(action=reencrypt), re-encrypts the data encryption keys that encrypt the object and its chunks. By default, when you create a bucket, the Object
      Storage
      service manages the master encryption key used to encrypt each object's data encryption keys. The encryption mechanism that you specify for
      the bucket applies to the objects it contains.
      You can alternatively employ one of these encryption strategies for an object:
      - You can assign a key that you created and control through the Oracle Cloud Infrastructure Vault service.
      - You can encrypt an object using your own encryption key. The key you supply is known as a customer-provided encryption key (SSE-C)."
    - For I(action=rename), rename an object in the given Object Storage namespace.
      See L(Object Names,https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements)
      for object naming requirements.
    - For I(action=restore), restores one or more objects specified by the objectName parameter.
      By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.
    - For I(action=update_object_storage_tier), changes the storage tier of the object specified by the objectName parameter.
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
    source_object_name:
        description:
            - The name of the object to be copied.
            - Required for I(action=copy).
        type: str
    source_object_if_match_e_tag:
        description:
            - The entity tag (ETag) to match against that of the source object. Used to confirm that the source object
              with a given name is the version of that object storing a specified ETag.
            - Applicable only for I(action=copy).
        type: str
    source_version_id:
        description:
            - VersionId of the object to copy. If not provided then current version is copied by default.
            - Applicable only for I(action=copy).
        type: str
    destination_region:
        description:
            - "The destination region the object will be copied to, for example \\"us-ashburn-1\\"."
            - Required for I(action=copy).
        type: str
    destination_namespace:
        description:
            - The destination Object Storage namespace the object will be copied to.
            - Required for I(action=copy).
        type: str
    destination_bucket:
        description:
            - The destination bucket the object will be copied to.
            - Required for I(action=copy).
        type: str
    destination_object_name:
        description:
            - The name of the destination object resulting from the copy operation. Avoid entering confidential information.
            - Required for I(action=copy).
        type: str
    destination_object_if_match_e_tag:
        description:
            - The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten).
              Used to confirm that the destination object stored under a given name is the version of that object
              storing a specified entity tag.
            - Applicable only for I(action=copy).
        type: str
    destination_object_if_none_match_e_tag:
        description:
            - "The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail
              if the object already exists in the destination bucket."
            - Applicable only for I(action=copy).
        type: str
    destination_object_metadata:
        description:
            - "Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in
              \\"opc-meta-*\\" format. Avoid entering confidential information. Metadata key-value pairs entered
              in this field are assigned to the destination object. If you enter no metadata values, the destination
              object will inherit any existing metadata values associated with the source object."
            - Applicable only for I(action=copy).
        type: dict
    destination_object_storage_tier:
        description:
            - The storage tier that the object should be stored in. If not specified, the object will be stored in
              the same storage tier as the bucket.
            - Applicable only for I(action=copy).
        type: str
        choices:
            - "Standard"
            - "InfrequentAccess"
            - "Archive"
    opc_sse_customer_algorithm:
        description:
            - "The optional header that specifies \\"AES256\\" as the encryption algorithm. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm)."
            - Applicable only for I(action=copy).
        type: str
    opc_sse_customer_key:
        description:
            - The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
              decrypt the data. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_sse_customer_key_sha256:
        description:
            - The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
              value is used to check the integrity of the encryption key. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_source_sse_customer_algorithm:
        description:
            - "The optional header that specifies \\"AES256\\" as the encryption algorithm to use to decrypt the source
              object. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm)."
            - Applicable only for I(action=copy).
        type: str
    opc_source_sse_customer_key:
        description:
            - The optional header that specifies the base64-encoded 256-bit encryption key to use to decrypt
              the source object. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_source_sse_customer_key_sha256:
        description:
            - The optional header that specifies the base64-encoded SHA256 hash of the encryption key used to
              decrypt the source object. This value is used to check the integrity of the encryption key. For
              more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_sse_kms_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a master encryption key used to call the Key
              Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.
            - Applicable only for I(action=copy).
        type: str
    object_name:
        description:
            - "The name of the object. Avoid entering confidential information.
              Example: `test/object1.log`"
            - Required for I(action=reencrypt), I(action=restore), I(action=update_object_storage_tier).
        type: str
    kms_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the master encryption key used to call the Vault
              service to re-encrypt the data encryption keys associated with the object and its chunks. If the kmsKeyId value is
              empty, whether null or an empty string, the API will perform re-encryption by using the kmsKeyId associated with the
              bucket or the master encryption key managed by Oracle, depending on the bucket encryption mechanism.
            - Applicable only for I(action=reencrypt).
        type: str
    sse_customer_key:
        description:
            - ""
            - Applicable only for I(action=reencrypt).
        type: dict
        suboptions:
            algorithm:
                description:
                    - "Specifies the encryption algorithm. The only supported value is \\"AES256\\"."
                type: str
                choices:
                    - "AES256"
                required: true
            key:
                description:
                    - Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.
                type: str
                required: true
            key_sha256:
                description:
                    - Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity
                      of the encryption key.
                type: str
                required: true
    source_sse_customer_key:
        description:
            - ""
            - Applicable only for I(action=reencrypt).
        type: dict
        suboptions:
            algorithm:
                description:
                    - "Specifies the encryption algorithm. The only supported value is \\"AES256\\"."
                type: str
                choices:
                    - "AES256"
                required: true
            key:
                description:
                    - Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.
                type: str
                required: true
            key_sha256:
                description:
                    - Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity
                      of the encryption key.
                type: str
                required: true
    version_id:
        description:
            - VersionId used to identify a particular version of the object
            - Applicable only for I(action=reencrypt)I(action=restore)I(action=update_object_storage_tier).
        type: str
    source_name:
        description:
            - The name of the source object to be renamed.
            - Required for I(action=rename).
        type: str
    new_name:
        description:
            - The new name of the source object. Avoid entering confidential information.
            - Required for I(action=rename).
        type: str
    src_obj_if_match_e_tag:
        description:
            - The if-match entity tag (ETag) of the source object.
            - Applicable only for I(action=rename).
        type: str
    new_obj_if_match_e_tag:
        description:
            - The if-match entity tag (ETag) of the new object.
            - Applicable only for I(action=rename).
        type: str
    new_obj_if_none_match_e_tag:
        description:
            - "The if-none-match entity tag (ETag) of the new object. The only valid value is '*', which indicates
              request should fail if the new object already exists."
            - Applicable only for I(action=rename).
        type: str
    hours:
        description:
            - The number of hours for which this object will be restored.
              By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.
            - Applicable only for I(action=restore).
        type: int
    storage_tier:
        description:
            - The storage tier that the object should be moved to.
            - Required for I(action=update_object_storage_tier).
        type: str
        choices:
            - "Standard"
            - "InfrequentAccess"
            - "Archive"
    action:
        description:
            - The action to perform on the Object.
        type: str
        required: true
        choices:
            - "copy"
            - "reencrypt"
            - "rename"
            - "restore"
            - "update_object_storage_tier"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action copy on object
  oci_object_storage_object_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    source_object_name: source_object_name_example
    destination_region: destination_region_example
    destination_namespace: destination_namespace_example
    destination_bucket: destination_bucket_example
    destination_object_name: destination_object_name_example
    action: copy

    # optional
    source_object_if_match_e_tag: source_object_if_match_e_tag_example
    source_version_id: "ocid1.sourceversion.oc1..xxxxxxEXAMPLExxxxxx"
    destination_object_if_match_e_tag: destination_object_if_match_e_tag_example
    destination_object_if_none_match_e_tag: destination_object_if_none_match_e_tag_example
    destination_object_metadata: null
    destination_object_storage_tier: Standard
    opc_sse_customer_algorithm: opc_sse_customer_algorithm_example
    opc_sse_customer_key: opc_sse_customer_key_example
    opc_sse_customer_key_sha256: opc_sse_customer_key_sha256_example
    opc_source_sse_customer_algorithm: opc_source_sse_customer_algorithm_example
    opc_source_sse_customer_key: opc_source_sse_customer_key_example
    opc_source_sse_customer_key_sha256: opc_source_sse_customer_key_sha256_example
    opc_sse_kms_key_id: "ocid1.opcssekmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action reencrypt on object
  oci_object_storage_object_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    object_name: test/object1.log
    action: reencrypt

    # optional
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    sse_customer_key:
      # required
      algorithm: AES256
      key: key_example
      key_sha256: key_sha256_example
    source_sse_customer_key:
      # required
      algorithm: AES256
      key: key_example
      key_sha256: key_sha256_example
    version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action rename on object
  oci_object_storage_object_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    source_name: source_name_example
    new_name: new_name_example
    action: rename

    # optional
    src_obj_if_match_e_tag: src_obj_if_match_e_tag_example
    new_obj_if_match_e_tag: new_obj_if_match_e_tag_example
    new_obj_if_none_match_e_tag: new_obj_if_none_match_e_tag_example

- name: Perform action restore on object
  oci_object_storage_object_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    object_name: test/object1.log
    action: restore

    # optional
    version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"
    hours: 56

- name: Perform action update_object_storage_tier on object
  oci_object_storage_object_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    object_name: test/object1.log
    storage_tier: Standard
    action: update_object_storage_tier

    # optional
    version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
object:
    description:
        - Details of the Object resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - "The name of the object. Avoid entering confidential information.
                  Example: test/object1.log"
            returned: on success
            type: str
            sample: name_example
        size:
            description:
                - Size of the object in bytes.
            returned: on success
            type: int
            sample: 56
        md5:
            description:
                - Base64-encoded MD5 hash of the object data.
            returned: on success
            type: str
            sample: md5_example
        time_created:
            description:
                - The date and time the object was created, as described in L(RFC 2616,https://tools.ietf.org/html/rfc2616#section-14.29).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        etag:
            description:
                - The current entity tag (ETag) for the object.
            returned: on success
            type: str
            sample: etag_example
        storage_tier:
            description:
                - The storage tier that the object is stored in.
            returned: on success
            type: str
            sample: Standard
        archival_state:
            description:
                - Archival state of an object. This field is set only for objects in Archive tier.
            returned: on success
            type: str
            sample: Archived
        time_modified:
            description:
                - The date and time the object was modified, as described in L(RFC 2616,https://tools.ietf.org/rfc/rfc2616), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        headers:
            description:
                - response headers for the object
            returned: on success
            type: dict
            sample: {'Content-Length':'37','opc-meta-key1':'value1'}
    sample: {
        "name": "name_example",
        "size": 56,
        "md5": "md5_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "storage_tier": "Standard",
        "archival_state": "Archived",
        "time_modified": "2013-10-20T19:20:30+01:00",
        "headers": {'Content-Length':'37','opc-meta-key1':'value1'}
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
    from oci.object_storage.models import CopyObjectDetails
    from oci.object_storage.models import ReencryptObjectDetails
    from oci.object_storage.models import RenameObjectDetails
    from oci.object_storage.models import RestoreObjectsDetails
    from oci.object_storage.models import UpdateObjectStorageTierDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        copy
        reencrypt
        rename
        restore
        update_object_storage_tier
    """

    @staticmethod
    def get_module_resource_id_param():
        return "bucket_name"

    def get_module_resource_id(self):
        return self.module.params.get("bucket_name")

    def get_get_fn(self):
        return self.client.get_object

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_object,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            object_name=self.module.params.get("object_name"),
        )

    def copy(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CopyObjectDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.copy_object,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                copy_object_details=action_details,
                opc_sse_customer_algorithm=self.module.params.get(
                    "opc_sse_customer_algorithm"
                ),
                opc_sse_customer_key=self.module.params.get("opc_sse_customer_key"),
                opc_sse_customer_key_sha256=self.module.params.get(
                    "opc_sse_customer_key_sha256"
                ),
                opc_source_sse_customer_algorithm=self.module.params.get(
                    "opc_source_sse_customer_algorithm"
                ),
                opc_source_sse_customer_key=self.module.params.get(
                    "opc_source_sse_customer_key"
                ),
                opc_source_sse_customer_key_sha256=self.module.params.get(
                    "opc_source_sse_customer_key_sha256"
                ),
                opc_sse_kms_key_id=self.module.params.get("opc_sse_kms_key_id"),
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

    def reencrypt(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ReencryptObjectDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reencrypt_object,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                object_name=self.module.params.get("object_name"),
                reencrypt_object_details=action_details,
                version_id=self.module.params.get("version_id"),
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

    def rename(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RenameObjectDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rename_object,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                rename_object_details=action_details,
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

    def restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreObjectsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_objects,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                restore_objects_details=action_details,
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

    def update_object_storage_tier(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateObjectStorageTierDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_object_storage_tier,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                update_object_storage_tier_details=action_details,
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


ObjectActionsHelperCustom = get_custom_class("ObjectActionsHelperCustom")


class ResourceHelper(ObjectActionsHelperCustom, ObjectActionsHelperGen):
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
            source_version_id=dict(type="str"),
            destination_region=dict(type="str"),
            destination_namespace=dict(type="str"),
            destination_bucket=dict(type="str"),
            destination_object_name=dict(type="str"),
            destination_object_if_match_e_tag=dict(type="str"),
            destination_object_if_none_match_e_tag=dict(type="str"),
            destination_object_metadata=dict(type="dict"),
            destination_object_storage_tier=dict(
                type="str", choices=["Standard", "InfrequentAccess", "Archive"]
            ),
            opc_sse_customer_algorithm=dict(type="str"),
            opc_sse_customer_key=dict(type="str", no_log=True),
            opc_sse_customer_key_sha256=dict(type="str", no_log=True),
            opc_source_sse_customer_algorithm=dict(type="str"),
            opc_source_sse_customer_key=dict(type="str", no_log=True),
            opc_source_sse_customer_key_sha256=dict(type="str", no_log=True),
            opc_sse_kms_key_id=dict(type="str"),
            object_name=dict(type="str"),
            kms_key_id=dict(type="str"),
            sse_customer_key=dict(
                type="dict",
                no_log=False,
                options=dict(
                    algorithm=dict(type="str", required=True, choices=["AES256"]),
                    key=dict(type="str", required=True, no_log=True),
                    key_sha256=dict(type="str", required=True, no_log=True),
                ),
            ),
            source_sse_customer_key=dict(
                type="dict",
                no_log=False,
                options=dict(
                    algorithm=dict(type="str", required=True, choices=["AES256"]),
                    key=dict(type="str", required=True, no_log=True),
                    key_sha256=dict(type="str", required=True, no_log=True),
                ),
            ),
            version_id=dict(type="str"),
            source_name=dict(type="str"),
            new_name=dict(type="str"),
            src_obj_if_match_e_tag=dict(type="str"),
            new_obj_if_match_e_tag=dict(type="str"),
            new_obj_if_none_match_e_tag=dict(type="str"),
            hours=dict(type="int"),
            storage_tier=dict(
                type="str", choices=["Standard", "InfrequentAccess", "Archive"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "copy",
                    "reencrypt",
                    "rename",
                    "restore",
                    "update_object_storage_tier",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="object",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
