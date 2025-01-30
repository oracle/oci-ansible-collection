#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_devops_repo_file_lines_facts
short_description: Fetches details about a RepoFileLines resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a RepoFileLines resource in Oracle Cloud Infrastructure
    - Retrieve lines of a specified file. Supports starting line number and limit.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        aliases: ["id"]
        required: true
    revision:
        description:
            - Retrieve file lines from specific revision.
        type: str
        required: true
    file_path:
        description:
            - A filter to return only commits that affect any of the specified paths.
        type: str
    start_line_number:
        description:
            - Line number from where to start returning file lines.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific repo_file_lines
  oci_devops_repo_file_lines_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    revision: revision_example

    # optional
    file_path: file_path_example
    start_line_number: 1

"""

RETURN = """
repo_file_lines:
    description:
        - RepoFileLines resource
    returned: on success
    type: complex
    contains:
        lines:
            description:
                - The list of lines in the file.
            returned: on success
            type: complex
            contains:
                line_number:
                    description:
                        - The line number.
                    returned: on success
                    type: int
                    sample: 56
                line_content:
                    description:
                        - The content of the line.
                    returned: on success
                    type: str
                    sample: line_content_example
    sample: {
        "lines": [{
            "line_number": 56,
            "line_content": "line_content_example"
        }]
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


class DevopsRepoFileLinesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "revision",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "file_path",
            "start_line_number",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_repo_file_lines,
            repository_id=self.module.params.get("repository_id"),
            revision=self.module.params.get("revision"),
            **optional_kwargs
        )


DevopsRepoFileLinesFactsHelperCustom = get_custom_class(
    "DevopsRepoFileLinesFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsRepoFileLinesFactsHelperCustom, DevopsRepoFileLinesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str", required=True),
            revision=dict(type="str", required=True),
            file_path=dict(type="str"),
            start_line_number=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repo_file_lines",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(repo_file_lines=result)


if __name__ == "__main__":
    main()
