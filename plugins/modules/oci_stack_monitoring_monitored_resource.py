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
module: oci_stack_monitoring_monitored_resource
short_description: Manage a MonitoredResource resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MonitoredResource resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new monitored resource for the given resource type with the details and submits
      a work request for promoting the resource to agent. Once the resource is successfully
      added to agent, resource state will be marked active.
    - "This resource has the following action operations in the M(oracle.oci.oci_stack_monitoring_monitored_resource_actions) module: associate,
      change_compartment, disable_external_database, disassociate, search_monitored_resource_associations, search_monitored_resource_members, search,
      update_and_propagate_tags."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - Monitored Resource Name.
            - Required for create using I(state=present).
        type: str
    type:
        description:
            - Monitored Resource Type.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - Compartment Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
        type: str
    external_id:
        description:
            - External resource is any OCI resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
              which is not a Stack Monitoring service resource.
              Currently supports only OCI compute instance.
        type: str
    management_agent_id:
        description:
            - Management Agent Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    external_resource_id:
        description:
            - Generally used by DBaaS to send the Database OCID stored on the DBaaS.
              The same will be passed to resource service to enable Stack Monitoring Service on DBM.
              This will be stored in Stack Monitoring Resource Service data store as identifier for monitored resource.
              If this header is not set as part of the request, then an id will be generated and stored for the resource.
        type: str
    display_name:
        description:
            - Monitored resource display name.
            - This parameter is updatable.
        type: str
    host_name:
        description:
            - Host name of the monitored resource.
            - This parameter is updatable.
        type: str
    resource_time_zone:
        description:
            - "Time zone in the form of tz database canonical zone ID. Specifies the preference with
              a value that uses the IANA Time Zone Database format (x-obmcs-time-zone).
              For example - America/Los_Angeles"
            - This parameter is updatable.
        type: str
    properties:
        description:
            - List of monitored resource properties.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Property Name.
                type: str
            value:
                description:
                    - Property Value.
                type: str
    database_connection_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            protocol:
                description:
                    - Protocol used in DB connection string when connecting to external database service.
                type: str
                choices:
                    - "TCP"
                    - "TCPS"
                required: true
            port:
                description:
                    - Listener Port number used for connection requests.
                type: int
                required: true
            connector_id:
                description:
                    - Database connector Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                type: str
            service_name:
                description:
                    - Service name used for connection requests.
                type: str
                required: true
            db_unique_name:
                description:
                    - UniqueName used for database connection requests.
                type: str
            db_id:
                description:
                    - dbId of the database.
                type: str
            ssl_secret_id:
                description:
                    - SSL Secret Identifier for TCPS connector in OCI VaultL(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                type: str
    credentials:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            key_id:
                description:
                    - The master key should be created in OCI Vault owned by the client of this API.
                      The user should have permission to access the vault key.
                    - Required when credential_type is 'ENCRYPTED'
                type: str
            source:
                description:
                    - The source type and source name combination, delimited with (.) separator.
                      {source type}.{source name} and source type max char limit is 63.
                type: str
            name:
                description:
                    - The name of the credential, within the context of the source.
                type: str
            type:
                description:
                    - The type of the credential ( ex. JMXCreds,DBCreds).
                type: str
            description:
                description:
                    - The user-specified textual description of the credential.
                type: str
            credential_type:
                description:
                    - "Type of credentials specified in the credentials element.
                      Three possible values - EXISTING, PLAINTEXT and ENCRYPTED.
                      * EXISTING  - Credential is already stored in agent and only credential name need
                              to be passed for existing credential.
                      * PLAINTEXT - The credential properties will have credentials in plain text format.
                      * ENCRYPTED - The credential properties will have credentials stored in vault in
                              encrypted format using KMS client which uses master key for encryption.
                              The same master key will be used to decrypt the credentials before passing
                              on to the management agent."
                type: str
                choices:
                    - "EXISTING"
                    - "ENCRYPTED"
                    - "PLAINTEXT"
                required: true
            properties:
                description:
                    - The credential properties list. Credential property values will be encrypted format.
                    - Required when credential_type is one of ['PLAINTEXT', 'ENCRYPTED']
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - "The name of the credential property, should confirm with names of properties of this credential's type.
                              Example: For JMXCreds type, credential property name for weblogic user is 'Username'."
                            - Required when credential_type is 'ENCRYPTED'
                        type: str
                        required: true
                    value:
                        description:
                            - "The value of the credential property name.
                              Example: For JMXCreds type, credential property value for 'Username' property is 'weblogic'."
                            - Required when credential_type is 'ENCRYPTED'
                        type: str
                        required: true
    aliases:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            source:
                description:
                    - "The source type and source name combination,delimited with (.) separator.
                      Example: {source type}.{source name} and source type max char limit is 63."
                type: str
                required: true
            name:
                description:
                    - The name of the alias, within the context of the source.
                type: str
                required: true
            credential:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    source:
                        description:
                            - The source type and source name combination,delimited with (.) separator.
                              This refers to the pre-existing source which alias cred should point to.
                              Ex. {source type}.{source name} and source type max char limit is 63.
                        type: str
                        required: true
                    name:
                        description:
                            - The name of the pre-existing source credential which alias cred should point to.
                              This should refer to the pre-existing source attribute which is bound to credential name.
                        type: str
                        required: true
                    service:
                        description:
                            - "The name of the service owning the credential.
                              Example: stack-monitoring or dbmgmt"
                        type: str
                        required: true
    additional_credentials:
        description:
            - "List of MonitoredResourceCredentials. This property complements the existing
              \\"credentials\\" property by allowing user to specify more than one credential.
              If both \\"credential\\" and \\"additionalCredentials\\" are specified, union of the
              values is used as list of credentials applicable for this resource.
              If any duplicate found in the combined list of \\"credentials\\" and \\"additionalCredentials\\",
              an error will be thrown."
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key_id:
                description:
                    - The master key should be created in OCI Vault owned by the client of this API.
                      The user should have permission to access the vault key.
                    - Required when credential_type is 'ENCRYPTED'
                type: str
            source:
                description:
                    - The source type and source name combination, delimited with (.) separator.
                      {source type}.{source name} and source type max char limit is 63.
                type: str
            name:
                description:
                    - The name of the credential, within the context of the source.
                type: str
            type:
                description:
                    - The type of the credential ( ex. JMXCreds,DBCreds).
                type: str
            description:
                description:
                    - The user-specified textual description of the credential.
                type: str
            credential_type:
                description:
                    - "Type of credentials specified in the credentials element.
                      Three possible values - EXISTING, PLAINTEXT and ENCRYPTED.
                      * EXISTING  - Credential is already stored in agent and only credential name need
                              to be passed for existing credential.
                      * PLAINTEXT - The credential properties will have credentials in plain text format.
                      * ENCRYPTED - The credential properties will have credentials stored in vault in
                              encrypted format using KMS client which uses master key for encryption.
                              The same master key will be used to decrypt the credentials before passing
                              on to the management agent."
                type: str
                choices:
                    - "EXISTING"
                    - "ENCRYPTED"
                    - "PLAINTEXT"
                required: true
            properties:
                description:
                    - The credential properties list. Credential property values will be encrypted format.
                    - Required when credential_type is one of ['PLAINTEXT', 'ENCRYPTED']
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - "The name of the credential property, should confirm with names of properties of this credential's type.
                              Example: For JMXCreds type, credential property name for weblogic user is 'Username'."
                            - Required when credential_type is 'ENCRYPTED'
                        type: str
                        required: true
                    value:
                        description:
                            - "The value of the credential property name.
                              Example: For JMXCreds type, credential property value for 'Username' property is 'weblogic'."
                            - Required when credential_type is 'ENCRYPTED'
                        type: str
                        required: true
    additional_aliases:
        description:
            - "List of MonitoredResourceAliasCredentials. This property complements the existing
              \\"aliases\\" property by allowing user to specify more than one credential alias.
              If both \\"aliases\\" and \\"additionalAliases\\" are specified, union of the
              values is used as list of aliases applicable for this resource.
              If any duplicate found in the combined list of \\"alias\\" and \\"additionalAliases\\",
              an error will be thrown."
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            source:
                description:
                    - "The source type and source name combination,delimited with (.) separator.
                      Example: {source type}.{source name} and source type max char limit is 63."
                type: str
                required: true
            name:
                description:
                    - The name of the alias, within the context of the source.
                type: str
                required: true
            credential:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    source:
                        description:
                            - The source type and source name combination,delimited with (.) separator.
                              This refers to the pre-existing source which alias cred should point to.
                              Ex. {source type}.{source name} and source type max char limit is 63.
                        type: str
                        required: true
                    name:
                        description:
                            - The name of the pre-existing source credential which alias cred should point to.
                              This should refer to the pre-existing source attribute which is bound to credential name.
                        type: str
                        required: true
                    service:
                        description:
                            - "The name of the service owning the credential.
                              Example: stack-monitoring or dbmgmt"
                        type: str
                        required: true
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
    monitored_resource_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored resource.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    is_delete_members:
        description:
            - If this query parameter is specified and set to true, all the member
              resources will be deleted before deleting the specified resource.
        type: bool
    state:
        description:
            - The state of the MonitoredResource.
            - Use I(state=present) to create or update a MonitoredResource.
            - Use I(state=absent) to delete a MonitoredResource.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create monitored_resource
  oci_stack_monitoring_monitored_resource:
    # required
    name: name_example
    type: type_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    external_id: "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx"
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
    external_resource_id: "ocid1.externalresource.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    host_name: host_name_example
    resource_time_zone: resource_time_zone_example
    properties:
    - # optional
      name: name_example
      value: value_example
    database_connection_details:
      # required
      protocol: TCP
      port: 56
      service_name: service_name_example

      # optional
      connector_id: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
      db_unique_name: db_unique_name_example
      db_id: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
      ssl_secret_id: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
    credentials:
      # required
      credential_type: EXISTING

      # optional
      source: source_example
      name: name_example
      type: type_example
      description: description_example
    aliases:
      # required
      source: source_example
      name: name_example
      credential:
        # required
        source: source_example
        name: name_example
        service: service_example
    additional_credentials:
    - # required
      credential_type: EXISTING

      # optional
      source: source_example
      name: name_example
      type: type_example
      description: description_example
    additional_aliases:
    - # required
      source: source_example
      name: name_example
      credential:
        # required
        source: source_example
        name: name_example
        service: service_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update monitored_resource
  oci_stack_monitoring_monitored_resource:
    # required
    monitored_resource_id: "ocid1.monitoredresource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    host_name: host_name_example
    resource_time_zone: resource_time_zone_example
    properties:
    - # optional
      name: name_example
      value: value_example
    database_connection_details:
      # required
      protocol: TCP
      port: 56
      service_name: service_name_example

      # optional
      connector_id: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
      db_unique_name: db_unique_name_example
      db_id: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
      ssl_secret_id: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
    credentials:
      # required
      credential_type: EXISTING

      # optional
      source: source_example
      name: name_example
      type: type_example
      description: description_example
    aliases:
      # required
      source: source_example
      name: name_example
      credential:
        # required
        source: source_example
        name: name_example
        service: service_example
    additional_credentials:
    - # required
      credential_type: EXISTING

      # optional
      source: source_example
      name: name_example
      type: type_example
      description: description_example
    additional_aliases:
    - # required
      source: source_example
      name: name_example
      credential:
        # required
        source: source_example
        name: name_example
        service: service_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete monitored_resource
  oci_stack_monitoring_monitored_resource:
    # required
    monitored_resource_id: "ocid1.monitoredresource.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    is_delete_members: true

"""

RETURN = """
monitored_resource:
    description:
        - Details of the MonitoredResource resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Monitored resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Monitored resource name.
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Monitored resource display name.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - Monitored Resource Type.
            returned: on success
            type: str
            sample: type_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tenant_id:
            description:
                - Tenancy Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - Monitored resource host name.
            returned: on success
            type: str
            sample: host_name_example
        external_id:
            description:
                - "The external resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  External resource is any OCI resource which is not a Stack Monitoring service resource.
                  Currently supports only following resource types - Container database, non-container database,
                  pluggable database and OCI compute instance."
            returned: on success
            type: str
            sample: "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx"
        management_agent_id:
            description:
                - Management Agent Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        resource_time_zone:
            description:
                - Time zone in the form of tz database canonical zone ID.
            returned: on success
            type: str
            sample: resource_time_zone_example
        time_created:
            description:
                - The date and time when the monitored resource was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time when the monitored resource was last updated, expressed in
                  L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Lifecycle state of the monitored resource.
            returned: on success
            type: str
            sample: CREATING
        properties:
            description:
                - List of monitored resource properties.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Property Name.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - Property Value.
                    returned: on success
                    type: str
                    sample: value_example
        database_connection_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                protocol:
                    description:
                        - Protocol used in DB connection string when connecting to external database service.
                    returned: on success
                    type: str
                    sample: TCP
                port:
                    description:
                        - Listener Port number used for connection requests.
                    returned: on success
                    type: int
                    sample: 56
                connector_id:
                    description:
                        - Database connector Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
                service_name:
                    description:
                        - Service name used for connection requests.
                    returned: on success
                    type: str
                    sample: service_name_example
                db_unique_name:
                    description:
                        - UniqueName used for database connection requests.
                    returned: on success
                    type: str
                    sample: db_unique_name_example
                db_id:
                    description:
                        - dbId of the database.
                    returned: on success
                    type: str
                    sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
                ssl_secret_id:
                    description:
                        - SSL Secret Identifier for TCPS connector in OCI VaultL(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
        credentials:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                key_id:
                    description:
                        - The master key should be created in OCI Vault owned by the client of this API.
                          The user should have permission to access the vault key.
                    returned: on success
                    type: str
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
                source:
                    description:
                        - The source type and source name combination, delimited with (.) separator.
                          {source type}.{source name} and source type max char limit is 63.
                    returned: on success
                    type: str
                    sample: source_example
                name:
                    description:
                        - The name of the credential, within the context of the source.
                    returned: on success
                    type: str
                    sample: name_example
                type:
                    description:
                        - The type of the credential ( ex. JMXCreds,DBCreds).
                    returned: on success
                    type: str
                    sample: type_example
                description:
                    description:
                        - The user-specified textual description of the credential.
                    returned: on success
                    type: str
                    sample: description_example
                credential_type:
                    description:
                        - "Type of credentials specified in the credentials element.
                          Three possible values - EXISTING, PLAINTEXT and ENCRYPTED.
                          * EXISTING  - Credential is already stored in agent and only credential name need
                                  to be passed for existing credential.
                          * PLAINTEXT - The credential properties will have credentials in plain text format.
                          * ENCRYPTED - The credential properties will have credentials stored in vault in
                                  encrypted format using KMS client which uses master key for encryption.
                                  The same master key will be used to decrypt the credentials before passing
                                  on to the management agent."
                    returned: on success
                    type: str
                    sample: EXISTING
                properties:
                    description:
                        - The credential properties list. Credential property values will be encrypted format.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - "The name of the credential property, should confirm with names of properties of this credential's type.
                                  Example: For JMXCreds type, credential property name for weblogic user is 'Username'."
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - "The value of the credential property name.
                                  Example: For JMXCreds type, credential property value for 'Username' property is 'weblogic'."
                            returned: on success
                            type: str
                            sample: value_example
        aliases:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - "The source type and source name combination,delimited with (.) separator.
                          Example: {source type}.{source name} and source type max char limit is 63."
                    returned: on success
                    type: str
                    sample: source_example
                name:
                    description:
                        - The name of the alias, within the context of the source.
                    returned: on success
                    type: str
                    sample: name_example
                credential:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        source:
                            description:
                                - The source type and source name combination,delimited with (.) separator.
                                  This refers to the pre-existing source which alias cred should point to.
                                  Ex. {source type}.{source name} and source type max char limit is 63.
                            returned: on success
                            type: str
                            sample: source_example
                        name:
                            description:
                                - The name of the pre-existing source credential which alias cred should point to.
                                  This should refer to the pre-existing source attribute which is bound to credential name.
                            returned: on success
                            type: str
                            sample: name_example
                        service:
                            description:
                                - "The name of the service owning the credential.
                                  Example: stack-monitoring or dbmgmt"
                            returned: on success
                            type: str
                            sample: service_example
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example",
        "type": "type_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "external_id": "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_time_zone": "resource_time_zone_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "properties": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "database_connection_details": {
            "protocol": "TCP",
            "port": 56,
            "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
            "service_name": "service_name_example",
            "db_unique_name": "db_unique_name_example",
            "db_id": "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx",
            "ssl_secret_id": "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "credentials": {
            "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
            "source": "source_example",
            "name": "name_example",
            "type": "type_example",
            "description": "description_example",
            "credential_type": "EXISTING",
            "properties": [{
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "aliases": {
            "source": "source_example",
            "name": "name_example",
            "credential": {
                "source": "source_example",
                "name": "name_example",
                "service": "service_example"
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.stack_monitoring import StackMonitoringClient
    from oci.stack_monitoring.models import CreateMonitoredResourceDetails
    from oci.stack_monitoring.models import UpdateMonitoredResourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitoredResourceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and delete"""

    def get_possible_entity_types(self):
        return super(MonitoredResourceHelperGen, self).get_possible_entity_types() + [
            "stackmonitoringresource",
            "stackmonitoringresources",
            "stackMonitoringstackmonitoringresource",
            "stackMonitoringstackmonitoringresources",
            "stackmonitoringresourceresource",
            "stackmonitoringresourcesresource",
            "monitoredresource",
            "monitoredresources",
            "stackMonitoringmonitoredresource",
            "stackMonitoringmonitoredresources",
            "monitoredresourceresource",
            "monitoredresourcesresource",
            "stackmonitoring",
        ]

    def get_module_resource_id_param(self):
        return "monitored_resource_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitored_resource_id")

    def get_get_fn(self):
        return self.client.get_monitored_resource

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitored_resource,
            monitored_resource_id=self.module.params.get("monitored_resource_id"),
        )

    def get_create_model_class(self):
        return CreateMonitoredResourceDetails

    def get_exclude_attributes(self):
        return ["additional_aliases", "additional_credentials"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_monitored_resource,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_monitored_resource_details=create_details,
                external_resource_id=self.module.params.get("external_resource_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMonitoredResourceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_monitored_resource,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                update_monitored_resource_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_monitored_resource,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                is_delete_members=self.module.params.get("is_delete_members"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MonitoredResourceHelperCustom = get_custom_class("MonitoredResourceHelperCustom")


class ResourceHelper(MonitoredResourceHelperCustom, MonitoredResourceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            type=dict(type="str"),
            compartment_id=dict(type="str"),
            external_id=dict(type="str"),
            management_agent_id=dict(type="str"),
            external_resource_id=dict(type="str"),
            display_name=dict(type="str"),
            host_name=dict(type="str"),
            resource_time_zone=dict(type="str"),
            properties=dict(
                type="list",
                elements="dict",
                options=dict(name=dict(type="str"), value=dict(type="str")),
            ),
            database_connection_details=dict(
                type="dict",
                options=dict(
                    protocol=dict(type="str", required=True, choices=["TCP", "TCPS"]),
                    port=dict(type="int", required=True),
                    connector_id=dict(type="str"),
                    service_name=dict(type="str", required=True),
                    db_unique_name=dict(type="str"),
                    db_id=dict(type="str"),
                    ssl_secret_id=dict(type="str"),
                ),
            ),
            credentials=dict(
                type="dict",
                options=dict(
                    key_id=dict(type="str"),
                    source=dict(type="str"),
                    name=dict(type="str"),
                    type=dict(type="str"),
                    description=dict(type="str"),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["EXISTING", "ENCRYPTED", "PLAINTEXT"],
                    ),
                    properties=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            aliases=dict(
                type="dict",
                options=dict(
                    source=dict(type="str", required=True),
                    name=dict(type="str", required=True),
                    credential=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            source=dict(type="str", required=True),
                            name=dict(type="str", required=True),
                            service=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            additional_credentials=dict(
                type="list",
                elements="dict",
                options=dict(
                    key_id=dict(type="str"),
                    source=dict(type="str"),
                    name=dict(type="str"),
                    type=dict(type="str"),
                    description=dict(type="str"),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["EXISTING", "ENCRYPTED", "PLAINTEXT"],
                    ),
                    properties=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            additional_aliases=dict(
                type="list",
                elements="dict",
                options=dict(
                    source=dict(type="str", required=True),
                    name=dict(type="str", required=True),
                    credential=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            source=dict(type="str", required=True),
                            name=dict(type="str", required=True),
                            service=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            monitored_resource_id=dict(aliases=["id"], type="str"),
            is_delete_members=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="monitored_resource",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
