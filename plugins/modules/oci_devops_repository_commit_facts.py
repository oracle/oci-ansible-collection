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
module: oci_devops_repository_commit_facts
short_description: Fetches details about one or multiple RepositoryCommit resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RepositoryCommit resources in Oracle Cloud Infrastructure
    - Returns a list of commits.
    - If I(commit_id) is specified, the details of a single RepositoryCommit will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        required: true
    commit_id:
        description:
            - A filter to return only resources that match the given commit ID.
            - Required to get a specific repository_commit.
        type: str
        aliases: ["id"]
    ref_name:
        description:
            - A filter to return only resources that match the given reference name.
        type: str
    exclude_ref_name:
        description:
            - A filter to exclude commits that match the given reference name.
        type: str
    file_path:
        description:
            - A filter to return only commits that affect any of the specified paths.
        type: str
    timestamp_greater_than_or_equal_to:
        description:
            - A filter to return commits only created after the specified timestamp value.
        type: str
    timestamp_less_than_or_equal_to:
        description:
            - A filter to return commits only created before the specified timestamp value.
        type: str
    commit_message:
        description:
            - A filter to return any commits that contains the given message.
        type: str
    author_name:
        description:
            - A filter to return any commits that are pushed by the requested author.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific repository_commit
  oci_devops_repository_commit_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    commit_id: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"

- name: List repository_commits
  oci_devops_repository_commit_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ref_name: ref_name_example
    exclude_ref_name: exclude_ref_name_example
    file_path: file_path_example
    timestamp_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    timestamp_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    commit_message: commit_message_example
    author_name: author_name_example

"""

RETURN = """
repository_commits:
    description:
        - List of RepositoryCommit resources
    returned: on success
    type: complex
    contains:
        commit_id:
            description:
                - Commit hash pointed to by reference name.
            returned: on success
            type: str
            sample: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
        commit_message:
            description:
                - The commit message.
            returned: on success
            type: str
            sample: commit_message_example
        author_name:
            description:
                - Name of the author of the repository.
            returned: on success
            type: str
            sample: author_name_example
        author_email:
            description:
                - Email of the author of the repository.
            returned: on success
            type: str
            sample: author_email_example
        committer_name:
            description:
                - Name of who creates the commit.
            returned: on success
            type: str
            sample: committer_name_example
        committer_email:
            description:
                - Email of who creates the commit.
            returned: on success
            type: str
            sample: committer_email_example
        parent_commit_ids:
            description:
                - An array of parent commit IDs of created commit.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time at which commit was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        tree_id:
            description:
                - Tree information for the specified commit.
            returned: on success
            type: str
            sample: "ocid1.tree.oc1..xxxxxxEXAMPLExxxxxx"
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
        "commit_message": "commit_message_example",
        "author_name": "author_name_example",
        "author_email": "author_email_example",
        "committer_name": "committer_name_example",
        "committer_email": "committer_email_example",
        "parent_commit_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "tree_id": "ocid1.tree.oc1..xxxxxxEXAMPLExxxxxx",
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


class RepositoryCommitFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "commit_id",
        ]

    def get_required_params_for_list(self):
        return [
            "repository_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_commit,
            repository_id=self.module.params.get("repository_id"),
            commit_id=self.module.params.get("commit_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "ref_name",
            "exclude_ref_name",
            "file_path",
            "timestamp_greater_than_or_equal_to",
            "timestamp_less_than_or_equal_to",
            "commit_message",
            "author_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_commits,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


RepositoryCommitFactsHelperCustom = get_custom_class(
    "RepositoryCommitFactsHelperCustom"
)


class ResourceFactsHelper(
    RepositoryCommitFactsHelperCustom, RepositoryCommitFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(type="str", required=True),
            commit_id=dict(aliases=["id"], type="str"),
            ref_name=dict(type="str"),
            exclude_ref_name=dict(type="str"),
            file_path=dict(type="str"),
            timestamp_greater_than_or_equal_to=dict(type="str"),
            timestamp_less_than_or_equal_to=dict(type="str"),
            commit_message=dict(type="str"),
            author_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_commit",
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

    module.exit_json(repository_commits=result)


if __name__ == "__main__":
    main()
