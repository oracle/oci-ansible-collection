#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_data_science_model_provenance
short_description: Manage a ModelProvenance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a ModelProvenance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates provenance information for the specified model.
version_added: "2.9"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model.
        type: str
        aliases: ["id"]
        required: true
    repository_url:
        description:
            - For model reproducibility purposes. URL of the git repository associated with model training.
            - This parameter is updatable.
        type: str
    git_branch:
        description:
            - For model reproducibility purposes. Branch of the git repository associated with model training.
            - This parameter is updatable.
        type: str
    git_commit:
        description:
            - For model reproducibility purposes. Commit ID of the git repository associated with model training.
            - This parameter is updatable.
        type: str
    script_dir:
        description:
            - For model reproducibility purposes. Path to model artifacts.
            - This parameter is updatable.
        type: str
    training_script:
        description:
            - "For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\\""
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the ModelProvenance.
            - Use I(state=present) to create or update a ModelProvenance.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create model_provenance
  oci_data_science_model_provenance:
    model_id: ocid1.model.oc1..xxxxxxEXAMPLExxxxxx

- name: Update model_provenance
  oci_data_science_model_provenance:
    model_id: ocid1.model.oc1..xxxxxxEXAMPLExxxxxx
    repository_url: http://git-remote.com/my-repo

"""

RETURN = """
model_provenance:
    description:
        - Details of the ModelProvenance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        repository_url:
            description:
                - For model reproducibility purposes. URL of the git repository associated with model training.
            returned: on success
            type: string
            sample: http://git-remote.com/my-repo
        git_branch:
            description:
                - For model reproducibility purposes. Branch of the git repository associated with model training.
            returned: on success
            type: string
            sample: master
        git_commit:
            description:
                - For model reproducibility purposes. Commit ID of the git repository associated with model training.
            returned: on success
            type: string
            sample: 0978b63
        script_dir:
            description:
                - For model reproducibility purposes. Path to model artifacts.
            returned: on success
            type: string
            sample: script_dir_example
        training_script:
            description:
                - "For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\\""
            returned: on success
            type: string
            sample: model-dev/model1/model-training.ipynb
    sample: {
        "repository_url": "http://git-remote.com/my-repo",
        "git_branch": "master",
        "git_commit": "0978b63",
        "script_dir": "script_dir_example",
        "training_script": "model-dev/model1/model-training.ipynb"
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
    from oci.data_science import DataScienceClient
    from oci.data_science.models import CreateModelProvenanceDetails
    from oci.data_science.models import UpdateModelProvenanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelProvenanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update and get"""

    def get_module_resource_id_param(self):
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model_provenance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_provenance,
            model_id=self.module.params.get("model_id"),
        )

    def get_create_model_class(self):
        return CreateModelProvenanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model_provenance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                create_model_provenance_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateModelProvenanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_model_provenance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                update_model_provenance_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )


DataScienceModelProvenanceHelperCustom = get_custom_class(
    "DataScienceModelProvenanceHelperCustom"
)


class ResourceHelper(
    DataScienceModelProvenanceHelperCustom, DataScienceModelProvenanceHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str", required=True),
            repository_url=dict(type="str"),
            git_branch=dict(type="str"),
            git_commit=dict(type="str"),
            script_dir=dict(type="str"),
            training_script=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model_provenance",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
