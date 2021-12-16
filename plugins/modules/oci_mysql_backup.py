#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_mysql_backup
short_description: Manage a Backup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Backup resource in Oracle Cloud Infrastructure
    - For I(state=present), create a backup of a DB System.
    - "This resource has the following action operations in the M(oracle.oci.oci_mysql_backup_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-supplied display name for the backup.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A user-supplied description for the backup.
            - This parameter is updatable.
        type: str
    backup_type:
        description:
            - The type of backup.
        type: str
        choices:
            - "FULL"
            - "INCREMENTAL"
    db_system_id:
        description:
            - The OCID of the DB System the Backup is associated with.
            - Required for create using I(state=present).
        type: str
    retention_in_days:
        description:
            - Number of days to retain this backup.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    backup_id:
        description:
            - The OCID of the Backup
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Backup.
            - Use I(state=present) to create or update a Backup.
            - Use I(state=absent) to delete a Backup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backup
  oci_mysql_backup:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    backup_type: FULL
    retention_in_days: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update backup
  oci_mysql_backup:
    # required
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    retention_in_days: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    retention_in_days: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete backup
  oci_mysql_backup:
    # required
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
backup:
    description:
        - Details of the Backup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the backup itself
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-supplied display name for the backup.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A user-supplied description for the backup.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the backup record was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which the backup was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the backup.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: str
            sample: lifecycle_details_example
        backup_type:
            description:
                - The type of backup.
            returned: on success
            type: str
            sample: FULL
        creation_type:
            description:
                - "Indicates how the backup was created: manually, automatic, or by an Operator."
            returned: on success
            type: str
            sample: MANUAL
        db_system_id:
            description:
                - The OCID of the DB System the backup is associated with.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_snapshot:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the DB System.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The user-friendly name for the DB System. It does not have to be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - User-provided data about the DB System.
                    returned: on success
                    type: str
                    sample: description_example
                compartment_id:
                    description:
                        - The OCID of the compartment the DB System belongs in.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The OCID of the subnet the DB System is associated with.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                availability_domain:
                    description:
                        - The Availability Domain where the primary DB System should be located.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - The name of the Fault Domain the DB System is located in.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                shape_name:
                    description:
                        - "The shape of the primary instances of the DB System. The shape
                          determines resources allocated to a DB System - CPU cores
                          and memory for VM shapes; CPU cores, memory and storage for non-VM
                          (or bare metal) shapes. To get a list of shapes, use (the
                          L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20181021/ShapeSummary/ListShapes) operation."
                    returned: on success
                    type: str
                    sample: shape_name_example
                mysql_version:
                    description:
                        - Name of the MySQL Version in use for the DB System.
                    returned: on success
                    type: str
                    sample: mysql_version_example
                admin_username:
                    description:
                        - The username for the administrative user.
                    returned: on success
                    type: str
                    sample: admin_username_example
                backup_policy:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - If automated backups are enabled or disabled.
                            returned: on success
                            type: bool
                            sample: true
                        window_start_time:
                            description:
                                - The start of a 30-minute window of time in which daily, automated backups occur.
                                - "This should be in the format of the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data
                                  will be truncated to zero."
                                - At some point in the window, the system may incur a brief service disruption as the backup is performed.
                                - "If not defined, a window is selected from the following Region-based time-spans:
                                  - eu-frankfurt-1: 20:00 - 04:00 UTC
                                  - us-ashburn-1: 03:00 - 11:00 UTC
                                  - uk-london-1: 06:00 - 14:00 UTC
                                  - ap-tokyo-1: 13:00 - 21:00
                                  - us-phoenix-1: 06:00 - 14:00"
                            returned: on success
                            type: str
                            sample: window_start_time_example
                        retention_in_days:
                            description:
                                - The number of days automated backups are retained.
                            returned: on success
                            type: int
                            sample: 56
                        freeform_tags:
                            description:
                                - Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                                - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                                - "Example: `{\\"bar-key\\": \\"value\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        defined_tags:
                            description:
                                - Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                                - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                            returned: on success
                            type: dict
                            sample: {'Operations': {'CostCenter': 'US'}}
                configuration_id:
                    description:
                        - The OCID of the Configuration to be used for Instances in this DB System.
                    returned: on success
                    type: str
                    sample: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
                data_storage_size_in_gbs:
                    description:
                        - Initial size of the data volume in GiBs that will be created and attached.
                    returned: on success
                    type: int
                    sample: 56
                hostname_label:
                    description:
                        - "The hostname for the primary endpoint of the DB System. Used for DNS.
                          The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
                          (for example, \\"dbsystem-1\\" in FQDN \\"dbsystem-1.subnet123.vcn1.oraclevcn.com\\").
                          Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123."
                    returned: on success
                    type: str
                    sample: hostname_label_example
                ip_address:
                    description:
                        - "The IP address the DB System is configured to listen on. A private
                          IP address of the primary endpoint of the DB System. Must be an
                          available IP address within the subnet's CIDR. This will be a
                          \\"dotted-quad\\" style IPv4 address."
                    returned: on success
                    type: str
                    sample: ip_address_example
                port:
                    description:
                        - The port for primary endpoint of the DB System to listen on.
                    returned: on success
                    type: int
                    sample: 56
                port_x:
                    description:
                        - The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.
                    returned: on success
                    type: int
                    sample: 56
                is_highly_available:
                    description:
                        - If the policy is to enable high availability of the instance, by
                          maintaining secondary/failover capacity as necessary.
                    returned: on success
                    type: bool
                    sample: true
                endpoints:
                    description:
                        - The network endpoints available for this DB System.
                    returned: on success
                    type: complex
                    contains:
                        hostname:
                            description:
                                - The network address of the DB System.
                            returned: on success
                            type: str
                            sample: hostname_example
                        ip_address:
                            description:
                                - The IP address the DB System is configured to listen on.
                            returned: on success
                            type: str
                            sample: ip_address_example
                        port:
                            description:
                                - The port the MySQL instance listens on.
                            returned: on success
                            type: int
                            sample: 56
                        port_x:
                            description:
                                - The network port where to connect to use this endpoint using the X protocol.
                            returned: on success
                            type: int
                            sample: 56
                        modes:
                            description:
                                - The access modes from the client that this endpoint supports.
                            returned: on success
                            type: list
                            sample: []
                        status:
                            description:
                                - The state of the endpoints, as far as it can seen from the DB System.
                                  There may be some inconsistency with the actual state of the MySQL service.
                            returned: on success
                            type: str
                            sample: ACTIVE
                        status_details:
                            description:
                                - Additional information about the current endpoint status.
                            returned: on success
                            type: str
                            sample: status_details_example
                maintenance:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        window_start_time:
                            description:
                                - The start time of the maintenance window.
                                - "This string is of the format: \\"{day-of-week} {time-of-day}\\"."
                                - "\\"{day-of-week}\\" is a case-insensitive string like \\"mon\\", \\"tue\\", &c."
                                - "\\"{time-of-day}\\" is the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be
                                  truncated to zero."
                            returned: on success
                            type: str
                            sample: window_start_time_example
                freeform_tags:
                    description:
                        - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
        backup_size_in_gbs:
            description:
                - The size of the backup in base-2 (IEC) gibibytes. (GiB).
            returned: on success
            type: int
            sample: 56
        retention_in_days:
            description:
                - Number of days to retain this backup.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_gbs:
            description:
                - Initial size of the data volume in GiBs.
            returned: on success
            type: int
            sample: 56
        mysql_version:
            description:
                - The MySQL server version of the DB System used for backup.
            returned: on success
            type: str
            sample: mysql_version_example
        shape_name:
            description:
                - The shape of the DB System used for backup.
            returned: on success
            type: str
            sample: shape_name_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "backup_type": "FULL",
        "creation_type": "MANUAL",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_snapshot": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1",
            "shape_name": "shape_name_example",
            "mysql_version": "mysql_version_example",
            "admin_username": "admin_username_example",
            "backup_policy": {
                "is_enabled": true,
                "window_start_time": "window_start_time_example",
                "retention_in_days": 56,
                "freeform_tags": {'Department': 'Finance'},
                "defined_tags": {'Operations': {'CostCenter': 'US'}}
            },
            "configuration_id": "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx",
            "data_storage_size_in_gbs": 56,
            "hostname_label": "hostname_label_example",
            "ip_address": "ip_address_example",
            "port": 56,
            "port_x": 56,
            "is_highly_available": true,
            "endpoints": [{
                "hostname": "hostname_example",
                "ip_address": "ip_address_example",
                "port": 56,
                "port_x": 56,
                "modes": [],
                "status": "ACTIVE",
                "status_details": "status_details_example"
            }],
            "maintenance": {
                "window_start_time": "window_start_time_example"
            },
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        },
        "backup_size_in_gbs": 56,
        "retention_in_days": 56,
        "data_storage_size_in_gbs": 56,
        "mysql_version": "mysql_version_example",
        "shape_name": "shape_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import WorkRequestsClient
    from oci.mysql import DbBackupsClient
    from oci.mysql.models import CreateBackupDetails
    from oci.mysql.models import UpdateBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_module_resource_id_param(self):
        return "backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("backup_id")

    def get_get_fn(self):
        return self.client.get_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup, backup_id=self.module.params.get("backup_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["backup_id", "db_system_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_backups, **kwargs)

    def get_create_model_class(self):
        return CreateBackupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_backup_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                backup_id=self.module.params.get("backup_id"),
                update_backup_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(backup_id=self.module.params.get("backup_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlBackupHelperCustom = get_custom_class("MysqlBackupHelperCustom")


class ResourceHelper(MysqlBackupHelperCustom, MysqlBackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            backup_type=dict(type="str", choices=["FULL", "INCREMENTAL"]),
            db_system_id=dict(type="str"),
            retention_in_days=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backup",
        service_client_class=DbBackupsClient,
        namespace="mysql",
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
