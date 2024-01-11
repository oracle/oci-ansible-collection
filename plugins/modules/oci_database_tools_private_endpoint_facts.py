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
module: oci_database_tools_private_endpoint_facts
short_description: Fetches details about one or multiple DatabaseToolsPrivateEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseToolsPrivateEndpoint resources in Oracle Cloud Infrastructure
    - Returns a list of Database Tools private endpoints.
    - If I(database_tools_private_endpoint_id) is specified, the details of a single DatabaseToolsPrivateEndpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_tools_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Database Tools private endpoint.
            - Required to get a specific database_tools_private_endpoint.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple database_tools_private_endpoints.
        type: str
    subnet_id:
        description:
            - A filter to return only resources their `subnetId` matches the specified `subnetId`.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    endpoint_service_id:
        description:
            - A filter to return only resources their `endpointServiceId` matches the specified `endpointServiceId`.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their `lifecycleState` matches the specified `lifecycleState`.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire specified display name.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific database_tools_private_endpoint
  oci_database_tools_private_endpoint_facts:
    # required
    database_tools_private_endpoint_id: "ocid1.databasetoolsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List database_tools_private_endpoints
  oci_database_tools_private_endpoint_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated
    endpoint_service_id: "ocid1.endpointservice.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example

"""

RETURN = """
database_tools_private_endpoints:
    description:
        - List of DatabaseToolsPrivateEndpoint resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the Database Tools private
                  endpoint.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A description of the Database Tools private endpoint.
            returned: on success
            type: str
            sample: description_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Tools private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_service_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Tools Endpoint Service.
            returned: on success
            type: str
            sample: "ocid1.endpointservice.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the Database Tools private endpoint was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Database Tools private endpoint was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN that the private endpoint belongs to.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet that the private endpoint belongs to.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the private endpoint's VNIC.
            returned: on success
            type: str
            sample: "ocid1.privateendpointvnic.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_ip:
            description:
                - The private IP address that represents the access point for the associated endpoint service.
            returned: on success
            type: str
            sample: private_endpoint_ip_example
        endpoint_fqdn:
            description:
                - Then FQDN to use for the private endpoint.
            returned: on success
            type: str
            sample: endpoint_fqdn_example
        additional_fqdns:
            description:
                - A list of additional FQDNs that can be also be used for the private endpoint.
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The current state of the Database Tools private endpoint.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        nsg_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups
                  that the private endpoint's VNIC belongs to.  For more information about NSGs, see
                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            returned: on success
            type: list
            sample: []
        reverse_connection_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                reverse_connections_source_ips:
                    description:
                        - A list of IP addresses in the customer VCN to be used as the source IPs for reverse connection packets
                          traveling from the service's VCN to the customer's VCN.
                    returned: on success
                    type: complex
                    contains:
                        source_ip:
                            description:
                                - The IP address in the customer's VCN to be used as the source IP for reverse connection packets
                                  traveling from the customer's VCN to the service's VCN.
                            returned: on success
                            type: str
                            sample: source_ip_example
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "system_tags": {},
        "display_name": "display_name_example",
        "description": "description_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_service_id": "ocid1.endpointservice.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_vnic_id": "ocid1.privateendpointvnic.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_ip": "private_endpoint_ip_example",
        "endpoint_fqdn": "endpoint_fqdn_example",
        "additional_fqdns": [],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "nsg_ids": [],
        "reverse_connection_configuration": {
            "reverse_connections_source_ips": [{
                "source_ip": "source_ip_example"
            }]
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
    from oci.database_tools import DatabaseToolsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseToolsPrivateEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_tools_private_endpoint_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_tools_private_endpoint,
            database_tools_private_endpoint_id=self.module.params.get(
                "database_tools_private_endpoint_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "subnet_id",
            "sort_order",
            "sort_by",
            "endpoint_service_id",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_tools_private_endpoints,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DatabaseToolsPrivateEndpointFactsHelperCustom = get_custom_class(
    "DatabaseToolsPrivateEndpointFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseToolsPrivateEndpointFactsHelperCustom,
    DatabaseToolsPrivateEndpointFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_tools_private_endpoint_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            endpoint_service_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_tools_private_endpoint",
        service_client_class=DatabaseToolsClient,
        namespace="database_tools",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_tools_private_endpoints=result)


if __name__ == "__main__":
    main()
