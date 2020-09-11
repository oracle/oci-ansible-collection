#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_mysql_db_system
short_description: Manage a DbSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DbSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates and launches a DB System.
    - "This resource has the following action operations in the M(oci_db_system_actions) module: restart, start, stop."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The user-friendly name for the DB System. It does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-provided data about the DB System.
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    availability_domain:
        description:
            - The Availability Domain where the primary instance should be located.
            - This parameter is updatable.
        type: str
    fault_domain:
        description:
            - The name of the Fault Domain the DB System is located in.
            - This parameter is updatable.
        type: str
    configuration_id:
        description:
            - The OCID of the Configuration to be used for this DB System.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    shape_name:
        description:
            - "The name of the shape. The shape determines the resources allocated
              - CPU cores and memory for VM shapes; CPU cores, memory and storage
              for non-VM (or bare metal) shapes. To get a list of shapes, use the
              L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20190415/ShapeSummary/ListShapes) operation."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    mysql_version:
        description:
            - The specific MySQL version identifier.
            - This parameter is updatable.
        type: str
    subnet_id:
        description:
            - The OCID of the subnet the DB System is associated with.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    admin_username:
        description:
            - The username for the administrative user.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    admin_password:
        description:
            - The password for the administrative user. The password must be
              between 8 and 32 characters long, and must contain at least 1
              numeric character, 1 lowercase character, 1 uppercase character, and
              1 special (nonalphanumeric) character.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    data_storage_size_in_gbs:
        description:
            - Initial size of the data volume in GBs that will be created and attached.
              Keep in mind that this only specifies the size of the database data volume,
              the log volume for the database will be scaled appropriately with its shape.
            - This parameter is updatable.
        type: int
    hostname_label:
        description:
            - The hostname for the primary endpoint of the DB System. Used for DNS.
            - "The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
              (for example, \\"dbsystem-1\\" in FQDN \\"dbsystem-1.subnet123.vcn1.oraclevcn.com\\")."
            - Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.
            - This parameter is updatable.
        type: str
    ip_address:
        description:
            - "The IP address the DB System is configured to listen on.
              A private IP address of your choice to assign to the primary endpoint of the DB System.
              Must be an available IP address within the subnet's CIDR. If you don't specify a value,
              Oracle automatically assigns a private IP address from the subnet. This should be a
              \\"dotted-quad\\" style IPv4 address."
            - This parameter is updatable.
        type: str
    port:
        description:
            - The port for primary endpoint of the DB System to listen on.
            - This parameter is updatable.
        type: int
    port_x:
        description:
            - The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
            - This parameter is updatable.
        type: int
    backup_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_enabled:
                description:
                    - Specifies if automatic backups are enabled.
                    - This parameter is updatable.
                type: bool
            window_start_time:
                description:
                    - The start of a 30-minute window of time in which daily, automated backups occur.
                    - "This should be in the format of the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be
                      truncated to zero."
                    - At some point in the window, the system may incur a brief service disruption as the backup is performed.
                    - This parameter is updatable.
                type: str
            retention_in_days:
                description:
                    - Number of days to retain an automatic backup.
                    - This parameter is updatable.
                type: int
            freeform_tags:
                description:
                    - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                      Example: `{\\"bar-key\\": \\"value\\"}`"
                    - This parameter is updatable.
                type: dict
            defined_tags:
                description:
                    - Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                    - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                    - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                    - This parameter is updatable.
                type: dict
    source:
        description:
            - ""
        type: dict
        suboptions:
            source_type:
                description:
                    - The specific source identifier.
                type: str
                choices:
                    - "BACKUP"
                    - "IMPORTURL"
                default: "NONE"
            backup_id:
                description:
                    - The OCID of the backup to be used as the source for the new DB System.
                    - Required when source_type is 'BACKUP'
                type: str
            source_url:
                description:
                    - The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.
                    - Required when source_type is 'IMPORTURL'
                type: str
    maintenance:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            window_start_time:
                description:
                    - The start of the 2 hour maintenance window.
                    - "This string is of the format: \\"{day-of-week} {time-of-day}\\"."
                    - "\\"{day-of-week}\\" is a case-insensitive string like \\"mon\\", \\"tue\\", &c."
                    - "\\"{time-of-day}\\" is the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to
                      zero."
                    - This parameter is updatable.
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DbSystem.
            - Use I(state=present) to create or update a DbSystem.
            - Use I(state=absent) to delete a DbSystem.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create db_system
  oci_mysql_db_system:
    admin_password: password
    admin_username: adminUser
    compartment_id: ocid1.compartment.oc1..UniqueID
    configuration_id: ocid1.mysqlconfiguration.oc1..UniqueID
    data_storage_size_in_gbs: 63
    description: MySQL Database Service
    display_name: DBSystem001
    shape_name: VM.Standard.E2.1
    subnet_id: ocid1.subnet.oc1.iad.UniqueID
    mysql_version: 8.0.20

- name: Update db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_db_system:
    display_name: DBSystem001
    description: MySQL Database Service
    compartment_id: ocid1.compartment.oc1..UniqueID
    availability_domain: Uocm:PHX-AD-1
    fault_domain: fault_domain_example
    configuration_id: ocid1.mysqlconfiguration.oc1..UniqueID
    shape_name: VM.Standard.E2.1
    mysql_version: 8.0.20
    subnet_id: ocid1.subnet.oc1.iad.UniqueID
    admin_username: adminUser
    admin_password: password
    data_storage_size_in_gbs: 63
    hostname_label: hostname_label_example
    ip_address: ip_address_example
    port: 56
    port_x: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update db_system
  oci_mysql_db_system:
    display_name: DBSystem001
    description: MySQL Database Service
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete db_system
  oci_mysql_db_system:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_db_system:
    display_name: DBSystem001
    compartment_id: ocid1.compartment.oc1..UniqueID
    state: absent

