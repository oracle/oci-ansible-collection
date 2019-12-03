#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
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
module: oci_bucket
short_description: Create,update and delete oci buckets
description:
    - Creates OCI bucket if not present.
    - Update OCI bucket, if present.
    - Delete OCI bucket, if present.
version_added: "2.5"
options:
    namespace_name:
        description: Name of the namespace in which the bucket is available or should be available
        required: true
    compartment_id:
        description: Identifier of the compartment in which the bucket is available or should be available. Mandatory
                     for I(state=present). Not required for I(state=absent)
        required: false
    name:
        description: Name of the bucket. Bucket name must be unique within a namespace.
                     For naming conventions, refer U(https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingbuckets.htm)
        required: true
    metadata:
        description: Use defined metadata dict(str,str) for the bucket. Limit is 4KB.
        required: false
    public_access_type:
        description: The type of public access  of the bucket. By default, no public access is allowed on the bucket.
                     If I(public_access_type=ObjectRead), user can perform read operation on the bucket.
        required: false
        default: "NoPublicAccess"
        choices: ["ObjectRead","NoPublicAccess","ObjectReadWithoutList"]
    storage_tier:
        description: The type of storage tier of this bucket. The bucket will be put in the standard storage tier.
                     When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier.
                     This property is immutable after bucket is created.
        default: "Standard"
        choices: ["Standard","Archive"]
    kms_key_id:
        description: The OCID of a KMS key id used to call KMS to generate the data key or decrypt the encrypted data key.
    state:
        description: Decides whether to create,update or delete bucket. For I(state=present), if the bucket does not
                     exist, it gets created. If it exists, it gets updated. For I(state=absent), the bucket gets
                     deleted.
        required: true
        default: 'present'
        choices: ['present','absent']
    force:
        description: If I(force='no') and the bucket contains objects and pre-authenticared request at the bucket level,
                     bucket will not be deleted. To delete a bucket which has objects and pre-authenticated request at
                     the bucket level, I(force='yes') should be specified.
        required: false
        default: 'no'
        type: bool

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Note: These examples do not set authentication details.

#Bucket creation or update
- name: Create or Update bucket
  oci_bucket:
    namespace_name: 'ansibletestspace'
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    name: 'AnsibleTestBucket'
    public_access_type: 'NoPublicAccess'
    metadata:
        project: 'Test Project'
    state: 'present'

#Delete bucket
- name: Delete bucket with 'force' to delete the bucket
        along with all the containing objects
  oci_bucket:
    namespace_name: 'ansibletestspace'
    name: 'AnsibleTestBucket'
    force: 'yes'
    state: 'absent'

"""

RETURN = """
bucket:
    description: Attributes of the created/updated bucket. Applicable only for create and update.
    returned: success
    type: dict
    sample: {"compartment_id": "ocid1....62xq","created_by":"ocid1.user.oc1..xxxxxEXAMPLExxxxx..qndq",
            "etag": "cb734ffe-da3a-48f4-....-161fd4604cf1","metadata": {},"name":"AnsibleTestBucket",
            "namespace":"ansibletestspace","public_access_type": "ObjectRead",
            "time_created": "2017-10-01T11:30:33.655000+00:00"}

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.object_storage.object_storage_client import ObjectStorageClient
    from oci.object_storage.models import CreateBucketDetails
    from oci.object_storage.models import UpdateBucketDetails
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

"""
Function
"""

logger = None


def create_or_update_bucket(object_storage_client, module):
    bucket = None
    result = dict(changed=False, bucket="")
    namespace_name = module.params["namespace_name"]
    bucket_name = module.params["name"]
    bucket = get_existing_bucket(object_storage_client, module)
    try:
        if bucket:
            changed = should_bucket_be_changed(
                bucket, module.params["metadata"], module.params["public_access_type"]
            )
            if changed:
                get_logger().info(
                    "Updating bucket %s in namespace %s", bucket_name, namespace_name
                )
                response = update_bucket(object_storage_client, module)
                bucket = response.data
                get_logger().info("Sucessfully updated bucket")
        else:
            get_logger().info(
                "Creating bucket %s in namespace %s", bucket_name, namespace_name
            )
            changed = True
            response = create_bucket(object_storage_client, module)
            bucket = response.data
            get_logger().info("Sucessfully created bucket %s", bucket_name)
    except ServiceError as ex:
        get_logger().error(
            "Failed to create or update bucket %s", bucket_name, exc_info=True
        )
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    result["bucket"] = to_dict(bucket)

    return result


