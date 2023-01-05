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
module: oci_data_science_notebook_session
short_description: Manage a NotebookSession resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NotebookSession resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new notebook session.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_science_notebook_session_actions) module: activate, change_compartment,
      deactivate."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the notebook session.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the notebook
              session.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    notebook_session_config_details:
        description:
            - ""
        type: dict
        suboptions:
            shape:
                description:
                    - The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved
                      using the `ListNotebookSessionShapes` endpoint.
                type: str
                required: true
            block_storage_size_in_gbs:
                description:
                    - A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.
                type: int
            subnet_id:
                description:
                    - A notebook session instance is provided with a VNIC for network access.  This specifies the
                      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create a VNIC in.  The subnet should
                      be in a VCN with a NAT gateway for egress to the internet.
                type: str
            notebook_session_shape_config_details:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the notebook session instance.
                        type: float
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the notebook session instance, in gigabytes.
                        type: float
    display_name:
        description:
            - "A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
              Example: `My NotebookSession`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    notebook_session_configuration_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            shape:
                description:
                    - The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved
                      using the `ListNotebookSessionShapes` endpoint.
                type: str
                required: true
            block_storage_size_in_gbs:
                description:
                    - A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.
                type: int
            subnet_id:
                description:
                    - A notebook session instance is provided with a VNIC for network access.  This specifies the
                      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create a VNIC in.  The subnet should
                      be in a VCN with a NAT gateway for egress to the internet.
                type: str
                required: true
            notebook_session_shape_config_details:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the notebook session instance.
                        type: float
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the notebook session instance, in gigabytes.
                        type: float
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    notebook_session_runtime_config_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            custom_environment_variables:
                description:
                    - Custom environment variables for Notebook Session. These key-value pairs will be available for customers in Notebook Sessions.
                type: dict
            notebook_session_git_config_details:
                description:
                    - ""
                type: dict
                suboptions:
                    notebook_session_git_repo_config_collection:
                        description:
                            - A collection of Git repository configurations.
                        type: list
                        elements: dict
                        suboptions:
                            url:
                                description:
                                    - The repository URL
                                type: str
                                required: true
    notebook_session_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the notebook session.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NotebookSession.
            - Use I(state=present) to create or update a NotebookSession.
            - Use I(state=absent) to delete a NotebookSession.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create notebook_session
  oci_data_science_notebook_session:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    notebook_session_config_details:
      # required
      shape: shape_example

      # optional
      block_storage_size_in_gbs: 56
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      notebook_session_shape_config_details:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
    display_name: display_name_example
    notebook_session_configuration_details:
      # required
      shape: shape_example
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      block_storage_size_in_gbs: 56
      notebook_session_shape_config_details:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    notebook_session_runtime_config_details:
      # optional
      custom_environment_variables: null
      notebook_session_git_config_details:
        # optional
        notebook_session_git_repo_config_collection:
        - # required
          url: url_example

- name: Update notebook_session
  oci_data_science_notebook_session:
    # required
    notebook_session_id: "ocid1.notebooksession.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    notebook_session_configuration_details:
      # required
      shape: shape_example
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      block_storage_size_in_gbs: 56
      notebook_session_shape_config_details:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    notebook_session_runtime_config_details:
      # optional
      custom_environment_variables: null
      notebook_session_git_config_details:
        # optional
        notebook_session_git_repo_config_collection:
        - # required
          url: url_example

- name: Update notebook_session using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_notebook_session:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    notebook_session_configuration_details:
      # required
      shape: shape_example
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      block_storage_size_in_gbs: 56
      notebook_session_shape_config_details:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    notebook_session_runtime_config_details:
      # optional
      custom_environment_variables: null
      notebook_session_git_config_details:
        # optional
        notebook_session_git_repo_config_collection:
        - # required
          url: url_example

- name: Delete notebook_session
  oci_data_science_notebook_session:
    # required
    notebook_session_id: "ocid1.notebooksession.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete notebook_session using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_notebook_session:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
