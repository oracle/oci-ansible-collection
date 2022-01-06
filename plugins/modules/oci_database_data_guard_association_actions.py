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
module: oci_database_data_guard_association_actions
short_description: Perform actions on a DataGuardAssociation resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataGuardAssociation resource in Oracle Cloud Infrastructure
    - For I(action=failover), performs a failover to transition the standby database identified by the `databaseId` parameter into the
      specified Data Guard association's primary role after the existing primary database fails or becomes unreachable.
      A failover might result in data loss depending on the protection mode in effect at the time of the primary
      database failure.
    - For I(action=reinstate), reinstates the database identified by the `databaseId` parameter into the standby role in a Data Guard association.
    - For I(action=switchover), performs a switchover to transition the primary database of a Data Guard association into a standby role. The
      standby database associated with the `dataGuardAssociationId` assumes the primary database role.
      A switchover guarantees no data loss.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    data_guard_association_id:
        description:
            - The Data Guard association's L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    database_admin_password:
        description:
            - The DB system administrator password.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DataGuardAssociation.
        type: str
        required: true
        choices:
            - "failover"
            - "reinstate"
            - "switchover"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action failover on data_guard_association
  oci_database_data_guard_association_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    data_guard_association_id: "ocid1.dataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    database_admin_password: example-password
    action: failover

- name: Perform action reinstate on data_guard_association
  oci_database_data_guard_association_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    data_guard_association_id: "ocid1.dataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    database_admin_password: example-password
    action: reinstate

- name: Perform action switchover on data_guard_association
  oci_database_data_guard_association_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    data_guard_association_id: "ocid1.dataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    database_admin_password: example-password
    action: switchover

"""

RETURN = """
data_guard_association:
    description:
        - Details of the DataGuardAssociation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Data Guard association.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the reporting database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        role:
            description:
                - The role of the reporting database in this Data Guard association.
            returned: on success
            type: str
            sample: PRIMARY
        lifecycle_state:
            description:
                - The current state of the Data Guard association.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState, if available.
            returned: on success
            type: str
            sample: lifecycle_details_example
        peer_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system containing the associated
                  peer database.
            returned: on success
            type: str
            sample: "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        peer_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home containing the associated peer
                  database.
            returned: on success
            type: str
            sample: "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx"
        peer_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated peer database.
            returned: on success
            type: str
            sample: "ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        peer_data_guard_association_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the peer database's Data Guard association.
            returned: on success
            type: str
            sample: "ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
        peer_role:
            description:
                - The role of the peer database in this Data Guard association.
            returned: on success
            type: str
            sample: PRIMARY
        apply_lag:
            description:
                - The lag time between updates to the primary database and application of the redo data on the standby database,
                  as computed by the reporting database.
                - "Example: `9 seconds`"
            returned: on success
            type: str
            sample: apply_lag_example
        apply_rate:
            description:
                - The rate at which redo logs are synced between the associated databases.
                - "Example: `180 Mb per second`"
            returned: on success
            type: str
            sample: apply_rate_example
        protection_mode:
            description:
                - The protection mode of this Data Guard association. For more information, see
                  L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: str
            sample: MAXIMUM_AVAILABILITY
        transport_type:
            description:
                - The redo transport type used by this Data Guard association.  For more information, see
                  L(Redo Transport Services,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: str
            sample: SYNC
        time_created:
            description:
                - The date and time the Data Guard association was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "role": "PRIMARY",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "peer_db_system_id": "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_db_home_id": "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_database_id": "ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_data_guard_association_id": "ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_role": "PRIMARY",
        "apply_lag": "apply_lag_example",
        "apply_rate": "apply_rate_example",
        "protection_mode": "MAXIMUM_AVAILABILITY",
        "transport_type": "SYNC",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import FailoverDataGuardAssociationDetails
    from oci.database.models import ReinstateDataGuardAssociationDetails
    from oci.database.models import SwitchoverDataGuardAssociationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataGuardAssociationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        failover
        reinstate
        switchover
    """

    def __init__(self, *args, **kwargs):
        super(DataGuardAssociationActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "data_guard_association_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_guard_association_id")

    def get_get_fn(self):
        return self.client.get_data_guard_association

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_guard_association,
            database_id=self.module.params.get("database_id"),
            data_guard_association_id=self.module.params.get(
                "data_guard_association_id"
            ),
        )

    def failover(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, FailoverDataGuardAssociationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.failover_data_guard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                data_guard_association_id=self.module.params.get(
                    "data_guard_association_id"
                ),
                failover_data_guard_association_details=action_details,
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
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ReinstateDataGuardAssociationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reinstate_data_guard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                data_guard_association_id=self.module.params.get(
                    "data_guard_association_id"
                ),
                reinstate_data_guard_association_details=action_details,
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
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SwitchoverDataGuardAssociationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switchover_data_guard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                data_guard_association_id=self.module.params.get(
                    "data_guard_association_id"
                ),
                switchover_data_guard_association_details=action_details,
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


DataGuardAssociationActionsHelperCustom = get_custom_class(
    "DataGuardAssociationActionsHelperCustom"
)


class ResourceHelper(
    DataGuardAssociationActionsHelperCustom, DataGuardAssociationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            database_id=dict(type="str", required=True),
            data_guard_association_id=dict(aliases=["id"], type="str", required=True),
            database_admin_password=dict(type="str", required=True, no_log=True),
            action=dict(
                type="str",
                required=True,
                choices=["failover", "reinstate", "switchover"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_guard_association",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
