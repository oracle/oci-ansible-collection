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
module: oci_waf_network_address_list
short_description: Manage a NetworkAddressList resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NetworkAddressList resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new NetworkAddressList.
    - "This resource has the following action operations in the M(oracle.oci.oci_waf_network_address_list_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - NetworkAddressList display name, can be renamed.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    type:
        description:
            - Type of NetworkAddressList.
            - Required for create using I(state=present), update using I(state=present) with network_address_list_id present.
        type: str
        choices:
            - "VCN_ADDRESSES"
            - "ADDRESSES"
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
    system_tags:
        description:
            - "Usage of system tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            - This parameter is updatable.
        type: dict
    vcn_addresses:
        description:
            - "A list of private address prefixes, each associated with a particular VCN.
              To specify all addresses in a VCN, use \\"0.0.0.0/0\\" for IPv4 and \\"::/0\\" for IPv6."
            - This parameter is updatable.
            - Required when type is 'VCN_ADDRESSES'
        type: list
        elements: dict
        suboptions:
            vcn_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
                    - Required when type is 'VCN_ADDRESSES'
                type: str
                required: true
            addresses:
                description:
                    - A private IP address or CIDR IP address range.
                    - Required when type is 'VCN_ADDRESSES'
                type: str
                required: true
    addresses:
        description:
            - "A list of IP address prefixes in CIDR notation.
              To specify all addresses, use \\"0.0.0.0/0\\" for IPv4 and \\"::/0\\" for IPv6."
            - This parameter is updatable.
            - Required when type is 'ADDRESSES'
        type: list
        elements: str
    network_address_list_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the NetworkAddressList.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NetworkAddressList.
            - Use I(state=present) to create or update a NetworkAddressList.
            - Use I(state=absent) to delete a NetworkAddressList.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create network_address_list with type = VCN_ADDRESSES
  oci_waf_network_address_list:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: VCN_ADDRESSES

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    vcn_addresses:
    - # required
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      addresses: addresses_example

- name: Create network_address_list with type = ADDRESSES
  oci_waf_network_address_list:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: ADDRESSES

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    addresses: [ "addresses_example" ]

- name: Update network_address_list with type = VCN_ADDRESSES
  oci_waf_network_address_list:
    # required
    type: VCN_ADDRESSES

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    vcn_addresses:
    - # required
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      addresses: addresses_example

- name: Update network_address_list with type = ADDRESSES
  oci_waf_network_address_list:
    # required
    type: ADDRESSES

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    addresses: [ "addresses_example" ]

- name: Update network_address_list using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = VCN_ADDRESSES
  oci_waf_network_address_list:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: VCN_ADDRESSES

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    vcn_addresses:
    - # required
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      addresses: addresses_example

- name: Update network_address_list using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = ADDRESSES
  oci_waf_network_address_list:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: ADDRESSES

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    addresses: [ "addresses_example" ]

- name: Delete network_address_list
  oci_waf_network_address_list:
    # required
    network_address_list_id: "ocid1.networkaddresslist.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete network_address_list using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waf_network_address_list:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
network_address_list:
    description:
        - Details of the NetworkAddressList resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the NetworkAddressList.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - NetworkAddressList display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the NetworkAddressList was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the NetworkAddressList was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the NetworkAddressList.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in FAILED state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        type:
            description:
                - Type of NetworkAddressList.
            returned: on success
            type: str
            sample: ADDRESSES
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
        addresses:
            description:
                - "A list of IP address prefixes in CIDR notation.
                  To specify all addresses, use \\"0.0.0.0/0\\" for IPv4 and \\"::/0\\" for IPv6."
            returned: on success
            type: list
            sample: []
        vcn_addresses:
            description:
                - "A list of private address prefixes, each associated with a particular VCN.
                  To specify all addresses in a VCN, use \\"0.0.0.0/0\\" for IPv4 and \\"::/0\\" for IPv6."
            returned: on success
            type: complex
            contains:
                vcn_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                addresses:
                    description:
                        - A private IP address or CIDR IP address range.
                    returned: on success
                    type: str
                    sample: addresses_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "type": "ADDRESSES",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "addresses": [],
        "vcn_addresses": [{
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "addresses": "addresses_example"
        }]
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
    from oci.waf import WafClient
    from oci.waf.models import CreateNetworkAddressListDetails
    from oci.waf.models import UpdateNetworkAddressListDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkAddressListHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "network_address_list_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_address_list_id")

    def get_get_fn(self):
        return self.client.get_network_address_list

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_address_list,
            network_address_list_id=self.module.params.get("network_address_list_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_network_address_lists, **kwargs
        )

    def get_create_model_class(self):
        return CreateNetworkAddressListDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_network_address_list,
            call_fn_args=(),
            call_fn_kwargs=dict(create_network_address_list_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNetworkAddressListDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_address_list,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_address_list_id=self.module.params.get(
                    "network_address_list_id"
                ),
                update_network_address_list_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_network_address_list,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_address_list_id=self.module.params.get(
                    "network_address_list_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkAddressListHelperCustom = get_custom_class("NetworkAddressListHelperCustom")


class ResourceHelper(NetworkAddressListHelperCustom, NetworkAddressListHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            type=dict(type="str", choices=["VCN_ADDRESSES", "ADDRESSES"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            vcn_addresses=dict(
                type="list",
                elements="dict",
                options=dict(
                    vcn_id=dict(type="str", required=True),
                    addresses=dict(type="str", required=True),
                ),
            ),
            addresses=dict(type="list", elements="str"),
            network_address_list_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_address_list",
        service_client_class=WafClient,
        namespace="waf",
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
