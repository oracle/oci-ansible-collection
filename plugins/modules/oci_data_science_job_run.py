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
module: oci_data_science_job_run
short_description: Manage a JobRun resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a JobRun resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a job run.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_science_job_run_actions) module: cancel, change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the job with.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the job.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job to create a run for.
            - Required for create using I(state=present).
        type: str
    job_configuration_override_details:
        description:
            - ""
        type: dict
        suboptions:
            job_type:
                description:
                    - The type of job.
                type: str
                choices:
                    - "DEFAULT"
                required: true
            environment_variables:
                description:
                    - Environment variables to set for the job.
                type: dict
            command_line_arguments:
                description:
                    - The arguments to pass to the job.
                type: str
            maximum_runtime_in_minutes:
                description:
                    - A time bound for the execution of the job. Timer starts when the job becomes active.
                type: int
    job_log_configuration_override_details:
        description:
            - ""
        type: dict
        suboptions:
            enable_logging:
                description:
                    - If customer logging is enabled for job runs.
                type: bool
            enable_auto_log_creation:
                description:
                    - If automatic on-behalf-of log object creation is enabled for job runs.
                type: bool
            log_group_id:
                description:
                    - The log group id for where log objects are for job runs.
                type: str
            log_id:
                description:
                    - The log id the job run will push logs too.
                type: str
    display_name:
        description:
            - A user-friendly display name for the resource.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    job_run_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job run.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the JobRun.
            - Use I(state=present) to create or update a JobRun.
            - Use I(state=absent) to delete a JobRun.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create job_run
  oci_data_science_job_run:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    job_configuration_override_details:
      # required
      job_type: DEFAULT

      # optional
      environment_variables: null
      command_line_arguments: command_line_arguments_example
      maximum_runtime_in_minutes: 56
    job_log_configuration_override_details:
      # optional
      enable_logging: true
      enable_auto_log_creation: true
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update job_run
  oci_data_science_job_run:
    # required
    job_run_id: "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update job_run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_job_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete job_run
  oci_data_science_job_run:
    # required
    job_run_id: "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete job_run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_job_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
                                - The total number of OCPUs available to the job run instance.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - The total amount of memory available to the job run instance, in gigabytes.
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.data_science import DataScienceClient
    from oci.data_science.models import CreateJobRunDetails
    from oci.data_science.models import UpdateJobRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceJobRunHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataScienceJobRunHelperGen, self).get_possible_entity_types() + [
            "jobrun",
            "jobruns",
            "dataSciencejobrun",
            "dataSciencejobruns",
            "jobrunresource",
            "jobrunsresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "job_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("job_run_id")

    def get_get_fn(self):
        return self.client.get_job_run

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_job_run, job_run_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job_run, job_run_id=self.module.params.get("job_run_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["job_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_job_runs, **kwargs)

    def get_create_model_class(self):
        return CreateJobRunDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_job_run,
            call_fn_args=(),
            call_fn_kwargs=dict(create_job_run_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateJobRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_job_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_run_id=self.module.params.get("job_run_id"),
                update_job_run_details=update_details,
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
            call_fn=self.client.delete_job_run,
            call_fn_args=(),
            call_fn_kwargs=dict(job_run_id=self.module.params.get("job_run_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataScienceJobRunHelperCustom = get_custom_class("DataScienceJobRunHelperCustom")


class ResourceHelper(DataScienceJobRunHelperCustom, DataScienceJobRunHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            job_id=dict(type="str"),
            job_configuration_override_details=dict(
                type="dict",
                options=dict(
                    job_type=dict(type="str", required=True, choices=["DEFAULT"]),
                    environment_variables=dict(type="dict"),
                    command_line_arguments=dict(type="str"),
                    maximum_runtime_in_minutes=dict(type="int"),
                ),
            ),
            job_log_configuration_override_details=dict(
                type="dict",
                options=dict(
                    enable_logging=dict(type="bool"),
                    enable_auto_log_creation=dict(type="bool"),
                    log_group_id=dict(type="str"),
                    log_id=dict(type="str"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            job_run_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
