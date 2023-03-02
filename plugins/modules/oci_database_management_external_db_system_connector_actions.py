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
module: oci_database_management_external_db_system_connector_actions
short_description: Perform actions on an ExternalDbSystemConnector resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExternalDbSystemConnector resource in Oracle Cloud Infrastructure
    - For I(action=check_external_db_system_connector_connection_status), checks the status of the external DB system component connection specified in this
      connector.
      This operation will refresh the connectionStatus and timeConnectionStatusLastUpdated fields.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_db_system_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ExternalDbSystemConnector.
        type: str
        required: true
        choices:
            - "check_external_db_system_connector_connection_status"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action check_external_db_system_connector_connection_status on external_db_system_connector
  oci_database_management_external_db_system_connector_actions:
    # required
    external_db_system_connector_id: "ocid1.externaldbsystemconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: check_external_db_system_connector_connection_status

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemConnectorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        check_external_db_system_connector_connection_status
    """

    @staticmethod
    def get_module_resource_id_param():
        return "external_db_system_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_db_system_connector_id")

    def get_get_fn(self):
        return self.client.get_external_db_system_connector

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_connector,
            external_db_system_connector_id=self.module.params.get(
                "external_db_system_connector_id"
            ),
        )

    def check_external_db_system_connector_connection_status(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.check_external_db_system_connector_connection_status,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_connector_id=self.module.params.get(
                    "external_db_system_connector_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


ExternalDbSystemConnectorActionsHelperCustom = get_custom_class(
    "ExternalDbSystemConnectorActionsHelperCustom"
)


class ResourceHelper(
    ExternalDbSystemConnectorActionsHelperCustom,
    ExternalDbSystemConnectorActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            external_db_system_connector_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=["check_external_db_system_connector_connection_status"],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
