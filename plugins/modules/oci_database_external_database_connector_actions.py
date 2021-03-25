#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_external_database_connector_actions
short_description: Perform actions on an ExternalDatabaseConnector resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExternalDatabaseConnector resource in Oracle Cloud Infrastructure
    - For I(action=check_external_database_connector_connection_status), check the status of the external database connection specified in this connector.
      This operation will refresh the connectionStatus and timeConnectionStatusLastUpdated fields.
version_added: "2.9"
author: Oracle (@oracle)
options:
    external_database_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              external database connector resource (`ExternalDatabaseConnectorId`).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ExternalDatabaseConnector.
        type: str
        required: true
        choices:
            - "check_external_database_connector_connection_status"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action check_external_database_connector_connection_status on external_database_connector
  oci_database_external_database_connector_actions:
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: check_external_database_connector_connection_status

"""

RETURN = """
external_database_connector:
    description:
        - Details of the ExternalDatabaseConnector resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - The user-friendly name for the
                  L(external database connector,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                  The name does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                  L(external database connector,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the external database connector resource.
            returned: on success
            type: string
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external connector was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        connector_type:
            description:
                - The type of connector used by the external database resource.
            returned: on success
            type: string
            sample: MACS
        external_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database resource.
            returned: on success
            type: string
            sample: "ocid1.externaldatabase.oc1..xxxxxxEXAMPLExxxxxx"
        connection_status:
            description:
                - The status of connectivity to the external database.
            returned: on success
            type: string
            sample: connection_status_example
        time_connection_status_last_updated:
            description:
                - The date and time the connectionStatus of this external connector was last updated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        connection_string:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The host name of the database.
                    returned: on success
                    type: string
                    sample: hostname_example
                port:
                    description:
                        - The port used to connect to the database.
                    returned: on success
                    type: int
                    sample: 56
                service:
                    description:
                        - The name of the service alias used to connect to the database.
                    returned: on success
                    type: string
                    sample: service_example
                protocol:
                    description:
                        - The protocol used to connect to the database.
                    returned: on success
                    type: string
                    sample: TCP
        connection_credentials:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                credential_type:
                    description:
                        - The type of credential used to connect to the database.
                    returned: on success
                    type: string
                    sample: NAME_REFERENCE
                credential_name:
                    description:
                        - The name of the credential information that used to connect to the database.
                    returned: on success
                    type: string
                    sample: credential_name_example
                username:
                    description:
                        - The username that will be used to connect to the database.
                    returned: on success
                    type: string
                    sample: username_example
                password:
                    description:
                        - The password that will be used to connect to the database.
                    returned: on success
                    type: string
                    sample: password_example
                role:
                    description:
                        - The role of the user that will be connecting to the database.
                    returned: on success
                    type: string
                    sample: SYSDBA
        connector_agent_id:
            description:
                - The ID of the agent used for the
                  L(external database connector,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            returned: on success
            type: string
            sample: "ocid1.connectoragent.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "connector_type": "MACS",
        "external_database_id": "ocid1.externaldatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_status": "connection_status_example",
        "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
        "connection_string": {
            "hostname": "hostname_example",
            "port": 56,
            "service": "service_example",
            "protocol": "TCP"
        },
        "connection_credentials": {
            "credential_type": "NAME_REFERENCE",
            "credential_name": "credential_name_example",
            "username": "username_example",
            "password": "password_example",
            "role": "SYSDBA"
        },
        "connector_agent_id": "ocid1.connectoragent.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDatabaseConnectorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        check_external_database_connector_connection_status
    """

    def __init__(self, *args, **kwargs):
        super(ExternalDatabaseConnectorActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "external_database_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_database_connector_id")

    def get_get_fn(self):
        return self.client.get_external_database_connector

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_database_connector,
            external_database_connector_id=self.module.params.get(
                "external_database_connector_id"
            ),
        )

    def check_external_database_connector_connection_status(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.check_external_database_connector_connection_status,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_database_connector_id=self.module.params.get(
                    "external_database_connector_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalDatabaseConnectorActionsHelperCustom = get_custom_class(
    "ExternalDatabaseConnectorActionsHelperCustom"
)


class ResourceHelper(
    ExternalDatabaseConnectorActionsHelperCustom,
    ExternalDatabaseConnectorActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            external_database_connector_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=["check_external_database_connector_connection_status"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_database_connector",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
