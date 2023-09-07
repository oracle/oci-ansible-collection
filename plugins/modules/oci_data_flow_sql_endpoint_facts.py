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
module: oci_data_flow_sql_endpoint_facts
short_description: Fetches details about one or multiple SqlEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlEndpoint resources in Oracle Cloud Infrastructure
    - Lists all Sql Endpoints in the specified compartment.
      The query must include compartmentId or sqlEndpointId.
      If the query does not include either compartmentId or sqlEndpointId, an error is returned.
    - If I(sql_endpoint_id) is specified, the details of a single SqlEndpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which to query resources.
        type: str
    sql_endpoint_id:
        description:
            - The unique id of the SQL Endpoint.
            - Required to get a specific sql_endpoint.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - A filter to return only those resources whose sqlEndpointLifecycleState matches the given sqlEndpointLifecycleState.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - The query parameter for the Spark application name.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The ordering of results in ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for displayName is
              ascending. If no value is specified timeCreated is used by default.
        type: str
        choices:
            - "id"
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sql_endpoint
  oci_data_flow_sql_endpoint_facts:
    # required
    sql_endpoint_id: "ocid1.sqlendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List sql_endpoints
  oci_data_flow_sql_endpoint_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sql_endpoint_id: "ocid1.sqlendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: id

"""

RETURN = """
sql_endpoints:
    description:
        - List of SqlEndpoint resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The provision identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The SQL Endpoint name, which can be changed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        jdbc_endpoint_url:
            description:
                - The JDBC URL field. For example, jdbc:spark://{serviceFQDN}:443/default;SparkServerType=DFI
            returned: on success
            type: str
            sample: jdbc_endpoint_url_example
        time_created:
            description:
                - The time the Sql Endpoint was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Sql Endpoint was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Sql Endpoint.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message describing the reason why the resource is in it's current state. Helps bubble up errors in state changes. For example, it can be
                  used to provide actionable information for a resource in the Failed state.
            returned: on success
            type: str
            sample: state_message_example
        sql_endpoint_version:
            description:
                - The version of SQL Endpoint.
            returned: on success
            type: str
            sample: sql_endpoint_version_example
        driver_shape:
            description:
                - The shape of the SQL Endpoint driver instance.
            returned: on success
            type: str
            sample: driver_shape_example
        driver_shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs used for the driver or executors.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 10
                memory_in_gbs:
                    description:
                        - The amount of memory used for the driver or executors.
                    returned: on success
                    type: float
                    sample: 10
        executor_shape:
            description:
                - The shape of the SQL Endpoint executor instance.
            returned: on success
            type: str
            sample: executor_shape_example
        executor_shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs used for the driver or executors.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 10
                memory_in_gbs:
                    description:
                        - The amount of memory used for the driver or executors.
                    returned: on success
                    type: float
                    sample: 10
        min_executor_count:
            description:
                - The minimum number of executors.
            returned: on success
            type: int
            sample: 56
        max_executor_count:
            description:
                - The maximum number of executors.
            returned: on success
            type: int
            sample: 56
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
                - Returned for list operation
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        metastore_id:
            description:
                - The OCID of OCI Hive Metastore.
            returned: on success
            type: str
            sample: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
        lake_id:
            description:
                - The OCID of OCI Lake.
            returned: on success
            type: str
            sample: "ocid1.lake.oc1..xxxxxxEXAMPLExxxxxx"
        warehouse_bucket_uri:
            description:
                - The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here
                  https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html
            returned: on success
            type: str
            sample: warehouse_bucket_uri_example
        description:
            description:
                - The description of the SQL Endpoint.
            returned: on success
            type: str
            sample: description_example
        last_accepted_request_token:
            description:
                - This token is used by Splat, and indicates that the service accepts the request, and that the request is currently being processed.
            returned: on success
            type: str
            sample: last_accepted_request_token_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        spark_advanced_configurations:
            description:
                - "The Spark configuration passed to the running process.
                  See https://spark.apache.org/docs/latest/configuration.html#available-properties.
                  Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
                  Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
                  not allowed to be overwritten will cause a 400 status to be returned."
            returned: on success
            type: dict
            sample: {}
        network_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                access_control_rules:
                    description:
                        - A list of SecureAccessControlRule's to which access is limited to
                    returned: on success
                    type: complex
                    contains:
                        ip_notation:
                            description:
                                - The type of IP notation.
                            returned: on success
                            type: str
                            sample: IP_ADDRESS
                        value:
                            description:
                                - The associated value of the selected IP notation.
                            returned: on success
                            type: str
                            sample: value_example
                        vcn_ips:
                            description:
                                - A comma-separated IP or CIDR address for VCN OCID IP notation selection.
                            returned: on success
                            type: str
                            sample: vcn_ips_example
                public_endpoint_ip:
                    description:
                        - Ip Address of public endpoint
                    returned: on success
                    type: str
                    sample: public_endpoint_ip_example
                network_type:
                    description:
                        - The type of network configuration.
                    returned: on success
                    type: str
                    sample: VCN
                vcn_id:
                    description:
                        - The VCN OCID.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The VCN Subnet OCID.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                host_name_prefix:
                    description:
                        - The host name prefix.
                    returned: on success
                    type: str
                    sample: host_name_prefix_example
                nsg_ids:
                    description:
                        - The OCIDs of Network Security Groups (NSGs).
                    returned: on success
                    type: list
                    sample: []
                private_endpoint_ip:
                    description:
                        - Ip Address of private endpoint
                    returned: on success
                    type: str
                    sample: private_endpoint_ip_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "jdbc_endpoint_url": "jdbc_endpoint_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "sql_endpoint_version": "sql_endpoint_version_example",
        "driver_shape": "driver_shape_example",
        "driver_shape_config": {
            "ocpus": 10,
            "memory_in_gbs": 10
        },
        "executor_shape": "executor_shape_example",
        "executor_shape_config": {
            "ocpus": 10,
            "memory_in_gbs": 10
        },
        "min_executor_count": 56,
        "max_executor_count": 56,
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
        "lake_id": "ocid1.lake.oc1..xxxxxxEXAMPLExxxxxx",
        "warehouse_bucket_uri": "warehouse_bucket_uri_example",
        "description": "description_example",
        "last_accepted_request_token": "last_accepted_request_token_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "spark_advanced_configurations": {},
        "network_configuration": {
            "access_control_rules": [{
                "ip_notation": "IP_ADDRESS",
                "value": "value_example",
                "vcn_ips": "vcn_ips_example"
            }],
            "public_endpoint_ip": "public_endpoint_ip_example",
            "network_type": "VCN",
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "host_name_prefix": "host_name_prefix_example",
            "nsg_ids": [],
            "private_endpoint_ip": "private_endpoint_ip_example"
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowSqlEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "sql_endpoint_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sql_endpoint,
            sql_endpoint_id=self.module.params.get("sql_endpoint_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "sql_endpoint_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_endpoints, **optional_kwargs
        )


DataFlowSqlEndpointFactsHelperCustom = get_custom_class(
    "DataFlowSqlEndpointFactsHelperCustom"
)


class ResourceFactsHelper(
    DataFlowSqlEndpointFactsHelperCustom, DataFlowSqlEndpointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            sql_endpoint_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_endpoint",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_endpoints=result)


if __name__ == "__main__":
    main()
