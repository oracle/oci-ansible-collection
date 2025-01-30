#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_golden_gate_deployment_upgrade_actions
short_description: Perform actions on a DeploymentUpgrade resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DeploymentUpgrade resource in Oracle Cloud Infrastructure
    - For I(action=cancel), cancels a DeploymentUpgrade, applicable only for DeploymentUpgrade in Waiting state. When provided, If-Match is checked against ETag
      values of the resource.
    - For I(action=cancel_snooze), cancel snooze of a DeploymentUpgrade. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=reschedule), reschedules a DeploymentUpgrade, applicable only for DeploymentUpgrade in Waiting state. When provided, If-Match is checked
      against ETag values of the resource.
    - For I(action=rollback), rollback a deployment to it's previous version. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=snooze), snooze a DeploymentUpgrade. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=upgrade), upgrade a deployment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    time_schedule:
        description:
            - The time of upgrade schedule. The format is defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            - Required for I(action=reschedule).
        type: str
    deployment_upgrade_id:
        description:
            - A unique Deployment Upgrade identifier.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - The type of a deploymentUpgrade cancel.
        type: str
        choices:
            - "DEFAULT"
            - "RESCHEDULE_TO_DATE"
        required: true
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
            - Applicable only for I(action=rollback)I(action=upgrade).
        type: bool
    action:
        description:
            - The action to perform on the DeploymentUpgrade.
        type: str
        required: true
        choices:
            - "cancel"
            - "cancel_snooze"
            - "reschedule"
            - "rollback"
            - "snooze"
            - "upgrade"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel on deployment_upgrade with type = DEFAULT
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: DEFAULT

- name: Perform action cancel on deployment_upgrade with type = RESCHEDULE_TO_DATE
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: RESCHEDULE_TO_DATE

- name: Perform action cancel_snooze on deployment_upgrade with type = DEFAULT
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: DEFAULT

- name: Perform action cancel_snooze on deployment_upgrade with type = RESCHEDULE_TO_DATE
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: RESCHEDULE_TO_DATE

- name: Perform action reschedule on deployment_upgrade with type = DEFAULT
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: DEFAULT

- name: Perform action reschedule on deployment_upgrade with type = RESCHEDULE_TO_DATE
  oci_golden_gate_deployment_upgrade_actions:
    # required
    time_schedule: time_schedule_example
    type: RESCHEDULE_TO_DATE

- name: Perform action rollback on deployment_upgrade with type = DEFAULT
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: DEFAULT

- name: Perform action rollback on deployment_upgrade with type = RESCHEDULE_TO_DATE
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: RESCHEDULE_TO_DATE

- name: Perform action snooze on deployment_upgrade with type = DEFAULT
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: DEFAULT

- name: Perform action snooze on deployment_upgrade with type = RESCHEDULE_TO_DATE
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: RESCHEDULE_TO_DATE

- name: Perform action upgrade on deployment_upgrade with type = DEFAULT
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: DEFAULT

- name: Perform action upgrade on deployment_upgrade with type = RESCHEDULE_TO_DATE
  oci_golden_gate_deployment_upgrade_actions:
    # required
    type: RESCHEDULE_TO_DATE

