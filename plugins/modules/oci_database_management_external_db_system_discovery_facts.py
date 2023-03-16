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
module: oci_database_management_external_db_system_discovery_facts
short_description: Fetches details about one or multiple ExternalDbSystemDiscovery resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalDbSystemDiscovery resources in Oracle Cloud Infrastructure
    - Lists the external DB system discovery resources in the specified compartment.
    - If I(external_db_system_discovery_id) is specified, the details of a single ExternalDbSystemDiscovery will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_db_system_discovery_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system discovery.
            - Required to get a specific external_db_system_discovery.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple external_db_system_discoveries.
        type: str
    display_name:
        description:
            - A filter to only return the resources that match the entire display name.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending.
              The `DISPLAYNAME` sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_db_system_discovery
  oci_database_management_external_db_system_discovery_facts:
    # required
    external_db_system_discovery_id: "ocid1.externaldbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_db_system_discoveries
  oci_database_management_external_db_system_discovery_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_db_system_discoveries:
    description:
        - List of ExternalDbSystemDiscovery resources
    returned: on success
    type: complex
    contains:
        grid_home:
            description:
                - The directory in which Oracle Grid Infrastructure is installed.
                - Returned for get operation
            returned: on success
            type: str
            sample: grid_home_example
        discovered_components:
            description:
                - The list of DB system components that were found in the DB system discovery.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_flex_enabled:
                    description:
                        - Indicates whether Oracle Flex ASM is enabled or not.
                    returned: on success
                    type: bool
                    sample: true
                asm_instances:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        component_id:
                            description:
                                - The identifier of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - The user-friendly name for the discovered DB system component. The name does not have to be unique.
                            returned: on success
                            type: str
                            sample: display_name_example
                        component_name:
                            description:
                                - The name of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: component_name_example
                        component_type:
                            description:
                                - The external DB system component type.
                            returned: on success
                            type: str
                            sample: ASM
                        resource_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the existing OCI resource matching the
                                  discovered DB system component.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        is_selected_for_monitoring:
                            description:
                                - Indicates whether the DB system component should be provisioned as an OCI resource or not.
                            returned: on success
                            type: bool
                            sample: true
                        status:
                            description:
                                - The state of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: NEW
                        associated_components:
                            description:
                                - The list of associated components.
                            returned: on success
                            type: complex
                            contains:
                                component_id:
                                    description:
                                        - The identifier of the associated component.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                                component_type:
                                    description:
                                        - The type of associated component.
                                    returned: on success
                                    type: str
                                    sample: ASM
                                association_type:
                                    description:
                                        - The association type.
                                    returned: on success
                                    type: str
                                    sample: CONTAINS
                        host_name:
                            description:
                                - The name of the host on which the ASM instance is running.
                            returned: on success
                            type: str
                            sample: host_name_example
                        instance_name:
                            description:
                                - The name of the ASM instance.
                            returned: on success
                            type: str
                            sample: instance_name_example
                        adr_home_directory:
                            description:
                                - The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.
                            returned: on success
                            type: str
                            sample: adr_home_directory_example
                instance_name:
                    description:
                        - The name of the ASM instance.
                    returned: on success
                    type: str
                    sample: instance_name_example
                grid_home:
                    description:
                        - The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.
                    returned: on success
                    type: str
                    sample: grid_home_example
                is_flex_cluster:
                    description:
                        - Indicates whether the cluster is an Oracle Flex Cluster or not.
                    returned: on success
                    type: bool
                    sample: true
                network_configurations:
                    description:
                        - The list of network address configurations of the external cluster.
                    returned: on success
                    type: complex
                    contains:
                        network_number:
                            description:
                                - The network number.
                            returned: on success
                            type: int
                            sample: 56
                        network_type:
                            description:
                                - The network type.
                            returned: on success
                            type: str
                            sample: AUTOCONFIG
                        subnet:
                            description:
                                - The subnet for the network.
                            returned: on success
                            type: str
                            sample: subnet_example
                vip_configurations:
                    description:
                        - The list of Virtual IP (VIP) configurations of the external cluster.
                    returned: on success
                    type: complex
                    contains:
                        node_name:
                            description:
                                - The name of the node with the VIP.
                            returned: on success
                            type: str
                            sample: node_name_example
                        address:
                            description:
                                - The VIP name or IP address.
                            returned: on success
                            type: str
                            sample: address_example
                        network_number:
                            description:
                                - The network number from which VIPs are obtained.
                            returned: on success
                            type: int
                            sample: 56
                scan_configurations:
                    description:
                        - The list of Single Client Access Name (SCAN) configurations of the external cluster.
                    returned: on success
                    type: complex
                    contains:
                        scan_name:
                            description:
                                - The name of the SCAN listener.
                            returned: on success
                            type: str
                            sample: scan_name_example
                        network_number:
                            description:
                                - The network number from which SCAN VIPs are obtained.
                            returned: on success
                            type: int
                            sample: 56
                        scan_port:
                            description:
                                - The port number of the SCAN listener.
                            returned: on success
                            type: int
                            sample: 56
                        scan_protocol:
                            description:
                                - The protocol of the SCAN listener.
                            returned: on success
                            type: str
                            sample: TCP
                ocr_file_location:
                    description:
                        - The location of the Oracle Cluster Registry (OCR) file.
                    returned: on success
                    type: str
                    sample: ocr_file_location_example
                cluster_instances:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        component_id:
                            description:
                                - The identifier of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - The user-friendly name for the discovered DB system component. The name does not have to be unique.
                            returned: on success
                            type: str
                            sample: display_name_example
                        component_name:
                            description:
                                - The name of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: component_name_example
                        component_type:
                            description:
                                - The external DB system component type.
                            returned: on success
                            type: str
                            sample: ASM
                        resource_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the existing OCI resource matching the
                                  discovered DB system component.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        is_selected_for_monitoring:
                            description:
                                - Indicates whether the DB system component should be provisioned as an OCI resource or not.
                            returned: on success
                            type: bool
                            sample: true
                        status:
                            description:
                                - The state of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: NEW
                        associated_components:
                            description:
                                - The list of associated components.
                            returned: on success
                            type: complex
                            contains:
                                component_id:
                                    description:
                                        - The identifier of the associated component.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                                component_type:
                                    description:
                                        - The type of associated component.
                                    returned: on success
                                    type: str
                                    sample: ASM
                                association_type:
                                    description:
                                        - The association type.
                                    returned: on success
                                    type: str
                                    sample: CONTAINS
                        host_name:
                            description:
                                - The name of the host on which the cluster instance is running.
                            returned: on success
                            type: str
                            sample: host_name_example
                        cluster_id:
                            description:
                                - The unique identifier of the Oracle cluster.
                            returned: on success
                            type: str
                            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
                        node_role:
                            description:
                                - The role of the cluster node.
                            returned: on success
                            type: str
                            sample: HUB
                        crs_base_directory:
                            description:
                                - The Oracle base location of Cluster Ready Services (CRS).
                            returned: on success
                            type: str
                            sample: crs_base_directory_example
                        adr_home_directory:
                            description:
                                - The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
                            returned: on success
                            type: str
                            sample: adr_home_directory_example
                        connector:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                connector_type:
                                    description:
                                        - The type of connector.
                                    returned: on success
                                    type: str
                                    sample: MACS
                                display_name:
                                    description:
                                        - The user-friendly name for the external connector. The name does not have to be unique.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                connection_status:
                                    description:
                                        - The status of connectivity to the external DB system component.
                                    returned: on success
                                    type: str
                                    sample: connection_status_example
                                connection_failure_message:
                                    description:
                                        - The error message indicating the reason for connection failure or `null` if
                                          the connection was successful.
                                    returned: on success
                                    type: str
                                    sample: connection_failure_message_example
                                time_connection_status_last_updated:
                                    description:
                                        - The date and time the connectionStatus of the external DB system connector was last updated.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                                agent_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
                                          used for the external DB system connector.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
                                connection_info:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        component_type:
                                            description:
                                                - The component type.
                                            returned: on success
                                            type: str
                                            sample: DATABASE
                                        connection_string:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                hosts:
                                                    description:
                                                        - The list of host names of the ASM instances.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                port:
                                                    description:
                                                        - The port used to connect to the ASM instance.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                service:
                                                    description:
                                                        - The service name of the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: service_example
                                                protocol:
                                                    description:
                                                        - The protocol used to connect to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: TCP
                                                host_name:
                                                    description:
                                                        - The host name of the database or the SCAN name in case of a RAC database.
                                                    returned: on success
                                                    type: str
                                                    sample: host_name_example
                                        connection_credentials:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                user_name:
                                                    description:
                                                        - The user name used to connect to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: user_name_example
                                                password_secret_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret
                                                          containing the user password.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                                role:
                                                    description:
                                                        - The role of the user connecting to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: SYSASM
                                                credential_type:
                                                    description:
                                                        - The type of credential used to connect to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: NAME_REFERENCE
                                                credential_name:
                                                    description:
                                                        - "The name of the credential information that used to connect to the DB system resource.
                                                          The name should be in \\"x.y\\" format, where the length of \\"x\\" has a maximum of 64 characters,
                                                          and length of \\"y\\" has a maximum of 199 characters. The name strings can contain letters,
                                                          numbers and the underscore character only. Other characters are not valid, except for
                                                          the \\".\\" character that separates the \\"x\\" and \\"y\\" portions of the name.
                                                          *IMPORTANT* - The name must be unique within the OCI region the credential is being created in.
                                                          If you specify a name that duplicates the name of another credential within the same OCI region,
                                                          you may overwrite or corrupt the credential that is already using the name."
                                                        - "For example: inventorydb.abc112233445566778899"
                                                    returned: on success
                                                    type: str
                                                    sample: credential_name_example
                                                ssl_secret_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret
                                                          containing the SSL keystore and truststore details.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
                cluster_id:
                    description:
                        - The unique identifier of the Oracle cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
                node_role:
                    description:
                        - The role of the cluster node.
                    returned: on success
                    type: str
                    sample: HUB
                crs_base_directory:
                    description:
                        - The Oracle base location of Cluster Ready Services (CRS).
                    returned: on success
                    type: str
                    sample: crs_base_directory_example
                db_unique_name:
                    description:
                        - The `DB_UNIQUE_NAME` of the external database.
                    returned: on success
                    type: str
                    sample: db_unique_name_example
                db_type:
                    description:
                        - The type of Oracle Database. Indicates whether the database is a Container Database,
                          Pluggable Database, or a Non-container Database.
                    returned: on success
                    type: str
                    sample: CDB
                is_cluster:
                    description:
                        - Indicates whether the Oracle Database is part of a cluster.
                    returned: on success
                    type: bool
                    sample: true
                db_edition:
                    description:
                        - The Oracle Database edition.
                    returned: on success
                    type: str
                    sample: db_edition_example
                db_id:
                    description:
                        - The Oracle Database ID.
                    returned: on success
                    type: str
                    sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
                db_packs:
                    description:
                        - The database packs licensed for the external Oracle Database.
                    returned: on success
                    type: str
                    sample: db_packs_example
                db_role:
                    description:
                        - The role of the Oracle Database in Oracle Data Guard configuration.
                    returned: on success
                    type: str
                    sample: LOGICAL_STANDBY
                db_version:
                    description:
                        - The Oracle Database version.
                    returned: on success
                    type: str
                    sample: db_version_example
                pluggable_databases:
                    description:
                        - The list of Pluggable Databases.
                    returned: on success
                    type: complex
                    contains:
                        component_id:
                            description:
                                - The identifier of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - The user-friendly name for the discovered DB system component. The name does not have to be unique.
                            returned: on success
                            type: str
                            sample: display_name_example
                        component_name:
                            description:
                                - The name of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: component_name_example
                        component_type:
                            description:
                                - The external DB system component type.
                            returned: on success
                            type: str
                            sample: ASM
                        resource_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the existing OCI resource matching the
                                  discovered DB system component.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        is_selected_for_monitoring:
                            description:
                                - Indicates whether the DB system component should be provisioned as an OCI resource or not.
                            returned: on success
                            type: bool
                            sample: true
                        status:
                            description:
                                - The state of the discovered DB system component.
                            returned: on success
                            type: str
                            sample: NEW
                        associated_components:
                            description:
                                - The list of associated components.
                            returned: on success
                            type: complex
                            contains:
                                component_id:
                                    description:
                                        - The identifier of the associated component.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                                component_type:
                                    description:
                                        - The type of associated component.
                                    returned: on success
                                    type: str
                                    sample: ASM
                                association_type:
                                    description:
                                        - The association type.
                                    returned: on success
                                    type: str
                                    sample: CONTAINS
                        compartment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        container_database_id:
                            description:
                                - The unique identifier of the parent Container Database (CDB).
                            returned: on success
                            type: str
                            sample: "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
                        guid:
                            description:
                                - The unique identifier of the PDB.
                            returned: on success
                            type: str
                            sample: guid_example
                        connector:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                connector_type:
                                    description:
                                        - The type of connector.
                                    returned: on success
                                    type: str
                                    sample: MACS
                                display_name:
                                    description:
                                        - The user-friendly name for the external connector. The name does not have to be unique.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                connection_status:
                                    description:
                                        - The status of connectivity to the external DB system component.
                                    returned: on success
                                    type: str
                                    sample: connection_status_example
                                connection_failure_message:
                                    description:
                                        - The error message indicating the reason for connection failure or `null` if
                                          the connection was successful.
                                    returned: on success
                                    type: str
                                    sample: connection_failure_message_example
                                time_connection_status_last_updated:
                                    description:
                                        - The date and time the connectionStatus of the external DB system connector was last updated.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                                agent_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
                                          used for the external DB system connector.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
                                connection_info:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        component_type:
                                            description:
                                                - The component type.
                                            returned: on success
                                            type: str
                                            sample: DATABASE
                                        connection_string:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                hosts:
                                                    description:
                                                        - The list of host names of the ASM instances.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                port:
                                                    description:
                                                        - The port used to connect to the ASM instance.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                service:
                                                    description:
                                                        - The service name of the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: service_example
                                                protocol:
                                                    description:
                                                        - The protocol used to connect to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: TCP
                                                host_name:
                                                    description:
                                                        - The host name of the database or the SCAN name in case of a RAC database.
                                                    returned: on success
                                                    type: str
                                                    sample: host_name_example
                                        connection_credentials:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                user_name:
                                                    description:
                                                        - The user name used to connect to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: user_name_example
                                                password_secret_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret
                                                          containing the user password.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                                role:
                                                    description:
                                                        - The role of the user connecting to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: SYSASM
                                                credential_type:
                                                    description:
                                                        - The type of credential used to connect to the ASM instance.
                                                    returned: on success
                                                    type: str
                                                    sample: NAME_REFERENCE
                                                credential_name:
                                                    description:
                                                        - "The name of the credential information that used to connect to the DB system resource.
                                                          The name should be in \\"x.y\\" format, where the length of \\"x\\" has a maximum of 64 characters,
                                                          and length of \\"y\\" has a maximum of 199 characters. The name strings can contain letters,
                                                          numbers and the underscore character only. Other characters are not valid, except for
                                                          the \\".\\" character that separates the \\"x\\" and \\"y\\" portions of the name.
                                                          *IMPORTANT* - The name must be unique within the OCI region the credential is being created in.
                                                          If you specify a name that duplicates the name of another credential within the same OCI region,
                                                          you may overwrite or corrupt the credential that is already using the name."
                                                        - "For example: inventorydb.abc112233445566778899"
                                                    returned: on success
                                                    type: str
                                                    sample: credential_name_example
                                                ssl_secret_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret
                                                          containing the SSL keystore and truststore details.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
                home_directory:
                    description:
                        - The location of the DB home.
                    returned: on success
                    type: str
                    sample: home_directory_example
                cpu_core_count:
                    description:
                        - The number of CPU cores available on the DB node.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_size_in_gbs:
                    description:
                        - The total memory in gigabytes (GB) on the DB node.
                    returned: on success
                    type: float
                    sample: 3.4
                db_node_name:
                    description:
                        - The name of the DB node.
                    returned: on success
                    type: str
                    sample: db_node_name_example
                oracle_home:
                    description:
                        - The Oracle home location of the listener.
                    returned: on success
                    type: str
                    sample: oracle_home_example
                listener_alias:
                    description:
                        - The listener alias.
                    returned: on success
                    type: str
                    sample: listener_alias_example
                adr_home_directory:
                    description:
                        - The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.
                    returned: on success
                    type: str
                    sample: adr_home_directory_example
                log_directory:
                    description:
                        - The destination directory of the listener log file.
                    returned: on success
                    type: str
                    sample: log_directory_example
                trace_directory:
                    description:
                        - The destination directory of the listener trace file.
                    returned: on success
                    type: str
                    sample: trace_directory_example
                version:
                    description:
                        - The ASM version.
                    returned: on success
                    type: str
                    sample: version_example
                listener_type:
                    description:
                        - The type of listener.
                    returned: on success
                    type: str
                    sample: ASM
                host_name:
                    description:
                        - The name of the host on which the ASM instance is running.
                    returned: on success
                    type: str
                    sample: host_name_example
                endpoints:
                    description:
                        - The list of protocol addresses the listener is configured to listen on.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique name of the service.
                            returned: on success
                            type: str
                            sample: key_example
                        protocol:
                            description:
                                - The listener protocol.
                            returned: on success
                            type: str
                            sample: IPC
                        services:
                            description:
                                - The list of services registered with the listener.
                            returned: on success
                            type: list
                            sample: []
                        host:
                            description:
                                - The host name or IP address.
                            returned: on success
                            type: str
                            sample: host_example
                        port:
                            description:
                                - The port number.
                            returned: on success
                            type: int
                            sample: 56
                component_id:
                    description:
                        - The identifier of the discovered DB system component.
                    returned: on success
                    type: str
                    sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The user-friendly name for the discovered DB system component. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                component_name:
                    description:
                        - The name of the discovered DB system component.
                    returned: on success
                    type: str
                    sample: component_name_example
                component_type:
                    description:
                        - The external DB system component type.
                    returned: on success
                    type: str
                    sample: ASM
                resource_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the existing OCI resource matching the
                          discovered DB system component.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                is_selected_for_monitoring:
                    description:
                        - Indicates whether the DB system component should be provisioned as an OCI resource or not.
                    returned: on success
                    type: bool
                    sample: true
                status:
                    description:
                        - The state of the discovered DB system component.
                    returned: on success
                    type: str
                    sample: NEW
                associated_components:
                    description:
                        - The list of associated components.
                    returned: on success
                    type: complex
                    contains:
                        component_id:
                            description:
                                - The identifier of the associated component.
                            returned: on success
                            type: str
                            sample: "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx"
                        component_type:
                            description:
                                - The type of associated component.
                            returned: on success
                            type: str
                            sample: ASM
                        association_type:
                            description:
                                - The association type.
                            returned: on success
                            type: str
                            sample: CONTAINS
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                container_database_id:
                    description:
                        - The unique identifier of the parent Container Database (CDB).
                    returned: on success
                    type: str
                    sample: "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
                guid:
                    description:
                        - The unique identifier of the PDB.
                    returned: on success
                    type: str
                    sample: guid_example
                connector:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        connector_type:
                            description:
                                - The type of connector.
                            returned: on success
                            type: str
                            sample: MACS
                        display_name:
                            description:
                                - The user-friendly name for the external connector. The name does not have to be unique.
                            returned: on success
                            type: str
                            sample: display_name_example
                        connection_status:
                            description:
                                - The status of connectivity to the external DB system component.
                            returned: on success
                            type: str
                            sample: connection_status_example
                        connection_failure_message:
                            description:
                                - The error message indicating the reason for connection failure or `null` if
                                  the connection was successful.
                            returned: on success
                            type: str
                            sample: connection_failure_message_example
                        time_connection_status_last_updated:
                            description:
                                - The date and time the connectionStatus of the external DB system connector was last updated.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        agent_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
                                  used for the external DB system connector.
                            returned: on success
                            type: str
                            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
                        connection_info:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                component_type:
                                    description:
                                        - The component type.
                                    returned: on success
                                    type: str
                                    sample: DATABASE
                                connection_string:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        hosts:
                                            description:
                                                - The list of host names of the ASM instances.
                                            returned: on success
                                            type: list
                                            sample: []
                                        port:
                                            description:
                                                - The port used to connect to the ASM instance.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        service:
                                            description:
                                                - The service name of the ASM instance.
                                            returned: on success
                                            type: str
                                            sample: service_example
                                        protocol:
                                            description:
                                                - The protocol used to connect to the ASM instance.
                                            returned: on success
                                            type: str
                                            sample: TCP
                                        host_name:
                                            description:
                                                - The host name of the database or the SCAN name in case of a RAC database.
                                            returned: on success
                                            type: str
                                            sample: host_name_example
                                connection_credentials:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        user_name:
                                            description:
                                                - The user name used to connect to the ASM instance.
                                            returned: on success
                                            type: str
                                            sample: user_name_example
                                        password_secret_id:
                                            description:
                                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing
                                                  the user password.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                        role:
                                            description:
                                                - The role of the user connecting to the ASM instance.
                                            returned: on success
                                            type: str
                                            sample: SYSASM
                                        credential_type:
                                            description:
                                                - The type of credential used to connect to the ASM instance.
                                            returned: on success
                                            type: str
                                            sample: NAME_REFERENCE
                                        credential_name:
                                            description:
                                                - "The name of the credential information that used to connect to the DB system resource.
                                                  The name should be in \\"x.y\\" format, where the length of \\"x\\" has a maximum of 64 characters,
                                                  and length of \\"y\\" has a maximum of 199 characters. The name strings can contain letters,
                                                  numbers and the underscore character only. Other characters are not valid, except for
                                                  the \\".\\" character that separates the \\"x\\" and \\"y\\" portions of the name.
                                                  *IMPORTANT* - The name must be unique within the OCI region the credential is being created in.
                                                  If you specify a name that duplicates the name of another credential within the same OCI region,
                                                  you may overwrite or corrupt the credential that is already using the name."
                                                - "For example: inventorydb.abc112233445566778899"
                                            returned: on success
                                            type: str
                                            sample: credential_name_example
                                        ssl_secret_id:
                                            description:
                                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing
                                                  the SSL keystore and truststore details.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the existing OCI resource matching the discovered DB
                  system.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system discovery.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the DB system. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
                  used for the external DB system discovery.
            returned: on success
            type: str
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB system discovery resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external DB system discovery was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB system discovery was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "grid_home": "grid_home_example",
        "discovered_components": [{
            "is_flex_enabled": true,
            "asm_instances": [{
                "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "component_name": "component_name_example",
                "component_type": "ASM",
                "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "is_selected_for_monitoring": true,
                "status": "NEW",
                "associated_components": [{
                    "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                    "component_type": "ASM",
                    "association_type": "CONTAINS"
                }],
                "host_name": "host_name_example",
                "instance_name": "instance_name_example",
                "adr_home_directory": "adr_home_directory_example"
            }],
            "instance_name": "instance_name_example",
            "grid_home": "grid_home_example",
            "is_flex_cluster": true,
            "network_configurations": [{
                "network_number": 56,
                "network_type": "AUTOCONFIG",
                "subnet": "subnet_example"
            }],
            "vip_configurations": [{
                "node_name": "node_name_example",
                "address": "address_example",
                "network_number": 56
            }],
            "scan_configurations": [{
                "scan_name": "scan_name_example",
                "network_number": 56,
                "scan_port": 56,
                "scan_protocol": "TCP"
            }],
            "ocr_file_location": "ocr_file_location_example",
            "cluster_instances": [{
                "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "component_name": "component_name_example",
                "component_type": "ASM",
                "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "is_selected_for_monitoring": true,
                "status": "NEW",
                "associated_components": [{
                    "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                    "component_type": "ASM",
                    "association_type": "CONTAINS"
                }],
                "host_name": "host_name_example",
                "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
                "node_role": "HUB",
                "crs_base_directory": "crs_base_directory_example",
                "adr_home_directory": "adr_home_directory_example",
                "connector": {
                    "connector_type": "MACS",
                    "display_name": "display_name_example",
                    "connection_status": "connection_status_example",
                    "connection_failure_message": "connection_failure_message_example",
                    "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
                    "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
                    "connection_info": {
                        "component_type": "DATABASE",
                        "connection_string": {
                            "hosts": [],
                            "port": 56,
                            "service": "service_example",
                            "protocol": "TCP",
                            "host_name": "host_name_example"
                        },
                        "connection_credentials": {
                            "user_name": "user_name_example",
                            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
                            "role": "SYSASM",
                            "credential_type": "NAME_REFERENCE",
                            "credential_name": "credential_name_example",
                            "ssl_secret_id": "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
                        }
                    }
                }
            }],
            "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
            "node_role": "HUB",
            "crs_base_directory": "crs_base_directory_example",
            "db_unique_name": "db_unique_name_example",
            "db_type": "CDB",
            "is_cluster": true,
            "db_edition": "db_edition_example",
            "db_id": "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx",
            "db_packs": "db_packs_example",
            "db_role": "LOGICAL_STANDBY",
            "db_version": "db_version_example",
            "pluggable_databases": [{
                "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "component_name": "component_name_example",
                "component_type": "ASM",
                "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "is_selected_for_monitoring": true,
                "status": "NEW",
                "associated_components": [{
                    "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                    "component_type": "ASM",
                    "association_type": "CONTAINS"
                }],
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "container_database_id": "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
                "guid": "guid_example",
                "connector": {
                    "connector_type": "MACS",
                    "display_name": "display_name_example",
                    "connection_status": "connection_status_example",
                    "connection_failure_message": "connection_failure_message_example",
                    "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
                    "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
                    "connection_info": {
                        "component_type": "DATABASE",
                        "connection_string": {
                            "hosts": [],
                            "port": 56,
                            "service": "service_example",
                            "protocol": "TCP",
                            "host_name": "host_name_example"
                        },
                        "connection_credentials": {
                            "user_name": "user_name_example",
                            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
                            "role": "SYSASM",
                            "credential_type": "NAME_REFERENCE",
                            "credential_name": "credential_name_example",
                            "ssl_secret_id": "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
                        }
                    }
                }
            }],
            "home_directory": "home_directory_example",
            "cpu_core_count": 3.4,
            "memory_size_in_gbs": 3.4,
            "db_node_name": "db_node_name_example",
            "oracle_home": "oracle_home_example",
            "listener_alias": "listener_alias_example",
            "adr_home_directory": "adr_home_directory_example",
            "log_directory": "log_directory_example",
            "trace_directory": "trace_directory_example",
            "version": "version_example",
            "listener_type": "ASM",
            "host_name": "host_name_example",
            "endpoints": [{
                "key": "key_example",
                "protocol": "IPC",
                "services": [],
                "host": "host_example",
                "port": 56
            }],
            "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "component_name": "component_name_example",
            "component_type": "ASM",
            "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "is_selected_for_monitoring": true,
            "status": "NEW",
            "associated_components": [{
                "component_id": "ocid1.component.oc1..xxxxxxEXAMPLExxxxxx",
                "component_type": "ASM",
                "association_type": "CONTAINS"
            }],
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "container_database_id": "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
            "guid": "guid_example",
            "connector": {
                "connector_type": "MACS",
                "display_name": "display_name_example",
                "connection_status": "connection_status_example",
                "connection_failure_message": "connection_failure_message_example",
                "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
                "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
                "connection_info": {
                    "component_type": "DATABASE",
                    "connection_string": {
                        "hosts": [],
                        "port": 56,
                        "service": "service_example",
                        "protocol": "TCP",
                        "host_name": "host_name_example"
                    },
                    "connection_credentials": {
                        "user_name": "user_name_example",
                        "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
                        "role": "SYSASM",
                        "credential_type": "NAME_REFERENCE",
                        "credential_name": "credential_name_example",
                        "ssl_secret_id": "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
                    }
                }
            }
        }],
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemDiscoveryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_db_system_discovery_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_discovery,
            external_db_system_discovery_id=self.module.params.get(
                "external_db_system_discovery_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_db_system_discoveries,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ExternalDbSystemDiscoveryFactsHelperCustom = get_custom_class(
    "ExternalDbSystemDiscoveryFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalDbSystemDiscoveryFactsHelperCustom, ExternalDbSystemDiscoveryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_db_system_discovery_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_db_system_discovery",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_db_system_discoveries=result)


if __name__ == "__main__":
    main()
