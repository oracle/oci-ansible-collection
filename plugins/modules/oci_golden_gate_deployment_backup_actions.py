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
module: oci_golden_gate_deployment_backup_actions
short_description: Perform actions on a DeploymentBackup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DeploymentBackup resource in Oracle Cloud Infrastructure
    - For I(action=cancel), cancels a Deployment Backup creation process.
    - For I(action=change_compartment), moves a DeploymentBackup into a different compartment within the same tenancy.  When provided,
      If-Match is checked against ETag values of the resource.  For information about moving
      resources between compartments, see L(Moving Resources Between
      Compartments,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=copy), creates a copy of a Deployment Backup.
    - For I(action=restore_deployment), restores a Deployment from a Deployment Backup created from the same Deployment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for I(action=change_compartment).
        type: str
    namespace_name:
        description:
            - Name of namespace that serves as a container for all of your buckets
            - Required for I(action=copy).
        type: str
    bucket_name:
        description:
            - Name of the bucket where the object is to be uploaded in the object storage
            - Required for I(action=copy).
        type: str
    freeform_tags:
        description:
            - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
              for cross-compatibility only.
            - "Example: `{\\"bar-key\\": \\"value\\"}`"
            - Applicable only for I(action=copy).
        type: dict
    defined_tags:
        description:
            - Tags defined for this resource. Each key is predefined and scoped to a namespace.
            - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - Applicable only for I(action=copy).
        type: dict
    deployment_backup_id:
        description:
            - A unique DeploymentBackup identifier.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - The type of a deployment backup cancel
            - Required for I(action=cancel), I(action=restore_deployment).
        type: str
        choices:
            - "DEFAULT"
    action:
        description:
            - The action to perform on the DeploymentBackup.
        type: str
        required: true
        choices:
            - "cancel"
            - "change_compartment"
            - "copy"
            - "restore_deployment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel on deployment_backup with type = DEFAULT
  oci_golden_gate_deployment_backup_actions:
    # required
    type: DEFAULT

- name: Perform action change_compartment on deployment_backup
  oci_golden_gate_deployment_backup_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_backup_id: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action copy on deployment_backup
  oci_golden_gate_deployment_backup_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    deployment_backup_id: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
    action: copy

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Perform action restore_deployment on deployment_backup with type = DEFAULT
  oci_golden_gate_deployment_backup_actions:
    # required
    type: DEFAULT

"""

RETURN = """
deployment_backup:
    description:
        - Details of the DeploymentBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        is_automatic:
            description:
                - True if this object is automatically created
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide
                  actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_of_backup:
            description:
                - The time of the resource backup. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_backup_finished:
            description:
                - The time of the resource backup finish. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        size_in_bytes:
            description:
                - The size of the backup stored in object storage (in bytes)
            returned: on success
            type: int
            sample: 56
        backup_type:
            description:
                - Possible Deployment backup types.
            returned: on success
            type: str
            sample: INCREMENTAL
        ogg_version:
            description:
                - Version of OGG
            returned: on success
            type: str
            sample: ogg_version_example
        namespace_name:
            description:
                - Name of namespace that serves as a container for all of your buckets
            returned: on success
            type: str
            sample: namespace_name_example
        bucket_name:
            description:
                - Name of the bucket where the object is to be uploaded in the object storage
            returned: on success
            type: str
            sample: bucket_name_example
        object_name:
            description:
                - Name of the object to be uploaded to object storage
            returned: on success
            type: str
            sample: object_name_example
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
                  for cross-compatibility only.
                - "Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Tags defined for this resource. Each key is predefined and scoped to a namespace.
                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - The system tags associated with this resource, if any. The system tags are set by Oracle
                  Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
                  information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "is_automatic": true,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_of_backup": "2013-10-20T19:20:30+01:00",
        "time_backup_finished": "2013-10-20T19:20:30+01:00",
        "size_in_bytes": 56,
        "backup_type": "INCREMENTAL",
        "ogg_version": "ogg_version_example",
        "namespace_name": "namespace_name_example",
        "bucket_name": "bucket_name_example",
        "object_name": "object_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CancelDeploymentBackupDetails
    from oci.golden_gate.models import ChangeDeploymentBackupCompartmentDetails
    from oci.golden_gate.models import CopyDeploymentBackupDetails
    from oci.golden_gate.models import RestoreDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentBackupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        change_compartment
        copy
        restore_deployment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "deployment_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_backup_id")

    def get_get_fn(self):
        return self.client.get_deployment_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment_backup,
            deployment_backup_id=self.module.params.get("deployment_backup_id"),
        )

    def cancel(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelDeploymentBackupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_deployment_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_backup_id=self.module.params.get("deployment_backup_id"),
                cancel_deployment_backup_details=action_details,
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
            self.module.params, ChangeDeploymentBackupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_deployment_backup_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_backup_id=self.module.params.get("deployment_backup_id"),
                change_deployment_backup_compartment_details=action_details,
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

    def copy(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CopyDeploymentBackupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.copy_deployment_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_backup_id=self.module.params.get("deployment_backup_id"),
                copy_deployment_backup_details=action_details,
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

    def restore_deployment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_backup_id=self.module.params.get("deployment_backup_id"),
                restore_deployment_details=action_details,
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


DeploymentBackupActionsHelperCustom = get_custom_class(
    "DeploymentBackupActionsHelperCustom"
)


class ResourceHelper(
    DeploymentBackupActionsHelperCustom, DeploymentBackupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            namespace_name=dict(type="str"),
            bucket_name=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deployment_backup_id=dict(aliases=["id"], type="str", required=True),
            type=dict(type="str", choices=["DEFAULT"]),
            action=dict(
                type="str",
                required=True,
                choices=["cancel", "change_compartment", "copy", "restore_deployment"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment_backup",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
