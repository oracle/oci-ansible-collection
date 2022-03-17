#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_devops_repository_ref_facts
short_description: Fetches details about one or multiple RepositoryRef resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RepositoryRef resources in Oracle Cloud Infrastructure
    - Returns a list of references.
    - If I(ref_name) is specified, the details of a single RepositoryRef will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        required: true
    ref_name:
        description:
            - A filter to return only resources that match the given reference name.
            - Required to get a specific repository_ref.
        type: str
    ref_type:
        description:
            - Reference type to distinguish between branch and tag. If it is not specified, all references are returned.
        type: str
        choices:
            - "BRANCH"
            - "TAG"
    commit_id:
        description:
            - Commit ID in a repository.
        type: str
    sort_order:
        description:
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for reference name is ascending. Default order for reference type is
              ascending. If no value is specified reference name is default.
        type: str
        choices:
            - "refType"
            - "refName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific repository_ref
  oci_devops_repository_ref_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    ref_name: ref_name_example

- name: List repository_reves
  oci_devops_repository_ref_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ref_name: ref_name_example
    ref_type: BRANCH
    commit_id: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: refType

"""

RETURN = """
repository_reves:
    description:
        - List of RepositoryRef resources
    returned: on success
    type: complex
    contains:
        commit_id:
            description:
                - Commit ID pointed to by the new branch.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
        object_id:
            description:
                - SHA-1 hash value of the object pointed to by the tag.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.object.oc1..xxxxxxEXAMPLExxxxxx"
        ref_name:
            description:
                - Unique reference name inside a repository.
            returned: on success
            type: str
            sample: ref_name_example
        ref_type:
            description:
                - The type of reference (Branch or Tag).
            returned: on success
            type: str
            sample: BRANCH
        full_ref_name:
            description:
                - Unique full reference name inside a repository.
            returned: on success
            type: str
            sample: full_ref_name_example
        repository_id:
            description:
                - The OCID of the repository containing the reference.
            returned: on success
            type: str
            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
                - Returned for list operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                - Returned for list operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "commit_id": "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx",
        "object_id": "ocid1.object.oc1..xxxxxxEXAMPLExxxxxx",
        "ref_name": "ref_name_example",
        "ref_type": "BRANCH",
        "full_ref_name": "full_ref_name_example",
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RepositoryRefFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "ref_name",
        ]

    def get_required_params_for_list(self):
        return [
            "repository_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ref,
            repository_id=self.module.params.get("repository_id"),
            ref_name=self.module.params.get("ref_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "ref_type",
            "commit_id",
            "ref_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_refs,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


RepositoryRefFactsHelperCustom = get_custom_class("RepositoryRefFactsHelperCustom")


class ResourceFactsHelper(RepositoryRefFactsHelperCustom, RepositoryRefFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(type="str", required=True),
            ref_name=dict(type="str"),
            ref_type=dict(type="str", choices=["BRANCH", "TAG"]),
            commit_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["refType", "refName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_ref",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(repository_reves=result)


if __name__ == "__main__":
    main()
