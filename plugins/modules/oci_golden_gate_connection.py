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
module: oci_golden_gate_connection
short_description: Manage a Connection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Connection.
    - "This resource has the following action operations in the M(oracle.oci.oci_golden_gate_connection_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet being referenced.
        type: str
    technology_type:
        description:
            - The PostgreSQL technology type.
            - Required for create using I(state=present).
        type: str
    wallet:
        description:
            - The wallet contents Oracle GoldenGate uses to make connections to a database.  This
              attribute is expected to be base64 encoded.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    session_mode:
        description:
            - "The mode of the database connection session to be established by the data client.
              'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
              Connection to a RAC database involves a redirection received from the SCAN listeners
              to the database node to connect to. By default the mode would be DIRECT."
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Autonomous Json Database.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MONGODB', 'ORACLE']
        type: str
    account_name:
        description:
            - Sets the Azure storage account name.
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
            - Required when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    account_key:
        description:
            - "Azure storage account key. This property is required when 'authenticationType' is set to 'SHARED_KEY'.
              e.g.: pa3WbhVATzj56xD4DH1VjOUhApRGEGHvOo58eQJVWIzX+j8j4CUVFcTjpIqDSRaSa1Wo2LbWY5at+AStEgLOIQ=="
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    sas_token:
        description:
            - "Credential that uses a shared access signature (SAS) to authenticate to an Azure Service. This property is
              required when 'authenticationType' is set to 'SHARED_ACCESS_SIGNATURE'.
              e.g.: ?sv=2020-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2020-09-10T20:27:28Z&st=2022-08-05T12:27:28Z&spr=https&sig=C1IgHsiLBmTSStYkXXGLTP8it0xBrArcg
              CqOsZbXwIQ%3D"
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    azure_tenant_id:
        description:
            - "Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
              e.g.: 14593954-d337-4a61-a364-9f758c64f97f"
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    client_id:
        description:
            - "Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
              e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d"
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    client_secret:
        description:
            - "Azure client secret (aka application password) for authentication. This property is required when 'authenticationType' is set to
              'AZURE_ACTIVE_DIRECTORY'.
              e.g.: dO29Q~F5-VwnA.lZdd11xFF_t5NAXCaGwDl9NbT1"
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    endpoint:
        description:
            - "Azure Storage service endpoint.
              e.g: https://test.blob.core.windows.net"
            - This parameter is updatable.
            - Applicable when connection_type is 'AZURE_DATA_LAKE_STORAGE'
        type: str
    should_use_jndi:
        description:
            - If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
            - Required when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: bool
    jndi_connection_factory:
        description:
            - "The Connection Factory can be looked up using this name.
              e.g.: 'ConnectionFactory'"
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: str
    jndi_provider_url:
        description:
            - "The URL that Java Message Service will use to contact the JNDI provider.
              e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'"
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: str
    jndi_initial_context_factory:
        description:
            - "The implementation of javax.naming.spi.InitialContextFactory interface
              that the client uses to obtain initial naming context.
              e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'"
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: str
    jndi_security_principal:
        description:
            - "Specifies the identity of the principal (user) to be authenticated.
              e.g.: 'admin2'"
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: str
    jndi_security_credentials:
        description:
            - The password associated to the principal.
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: str
    connection_factory:
        description:
            - "The of Java class implementing javax.jms.ConnectionFactory interface
              supplied by the Java Message Service provider.
              e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'"
            - This parameter is updatable.
            - Applicable when connection_type is 'JAVA_MESSAGE_SERVICE'
        type: str
    deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            - This parameter is updatable.
            - Applicable when connection_type is 'GOLDENGATE'
        type: str
    should_validate_server_certificate:
        description:
            - If set to true, the driver validates the certificate that is sent by the database server.
            - This parameter is updatable.
            - Applicable when connection_type is 'MICROSOFT_SQLSERVER'
        type: bool
    tenancy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related OCI tenancy.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['OCI_OBJECT_STORAGE', 'ORACLE_NOSQL']
        type: str
    region:
        description:
            - "The name of the region. e.g.: us-ashburn-1"
            - This parameter is updatable.
            - Applicable when connection_type is one of ['OCI_OBJECT_STORAGE', 'ORACLE_NOSQL']
        type: str
    user_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the OCI user who will access the Object Storage.
              The user must have write access to the bucket they want to connect to.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['OCI_OBJECT_STORAGE', 'ORACLE_NOSQL']
        type: str
    public_key_fingerprint:
        description:
            - "The fingerprint of the API Key of the user specified by the userId.
              See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm"
            - This parameter is updatable.
            - Applicable when connection_type is one of ['OCI_OBJECT_STORAGE', 'ORACLE_NOSQL']
            - Required when connection_type is one of ['OCI_OBJECT_STORAGE', 'ORACLE_NOSQL']
        type: str
    url:
        description:
            - "Kafka Schema Registry URL.
              e.g.: 'https://server1.us.oracle.com:8081'"
            - This parameter is updatable.
            - Applicable when connection_type is 'KAFKA_SCHEMA_REGISTRY'
            - Required when connection_type is 'KAFKA_SCHEMA_REGISTRY'
        type: str
    access_key_id:
        description:
            - "Access key ID to access the Amazon S3 bucket.
              e.g.: \\"this-is-not-the-secret\\""
            - This parameter is updatable.
            - Applicable when connection_type is 'AMAZON_S3'
            - Required when connection_type is 'AMAZON_S3'
        type: str
    secret_access_key:
        description:
            - "Secret access key to access the Amazon S3 bucket.
              e.g.: \\"this-is-not-the-secret\\""
            - This parameter is updatable.
            - Applicable when connection_type is 'AMAZON_S3'
            - Required when connection_type is 'AMAZON_S3'
        type: str
    connection_url:
        description:
            - "Connectin URL of the Java Message Service, specifying the protocol, host, and port.
              e.g.: 'mq://myjms.host.domain:7676'"
            - This parameter is updatable.
            - Applicable when connection_type is one of ['SNOWFLAKE', 'JAVA_MESSAGE_SERVICE']
            - Required when connection_type is 'SNOWFLAKE'
        type: str
    authentication_type:
        description:
            - Used authentication mechanism to access Schema Registry.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['AZURE_DATA_LAKE_STORAGE', 'SNOWFLAKE', 'KAFKA_SCHEMA_REGISTRY']
            - Required when connection_type is one of ['AZURE_DATA_LAKE_STORAGE', 'SNOWFLAKE', 'KAFKA_SCHEMA_REGISTRY']
        type: str
    private_key_file:
        description:
            - The base64 encoded content of private key file in PEM format.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['OCI_OBJECT_STORAGE', 'SNOWFLAKE', 'ORACLE_NOSQL']
            - Required when connection_type is one of ['OCI_OBJECT_STORAGE', 'ORACLE_NOSQL']
        type: str
    private_key_passphrase:
        description:
            - Password if the private key file is encrypted.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['OCI_OBJECT_STORAGE', 'SNOWFLAKE', 'ORACLE_NOSQL']
        type: str
    core_site_xml:
        description:
            - The base64 encoded content of the Hadoop Distributed File System configuration file (core-site.xml).
            - This parameter is updatable.
            - Applicable when connection_type is 'HDFS'
            - Required when connection_type is 'HDFS'
        type: str
    host:
        description:
            - The name or address of a host.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'GOLDENGATE', 'POSTGRESQL']
            - Required when connection_type is one of ['MICROSOFT_SQLSERVER', 'POSTGRESQL']
        type: str
    port:
        description:
            - The port of an endpoint usually specified for a connection.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'GOLDENGATE', 'POSTGRESQL']
            - Required when connection_type is one of ['MICROSOFT_SQLSERVER', 'POSTGRESQL']
        type: int
    database_name:
        description:
            - The name of the database.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'POSTGRESQL']
            - Required when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'POSTGRESQL']
        type: str
    ssl_mode:
        description:
            - SSL modes for PostgreSQL.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'POSTGRESQL']
        type: str
    ssl_ca:
        description:
            - The base64 encoded certificate of the trusted certificate authorities (Trusted CA) for PostgreSQL.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'POSTGRESQL']
        type: str
    ssl_crl:
        description:
            - The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA) for PostgreSQL.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'POSTGRESQL']
        type: str
    ssl_cert:
        description:
            - The base64 encoded certificate of the PostgreSQL server.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'POSTGRESQL']
        type: str
    ssl_key:
        description:
            - The base64 encoded private key of the PostgreSQL server.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'POSTGRESQL']
        type: str
    private_ip:
        description:
            - The private IP address of the connection's endpoint in the customer's VCN, typically a
              database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
              In case the privateIp is provided, the subnetId must also be provided.
              In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
              In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'GOLDENGATE', 'KAFKA_SCHEMA_REGISTRY',
              'POSTGRESQL', 'ORACLE']
        type: str
    additional_attributes:
        description:
            - An array of name-value pair attribute entries.
              Used as additional parameters in connection string.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'POSTGRESQL']
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The name of the property entry.
                    - Required when connection_type is 'POSTGRESQL'
                type: str
                required: true
            value:
                description:
                    - The value of the property entry.
                    - Required when connection_type is 'POSTGRESQL'
                type: str
                required: true
    db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system being referenced.
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    stream_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the stream pool being referenced.
            - This parameter is updatable.
            - Applicable when connection_type is 'KAFKA'
        type: str
    bootstrap_servers:
        description:
            - "Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
              list of KafkaBootstrapServer objects specified by host/port.
              Used for establishing the initial connection to the Kafka cluster.
              Example: `\\"server1.example.com:9092,server2.example.com:9092\\"`"
            - This parameter is updatable.
            - Applicable when connection_type is 'KAFKA'
        type: list
        elements: dict
        suboptions:
            host:
                description:
                    - The name or address of a host.
                    - Required when connection_type is 'KAFKA'
                type: str
                required: true
            port:
                description:
                    - The port of an endpoint usually specified for a connection.
                    - Applicable when connection_type is 'KAFKA'
                type: int
            private_ip:
                description:
                    - The private IP address of the connection's endpoint in the customer's VCN, typically a
                      database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
                      In case the privateIp is provided, the subnetId must also be provided.
                      In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
                      In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.
                    - Applicable when connection_type is 'KAFKA'
                type: str
    security_protocol:
        description:
            - Security protocol for PostgreSQL.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'KAFKA', 'POSTGRESQL']
            - Required when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'POSTGRESQL']
        type: str
    trust_store:
        description:
            - The base64 encoded content of the TrustStore file.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['KAFKA', 'KAFKA_SCHEMA_REGISTRY']
        type: str
    trust_store_password:
        description:
            - The TrustStore password.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['KAFKA', 'KAFKA_SCHEMA_REGISTRY']
        type: str
    key_store:
        description:
            - The base64 encoded content of the KeyStore file.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['KAFKA', 'KAFKA_SCHEMA_REGISTRY']
        type: str
    key_store_password:
        description:
            - The KeyStore password.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['KAFKA', 'KAFKA_SCHEMA_REGISTRY']
        type: str
    ssl_key_password:
        description:
            - The password for the cert inside the KeyStore.
              In case it differs from the KeyStore password, it should be provided.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['KAFKA', 'KAFKA_SCHEMA_REGISTRY']
        type: str
    consumer_properties:
        description:
            - The base64 encoded content of the consumer.properties file.
            - This parameter is updatable.
            - Applicable when connection_type is 'KAFKA'
        type: str
    producer_properties:
        description:
            - The base64 encoded content of the producer.properties file.
            - This parameter is updatable.
            - Applicable when connection_type is 'KAFKA'
        type: str
    connection_type:
        description:
            - The connection type.
            - Required for create using I(state=present), update using I(state=present) with connection_id present.
            - Applicable when connection_type is one of ['AZURE_DATA_LAKE_STORAGE', 'MYSQL', 'OCI_OBJECT_STORAGE', 'HDFS', 'MONGODB', 'JAVA_MESSAGE_SERVICE',
              'ORACLE', 'MICROSOFT_SQLSERVER', 'AMAZON_S3', 'SNOWFLAKE', 'KAFKA', 'ORACLE_NOSQL', 'GOLDENGATE', 'KAFKA_SCHEMA_REGISTRY',
              'AZURE_SYNAPSE_ANALYTICS', 'POSTGRESQL']
        type: str
        choices:
            - "POSTGRESQL"
            - "KAFKA_SCHEMA_REGISTRY"
            - "MICROSOFT_SQLSERVER"
            - "JAVA_MESSAGE_SERVICE"
            - "SNOWFLAKE"
            - "AZURE_DATA_LAKE_STORAGE"
            - "MONGODB"
            - "AMAZON_S3"
            - "HDFS"
            - "OCI_OBJECT_STORAGE"
            - "AZURE_SYNAPSE_ANALYTICS"
            - "MYSQL"
            - "KAFKA"
            - "ORACLE"
            - "GOLDENGATE"
            - "ORACLE_NOSQL"
    display_name:
        description:
            - An object's Display Name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Applicable when connection_type is one of ['AZURE_DATA_LAKE_STORAGE', 'MYSQL', 'OCI_OBJECT_STORAGE', 'HDFS', 'MONGODB', 'JAVA_MESSAGE_SERVICE',
              'ORACLE', 'MICROSOFT_SQLSERVER', 'AMAZON_S3', 'SNOWFLAKE', 'KAFKA', 'ORACLE_NOSQL', 'GOLDENGATE', 'KAFKA_SCHEMA_REGISTRY',
              'AZURE_SYNAPSE_ANALYTICS', 'POSTGRESQL']
        type: str
        aliases: ["name"]
    description:
        description:
            - Metadata about this specific object.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
              for cross-compatibility only.
            - "Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Tags defined for this resource. Each key is predefined and scoped to a namespace.
            - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    vault_id:
        description:
            - Refers to the customer's vault OCID.
              If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
              to manage secrets contained within this vault.
            - This parameter is updatable.
        type: str
    key_id:
        description:
            - Refers to the customer's master key OCID.
              If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
            - This parameter is updatable.
        type: list
        elements: str
    connection_string:
        description:
            - "MongoDB connection string.
              e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'"
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MONGODB', 'AZURE_SYNAPSE_ANALYTICS', 'ORACLE']
            - Required when connection_type is 'AZURE_SYNAPSE_ANALYTICS'
        type: str
    username:
        description:
            - The username Oracle GoldenGate uses to connect the associated system of the given technology.
              This username must already exist and be available by the system/application to be connected to
              and must conform to the case sensitivty requirments defined in it.
            - This parameter is updatable.
            - Required when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'AZURE_SYNAPSE_ANALYTICS', 'POSTGRESQL', 'ORACLE']
        type: str
    password:
        description:
            - The password Oracle GoldenGate uses to connect the associated system of the given technology.
              It must conform to the specific security requirements including length, case sensitivity, and so on.
            - This parameter is updatable.
            - Required when connection_type is one of ['MICROSOFT_SQLSERVER', 'MYSQL', 'AZURE_SYNAPSE_ANALYTICS', 'POSTGRESQL', 'ORACLE']
        type: str
    connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Connection.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Connection.
            - Use I(state=present) to create or update a Connection.
            - Use I(state=absent) to delete a Connection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create connection with connection_type = POSTGRESQL
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: POSTGRESQL

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = KAFKA_SCHEMA_REGISTRY
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: KAFKA_SCHEMA_REGISTRY

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    url: url_example
    authentication_type: authentication_type_example
    private_ip: private_ip_example
    trust_store: trust_store_example
    trust_store_password: example-password
    key_store: key_store_example
    key_store_password: example-password
    ssl_key_password: example-password
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = MICROSOFT_SQLSERVER
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: MICROSOFT_SQLSERVER

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    should_validate_server_certificate: true
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_ca: ssl_ca_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = JAVA_MESSAGE_SERVICE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: JAVA_MESSAGE_SERVICE

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    should_use_jndi: true
    jndi_connection_factory: jndi_connection_factory_example
    jndi_provider_url: jndi_provider_url_example
    jndi_initial_context_factory: jndi_initial_context_factory_example
    jndi_security_principal: jndi_security_principal_example
    jndi_security_credentials: jndi_security_credentials_example
    connection_factory: connection_factory_example
    connection_url: connection_url_example
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = SNOWFLAKE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: SNOWFLAKE

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    connection_url: connection_url_example
    authentication_type: authentication_type_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = AZURE_DATA_LAKE_STORAGE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: AZURE_DATA_LAKE_STORAGE

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    account_name: account_name_example
    account_key: account_key_example
    sas_token: sas_token_example
    azure_tenant_id: "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx"
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    client_secret: client_secret_example
    endpoint: endpoint_example
    authentication_type: authentication_type_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Create connection with connection_type = MONGODB
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: MONGODB

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Create connection with connection_type = AMAZON_S3
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: AMAZON_S3

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    access_key_id: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
    secret_access_key: secret_access_key_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Create connection with connection_type = HDFS
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: HDFS

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    core_site_xml: core_site_xml_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Create connection with connection_type = OCI_OBJECT_STORAGE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: OCI_OBJECT_STORAGE

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    public_key_fingerprint: public_key_fingerprint_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Create connection with connection_type = AZURE_SYNAPSE_ANALYTICS
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: AZURE_SYNAPSE_ANALYTICS

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Create connection with connection_type = MYSQL
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: MYSQL

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = KAFKA
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: KAFKA

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    bootstrap_servers:
    - # required
      host: host_example

      # optional
      port: 56
      private_ip: private_ip_example
    security_protocol: security_protocol_example
    trust_store: trust_store_example
    trust_store_password: example-password
    key_store: key_store_example
    key_store_password: example-password
    ssl_key_password: example-password
    consumer_properties: consumer_properties_example
    producer_properties: producer_properties_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = ORACLE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: ORACLE

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    wallet: wallet_example
    session_mode: session_mode_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Create connection with connection_type = GOLDENGATE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: GOLDENGATE

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    host: host_example
    port: 56
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Create connection with connection_type = ORACLE_NOSQL
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: ORACLE_NOSQL

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    public_key_fingerprint: public_key_fingerprint_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection with connection_type = POSTGRESQL
  oci_golden_gate_connection:
    # required
    connection_type: POSTGRESQL

    # optional
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = KAFKA_SCHEMA_REGISTRY
  oci_golden_gate_connection:
    # required
    connection_type: KAFKA_SCHEMA_REGISTRY

    # optional
    url: url_example
    authentication_type: authentication_type_example
    private_ip: private_ip_example
    trust_store: trust_store_example
    trust_store_password: example-password
    key_store: key_store_example
    key_store_password: example-password
    ssl_key_password: example-password
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = MICROSOFT_SQLSERVER
  oci_golden_gate_connection:
    # required
    connection_type: MICROSOFT_SQLSERVER

    # optional
    should_validate_server_certificate: true
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_ca: ssl_ca_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = JAVA_MESSAGE_SERVICE
  oci_golden_gate_connection:
    # required
    connection_type: JAVA_MESSAGE_SERVICE

    # optional
    should_use_jndi: true
    jndi_connection_factory: jndi_connection_factory_example
    jndi_provider_url: jndi_provider_url_example
    jndi_initial_context_factory: jndi_initial_context_factory_example
    jndi_security_principal: jndi_security_principal_example
    jndi_security_credentials: jndi_security_credentials_example
    connection_factory: connection_factory_example
    connection_url: connection_url_example
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = SNOWFLAKE
  oci_golden_gate_connection:
    # required
    connection_type: SNOWFLAKE

    # optional
    connection_url: connection_url_example
    authentication_type: authentication_type_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = AZURE_DATA_LAKE_STORAGE
  oci_golden_gate_connection:
    # required
    connection_type: AZURE_DATA_LAKE_STORAGE

    # optional
    account_name: account_name_example
    account_key: account_key_example
    sas_token: sas_token_example
    azure_tenant_id: "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx"
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    client_secret: client_secret_example
    endpoint: endpoint_example
    authentication_type: authentication_type_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection with connection_type = MONGODB
  oci_golden_gate_connection:
    # required
    connection_type: MONGODB

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Update connection with connection_type = AMAZON_S3
  oci_golden_gate_connection:
    # required
    connection_type: AMAZON_S3

    # optional
    access_key_id: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
    secret_access_key: secret_access_key_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection with connection_type = HDFS
  oci_golden_gate_connection:
    # required
    connection_type: HDFS

    # optional
    core_site_xml: core_site_xml_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection with connection_type = OCI_OBJECT_STORAGE
  oci_golden_gate_connection:
    # required
    connection_type: OCI_OBJECT_STORAGE

    # optional
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    public_key_fingerprint: public_key_fingerprint_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection with connection_type = AZURE_SYNAPSE_ANALYTICS
  oci_golden_gate_connection:
    # required
    connection_type: AZURE_SYNAPSE_ANALYTICS

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Update connection with connection_type = MYSQL
  oci_golden_gate_connection:
    # required
    connection_type: MYSQL

    # optional
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = KAFKA
  oci_golden_gate_connection:
    # required
    connection_type: KAFKA

    # optional
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    bootstrap_servers:
    - # required
      host: host_example

      # optional
      port: 56
      private_ip: private_ip_example
    security_protocol: security_protocol_example
    trust_store: trust_store_example
    trust_store_password: example-password
    key_store: key_store_example
    key_store_password: example-password
    ssl_key_password: example-password
    consumer_properties: consumer_properties_example
    producer_properties: producer_properties_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = ORACLE
  oci_golden_gate_connection:
    # required
    connection_type: ORACLE

    # optional
    wallet: wallet_example
    session_mode: session_mode_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Update connection with connection_type = GOLDENGATE
  oci_golden_gate_connection:
    # required
    connection_type: GOLDENGATE

    # optional
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    host: host_example
    port: 56
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection with connection_type = ORACLE_NOSQL
  oci_golden_gate_connection:
    # required
    connection_type: ORACLE_NOSQL

    # optional
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    public_key_fingerprint: public_key_fingerprint_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = POSTGRESQL
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: POSTGRESQL

    # optional
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = KAFKA_SCHEMA_REGISTRY
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: KAFKA_SCHEMA_REGISTRY

    # optional
    url: url_example
    authentication_type: authentication_type_example
    private_ip: private_ip_example
    trust_store: trust_store_example
    trust_store_password: example-password
    key_store: key_store_example
    key_store_password: example-password
    ssl_key_password: example-password
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = MICROSOFT_SQLSERVER
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: MICROSOFT_SQLSERVER

    # optional
    should_validate_server_certificate: true
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_ca: ssl_ca_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = JAVA_MESSAGE_SERVICE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: JAVA_MESSAGE_SERVICE

    # optional
    should_use_jndi: true
    jndi_connection_factory: jndi_connection_factory_example
    jndi_provider_url: jndi_provider_url_example
    jndi_initial_context_factory: jndi_initial_context_factory_example
    jndi_security_principal: jndi_security_principal_example
    jndi_security_credentials: jndi_security_credentials_example
    connection_factory: connection_factory_example
    connection_url: connection_url_example
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = SNOWFLAKE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: SNOWFLAKE

    # optional
    connection_url: connection_url_example
    authentication_type: authentication_type_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = AZURE_DATA_LAKE_STORAGE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: AZURE_DATA_LAKE_STORAGE

    # optional
    account_name: account_name_example
    account_key: account_key_example
    sas_token: sas_token_example
    azure_tenant_id: "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx"
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    client_secret: client_secret_example
    endpoint: endpoint_example
    authentication_type: authentication_type_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = MONGODB
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: MONGODB

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = AMAZON_S3
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: AMAZON_S3

    # optional
    access_key_id: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
    secret_access_key: secret_access_key_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = HDFS
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: HDFS

    # optional
    core_site_xml: core_site_xml_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = OCI_OBJECT_STORAGE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: OCI_OBJECT_STORAGE

    # optional
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    public_key_fingerprint: public_key_fingerprint_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = AZURE_SYNAPSE_ANALYTICS
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: AZURE_SYNAPSE_ANALYTICS

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = MYSQL
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: MYSQL

    # optional
    host: host_example
    port: 56
    database_name: database_name_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    private_ip: private_ip_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    security_protocol: security_protocol_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = KAFKA
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: KAFKA

    # optional
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    bootstrap_servers:
    - # required
      host: host_example

      # optional
      port: 56
      private_ip: private_ip_example
    security_protocol: security_protocol_example
    trust_store: trust_store_example
    trust_store_password: example-password
    key_store: key_store_example
    key_store_password: example-password
    ssl_key_password: example-password
    consumer_properties: consumer_properties_example
    producer_properties: producer_properties_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = ORACLE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: ORACLE

    # optional
    wallet: wallet_example
    session_mode: session_mode_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    connection_string: connection_string_example
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = GOLDENGATE
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: GOLDENGATE

    # optional
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    host: host_example
    port: 56
    private_ip: private_ip_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = ORACLE_NOSQL
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: ORACLE_NOSQL

    # optional
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    public_key_fingerprint: public_key_fingerprint_example
    private_key_file: private_key_file_example
    private_key_passphrase: private_key_passphrase_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]

