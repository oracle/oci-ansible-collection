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
module: oci_devops_diff_response_facts
short_description: Fetches details about a DiffResponse resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a DiffResponse resource in Oracle Cloud Infrastructure
    - Compares two revisions for their differences. Supports comparison between two references or commits.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        aliases: ["id"]
        required: true
    target_version:
        description:
            - The commit or reference name where changes are coming from.
        type: str
        required: true
    base_version:
        description:
            - The commit or reference name to compare changes against. If base version is not provided, the difference goes against an empty tree.
        type: str
    is_comparison_from_merge_base:
        description:
            - Boolean value to indicate whether to use merge base or most recent revision.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific diff_response
  oci_devops_diff_response_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    target_version: target_version_example

    # optional
    base_version: base_version_example
    is_comparison_from_merge_base: true

"""

RETURN = """
diff_response:
    description:
        - DiffResponse resource
    returned: on success
    type: complex
    contains:
        are_all_changes_included:
            description:
                - Boolean value to indicate if all changes are included in the response.
            returned: on success
            type: bool
            sample: true
        change_type_count:
            description:
                - Count of each type of change in difference.
            returned: on success
            type: dict
            sample: {}
        common_commit:
            description:
                - The ID of the common commit between source and target.
            returned: on success
            type: str
            sample: common_commit_example
        commits_ahead_count:
            description:
                - The number of commits source is ahead of target by.
            returned: on success
            type: int
            sample: 56
        commits_behind_count:
            description:
                - The number of commits source is behind target by.
            returned: on success
            type: int
            sample: 56
        added_lines_count:
            description:
                - The number of lines added in whole difference.
            returned: on success
            type: int
            sample: 56
        deleted_lines_count:
            description:
                - The number of lines deleted in whole difference.
            returned: on success
            type: int
            sample: 56
        changes:
            description:
                - List of changes in the difference.
            returned: on success
            type: complex
            contains:
                change_type:
                    description:
                        - Type of change made to file.
                    returned: on success
                    type: str
                    sample: change_type_example
                object_type:
                    description:
                        - The type of the changed object.
                    returned: on success
                    type: str
                    sample: object_type_example
                commit_id:
                    description:
                        - The ID of the commit where the change is coming from.
                    returned: on success
                    type: str
                    sample: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
                old_path:
                    description:
                        - The path on the target to the changed object.
                    returned: on success
                    type: str
                    sample: old_path_example
                new_path:
                    description:
                        - The path on the source to the changed object.
                    returned: on success
                    type: str
                    sample: new_path_example
                old_id:
                    description:
                        - The ID of the changed object on the target.
                    returned: on success
                    type: str
                    sample: "ocid1.old.oc1..xxxxxxEXAMPLExxxxxx"
                new_id:
                    description:
                        - The ID of the changed object on the source.
                    returned: on success
                    type: str
                    sample: "ocid1.new.oc1..xxxxxxEXAMPLExxxxxx"
                url:
                    description:
                        - The URL of the changed object.
                    returned: on success
                    type: str
                    sample: url_example
                added_lines_count:
                    description:
                        - The number of lines added in whole difference.
                    returned: on success
                    type: int
                    sample: 56
                deleted_lines_count:
                    description:
                        - The number of lines deleted in whole difference.
                    returned: on success
                    type: int
                    sample: 56
                are_conflicts_in_file:
                    description:
                        - Indicates whether the changed file contains conflicts.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "are_all_changes_included": true,
        "change_type_count": {},
        "common_commit": "common_commit_example",
        "commits_ahead_count": 56,
        "commits_behind_count": 56,
        "added_lines_count": 56,
        "deleted_lines_count": 56,
        "changes": [{
            "change_type": "change_type_example",
            "object_type": "object_type_example",
            "commit_id": "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx",
            "old_path": "old_path_example",
            "new_path": "new_path_example",
            "old_id": "ocid1.old.oc1..xxxxxxEXAMPLExxxxxx",
            "new_id": "ocid1.new.oc1..xxxxxxEXAMPLExxxxxx",
            "url": "url_example",
            "added_lines_count": 56,
            "deleted_lines_count": 56,
            "are_conflicts_in_file": true
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


class DiffResponseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "target_version",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "base_version",
            "is_comparison_from_merge_base",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_commit_diff,
            repository_id=self.module.params.get("repository_id"),
            target_version=self.module.params.get("target_version"),
            **optional_kwargs
        )


DiffResponseFactsHelperCustom = get_custom_class("DiffResponseFactsHelperCustom")


class ResourceFactsHelper(DiffResponseFactsHelperCustom, DiffResponseFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str", required=True),
            target_version=dict(type="str", required=True),
            base_version=dict(type="str"),
            is_comparison_from_merge_base=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="diff_response",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(diff_response=result)


if __name__ == "__main__":
    main()
