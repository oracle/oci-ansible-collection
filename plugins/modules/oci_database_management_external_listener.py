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
module: oci_database_management_external_listener
short_description: Manage an ExternalListener resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an ExternalListener resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_listener_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external listener.
        type: str
        aliases: ["id"]
        required: true
    external_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the ExternalListener.
            - Use I(state=present) to update an existing an ExternalListener.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update external_listener
  oci_database_management_external_listener:
    # required
    external_listener_id: "ocid1.externallistener.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    external_connector_id: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_listener:
    description:
        - Details of the ExternalListener resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external listener.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external listener. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external listener.
            returned: on success
            type: str
            sample: component_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the listener is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_node_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB node.
            returned: on success
            type: str
            sample: "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB home.
            returned: on success
            type: str
            sample: "ocid1.externaldbhome.oc1..xxxxxxEXAMPLExxxxxx"
        listener_alias:
            description:
                - The listener alias.
            returned: on success
            type: str
            sample: listener_alias_example
        listener_type:
            description:
                - The type of listener.
            returned: on success
            type: str
            sample: ASM
        additional_details:
            description:
                - "The additional details of the external listener defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The current lifecycle state of the external listener.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        listener_ora_location:
            description:
                - The location of the listener configuration file listener.ora.
            returned: on success
            type: str
            sample: listener_ora_location_example
        oracle_home:
            description:
                - The Oracle home location of the listener.
            returned: on success
            type: str
            sample: oracle_home_example
        host_name:
            description:
                - The name of the host on which the external listener is running.
            returned: on success
            type: str
            sample: host_name_example
        adr_home_directory:
            description:
                - The directory that stores tracing and logging incidents when Automatic Diagnostic Repository (ADR) is enabled.
            returned: on success
            type: str
            sample: adr_home_directory_example
        log_directory:
            description:
                - The destination directory of the listener log file.
            returned: on success
            type: str
            sample: log_directory_example
        trace_directory:
            description:
                - The destination directory of the listener trace file.
            returned: on success
            type: str
            sample: trace_directory_example
        version:
            description:
                - The listener version.
            returned: on success
            type: str
            sample: version_example
        endpoints:
            description:
                - The list of protocol addresses the listener is configured to listen on.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The unique name of the service.
                    returned: on success
                    type: str
                    sample: key_example
                protocol:
                    description:
                        - The listener protocol.
                    returned: on success
                    type: str
                    sample: IPC
                services:
                    description:
                        - The list of services registered with the listener.
                    returned: on success
                    type: list
                    sample: []
                host:
                    description:
                        - The host name or IP address.
                    returned: on success
                    type: str
                    sample: host_example
                port:
                    description:
                        - The port number.
                    returned: on success
                    type: int
                    sample: 56
        serviced_databases:
            description:
                - The list of databases that are serviced by the listener.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The user-friendly name for the database. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                db_unique_name:
                    description:
                        - The unique name of the external database.
                    returned: on success
                    type: str
                    sample: db_unique_name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the external database
                          resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                database_type:
                    description:
                        - The type of Oracle Database installation.
                    returned: on success
                    type: str
                    sample: EXTERNAL_SIDB
                database_sub_type:
                    description:
                        - The subtype of Oracle Database. Indicates whether the database is a Container Database,
                          Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.
                    returned: on success
                    type: str
                    sample: CDB
                is_managed:
                    description:
                        - Indicates whether the database is a Managed Database or not.
                    returned: on success
                    type: bool
                    sample: true
        serviced_asms:
            description:
                - The list of ASMs that are serviced by the listener.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external ASM.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The user-friendly name for the external ASM. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the external ASM
                          resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the external listener was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external listener was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_node_id": "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_home_id": "ocid1.externaldbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "listener_alias": "listener_alias_example",
        "listener_type": "ASM",
        "additional_details": {},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "listener_ora_location": "listener_ora_location_example",
        "oracle_home": "oracle_home_example",
        "host_name": "host_name_example",
        "adr_home_directory": "adr_home_directory_example",
        "log_directory": "log_directory_example",
        "trace_directory": "trace_directory_example",
        "version": "version_example",
        "endpoints": [{
            "key": "key_example",
            "protocol": "IPC",
            "services": [],
            "host": "host_example",
            "port": 56
        }],
        "serviced_databases": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "db_unique_name": "db_unique_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "database_type": "EXTERNAL_SIDB",
            "database_sub_type": "CDB",
            "is_managed": true
        }],
        "serviced_asms": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.database_management.models import UpdateExternalListenerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalListenerHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(ExternalListenerHelperGen, self).get_possible_entity_types() + [
            "externallistener",
            "externallisteners",
            "databaseManagementexternallistener",
            "databaseManagementexternallisteners",
            "externallistenerresource",
            "externallistenersresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_listener_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_listener_id")

    def get_get_fn(self):
        return self.client.get_external_listener

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_listener, external_listener_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_listener,
            external_listener_id=self.module.params.get("external_listener_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_external_listeners, **kwargs
        )

    def get_update_model_class(self):
        return UpdateExternalListenerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_listener,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_listener_id=self.module.params.get("external_listener_id"),
                update_external_listener_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalListenerHelperCustom = get_custom_class("ExternalListenerHelperCustom")


class ResourceHelper(ExternalListenerHelperCustom, ExternalListenerHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            external_listener_id=dict(aliases=["id"], type="str", required=True),
            external_connector_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_listener",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
