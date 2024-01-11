#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_stack_monitoring_monitored_resource_facts
short_description: Fetches details about a MonitoredResource resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a MonitoredResource resource in Oracle Cloud Infrastructure
    - Get monitored resource for the given identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    monitored_resource_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored resource.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific monitored_resource
  oci_stack_monitoring_monitored_resource_facts:
    # required
    monitored_resource_id: "ocid1.monitoredresource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
monitored_resource:
    description:
        - MonitoredResource resource
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

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.stack_monitoring import StackMonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitoredResourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "monitored_resource_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitored_resource,
            monitored_resource_id=self.module.params.get("monitored_resource_id"),
        )


MonitoredResourceFactsHelperCustom = get_custom_class(
    "MonitoredResourceFactsHelperCustom"
)


class ResourceFactsHelper(
    MonitoredResourceFactsHelperCustom, MonitoredResourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            monitored_resource_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="monitored_resource",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(monitored_resource=result)


if __name__ == "__main__":
    main()
