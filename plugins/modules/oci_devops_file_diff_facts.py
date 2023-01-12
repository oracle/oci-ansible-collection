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
module: oci_devops_file_diff_facts
short_description: Fetches details about a FileDiff resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a FileDiff resource in Oracle Cloud Infrastructure
    - Gets the line-by-line difference between file on different commits.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        aliases: ["id"]
        required: true
    base_version:
        description:
            - The branch to compare changes against.
        type: str
        required: true
    target_version:
        description:
            - The branch where changes are coming from.
        type: str
        required: true
    file_path:
        description:
            - A filter to return only commits that affect any of the specified paths.
        type: str
    is_comparison_from_merge_base:
        description:
            - Boolean to indicate whether to use merge base or most recent revision.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific file_diff
  oci_devops_file_diff_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    base_version: base_version_example
    target_version: target_version_example

    # optional
    file_path: file_path_example
    is_comparison_from_merge_base: true

"""

RETURN = """
file_diff_response:
    description:
        - FileDiff resource
    returned: on success
    type: complex
    contains:
        old_path:
            description:
                - The path on the base version to the changed object.
            returned: on success
            type: str
            sample: old_path_example
        new_path:
            description:
                - The path on the target version to the changed object.
            returned: on success
            type: str
            sample: new_path_example
        old_id:
            description:
                - The ID of the changed object on the base version.
            returned: on success
            type: str
            sample: "ocid1.old.oc1..xxxxxxEXAMPLExxxxxx"
        new_id:
            description:
                - The ID of the changed object on the target version.
            returned: on success
            type: str
            sample: "ocid1.new.oc1..xxxxxxEXAMPLExxxxxx"
        are_conflicts_in_file:
            description:
                - Indicates whether the changed file contains conflicts.
            returned: on success
            type: bool
            sample: true
        is_large:
            description:
                - Indicates whether the file is large.
            returned: on success
            type: bool
            sample: true
        is_binary:
            description:
                - Indicates whether the file is binary.
            returned: on success
            type: bool
            sample: true
        changes:
            description:
                - List of changed section in the file.
            returned: on success
            type: complex
            contains:
                base_line:
                    description:
                        - Line number in base version where changes begin.
                    returned: on success
                    type: int
                    sample: 56
                base_span:
                    description:
                        - Number of lines chunk spans in base version.
                    returned: on success
                    type: int
                    sample: 56
                target_line:
                    description:
                        - Line number in target version where changes begin.
                    returned: on success
                    type: int
                    sample: 56
                target_span:
                    description:
                        - Number of lines chunk spans in target version.
                    returned: on success
                    type: int
                    sample: 56
                diff_sections:
                    description:
                        - List of difference section.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of change.
                            returned: on success
                            type: str
                            sample: type_example
                        lines:
                            description:
                                - The lines within changed section.
                            returned: on success
                            type: complex
                            contains:
                                base_line:
                                    description:
                                        - The number of a line in the base version.
                                    returned: on success
                                    type: int
                                    sample: 56
                                target_line:
                                    description:
                                        - The number of a line in the target version.
                                    returned: on success
                                    type: int
                                    sample: 56
                                line_content:
                                    description:
                                        - The contents of a line.
                                    returned: on success
                                    type: str
                                    sample: line_content_example
                                conflict_marker:
                                    description:
                                        - Indicates whether a line in a conflicted section of the difference is from the base version, the target version, or if
                                          its just a marker indicating the beginning, middle, or end of a conflicted section.
                                    returned: on success
                                    type: str
                                    sample: BASE
    sample: {
        "old_path": "old_path_example",
        "new_path": "new_path_example",
        "old_id": "ocid1.old.oc1..xxxxxxEXAMPLExxxxxx",
        "new_id": "ocid1.new.oc1..xxxxxxEXAMPLExxxxxx",
        "are_conflicts_in_file": true,
        "is_large": true,
        "is_binary": true,
        "changes": [{
            "base_line": 56,
            "base_span": 56,
            "target_line": 56,
            "target_span": 56,
            "diff_sections": [{
                "type": "type_example",
                "lines": [{
                    "base_line": 56,
                    "target_line": 56,
                    "line_content": "line_content_example",
                    "conflict_marker": "BASE"
                }]
            }]
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


class DevopsFileDiffFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "base_version",
            "target_version",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "file_path",
            "is_comparison_from_merge_base",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_repo_file_diff,
            repository_id=self.module.params.get("repository_id"),
            base_version=self.module.params.get("base_version"),
            target_version=self.module.params.get("target_version"),
            **optional_kwargs
        )


DevopsFileDiffFactsHelperCustom = get_custom_class("DevopsFileDiffFactsHelperCustom")


class ResourceFactsHelper(
    DevopsFileDiffFactsHelperCustom, DevopsFileDiffFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str", required=True),
            base_version=dict(type="str", required=True),
            target_version=dict(type="str", required=True),
            file_path=dict(type="str"),
            is_comparison_from_merge_base=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="file_diff",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(file_diff_response=result)


if __name__ == "__main__":
    main()
