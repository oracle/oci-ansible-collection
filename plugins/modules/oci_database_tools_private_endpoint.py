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
module: oci_database_tools_private_endpoint
short_description: Manage a DatabaseToolsPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DatabaseToolsPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DatabaseToolsPrivateEndpoint.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_tools_private_endpoint_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the containing Compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A description of the DatabaseToolsPrivateEndpoint.
            - This parameter is updatable.
        type: str
    endpoint_service_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DatabaseToolsEndpointService.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet that the private endpoint belongs to.
            - Required for create using I(state=present).
        type: str
    private_endpoint_ip:
        description:
            - The private IP address that represents the access point for the associated endpoint service.
        type: str
    nsg_ids:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups
              that the private endpoint's VNIC belongs to.  For more information about NSGs, see
              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            - This parameter is updatable.
        type: list
        elements: str
    database_tools_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a DatabaseToolsPrivateEndpoint.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DatabaseToolsPrivateEndpoint.
            - Use I(state=present) to create or update a DatabaseToolsPrivateEndpoint.
            - Use I(state=absent) to delete a DatabaseToolsPrivateEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create database_tools_private_endpoint
  oci_database_tools_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    endpoint_service_id: "ocid1.endpointservice.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    description: description_example
    private_endpoint_ip: private_endpoint_ip_example
    nsg_ids: [ "nsg_ids_example" ]

- name: Update database_tools_private_endpoint
  oci_database_tools_private_endpoint:
    # required
    database_tools_private_endpoint_id: "ocid1.databasetoolsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    display_name: display_name_example
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]

- name: Update database_tools_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_tools_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]

- name: Delete database_tools_private_endpoint
  oci_database_tools_private_endpoint:
    # required
    database_tools_private_endpoint_id: "ocid1.databasetoolsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete database_tools_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_tools_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the containing Compartment.
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
                - A description of the DatabaseToolsPrivateEndpoint.
            returned: on success
            type: str
            sample: description_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DatabaseToolsPrivateEndpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_service_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DatabaseToolsEndpointService.
            returned: on success
            type: str
            sample: "ocid1.endpointservice.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the DatabaseToolsPrivateEndpoint was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the DatabaseToolsPrivateEndpoint was updated. An RFC3339 formatted datetime string
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
                - The current state of the DatabaseToolsPrivateEndpoint.
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database_tools import DatabaseToolsClient
    from oci.database_tools.models import CreateDatabaseToolsPrivateEndpointDetails
    from oci.database_tools.models import UpdateDatabaseToolsPrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseToolsPrivateEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "subnet_id",
            "endpoint_service_id",
            "display_name",
        ]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_database_tools_private_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreateDatabaseToolsPrivateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_database_tools_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_database_tools_private_endpoint_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatabaseToolsPrivateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_database_tools_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_private_endpoint_id=self.module.params.get(
                    "database_tools_private_endpoint_id"
                ),
                update_database_tools_private_endpoint_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_database_tools_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_private_endpoint_id=self.module.params.get(
                    "database_tools_private_endpoint_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseToolsPrivateEndpointHelperCustom = get_custom_class(
    "DatabaseToolsPrivateEndpointHelperCustom"
)


class ResourceHelper(
    DatabaseToolsPrivateEndpointHelperCustom, DatabaseToolsPrivateEndpointHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            endpoint_service_id=dict(type="str"),
            subnet_id=dict(type="str"),
            private_endpoint_ip=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            database_tools_private_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_tools_private_endpoint",
        service_client_class=DatabaseToolsClient,
        namespace="database_tools",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
