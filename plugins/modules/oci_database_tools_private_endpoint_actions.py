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
module: oci_database_tools_private_endpoint_actions
short_description: Perform actions on a DatabaseToolsPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseToolsPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Database Tools private endpoint into a different compartment in the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_tools_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Database Tools private endpoint.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the `DatabaseConnectionProfile` to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DatabaseToolsPrivateEndpoint.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on database_tools_private_endpoint
  oci_database_tools_private_endpoint_actions:
    # required
    database_tools_private_endpoint_id: "ocid1.databasetoolsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
database_tools_private_endpoint:
    description:
        - Details of the DatabaseToolsPrivateEndpoint resource acted upon by the current operation
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
    sample: {
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_tools import DatabaseToolsClient
    from oci.database_tools.models import (
        ChangeDatabaseToolsPrivateEndpointCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseToolsPrivateEndpointActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "database_tools_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_tools_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_database_tools_private_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_tools_private_endpoint,
            database_tools_private_endpoint_id=self.module.params.get(
                "database_tools_private_endpoint_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatabaseToolsPrivateEndpointCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_tools_private_endpoint_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_private_endpoint_id=self.module.params.get(
                    "database_tools_private_endpoint_id"
                ),
                change_database_tools_private_endpoint_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseToolsPrivateEndpointActionsHelperCustom = get_custom_class(
    "DatabaseToolsPrivateEndpointActionsHelperCustom"
)


class ResourceHelper(
    DatabaseToolsPrivateEndpointActionsHelperCustom,
    DatabaseToolsPrivateEndpointActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            database_tools_private_endpoint_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_tools_private_endpoint",
        service_client_class=DatabaseToolsClient,
        namespace="database_tools",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
