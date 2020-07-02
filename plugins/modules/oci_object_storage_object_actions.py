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
module: oci_object_storage_object_actions
short_description: Perform actions on an Object resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Object resource in Oracle Cloud Infrastructure
    - For I(action=copy), creates a request to copy an object within a region or to another region.
    - For I(action=rename), rename an object in the given Object Storage namespace.
    - For I(action=restore), restores one or more objects specified by the objectName parameter.
      By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.
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
            - The name of the destination object resulting from the copy operation.
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
    opc_sse_customer_algorithm:
        description:
            - "The optional header that specifies \\"AES256\\" as the encryption algorithm. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourecryptionkeys.htm)."
            - Applicable only for I(action=copy).
        type: str
    opc_sse_customer_key:
        description:
            - The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
              decrypt the data. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourecryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_sse_customer_key_sha256:
        description:
            - The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
              value is used to check the integrity of the encryption key. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourecryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_source_sse_customer_algorithm:
        description:
            - "The optional header that specifies \\"AES256\\" as the encryption algorithm to use to decrypt the source
              object. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourecryptionkeys.htm)."
            - Applicable only for I(action=copy).
        type: str
    opc_source_sse_customer_key:
        description:
            - The optional header that specifies the base64-encoded 256-bit encryption key to use to decrypt
              the source object. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourecryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    opc_source_sse_customer_key_sha256:
        description:
            - The optional header that specifies the base64-encoded SHA256 hash of the encryption key used to
              decrypt the source object. This value is used to check the integrity of the encryption key. For
              more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourecryptionkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    source_name:
        description:
            - The name of the source object to be renamed.
            - Required for I(action=rename).
        type: str
    new_name:
        description:
            - The new name of the source object.
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
            - The if-none-match entity tag (ETag) of the new object.
            - Applicable only for I(action=rename).
        type: str
    object_name:
        description:
            - An object that is in an archive storage tier and needs to be restored.
            - Required for I(action=restore).
        type: str
    hours:
        description:
            - The number of hours for which this object will be restored.
              By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.
            - Applicable only for I(action=restore).
        type: int
    version_id:
        description:
            - The versionId of the object to restore. Current object version is used by default.
            - Applicable only for I(action=restore).
        type: str
    action:
        description:
            - The action to perform on the Object.
        type: str
        required: true
        choices:
            - "copy"
            - "rename"
            - "restore"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action copy on object
  oci_object_storage_object_actions:
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
    action: copy

- name: Perform action rename on object
  oci_object_storage_object_actions:
    source_name: SourceObjectName
    new_name: TargetObjectName
    src_obj_if_match_e_tag: '*'
    new_obj_if_match_e_tag: '*'
    new_obj_if_none_match_e_tag: '*'
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    action: rename

- name: Perform action restore on object
  oci_object_storage_object_actions:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    object_name: object_name_example
    action: restore

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
            type: string
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
            type: string
            sample: md5_example
        time_created:
            description:
                - The date and time the object was created, as described in L(RFC 2616,https://tools.ietf.org/html/rfc2616#section-14.29).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        etag:
            description:
                - The current entity tag (ETag) for the object.
            returned: on success
            type: string
            sample: etag_example
        time_modified:
            description:
                - The date and time the object was modified, as described in L(RFC 2616,https://tools.ietf.org/rfc/rfc2616), section 14.29.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "name": "name_example",
        "size": 56,
        "md5": "md5_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "time_modified": "2013-10-20T19:20:30+01:00"
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
    from oci.object_storage.models import RenameObjectDetails
    from oci.object_storage.models import RestoreObjectsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        copy
        rename
        restore
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
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
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
            waiter_client=self.client,
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
            waiter_client=self.client,
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
            opc_sse_customer_algorithm=dict(type="str"),
            opc_sse_customer_key=dict(type="str"),
            opc_sse_customer_key_sha256=dict(type="str"),
            opc_source_sse_customer_algorithm=dict(type="str"),
            opc_source_sse_customer_key=dict(type="str"),
            opc_source_sse_customer_key_sha256=dict(type="str"),
            source_name=dict(type="str"),
            new_name=dict(type="str"),
            src_obj_if_match_e_tag=dict(type="str"),
            new_obj_if_match_e_tag=dict(type="str"),
            new_obj_if_none_match_e_tag=dict(type="str"),
            object_name=dict(type="str"),
            hours=dict(type="int"),
            version_id=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["copy", "rename", "restore"]
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
