#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_preauthenticated_request
short_description: Create and delete an OCI Preauthenticated Request
description:
    - Create a new OCI Preauthenticated Request for a bucket or an object
    - Delete an OCI Preauthenticated Request, if present
    - Note that the unique URL provided by the system when you create a pre-authenticated request is the only way a
      user can access the bucket or object specified as the request target. Copy the URL to durable storage. The URL is
      returned only at the time of creation and cannot be retrieved later.
version_added: "2.5"
options:
    namespace_name:
        description: The Object Storage namespace used for the request.
        required: true
    bucket_name:
        description: The name of the bucket. Avoid entering confidential information.
        required: false
    par_id:
        description: Identifier of the Preauthenticated Request. Mandatory for delete.
        required: false
        aliases: ['id']
    name:
        description: A user-specified name for the pre-authenticated request. Names can be helpful in managing
                     pre-authenticated requests. Required while creating a Preauthenticated request with
                     I(state=present).
        required: false
        aliases: ['display_name']
    object_name:
        description: The name of the object that is being granted access to by the pre-authenticated request.
                     Avoid entering confidential information. The object name can be null and if so, the
                     pre-authenticated request grants access to the entire bucket.
        required: false
    time_expires:
        description: The expiration date for the pre-authenticated request as per RFC 3339. After this date
                     the pre-authenticated request will no longer be valid.
        required: false
    access_type:
        description: The expiration date for the pre-authenticated request as per RFC 3339. After this date
                     the pre-authenticated request will no longer be valid. Required while creating a Preauthenticated
                     request with I(state=present).
        required: false
        choices: ["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]
    state:
        description: Create or delete Preauthenticated Request. Use I(state=present) to create a Preauthenticated
                     request and I(state=absent) to delete a Preauthenticated request.
        required: false
        default: 'present'
        choices: ['present','absent']

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Preauthenticated Request for Entire Bucket
- name: Create Preauthenticated Request for a Bucket and permit uploading one or more objects to it
  oci_preauthenticated_request:
    namespace_name: 'us-example-1'
    bucket_name: 'ansible_bucket'
    name: 'ansible_bucket_par'
    access_type: 'AnyObjectWrite'
    time_expires: '2018-12-22T00:00:00+00:00'
    state: 'present'

# Create Preauthenticated Request for Entire Bucket
- name: Create Preauthenticated Request for a specific Object and permit writes to the object
  oci_preauthenticated_request:
    namespace_name: 'us-example-1'
    bucket_name: 'ansible_bucket'
    object_name: 'ansible_object'
    name: 'ansible_object_par'
    access_type: 'ObjectWrite'
    time_expires: '2018-12-22T00:00:00+00:00'
    state: 'present'

# Delete Preauthenticated Request
- name: Delete an existing Preauthenticated Request
  oci_preauthenticated_request:
    namespace_name: 'us-example-1'
    bucket_name: 'ansible_bucket'
    par_id: 'fEbFqu0/thO3JqpA/MRVbD/BpE='
    state: 'absent'
"""

RETURN = """
    preauthenticated_request:
        description: Attributes of the created Preauthenticated Request. For delete, deleted Preauthenticated Request
                     description will be returned.
        returned: success
        type: complex
        contains:
            name:
                description: The user-provided name of the pre-authenticated request.
                returned: always
                type: string
                sample: ansible_bucker_par
            id:
                description: Identifier of the Preauthenticated Request
                returned: always
                type: string
                sample: fEbFqu0/thO3JqpA/MRVbD/BpE=
            access_uri:
                description: The URI to embed in the URL when using the pre-authenticated request.
                returned: always
                type: string
                sample: /p/TF0WATak6uM7AU4PXA/n/us-example-1/b/ansible_bucket/o/
            object_name:
                description: The name of the object that is being granted access to by the
                             pre-authenticated request.
                returned: always
                type: string
                sample: ansible_object
            access_type:
                description: The collection of rules for routing destination IPs to network devices.
                returned: always
                type: string
                sample: AnyObjectWrite
            time_expires:
                description: The expiration date for the pre-authenticated request as per RFC 3339.
                returned: always
                type: datetime
                sample: 2018-12-22T00:00:00+00:00
            time_created:
                description: The date when the pre-authenticated request was created as per specification
                             RFC 3339.
                returned: always
                type: datetime
                sample: 2018-12-22T12:04:02.229000+00:00
        sample: {
                   "access_type":"AnyObjectWrite",
                   "access_uri":"/p/TF0WATak/n/us-example-1/b/ansible_bucket/o/ansible_object",
                   "id":"EbFqu0/thO3/MRVb/XmZ0iaT6IA=",
                   "name":"ansible_bucket_par",
                   "object_name":"ansible_object",
                   "time_created":"2018-12-22T12:04:02.229000+00:00",
                   "time_expires":"2018-12-23T17:31:35+00:00"
                }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.object_storage.object_storage_client import ObjectStorageClient
    from oci.exceptions import ServiceError, ClientError
    from oci.object_storage.models import CreatePreauthenticatedRequestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def create_preauthenticated_request(object_storage_client, module):
    create_preauthenticated_request_details = CreatePreauthenticatedRequestDetails()
    for attribute in create_preauthenticated_request_details.attribute_map:
        create_preauthenticated_request_details.__setattr__(
            attribute, module.params.get(attribute)
        )
    result = oci_utils.create_resource(
        resource_type="preauthenticated_request",
        create_fn=object_storage_client.create_preauthenticated_request,
        kwargs_create={
            "namespace_name": module.params.get("namespace_name"),
            "bucket_name": module.params.get("bucket_name"),
            "create_preauthenticated_request_details": create_preauthenticated_request_details,
        },
        module=module,
    )
    return result


def delete_preauthenticated_request(object_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="preauthenticated_request",
        client=object_storage_client,
        get_fn=object_storage_client.get_preauthenticated_request,
        kwargs_get={
            "par_id": module.params["par_id"],
            "namespace_name": module.params.get("namespace_name"),
            "bucket_name": module.params.get("bucket_name"),
        },
        delete_fn=object_storage_client.delete_preauthenticated_request,
        kwargs_delete={
            "par_id": module.params["par_id"],
            "namespace_name": module.params.get("namespace_name"),
            "bucket_name": module.params.get("bucket_name"),
        },
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_preauthenticated_request")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            par_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False, aliases=["display_name"]),
            object_name=dict(type="str", required=False),
            time_expires=dict(type="str", required=False),
            access_type=dict(
                type="str",
                required=False,
                choices=[
                    "ObjectRead",
                    "ObjectWrite",
                    "ObjectReadWrite",
                    "AnyObjectWrite",
                ],
            ),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    object_storage_client = oci_utils.create_service_client(module, ObjectStorageClient)
    state = module.params["state"]

    if state == "present":
        try:
            result = oci_utils.check_and_create_resource(
                resource_type="preauthenticated_request",
                create_fn=create_preauthenticated_request,
                kwargs_create={
                    "object_storage_client": object_storage_client,
                    "module": module,
                },
                list_fn=object_storage_client.list_preauthenticated_requests,
                kwargs_list={
                    "namespace_name": module.params.get("namespace_name"),
                    "bucket_name": module.params.get("bucket_name"),
                },
                module=module,
                model=CreatePreauthenticatedRequestDetails(),
            )
        except ServiceError as ex:
            get_logger().error(
                "Unable to create Preauthenticated Request due to: %s", ex.message
            )
            module.fail_json(msg=ex.message)
        except ClientError as ex:
            get_logger().error(
                "Unable to create Preauthenticated Request due to: %s", str(ex)
            )
            module.fail_json(msg=str(ex))
    elif state == "absent":
        result = delete_preauthenticated_request(object_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
