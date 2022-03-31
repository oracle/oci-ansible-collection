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
module: oci_devops_repository_ref
short_description: Manage a RepositoryRef resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a RepositoryRef resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    object_id:
        description:
            - SHA-1 hash value of the object pointed to by the tag.
            - This parameter is updatable.
            - Required when ref_type is 'TAG'
        type: str
    ref_type:
        description:
            - The type of reference (Branch or Tag).
            - Required for update using I(state=present) with ref_name present.
        type: str
        choices:
            - "TAG"
            - "BRANCH"
    commit_id:
        description:
            - Commit ID pointed to by the new branch.
            - This parameter is updatable.
            - Required when ref_type is 'BRANCH'
        type: str
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        required: true
    ref_name:
        description:
            - A filter to return only resources that match the given reference name.
        type: str
        required: true
    state:
        description:
            - The state of the RepositoryRef.
            - Use I(state=present) to update an existing a RepositoryRef.
            - Use I(state=absent) to delete a RepositoryRef.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update repository_ref with ref_type = TAG
  oci_devops_repository_ref:
    # required
    object_id: "ocid1.object.oc1..xxxxxxEXAMPLExxxxxx"
    ref_type: TAG

- name: Update repository_ref with ref_type = BRANCH
  oci_devops_repository_ref:
    # required
    ref_type: BRANCH
    commit_id: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete repository_ref
  oci_devops_repository_ref:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    ref_name: ref_name_example
    state: absent

"""

RETURN = """
repository_ref:
    description:
        - Details of the RepositoryRef resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        commit_id:
            description:
                - Commit ID pointed to by the new branch.
            returned: on success
            type: str
            sample: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
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
        object_id:
            description:
                - SHA-1 hash value of the object pointed to by the tag.
            returned: on success
            type: str
            sample: "ocid1.object.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "commit_id": "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx",
        "ref_name": "ref_name_example",
        "ref_type": "BRANCH",
        "full_ref_name": "full_ref_name_example",
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "object_id": "ocid1.object.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.devops.models import PutRepositoryRefDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RepositoryRefHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RepositoryRefHelperGen, self).get_possible_entity_types() + [
            "repositoryref",
            "repositoryreves",
            "devopsrepositoryref",
            "devopsrepositoryreves",
            "repositoryrefresource",
            "repositoryrevesresource",
            "ref",
            "reves",
            "devopsref",
            "devopsreves",
            "refresource",
            "revesresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "ref_name"

    def get_module_resource_id(self):
        return self.module.params.get("ref_name")

    def get_get_fn(self):
        return self.client.get_ref

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_ref,
            ref_name=summary_model.ref_name,
            repository_id=self.module.params.get("repository_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ref,
            repository_id=self.module.params.get("repository_id"),
            ref_name=self.module.params.get("ref_name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "repository_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["ref_type", "commit_id", "ref_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_refs, **kwargs)

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return PutRepositoryRefDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.put_repository_ref,
            call_fn_args=(),
            call_fn_kwargs=dict(
                repository_id=self.module.params.get("repository_id"),
                ref_name=self.module.params.get("ref_name"),
                put_repository_ref_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ref,
            call_fn_args=(),
            call_fn_kwargs=dict(
                repository_id=self.module.params.get("repository_id"),
                ref_name=self.module.params.get("ref_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RepositoryRefHelperCustom = get_custom_class("RepositoryRefHelperCustom")


class ResourceHelper(RepositoryRefHelperCustom, RepositoryRefHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            object_id=dict(type="str"),
            ref_type=dict(type="str", choices=["TAG", "BRANCH"]),
            commit_id=dict(type="str"),
            repository_id=dict(type="str", required=True),
            ref_name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="repository_ref",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
