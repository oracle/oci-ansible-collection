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
module: oci_devops_diff_facts
short_description: Fetches details about one or multiple Diff resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Diff resources in Oracle Cloud Infrastructure
    - Compares two revisions and lists the differences. Supports comparison between two refs or commits.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - unique Repository identifier.
        type: str
        required: true
    base_version:
        description:
            - The commit or ref name to compare changes against
        type: str
        required: true
    target_version:
        description:
            - The commit or ref name where changes are coming from
        type: str
        required: true
    is_comparison_from_merge_base:
        description:
            - boolean for whether to use merge base or most recent revision
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List diffs
  oci_devops_diff_facts:
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    base_version: base_version_example
    target_version: target_version_example

"""

RETURN = """
diffs:
    description:
        - List of Diff resources
    returned: on success
    type: complex
    contains:
        old_path:
            description:
                - The path on the baseVersion to the changed object.
            returned: on success
            type: str
            sample: old_path_example
        new_path:
            description:
                - The path on the targetVersion to the changed object.
            returned: on success
            type: str
            sample: new_path_example
        old_id:
            description:
                - The ID of the changed object on the baseVersion.
            returned: on success
            type: str
            sample: "ocid1.old.oc1..xxxxxxEXAMPLExxxxxx"
        new_id:
            description:
                - The ID of the changed object on the targetVersion.
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
                        - List of DiffSection.
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
                                        - Indicates whether a line in a conflicted section of the diff is from the base version, the target version, or if its
                                          just a marker indicating the beginning, middle, or end of a conflicted section.
                                    returned: on success
                                    type: str
                                    sample: BASE
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
        }],
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


class DiffFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "repository_id",
            "base_version",
            "target_version",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "is_comparison_from_merge_base",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_commit_diffs,
            repository_id=self.module.params.get("repository_id"),
            base_version=self.module.params.get("base_version"),
            target_version=self.module.params.get("target_version"),
            **optional_kwargs
        )


DiffFactsHelperCustom = get_custom_class("DiffFactsHelperCustom")


class ResourceFactsHelper(DiffFactsHelperCustom, DiffFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(type="str", required=True),
            base_version=dict(type="str", required=True),
            target_version=dict(type="str", required=True),
            is_comparison_from_merge_base=dict(type="bool"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="diff",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(diffs=result)


if __name__ == "__main__":
    main()
