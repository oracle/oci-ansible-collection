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
module: oci_object_storage_object_facts
short_description: Fetches details about one or multiple Object resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Object resources in Oracle Cloud Infrastructure
    - Lists the objects in a bucket.
    - To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
      talk to an administrator. If you are an administrator who needs to write policies to give users access, see
      L(Getting Started with Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm).
    - If I(object_name) is specified, the details of a single Object will be returned.
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
            - Required to get a specific object.
        type: str
    version_id:
        description:
            - VersionId used to identify a particular version of the object
        type: str
    range:
        description:
            - Optional byte range to fetch, as described in L(RFC 7233,https://tools.ietf.org/html/rfc7233#section-2.1).
              Note that only a single range of bytes is supported.
        type: str
    prefix:
        description:
            - The string to use for matching against the start of object names in a list query.
        type: str
    start:
        description:
            - Object names returned by a list query must be greater or equal to this parameter.
        type: str
    end:
        description:
            - Object names returned by a list query must be strictly less than this parameter.
        type: str
    delimiter:
        description:
            - When this parameter is set, only objects whose names do not contain the delimiter character
              (after an optionally specified prefix) are returned in the objects key of the response body.
              Scanned objects whose names contain the delimiter have the part of their name up to the first
              occurrence of the delimiter (including the optional prefix) returned as a set of prefixes.
              Note that only '/' is a supported delimiter character at this time.
        type: str
    fields:
        description:
            - Object summary in list of objects includes the 'name' field. This parameter can also include 'size'
              (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time) and 'timeModified'
              (object modification date and time).
              Value of this parameter should be a comma-separated, case-insensitive list of those field names.
              For example 'name,etag,timeCreated,md5,timeModified'
        type: str
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List objects
  oci_object_storage_object_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

- name: Get a specific object
  oci_object_storage_object_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    object_name: test/object1.log

"""

RETURN = """
objects:
    description:
        - List of Object resources
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
    sample: [{
        "name": "name_example",
        "size": 56,
        "md5": "md5_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "time_modified": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "bucket_name",
            "object_name",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "version_id",
            "range",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_object,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            object_name=self.module.params.get("object_name"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "prefix",
            "start",
            "end",
            "delimiter",
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_objects,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )


ObjectFactsHelperCustom = get_custom_class("ObjectFactsHelperCustom")


class ResourceFactsHelper(ObjectFactsHelperCustom, ObjectFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            object_name=dict(type="str"),
            version_id=dict(type="str"),
            range=dict(type="str"),
            prefix=dict(type="str"),
            start=dict(type="str"),
            end=dict(type="str"),
            delimiter=dict(type="str"),
            fields=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="object",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(objects=result)


if __name__ == "__main__":
    main()
