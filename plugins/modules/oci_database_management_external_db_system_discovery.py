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
module: oci_database_management_external_db_system_discovery
short_description: Manage an ExternalDbSystemDiscovery resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update, patch and delete an ExternalDbSystemDiscovery resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an external DB system discovery resource and initiates the discovery process.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    agent_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
              used for the external DB system discovery.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the external DB system resides.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly name for the DB system. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    items:
        description:
            - A sequence of instructions to apply to the resource.
        type: list
        elements: dict
        suboptions:
            operation:
                description:
                    - The type of operation.
                type: str
                choices:
                    - "MERGE"
                required: true
            selection:
                description:
                    - The set of values to which the operation applies as a L(JMESPath expression,https://jmespath.org/specification.html) for evaluation
                      against the context resource.
                      An operation fails if the selection yields an exception, except as otherwise specified.
                      Note that comparisons involving non-primitive values (objects or arrays) are not supported and will always evaluate to false.
                type: str
                required: true
            value:
                description:
                    - A value to be merged into the target.
                type: dict
    external_db_system_discovery_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system discovery.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExternalDbSystemDiscovery.
            - Use I(state=present) to create or update an ExternalDbSystemDiscovery.
            - Use I(state=absent) to delete an ExternalDbSystemDiscovery.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_db_system_discovery
  oci_database_management_external_db_system_discovery:
    # required
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example

- name: Update external_db_system_discovery
  oci_database_management_external_db_system_discovery:
    # required
    external_db_system_discovery_id: "ocid1.externaldbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example

- name: Update external_db_system_discovery using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_db_system_discovery:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

- name: Delete external_db_system_discovery
  oci_database_management_external_db_system_discovery:
    # required
    external_db_system_discovery_id: "ocid1.externaldbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_db_system_discovery using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_db_system_discovery:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
external_db_system_discovery:
    description:
        - Details of the ExternalDbSystemDiscovery resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        grid_home:
            description:
                - The directory in which Oracle Grid Infrastructure is installed.
            returned: on success
            type: str
            sample: grid_home_example
        discovered_components:
            description:
                - The list of DB system components that were found in the DB system discovery.
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
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
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
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import CreateExternalDbSystemDiscoveryDetails
    from oci.database_management.models import UpdateExternalDbSystemDiscoveryDetails
    from oci.database_management.models import PatchExternalDbSystemDiscoveryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemDiscoveryHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, patch, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ExternalDbSystemDiscoveryHelperGen, self
        ).get_possible_entity_types() + [
            "externaldbsystemdiscovery",
            "externaldbsystemdiscoveries",
            "databaseManagementexternaldbsystemdiscovery",
            "databaseManagementexternaldbsystemdiscoveries",
            "externaldbsystemdiscoveryresource",
            "externaldbsystemdiscoveriesresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_db_system_discovery_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_db_system_discovery_id")

    def get_get_fn(self):
        return self.client.get_external_db_system_discovery

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_discovery,
            external_db_system_discovery_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_discovery,
            external_db_system_discovery_id=self.module.params.get(
                "external_db_system_discovery_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_external_db_system_discoveries, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalDbSystemDiscoveryDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_db_system_discovery,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_db_system_discovery_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExternalDbSystemDiscoveryDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_db_system_discovery,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_discovery_id=self.module.params.get(
                    "external_db_system_discovery_id"
                ),
                update_external_db_system_discovery_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def get_patch_model_class(self):
        return PatchExternalDbSystemDiscoveryDetails

    def patch_resource(self):
        patch_details = self.get_patch_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.patch_external_db_system_discovery,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_discovery_id=self.module.params.get(
                    "external_db_system_discovery_id"
                ),
                patch_external_db_system_discovery_details=patch_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.PATCH_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.PATCH_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_external_db_system_discovery,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_discovery_id=self.module.params.get(
                    "external_db_system_discovery_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ExternalDbSystemDiscoveryHelperCustom = get_custom_class(
    "ExternalDbSystemDiscoveryHelperCustom"
)


class ResourceHelper(
    ExternalDbSystemDiscoveryHelperCustom, ExternalDbSystemDiscoveryHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            agent_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    operation=dict(type="str", required=True, choices=["MERGE"]),
                    selection=dict(type="str", required=True),
                    value=dict(type="dict"),
                ),
            ),
            external_db_system_discovery_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_db_system_discovery",
        service_client_class=DbManagementClient,
        namespace="database_management",
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
    elif resource_helper.is_patch_using_name():
        result = resource_helper.patch_using_name()
    elif resource_helper.is_patch():
        result = resource_helper.patch()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
