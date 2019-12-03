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
module: oci_bucket_facts
short_description: Fetches details of a bucket or all available buckets within a namespace
description:
    - This module retrieves details of a bucket or all the buckets available for specified namespace and compartment
      identifier.
version_added: "2.5"
options:
    namespace_name:
        description: Name of the namespace from which facts of constituent buckets needs to be fetched.
        required: true
    compartment_id:
        description: Identifier of the compartment from which facts of constituent buckets needs to be fetched.
                    Required to get details of all buckets in a specified namespace and compartment.
    name:
        description: Name of the bucket. Required to fetch details of a specific bucket.
        required: false
        aliases: [ 'bucket' ]
    fields:
        description: Specifies additional fields to be returned in the response.  By default a response includes
                     the 'namespace', 'name', 'compartment_id', 'created_by', 'time_created', and 'etag' fields.
                     Specifying "tags" will populate the fields "freeform_tags" and "defined_tags".  Specifying
                     "approximateSize" will populate the field "approximate_size".  Specifying "approximateCount"
                     will populate the field "approximate_size".  Any combination of the values may be provided.
        required: false
        choices: ["tags", "approximateCount", "approximateSize"]
        type: 'list'
author: "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Note: These examples do not set authentication details.

#Listing facts of all buckets in a given namespace and compartment

- name: List bucket facts
  oci_bucket_facts:
    namespace_name: 'mynamespace'
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: List bucket facts (including tags)
  oci_bucket_facts:
    namespace_name: 'mynamespace'
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    fields: ["tags"]

# Fetch facts of a specific bucket
- name: Fetch a bucket
  oci_bucket_facts:
    namespace_name: 'mynamespace'
    name: 'Bucket1'

# Fetch facts of a specific bucket (including approximate size and count)
- name: Fetch a bucket
  oci_bucket_facts:
    namespace_name: 'mynamespace'
    name: 'Bucket1'
    fields: ["approximateSize", "approximateCount"]
"""

RETURN = """
buckets:
    description: The specified bucket or a list of all available buckets in the specified namespace and compartment.
    returned: on success
    type: complex
    contains:
        compartment_id:
            description: The ID of the compartment in which the bucket is authorized
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        created_by:
            description: The OCID of the user who created the bucket.
            returned: always
            type: string
            sample: ocid1.user.oc1..xxxxxEXAMPLExxxxx
        etag:
            description: The entity tag for the bucket.
            returned: always
            type: string
            sample: 7d48fea5-ghfc
        metadata:
            description: Arbitrary string keys and values for user-defined metadata.
            returned: On retrieving a specific bucket
            type: dict(str,str)
            sample: {foo: bar}
        name:
            description: The name of the bucket
            returned: always
            type: string
            sample: my-new-bucket1
        namespace:
            description: The namespace in which the bucket lives
            returned: always
            type: string
            sample: mynamespace
        public_access_type:
            description: The type of public access enabled on this bucket. A bucket is set to NoPublicAccess by \
                        default, which only allows an authenticated caller to access the bucket and its contents. When \
                        ObjectRead is enabled on the bucket, public access is allowed for the GetObject, HeadObject, \
                        and ListObjects operations.
            returned: On retrieving a specific bucket
            type: string
            sample: NoPublicAccess
        time_created:
            description: The date and time the bucket was created, as described in RFC 2616, section 14.29
            returned: always
            type: string
            sample: 2017-10-07T16:20:33.933000+00:00
        approximate_size:
            description: The approximate total size of all objects in the bucket. \
                         Size statistics are reported periodically. You will see a lag between what is displayed and \
                         the actual size of the bucket.
            returned: only when 'approximateSize' is specified in the 'fields' input option
            type: int
        approximate_count:
            description: The approximate number of objects in the bucket.  \
                         Count statistics are reported periodically. You will see a lag between what is displayed \
                         and the actual object count.
            returned: only when 'approximateCount' is specified in the 'fields' input option
            type: int
    sample: [{"compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
              "created_by": "ocid1.user.oc1..xxxxxEXAMPLExxxxx",
              "etag": "7d48fea5-ghfc",
              "name": "Bucket1",
              "namespace": "mynamespace",
              "time_created": "2017-10-07T16:20:33.933000+00:00"
              }, {
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
              "created_by": "ocid1.user.oc1..xxxxxEXAMPLExxxxx",
              "etag": "3f0158f2-68ea",
              "name": "Bucket2",
              "namespace": "mynamespace",
              "time_created": "2017-10-06T13:47:38.544000+00:00"
             }]
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


def list_buckets(object_storage_client, module, get_kwargs, list_kwargs):
    try:
        namespace_name = module.params["namespace_name"]
        compartment_id = module.params["compartment_id"]

        buckets_to_return = []

        buckets = oci_utils.list_all_resources(
            object_storage_client.list_buckets,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **list_kwargs
        )

        # if there are fields requested that are only available on the Get call
        # we must individually fetch each bucket in the list
        if get_kwargs:
            for bucket in buckets:
                buckets_to_return.append(
                    object_storage_client.get_bucket(
                        namespace_name, bucket.name, **get_kwargs
                    ).data
                )
        else:
            buckets_to_return = buckets
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    return to_dict(buckets_to_return)


def filter_to_whitelisted_arguments(argument_list, whitelist):
    filtered_list = []
    for value in argument_list:
        if value in whitelist:
            filtered_list.append(value)

    return filtered_list


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            compartment_id=dict(type="str", required=False),
            name=dict(type="str", required=False, aliases=["bucket"]),
            fields=dict(
                type="list",
                required=False,
                choices=["tags", "approximateSize", "approximateCount"],
            ),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "name"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    object_storage_client = oci_utils.create_service_client(module, ObjectStorageClient)

    valid_field_values_for_list_call = ["tags"]
    valid_field_values_for_get_call = ["approximateSize", "approximateCount"]

    get_kwargs = {}
    list_kwargs = {}

    fields_arg_value = module.params.get("fields")
    if fields_arg_value:
        get_kwargs["fields"] = filter_to_whitelisted_arguments(
            fields_arg_value, valid_field_values_for_get_call
        )
        list_kwargs["fields"] = filter_to_whitelisted_arguments(
            fields_arg_value, valid_field_values_for_list_call
        )

    bucket_name = module.params["name"]
    if bucket_name is not None:
        try:
            result = [
                to_dict(
                    object_storage_client.get_bucket(
                        module.params["namespace_name"], bucket_name, **get_kwargs
                    ).data
                )
            ]
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    else:
        result = list_buckets(object_storage_client, module, get_kwargs, list_kwargs)

    module.exit_json(buckets=result)


if __name__ == "__main__":
    main()
