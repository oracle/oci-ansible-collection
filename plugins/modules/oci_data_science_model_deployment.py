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
module: oci_data_science_model_deployment
short_description: Manage a ModelDeployment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ModelDeployment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new model deployment.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_science_model_deployment_actions) module: activate, change_compartment,
      deactivate."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model deployment.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the model
              deployment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - "A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
              Example: `My ModelDeployment`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A short description of the model deployment.
            - This parameter is updatable.
        type: str
    model_deployment_configuration_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            deployment_type:
                description:
                    - The type of the model deployment.
                    - This parameter is updatable.
                    - Applicable when deployment_type is 'SINGLE_MODEL'
                type: str
                choices:
                    - "SINGLE_MODEL"
                required: true
            model_configuration_details:
                description:
                    - ""
                    - Applicable when deployment_type is 'SINGLE_MODEL'
                type: dict
                suboptions:
                    model_id:
                        description:
                            - The OCID of the model you want to deploy.
                            - This parameter is updatable.
                        type: str
                        required: true
                    instance_configuration:
                        description:
                            - ""
                            - Applicable when deployment_type is 'SINGLE_MODEL'
                        type: dict
                        suboptions:
                            instance_shape_name:
                                description:
                                    - The shape used to launch the model deployment instances.
                                type: str
                                required: true
                            model_deployment_instance_shape_config_details:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    ocpus:
                                        description:
                                            - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the ocpu count to be
                                              specified with in the range of 1 to 64 ocpu. VM.Standard3.Flex OCPU range is between 1 to 32 ocpu and for
                                              VM.Optimized3.Flex OCPU range is 1 to 18 ocpu.
                                        type: float
                                    memory_in_gbs:
                                        description:
                                            - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the memory to be specified
                                              with in the range of 6 to 1024 GB. VM.Standard3.Flex memory range is between 6 to 512 GB and VM.Optimized3.Flex
                                              memory range is between 6 to 256 GB.
                                        type: float
                    scaling_policy:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            policy_type:
                                description:
                                    - The type of scaling policy.
                                type: str
                                choices:
                                    - "FIXED_SIZE"
                                required: true
                            instance_count:
                                description:
                                    - The number of instances for the model deployment.
                                type: int
                                required: true
                    bandwidth_mbps:
                        description:
                            - The network bandwidth for the model.
                            - This parameter is updatable.
                        type: int
    category_log_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            access:
                description:
                    - ""
                type: dict
                suboptions:
                    log_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log to work with.
                        type: str
                        required: true
                    log_group_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log group to work with.
                        type: str
                        required: true
            predict:
                description:
                    - ""
                type: dict
                suboptions:
                    log_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log to work with.
                        type: str
                        required: true
                    log_group_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log group to work with.
                        type: str
                        required: true
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
    model_deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ModelDeployment.
            - Use I(state=present) to create or update a ModelDeployment.
            - Use I(state=absent) to delete a ModelDeployment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create model_deployment
  oci_data_science_model_deployment:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    model_deployment_configuration_details:
      # required
      deployment_type: SINGLE_MODEL
      model_configuration_details:
        # required
        model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        instance_configuration:
          # required
          instance_shape_name: instance_shape_name_example

          # optional
          model_deployment_instance_shape_config_details:
            # optional
            ocpus: 3.4
            memory_in_gbs: 3.4
        scaling_policy:
          # required
          policy_type: FIXED_SIZE
          instance_count: 56
        bandwidth_mbps: 56

    # optional
    display_name: display_name_example
    description: description_example
    category_log_details:
      # optional
      access:
        # required
        log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      predict:
        # required
        log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model_deployment
  oci_data_science_model_deployment:
    # required
    model_deployment_id: "ocid1.modeldeployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    model_deployment_configuration_details:
      # required
      deployment_type: SINGLE_MODEL
      model_configuration_details:
        # required
        model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        instance_configuration:
          # required
          instance_shape_name: instance_shape_name_example

          # optional
          model_deployment_instance_shape_config_details:
            # optional
            ocpus: 3.4
            memory_in_gbs: 3.4
        scaling_policy:
          # required
          policy_type: FIXED_SIZE
          instance_count: 56
        bandwidth_mbps: 56
    category_log_details:
      # optional
      access:
        # required
        log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      predict:
        # required
        log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model_deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_model_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    model_deployment_configuration_details:
      # required
      deployment_type: SINGLE_MODEL
      model_configuration_details:
        # required
        model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        instance_configuration:
          # required
          instance_shape_name: instance_shape_name_example

          # optional
          model_deployment_instance_shape_config_details:
            # optional
            ocpus: 3.4
            memory_in_gbs: 3.4
        scaling_policy:
          # required
          policy_type: FIXED_SIZE
          instance_count: 56
        bandwidth_mbps: 56
    category_log_details:
      # optional
      access:
        # required
        log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      predict:
        # required
        log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete model_deployment
  oci_data_science_model_deployment:
    # required
    model_deployment_id: "ocid1.modeldeployment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete model_deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_model_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