- name: Delete connection
  oci_golden_gate_connection:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        access_key_id:
            description:
                - "Access key ID to access the Amazon S3 bucket.
                  e.g.: \\"this-is-not-the-secret\\""
            returned: on success
            type: str
            sample: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
        account_name:
            description:
                - Sets the Azure storage account name.
            returned: on success
            type: str
            sample: account_name_example
        azure_tenant_id:
            description:
                - "Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
                  e.g.: 14593954-d337-4a61-a364-9f758c64f97f"
            returned: on success
            type: str
            sample: "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx"
        client_id:
            description:
                - "Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
                  e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d"
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint:
            description:
                - "Azure Storage service endpoint.
                  e.g: https://test.blob.core.windows.net"
            returned: on success
            type: str
            sample: endpoint_example
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        should_use_jndi:
            description:
                - If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.
            returned: on success
            type: bool
            sample: true
        jndi_connection_factory:
            description:
                - "The Connection Factory can be looked up using this name.
                  e.g.: 'ConnectionFactory'"
            returned: on success
            type: str
            sample: jndi_connection_factory_example
        jndi_provider_url:
            description:
                - "The URL that Java Message Service will use to contact the JNDI provider.
                  e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'"
            returned: on success
            type: str
            sample: jndi_provider_url_example
        jndi_initial_context_factory:
            description:
                - "The implementation of javax.naming.spi.InitialContextFactory interface
                  that the client uses to obtain initial naming context.
                  e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'"
            returned: on success
            type: str
            sample: jndi_initial_context_factory_example
        jndi_security_principal:
            description:
                - "Specifies the identity of the principal (user) to be authenticated.
                  e.g.: 'admin2'"
            returned: on success
            type: str
            sample: jndi_security_principal_example
        connection_factory:
            description:
                - "The of Java class implementing javax.jms.ConnectionFactory interface
                  supplied by the Java Message Service provider.
                  e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'"
            returned: on success
            type: str
            sample: connection_factory_example
        stream_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the stream pool being referenced.
            returned: on success
            type: str
            sample: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        bootstrap_servers:
            description:
                - "Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
                  list of KafkaBootstrapServer objects specified by host/port.
                  Used for establishing the initial connection to the Kafka cluster.
                  Example: `\\"server1.example.com:9092,server2.example.com:9092\\"`"
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
            returned: on success
            type: str
            sample: url_example
        ssl_ca:
            description:
                - "Database Certificate - The base64 encoded content of pem file
                  containing the server public key (for 1-way SSL)."
            returned: on success
            type: str
            sample: ssl_ca_example
        should_validate_server_certificate:
            description:
                - If set to true, the driver validates the certificate that is sent by the database server.
            returned: on success
            type: bool
            sample: true
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system being referenced.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        connection_string:
            description:
                - "JDBC connection string.
                  e.g.: 'jdbc:sqlserver://<synapse-workspace>.sql.azuresynapse.net:1433;database=<db-
                  name>;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'"
            returned: on success
            type: str
            sample: connection_string_example
        session_mode:
            description:
                - "The mode of the database connection session to be established by the data client.
                  'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
                  Connection to a RAC database involves a redirection received from the SCAN listeners
                  to the database node to connect to. By default the mode would be DIRECT."
            returned: on success
            type: str
            sample: DIRECT
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Autonomous Json Database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related OCI tenancy.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - "The name of the region. e.g.: us-ashburn-1"
            returned: on success
            type: str
            sample: us-phoenix-1
        user_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the OCI user who will access the Object Storage.
                  The user must have write access to the bucket they want to connect to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - The name of the database.
            returned: on success
            type: str
            sample: database_name_example
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
        additional_attributes:
            description:
                - An array of name-value pair attribute entries.
                  Used as additional parameters in connection string.
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
            returned: on success
            type: str
            sample: SSL
        ssl_mode:
            description:
                - SSL modes for MySQL.
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
            returned: on success
            type: str
            sample: private_ip_example
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
        technology_type:
            description:
                - The Amazon S3 technology type.
            returned: on success
            type: str
            sample: AMAZON_S3
        connection_url:
            description:
                - "Connectin URL of the Java Message Service, specifying the protocol, host, and port.
                  e.g.: 'mq://myjms.host.domain:7676'"
            returned: on success
            type: str
            sample: connection_url_example
        authentication_type:
            description:
                - Used authentication mechanism to access Azure Data Lake Storage.
            returned: on success
            type: str
            sample: SHARED_KEY
        username:
            description:
                - The username Oracle GoldenGate uses to connect the associated system of the given technology.
                  This username must already exist and be available by the system/application to be connected to
                  and must conform to the case sensitivty requirments defined in it.
            returned: on success
            type: str
            sample: username_example
    sample: {
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
        "nsg_ids": [],
        "technology_type": "AMAZON_S3",
        "connection_url": "connection_url_example",
        "authentication_type": "SHARED_KEY",
        "username": "username_example"
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateConnectionDetails
    from oci.golden_gate.models import UpdateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConnectionHelperGen, self).get_possible_entity_types() + [
            "goldengateconnection",
            "goldengateconnections",
            "goldenGategoldengateconnection",
            "goldenGategoldengateconnections",
            "goldengateconnectionresource",
            "goldengateconnectionsresource",
            "connection",
            "connections",
            "goldenGateconnection",
            "goldenGateconnections",
            "connectionresource",
            "connectionsresource",
            "goldengate",
        ]

    def get_module_resource_id_param(self):
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection, connection_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
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
            self.client.list_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectionDetails

    def get_exclude_attributes(self):
        return [
            "ssl_crl",
            "wallet",
            "consumer_properties",
            "ssl_key",
            "trust_store",
            "secret_access_key",
            "account_key",
            "producer_properties",
            "ssl_key_password",
            "private_key_passphrase",
            "key_store",
            "sas_token",
            "password",
            "private_key_file",
            "core_site_xml",
            "jndi_security_credentials",
            "key_store_password",
            "public_key_fingerprint",
            "client_secret",
            "trust_store_password",
            "ssl_cert",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(create_connection_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                update_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(connection_id=self.module.params.get("connection_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ConnectionHelperCustom = get_custom_class("ConnectionHelperCustom")


class ResourceHelper(ConnectionHelperCustom, ConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            technology_type=dict(type="str"),
            wallet=dict(type="str"),
            session_mode=dict(type="str"),
            database_id=dict(type="str"),
            account_name=dict(type="str"),
            account_key=dict(type="str", no_log=True),
            sas_token=dict(type="str", no_log=True),
            azure_tenant_id=dict(type="str"),
            client_id=dict(type="str"),
            client_secret=dict(type="str", no_log=True),
            endpoint=dict(type="str"),
            should_use_jndi=dict(type="bool"),
            jndi_connection_factory=dict(type="str"),
            jndi_provider_url=dict(type="str"),
            jndi_initial_context_factory=dict(type="str"),
            jndi_security_principal=dict(type="str"),
            jndi_security_credentials=dict(type="str"),
            connection_factory=dict(type="str"),
            deployment_id=dict(type="str"),
            should_validate_server_certificate=dict(type="bool"),
            tenancy_id=dict(type="str"),
            region=dict(type="str"),
            user_id=dict(type="str"),
            public_key_fingerprint=dict(type="str", no_log=True),
            url=dict(type="str"),
            access_key_id=dict(type="str"),
            secret_access_key=dict(type="str", no_log=True),
            connection_url=dict(type="str"),
            authentication_type=dict(type="str"),
            private_key_file=dict(type="str"),
            private_key_passphrase=dict(type="str", no_log=True),
            core_site_xml=dict(type="str"),
            host=dict(type="str"),
            port=dict(type="int"),
            database_name=dict(type="str"),
            ssl_mode=dict(type="str"),
            ssl_ca=dict(type="str"),
            ssl_crl=dict(type="str"),
            ssl_cert=dict(type="str"),
            ssl_key=dict(type="str", no_log=True),
            private_ip=dict(type="str"),
            additional_attributes=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            db_system_id=dict(type="str"),
            stream_pool_id=dict(type="str"),
            bootstrap_servers=dict(
                type="list",
                elements="dict",
                options=dict(
                    host=dict(type="str", required=True),
                    port=dict(type="int"),
                    private_ip=dict(type="str"),
                ),
            ),
            security_protocol=dict(type="str"),
            trust_store=dict(type="str"),
            trust_store_password=dict(type="str", no_log=True),
            key_store=dict(type="str", no_log=True),
            key_store_password=dict(type="str", no_log=True),
            ssl_key_password=dict(type="str", no_log=True),
            consumer_properties=dict(type="str"),
            producer_properties=dict(type="str"),
            connection_type=dict(
                type="str",
                choices=[
                    "POSTGRESQL",
                    "KAFKA_SCHEMA_REGISTRY",
                    "MICROSOFT_SQLSERVER",
                    "JAVA_MESSAGE_SERVICE",
                    "SNOWFLAKE",
                    "AZURE_DATA_LAKE_STORAGE",
                    "MONGODB",
                    "AMAZON_S3",
                    "HDFS",
                    "OCI_OBJECT_STORAGE",
                    "AZURE_SYNAPSE_ANALYTICS",
                    "MYSQL",
                    "KAFKA",
                    "ORACLE",
                    "GOLDENGATE",
                    "ORACLE_NOSQL",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            vault_id=dict(type="str"),
            key_id=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            connection_string=dict(type="str"),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
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
