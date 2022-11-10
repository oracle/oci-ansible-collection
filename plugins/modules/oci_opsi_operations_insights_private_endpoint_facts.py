#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_opsi_operations_insights_private_endpoint_facts
short_description: Fetches details about one or multiple OperationsInsightsPrivateEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OperationsInsightsPrivateEndpoint resources in Oracle Cloud Infrastructure
    - Gets a list of Operation Insights private endpoints.
    - If I(operations_insights_private_endpoint_id) is specified, the details of a single OperationsInsightsPrivateEndpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operations_insights_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Operation Insights private endpoint.
            - Required to get a specific operations_insights_private_endpoint.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name.
        type: str
        aliases: ["name"]
    opsi_private_endpoint_id:
        description:
            - Unique Operations Insights PrivateEndpoint identifier
        type: str
    is_used_for_rac_dbs:
        description:
            - The option to filter OPSI private endpoints that can used for RAC. Should be used along with vcnId query parameter.
        type: bool
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    lifecycle_state:
        description:
            - Lifecycle states
        type: list
        elements: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort private endpoints.
        type: str
        choices:
            - "timeCreated"
            - "id"
            - "displayName"
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific operations_insights_private_endpoint
  oci_opsi_operations_insights_private_endpoint_facts:
    # required
    operations_insights_private_endpoint_id: "ocid1.operationsinsightsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List operations_insights_private_endpoints
  oci_opsi_operations_insights_private_endpoint_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    is_used_for_rac_dbs: true
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: [ "CREATING" ]
    sort_order: ASC
    sort_by: timeCreated
    compartment_id_in_subtree: true

"""

RETURN = """
operations_insights_private_endpoints:
    description:
        - List of OperationsInsightsPrivateEndpoint resources
    returned: on success
    type: complex
    contains:
        private_ip:
            description:
                - The private IP addresses assigned to the private endpoint. All IP addresses will be concatenated if it is RAC DBs.
                - Returned for get operation
            returned: on success
            type: str
            sample: private_ip_example
        nsg_ids:
            description:
                - The OCIDs of the network security groups that the private endpoint belongs to.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - The OCID of the Private service accessed database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the private endpoint.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The compartment OCID of the Private service accessed database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        is_used_for_rac_dbs:
            description:
                - The flag is to identify if private endpoint is used for rac database or not
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - The description of the private endpoint.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the private endpoint was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The current state of the private endpoint.
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
        private_endpoint_status_details:
            description:
                - A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable
                  information about the validity of the private endpoint connection.
            returned: on success
            type: str
            sample: private_endpoint_status_details_example
    sample: [{
        "private_ip": "private_ip_example",
        "nsg_ids": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "is_used_for_rac_dbs": true,
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "private_endpoint_status_details": "private_endpoint_status_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsPrivateEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "operations_insights_private_endpoint_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_private_endpoint,
            operations_insights_private_endpoint_id=self.module.params.get(
                "operations_insights_private_endpoint_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "opsi_private_endpoint_id",
            "is_used_for_rac_dbs",
            "vcn_id",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "compartment_id_in_subtree",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_operations_insights_private_endpoints, **optional_kwargs
        )


OperationsInsightsPrivateEndpointFactsHelperCustom = get_custom_class(
    "OperationsInsightsPrivateEndpointFactsHelperCustom"
)


class ResourceFactsHelper(
    OperationsInsightsPrivateEndpointFactsHelperCustom,
    OperationsInsightsPrivateEndpointFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operations_insights_private_endpoint_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            opsi_private_endpoint_id=dict(type="str"),
            is_used_for_rac_dbs=dict(type="bool"),
            vcn_id=dict(type="str"),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "id", "displayName"]),
            compartment_id_in_subtree=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operations_insights_private_endpoint",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(operations_insights_private_endpoints=result)


if __name__ == "__main__":
    main()
