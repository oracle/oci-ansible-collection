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
module: oci_database_management_external_cluster_facts
short_description: Fetches details about one or multiple ExternalCluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalCluster resources in Oracle Cloud Infrastructure
    - Lists the clusters in the specified external DB system.
    - If I(external_cluster_id) is specified, the details of a single ExternalCluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster.
            - Required to get a specific external_cluster.
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
- name: Get a specific external_cluster
  oci_database_management_external_cluster_facts:
    # required
    external_cluster_id: "ocid1.externalcluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_clusters
  oci_database_management_external_cluster_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_clusters:
    description:
        - List of ExternalCluster resources
    returned: on success
    type: complex
    contains:
        grid_home:
            description:
                - The directory in which Oracle Grid Infrastructure is installed.
                - Returned for get operation
            returned: on success
            type: str
            sample: grid_home_example
        is_flex_cluster:
            description:
                - Indicates whether the cluster is Oracle Flex Cluster or not.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        additional_details:
            description:
                - "The additional details of the external cluster defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        network_configurations:
            description:
                - The list of network address configurations of the external cluster.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                network_number:
                    description:
                        - The network number.
                    returned: on success
                    type: int
                    sample: 56
                network_type:
                    description:
                        - The network type.
                    returned: on success
                    type: str
                    sample: AUTOCONFIG
                subnet:
                    description:
                        - The subnet for the network.
                    returned: on success
                    type: str
                    sample: subnet_example
        vip_configurations:
            description:
                - The list of Virtual IP (VIP) configurations of the external cluster.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                node_name:
                    description:
                        - The name of the node with the VIP.
                    returned: on success
                    type: str
                    sample: node_name_example
                address:
                    description:
                        - The VIP name or IP address.
                    returned: on success
                    type: str
                    sample: address_example
                network_number:
                    description:
                        - The network number from which VIPs are obtained.
                    returned: on success
                    type: int
                    sample: 56
        scan_configurations:
            description:
                - The list of Single Client Access Name (SCAN) configurations of the external cluster.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                scan_name:
                    description:
                        - The name of the SCAN listener.
                    returned: on success
                    type: str
                    sample: scan_name_example
                network_number:
                    description:
                        - The network number from which SCAN VIPs are obtained.
                    returned: on success
                    type: int
                    sample: 56
                scan_port:
                    description:
                        - The port number of the SCAN listener.
                    returned: on success
                    type: int
                    sample: 56
                scan_protocol:
                    description:
                        - The protocol of the SCAN listener.
                    returned: on success
                    type: str
                    sample: TCP
        ocr_file_location:
            description:
                - The location of the Oracle Cluster Registry (OCR).
                - Returned for get operation
            returned: on success
            type: str
            sample: ocr_file_location_example
        version:
            description:
                - The cluster version.
                - Returned for get operation
            returned: on success
            type: str
            sample: version_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external cluster. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external cluster.
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the external cluster.
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
                - The date and time the external cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external cluster was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "grid_home": "grid_home_example",
        "is_flex_cluster": true,
        "additional_details": {},
        "network_configurations": [{
            "network_number": 56,
            "network_type": "AUTOCONFIG",
            "subnet": "subnet_example"
        }],
        "vip_configurations": [{
            "node_name": "node_name_example",
            "address": "address_example",
            "network_number": 56
        }],
        "scan_configurations": [{
            "scan_name": "scan_name_example",
            "network_number": 56,
            "scan_port": 56,
            "scan_protocol": "TCP"
        }],
        "ocr_file_location": "ocr_file_location_example",
        "version": "version_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
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


class ExternalClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_cluster_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_cluster,
            external_cluster_id=self.module.params.get("external_cluster_id"),
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
            self.client.list_external_clusters, **optional_kwargs
        )


ExternalClusterFactsHelperCustom = get_custom_class("ExternalClusterFactsHelperCustom")


class ResourceFactsHelper(
    ExternalClusterFactsHelperCustom, ExternalClusterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_cluster_id=dict(aliases=["id"], type="str"),
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
        resource_type="external_cluster",
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

    module.exit_json(external_clusters=result)


if __name__ == "__main__":
    main()
