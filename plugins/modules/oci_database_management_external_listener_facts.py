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
module: oci_database_management_external_listener_facts
short_description: Fetches details about one or multiple ExternalListener resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalListener resources in Oracle Cloud Infrastructure
    - Lists the listeners in the specified external DB system.
    - If I(external_listener_id) is specified, the details of a single ExternalListener will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_listener_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external listener.
            - Required to get a specific external_listener.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
        type: str
    display_name:
        description:
            - A filter to only return the resources that match the entire display name.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending.
              The `DISPLAYNAME` sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_listener
  oci_database_management_external_listener_facts:
    # required
    external_listener_id: "ocid1.externallistener.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_listeners
  oci_database_management_external_listener_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_listeners:
    description:
        - List of ExternalListener resources
    returned: on success
    type: complex
    contains:
        external_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB home.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.externaldbhome.oc1..xxxxxxEXAMPLExxxxxx"
        listener_alias:
            description:
                - The listener alias.
                - Returned for get operation
            returned: on success
            type: str
            sample: listener_alias_example
        additional_details:
            description:
                - "The additional details of the external listener defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        listener_ora_location:
            description:
                - The location of the listener configuration file listener.ora.
                - Returned for get operation
            returned: on success
            type: str
            sample: listener_ora_location_example
        oracle_home:
            description:
                - The Oracle home location of the listener.
                - Returned for get operation
            returned: on success
            type: str
            sample: oracle_home_example
        host_name:
            description:
                - The name of the host on which the external listener is running.
                - Returned for get operation
            returned: on success
            type: str
            sample: host_name_example
        adr_home_directory:
            description:
                - The directory that stores tracing and logging incidents when Automatic Diagnostic Repository (ADR) is enabled.
                - Returned for get operation
            returned: on success
            type: str
            sample: adr_home_directory_example
        log_directory:
            description:
                - The destination directory of the listener log file.
                - Returned for get operation
            returned: on success
            type: str
            sample: log_directory_example
        trace_directory:
            description:
                - The destination directory of the listener trace file.
                - Returned for get operation
            returned: on success
            type: str
            sample: trace_directory_example
        version:
            description:
                - The listener version.
                - Returned for get operation
            returned: on success
            type: str
            sample: version_example
        endpoints:
            description:
                - The list of protocol addresses the listener is configured to listen on.
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
        listener_type:
            description:
                - The type of listener.
            returned: on success
            type: str
            sample: ASM
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
    sample: [{
        "external_db_home_id": "ocid1.externaldbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "listener_alias": "listener_alias_example",
        "additional_details": {},
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_node_id": "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx",
        "listener_type": "ASM",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalListenerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_listener_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_listener,
            external_listener_id=self.module.params.get("external_listener_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "external_db_system_id",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_listeners, **optional_kwargs
        )


ExternalListenerFactsHelperCustom = get_custom_class(
    "ExternalListenerFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalListenerFactsHelperCustom, ExternalListenerFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_listener_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_db_system_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_listener",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_listeners=result)


if __name__ == "__main__":
    main()
