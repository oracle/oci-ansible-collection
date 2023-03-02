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
module: oci_database_management_external_db_system_connector
short_description: Manage an ExternalDbSystemConnector resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalDbSystemConnector resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new external connector.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_external_db_system_connector_actions) module:
      check_external_db_system_connector_connection_status."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The user-friendly name for the external connector. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
            - Required for create using I(state=present).
        type: str
    agent_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
              used for the external DB system connector.
            - Required for create using I(state=present).
        type: str
    connector_type:
        description:
            - The type of connector.
            - Required for create using I(state=present), update using I(state=present) with external_db_system_connector_id present.
        type: str
        choices:
            - "MACS"
    connection_info:
        description:
            - ""
            - Required for update using I(state=present) with external_db_system_connector_id present.
            - Applicable when connector_type is 'MACS'
        type: dict
        suboptions:
            component_type:
                description:
                    - The component type.
                type: str
                choices:
                    - "ASM"
                    - "DATABASE"
                required: true
            connection_string:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    hosts:
                        description:
                            - The list of host names of the ASM instances.
                            - Required when component_type is 'ASM'
                        type: list
                        elements: str
                    host_name:
                        description:
                            - The host name of the database or the SCAN name in case of a RAC database.
                            - Required when component_type is 'DATABASE'
                        type: str
                    port:
                        description:
                            - The port used to connect to the ASM instance.
                        type: int
                        required: true
                    service:
                        description:
                            - The service name of the ASM instance.
                        type: str
                        required: true
                    protocol:
                        description:
                            - The protocol used to connect to the ASM instance.
                        type: str
                        choices:
                            - "TCP"
                            - "TCPS"
                        required: true
            connection_credentials:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    ssl_secret_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the SSL keystore and
                              truststore details.
                            - Required when credential_type is 'SSL_DETAILS'
                        type: str
                    credential_type:
                        description:
                            - The type of credential used to connect to the ASM instance.
                        type: str
                        choices:
                            - "NAME_REFERENCE"
                            - "DETAILS"
                            - "SSL_DETAILS"
                        default: "DETAILS"
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
                            - Required when credential_type is 'NAME_REFERENCE'
                        type: str
                    user_name:
                        description:
                            - The user name used to connect to the ASM instance.
                            - Required when credential_type is one of ['SSL_DETAILS', 'DETAILS']
                        type: str
                    password_secret_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the user password.
                            - Required when credential_type is one of ['SSL_DETAILS', 'DETAILS']
                        type: str
                    role:
                        description:
                            - The role of the user connecting to the ASM instance.
                            - Required when credential_type is one of ['SSL_DETAILS', 'DETAILS']
                        type: str
                        choices:
                            - "SYSASM"
                            - "SYSDBA"
                            - "SYSOPER"
                            - "NORMAL"
    external_db_system_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExternalDbSystemConnector.
            - Use I(state=present) to create or update an ExternalDbSystemConnector.
            - Use I(state=absent) to delete an ExternalDbSystemConnector.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_db_system_connector with connector_type = MACS
  oci_database_management_external_db_system_connector:
    # required
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    connector_type: MACS

    # optional
    display_name: display_name_example
    connection_info:
      # required
      component_type: ASM
      connection_string:
        # required
        port: 56
        service: service_example
        protocol: TCP

        # optional
        hosts: [ "hosts_example" ]
        host_name: host_name_example
      connection_credentials:
        # required
        credential_type: NAME_REFERENCE
        credential_name: credential_name_example

- name: Update external_db_system_connector with connector_type = MACS
  oci_database_management_external_db_system_connector:
    # required
    connector_type: MACS

    # optional
    connection_info:
      # required
      component_type: ASM
      connection_string:
        # required
        port: 56
        service: service_example
        protocol: TCP

        # optional
        hosts: [ "hosts_example" ]
        host_name: host_name_example
      connection_credentials:
        # required
        credential_type: NAME_REFERENCE
        credential_name: credential_name_example

