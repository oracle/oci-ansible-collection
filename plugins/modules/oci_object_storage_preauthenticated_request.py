#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_object_storage_preauthenticated_request
short_description: Manage a PreauthenticatedRequest resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a PreauthenticatedRequest resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a pre-authenticated request specific to the bucket.
version_added: "2.9.0"
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
    name:
        description:
            - A user-specified name for the pre-authenticated request. Names can be helpful in managing pre-authenticated requests.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    bucket_listing_action:
        description:
            - "Specifies whether a list operation is allowed on a PAR with accessType \\"AnyObjectRead\\" or \\"AnyObjectReadWrite\\".
              Deny: Prevents the user from performing a list operation.
              ListObjects: Authorizes the user to perform a list operation."
        type: str
    object_name:
        description:
            - The name of the object that is being granted access to by the pre-authenticated request. Avoid entering confidential
              information. The object name can be null and if so, the pre-authenticated request grants access to the entire bucket
              if the access type allows that. The object name can be a prefix as well, in that case pre-authenticated request
              grants access to all the objects within the bucket starting with that prefix provided that we have the correct access type.
        type: str
    access_type:
        description:
            - The operation that can be performed on this resource.
            - Required for create using I(state=present).
        type: str
        choices:
            - "ObjectRead"
            - "ObjectWrite"
            - "ObjectReadWrite"
            - "AnyObjectWrite"
            - "AnyObjectRead"
            - "AnyObjectReadWrite"
    time_expires:
        description:
            - The expiration date for the pre-authenticated request as per L(RFC 3339,https://tools.ietf.org/html/rfc3339).
              After this date the pre-authenticated request will no longer be valid.
            - Required for create using I(state=present).
        type: str
    par_id:
        description:
            - The unique identifier for the pre-authenticated request. This can be used to manage operations against
              the pre-authenticated request, such as GET or DELETE.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PreauthenticatedRequest.
            - Use I(state=present) to create a PreauthenticatedRequest.
            - Use I(state=absent) to delete a PreauthenticatedRequest.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create preauthenticated_request
  oci_object_storage_preauthenticated_request:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    name: name_example
    access_type: ObjectRead
    time_expires: 2013-10-20T19:20:30+01:00

    # optional
    bucket_listing_action: bucket_listing_action_example
    object_name: object_name_example

- name: Delete preauthenticated_request
  oci_object_storage_preauthenticated_request:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    par_id: "ocid1.par.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete preauthenticated_request using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_object_storage_preauthenticated_request:
    # required
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    name: name_example
    state: absent

"""

RETURN = """
preauthenticated_request:
    description:
        - Details of the PreauthenticatedRequest resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier to use when directly addressing the pre-authenticated request.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The user-provided name of the pre-authenticated request.
            returned: on success
            type: str
            sample: name_example
        object_name:
            description:
                - The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is,
                  the pre-authenticated request grants access to the entire bucket.
            returned: on success
            type: str
            sample: object_name_example
        bucket_listing_action:
            description:
                - "Specifies whether a list operation is allowed on a PAR with accessType \\"AnyObjectRead\\" or \\"AnyObjectReadWrite\\".
                  Deny: Prevents the user from performing a list operation.
                  ListObjects: Authorizes the user to perform a list operation."
            returned: on success
            type: str
            sample: bucket_listing_action_example
        access_type:
            description:
                - The operation that can be performed on this resource.
            returned: on success
            type: str
            sample: ObjectRead
        time_expires:
            description:
                - The expiration date for the pre-authenticated request as per L(RFC 3339,https://tools.ietf.org/html/rfc3339). After this date the pre-
                  authenticated request will no longer be valid.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date when the pre-authenticated request was created as per L(RFC 3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "object_name": "object_name_example",
        "bucket_listing_action": "bucket_listing_action_example",
        "access_type": "ObjectRead",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.object_storage.models import CreatePreauthenticatedRequestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PreauthenticatedRequestHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "par_id"

    def get_module_resource_id(self):
        return self.module.params.get("par_id")

    def get_get_fn(self):
        return self.client.get_preauthenticated_request

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_preauthenticated_request,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            par_id=self.module.params.get("par_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "bucket_name",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_preauthenticated_requests, **kwargs
        )

    def get_create_model_class(self):
        return CreatePreauthenticatedRequestDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_preauthenticated_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                create_preauthenticated_request_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_preauthenticated_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                par_id=self.module.params.get("par_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PreauthenticatedRequestHelperCustom = get_custom_class(
    "PreauthenticatedRequestHelperCustom"
)


class ResourceHelper(
    PreauthenticatedRequestHelperCustom, PreauthenticatedRequestHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            name=dict(type="str"),
            bucket_listing_action=dict(type="str"),
            object_name=dict(type="str"),
            access_type=dict(
                type="str",
                choices=[
                    "ObjectRead",
                    "ObjectWrite",
                    "ObjectReadWrite",
                    "AnyObjectWrite",
                    "AnyObjectRead",
                    "AnyObjectReadWrite",
                ],
            ),
            time_expires=dict(type="str"),
            par_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="preauthenticated_request",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
