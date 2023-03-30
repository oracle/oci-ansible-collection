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
module: oci_golden_gate_connection_facts
short_description: Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
    - Lists the Connections in the compartment.
    - If I(connection_id) is specified, the details of a single Connection will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Connection.
            - Required to get a specific connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment that contains the work request. Work requests should be scoped
              to the same compartment as the resource the work request affects. If the work request concerns
              multiple resources, and those resources are not in the same compartment, it is up to the service team
              to pick the primary resource whose compartment should be used.
            - Required to list multiple connections.
        type: str
    technology_type:
        description:
            - The array of technology types.
        type: list
        elements: str
        choices:
            - "GOLDENGATE"
            - "OCI_AUTONOMOUS_DATABASE"
            - "OCI_AUTONOMOUS_JSON_DATABASE"
            - "OCI_MYSQL"
            - "OCI_OBJECT_STORAGE"
            - "OCI_STREAMING"
            - "ORACLE_DATABASE"
            - "ORACLE_EXADATA"
            - "ORACLE_NOSQL"
            - "ORACLE_WEBLOGIC_JMS"
            - "AMAZON_RDS_ORACLE"
            - "AMAZON_RDS_SQLSERVER"
            - "AMAZON_S3"
            - "AMAZON_AURORA_MYSQL"
            - "AMAZON_AURORA_POSTGRESQL"
            - "AMAZON_RDS_MARIADB"
            - "AMAZON_RDS_MYSQL"
            - "AMAZON_RDS_POSTGRESQL"
            - "APACHE_KAFKA"
            - "AZURE_COSMOS_DB_FOR_MONGODB"
            - "AZURE_DATA_LAKE_STORAGE"
            - "AZURE_EVENT_HUBS"
            - "AZURE_MYSQL"
            - "AZURE_POSTGRESQL"
            - "AZURE_SQLSERVER_MANAGED_INSTANCE"
            - "AZURE_SQLSERVER_NON_MANAGED_INSTANCE"
            - "AZURE_SYNAPSE_ANALYTICS"
            - "CONFLUENT_KAFKA"
            - "CONFLUENT_SCHEMA_REGISTRY"
            - "GOOGLE_CLOUD_SQL_MYSQL"
            - "GOOGLE_CLOUD_SQL_POSTGRESQL"
            - "HDFS"
            - "MARIADB"
            - "MICROSOFT_SQLSERVER"
            - "MONGODB"
            - "MYSQL_SERVER"
            - "POSTGRESQL_SERVER"
            - "SNOWFLAKE"
    connection_type:
        description:
            - The array of connection types.
        type: list
        elements: str
        choices:
            - "GOLDENGATE"
            - "KAFKA"
            - "KAFKA_SCHEMA_REGISTRY"
            - "MYSQL"
            - "JAVA_MESSAGE_SERVICE"
            - "MICROSOFT_SQLSERVER"
            - "OCI_OBJECT_STORAGE"
            - "ORACLE"
            - "AZURE_DATA_LAKE_STORAGE"
            - "POSTGRESQL"
            - "AZURE_SYNAPSE_ANALYTICS"
            - "SNOWFLAKE"
            - "AMAZON_S3"
            - "HDFS"
            - "ORACLE_NOSQL"
            - "MONGODB"
    assigned_deployment_id:
        description:
            - The OCID of the deployment which for the connection must be assigned.
        type: str
    assignable_deployment_id:
        description:
            - Filters for compatible connections which can be, but currently not assigned to the deployment specified by its id.
        type: str
    assignable_deployment_type:
        description:
            - Filters for connections which can be assigned to the latest version of the specified deployment type.
        type: str
        choices:
            - "OGG"
            - "DATABASE_ORACLE"
            - "BIGDATA"
            - "DATABASE_MICROSOFT_SQLSERVER"
            - "DATABASE_MYSQL"
            - "DATABASE_POSTGRESQL"
    lifecycle_state:
        description:
            - A filter to return only connections having the 'lifecycleState' given.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connection
  oci_golden_gate_connection_facts:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: List connections
  oci_golden_gate_connection_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    technology_type: [ "GOLDENGATE" ]
    connection_type: [ "GOLDENGATE" ]
    assigned_deployment_id: "ocid1.assigneddeployment.oc1..xxxxxxEXAMPLExxxxxx"
    assignable_deployment_id: "ocid1.assignabledeployment.oc1..xxxxxxEXAMPLExxxxxx"
    assignable_deployment_type: OGG
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
connections:
    description:
        - List of Connection resources
    returned: on success
    type: complex
    contains:
        access_key_id:
            description:
                - "Access key ID to access the Amazon S3 bucket.
                  e.g.: \\"this-is-not-the-secret\\""
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
        account_name:
            description:
                - Sets the Azure storage account name.
                - Returned for get operation
            returned: on success
            type: str
            sample: account_name_example
        azure_tenant_id:
            description:
                - "Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
                  e.g.: 14593954-d337-4a61-a364-9f758c64f97f"
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx"
        client_id:
            description:
                - "Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
                  e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d"
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint:
            description:
                - "Azure Storage service endpoint.
                  e.g: https://test.blob.core.windows.net"
                - Returned for get operation
            returned: on success
            type: str
            sample: endpoint_example
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        should_use_jndi:
            description:
                - If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        jndi_connection_factory:
            description:
                - "The Connection Factory can be looked up using this name.
                  e.g.: 'ConnectionFactory'"
                - Returned for get operation
            returned: on success
            type: str
            sample: jndi_connection_factory_example
        jndi_provider_url:
            description:
                - "The URL that Java Message Service will use to contact the JNDI provider.
                  e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'"
                - Returned for get operation
            returned: on success
            type: str
            sample: jndi_provider_url_example
        jndi_initial_context_factory:
            description:
                - "The implementation of javax.naming.spi.InitialContextFactory interface
                  that the client uses to obtain initial naming context.
                  e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'"
                - Returned for get operation
            returned: on success
            type: str
            sample: jndi_initial_context_factory_example
        jndi_security_principal:
            description:
                - "Specifies the identity of the principal (user) to be authenticated.
                  e.g.: 'admin2'"
                - Returned for get operation
            returned: on success
            type: str
            sample: jndi_security_principal_example
        connection_factory:
            description:
                - "The of Java class implementing javax.jms.ConnectionFactory interface
                  supplied by the Java Message Service provider.
                  e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'"
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_factory_example
        stream_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the stream pool being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        bootstrap_servers:
            description:
                - "Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
                  list of KafkaBootstrapServer objects specified by host/port.
                  Used for establishing the initial connection to the Kafka cluster.
                  Example: `\\"server1.example.com:9092,server2.example.com:9092\\"`"
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                host:
                    description:
                        - The name or address of a host.
                    returned: on success
                    type: str
                    sample: host_example
                port:
                    description:
                        - The port of an endpoint usually specified for a connection.
                    returned: on success
                    type: int
                    sample: 56
                private_ip:
                    description:
                        - The private IP address of the connection's endpoint in the customer's VCN, typically a
                          database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
                          In case the privateIp is provided, the subnetId must also be provided.
                          In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
                          In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.
                    returned: on success
                    type: str
                    sample: private_ip_example
        url:
            description:
                - "Kafka Schema Registry URL.
                  e.g.: 'https://server1.us.oracle.com:8081'"
                - Returned for get operation
            returned: on success
            type: str
            sample: url_example
        ssl_ca:
            description:
                - "Database Certificate - The base64 encoded content of pem file
                  containing the server public key (for 1-way SSL)."
                - Returned for get operation
            returned: on success
            type: str
            sample: ssl_ca_example
        should_validate_server_certificate:
            description:
                - If set to true, the driver validates the certificate that is sent by the database server.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        connection_string:
            description:
                - "JDBC connection string.
                  e.g.: 'jdbc:sqlserver://<synapse-workspace>.sql.azuresynapse.net:1433;database=<db-
                  name>;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'"
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_string_example
        session_mode:
            description:
                - "The mode of the database connection session to be established by the data client.
                  'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
                  Connection to a RAC database involves a redirection received from the SCAN listeners
                  to the database node to connect to. By default the mode would be DIRECT."
                - Returned for get operation
            returned: on success
            type: str
            sample: DIRECT
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Autonomous Json Database.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related OCI tenancy.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - "The name of the region. e.g.: us-ashburn-1"
                - Returned for get operation
            returned: on success
            type: str
            sample: us-phoenix-1
        user_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the OCI user who will access the Object Storage.
                  The user must have write access to the bucket they want to connect to.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - The name of the database.
                - Returned for get operation
            returned: on success
            type: str
            sample: database_name_example
        host:
            description:
                - The name or address of a host.
                - Returned for get operation
            returned: on success
            type: str
            sample: host_example
        port:
            description:
                - The port of an endpoint usually specified for a connection.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        additional_attributes:
            description:
                - An array of name-value pair attribute entries.
                  Used as additional parameters in connection string.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the property entry.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - The value of the property entry.
                    returned: on success
                    type: str
                    sample: value_example
        security_protocol:
            description:
                - Kafka security protocol.
                - Returned for get operation
            returned: on success
            type: str
            sample: SSL
        ssl_mode:
            description:
                - SSL modes for MySQL.
                - Returned for get operation
            returned: on success
            type: str
            sample: DISABLED
        private_ip:
            description:
                - The private IP address of the connection's endpoint in the customer's VCN, typically a
                  database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
                  In case the privateIp is provided, the subnetId must also be provided.
                  In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
                  In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.
                - Returned for get operation
            returned: on success
            type: str
            sample: private_ip_example
        technology_type:
            description:
                - The Amazon S3 technology type.
                - Returned for get operation
            returned: on success
            type: str
            sample: AMAZON_S3
        connection_url:
            description:
                - "Connectin URL of the Java Message Service, specifying the protocol, host, and port.
                  e.g.: 'mq://myjms.host.domain:7676'"
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_url_example
        authentication_type:
            description:
                - Used authentication mechanism to access Azure Data Lake Storage.
                - Returned for get operation
            returned: on success
            type: str
            sample: SHARED_KEY
        username:
            description:
                - The username Oracle GoldenGate uses to connect the associated system of the given technology.
                  This username must already exist and be available by the system/application to be connected to
                  and must conform to the case sensitivty requirments defined in it.
                - Returned for get operation
            returned: on success
            type: str
            sample: username_example
        connection_type:
            description:
                - The connection type.
            returned: on success
            type: str
            sample: GOLDENGATE
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection being
                  referenced.
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
        lifecycle_state:
            description:
                - Possible lifecycle states for connection.
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
        vault_id:
            description:
                - Refers to the customer's vault OCID.
                  If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
                  to manage secrets contained within this vault.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - Refers to the customer's master key OCID.
                  If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet being referenced.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        ingress_ips:
            description:
                - List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp.
                  Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.
            returned: on success
            type: complex
            contains:
                ingress_ip:
                    description:
                        - A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.
                    returned: on success
                    type: str
                    sample: ingress_ip_example
        nsg_ids:
            description:
                - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
            returned: on success
            type: list
            sample: []
    sample: [{
        "access_key_id": "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx",
        "account_name": "account_name_example",
        "azure_tenant_id": "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx",
        "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint": "endpoint_example",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "should_use_jndi": true,
        "jndi_connection_factory": "jndi_connection_factory_example",
        "jndi_provider_url": "jndi_provider_url_example",
        "jndi_initial_context_factory": "jndi_initial_context_factory_example",
        "jndi_security_principal": "jndi_security_principal_example",
        "connection_factory": "connection_factory_example",
        "stream_pool_id": "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx",
        "bootstrap_servers": [{
            "host": "host_example",
            "port": 56,
            "private_ip": "private_ip_example"
        }],
        "url": "url_example",
        "ssl_ca": "ssl_ca_example",
        "should_validate_server_certificate": true,
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_string": "connection_string_example",
        "session_mode": "DIRECT",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "region": "us-phoenix-1",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "database_name": "database_name_example",
        "host": "host_example",
        "port": 56,
        "additional_attributes": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "security_protocol": "SSL",
        "ssl_mode": "DISABLED",
        "private_ip": "private_ip_example",
        "technology_type": "AMAZON_S3",
        "connection_url": "connection_url_example",
        "authentication_type": "SHARED_KEY",
        "username": "username_example",
        "connection_type": "GOLDENGATE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ingress_ips": [{
            "ingress_ip": "ingress_ip_example"
        }],
        "nsg_ids": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "connection_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "technology_type",
            "connection_type",
            "assigned_deployment_id",
            "assignable_deployment_id",
            "assignable_deployment_type",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_connections,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ConnectionFactsHelperCustom = get_custom_class("ConnectionFactsHelperCustom")


class ResourceFactsHelper(ConnectionFactsHelperCustom, ConnectionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            technology_type=dict(
                type="list",
                elements="str",
                choices=[
                    "GOLDENGATE",
                    "OCI_AUTONOMOUS_DATABASE",
                    "OCI_AUTONOMOUS_JSON_DATABASE",
                    "OCI_MYSQL",
                    "OCI_OBJECT_STORAGE",
                    "OCI_STREAMING",
                    "ORACLE_DATABASE",
                    "ORACLE_EXADATA",
                    "ORACLE_NOSQL",
                    "ORACLE_WEBLOGIC_JMS",
                    "AMAZON_RDS_ORACLE",
                    "AMAZON_RDS_SQLSERVER",
                    "AMAZON_S3",
                    "AMAZON_AURORA_MYSQL",
                    "AMAZON_AURORA_POSTGRESQL",
                    "AMAZON_RDS_MARIADB",
                    "AMAZON_RDS_MYSQL",
                    "AMAZON_RDS_POSTGRESQL",
                    "APACHE_KAFKA",
                    "AZURE_COSMOS_DB_FOR_MONGODB",
                    "AZURE_DATA_LAKE_STORAGE",
                    "AZURE_EVENT_HUBS",
                    "AZURE_MYSQL",
                    "AZURE_POSTGRESQL",
                    "AZURE_SQLSERVER_MANAGED_INSTANCE",
                    "AZURE_SQLSERVER_NON_MANAGED_INSTANCE",
                    "AZURE_SYNAPSE_ANALYTICS",
                    "CONFLUENT_KAFKA",
                    "CONFLUENT_SCHEMA_REGISTRY",
                    "GOOGLE_CLOUD_SQL_MYSQL",
                    "GOOGLE_CLOUD_SQL_POSTGRESQL",
                    "HDFS",
                    "MARIADB",
                    "MICROSOFT_SQLSERVER",
                    "MONGODB",
                    "MYSQL_SERVER",
                    "POSTGRESQL_SERVER",
                    "SNOWFLAKE",
                ],
            ),
            connection_type=dict(
                type="list",
                elements="str",
                choices=[
                    "GOLDENGATE",
                    "KAFKA",
                    "KAFKA_SCHEMA_REGISTRY",
                    "MYSQL",
                    "JAVA_MESSAGE_SERVICE",
                    "MICROSOFT_SQLSERVER",
                    "OCI_OBJECT_STORAGE",
                    "ORACLE",
                    "AZURE_DATA_LAKE_STORAGE",
                    "POSTGRESQL",
                    "AZURE_SYNAPSE_ANALYTICS",
                    "SNOWFLAKE",
                    "AMAZON_S3",
                    "HDFS",
                    "ORACLE_NOSQL",
                    "MONGODB",
                ],
            ),
            assigned_deployment_id=dict(type="str"),
            assignable_deployment_id=dict(type="str"),
            assignable_deployment_type=dict(
                type="str",
                choices=[
                    "OGG",
                    "DATABASE_ORACLE",
                    "BIGDATA",
                    "DATABASE_MICROSOFT_SQLSERVER",
                    "DATABASE_MYSQL",
                    "DATABASE_POSTGRESQL",
                ],
            ),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connection",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(connections=result)


if __name__ == "__main__":
    main()
