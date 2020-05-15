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
module: oci_object_storage_preauthenticated_request_facts
short_description: Fetches details about one or multiple PreauthenticatedRequest resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PreauthenticatedRequest resources in Oracle Cloud Infrastructure
    - Lists pre-authenticated requests for the bucket.
    - If I(par_id) is specified, the details of a single PreauthenticatedRequest will be returned.
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
    par_id:
        description:
            - The unique identifier for the pre-authenticated request. This can be used to manage operations against
              the pre-authenticated request, such as GET or DELETE.
            - Required to get a specific preauthenticated_request.
        type: str
        aliases: ["id"]
    object_name_prefix:
        description:
            - User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.
        type: str
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List preauthenticated_requests
  oci_object_storage_preauthenticated_request_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

- name: Get a specific preauthenticated_request
  oci_object_storage_preauthenticated_request_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    par_id: ocid1.par.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
preauthenticated_requests:
    description:
        - List of PreauthenticatedRequest resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier to use when directly addressing the pre-authenticated request.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The user-provided name of the pre-authenticated request.
            returned: on success
            type: string
            sample: name_example
        object_name:
            description:
                - The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is,
                  the pre-authenticated request grants access to the entire bucket.
            returned: on success
            type: string
            sample: object_name_example
        access_type:
            description:
                - The operation that can be performed on this resource.
            returned: on success
            type: string
            sample: ObjectRead
        time_expires:
            description:
                - The expiration date for the pre-authenticated request as per L(RFC 3339,https://tools.ietf.org/html/rfc3339). After this date the pre-
                  authenticated request will no longer be valid.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_created:
            description:
                - The date when the pre-authenticated request was created as per L(RFC 3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "object_name": "object_name_example",
        "access_type": "ObjectRead",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class PreauthenticatedRequestFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "bucket_name",
            "par_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_preauthenticated_request,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            par_id=self.module.params.get("par_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "object_name_prefix",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_preauthenticated_requests,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )


PreauthenticatedRequestFactsHelperCustom = get_custom_class(
    "PreauthenticatedRequestFactsHelperCustom"
)


class ResourceFactsHelper(
    PreauthenticatedRequestFactsHelperCustom, PreauthenticatedRequestFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            par_id=dict(aliases=["id"], type="str"),
            object_name_prefix=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="preauthenticated_request",
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

    module.exit_json(preauthenticated_requests=result)


if __name__ == "__main__":
    main()