notebook_session:
    description:
        - Details of the NotebookSession resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the notebook session.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - "A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
                  Example: `My NotebookSession`"
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the notebook session.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the notebook session.
            returned: on success
            type: str
            sample: created_by_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the notebook session's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        notebook_session_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved
                          using the `ListNotebookSessionShapes` endpoint.
                    returned: on success
                    type: str
                    sample: shape_example
                block_storage_size_in_gbs:
                    description:
                        - A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.
                    returned: on success
                    type: int
                    sample: 56
                subnet_id:
                    description:
                        - A notebook session instance is provided with a VNIC for network access.  This specifies the
                          L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create a VNIC in.  The subnet
                          should be in a VCN with a NAT gateway for egress to the internet.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                notebook_session_shape_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs available to the notebook session instance.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - The total amount of memory available to the notebook session instance, in gigabytes.
                            returned: on success
                            type: float
                            sample: 3.4
        notebook_session_config_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved
                          using the `ListNotebookSessionShapes` endpoint.
                    returned: on success
                    type: str
                    sample: shape_example
                block_storage_size_in_gbs:
                    description:
                        - A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.
                    returned: on success
                    type: int
                    sample: 56
                subnet_id:
                    description:
                        - A notebook session instance is provided with a VNIC for network access.  This specifies the
                          L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create a VNIC in.  The subnet
                          should be in a VCN with a NAT gateway for egress to the internet.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                notebook_session_shape_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs available to the notebook session instance.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - The total amount of memory available to the notebook session instance, in gigabytes.
                            returned: on success
                            type: float
                            sample: 3.4
        notebook_session_runtime_config_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                custom_environment_variables:
                    description:
                        - Custom environment variables for Notebook Session. These key-value pairs will be available for customers in Notebook Sessions.
                    returned: on success
                    type: dict
                    sample: {}
                notebook_session_git_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        notebook_session_git_repo_config_collection:
                            description:
                                - A collection of Git repository configurations.
                            returned: on success
                            type: complex
                            contains:
                                url:
                                    description:
                                        - The repository URL
                                    returned: on success
                                    type: str
                                    sample: url_example
        notebook_session_url:
            description:
                - The URL to interact with the notebook session.
            returned: on success
            type: str
            sample: notebook_session_url_example
        lifecycle_state:
            description:
                - The state of the notebook session.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the state of the notebook session.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "notebook_session_configuration_details": {
            "shape": "shape_example",
            "block_storage_size_in_gbs": 56,
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "notebook_session_shape_config_details": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            }
        },
        "notebook_session_config_details": {
            "shape": "shape_example",
            "block_storage_size_in_gbs": 56,
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "notebook_session_shape_config_details": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            }
        },
        "notebook_session_runtime_config_details": {
            "custom_environment_variables": {},
            "notebook_session_git_config_details": {
                "notebook_session_git_repo_config_collection": [{
                    "url": "url_example"
                }]
            }
        },
        "notebook_session_url": "notebook_session_url_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_science import DataScienceClient
    from oci.data_science.models import CreateNotebookSessionDetails
    from oci.data_science.models import UpdateNotebookSessionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceNotebookSessionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataScienceNotebookSessionHelperGen, self
        ).get_possible_entity_types() + [
            "notebooksession",
            "notebooksessions",
            "dataSciencenotebooksession",
            "dataSciencenotebooksessions",
            "notebooksessionresource",
            "notebooksessionsresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "notebook_session_id"

    def get_module_resource_id(self):
        return self.module.params.get("notebook_session_id")

    def get_get_fn(self):
        return self.client.get_notebook_session

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_notebook_session, notebook_session_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_notebook_session,
            notebook_session_id=self.module.params.get("notebook_session_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
            self.client.list_notebook_sessions, **kwargs
        )

    def get_create_model_class(self):
        return CreateNotebookSessionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_notebook_session,
            call_fn_args=(),
            call_fn_kwargs=dict(create_notebook_session_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNotebookSessionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_notebook_session,
            call_fn_args=(),
            call_fn_kwargs=dict(
                notebook_session_id=self.module.params.get("notebook_session_id"),
                update_notebook_session_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_notebook_session,
            call_fn_args=(),
            call_fn_kwargs=dict(
                notebook_session_id=self.module.params.get("notebook_session_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataScienceNotebookSessionHelperCustom = get_custom_class(
    "DataScienceNotebookSessionHelperCustom"
)


class ResourceHelper(
    DataScienceNotebookSessionHelperCustom, DataScienceNotebookSessionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            notebook_session_config_details=dict(
                type="dict",
                options=dict(
                    shape=dict(type="str", required=True),
                    block_storage_size_in_gbs=dict(type="int"),
                    subnet_id=dict(type="str"),
                    notebook_session_shape_config_details=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                        ),
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            notebook_session_configuration_details=dict(
                type="dict",
                options=dict(
                    shape=dict(type="str", required=True),
                    block_storage_size_in_gbs=dict(type="int"),
                    subnet_id=dict(type="str", required=True),
                    notebook_session_shape_config_details=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            notebook_session_runtime_config_details=dict(
                type="dict",
                options=dict(
                    custom_environment_variables=dict(type="dict"),
                    notebook_session_git_config_details=dict(
                        type="dict",
                        options=dict(
                            notebook_session_git_repo_config_collection=dict(
                                type="list",
                                elements="dict",
                                options=dict(url=dict(type="str", required=True)),
                            )
                        ),
                    ),
                ),
            ),
            notebook_session_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="notebook_session",
        service_client_class=DataScienceClient,
        namespace="data_science",
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
