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
module: oci_database_management_external_cluster_instance_facts
short_description: Fetches details about one or multiple ExternalClusterInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalClusterInstance resources in Oracle Cloud Infrastructure
    - Lists the cluster instances in the specified external cluster.
    - If I(external_cluster_instance_id) is specified, the details of a single ExternalClusterInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_cluster_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster instance.
            - Required to get a specific external_cluster_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    external_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster.
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
            - The option to sort information in ascending (???ASC???) or descending (???DESC???) order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_cluster_instance
  oci_database_management_external_cluster_instance_facts:
    # required
    external_cluster_instance_id: "ocid1.externalclusterinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_cluster_instances
  oci_database_management_external_cluster_instance_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_cluster_id: "ocid1.externalcluster.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_cluster_instances:
    description:
        - List of ExternalClusterInstance resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the cluster instance. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external cluster instance.
            returned: on success
            type: str
            sample: component_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs
                  to.
            returned: on success
            type: str
            sample: "ocid1.externalcluster.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a
                  part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_node_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB node.
            returned: on success
            type: str
            sample: "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The name of the host on which the cluster instance is running.
            returned: on success
            type: str
            sample: host_name_example
        node_role:
            description:
                - The role of the cluster node.
            returned: on success
            type: str
            sample: HUB
        crs_base_directory:
            description:
                - The Oracle base location of Cluster Ready Services (CRS).
            returned: on success
            type: str
            sample: crs_base_directory_example
        adr_home_directory:
            description:
                - The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
            returned: on success
            type: str
            sample: adr_home_directory_example
        lifecycle_state:
            description:
                - The current lifecycle state of the external cluster instance.
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
                - The date and time the external cluster instance was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external cluster instance was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_cluster_id": "ocid1.externalcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_node_id": "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "node_role": "HUB",
        "crs_base_directory": "crs_base_directory_example",
        "adr_home_directory": "adr_home_directory_example",
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


class ExternalClusterInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_cluster_instance_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_cluster_instance,
            external_cluster_instance_id=self.module.params.get(
                "external_cluster_instance_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "external_cluster_id",
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
            self.client.list_external_cluster_instances, **optional_kwargs
        )


ExternalClusterInstanceFactsHelperCustom = get_custom_class(
    "ExternalClusterInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalClusterInstanceFactsHelperCustom, ExternalClusterInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_cluster_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_cluster_id=dict(type="str"),
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
        resource_type="external_cluster_instance",
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

    module.exit_json(external_cluster_instances=result)


if __name__ == "__main__":
    main()
