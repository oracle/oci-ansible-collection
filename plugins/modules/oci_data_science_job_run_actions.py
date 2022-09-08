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
module: oci_data_science_job_run_actions
short_description: Perform actions on a JobRun resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a JobRun resource in Oracle Cloud Infrastructure
    - For I(action=cancel), cancels an IN_PROGRESS job run.
    - For I(action=change_compartment), changes a job run's compartment
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_run_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job run.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the JobRun.
        type: str
        required: true
        choices:
            - "cancel"
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel on job_run
  oci_data_science_job_run_actions:
    # required
    job_run_id: "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

- name: Perform action change_compartment on job_run
  oci_data_science_job_run_actions:
    # required
    job_run_id: "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
job_run:
    description:
        - Details of the JobRun resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job run.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_accepted:
            description:
                - The date and time the job run was accepted in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - The date and time the job run request was started in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The date and time the job run request was finished in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the job run.
            returned: on success
            type: str
            sample: created_by_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the job with.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the job.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        job_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job run.
            returned: on success
            type: str
            sample: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource.
            returned: on success
            type: str
            sample: display_name_example
        job_configuration_override_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                job_type:
                    description:
                        - The type of job.
                    returned: on success
                    type: str
                    sample: DEFAULT
                environment_variables:
                    description:
                        - Environment variables to set for the job.
                    returned: on success
                    type: dict
                    sample: {}
                command_line_arguments:
                    description:
                        - The arguments to pass to the job.
                    returned: on success
                    type: str
                    sample: command_line_arguments_example
                maximum_runtime_in_minutes:
                    description:
                        - A time bound for the execution of the job. Timer starts when the job becomes active.
                    returned: on success
                    type: int
                    sample: 56
        job_infrastructure_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                job_infrastructure_type:
                    description:
                        - The infrastructure type used for job run.
                    returned: on success
                    type: str
                    sample: STANDALONE
                shape_name:
                    description:
                        - The shape used to launch the job run instances.
                    returned: on success
                    type: str
                    sample: shape_name_example
                subnet_id:
                    description:
                        - The subnet to create a secondary vnic in to attach to the instance running the job
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                block_storage_size_in_gbs:
                    description:
                        - The size of the block storage volume to attach to the instance running the job
                    returned: on success
                    type: int
                    sample: 56
                job_shape_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - A job run instance of type VM.Standard.E3.Flex allows the ocpu count to be specified.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - A job run instance of type VM.Standard.E3.Flex allows memory to be specified. This specifies the size of the memory in GBs.
                            returned: on success
                            type: float
                            sample: 3.4
        job_log_configuration_override_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                enable_logging:
                    description:
                        - If customer logging is enabled for job runs.
                    returned: on success
                    type: bool
                    sample: true
                enable_auto_log_creation:
                    description:
                        - If automatic on-behalf-of log object creation is enabled for job runs.
                    returned: on success
                    type: bool
                    sample: true
                log_group_id:
                    description:
                        - The log group id for where log objects are for job runs.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The log id the job run will push logs too.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        log_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The log group id for where log objects will be for job runs.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The log id of the log object the job run logs will be shipped to.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The state of the job run.
            returned: on success
            type: str
            sample: ACCEPTED
        lifecycle_details:
            description:
                - Details of the state of the job run.
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
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "job_id": "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "job_configuration_override_details": {
            "job_type": "DEFAULT",
            "environment_variables": {},
            "command_line_arguments": "command_line_arguments_example",
            "maximum_runtime_in_minutes": 56
        },
        "job_infrastructure_configuration_details": {
            "job_infrastructure_type": "STANDALONE",
            "shape_name": "shape_name_example",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "block_storage_size_in_gbs": 56,
            "job_shape_config_details": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            }
        },
        "job_log_configuration_override_details": {
            "enable_logging": true,
            "enable_auto_log_creation": true,
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "log_details": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "lifecycle_state": "ACCEPTED",
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
    from oci.data_science.models import ChangeJobRunCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceJobRunActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "job_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("job_run_id")

    def get_get_fn(self):
        return self.client.get_job_run

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job_run, job_run_id=self.module.params.get("job_run_id"),
        )

    def cancel(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_job_run,
            call_fn_args=(),
            call_fn_kwargs=dict(job_run_id=self.module.params.get("job_run_id"),),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeJobRunCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_job_run_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_run_id=self.module.params.get("job_run_id"),
                change_job_run_compartment_details=action_details,
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


DataScienceJobRunActionsHelperCustom = get_custom_class(
    "DataScienceJobRunActionsHelperCustom"
)


class ResourceHelper(
    DataScienceJobRunActionsHelperCustom, DataScienceJobRunActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            job_run_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["cancel", "change_compartment"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="job_run",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
