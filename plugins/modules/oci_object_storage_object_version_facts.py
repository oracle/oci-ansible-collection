#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_object_storage_object_version_facts
short_description: Fetches details about one or multiple ObjectVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ObjectVersion resources in Oracle Cloud Infrastructure
    - Lists the object versions in a bucket.
    - ListObjectVersions returns an ObjectVersionCollection containing at most 1000 object versions. To paginate through
      more object versions, use the returned `opc-next-page` value with the `page` request parameter.
    - To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
      talk to an administrator. If you are an administrator who needs to write policies to give users access, see
      L(Getting Started with Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm).
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List object_versions
  oci_object_storage_object_version_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

"""

RETURN = """
object_versions:
    description:
        - List of ObjectVersion resources
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
        time_modified:
            description:
                - The date and time the object was modified, as described in L(RFC 2616,https://tools.ietf.org/rfc/rfc2616#section-14.29).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        etag:
            description:
                - The current entity tag (ETag) for the object.
            returned: on success
            type: string
            sample: etag_example
        storage_tier:
            description:
                - The storage tier that the object is stored in.
            returned: on success
            type: string
            sample: Standard
        archival_state:
            description:
                - Archival state of an object. This field is set only for objects in Archive tier.
            returned: on success
            type: string
            sample: Archived
        version_id:
            description:
                - VersionId of the object.
            returned: on success
            type: string
            sample: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"
        is_delete_marker:
            description:
                - This flag will indicate if the version is deleted or not.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "size": 56,
        "md5": "md5_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_modified": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "storage_tier": "Standard",
        "archival_state": "Archived",
        "version_id": "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx",
        "is_delete_marker": true
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


class ObjectVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "prefix",
            "start",
            "end",
            "delimiter",
            "fields",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_object_versions,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )


ObjectVersionFactsHelperCustom = get_custom_class("ObjectVersionFactsHelperCustom")


class ResourceFactsHelper(ObjectVersionFactsHelperCustom, ObjectVersionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            prefix=dict(type="str"),
            start=dict(type="str"),
            end=dict(type="str"),
            delimiter=dict(type="str"),
            fields=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="object_version",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(object_versions=result)


if __name__ == "__main__":
    main()
