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
module: oci_mysql_db_system_facts
short_description: Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
    - Get a list of DB Systems in the specified compartment.
      The default sort order is by timeUpdated, descending.
    - If I(db_system_id) is specified, the details of a single DbSystem will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_system.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple db_systems.
        type: str
    is_analytics_cluster_attached:
        description:
            - If true, return only DB Systems with an Analytics Cluster attached, if false
              return only DB Systems with no Analytics Cluster attached. If not
              present, return all DB Systems.
        type: bool
    display_name:
        description:
            - A filter to return only the resource matching the given display name exactly.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - DbSystem Lifecycle State
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    configuration_id:
        description:
            - The requested Configuration instance.
        type: str
    is_up_to_date:
        description:
            - Filter instances if they are using the latest revision of the
              Configuration they are associated with.
        type: bool
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as
              ascending.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
    sort_order:
        description:
            - The sort order to use (ASC or DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List db_systems
  oci_mysql_db_system_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific db_system
  oci_mysql_db_system_facts:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
db_systems:
    description:
        - List of DbSystem resources
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
        is_analytics_cluster_attached:
            description:
                - If the DB System has an Analytics Cluster attached.
            returned: on success
            type: bool
            sample: true
        analytics_cluster:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape_name:
                    description:
                        - "The shape determines resources to allocate to the Analytics
                          Cluster nodes - CPU cores, memory."
                    returned: on success
                    type: string
                    sample: shape_name_example
                cluster_size:
                    description:
                        - The number of analytics-processing compute instances, of the
                          specified shape, in the Analytics Cluster.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the MySQL Analytics Cluster.
                    returned: on success
                    type: string
                    sample: lifecycle_state_example
                time_created:
                    description:
                        - The date and time the Analytics Cluster was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - The time the Analytics Cluster was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
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
        channels:
            description:
                - A list with a summary of all the Channels attached to the DB System.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the Channel.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                compartment_id:
                    description:
                        - The OCID of the compartment.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                is_enabled:
                    description:
                        - Whether the Channel has been enabled by the user.
                    returned: on success
                    type: bool
                    sample: true
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
                            sample: MYSQL
                        hostname:
                            description:
                                - The network address of the MySQL instance.
                            returned: on success
                            type: string
                            sample: hostname_example
                        port:
                            description:
                                - The port the source MySQL instance listens on.
                            returned: on success
                            type: int
                            sample: 56
                        username:
                            description:
                                - The name of the replication user on the source MySQL instance.
                                  The username has a maximum length of 96 characters. For more information,
                                  please see the L(MySQL documentation,https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)
                            returned: on success
                            type: string
                            sample: username_example
                        ssl_mode:
                            description:
                                - The SSL mode of the Channel.
                            returned: on success
                            type: string
                            sample: VERIFY_IDENTITY
                        ssl_ca_certificate:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                certificate_type:
                                    description:
                                        - The type of CA certificate.
                                    returned: on success
                                    type: string
                                    sample: PEM
                                contents:
                                    description:
                                        - The string containing the CA certificate in PEM format.
                                    returned: on success
                                    type: string
                                    sample: contents_example
                target:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        target_type:
                            description:
                                - The specific target identifier.
                            returned: on success
                            type: string
                            sample: DBSYSTEM
                        db_system_id:
                            description:
                                - The OCID of the source DB System.
                            returned: on success
                            type: string
                            sample: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
                        channel_name:
                            description:
                                - The case-insensitive name that identifies the replication channel. Channel names
                                  must follow the rules defined for L(MySQL identifiers,https://dev.mysql.com/doc/refman/8.0/en/identifiers.html).
                                  The names of non-Deleted Channels must be unique for each DB System.
                            returned: on success
                            type: string
                            sample: channel_name_example
                        applier_username:
                            description:
                                - The username for the replication applier of the target MySQL DB System.
                            returned: on success
                            type: string
                            sample: applier_username_example
                lifecycle_state:
                    description:
                        - The state of the Channel.
                    returned: on success
                    type: string
                    sample: lifecycle_state_example
                lifecycle_details:
                    description:
                        - A message describing the state of the Channel.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
                display_name:
                    description:
                        - The user-friendly name for the Channel. It does not have to be unique.
                    returned: on success
                    type: string
                    sample: display_name_example
                time_created:
                    description:
                        - The date and time the Channel was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - The time the Channel was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "is_analytics_cluster_attached": true,
        "analytics_cluster": {
            "shape_name": "shape_name_example",
            "cluster_size": 56,
            "lifecycle_state": "lifecycle_state_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        },
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
        "channels": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "is_enabled": true,
            "source": {
                "source_type": "MYSQL",
                "hostname": "hostname_example",
                "port": 56,
                "username": "username_example",
                "ssl_mode": "VERIFY_IDENTITY",
                "ssl_ca_certificate": {
                    "certificate_type": "PEM",
                    "contents": "contents_example"
                }
            },
            "target": {
                "target_type": "DBSYSTEM",
                "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
                "channel_name": "channel_name_example",
                "applier_username": "applier_username_example"
            },
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example",
            "display_name": "display_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import DbSystemClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlDbSystemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "is_analytics_cluster_attached",
            "db_system_id",
            "display_name",
            "lifecycle_state",
            "configuration_id",
            "is_up_to_date",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_systems,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlDbSystemFactsHelperCustom = get_custom_class("MysqlDbSystemFactsHelperCustom")


class ResourceFactsHelper(MysqlDbSystemFactsHelperCustom, MysqlDbSystemFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_system_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            is_analytics_cluster_attached=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            configuration_id=dict(type="str"),
            is_up_to_date=dict(type="bool"),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_systems=result)


if __name__ == "__main__":
    main()
