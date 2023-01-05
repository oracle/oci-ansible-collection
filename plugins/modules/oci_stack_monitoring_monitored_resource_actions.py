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
module: oci_stack_monitoring_monitored_resource_actions
short_description: Perform actions on a MonitoredResource resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MonitoredResource resource in Oracle Cloud Infrastructure
    - For I(action=associate), create an association between two monitored resources.
    - For I(action=change_compartment), moves a MonitoredResource resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
    - For I(action=disable_external_database), disable external database resource monitoring.
    - For I(action=disassociate), removes associations between two monitored resources.
    - For I(action=search_monitored_resource_associations), returns a list of monitored resource associations.
    - For I(action=search_monitored_resource_members), list resources which are members of the given monitored resource
    - For I(action=search), returns a list of monitored resources.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_resource_id:
        description:
            - Source Monitored Resource Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            - Required for I(action=associate).
        type: str
    source_resource_name:
        description:
            - Source Monitored Resource Name
            - Applicable only for I(action=search_monitored_resource_associations).
        type: str
    source_resource_type:
        description:
            - Source Monitored Resource Type
            - Applicable only for I(action=search_monitored_resource_associations).
        type: str
    destination_resource_name:
        description:
            - Source Monitored Resource Name
            - Applicable only for I(action=search_monitored_resource_associations).
        type: str
    destination_resource_type:
        description:
            - Source Monitored Resource Type
            - Applicable only for I(action=search_monitored_resource_associations).
        type: str
    association_type:
        description:
            - Association type to be created between source and destination resources
            - Required for I(action=associate).
        type: str
    monitored_resource_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored resource.
            - Required for I(action=change_compartment), I(action=disable_external_database), I(action=search_monitored_resource_members).
        type: str
    destination_resource_id:
        description:
            - Destination Monitored Resource Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            - Required for I(action=associate).
        type: str
    limit_level:
        description:
            - The field which determines the depth of hierarchy while searching for members
            - Applicable only for I(action=search_monitored_resource_members).
        type: int
    compartment_id:
        description:
            - Compartment Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            - Required for I(action=associate), I(action=change_compartment), I(action=disassociate), I(action=search_monitored_resource_associations),
              I(action=search).
        type: str
    name:
        description:
            - A filter to return resources that match exact resource name
            - Applicable only for I(action=search).
        type: str
    name_contains:
        description:
            - A filter to return resources that match resource name pattern given. The match is not case sensitive.
            - Applicable only for I(action=search).
        type: str
    type:
        description:
            - A filter to return resources that match resource type
            - Applicable only for I(action=search).
        type: str
    host_name:
        description:
            - A filter to return resources with host name match
            - Applicable only for I(action=search).
        type: str
    external_id:
        description:
            - "External resource is any OCI resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
              which is not a Stack Monitoring service resource.
              Currently supports only following resource type identifiers - externalcontainerdatabase,
              externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance."
            - Applicable only for I(action=search).
        type: str
    host_name_contains:
        description:
            - A filter to return resources with host name pattern
            - Applicable only for I(action=search).
        type: str
    management_agent_id:
        description:
            - A filter to return resources with matching management agent id.
            - Applicable only for I(action=search).
        type: str
    lifecycle_state:
        description:
            - A filter to return resources with matching lifecycle state.
            - Applicable only for I(action=search).
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    time_created_greater_than_or_equal_to:
        description:
            - "Search for resources that were created within a specific date range,
              using this parameter to specify the earliest creation date for the
              returned list (inclusive). Specifying this parameter without the
              corresponding `timeCreatedLessThan` parameter will retrieve resources created from the
              given `timeCreatedGreaterThanOrEqualTo` to the current time, in \\"YYYY-MM-ddThh:mmZ\\" format with a
              Z offset, as defined by L(RFC 3339,https://tools.ietf.org/html/rfc3339)."
            - "**Example:** 2016-12-19T16:39:57.600Z"
            - Applicable only for I(action=search).
        type: str
    time_created_less_than:
        description:
            - "Search for resources that were created within a specific date range,
              using this parameter to specify the latest creation date for the returned
              list (exclusive). Specifying this parameter without the corresponding
              `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all resources created before the
              specified end date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as
              defined by L(RFC 3339,https://tools.ietf.org/html/rfc3339)."
            - "**Example:** 2016-12-19T16:39:57.600Z"
            - Applicable only for I(action=search).
        type: str
    time_updated_greater_than_or_equal_to:
        description:
            - "Search for resources that were updated within a specific date range,
              using this parameter to specify the earliest update date for the
              returned list (inclusive). Specifying this parameter without the
              corresponding `timeUpdatedLessThan` parameter will retrieve resources updated from the
              given `timeUpdatedGreaterThanOrEqualTo` to the current time, in \\"YYYY-MM-ddThh:mmZ\\" format with a
              Z offset, as defined by L(RFC 3339,https://tools.ietf.org/html/rfc3339)."
            - "**Example:** 2016-12-19T16:39:57.600Z"
            - Applicable only for I(action=search).
        type: str
    time_updated_less_than:
        description:
            - "Search for resources that were updated within a specific date range,
              using this parameter to specify the latest creation date for the returned
              list (exclusive). Specifying this parameter without the corresponding
              `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated before the
              specified end date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as
              defined by L(RFC 3339,https://tools.ietf.org/html/rfc3339)."
            - "**Example:** 2016-12-19T16:39:57.600Z"
            - Applicable only for I(action=search).
        type: str
    resource_time_zone:
        description:
            - Time zone in the form of tz database canonical zone ID.
            - Applicable only for I(action=search).
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
            - Applicable only for I(action=search_monitored_resource_associations)I(action=search_monitored_resource_members)I(action=search).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for timeCreated is descending. Default order for assocType is descending.
            - Applicable only for I(action=search_monitored_resource_associations)I(action=search_monitored_resource_members)I(action=search).
        type: str
        choices:
            - "TIME_CREATED"
            - "ASSOC_TYPE"
            - "resourceName"
            - "resourceType"
            - "sourceResourceType"
            - "RESOURCE_NAME"
    property_equals:
        description:
            - Criteria based on resource property.
            - Applicable only for I(action=search).
        type: dict
    fields:
        description:
            - "Partial response refers to an optimization technique offered
              by the RESTful web APIs, to return only the information
              (fields) required by the client. In this mechanism, the client
              sends the required field names as the query parameters for
              an API to the server, and the server trims down the default
              response content by removing the fields that are not required
              by the client. The parameter controls which fields to
              return and should be a query string parameter called \\"fields\\" of
              an array type, provide the values as enums, and use collectionFormat."
            - Applicable only for I(action=search).
        type: list
        elements: str
    exclude_fields:
        description:
            - "Partial response refers to an optimization technique offered
              by the RESTful web APIs, to return all the information except
              the fields requested to be excluded (excludeFields) by the client.
              In this mechanism, the client
              sends the exclude field names as the query parameters for
              an API to the server, and the server trims down the default
              response content by removing the fields that are not required
              by the client. The parameter controls which fields to
              exlude and to return and should be a query string parameter
              called \\"excludeFields\\" of an array type, provide the values
              as enums, and use collectionFormat."
            - Applicable only for I(action=search).
        type: list
        elements: str
    action:
        description:
            - The action to perform on the MonitoredResource.
        type: str
        required: true
        choices:
            - "associate"
            - "change_compartment"
            - "disable_external_database"
            - "disassociate"
            - "search_monitored_resource_associations"
            - "search_monitored_resource_members"
            - "search"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action associate on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    source_resource_id: "ocid1.sourceresource.oc1..xxxxxxEXAMPLExxxxxx"
    association_type: association_type_example
    destination_resource_id: "ocid1.destinationresource.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: associate

- name: Perform action change_compartment on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    monitored_resource_id: "ocid1.monitoredresource.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action disable_external_database on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    monitored_resource_id: "ocid1.monitoredresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_database

- name: Perform action disassociate on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: disassociate

    # optional
    source_resource_id: "ocid1.sourceresource.oc1..xxxxxxEXAMPLExxxxxx"
    association_type: association_type_example
    destination_resource_id: "ocid1.destinationresource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action search_monitored_resource_associations on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: search_monitored_resource_associations

    # optional
    source_resource_id: "ocid1.sourceresource.oc1..xxxxxxEXAMPLExxxxxx"
    source_resource_name: source_resource_name_example
    source_resource_type: source_resource_type_example
    destination_resource_name: destination_resource_name_example
    destination_resource_type: destination_resource_type_example
    association_type: association_type_example
    destination_resource_id: "ocid1.destinationresource.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: TIME_CREATED

- name: Perform action search_monitored_resource_members on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    monitored_resource_id: "ocid1.monitoredresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: search_monitored_resource_members

    # optional
    destination_resource_id: "ocid1.destinationresource.oc1..xxxxxxEXAMPLExxxxxx"
    limit_level: 56
    sort_order: ASC
    sort_by: TIME_CREATED

- name: Perform action search on monitored_resource
  oci_stack_monitoring_monitored_resource_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: search

    # optional
    name: name_example
    name_contains: name_contains_example
    type: type_example
    host_name: host_name_example
    external_id: "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx"
    host_name_contains: host_name_contains_example
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    time_created_greater_than_or_equal_to: time_created_greater_than_or_equal_to_example
    time_created_less_than: time_created_less_than_example
    time_updated_greater_than_or_equal_to: time_updated_greater_than_or_equal_to_example
    time_updated_less_than: time_updated_less_than_example
    resource_time_zone: resource_time_zone_example
    sort_order: ASC
    sort_by: TIME_CREATED
    property_equals: null
    fields: [ "fields_example" ]
    exclude_fields: [ "exclude_fields_example" ]

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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored resource.
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
                - Monitored resource type
            returned: on success
            type: str
            sample: type_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tenant_id:
            description:
                - Tenancy Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
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
                - "External resource is any OCI resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
                  which is not a Stack Monitoring service resource.
                  Currently supports only following resource type identifiers - externalcontainerdatabase,
                  externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance."
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
                - The time the the resource was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the the resource was updated. An RFC3339 formatted datetime string
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
                - List of monitored resource properties
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - property name
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - property value
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
                        - Database connector Identifier
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
                        - dbId of the database
                    returned: on success
                    type: str
                    sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
                ssl_secret_id:
                    description:
                        - SSL Secret Identifier for TCPS connector in OCI VaultL(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
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
                        - The master key OCID and applicable only for property value type ENCRYPTION. Key OCID is passed as input to Key management service
                          decrypt API to retrieve the encrypted property value text.
                    returned: on success
                    type: str
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
                source:
                    description:
                        - The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit
                          is 63.
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
                        - "Type of credentials specified in the credentials element. Three possible values - EXISTING, PLAINTEXT and ENCRYPTED. * EXISTING  -
                          Credential is already stored in agent and only credential name need to be passed for existing credential. * PLAINTEXT - The credential
                          properties will have credentials in plain text format. * ENCRYPTED - The credential properties will have credentials stored in vault
                          in encrypted format using KMS client which uses master key for encryption. The same master key will be used to decrypt the credentials
                          before passing on to the management agent."
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
                                - The name of the credential property, should confirm with names of properties of this credential's type. Ex. For JMXCreds type
                                  , credential property name for weblogic user is 'Username'.
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - The value of the credential property name. Ex. For JMXCreds type, credential property value for 'Username' property is
                                  'weblogic'.
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
                        - The source type and source name combination,delimited with (.) separator. Ex. {source type}.{source name} and source type max char
                          limit is 63.
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
                                - The source type and source name combination,delimited with (.) separator. This refers to the pre-existing source which alias
                                  cred should point to. Ex. {source type}.{source name} and source type max char limit is 63.
                            returned: on success
                            type: str
                            sample: source_example
                        name:
                            description:
                                - The name of the pre-existing source credential which alias cred should point to. This should refer to the pre-existing source
                                  attribute binded credential name.
                            returned: on success
                            type: str
                            sample: name_example
                        service:
                            description:
                                - The name of the service owning the credential. Ex stack-monitoring or dbmgmt
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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.stack_monitoring import StackMonitoringClient
    from oci.stack_monitoring.models import AssociateMonitoredResourcesDetails
    from oci.stack_monitoring.models import ChangeMonitoredResourceCompartmentDetails
    from oci.stack_monitoring.models import DisassociateMonitoredResourcesDetails
    from oci.stack_monitoring.models import SearchMonitoredResourceAssociationsDetails
    from oci.stack_monitoring.models import SearchMonitoredResourceMembersDetails
    from oci.stack_monitoring.models import SearchMonitoredResourcesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitoredResourceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        associate
        change_compartment
        disable_external_database
        disassociate
        search_monitored_resource_associations
        search_monitored_resource_members
        search
    """

    def get_get_fn(self):
        return self.client.get_monitored_resource

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitored_resource,
            monitored_resource_id=self.module.params.get("monitored_resource_id"),
        )

    def associate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AssociateMonitoredResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.associate_monitored_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(associate_monitored_resources_details=action_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMonitoredResourceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_monitored_resource_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                change_monitored_resource_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disable_external_database(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disassociate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisassociateMonitoredResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disassociate_monitored_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                disassociate_monitored_resources_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def search_monitored_resource_associations(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchMonitoredResourceAssociationsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.search_monitored_resource_associations,
            call_fn_args=(),
            call_fn_kwargs=dict(
                search_monitored_resource_associations_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def search_monitored_resource_members(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchMonitoredResourceMembersDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.search_monitored_resource_members,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_resource_id=self.module.params.get("monitored_resource_id"),
                search_monitored_resource_members_details=action_details,
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def search(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchMonitoredResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.search_monitored_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                search_monitored_resources_details=action_details,
                fields=self.module.params.get("fields"),
                exclude_fields=self.module.params.get("exclude_fields"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


MonitoredResourceActionsHelperCustom = get_custom_class(
    "MonitoredResourceActionsHelperCustom"
)


class ResourceHelper(
    MonitoredResourceActionsHelperCustom, MonitoredResourceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            source_resource_id=dict(type="str"),
            source_resource_name=dict(type="str"),
            source_resource_type=dict(type="str"),
            destination_resource_name=dict(type="str"),
            destination_resource_type=dict(type="str"),
            association_type=dict(type="str"),
            monitored_resource_id=dict(type="str"),
            destination_resource_id=dict(type="str"),
            limit_level=dict(type="int"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            type=dict(type="str"),
            host_name=dict(type="str"),
            external_id=dict(type="str"),
            host_name_contains=dict(type="str"),
            management_agent_id=dict(type="str"),
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
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            time_updated_greater_than_or_equal_to=dict(type="str"),
            time_updated_less_than=dict(type="str"),
            resource_time_zone=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "TIME_CREATED",
                    "ASSOC_TYPE",
                    "resourceName",
                    "resourceType",
                    "sourceResourceType",
                    "RESOURCE_NAME",
                ],
            ),
            property_equals=dict(type="dict"),
            fields=dict(type="list", elements="str"),
            exclude_fields=dict(type="list", elements="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "associate",
                    "change_compartment",
                    "disable_external_database",
                    "disassociate",
                    "search_monitored_resource_associations",
                    "search_monitored_resource_members",
                    "search",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
