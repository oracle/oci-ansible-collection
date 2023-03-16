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
module: oci_database_management_external_db_system_facts
short_description: Fetches details about one or multiple ExternalDbSystem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalDbSystem resources in Oracle Cloud Infrastructure
    - Lists the external DB systems in the specified compartment.
    - If I(external_db_system_id) is specified, the details of a single ExternalDbSystem will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
            - Required to get a specific external_db_system.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple external_db_systems.
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
- name: Get a specific external_db_system
  oci_database_management_external_db_system_facts:
    # required
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_db_systems
  oci_database_management_external_db_system_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_db_systems:
    description:
        - List of ExternalDbSystem resources
    returned: on success
    type: complex
    contains:
        db_system_discovery_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system discovery.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"
        discovery_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent used during the discovery of the DB
                  system.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.discoveryagent.oc1..xxxxxxEXAMPLExxxxxx"
        is_cluster:
            description:
                - Indicates whether the DB system is a cluster DB system or not.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the DB system. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        home_directory:
            description:
                - The Oracle Grid home directory in case of cluster-based DB system and
                  Oracle home directory in case of single instance-based DB system.
            returned: on success
            type: str
            sample: home_directory_example
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB system resource.
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
                - The date and time the external DB system was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB system was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "db_system_discovery_id": "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_agent_id": "ocid1.discoveryagent.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cluster": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "home_directory": "home_directory_example",
        "database_management_config": {
            "license_model": "LICENSE_INCLUDED"
        },
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


class ExternalDbSystemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_db_system_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system,
            external_db_system_id=self.module.params.get("external_db_system_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_external_db_systems,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ExternalDbSystemFactsHelperCustom = get_custom_class(
    "ExternalDbSystemFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalDbSystemFactsHelperCustom, ExternalDbSystemFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_db_system_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
        resource_type="external_db_system",
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

    module.exit_json(external_db_systems=result)


if __name__ == "__main__":
    main()
