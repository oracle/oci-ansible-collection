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
module: oci_database_management_external_exadata_storage_connector
short_description: Manage an ExternalExadataStorageConnector resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalExadataStorageConnector resource in Oracle Cloud Infrastructure
    - For I(state=present), create the storage server connector after validating the connection information.
      Or only validates the connection information for creating the connection to the storage server.
      The connector for one storage server is associated with the Exadata infrastructure discovery or existing Exadata infrastructure.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_external_exadata_storage_connector_actions) module: check."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    storage_server_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
            - Required for create using I(state=present).
        type: str
    agent_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
            - Required for create using I(state=present).
        type: str
    connector_name:
        description:
            - The connector name if OCI connector is created.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    connection_uri:
        description:
            - "The unique connection string of the connection. For example, \\"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\\"."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    credential_info:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            username:
                description:
                    - The name of the user.
                type: str
                required: true
            password:
                description:
                    - The password of the user.
                type: str
                required: true
            ssl_trust_store_type:
                description:
                    - The SSL trust store type.
                type: str
                choices:
                    - "JKS"
                    - "BCFKS"
            ssl_trust_store_location:
                description:
                    - The full path of the SSL trust store Location in the agent.
                type: str
            ssl_trust_store_password:
                description:
                    - The password of the SSL trust store Location in the agent.
                type: str
    external_exadata_storage_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connector to the Exadata storage server.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
        type: str
    external_exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the ExternalExadataStorageConnector.
            - Use I(state=present) to create or update an ExternalExadataStorageConnector.
            - Use I(state=absent) to delete an ExternalExadataStorageConnector.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_exadata_storage_connector
  oci_database_management_external_exadata_storage_connector:
    # required
    storage_server_id: "ocid1.storageserver.oc1..xxxxxxEXAMPLExxxxxx"
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    connector_name: connector_name_example
    connection_uri: connection_uri_example
    credential_info:
      # required
      username: username_example
      password: example-password

      # optional
      ssl_trust_store_type: JKS
      ssl_trust_store_location: ssl_trust_store_location_example
      ssl_trust_store_password: example-password

- name: Update external_exadata_storage_connector
  oci_database_management_external_exadata_storage_connector:
    # required
    external_exadata_storage_connector_id: "ocid1.externalexadatastorageconnector.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    connector_name: connector_name_example
    connection_uri: connection_uri_example
    credential_info:
      # required
      username: username_example
      password: example-password

      # optional
      ssl_trust_store_type: JKS
      ssl_trust_store_location: ssl_trust_store_location_example
      ssl_trust_store_password: example-password

- name: Delete external_exadata_storage_connector
  oci_database_management_external_exadata_storage_connector:
    # required
    external_exadata_storage_connector_id: "ocid1.externalexadatastorageconnector.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
external_exadata_storage_connector:
    description:
        - Details of the ExternalExadataStorageConnector resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - The version of the resource.
            returned: on success
            type: str
            sample: version_example
        internal_id:
            description:
                - The internal ID.
            returned: on success
            type: str
            sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the entity.
            returned: on success
            type: str
            sample: status_example
        lifecycle_state:
            description:
                - The current lifecycle state of the database resource.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The timestamp of the creation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The timestamp of the last update.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - The details of the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        additional_details:
            description:
                - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        resource_type:
            description:
                - The type of resource.
            returned: on success
            type: str
            sample: INFRASTRUCTURE_SUMMARY
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of Exadata infrastructure system.
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
            returned: on success
            type: str
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
        connection_uri:
            description:
                - "The unique connection string of the connection. For example, \\"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\\"."
            returned: on success
            type: str
            sample: connection_uri_example
        storage_server_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
            returned: on success
            type: str
            sample: "ocid1.storageserver.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "version": "version_example",
        "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "status_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "additional_details": {},
        "resource_type": "INFRASTRUCTURE_SUMMARY",
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_uri": "connection_uri_example",
        "storage_server_id": "ocid1.storageserver.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.database_management.models import (
        CreateExternalExadataStorageConnectorDetails,
    )
    from oci.database_management.models import (
        UpdateExternalExadataStorageConnectorDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalExadataStorageConnectorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ExternalExadataStorageConnectorHelperGen, self
        ).get_possible_entity_types() + [
            "externalexadatastorageconnector",
            "externalexadatastorageconnectors",
            "databaseManagementexternalexadatastorageconnector",
            "databaseManagementexternalexadatastorageconnectors",
            "externalexadatastorageconnectorresource",
            "externalexadatastorageconnectorsresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_exadata_storage_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_exadata_storage_connector_id")

    def get_get_fn(self):
        return self.client.get_external_exadata_storage_connector

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_storage_connector,
            external_exadata_storage_connector_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_storage_connector,
            external_exadata_storage_connector_id=self.module.params.get(
                "external_exadata_storage_connector_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "external_exadata_infrastructure_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_external_exadata_storage_connectors, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalExadataStorageConnectorDetails

    def get_exclude_attributes(self):
        return ["credential_info", "connector_name"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_exadata_storage_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_exadata_storage_connector_details=create_details,
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
        return UpdateExternalExadataStorageConnectorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_exadata_storage_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_storage_connector_id=self.module.params.get(
                    "external_exadata_storage_connector_id"
                ),
                update_external_exadata_storage_connector_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_external_exadata_storage_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_storage_connector_id=self.module.params.get(
                    "external_exadata_storage_connector_id"
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


ExternalExadataStorageConnectorHelperCustom = get_custom_class(
    "ExternalExadataStorageConnectorHelperCustom"
)


class ResourceHelper(
    ExternalExadataStorageConnectorHelperCustom,
    ExternalExadataStorageConnectorHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            storage_server_id=dict(type="str"),
            agent_id=dict(type="str"),
            connector_name=dict(type="str"),
            connection_uri=dict(type="str"),
            credential_info=dict(
                type="dict",
                options=dict(
                    username=dict(type="str", required=True),
                    password=dict(type="str", required=True, no_log=True),
                    ssl_trust_store_type=dict(type="str", choices=["JKS", "BCFKS"]),
                    ssl_trust_store_location=dict(type="str"),
                    ssl_trust_store_password=dict(type="str", no_log=True),
                ),
            ),
            external_exadata_storage_connector_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_exadata_infrastructure_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_exadata_storage_connector",
        service_client_class=DbManagementClient,
        namespace="database_management",
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
