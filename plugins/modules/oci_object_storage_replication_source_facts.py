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
module: oci_object_storage_replication_source_facts
short_description: Fetches details about one or multiple ReplicationSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ReplicationSource resources in Oracle Cloud Infrastructure
    - List the replication sources of a destination bucket.
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
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List replication_sources
  oci_object_storage_replication_source_facts:
    namespace_name: namespace_name_example
    bucket_name: my-new-bucket1

"""

RETURN = """
replication_sources:
    description:
        - List of ReplicationSource resources
    returned: on success
    type: complex
    contains:
        policy_name:
            description:
                - The name of the policy.
            returned: on success
            type: string
            sample: policy_name_example
        source_region_name:
            description:
                - "The source region replicating data from, for example \\"us-ashburn-1\\"."
            returned: on success
            type: string
            sample: source_region_name_example
        source_bucket_name:
            description:
                - The source bucket replicating data from.
            returned: on success
            type: string
            sample: source_bucket_name_example
    sample: [{
        "policy_name": "policy_name_example",
        "source_region_name": "source_region_name_example",
        "source_bucket_name": "source_bucket_name_example"
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


class ReplicationSourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "bucket_name",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_replication_sources,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            **optional_kwargs
        )


ReplicationSourceFactsHelperCustom = get_custom_class(
    "ReplicationSourceFactsHelperCustom"
)


class ResourceFactsHelper(
    ReplicationSourceFactsHelperCustom, ReplicationSourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            bucket_name=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="replication_source",
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

    module.exit_json(replication_sources=result)


if __name__ == "__main__":
    main()
