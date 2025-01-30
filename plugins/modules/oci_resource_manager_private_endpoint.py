#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_resource_manager_private_endpoint
short_description: Manage a PrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a private endpoint in the specified compartment.
    - "This resource has the following action operations in the M(oracle.oci.oci_resource_manager_private_endpoint_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this private endpoint.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The private endpoint display name. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the private endpoint. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN for the private endpoint.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet within the VCN for the private endpoint.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    dns_zones:
        description:
            - DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to
              service provider VCN resolver.
            - This parameter is updatable.
        type: list
        elements: str
    nsg_id_list:
        description:
            - The L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of
              L(network security groups (NSGs),https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)
              for the private endpoint.
              Order does not matter.
            - This parameter is updatable.
        type: list
        elements: str
    is_used_with_configuration_source_provider:
        description:
            - When `true`, allows the private endpoint to be used with a configuration source provider.
            - This parameter is updatable.
        type: bool
    freeform_tags:
        description:
            - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PrivateEndpoint.
            - Use I(state=present) to create or update a PrivateEndpoint.
            - Use I(state=absent) to delete a PrivateEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create private_endpoint
  oci_resource_manager_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    dns_zones: [ "dns_zones_example" ]
    nsg_id_list: [ "nsg_id_list_example" ]
    is_used_with_configuration_source_provider: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update private_endpoint
  oci_resource_manager_private_endpoint:
    # required
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    dns_zones: [ "dns_zones_example" ]
    nsg_id_list: [ "nsg_id_list_example" ]
    is_used_with_configuration_source_provider: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_private_endpoint:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    dns_zones: [ "dns_zones_example" ]
    nsg_id_list: [ "nsg_id_list_example" ]
    is_used_with_configuration_source_provider: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete private_endpoint
  oci_resource_manager_private_endpoint:
    # required
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_private_endpoint:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
private_endpoint:
    description:
        - Details of the PrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this private endpoint.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the private endpoint. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN for the private endpoint.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet within the VCN for the private endpoint.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        source_ips:
            description:
                - The source IP addresses that Resource Manager uses to connect to your network. Automatically assigned by Resource Manager.
            returned: on success
            type: list
            sample: []
        nsg_id_list:
            description:
                - The L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of
                  L(network security groups (NSGs),https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)
                  for the private endpoint.
                  Order does not matter.
            returned: on success
            type: list
            sample: []
        is_used_with_configuration_source_provider:
            description:
                - When `true`, allows the private endpoint to be used with a configuration source provider.
            returned: on success
            type: bool
            sample: true
        dns_zones:
            description:
                - "DNS zones to use for accessing private Git servers.
                  For private Git server instructions, see
                  L(Private Git Server,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git).
                  Specify DNS fully qualified domain names (FQDNs); DNS Proxy forwards related DNS FQDN queries to the consumer DNS resolver.
                  For DNS FQDNs not specified, queries go to service provider VCN resolver.
                  Example: `abc.oraclevcn.com`"
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - "The date and time at which the private endpoint was created.
                  Format is defined by RFC3339.
                  Example: `2020-11-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the private endpoint.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "source_ips": [],
        "nsg_id_list": [],
        "is_used_with_configuration_source_provider": true,
        "dns_zones": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import CreatePrivateEndpointDetails
    from oci.resource_manager.models import UpdatePrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PrivateEndpointHelperGen, self).get_possible_entity_types() + [
            "ormprivateendpoint",
            "ormprivateendpoints",
            "resourceManagerormprivateendpoint",
            "resourceManagerormprivateendpoints",
            "ormprivateendpointresource",
            "ormprivateendpointsresource",
            "privateendpoint",
            "privateendpoints",
            "resourceManagerprivateendpoint",
            "resourceManagerprivateendpoints",
            "privateendpointresource",
            "privateendpointsresource",
            "resourcemanager",
        ]

    def get_module_resource_id_param(self):
        return "private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_private_endpoint

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_endpoint, private_endpoint_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_endpoint,
            private_endpoint_id=self.module.params.get("private_endpoint_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["compartment_id", "private_endpoint_id", "display_name"]
            if self._use_name_as_identifier()
            else ["compartment_id", "private_endpoint_id", "display_name", "vcn_id"]
        )

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
            self.client.list_private_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreatePrivateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(create_private_endpoint_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePrivateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_endpoint_id=self.module.params.get("private_endpoint_id"),
                update_private_endpoint_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_endpoint_id=self.module.params.get("private_endpoint_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PrivateEndpointHelperCustom = get_custom_class("PrivateEndpointHelperCustom")


class ResourceHelper(PrivateEndpointHelperCustom, PrivateEndpointHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            dns_zones=dict(type="list", elements="str"),
            nsg_id_list=dict(type="list", elements="str"),
            is_used_with_configuration_source_provider=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            private_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_endpoint",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
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