"""

RETURN = """
deployment_upgrade:
    description:
        - Details of the DeploymentUpgrade resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment upgrade being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Metadata about this specific object.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_upgrade_type:
            description:
                - "The type of the deployment upgrade: MANUAL or AUTOMATIC"
            returned: on success
            type: str
            sample: MANUAL
        time_started:
            description:
                - The date and time the request was started. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The date and time the request was finished. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        ogg_version:
            description:
                - Version of OGG
            returned: on success
            type: str
            sample: ogg_version_example
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
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_sub_state:
            description:
                - Possible GGS lifecycle sub-states.
            returned: on success
            type: str
            sample: RECOVERING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide
                  actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        previous_ogg_version:
            description:
                - Version of OGG
            returned: on success
            type: str
            sample: previous_ogg_version_example
        time_schedule:
            description:
                - The time of upgrade schedule. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_snoozed:
            description:
                - Indicates if upgrade notifications are snoozed or not.
            returned: on success
            type: bool
            sample: true
        time_snoozed_until:
            description:
                - The time the upgrade notifications are snoozed until. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_released:
            description:
                - The time the resource was released. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        release_type:
            description:
                - The type of release.
            returned: on success
            type: str
            sample: MAJOR
        is_security_fix:
            description:
                - Indicates if OGG release contains security fix.
            returned: on success
            type: bool
            sample: true
        is_rollback_allowed:
            description:
                - "Indicates if rollback is allowed. In practice only the last upgrade can be rolled back.
                  - Manual upgrade is allowed to rollback only until the old version isn't deprecated yet.
                  - Automatic upgrade by default is not allowed, unless a serious issue does not justify."
            returned: on success
            type: bool
            sample: true
        time_ogg_version_supported_until:
            description:
                - The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_cancel_allowed:
            description:
                - Indicates if cancel is allowed. Scheduled upgrade can be cancelled only if target version is not forced by service,
                  otherwise only reschedule allowed.
            returned: on success
            type: bool
            sample: true
        is_reschedule_allowed:
            description:
                - Indicates if reschedule is allowed. Upgrade can be rescheduled postponed until the end of the service defined auto-upgrade period.
            returned: on success
            type: bool
            sample: true
        time_schedule_max:
            description:
                - Indicates the latest time until the deployment upgrade could be rescheduled. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_upgrade_type": "MANUAL",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "ogg_version": "ogg_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "RECOVERING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "previous_ogg_version": "previous_ogg_version_example",
        "time_schedule": "2013-10-20T19:20:30+01:00",
        "is_snoozed": true,
        "time_snoozed_until": "2013-10-20T19:20:30+01:00",
        "time_released": "2013-10-20T19:20:30+01:00",
        "release_type": "MAJOR",
        "is_security_fix": true,
        "is_rollback_allowed": true,
        "time_ogg_version_supported_until": "2013-10-20T19:20:30+01:00",
        "is_cancel_allowed": true,
        "is_reschedule_allowed": true,
        "time_schedule_max": "2013-10-20T19:20:30+01:00"
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
    from oci.golden_gate.models import CancelDeploymentUpgradeDetails
    from oci.golden_gate.models import CancelSnoozeDeploymentUpgradeDetails
    from oci.golden_gate.models import RescheduleDeploymentUpgradeDetails
    from oci.golden_gate.models import RollbackDeploymentUpgradeDetails
    from oci.golden_gate.models import SnoozeDeploymentUpgradeDetails
    from oci.golden_gate.models import UpgradeDeploymentUpgradeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentUpgradeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        cancel_snooze
        reschedule
        rollback
        snooze
        upgrade
    """

    @staticmethod
    def get_module_resource_id_param():
        return "deployment_upgrade_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_upgrade_id")

    def get_get_fn(self):
        return self.client.get_deployment_upgrade

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment_upgrade,
            deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
        )

    def cancel(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                cancel_deployment_upgrade_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def cancel_snooze(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelSnoozeDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_snooze_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                cancel_snooze_deployment_upgrade_details=action_details,
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

    def reschedule(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RescheduleDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reschedule_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                reschedule_deployment_upgrade_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def rollback(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RollbackDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rollback_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                rollback_deployment_upgrade_details=action_details,
                is_lock_override=self.module.params.get("is_lock_override"),
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

    def snooze(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SnoozeDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.snooze_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                snooze_deployment_upgrade_details=action_details,
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

    def upgrade(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpgradeDeploymentUpgradeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_deployment_upgrade,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_upgrade_id=self.module.params.get("deployment_upgrade_id"),
                upgrade_deployment_upgrade_details=action_details,
                is_lock_override=self.module.params.get("is_lock_override"),
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


DeploymentUpgradeActionsHelperCustom = get_custom_class(
    "DeploymentUpgradeActionsHelperCustom"
)


class ResourceHelper(
    DeploymentUpgradeActionsHelperCustom, DeploymentUpgradeActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            time_schedule=dict(type="str"),
            deployment_upgrade_id=dict(aliases=["id"], type="str", required=True),
            type=dict(
                type="str", required=True, choices=["DEFAULT", "RESCHEDULE_TO_DATE"]
            ),
            is_lock_override=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel",
                    "cancel_snooze",
                    "reschedule",
                    "rollback",
                    "snooze",
                    "upgrade",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment_upgrade",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
