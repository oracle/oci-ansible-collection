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
module: oci_object_storage_object
short_description: Manage an Object resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete an Object resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oci_object_actions) module: copy, rename, restore."
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
    object_name:
        description:
            - "The name of the object. Avoid entering confidential information.
              Example: `test/object1.log`"
        type: str
        required: true
    content_length:
        description:
            - The content length of the body.
        type: int
    expect:
        description:
            - 100-continue
        type: str
    content_md5:
        description:
            - "The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object
              Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the
              MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error
              is returned with the message:"
            - "\\"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\\""
        type: str
    content_type:
        description:
            - The optional Content-Type header that defines the standard MIME type format of the object. Content type defaults to
              'application/octet-stream' if not specified in the PutObject call. Specifying values for this header has no effect
              on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example,
              you could use this header to identify and perform special operations on text only objects.
        type: str
    content_language:
        description:
            - The optional Content-Language header that defines the content language of the object to upload. Specifying
              values for this header has no effect on Object Storage behavior. Programs that read the object determine what
              to do based on the value provided. For example, you could use this header to identify and differentiate objects
              based on a particular language.
        type: str
    content_encoding:
        description:
            - The optional Content-Encoding header that defines the content encodings that were applied to the object to
              upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the
              object determine what to do based on the value provided. For example, you could use this header to determine
              what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of
              the object.
        type: str
    opc_meta:
        description:
            - Optional user-defined metadata key and value.
        type: dict
    version_id:
        description:
            - VersionId used to identify a particular version of the object
        type: str
    src:
        description:
            - The source file path when uploading an object. Use with I(state=present) to upload an object. This option is mutually exclusive with I(dest).
        type: str
    dest:
        description:
            - The destination file path when downloading an object. Use with I(namespace_name), I(bucket_name) and I(object_name) to download an object.
        type: str
    force:
        description:
            - Force overwriting existing local file when downloading or existing remote object when uploading.
        type: bool
        default: "true"
    state:
        description:
            - The state of the Object.
            - Use I(state=present) to update an existing an Object.
            - Use I(state=absent) to delete an Object.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update object
  oci_object_storage_object:
    namespace_name: namespace_example
    bucket_name: bucket_example
    object_name: object_example
    src: /usr/local/myobject.txt

- name: Update object
  oci_object_storage_object:
    namespace_name: namespace_example
    bucket_name: bucket_example
    object_name: object_example
    dest: /usr/local/myobject.txt

- name: Delete object
  oci_object_storage_object:
    namespace_name: namespace_example
    bucket_name: bucket_example
    object_name: object_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "object_name"

    def get_module_resource_id(self):
        return self.module.params.get("object_name")

    def get_get_fn(self):
        return self.client.get_object

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_object,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            object_name=self.module.params.get("object_name"),
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

        return oci_common_utils.list_all_resources(self.client.list_objects, **kwargs)

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def update_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.put_object,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                object_name=self.module.params.get("object_name"),
                content_length=self.module.params.get("content_length"),
                put_object_body=self.module.params.get("put_object_body"),
                expect=self.module.params.get("expect"),
                content_md5=self.module.params.get("content_md5"),
                content_type=self.module.params.get("content_type"),
                content_language=self.module.params.get("content_language"),
                content_encoding=self.module.params.get("content_encoding"),
                opc_meta=self.module.params.get("opc_meta"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_object,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                object_name=self.module.params.get("object_name"),
                version_id=self.module.params.get("version_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


ObjectHelperCustom = get_custom_class("ObjectHelperCustom")


class ResourceHelper(ObjectHelperCustom, ObjectHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            object_name=dict(type="str", required=True),
            content_length=dict(type="int"),
            expect=dict(type="str"),
            content_md5=dict(type="str"),
            content_type=dict(type="str"),
            content_language=dict(type="str"),
            content_encoding=dict(type="str"),
            opc_meta=dict(type="dict"),
            version_id=dict(type="str"),
            src=dict(type="str"),
            dest=dict(type="str"),
            force=dict(type="bool", default="true"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