model_deployment:
    description:
        - Details of the ModelDeployment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created, in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - "A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
                  Example: `My ModelDeployment`"
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A short description of the model deployment.
            returned: on success
            type: str
            sample: description_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the model deployment.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the model deployment.
            returned: on success
            type: str
            sample: created_by_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        model_deployment_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deployment_type:
                    description:
                        - The type of the model deployment.
                    returned: on success
                    type: str
                    sample: SINGLE_MODEL
                model_configuration_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        model_id:
                            description:
                                - The OCID of the model you want to deploy.
                            returned: on success
                            type: str
                            sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
                        instance_configuration:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                instance_shape_name:
                                    description:
                                        - The shape used to launch the model deployment instances.
                                    returned: on success
                                    type: str
                                    sample: instance_shape_name_example
                                model_deployment_instance_shape_config_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        ocpus:
                                            description:
                                                - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the ocpu count to be
                                                  specified with in the range of 1 to 64 ocpu. VM.Standard3.Flex OCPU range is between 1 to 32 ocpu and for
                                                  VM.Optimized3.Flex OCPU range is 1 to 18 ocpu.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        memory_in_gbs:
                                            description:
                                                - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the memory to be
                                                  specified with in the range of 6 to 1024 GB. VM.Standard3.Flex memory range is between 6 to 512 GB and
                                                  VM.Optimized3.Flex memory range is between 6 to 256 GB.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                        scaling_policy:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                policy_type:
                                    description:
                                        - The type of scaling policy.
                                    returned: on success
                                    type: str
                                    sample: FIXED_SIZE
                                instance_count:
                                    description:
                                        - The number of instances for the model deployment.
                                    returned: on success
                                    type: int
                                    sample: 56
                        bandwidth_mbps:
                            description:
                                - The network bandwidth for the model.
                            returned: on success
                            type: int
                            sample: 56
        category_log_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                access:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log group to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                predict:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log group to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
        model_deployment_url:
            description:
                - The URL to interact with the model deployment.
            returned: on success
            type: str
            sample: model_deployment_url_example
        lifecycle_state:
            description:
                - The state of the model deployment.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the state of the model deployment.
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
        "description": "description_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_deployment_configuration_details": {
            "deployment_type": "SINGLE_MODEL",
            "model_configuration_details": {
                "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
                "instance_configuration": {
                    "instance_shape_name": "instance_shape_name_example",
                    "model_deployment_instance_shape_config_details": {
                        "ocpus": 3.4,
                        "memory_in_gbs": 3.4
                    }
                },
                "scaling_policy": {
                    "policy_type": "FIXED_SIZE",
                    "instance_count": 56
                },
                "bandwidth_mbps": 56
            }
        },
        "category_log_details": {
            "access": {
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "predict": {
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "model_deployment_url": "model_deployment_url_example",
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
    from oci.data_science.models import CreateModelDeploymentDetails
    from oci.data_science.models import UpdateModelDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelDeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataScienceModelDeploymentHelperGen, self
        ).get_possible_entity_types() + [
            "modeldeployment",
            "modeldeployments",
            "dataSciencemodeldeployment",
            "dataSciencemodeldeployments",
            "modeldeploymentresource",
            "modeldeploymentsresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "model_deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_deployment_id")

    def get_get_fn(self):
        return self.client.get_model_deployment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_deployment, model_deployment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_deployment,
            model_deployment_id=self.module.params.get("model_deployment_id"),
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
            self.client.list_model_deployments, **kwargs
        )

    def get_create_model_class(self):
        return CreateModelDeploymentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_model_deployment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateModelDeploymentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_model_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_deployment_id=self.module.params.get("model_deployment_id"),
                update_model_deployment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_model_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_deployment_id=self.module.params.get("model_deployment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataScienceModelDeploymentHelperCustom = get_custom_class(
    "DataScienceModelDeploymentHelperCustom"
)


class ResourceHelper(
    DataScienceModelDeploymentHelperCustom, DataScienceModelDeploymentHelperGen
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
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            model_deployment_configuration_details=dict(
                type="dict",
                options=dict(
                    deployment_type=dict(
                        type="str", required=True, choices=["SINGLE_MODEL"]
                    ),
                    model_configuration_details=dict(
                        type="dict",
                        options=dict(
                            model_id=dict(type="str", required=True),
                            instance_configuration=dict(
                                type="dict",
                                options=dict(
                                    instance_shape_name=dict(type="str", required=True),
                                    model_deployment_instance_shape_config_details=dict(
                                        type="dict",
                                        options=dict(
                                            ocpus=dict(type="float"),
                                            memory_in_gbs=dict(type="float"),
                                        ),
                                    ),
                                ),
                            ),
                            scaling_policy=dict(
                                type="dict",
                                options=dict(
                                    policy_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["FIXED_SIZE"],
                                    ),
                                    instance_count=dict(type="int", required=True),
                                ),
                            ),
                            bandwidth_mbps=dict(type="int"),
                        ),
                    ),
                ),
            ),
            category_log_details=dict(
                type="dict",
                options=dict(
                    access=dict(
                        type="dict",
                        options=dict(
                            log_id=dict(type="str", required=True),
                            log_group_id=dict(type="str", required=True),
                        ),
                    ),
                    predict=dict(
                        type="dict",
                        options=dict(
                            log_id=dict(type="str", required=True),
                            log_group_id=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            model_deployment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model_deployment",
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