def get_existing_bucket(object_storage_client, module):
    namespace_name = module.params["namespace_name"]
    name = module.params["name"]
    existing_bucket = None
    get_logger().debug(
        "Checking whether bucket %s exists in namespace %s", name, namespace_name
    )
    try:
        response = object_storage_client.get_bucket(namespace_name, name)
        existing_bucket = response.data
    except ServiceError as ex:
        if ex.status != 404:
            get_logger().error(
                "Failed to perform checking existing bucket", exc_info=True
            )
            module.fail_json(msg=ex.message)
        get_logger().debug(
            "Bucket %s does not exist in namespace %s", name, namespace_name
        )

    return existing_bucket


def should_bucket_be_changed(existing_bucket, metadata, public_access_type):
    return (
        existing_bucket.metadata != metadata
        or existing_bucket.public_access_type != public_access_type
    )


def bucket_details_factory(bucket_details_type, module):
    bucket_details = None
    if bucket_details_type == "create":
        bucket_details = CreateBucketDetails()
        bucket_details.storage_tier = module.params["storage_tier"]
    elif bucket_details_type == "update":
        bucket_details = UpdateBucketDetails()

    bucket_details.compartment_id = module.params["compartment_id"]
    bucket_details.name = module.params["name"]
    bucket_details.public_access_type = module.params["public_access_type"]
    bucket_details.kms_key_id = module.params["kms_key_id"]
    bucket_details.metadata = module.params["metadata"]

    return bucket_details


def create_bucket(object_storage_client, module):
    namespace_name = module.params["namespace_name"]
    create_bucket_details = bucket_details_factory("create", module)

    return object_storage_client.create_bucket(namespace_name, create_bucket_details)


def update_bucket(object_storage_client, module):
    namespace_name = module.params["namespace_name"]
    bucket_name = module.params["name"]
    update_bucket_details = bucket_details_factory("update", module)

    return object_storage_client.update_bucket(
        namespace_name, bucket_name, update_bucket_details
    )


def delete_bucket(object_storage_client, module):
    namespace_name = module.params["namespace_name"]
    bucket_name = module.params["name"]
    force = module.params["force"]
    opc_client_request_id_dict = {"opc_client_request_id": "ax55b"}
    changed = False
    result = dict(changed=False)
    get_logger().info(
        "Deleting bucket %s in namespace %s with force option:%s",
        bucket_name,
        namespace_name,
        force,
    )
    existing_bucket = get_existing_bucket(object_storage_client, module)
    try:
        if existing_bucket:
            if force:
                delete_all_objects_in_bucket(
                    object_storage_client, namespace_name, bucket_name
                )
                delete_all_pars_of_bucket(
                    object_storage_client, namespace_name, bucket_name
                )
            object_storage_client.delete_bucket(
                namespace_name, bucket_name, **opc_client_request_id_dict
            )
            changed = True
            get_logger().info(
                "Successfully deleted bucket % s in namespace % s \
                              with force option: % s",
                bucket_name,
                namespace_name,
                force,
            )
    except ServiceError as ex:
        get_logger().error("Failed to delete bucket %s", bucket_name, exc_info=True)
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    result["bucket"] = to_dict(existing_bucket)

    return result


def delete_all_objects_in_bucket(object_storage_client, namespace_name, bucket_name):
    get_logger().debug("Deleting all objects inside bucket: %s", bucket_name)
    fields_to_retrieve = "name"
    objects_in_bucket = oci_utils.list_all_resources(
        object_storage_client.list_objects,
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        fields=fields_to_retrieve,
    )
    for obj in objects_in_bucket.objects:
        get_logger().debug("Deleting object: %s", obj.name)
        object_storage_client.delete_object(namespace_name, bucket_name, obj.name)


def delete_all_pars_of_bucket(object_storage_client, namespace_name, bucket_name):
    get_logger().debug(
        "Deleting all Pre-Authenticated Requests of bucket: %s", bucket_name
    )
    pars_of_bucket = oci_utils.list_all_resources(
        object_storage_client.list_preauthenticated_requests,
        namespace_name=namespace_name,
        bucket_name=bucket_name,
    )
    for par in pars_of_bucket:
        get_logger().debug("Deleting Pre-authenticated Request: %s", par.id)
        oci_utils.call_with_backoff(
            object_storage_client.delete_preauthenticated_request,
            par_id=par.id,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
        )


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_bucket")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            compartment_id=dict(type="str", required=False),
            name=dict(type="str", required=True),
            public_access_type=dict(
                type="str",
                required=False,
                default="NoPublicAccess",
                choices=["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"],
            ),
            metadata=dict(type="dict", default={}),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            storage_tier=dict(
                type="str",
                required=False,
                default="Standard",
                choices=["Standard", "Archive"],
            ),
            kms_key_id=dict(type="str", required=False),
            force=dict(type="bool", required=False, default=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    object_storage_client = oci_utils.create_service_client(module, ObjectStorageClient)
    state = module.params["state"]
    if state == "present":
        result = create_or_update_bucket(object_storage_client, module)
    elif state == "absent":
        result = delete_bucket(object_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
