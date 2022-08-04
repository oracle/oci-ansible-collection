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
module: oci_data_science_model_deployment_actions
short_description: Perform actions on a ModelDeployment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ModelDeployment resource in Oracle Cloud Infrastructure
    - For I(action=activate), activates the model deployment.
    - For I(action=change_compartment), moves a model deployment into a different compartment. When provided, If-Match is checked against ETag values of the
      resource.
    - For I(action=deactivate), deactivates the model deployment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    model_deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ModelDeployment.
        type: str
        required: true
        choices:
            - "activate"
            - "change_compartment"
            - "deactivate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on model_deployment
  oci_data_science_model_deployment_actions:
    # required
    model_deployment_id: "ocid1.modeldeployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

- name: Perform action change_compartment on model_deployment
  oci_data_science_model_deployment_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    model_deployment_id: "ocid1.modeldeployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action deactivate on model_deployment
  oci_data_science_model_deployment_actions:
    # required
    model_deployment_id: "ocid1.modeldeployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: deactivate

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
                                                  specified.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        memory_in_gbs:
                                            description:
                                                - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows memory to be specified.
                                                  This specifies the size of the memory in GBs.
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
    from oci.data_science import DataScienceClient
    from oci.data_science.models import ChangeModelDeploymentCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelDeploymentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        change_compartment
        deactivate
    """

    @staticmethod
    def get_module_resource_id_param():
        return "model_deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_deployment_id")

    def get_get_fn(self):
        return self.client.get_model_deployment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_deployment,
            model_deployment_id=self.module.params.get("model_deployment_id"),
        )

    def activate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_model_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_deployment_id=self.module.params.get("model_deployment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeModelDeploymentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_model_deployment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_deployment_id=self.module.params.get("model_deployment_id"),
                change_model_deployment_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def deactivate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deactivate_model_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_deployment_id=self.module.params.get("model_deployment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataScienceModelDeploymentActionsHelperCustom = get_custom_class(
    "DataScienceModelDeploymentActionsHelperCustom"
)


class ResourceHelper(
    DataScienceModelDeploymentActionsHelperCustom,
    DataScienceModelDeploymentActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            model_deployment_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["activate", "change_compartment", "deactivate"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model_deployment",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
