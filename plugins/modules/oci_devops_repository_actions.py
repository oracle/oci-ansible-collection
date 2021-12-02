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
module: oci_devops_repository_actions
short_description: Perform actions on a Repository resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Repository resource in Oracle Cloud Infrastructure
    - For I(action=mirror), synchronize a mirrored repository to the latest version from external providers
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - unique Repository identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Repository.
        type: str
        required: true
        choices:
            - "mirror"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action mirror on repository
  oci_devops_repository_actions:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    action: mirror

"""

RETURN = """
repository:
    description:
        - Details of the Repository resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
                - The OCID of the repository's Compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - Tenancy unique namespace
            returned: on success
            type: str
            sample: namespace_example
        project_id:
            description:
                - The OCID of the Project containing the repository.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        project_name:
            description:
                - Project unique Name under namespace
            returned: on success
            type: str
            sample: project_name_example
        ssh_url:
            description:
                - ssh url user utilized to git clone, pull and push
            returned: on success
            type: str
            sample: ssh_url_example
        http_url:
            description:
                - http url user utilized to git clone, pull and push
            returned: on success
            type: str
            sample: http_url_example
        description:
            description:
                - The description of this repository. Avoid entering confidential information
            returned: on success
            type: str
            sample: description_example
        default_branch:
            description:
                - The default branch of the repository
            returned: on success
            type: str
            sample: default_branch_example
        repository_type:
            description:
                - "Type of repository
                  MIRRORED - Repository was created by mirroring an existing repository.
                  HOSTED - Repository was created and hosted using OCI Devops Code Repository."
            returned: on success
            type: str
            sample: MIRRORED
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
                        - Url of external repository we'd like to mirror
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
                                - "Different types to trigger schedule
                                  - NONE - No automated sync schedule.
                                  - DEFAULT - Trigger Schedule will be every 30 minutes.
                                  - CUSTOM - Custom triggering schedule."
                            returned: on success
                            type: str
                            sample: NONE
                        custom_schedule:
                            description:
                                - Valid if type is CUSTOM. Following RFC 5545 recurrence rules, we can specify starting time, occurrence frequency, and interval
                                  size.
                                  Example for frequency could be DAILY/WEEKLY/HOURLY or any RFC 5545 supported frequency, which is followed by start time of
                                  this window, we can
                                  control the start time with BYHOUR, BYMINUTE and BYSECONDS. It is followed by the interval size.
                            returned: on success
                            type: str
                            sample: custom_schedule_example
        time_created:
            description:
                - The time the the Repository was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Repository was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Repository.
            returned: on success
            type: str
            sample: ACTIVE
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
        branch_count:
            description:
                - The count of the branches present in the repository.
            returned: on success
            type: int
            sample: 56
        commit_count:
            description:
                - The count of the commits present in the repository.
            returned: on success
            type: int
            sample: 56
        size_in_bytes:
            description:
                - The size of the repository in bytes.
            returned: on success
            type: int
            sample: 56
        trigger_build_events:
            description:
                - "Trigger Build Events supported for this repository
                  PUSH - Build is triggered when a push event occurs
                  COMMIT_UPDATES - Build is triggered when new commits are mirrored into repository"
            returned: on success
            type: list
            sample: []
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "project_name": "project_name_example",
        "ssh_url": "ssh_url_example",
        "http_url": "http_url_example",
        "description": "description_example",
        "default_branch": "default_branch_example",
        "repository_type": "MIRRORED",
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
        "lifecyle_details": "lifecyle_details_example",
        "branch_count": 56,
        "commit_count": 56,
        "size_in_bytes": 56,
        "trigger_build_events": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RepositoryActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        mirror
    """

    @staticmethod
    def get_module_resource_id_param():
        return "repository_id"

    def get_module_resource_id(self):
        return self.module.params.get("repository_id")

    def get_get_fn(self):
        return self.client.get_repository

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_repository,
            repository_id=self.module.params.get("repository_id"),
        )

    def mirror(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.mirror_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(repository_id=self.module.params.get("repository_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RepositoryActionsHelperCustom = get_custom_class("RepositoryActionsHelperCustom")


class ResourceHelper(RepositoryActionsHelperCustom, RepositoryActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["mirror"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="repository",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
