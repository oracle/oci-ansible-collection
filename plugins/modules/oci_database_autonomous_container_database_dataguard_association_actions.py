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
module: oci_database_autonomous_container_database_dataguard_association_actions
short_description: Perform actions on an AutonomousContainerDatabaseDataguardAssociation resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AutonomousContainerDatabaseDataguardAssociation resource in Oracle Cloud Infrastructure
    - For I(action=failover), fails over the standby Autonomous Container Database identified by the autonomousContainerDatabaseId parameter to the primary
      Autonomous Container Database after the existing primary Autonomous Container Database fails or becomes unreachable.
      A failover can result in data loss, depending on the protection mode in effect at the time the primary Autonomous Container Database fails.
    - For I(action=reinstate), reinstates a disabled standby Autonomous Container Database, identified by the autonomousContainerDatabaseId parameter, to an
      active standby Autonomous Container Database.
    - For I(action=switchover), switches over the primary Autonomous Container Database of an Autonomous Data Guard peer association to standby role. The
      standby Autonomous Container Database associated with autonomousContainerDatabaseDataguardAssociationId assumes the primary Autonomous Container Database
      role.
      A switchover incurs no data loss.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_container_database_id:
        description:
            - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    autonomous_container_database_dataguard_association_id:
        description:
            - The Autonomous Container Database-Autonomous Data Guard association
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the AutonomousContainerDatabaseDataguardAssociation.
        type: str
        required: true
        choices:
            - "failover"
            - "reinstate"
            - "switchover"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action failover on autonomous_container_database_dataguard_association
  oci_database_autonomous_container_database_dataguard_association_actions:
    # required
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_container_database_dataguard_association_id: "ocid1.autonomouscontainerdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    action: failover

- name: Perform action reinstate on autonomous_container_database_dataguard_association
  oci_database_autonomous_container_database_dataguard_association_actions:
    # required
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_container_database_dataguard_association_id: "ocid1.autonomouscontainerdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    action: reinstate

- name: Perform action switchover on autonomous_container_database_dataguard_association
  oci_database_autonomous_container_database_dataguard_association_actions:
    # required
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_container_database_dataguard_association_id: "ocid1.autonomouscontainerdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    action: switchover

"""

RETURN = """
autonomous_container_database_dataguard_association:
    description:
        - Details of the AutonomousContainerDatabaseDataguardAssociation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Autonomous Data Guard created for a given Autonomous Container Database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_container_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Container Database that has a
                  relationship with the peer Autonomous Container Database.
            returned: on success
            type: str
            sample: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        lifecycle_state:
            description:
                - The current state of Autonomous Data Guard.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState, if available.
            returned: on success
            type: str
            sample: lifecycle_details_example
        peer_autonomous_container_database_dataguard_association_id:
            description:
                - The OCID of the peer Autonomous Container Database-Autonomous Data Guard association.
            returned: on success
            type: str
            sample: "ocid1.peerautonomouscontainerdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
        peer_autonomous_container_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the peer Autonomous Container Database.
            returned: on success
            type: str
            sample: "ocid1.peerautonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        peer_role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        peer_lifecycle_state:
            description:
                - The current state of Autonomous Data Guard.
            returned: on success
            type: str
            sample: PROVISIONING
        protection_mode:
            description:
                - The protection mode of this Autonomous Data Guard association. For more information, see
                  L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: str
            sample: MAXIMUM_AVAILABILITY
        fast_start_fail_over_lag_limit_in_seconds:
            description:
                - The lag time for my preference based on data loss tolerance in seconds.
            returned: on success
            type: int
            sample: 56
        apply_lag:
            description:
                - The lag time between updates to the primary Autonomous Container Database and application of the redo data on the standby Autonomous Container
                  Database,
                  as computed by the reporting database.
                - "Example: `9 seconds`"
            returned: on success
            type: str
            sample: apply_lag_example
        apply_rate:
            description:
                - The rate at which redo logs are synchronized between the associated Autonomous Container Databases.
                - "Example: `180 Mb per second`"
            returned: on success
            type: str
            sample: apply_rate_example
        is_automatic_failover_enabled:
            description:
                - Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association
            returned: on success
            type: bool
            sample: true
        transport_lag:
            description:
                - The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database,
                  as computed by the reporting database.
                - "Example: `7 seconds`"
            returned: on success
            type: str
            sample: transport_lag_example
        time_last_synced:
            description:
                - The date and time of the last update to the apply lag, apply rate, and transport lag values.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time the Autonomous DataGuard association was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_role_changed:
            description:
                - The date and time when the last role change action happened.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_container_database_id": "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "role": "PRIMARY",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "peer_autonomous_container_database_dataguard_association_id": "ocid1.peerautonomouscontainerdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_autonomous_container_database_id": "ocid1.peerautonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_role": "PRIMARY",
        "peer_lifecycle_state": "PROVISIONING",
        "protection_mode": "MAXIMUM_AVAILABILITY",
        "fast_start_fail_over_lag_limit_in_seconds": 56,
        "apply_lag": "apply_lag_example",
        "apply_rate": "apply_rate_example",
        "is_automatic_failover_enabled": true,
        "transport_lag": "transport_lag_example",
        "time_last_synced": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_role_changed": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousContainerDatabaseDataguardAssociationActionsHelperGen(
    OCIActionsHelperBase
):
    """
    Supported actions:
        failover
        reinstate
        switchover
    """

    def __init__(self, *args, **kwargs):
        super(
            AutonomousContainerDatabaseDataguardAssociationActionsHelperGen, self
        ).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "autonomous_container_database_dataguard_association_id"

    def get_module_resource_id(self):
        return self.module.params.get(
            "autonomous_container_database_dataguard_association_id"
        )

    def get_get_fn(self):
        return self.client.get_autonomous_container_database_dataguard_association

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_container_database_dataguard_association,
            autonomous_container_database_id=self.module.params.get(
                "autonomous_container_database_id"
            ),
            autonomous_container_database_dataguard_association_id=self.module.params.get(
                "autonomous_container_database_dataguard_association_id"
            ),
        )

    def failover(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.failover_autonomous_container_database_dataguard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
                autonomous_container_database_dataguard_association_id=self.module.params.get(
                    "autonomous_container_database_dataguard_association_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def reinstate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reinstate_autonomous_container_database_dataguard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
                autonomous_container_database_dataguard_association_id=self.module.params.get(
                    "autonomous_container_database_dataguard_association_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def switchover(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switchover_autonomous_container_database_dataguard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
                autonomous_container_database_dataguard_association_id=self.module.params.get(
                    "autonomous_container_database_dataguard_association_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousContainerDatabaseDataguardAssociationActionsHelperCustom = get_custom_class(
    "AutonomousContainerDatabaseDataguardAssociationActionsHelperCustom"
)


class ResourceHelper(
    AutonomousContainerDatabaseDataguardAssociationActionsHelperCustom,
    AutonomousContainerDatabaseDataguardAssociationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            autonomous_container_database_id=dict(type="str", required=True),
            autonomous_container_database_dataguard_association_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=["failover", "reinstate", "switchover"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_container_database_dataguard_association",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
