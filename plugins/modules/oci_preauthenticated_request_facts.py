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
module: oci_preauthenticated_request_facts
short_description: Fetches details of existing OCI Preauthenticated Requests.
description:
    - Fetches details of all OCI Preauthenticated Requests for a specific Bucket or an OCI Preauthenticated Request
version_added: "2.5"
options:
    namespace_name:
        description: Namespace name from which details of all preauthenticated-requests must be fetched.
        required: true
    bucket_name:
        description: Bucket name from which details of all preauthenticated-requests must be fetched.
        required: true
    par_id:
        description: Identifier of the preauthenticated-request. Required if the details of a
                     specific preauthenticated-request details needs to be fetched.
        required: false
        aliases: ['id']
    object_name_prefix:
        description: User-specified object name prefixes can be used to query and return a
                     list of pre-authenticated requests.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Fetch Preauthenticated Request
- name: List all Preauthenticated Request of a Bucket
  oci_preauthenticated_request_facts:
    namespace_name: 'us-example-1'
    bucket_name: 'ansible_bucket'

# Fetch Preauthenticated Request for a specific Object
- name: List Preauthenticated Request for objects with a specified name prefix
  oci_preauthenticated_request_facts:
    namespace_name: 'us-example-1'
    bucket_name: 'ansible_bucket'
    object_name_prefix: 'ansible_object'

# Fetch a specific Preauthenticated Request
- name: List a specific Preauthenticated Request
  oci_preauthenticated_request_facts:
    namespace_name: 'us-example-1'
    bucket_name: 'ansible_bucket'
    par_id: 'fEbFqu0/thO3JqpA/MRVbD/BpE='
"""

RETURN = """
    preauthenticated_requests:
        description: Attributes of the Fetched Preauthenticated Request.
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
        sample: [{
                   "access_type":"AnyObjectWrite",
                   "id":"EbFqu0/thO3/MRVb/XmZ0iaT6IA=",
                   "name":"ansible_bucket_par",
                   "object_name":"ansible_object",
                   "time_created":"2018-12-22T12:04:02.229000+00:00",
                   "time_expires":"2018-12-23T17:31:35+00:00"
                }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.object_storage.object_storage_client import ObjectStorageClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_preauthenticated_requests(object_storage_client, module):
    result = dict(preauthenticated_requests="")
    namespace_name = module.params.get("namespace_name")
    bucket_name = module.params.get("bucket_name")
    par_id = module.params.get("par_id")
    try:
        if par_id:
            get_logger().debug("Listing Preauthenticated Request Summary of %s", par_id)
            response = oci_utils.call_with_backoff(
                object_storage_client.get_preauthenticated_request,
                namespace_name=namespace_name,
                bucket_name=bucket_name,
                par_id=par_id,
            )
            existing_preauthenticated_requests = [response.data]
        else:
            get_logger().debug(
                "Listing all Preauthenticated Request Summaries under namespace %s and bucket %s",
                namespace_name,
                bucket_name,
            )
            optional_list_method_params = ["object_name_prefix"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_preauthenticated_requests = to_dict(
                oci_utils.list_all_resources(
                    object_storage_client.list_preauthenticated_requests,
                    namespace_name=namespace_name,
                    bucket_name=bucket_name,
                    **optional_kwargs
                )
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to list Preauthenticated Requests due to %s", ex.message
        )
        module.fail_json(msg=ex.message)
    result["preauthenticated_requests"] = to_dict(existing_preauthenticated_requests)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_preauthenticated_request_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            par_id=dict(type="str", required=False, aliases=["id"]),
            object_name_prefix=dict(type=str, required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    object_storage_client = oci_utils.create_service_client(module, ObjectStorageClient)
    result = list_preauthenticated_requests(object_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