- name: Update external_db_system_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connector_type = MACS
  oci_database_management_external_db_system_connector:
    # required
    connector_type: MACS

    # optional
    display_name: display_name_example
    connection_info:
      # required
      component_type: ASM
      connection_string:
        # required
        port: 56
        service: service_example
        protocol: TCP

        # optional
        hosts: [ "hosts_example" ]
        host_name: host_name_example
      connection_credentials:
        # required
        credential_type: NAME_REFERENCE
        credential_name: credential_name_example

- name: Delete external_db_system_connector
  oci_database_management_external_db_system_connector:
    # required
    external_db_system_connector_id: "ocid1.externaldbsystemconnector.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_db_system_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_db_system_connector:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
external_db_system_connector:
    description:
        - Details of the ExternalDbSystemConnector resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        connector_type:
            description:
                - The type of connector.
            returned: on success
            type: str
            sample: MACS
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system connector.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external connector. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the connector is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
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
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB system connector.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_connection_status_last_updated:
            description:
                - The date and time the connectionStatus of the external DB system connector was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time the external DB system connector was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB system connector was last updated.
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
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the user password.
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
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the SSL keystore
                                  and truststore details.
                            returned: on success
                            type: str
                            sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "connector_type": "MACS",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_status": "connection_status_example",
        "connection_failure_message": "connection_failure_message_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.database_management.models import CreateExternalDbSystemConnectorDetails
    from oci.database_management.models import UpdateExternalDbSystemConnectorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemConnectorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ExternalDbSystemConnectorHelperGen, self
        ).get_possible_entity_types() + [
            "externaldbsystemconnector",
            "externaldbsystemconnectors",
            "databaseManagementexternaldbsystemconnector",
            "databaseManagementexternaldbsystemconnectors",
            "externaldbsystemconnectorresource",
            "externaldbsystemconnectorsresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_db_system_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_db_system_connector_id")

    def get_get_fn(self):
        return self.client.get_external_db_system_connector

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_connector,
            external_db_system_connector_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_connector,
            external_db_system_connector_id=self.module.params.get(
                "external_db_system_connector_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["external_db_system_id", "display_name"]

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
            self.client.list_external_db_system_connectors, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalDbSystemConnectorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_db_system_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_db_system_connector_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateExternalDbSystemConnectorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_db_system_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_connector_id=self.module.params.get(
                    "external_db_system_connector_id"
                ),
                update_external_db_system_connector_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_external_db_system_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_connector_id=self.module.params.get(
                    "external_db_system_connector_id"
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


ExternalDbSystemConnectorHelperCustom = get_custom_class(
    "ExternalDbSystemConnectorHelperCustom"
)


class ResourceHelper(
    ExternalDbSystemConnectorHelperCustom, ExternalDbSystemConnectorHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            external_db_system_id=dict(type="str"),
            agent_id=dict(type="str"),
            connector_type=dict(type="str", choices=["MACS"]),
            connection_info=dict(
                type="dict",
                options=dict(
                    component_type=dict(
                        type="str", required=True, choices=["ASM", "DATABASE"]
                    ),
                    connection_string=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            hosts=dict(type="list", elements="str"),
                            host_name=dict(type="str"),
                            port=dict(type="int", required=True),
                            service=dict(type="str", required=True),
                            protocol=dict(
                                type="str", required=True, choices=["TCP", "TCPS"]
                            ),
                        ),
                    ),
                    connection_credentials=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            ssl_secret_id=dict(type="str"),
                            credential_type=dict(
                                type="str",
                                default="DETAILS",
                                choices=["NAME_REFERENCE", "DETAILS", "SSL_DETAILS"],
                            ),
                            credential_name=dict(type="str"),
                            user_name=dict(type="str"),
                            password_secret_id=dict(type="str"),
                            role=dict(
                                type="str",
                                choices=["SYSASM", "SYSDBA", "SYSOPER", "NORMAL"],
                            ),
                        ),
                    ),
                ),
            ),
            external_db_system_connector_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_db_system_connector",
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
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
