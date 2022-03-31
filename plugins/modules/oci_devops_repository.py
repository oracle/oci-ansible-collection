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
module: oci_devops_repository
short_description: Manage a Repository resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Repository resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new repository.
    - "This resource has the following action operations in the M(oracle.oci.oci_devops_repository_actions) module: mirror."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The OCID of the DevOps project containing the repository.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - Unique name of a repository.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    description:
        description:
            - Details of the repository. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    default_branch:
        description:
            - The default branch of the repository.
            - This parameter is updatable.
        type: str
    repository_type:
        description:
            - Type of repository.
            - This parameter is updatable.
        type: str
    mirror_repository_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            connector_id:
                description:
                    - Upstream git repository connection identifer.
                type: str
            repository_url:
                description:
                    - URL of external repository you want to mirror.
                type: str
            trigger_schedule:
                description:
                    - ""
                type: dict
                suboptions:
                    schedule_type:
                        description:
                            - "Different types of trigger schedule:
                              None - No automated synchronization schedule.
                              Default - Trigger schedule is every 30 minutes.
                              Custom - Custom triggering schedule."
                        type: str
                        choices:
                            - "NONE"
                            - "DEFAULT"
                            - "CUSTOM"
                        required: true
                    custom_schedule:
                        description:
                            - Valid if type is CUSTOM. Following RFC 5545 recurrence rules, we can specify starting time, occurrence frequency, and interval
                              size.
                              Example for frequency could be DAILY/WEEKLY/HOURLY or any RFC 5545 supported frequency, which is followed by start time of this
                              window.
                              You can control the start time with BYHOUR, BYMINUTE and BYSECONDS. It is followed by the interval size.
                        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    repository_id:
        description:
            - Unique repository identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Repository.
            - Use I(state=present) to create or update a Repository.
            - Use I(state=absent) to delete a Repository.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create repository
  oci_devops_repository:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    description: description_example
    default_branch: default_branch_example
    repository_type: repository_type_example
    mirror_repository_config:
      # optional
      connector_id: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
      repository_url: repository_url_example
      trigger_schedule:
        # required
        schedule_type: NONE

        # optional
        custom_schedule: custom_schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update repository
  oci_devops_repository:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    description: description_example
    default_branch: default_branch_example
    repository_type: repository_type_example
    mirror_repository_config:
      # optional
      connector_id: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
      repository_url: repository_url_example
      trigger_schedule:
        # required
        schedule_type: NONE

        # optional
        custom_schedule: custom_schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update repository using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_repository:
    # required
    name: name_example

    # optional
    description: description_example
    default_branch: default_branch_example
    repository_type: repository_type_example
    mirror_repository_config:
      # optional
      connector_id: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
      repository_url: repository_url_example
      trigger_schedule:
        # required
        schedule_type: NONE

        # optional
        custom_schedule: custom_schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete repository
  oci_devops_repository:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete repository using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_repository:
    # required
    name: name_example
    state: absent

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
                - The OCID of the repository's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - Tenancy unique namespace.
            returned: on success
            type: str
            sample: namespace_example
        project_id:
            description:
                - The OCID of the DevOps project containing the repository.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        project_name:
            description:
                - Unique project name in a namespace.
            returned: on success
            type: str
            sample: project_name_example
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
                  Mirrored - Repository created by mirroring an existing repository.
                  Hosted - Repository created and hosted using OCI DevOps code repository."
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
                                  None - No automated synchronization schedule.
                                  Default - Trigger schedule is every 30 minutes.
                                  Custom - Custom triggering schedule."
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
                - "Trigger build events supported for this repository:
                  Push - Build is triggered when a push event occurs.
                  Commit updates - Build is triggered when new commits are mirrored into a repository."
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient
    from oci.devops.models import CreateRepositoryDetails
    from oci.devops.models import UpdateRepositoryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RepositoryHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RepositoryHelperGen, self).get_possible_entity_types() + [
            "devopsrepository",
            "devopsrepositories",
            "devopsdevopsrepository",
            "devopsdevopsrepositories",
            "devopsrepositoryresource",
            "devopsrepositoriesresource",
            "repository",
            "repositories",
            "repositoryresource",
            "repositoriesresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "repository_id", "name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_repositories, **kwargs
        )

    def get_create_model_class(self):
        return CreateRepositoryDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(create_repository_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateRepositoryDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(
                repository_id=self.module.params.get("repository_id"),
                update_repository_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(repository_id=self.module.params.get("repository_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RepositoryHelperCustom = get_custom_class("RepositoryHelperCustom")


class ResourceHelper(RepositoryHelperCustom, RepositoryHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            name=dict(type="str"),
            description=dict(type="str"),
            default_branch=dict(type="str"),
            repository_type=dict(type="str"),
            mirror_repository_config=dict(
                type="dict",
                options=dict(
                    connector_id=dict(type="str"),
                    repository_url=dict(type="str"),
                    trigger_schedule=dict(
                        type="dict",
                        options=dict(
                            schedule_type=dict(
                                type="str",
                                required=True,
                                choices=["NONE", "DEFAULT", "CUSTOM"],
                            ),
                            custom_schedule=dict(type="str"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            repository_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
