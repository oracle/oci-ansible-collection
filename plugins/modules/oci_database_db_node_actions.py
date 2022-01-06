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
module: oci_database_db_node_actions
short_description: Perform actions on a DbNode resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DbNode resource in Oracle Cloud Infrastructure
    - "Performs one of the following power actions on the specified DB node:
      - start - power on
      - stop - power off
      - softreset - ACPI shutdown and power on
      - reset - power off and power on"
    - "**Note:** Stopping a node affects billing differently, depending on the type of DB system:
      *Bare metal and Exadata systems* - The _stop_ state has no effect on the resources you consume.
      Billing continues for DB nodes that you stop, and related resources continue
      to apply against any relevant quotas. You must terminate the DB system
      (L(TerminateDbSystem,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/DbSystem/TerminateDbSystem))
      to remove its resources from billing and quotas.
      *Virtual machine DB systems* - Stopping a node stops billing for all OCPUs associated with that node, and billing resumes when you restart the node."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_node_id:
        description:
            - The database node L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the DB Node.
        type: str
        choices:
            - "stop"
            - "start"
            - "softreset"
            - "reset"
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action stop on db_node
  oci_database_db_node_actions:
    # required
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
    action: STOP

- name: Perform action start on db_node
  oci_database_db_node_actions:
    # required
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
    action: STOP

- name: Perform action softreset on db_node
  oci_database_db_node_actions:
    # required
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
    action: STOP

- name: Perform action reset on db_node
  oci_database_db_node_actions:
    # required
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
    action: STOP

"""

RETURN = """
db_node:
    description:
        - Details of the DbNode resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database node.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC.
            returned: on success
            type: str
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        backup_vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup VNIC.
            returned: on success
            type: str
            sample: "ocid1.backupvnic.oc1..xxxxxxEXAMPLExxxxxx"
        host_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the host IP address associated with the database node.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.hostip.oc1..xxxxxxEXAMPLExxxxxx"
        backup_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup IP address associated with the database node.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.backupip.oc1..xxxxxxEXAMPLExxxxxx"
        vnic2_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second VNIC.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.vnic2.oc1..xxxxxxEXAMPLExxxxxx"
        backup_vnic2_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second backup VNIC.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.backupvnic2.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the database node.
            returned: on success
            type: str
            sample: PROVISIONING
        hostname:
            description:
                - The host name for the database node.
            returned: on success
            type: str
            sample: hostname_example
        fault_domain:
            description:
                - The name of the Fault Domain the instance is contained in.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        time_created:
            description:
                - The date and time that the database node was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        software_storage_size_in_gb:
            description:
                - The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        maintenance_type:
            description:
                - The type of database node maintenance.
            returned: on success
            type: str
            sample: VMDB_REBOOT_MIGRATION
        time_maintenance_window_start:
            description:
                - Start date and time of maintenance window.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_maintenance_window_end:
            description:
                - End date and time of maintenance window.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        additional_details:
            description:
                - Additional information about the planned maintenance.
            returned: on success
            type: str
            sample: additional_details_example
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the Db node.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The allocated memory in GBs on the Db node.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The allocated local node storage in GBs on the Db node.
            returned: on success
            type: int
            sample: 56
        db_server_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exacc Db server associated with the database node.
            returned: on success
            type: str
            sample: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_vnic_id": "ocid1.backupvnic.oc1..xxxxxxEXAMPLExxxxxx",
        "host_ip_id": "ocid1.hostip.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_ip_id": "ocid1.backupip.oc1..xxxxxxEXAMPLExxxxxx",
        "vnic2_id": "ocid1.vnic2.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_vnic2_id": "ocid1.backupvnic2.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "hostname": "hostname_example",
        "fault_domain": "FAULT-DOMAIN-1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "software_storage_size_in_gb": 56,
        "maintenance_type": "VMDB_REBOOT_MIGRATION",
        "time_maintenance_window_start": "2013-10-20T19:20:30+01:00",
        "time_maintenance_window_end": "2013-10-20T19:20:30+01:00",
        "additional_details": "additional_details_example",
        "cpu_core_count": 56,
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "db_server_id": "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbNodeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        db_node_action
    """

    def __init__(self, *args, **kwargs):
        super(DbNodeActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "db_node_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_node_id")

    def get_get_fn(self):
        return self.client.get_db_node

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_node, db_node_id=self.module.params.get("db_node_id"),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.db_node_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_node_id=self.module.params.get("db_node_id"), action="STOP",
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

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.db_node_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_node_id=self.module.params.get("db_node_id"), action="START",
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

    def softreset(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.db_node_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_node_id=self.module.params.get("db_node_id"), action="SOFTRESET",
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

    def reset(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.db_node_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_node_id=self.module.params.get("db_node_id"), action="RESET",
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


DbNodeActionsHelperCustom = get_custom_class("DbNodeActionsHelperCustom")


class ResourceHelper(DbNodeActionsHelperCustom, DbNodeActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            db_node_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["stop", "start", "softreset", "reset"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_node",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
