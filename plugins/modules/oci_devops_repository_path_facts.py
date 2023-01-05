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
module: oci_devops_repository_path_facts
short_description: Fetches details about one or multiple RepositoryPath resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RepositoryPath resources in Oracle Cloud Infrastructure
    - Retrieves a list of files and directories in a repository.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        required: true
    ref:
        description:
            - "The name of branch/tag or commit hash it points to. If names conflict, order of preference is commit > branch > tag.
              You can disambiguate with \\"heads/foobar\\" and \\"tags/foobar\\". If left blank repository's default branch will be used."
        type: str
    paths_in_subtree:
        description:
            - Flag to determine if files must be retrived recursively. Flag is False by default.
        type: bool
    folder_path:
        description:
            - The fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to
              a folder named examples that was created off of the root directory (/) of a repository.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
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
            - The field to sort by. Only one sort order may be provided. Default order is ascending. If no value is specified name is default.
        type: str
        choices:
            - "type"
            - "sizeInBytes"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List repository_paths
  oci_devops_repository_path_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ref: ref_example
    paths_in_subtree: true
    folder_path: folder_path_example
    display_name: display_name_example
    sort_order: ASC
    sort_by: type

"""

RETURN = """
repository_paths:
    description:
        - List of RepositoryPath resources
    returned: on success
    type: complex
    contains:
        type:
            description:
                - File or directory.
            returned: on success
            type: str
            sample: type_example
        size_in_bytes:
            description:
                - Size of file or directory.
            returned: on success
            type: int
            sample: 56
        name:
            description:
                - Name of file or directory.
            returned: on success
            type: str
            sample: name_example
        path:
            description:
                - Path to file or directory in a repository.
            returned: on success
            type: str
            sample: path_example
        sha:
            description:
                - SHA-1 checksum of blob or tree.
            returned: on success
            type: str
            sample: sha_example
        submodule_git_url:
            description:
                - The git URL of the submodule.
            returned: on success
            type: str
            sample: submodule_git_url_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "type": "type_example",
        "size_in_bytes": 56,
        "name": "name_example",
        "path": "path_example",
        "sha": "sha_example",
        "submodule_git_url": "submodule_git_url_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
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


class RepositoryPathFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "repository_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "ref",
            "paths_in_subtree",
            "folder_path",
            "display_name",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_paths,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


RepositoryPathFactsHelperCustom = get_custom_class("RepositoryPathFactsHelperCustom")


class ResourceFactsHelper(
    RepositoryPathFactsHelperCustom, RepositoryPathFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(type="str", required=True),
            ref=dict(type="str"),
            paths_in_subtree=dict(type="bool"),
            folder_path=dict(type="str"),
            display_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["type", "sizeInBytes", "name"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_path",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(repository_paths=result)


if __name__ == "__main__":
    main()
