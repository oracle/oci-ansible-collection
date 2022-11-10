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
module: oci_object_storage_object_facts
short_description: Fetches details about one or multiple Object resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Object resources in Oracle Cloud Infrastructure
    - Lists the objects in a bucket. By default, ListObjects returns object names only. See the `fields`
      parameter for other fields that you can optionally include in ListObjects response.
    - ListObjects returns at most 1000 objects. To paginate through more objects, use the returned 'nextStartWith'
      value with the 'start' parameter. To filter which objects ListObjects returns, use the 'start' and 'end'
      parameters.
    - To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
      talk to an administrator. If you are an administrator who needs to write policies to give users access, see
      L(Getting Started with Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm).
    - If I(object_name) is specified, the details of a single Object will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
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
    opc_sse_customer_algorithm:
        description:
            - "The optional header that specifies \\"AES256\\" as the encryption algorithm. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm)."
        type: str
    opc_sse_customer_key:
        description:
            - The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
              decrypt the data. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm).
        type: str
    opc_sse_customer_key_sha256:
        description:
            - The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
              value is used to check the integrity of the encryption key. For more information, see
              L(Using Your Own Keys for Server-Side Encryption,https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm).
        type: str
    http_response_content_disposition:
        description:
            - Specify this query parameter to override the value of the Content-Disposition response header in the GetObject response.
        type: str
    http_response_cache_control:
        description:
            - Specify this query parameter to override the Cache-Control response header in the GetObject response.
        type: str
    http_response_content_type:
        description:
            - Specify this query parameter to override the Content-Type response header in the GetObject response.
        type: str
    http_response_content_language:
        description:
            - Specify this query parameter to override the Content-Language response header in the GetObject response.
        type: str
    http_response_content_encoding:
        description:
            - Specify this query parameter to override the Content-Encoding response header in the GetObject response.
        type: str
    http_response_expires:
        description:
            - Specify this query parameter to override the Expires response header in the GetObject response.
        type: str
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
            - Object summary by default includes only the 'name' field. Use this parameter to also
              include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time),
              'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields.
              Specify the value of this parameter as a comma-separated, case-insensitive list of those field names.
              For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific object
  oci_object_storage_object_facts:
    # required
    object_name: object_name_example
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example

    # optional
    version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"
    range: range_example
    opc_sse_customer_algorithm: opc_sse_customer_algorithm_example
    opc_sse_customer_key: opc_sse_customer_key_example
    opc_sse_customer_key_sha256: opc_sse_customer_key_sha256_example
    http_response_content_disposition: http_response_content_disposition_example
    http_response_cache_control: http_response_cache_control_example
    http_response_content_type: http_response_content_type_example
    http_response_content_language: http_response_content_language_example
    http_response_content_encoding: http_response_content_encoding_example
    http_response_expires: http_response_expires_example

- name: List objects
  oci_object_storage_object_facts:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example

    # optional
    prefix: prefix_example
    start: start_example
    end: end_example
    delimiter: delimiter_example
    fields: fields_example

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
    sample: [{
        "name": "name_example",
        "size": 56,
        "md5": "md5_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "storage_tier": "Standard",
        "archival_state": "Archived",
        "time_modified": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "http_response_content_disposition",
            "http_response_cache_control",
            "http_response_content_type",
            "http_response_content_language",
            "http_response_content_encoding",
            "http_response_expires",
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
            object_name=dict(type="str"),
            version_id=dict(type="str"),
            range=dict(type="str"),
            opc_sse_customer_algorithm=dict(type="str"),
            opc_sse_customer_key=dict(type="str", no_log=True),
            opc_sse_customer_key_sha256=dict(type="str", no_log=True),
            http_response_content_disposition=dict(type="str"),
            http_response_cache_control=dict(type="str"),
            http_response_content_type=dict(type="str"),
            http_response_content_language=dict(type="str"),
            http_response_content_encoding=dict(type="str"),
            http_response_expires=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            prefix=dict(type="str"),
            start=dict(type="str"),
            end=dict(type="str"),
            delimiter=dict(type="str"),
            fields=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

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
