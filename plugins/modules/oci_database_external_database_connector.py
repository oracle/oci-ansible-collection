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
module: oci_database_external_database_connector
short_description: Manage an ExternalDatabaseConnector resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalDatabaseConnector resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new external database connector.
    - "This resource has the following action operations in the M(oci_external_database_connector_actions) module:
      check_external_database_connector_connection_status."
version_added: "2.9"
author: Oracle (@oracle)
options:
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - The user-friendly name for the
              L(external database connector,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
              The name does not have to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Applicable when connector_type is 'MACS'
        type: str
        aliases: ["name"]
    connector_type:
        description:
            - The type of connector used by the external database resource.
            - This parameter is updatable.
        type: str
        choices:
            - "MACS"
        default: "MACS"
    external_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database resource.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    connection_string:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when connector_type is 'MACS'
        type: dict
        suboptions:
            hostname:
                description:
                    - The host name of the database.
                type: str
                required: true
            port:
                description:
                    - The port used to connect to the database.
                type: int
                required: true
            service:
                description:
                    - The name of the service alias used to connect to the database.
                type: str
                required: true
            protocol:
                description:
                    - The protocol used to connect to the database.
                type: str
                choices:
                    - "TCP"
                required: true
    connection_credentials:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when connector_type is 'MACS'
        type: dict
        suboptions:
            credential_type:
                description:
                    - The type of credential used to connect to the database.
                type: str
                choices:
                    - "NAME_REFERENCE"
                    - "DETAILS"
                default: "DETAILS"
            credential_name:
                description:
                    - The name of the credential information that used to connect to the database.
                    - Required when credential_type is 'NAME_REFERENCE'
                type: str
            username:
                description:
                    - The username that will be used to connect to the database.
                    - Required when credential_type is 'DETAILS'
                type: str
            password:
                description:
                    - The password that will be used to connect to the database.
                    - Required when credential_type is 'DETAILS'
                type: str
            role:
                description:
                    - The role of the user that will be connecting to the database.
                    - Required when credential_type is 'DETAILS'
                type: str
                choices:
                    - "SYSDBA"
                    - "NORMAL"
    connector_agent_id:
        description:
            - The ID of the agent used for the
              L(external database connector,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            - Required for create using I(state=present).
        type: str
    external_database_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              external database connector resource (`ExternalDatabaseConnectorId`).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the ExternalDatabaseConnector.
            - Use I(state=present) to create or update an ExternalDatabaseConnector.
            - Use I(state=absent) to delete an ExternalDatabaseConnector.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_database_connector
  oci_database_external_database_connector:
    display_name: "myTestConn"
    connection_string:
      hostname: "myHost.test"
      port: 1521
      service: "testService"
      protocol: "TCP"
    connection_credentials:
      username: "testUser"
      password: "greatPassword"
      role: "SYSDBA"
    connector_type: "MACS"
    connector_agent_id: "ocid"
    external_database_id: "ocid"

- name: Update external_database_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_external_database_connector:
    connection_credentials:
      username: "testUser"
      password: "greatPassword2"
      role: "SYSDBA"

- name: Update external_database_connector
  oci_database_external_database_connector:
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete external_database_connector
  oci_database_external_database_connector:
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_database_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_external_database_connector:
    display_name: myTestConn
    external_database_id: ocid
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateExternalDatabaseConnectorDetails
    from oci.database.models import UpdateExternalDatabaseConnectorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDatabaseConnectorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ExternalDatabaseConnectorHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "external_database_id",
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
            self.client.list_external_database_connectors, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalDatabaseConnectorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_database_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_database_connector_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExternalDatabaseConnectorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_database_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_database_connector_id=self.module.params.get(
                    "external_database_connector_id"
                ),
                update_external_database_connector_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_external_database_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_database_connector_id=self.module.params.get(
                    "external_database_connector_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalDatabaseConnectorHelperCustom = get_custom_class(
    "ExternalDatabaseConnectorHelperCustom"
)


class ResourceHelper(
    ExternalDatabaseConnectorHelperCustom, ExternalDatabaseConnectorHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            connector_type=dict(type="str", default="MACS", choices=["MACS"]),
            external_database_id=dict(type="str"),
            connection_string=dict(
                type="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    port=dict(type="int", required=True),
                    service=dict(type="str", required=True),
                    protocol=dict(type="str", required=True, choices=["TCP"]),
                ),
            ),
            connection_credentials=dict(
                type="dict",
                options=dict(
                    credential_type=dict(
                        type="str",
                        default="DETAILS",
                        choices=["NAME_REFERENCE", "DETAILS"],
                    ),
                    credential_name=dict(type="str"),
                    username=dict(type="str"),
                    password=dict(type="str", no_log=True),
                    role=dict(type="str", choices=["SYSDBA", "NORMAL"]),
                ),
            ),
            connector_agent_id=dict(type="str"),
            external_database_connector_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
