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
module: oci_object_storage_replication_policy_facts
short_description: Fetches details about one or multiple ReplicationPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ReplicationPolicy resources in Oracle Cloud Infrastructure
    - List the replication policies associated with a bucket.
    - If I(replication_id) is specified, the details of a single ReplicationPolicy will be returned.
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
    replication_id:
        description:
            - The ID of the replication policy.
            - Required to get a specific replication_policy.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List replication_policies
  oci_object_storage_replication_policy_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

- name: Get a specific replication_policy
  oci_object_storage_replication_policy_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1
    replication_id: ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
replication_policies:
    description:
        - List of ReplicationPolicy resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The id of the replication policy.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name of the policy.
            returned: on success
            type: string
            sample: name_example
        destination_region_name:
            description:
                - "The destination region to replicate to, for example \\"us-ashburn-1\\"."
            returned: on success
            type: string
            sample: destination_region_name_example
        destination_bucket_name:
            description:
                - The bucket to replicate to in the destination region. Replication policy creation does not automatically
                  create a destination bucket. Create the destination bucket before creating the policy.
            returned: on success
            type: string
            sample: destination_bucket_name_example
        time_created:
            description:
                - The date when the replication policy was created as per L(RFC 3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_sync:
            description:
                - Changes made to the source bucket before this time has been replicated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        status:
            description:
                - The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue
                  described in the status message, the status will become ACTIVE.
            returned: on success
            type: string
            sample: ACTIVE
        status_message:
            description:
                - A human-readable description of the status.
            returned: on success
            type: string
            sample: status_message_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "destination_region_name": "destination_region_name_example",
        "destination_bucket_name": "destination_bucket_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_sync": "2013-10-20T19:20:30+01:00",
        "status": "ACTIVE",
        "status_message": "status_message_example"
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


class ReplicationPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "bucket_name",
            "replication_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_policy,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            replication_id=self.module.params.get("replication_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_replication_policies,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )


ReplicationPolicyFactsHelperCustom = get_custom_class(
    "ReplicationPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    ReplicationPolicyFactsHelperCustom, ReplicationPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
            replication_id=dict(aliases=["id"], type="str"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="replication_policy",
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

    module.exit_json(replication_policies=result)


if __name__ == "__main__":
    main()
