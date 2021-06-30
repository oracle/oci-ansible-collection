#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_bastion
short_description: Manage a Bastion resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Bastion resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new bastion. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach
      from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a
      private subnet.
    - "This resource has the following action operations in the M(oci_bastion_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    bastion_type:
        description:
            - The type of bastion. Use `standard`.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - The name of the bastion, which can't be changed after creation.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment where the bastion is located.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    target_subnet_id:
        description:
            - The unique identifier (OCID) of the subnet that the bastion connects to.
            - Required for create using I(state=present).
        type: str
    phone_book_entry:
        description:
            - The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.
        type: str
    static_jump_host_ip_addresses:
        description:
            - A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.
            - This parameter is updatable.
        type: list
    client_cidr_block_allow_list:
        description:
            - A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.
            - This parameter is updatable.
        type: list
    max_session_ttl_in_seconds:
        description:
            - The maximum amount of time that any session on the bastion can remain active.
            - This parameter is updatable.
        type: int
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
    bastion_id:
        description:
            - The unique identifier (OCID) of the bastion.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Bastion.
            - Use I(state=present) to create or update a Bastion.
            - Use I(state=absent) to delete a Bastion.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create bastion
  oci_bastion:
    bastion_type: bastion_type_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    target_subnet_id: "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update bastion using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bastion:
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    max_session_ttl_in_seconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update bastion
  oci_bastion:
    max_session_ttl_in_seconds: 56
    freeform_tags: {'Department': 'Finance'}
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete bastion
  oci_bastion:
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete bastion using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bastion:
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
bastion:
    description:
        - Details of the Bastion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        bastion_type:
            description:
                - The type of bastion.
            returned: on success
            type: string
            sample: bastion_type_example
        id:
            description:
                - The unique identifier (OCID) of the bastion, which can't be changed after creation.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the bastion, which can't be changed after creation.
            returned: on success
            type: string
            sample: name_example
        compartment_id:
            description:
                - The unique identifier (OCID) of the compartment where the bastion is located.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        target_vcn_id:
            description:
                - The unique identifier (OCID) of the virtual cloud network (VCN) that the bastion connects to.
            returned: on success
            type: string
            sample: "ocid1.targetvcn.oc1..xxxxxxEXAMPLExxxxxx"
        target_subnet_id:
            description:
                - The unique identifier (OCID) of the subnet that the bastion connects to.
            returned: on success
            type: string
            sample: "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        phone_book_entry:
            description:
                - The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.
            returned: on success
            type: string
            sample: phone_book_entry_example
        client_cidr_block_allow_list:
            description:
                - A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.
            returned: on success
            type: list
            sample: []
        static_jump_host_ip_addresses:
            description:
                - A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.
            returned: on success
            type: list
            sample: []
        private_endpoint_ip_address:
            description:
                - The private IP address of the created private endpoint.
            returned: on success
            type: string
            sample: private_endpoint_ip_address_example
        max_session_ttl_in_seconds:
            description:
                - The maximum amount of time that any session on the bastion can remain active.
            returned: on success
            type: int
            sample: 56
        max_sessions_allowed:
            description:
                - The maximum number of active sessions allowed on the bastion.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The time the bastion was created. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
        time_updated:
            description:
                - "The time the bastion was updated. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The current state of the bastion.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
            returned: on success
            type: string
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
        "bastion_type": "bastion_type_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_vcn_id": "ocid1.targetvcn.oc1..xxxxxxEXAMPLExxxxxx",
        "target_subnet_id": "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "phone_book_entry": "phone_book_entry_example",
        "client_cidr_block_allow_list": [],
        "static_jump_host_ip_addresses": [],
        "private_endpoint_ip_address": "private_endpoint_ip_address_example",
        "max_session_ttl_in_seconds": 56,
        "max_sessions_allowed": 56,
        "time_created": "2020-01-25T21:10:29.600Z",
        "time_updated": "2020-01-25T21:10:29.600Z",
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
    from oci.bastion import BastionClient
    from oci.bastion.models import CreateBastionDetails
    from oci.bastion.models import UpdateBastionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BastionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "bastion_id"

    def get_module_resource_id(self):
        return self.module.params.get("bastion_id")

    def get_get_fn(self):
        return self.client.get_bastion

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bastion, bastion_id=self.module.params.get("bastion_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["bastion_id", "name"]

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
        return oci_common_utils.list_all_resources(self.client.list_bastions, **kwargs)

    def get_create_model_class(self):
        return CreateBastionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_bastion,
            call_fn_args=(),
            call_fn_kwargs=dict(create_bastion_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBastionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_bastion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bastion_id=self.module.params.get("bastion_id"),
                update_bastion_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_bastion,
            call_fn_args=(),
            call_fn_kwargs=dict(bastion_id=self.module.params.get("bastion_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BastionHelperCustom = get_custom_class("BastionHelperCustom")


class ResourceHelper(BastionHelperCustom, BastionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            bastion_type=dict(type="str"),
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            target_subnet_id=dict(type="str"),
            phone_book_entry=dict(type="str"),
            static_jump_host_ip_addresses=dict(type="list"),
            client_cidr_block_allow_list=dict(type="list"),
            max_session_ttl_in_seconds=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            bastion_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bastion",
        service_client_class=BastionClient,
        namespace="bastion",
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
