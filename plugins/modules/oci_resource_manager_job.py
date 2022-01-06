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
module: oci_resource_manager_job
short_description: Manage a Job resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Job resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack that is associated with the current job.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - Description of the job.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    operation:
        description:
            - Terraform-specific operation to execute.
        type: str
    job_operation_details:
        description:
            - ""
        type: dict
        suboptions:
            operation:
                description:
                    - Terraform-specific operation to execute.
                type: str
                choices:
                    - "IMPORT_TF_STATE"
                    - "APPLY"
                    - "PLAN"
                    - "DESTROY"
                required: true
            tf_state_base64_encoded:
                description:
                    - Base64-encoded state file
                    - Required when operation is 'IMPORT_TF_STATE'
                type: str
            terraform_advanced_options:
                description:
                    - ""
                    - Applicable when operation is one of ['DESTROY', 'APPLY', 'PLAN']
                type: dict
                suboptions:
                    is_refresh_required:
                        description:
                            - "Specifies whether to refresh the state for each resource before running the job (operation).
                              Refreshing the state can affect performance. Consider setting to `false` if the configuration includes several resources.
                              Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            - Applicable when operation is 'APPLY'
                        type: bool
                    parallelism:
                        description:
                            - "Limits the number of concurrent Terraform operations when L(walking the
                              graph,https://www.terraform.io/docs/internals/graph.html#walking-the-graph).
                              Use this parameter to help debug Terraform issues or to accomplish certain special use cases.
                              A higher value might cause resources to be throttled.
                              Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            - Applicable when operation is 'APPLY'
                        type: int
                    detailed_log_level:
                        description:
                            - "Enables detailed logs at the specified verbosity for running the job (operation).
                              Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            - Applicable when operation is 'APPLY'
                        type: str
                        choices:
                            - "ERROR"
                            - "WARN"
                            - "INFO"
                            - "DEBUG"
                            - "TRACE"
            execution_plan_strategy:
                description:
                    - Specifies the source of the execution plan to apply.
                      Use `AUTO_APPROVED` to run the job without an execution plan.
                    - Applicable when operation is 'APPLY'
                    - Required when operation is 'DESTROY'
                type: str
            execution_plan_job_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a plan job, for use when specifying
                      `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.
                    - Applicable when operation is 'APPLY'
                type: str
    apply_job_plan_resolution:
        description:
            - ""
        type: dict
        suboptions:
            plan_job_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that specifies the most recently executed plan
                      job.
                type: str
            is_use_latest_job_id:
                description:
                    - Specifies whether to use the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the most recently run
                      plan job.
                      `True` if using the latest job L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be a plan job
                      that completed successfully.
                type: bool
            is_auto_approved:
                description:
                    - Specifies whether to use the configuration directly, without reference to a Plan job.
                      `True` if using the configuration directly. Note that it is not necessary
                      for a Plan job to have run successfully.
                type: bool
    freeform_tags:
        description:
            - "Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_forced:
        description:
            - Indicates whether a forced cancellation is requested for the job while it was running.
              A forced cancellation can result in an incorrect state file.
              For example, the state file might not reflect the exact state of the provisioned resources.
        type: bool
    state:
        description:
            - The state of the Job.
            - Use I(state=present) to create or update a Job.
            - Use I(state=absent) to delete a Job.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create job
  oci_resource_manager_job:
    # required
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    operation: operation_example
    job_operation_details:
      # required
      operation: IMPORT_TF_STATE
      tf_state_base64_encoded: tf_state_base64_encoded_example
    apply_job_plan_resolution:
      # optional
      plan_job_id: "ocid1.planjob.oc1..xxxxxxEXAMPLExxxxxx"
      is_use_latest_job_id: true
      is_auto_approved: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update job
  oci_resource_manager_job:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_job:
    # required
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete job
  oci_resource_manager_job:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    is_forced: true

- name: Delete job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_job:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
job:
    description:
        - Details of the Job resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        stack_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack that is associated with the job.
            returned: on success
            type: str
            sample: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the job's associated stack
                  resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The job's display name.
            returned: on success
            type: str
            sample: display_name_example
        operation:
            description:
                - The type of job executing.
            returned: on success
            type: str
            sample: PLAN
        job_operation_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                operation:
                    description:
                        - Terraform-specific operation to execute.
                    returned: on success
                    type: str
                    sample: APPLY
                terraform_advanced_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_refresh_required:
                            description:
                                - "Specifies whether to refresh the state for each resource before running the job (operation).
                                  Refreshing the state can affect performance. Consider setting to `false` if the configuration includes several resources.
                                  Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            returned: on success
                            type: bool
                            sample: true
                        parallelism:
                            description:
                                - "Limits the number of concurrent Terraform operations when L(walking the
                                  graph,https://www.terraform.io/docs/internals/graph.html#walking-the-graph).
                                  Use this parameter to help debug Terraform issues or to accomplish certain special use cases.
                                  A higher value might cause resources to be throttled.
                                  Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            returned: on success
                            type: int
                            sample: 56
                        detailed_log_level:
                            description:
                                - "Enables detailed logs at the specified verbosity for running the job (operation).
                                  Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            returned: on success
                            type: str
                            sample: ERROR
                execution_plan_strategy:
                    description:
                        - Specifies the source of the execution plan to apply.
                          Use `AUTO_APPROVED` to run the job without an execution plan.
                    returned: on success
                    type: str
                    sample: FROM_PLAN_JOB_ID
                execution_plan_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the plan job that contains the execution
                          plan used for this job,
                          or `null` if no execution plan was used.
                    returned: on success
                    type: str
                    sample: "ocid1.executionplanjob.oc1..xxxxxxEXAMPLExxxxxx"
        apply_job_plan_resolution:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                plan_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that specifies the most recently executed plan
                          job.
                    returned: on success
                    type: str
                    sample: "ocid1.planjob.oc1..xxxxxxEXAMPLExxxxxx"
                is_use_latest_job_id:
                    description:
                        - Specifies whether to use the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the most recently
                          run plan job.
                          `True` if using the latest job L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be a plan job
                          that completed successfully.
                    returned: on success
                    type: bool
                    sample: true
                is_auto_approved:
                    description:
                        - Specifies whether to use the configuration directly, without reference to a Plan job.
                          `True` if using the configuration directly. Note that it is not necessary
                          for a Plan job to have run successfully.
                    returned: on success
                    type: bool
                    sample: true
        resolved_plan_job_id:
            description:
                - Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead.
                  The plan job L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that was used (if this was an apply job and
                  was not auto-approved).
            returned: on success
            type: str
            sample: "ocid1.resolvedplanjob.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time when the job was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - "The date and time when the job stopped running, irrespective of whether the job ran successfully.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Current state of the specified job.
                  For more information about job lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__JobStates).
            returned: on success
            type: str
            sample: ACCEPTED
        failure_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - Job failure reason.
                    returned: on success
                    type: str
                    sample: INTERNAL_SERVICE_ERROR
                message:
                    description:
                        - A human-readable error string.
                    returned: on success
                    type: str
                    sample: message_example
        cancellation_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_forced:
                    description:
                        - Indicates whether a forced cancellation was requested for the job while it was running.
                          A forced cancellation can result in an incorrect state file.
                          For example, the state file might not reflect the exact state of the provisioned resources.
                    returned: on success
                    type: bool
                    sample: true
        working_directory:
            description:
                - File path to the directory from which Terraform runs.
                  If not specified, the root directory is used.
                  This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.
            returned: on success
            type: str
            sample: working_directory_example
        variables:
            description:
                - "Terraform variables associated with this resource.
                  Maximum number of variables supported is 250.
                  The maximum size of each variable, including both name and value, is 8192 bytes.
                  Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
            returned: on success
            type: dict
            sample: {}
        config_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                config_source_record_type:
                    description:
                        - The type of configuration source to use for the Terraform configuration.
                    returned: on success
                    type: str
                    sample: ZIP_UPLOAD
                configuration_source_provider_id:
                    description:
                        - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm))
                          for the Git configuration source.
                    returned: on success
                    type: str
                    sample: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
                repository_url:
                    description:
                        - The URL of the Git repository.
                    returned: on success
                    type: str
                    sample: repository_url_example
                branch_name:
                    description:
                        - The name of the branch within the Git repository.
                    returned: on success
                    type: str
                    sample: branch_name_example
                commit_id:
                    description:
                        - The unique identifier (SHA-1 hash) of the individual change to the Git repository.
                    returned: on success
                    type: str
                    sample: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
                region:
                    description:
                        - "The name of the bucket's region.
                          Example: `PHX`"
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                namespace:
                    description:
                        - The Object Storage namespace that contains the bucket.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - The name of the bucket that contains the Terraform configuration files.
                    returned: on success
                    type: str
                    sample: bucket_name_example
        freeform_tags:
            description:
                - "Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "stack_id": "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "operation": "PLAN",
        "job_operation_details": {
            "operation": "APPLY",
            "terraform_advanced_options": {
                "is_refresh_required": true,
                "parallelism": 56,
                "detailed_log_level": "ERROR"
            },
            "execution_plan_strategy": "FROM_PLAN_JOB_ID",
            "execution_plan_job_id": "ocid1.executionplanjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "apply_job_plan_resolution": {
            "plan_job_id": "ocid1.planjob.oc1..xxxxxxEXAMPLExxxxxx",
            "is_use_latest_job_id": true,
            "is_auto_approved": true
        },
        "resolved_plan_job_id": "ocid1.resolvedplanjob.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "failure_details": {
            "code": "INTERNAL_SERVICE_ERROR",
            "message": "message_example"
        },
        "cancellation_details": {
            "is_forced": true
        },
        "working_directory": "working_directory_example",
        "variables": {},
        "config_source": {
            "config_source_record_type": "ZIP_UPLOAD",
            "configuration_source_provider_id": "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "branch_name": "branch_name_example",
            "commit_id": "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx",
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example"
        },
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
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import CreateJobDetails
    from oci.resource_manager.models import UpdateJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "job_id"

    def get_module_resource_id(self):
        return self.module.params.get("job_id")

    def get_get_fn(self):
        return self.client.get_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["stack_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_jobs, **kwargs)

    def get_create_model_class(self):
        return CreateJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_id=self.module.params.get("job_id"),
                update_job_details=update_details,
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
            call_fn=self.client.cancel_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_id=self.module.params.get("job_id"),
                is_forced=self.module.params.get("is_forced"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


JobHelperCustom = get_custom_class("JobHelperCustom")


class ResourceHelper(JobHelperCustom, JobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            stack_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            operation=dict(type="str"),
            job_operation_details=dict(
                type="dict",
                options=dict(
                    operation=dict(
                        type="str",
                        required=True,
                        choices=["IMPORT_TF_STATE", "APPLY", "PLAN", "DESTROY"],
                    ),
                    tf_state_base64_encoded=dict(type="str"),
                    terraform_advanced_options=dict(
                        type="dict",
                        options=dict(
                            is_refresh_required=dict(type="bool"),
                            parallelism=dict(type="int"),
                            detailed_log_level=dict(
                                type="str",
                                choices=["ERROR", "WARN", "INFO", "DEBUG", "TRACE"],
                            ),
                        ),
                    ),
                    execution_plan_strategy=dict(type="str"),
                    execution_plan_job_id=dict(type="str"),
                ),
            ),
            apply_job_plan_resolution=dict(
                type="dict",
                options=dict(
                    plan_job_id=dict(type="str"),
                    is_use_latest_job_id=dict(type="bool"),
                    is_auto_approved=dict(type="bool"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            job_id=dict(aliases=["id"], type="str"),
            is_forced=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="job",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
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
