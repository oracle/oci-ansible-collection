#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
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
module: oci_object_facts
short_description: Retrieve details of an object or all the objects in a specific namespace and bucket in OCI Object \
                    Storage Service
description:
    - This module retrieves details of an object or all the objects present in a specified namespace and bucket in OCI \
      Object Storage Service.
version_added: "2.5"
options:
    namespace_name:
        description: Name of the namespace from which facts of objects need to be fetched.
        required: true
        aliases: [ 'namespace' ]
    bucket_name:
        description: Name of the bucket from which facts of objects need to be fetched.
        required: true
        aliases: [ 'bucket' ]
    object_name:
        description: Name of the object. Required to fetch details of a specific object.
        required: false
        aliases: [ 'object', 'name' ]
    prefix:
        description: The string to use for matching against the start of object names in a list query.
        required: false
    start:
        description: Object names returned by a list query must be greater or equal to this parameter.
        required: false
    end:
        description: Object names returned by a list query must be strictly less than this parameter.
        required: false
    delimiter:
        description: When this parameter is set, only objects whose names do not contain the delimiter character (after
                     an optionally specified prefix) are returned in the objects key of the response body. Scanned
                     objects whose names contain the delimiter have the part of their name up to the first
                     occurrence of the delimiter (including the optional prefix) returned as a set of prefixes.
                     Note that only '/' is a supported delimiter character at this time.
        required: false
        choices: ['/']
    fields:
        description: Object summary in list of objects includes the 'name' field. This parameter can also include 'size'
                     (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields.
                     Value of this parameter should be a comma-separated, case-insensitive list of those field names.
                     For example 'name,timeCreated,md5'. Allowed values are "name", "size", "timeCreated", "md5"
        required: false
        type: str
    list_multipart_uploads:
        description: If I(list_multipart_uploads=True), all in-progress multipart uploads for the given I(bucket) would
                     be listed.
        required: false
        default: False
    upload_id:
        description: The upload ID for a multipart upload. When I(upload_id) is specified, all the parts of the
                     specified in-progress multipart upload is listed.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all the objects in namespace 'mynamespace' and bucket 'mybucket'
  oci_object_facts:
    namespace: mynamespace
    bucket: mybucket

- name: Get details of all the objects in namespace 'mynamespace' and bucket 'mybucket' and only retrieve name and md5
  oci_object_facts:
    namespace: mynamespace
    bucket: mybucket
    fields: "name,md5"

- name: Get details of a specific object
  oci_object_facts:
    name: mynamespace
    bucket: mybucket
    object: myobject

- name: Get details of all in-progress multipart uploads for the given bucket
  oci_object_facts:
    name: mynamespace
    bucket: mybucket
    list_multipart_uploads: True

- name: Get details of all the parts of an in-progress multipart upload for a specific object
  oci_object_facts:
    name: mynamespace
    bucket: mybucket
    object: myobject
    upload_id: 951f4759-f910-50b4-udf99gf
"""

RETURN = """
objects:
    description: List of object details
    returned: On success
    type: complex
    contains:
        md5:
            description: Base64-encoded MD5 hash of the object data
            returned: always
            type: string
            sample: 3zBENq6MBnedDrpl2+SttQ==
        name:
            description: Name of the object
            returned: always
            type: string
            sample: image2a343.png
        size:
            description: Size of the object in bytes
            returned: always
            type: int
            sample: 165661
        time_created:
            description: Date and time of object creation
            returned: always
            type: datetime
            sample: 2017-10-09T08:39:17.411000+00:00
        etag:
            description: The current entity tag for the part.
            returned: multipart upload parts listing
            type: string
            sample: 7DF108FC90D40327E053821BC20
        part_size:
            description: The part number for this part.
            returned: multipart upload parts listing
            type: int
            sample: 2
        namespace:
            description: The Object Storage namespace in which the in-progress
                         multipart upload is stored.
            returned: multipart uploads listing
            type: int
            sample: 'ansible_namespace'
        bucket:
            description: The bucket in which the in-progress multipart upload
                         is stored.
            returned: multipart uploads listing
            type: int
            sample: 'ansible_bucket'
        object:
            description: The object name of the in-progress multipart upload.
            returned: multipart uploads listing
            type: int
            sample: 'ansible_object'
        upload_id:
            description: The unique identifier for the in-progress multipart upload.
            returned: multipart uploads listing
            type: string
            sample: '3f7c3d1f-15cf-97a6-c6d7-f31'
    sample: [
        {
            "md5": "3zBENq6MBnedDrpl2+SttQ==",
            "name": "image2a343.png",
            "size": 165661,
            "time_created": "2017-10-09T10:27:53.688000+00:00"
        },
        {
            "md5": "LWX13se0YFa6VVlv0R3hqA==",
            "name": "info1.txt",
            "size": 1084,
            "time_created": "2017-10-09T08:39:17.411000+00:00"
        },
        {
            "namespace":"ansible_namespace",
            "bucket":"ansible_bucket",
            "object":"ansible_object",
            "upload_id":"3f7c3d1f-15cf-97a6-c6d7-f319",
            "time_created":"2018-12-26T13:48:18.326000+00:00"
        },
        {
            "etag":"7DF108FC90D40327E053821BC20AC918",
            "md5":"J0doWIKY7JfZTrS1IPEGvA==",
            "size":28282272,
            "part_number":2
        }
    ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.object_storage.object_storage_client import ObjectStorageClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True, aliases=["namespace"]),
            bucket_name=dict(type="str", required=True, aliases=["bucket"]),
            object_name=dict(type="str", required=False, aliases=["name", "object"]),
            upload_id=dict(type="str", required=False),
            prefix=dict(type="str", required=False),
            start=dict(type="str", required=False),
            end=dict(type="str", required=False),
            delimiter=dict(type="str", required=False, choices=["/"]),
            fields=dict(type="str", required=False),
            list_multipart_uploads=dict(type=bool, required=False, default=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["list_multipart_uploads", "upload_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    object_storage_client = oci_utils.create_service_client(module, ObjectStorageClient)

    namespace = module.params["namespace_name"]
    bucket = module.params["bucket_name"]
    object_name = module.params["object_name"]
    fields_to_retrieve = ",".join(["name", "size", "timeCreated", "md5"])
    try:
        if module.params.get("upload_id") is not None:
            result = to_dict(
                oci_utils.list_all_resources(
                    object_storage_client.list_multipart_upload_parts,
                    namespace_name=namespace,
                    bucket_name=bucket,
                    object_name=object_name,
                    upload_id=module.params.get("upload_id"),
                )
            )
        elif module.params.get("list_multipart_uploads"):
            result = to_dict(
                oci_utils.list_all_resources(
                    object_storage_client.list_multipart_uploads,
                    namespace_name=namespace,
                    bucket_name=bucket,
                )
            )
        elif object_name is not None:
            result = to_dict(
                oci_utils.list_all_resources(
                    object_storage_client.list_objects,
                    namespace_name=namespace,
                    bucket_name=bucket,
                    prefix=object_name,
                    fields=fields_to_retrieve,
                ).objects
            )
        else:
            optional_list_method_params = [
                "prefix",
                "start",
                "end",
                "delimiter",
                "fields",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            # if the user hasn't specified a preference for fields, use the default "fields_to_retrieve"
            if optional_kwargs.get("fields") is None:
                optional_kwargs["fields"] = fields_to_retrieve

            result = to_dict(
                oci_utils.list_all_resources(
                    object_storage_client.list_objects,
                    namespace_name=namespace,
                    bucket_name=bucket,
                    **optional_kwargs
                ).objects
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(objects=result)


if __name__ == "__main__":
    main()
