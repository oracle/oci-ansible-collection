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
module: oci_devops_repository_facts
short_description: Fetches details about one or multiple Repository resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Repository resources in Oracle Cloud Infrastructure
    - Returns a list of repositories given a compartment ID or a project ID.
    - If I(repository_id) is specified, the details of a single Repository will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fields:
        description:
            - Fields parameter can contain multiple flags useful in deciding the API functionality.
        type: list
        elements: str
        choices:
            - "branchCount"
            - "commitCount"
            - "sizeInBytes"
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    project_id:
        description:
            - unique project identifier
        type: str
    repository_id:
        description:
            - Unique repository identifier.
            - Required to get a specific repository.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycle state matches the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETED"
            - "DELETING"
    name:
        description:
            - A filter to return only resources that match the entire name given.
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
            - The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for name is ascending. If
              no value is specified time created is default.
        type: str
        choices:
            - "timeCreated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific repository
  oci_devops_repository_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fields: [ "branchCount" ]

- name: List repositories
  oci_devops_repository_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    name: name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
repositories:
    description:
        - List of Repository resources
    returned: on success
    type: complex
    contains:
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecyle_details_example
        branch_count:
            description:
                - The count of the branches present in the repository.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        commit_count:
            description:
                - The count of the commits present in the repository.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        size_in_bytes:
            description:
                - The size of the repository in bytes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        trigger_build_events:
            description:
                - "Trigger build events supported for this repository:
                  PUSH - Build is triggered when a push event occurs.
                  COMMIT_UPDATES - Build is triggered when new commits are mirrored into a repository."
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - The OCID of the repository. This value is unique and immutable.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Unique name of a repository. This value is mutable.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The OCID of the repository's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project containing the repository.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - Tenancy unique namespace.
            returned: on success
            type: str
            sample: namespace_example
        project_name:
            description:
                - Unique project name in a namespace.
            returned: on success
            type: str
            sample: project_name_example
        description:
            description:
                - Details of the repository. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        default_branch:
            description:
                - The default branch of the repository.
            returned: on success
            type: str
            sample: default_branch_example
        repository_type:
            description:
                - "Type of repository:
                  MIRRORED - Repository created by mirroring an existing repository.
                  HOSTED - Repository created and hosted using OCI DevOps code repository."
            returned: on success
            type: str
            sample: MIRRORED
        ssh_url:
            description:
                - SSH URL that you use to git clone, pull and push.
            returned: on success
            type: str
            sample: ssh_url_example
        http_url:
            description:
                - HTTP URL that you use to git clone, pull and push.
            returned: on success
            type: str
            sample: http_url_example
        mirror_repository_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                connector_id:
                    description:
                        - Upstream git repository connection identifer.
                    returned: on success
                    type: str
                    sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
                repository_url:
                    description:
                        - URL of external repository you want to mirror.
                    returned: on success
                    type: str
                    sample: repository_url_example
                trigger_schedule:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        schedule_type:
                            description:
                                - "Different types of trigger schedule:
                                  NONE - No automated synchronization schedule.
                                  DEFAULT - Trigger schedule is every 30 minutes.
                                  CUSTOM - Custom triggering schedule."
                            returned: on success
                            type: str
                            sample: NONE
                        custom_schedule:
                            description:
                                - Valid if type is CUSTOM. Following RFC 5545 recurrence rules, we can specify starting time, occurrence frequency, and interval
                                  size.
                                  Example for frequency could be DAILY/WEEKLY/HOURLY or any RFC 5545 supported frequency, which is followed by start time of
                                  this window.
                                  You can control the start time with BYHOUR, BYMINUTE and BYSECONDS. It is followed by the interval size.
                            returned: on success
                            type: str
                            sample: custom_schedule_example
        time_created:
            description:
                - The time the repository was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the repository was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the repository.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "lifecyle_details": "lifecyle_details_example",
        "branch_count": 56,
        "commit_count": 56,
        "size_in_bytes": 56,
        "trigger_build_events": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "project_name": "project_name_example",
        "description": "description_example",
        "default_branch": "default_branch_example",
        "repository_type": "MIRRORED",
        "ssh_url": "ssh_url_example",
        "http_url": "http_url_example",
        "mirror_repository_config": {
            "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "trigger_schedule": {
                "schedule_type": "NONE",
                "custom_schedule": "custom_schedule_example"
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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


class DevopsRepositoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_repository,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "project_id",
            "repository_id",
            "lifecycle_state",
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_repositories, **optional_kwargs
        )


DevopsRepositoryFactsHelperCustom = get_custom_class(
    "DevopsRepositoryFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsRepositoryFactsHelperCustom, DevopsRepositoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            fields=dict(
                type="list",
                elements="str",
                choices=["branchCount", "commitCount", "sizeInBytes"],
            ),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            repository_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "CREATING", "DELETED", "DELETING"]
            ),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository",
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

    module.exit_json(repositories=result)


if __name__ == "__main__":
    main()
