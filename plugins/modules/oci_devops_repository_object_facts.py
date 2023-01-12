#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_devops_repository_object_facts
short_description: Fetches details about a RepositoryObject resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a RepositoryObject resource in Oracle Cloud Infrastructure
    - Retrieves blob of specific branch name/commit ID and file path.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        aliases: ["id"]
        required: true
    file_path:
        description:
            - A filter to return only commits that affect any of the specified paths.
        type: str
    ref_name:
        description:
            - A filter to return only resources that match the given reference name.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific repository_object
  oci_devops_repository_object_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    file_path: file_path_example
    ref_name: ref_name_example

"""

RETURN = """
repository_object:
    description:
        - RepositoryObject resource
    returned: on success
    type: complex
    contains:
        type:
            description:
                - The type of git object.
            returned: on success
            type: str
            sample: BLOB
        size_in_bytes:
            description:
                - Size in bytes.
            returned: on success
            type: int
            sample: 56
        sha:
            description:
                - SHA-1 hash of git object.
            returned: on success
            type: str
            sample: sha_example
        is_binary:
            description:
                - Flag to determine if the object contains binary file content or not.
            returned: on success
            type: bool
            sample: true
    sample: {
        "type": "BLOB",
        "size_in_bytes": 56,
        "sha": "sha_example",
        "is_binary": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsRepositoryObjectFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "file_path",
            "ref_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_object,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


DevopsRepositoryObjectFactsHelperCustom = get_custom_class(
    "DevopsRepositoryObjectFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsRepositoryObjectFactsHelperCustom, DevopsRepositoryObjectFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str", required=True),
            file_path=dict(type="str"),
            ref_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_object",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(repository_object=result)


if __name__ == "__main__":
    main()