"""

RETURN = """
db_system:
    description:
        - Details of the DbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the DB System.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name for the DB System. It does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - User-provided data about the DB System.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment the DB System belongs in.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        subnet_id:
            description:
                - The OCID of the subnet the DB System is associated with.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        availability_domain:
            description:
                - The Availability Domain where the primary DB System should be located.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The name of the Fault Domain the DB System is located in.
            returned: on success
            type: string
            sample: fault_domain_example
        shape_name:
            description:
                - "The shape of the primary instances of the DB System. The shape
                  determines resources allocated to a DB System - CPU cores
                  and memory for VM shapes; CPU cores, memory and storage for non-VM
                  (or bare metal) shapes. To get a list of shapes, use (the
                  L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20181021/ShapeSummary/ListShapes) operation."
            returned: on success
            type: string
            sample: shape_name_example
        mysql_version:
            description:
                - Name of the MySQL Version in use for the DB System.
            returned: on success
            type: string
            sample: mysql_version_example
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
                        - "This should be in the format of the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be
                          truncated to zero."
                        - At some point in the window, the system may incur a brief service disruption as the backup is performed.
                        - "If not defined, a window is selected from the following Region-based time-spans:
                          - eu-frankfurt-1: 20:00 - 04:00 UTC
                          - us-ashburn-1: 03:00 - 11:00 UTC
                          - uk-london-1: 06:00 - 14:00 UTC
                          - ap-tokyo-1: 13:00 - 21:00
                          - us-phoenix-1: 06:00 - 14:00"
                    returned: on success
                    type: string
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
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The specific source identifier.
                    returned: on success
                    type: string
                    sample: NONE
                backup_id:
                    description:
                        - The OCID of the backup to be used as the source for the new DB System.
                    returned: on success
                    type: string
                    sample: ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx
        configuration_id:
            description:
                - The OCID of the Configuration to be used for Instances in this DB System.
            returned: on success
            type: string
            sample: ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: hostname_label_example
        ip_address:
            description:
                - "The IP address the DB System is configured to listen on. A private
                  IP address of the primary endpoint of the DB System. Must be an
                  available IP address within the subnet's CIDR. This will be a
                  \\"dotted-quad\\" style IPv4 address."
            returned: on success
            type: string
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
                    type: string
                    sample: hostname_example
                ip_address:
                    description:
                        - The IP address the DB System is configured to listen on.
                    returned: on success
                    type: string
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
                    type: string
                    sample: ACTIVE
                status_details:
                    description:
                        - Additional information about the current endpoint status.
                    returned: on success
                    type: string
                    sample: status_details_example
        lifecycle_state:
            description:
                - The current state of the DB System.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
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
                        - "\\"{time-of-day}\\" is the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated
                          to zero."
                    returned: on success
                    type: string
                    sample: window_start_time_example
        time_created:
            description:
                - The date and time the DB System was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the DB System was last updated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "fault_domain_example",
        "shape_name": "shape_name_example",
        "mysql_version": "mysql_version_example",
        "backup_policy": {
            "is_enabled": true,
            "window_start_time": "window_start_time_example",
            "retention_in_days": 56,
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        },
        "source": {
            "source_type": "NONE",
            "backup_id": "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "configuration_id": "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx",
        "data_storage_size_in_gbs": 56,
        "hostname_label": "hostname_label_example",
        "ip_address": "ip_address_example",
        "port": 56,
        "port_x": 56,
        "endpoints": [{
            "hostname": "hostname_example",
            "ip_address": "ip_address_example",
            "port": 56,
            "port_x": 56,
            "modes": [],
            "status": "ACTIVE",
            "status_details": "status_details_example"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "maintenance": {
            "window_start_time": "window_start_time_example"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.mysql import DbSystemClient
    from oci.mysql.models import CreateDbSystemDetails
    from oci.mysql.models import UpdateDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlDbSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_db_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["db_system_id", "display_name"]
            if self._use_name_as_identifier()
            else ["db_system_id", "display_name", "configuration_id"]
        )

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
        return oci_common_utils.list_all_resources(
            self.client.list_db_systems, **kwargs
        )

    def get_create_model_class(self):
        return CreateDbSystemDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(create_db_system_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDbSystemDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                update_db_system_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlDbSystemHelperCustom = get_custom_class("MysqlDbSystemHelperCustom")


class ResourceHelper(MysqlDbSystemHelperCustom, MysqlDbSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            fault_domain=dict(type="str"),
            configuration_id=dict(type="str"),
            shape_name=dict(type="str"),
            mysql_version=dict(type="str"),
            subnet_id=dict(type="str"),
            admin_username=dict(type="str"),
            admin_password=dict(type="str", no_log=True),
            data_storage_size_in_gbs=dict(type="int"),
            hostname_label=dict(type="str"),
            ip_address=dict(type="str"),
            port=dict(type="int"),
            port_x=dict(type="int"),
            backup_policy=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool"),
                    window_start_time=dict(type="str"),
                    retention_in_days=dict(type="int"),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            source=dict(
                type="dict",
                options=dict(
                    source_type=dict(
                        type="str", default="NONE", choices=["BACKUP", "IMPORTURL"]
                    ),
                    backup_id=dict(type="str"),
                    source_url=dict(type="str"),
                ),
            ),
            maintenance=dict(
                type="dict", options=dict(window_start_time=dict(type="str"))
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            db_system_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system",
        service_client_class=DbSystemClient,
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
