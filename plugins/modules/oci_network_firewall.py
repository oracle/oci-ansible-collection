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
module: oci_network_firewall
short_description: Manage a NetworkFirewall resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NetworkFirewall resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new NetworkFirewall.
    - "This resource has the following action operations in the M(oracle.oci.oci_network_firewall_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Network Firewall.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet associated with the Network Firewall.
            - Required for create using I(state=present).
        type: str
    availability_domain:
        description:
            - "Availability Domain where Network Firewall instance is created.
              To get a list of availability domains for a tenancy, use L(ListAvailabilityDomains,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/identity/20160918/AvailabilityDomain/ListAvailabilityDomains) operation.
              Example: `kIdk:PHX-AD-1`"
        type: str
    ipv4_address:
        description:
            - IPv4 address for the Network Firewall.
        type: str
    ipv6_address:
        description:
            - IPv6 address for the Network Firewall.
        type: str
    display_name:
        description:
            - A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    network_firewall_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall Policy.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    network_security_group_ids:
        description:
            - An array of network security groups L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with the
              Network Firewall.
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    network_firewall_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NetworkFirewall.
            - Use I(state=present) to create or update a NetworkFirewall.
            - Use I(state=absent) to delete a NetworkFirewall.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create network_firewall
  oci_network_firewall:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    ipv4_address: ipv4_address_example
    ipv6_address: ipv6_address_example
    display_name: display_name_example
    network_security_group_ids: [ "network_security_group_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_firewall
  oci_network_firewall:
    # required
    network_firewall_id: "ocid1.networkfirewall.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    network_security_group_ids: [ "network_security_group_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_firewall using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_firewall:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    network_security_group_ids: [ "network_security_group_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete network_firewall
  oci_network_firewall:
    # required
    network_firewall_id: "ocid1.networkfirewall.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete network_firewall using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_firewall:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
network_firewall:
    description:
        - Details of the NetworkFirewall resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Network Firewall.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet associated with the Network Firewall.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        ipv4_address:
            description:
                - IPv4 address for the Network Firewall.
            returned: on success
            type: str
            sample: ipv4_address_example
        ipv6_address:
            description:
                - IPv6 address for the Network Firewall.
            returned: on success
            type: str
            sample: ipv6_address_example
        network_firewall_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Network Firewall Policy.
            returned: on success
            type: str
            sample: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - "Availability Domain where Network Firewall instance is created.
                  To get a list of availability domains for a tenancy, use L(ListAvailabilityDomains,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/identity/20160918/AvailabilityDomain/ListAvailabilityDomains) operation.
                  Example: `kIdk:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        network_security_group_ids:
            description:
                - An array of network security groups L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with the
                  Network Firewall.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - "The time instant at which the Network Firewall was created in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time instant at which the Network Firewall was updated in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Network Firewall.
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ipv4_address": "ipv4_address_example",
        "ipv6_address": "ipv6_address_example",
        "network_firewall_policy_id": "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "network_security_group_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.network_firewall import NetworkFirewallClient
    from oci.network_firewall.models import CreateNetworkFirewallDetails
    from oci.network_firewall.models import UpdateNetworkFirewallDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkFirewallHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(NetworkFirewallHelperGen, self).get_possible_entity_types() + [
            "networkfirewall",
            "networkfirewalls",
            "networkFirewallnetworkfirewall",
            "networkFirewallnetworkfirewalls",
            "networkfirewallresource",
            "networkfirewallsresource",
        ]

    def get_module_resource_id_param(self):
        return "network_firewall_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_firewall_id")

    def get_get_fn(self):
        return self.client.get_network_firewall

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_firewall, network_firewall_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_firewall,
            network_firewall_id=self.module.params.get("network_firewall_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "availability_domain"]
            if self._use_name_as_identifier()
            else ["display_name", "network_firewall_policy_id", "availability_domain"]
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
            self.client.list_network_firewalls, **kwargs
        )

    def get_create_model_class(self):
        return CreateNetworkFirewallDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_network_firewall,
            call_fn_args=(),
            call_fn_kwargs=dict(create_network_firewall_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNetworkFirewallDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_firewall,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_firewall_id=self.module.params.get("network_firewall_id"),
                update_network_firewall_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_network_firewall,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_firewall_id=self.module.params.get("network_firewall_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkFirewallHelperCustom = get_custom_class("NetworkFirewallHelperCustom")


class ResourceHelper(NetworkFirewallHelperCustom, NetworkFirewallHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            availability_domain=dict(type="str"),
            ipv4_address=dict(type="str"),
            ipv6_address=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            network_firewall_policy_id=dict(type="str"),
            network_security_group_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            network_firewall_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_firewall",
        service_client_class=NetworkFirewallClient,
        namespace="network_firewall",
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
