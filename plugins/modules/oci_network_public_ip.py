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
module: oci_network_public_ip
short_description: Manage a PublicIp resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PublicIp resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or
      reserved public IP. For information about limits on how many you can create, see
      L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
    - "* **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId`
      with the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the primary private IP you want to assign the public IP
      to. The public IP is
      created in the same availability domain as the private IP. An ephemeral public IP must always be
      assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary
      private IP. Exception: If you create a L(NatGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NatGateway/), Oracle
      automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove."
    - "* **For a reserved public IP:** You may also optionally assign the public IP to a private
      IP by specifying `privateIpId`. Or you can later assign the public IP with
      L(UpdatePublicIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)."
    - "**Note:** When assigning a public IP to a private IP, the private IP must not already have
      a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned."
    - Also, for reserved public IPs, the optional assignment part of this operation is
      asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment
      succeeded.
    - "This resource has the following action operations in the M(oracle.oci.oci_network_public_ip_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the public IP. For ephemeral
              public IPs,
              you must set this to the private IP's compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    lifetime:
        description:
            - Defines when the public IP is deleted and released back to the Oracle Cloud
              Infrastructure public IP pool. For more information, see
              L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
            - Required for create using I(state=present).
        type: str
        choices:
            - "EPHEMERAL"
            - "RESERVED"
    public_ip_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    private_ip_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private IP to assign the public IP to.
            - "Required for an ephemeral public IP because it must always be assigned to a private IP
              (specifically a *primary* private IP)."
            - Optional for a reserved public IP. If you don't provide it, the public IP is created but not
              assigned to a private IP. You can later assign the public IP with
              L(UpdatePublicIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp).
            - This parameter is updatable.
        type: str
    public_ip_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    scope:
        description:
            - Whether the public IP is regional or specific to a particular availability domain.
            - "* `REGION`: The public IP exists within a region and is assigned to a regional entity
              (such as a L(NatGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NatGateway/)), or can be assigned to a private IP
              in any availability domain in the region. Reserved public IPs have `scope` = `REGION`, as do
              ephemeral public IPs assigned to a regional entity."
            - "* `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity
              it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
              Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`."
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        choices:
            - "REGION"
            - "AVAILABILITY_DOMAIN"
    state:
        description:
            - The state of the PublicIp.
            - Use I(state=present) to create or update a PublicIp.
            - Use I(state=absent) to delete a PublicIp.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create public_ip
  oci_network_public_ip:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifetime: EPHEMERAL

    # optional
    public_ip_pool_id: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    private_ip_id: "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update public_ip
  oci_network_public_ip:
    # required
    public_ip_id: "ocid1.publicip.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    private_ip_id: "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update public_ip using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_public_ip:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    scope: REGION

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    private_ip_id: "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete public_ip
  oci_network_public_ip:
    # required
    public_ip_id: "ocid1.publicip.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete public_ip using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_public_ip:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    scope: REGION
    state: absent

"""

RETURN = """
public_ip:
    description:
        - Details of the PublicIp resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        assigned_entity_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the entity the public IP is assigned to, or in the
                  process of
                  being assigned to.
            returned: on success
            type: str
            sample: "ocid1.assignedentity.oc1..xxxxxxEXAMPLExxxxxx"
        assigned_entity_type:
            description:
                - The type of entity the public IP is assigned to, or in the process of being
                  assigned to.
            returned: on success
            type: str
            sample: PRIVATE_IP
        availability_domain:
            description:
                - The public IP's availability domain. This property is set only for ephemeral public IPs
                  that are assigned to a private IP (that is, when the `scope` of the public IP is set to
                  AVAILABILITY_DOMAIN). The value is the availability domain of the assigned private IP.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the public IP. For an
                  ephemeral public IP, this is
                  the compartment of its assigned entity (which can be a private IP or a regional entity such
                  as a NAT gateway). For a reserved public IP that is currently assigned,
                  its compartment can be different from the assigned private IP's.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The public IP's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The public IP address of the `publicIp` object.
                - "Example: `203.0.113.2`"
            returned: on success
            type: str
            sample: ip_address_example
        lifecycle_state:
            description:
                - The public IP's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        lifetime:
            description:
                - Defines when the public IP is deleted and released back to Oracle's public IP pool.
                - "* `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned entity. An ephemeral
                  public IP must always be assigned to an entity. If the assigned entity is a private IP,
                  the ephemeral public IP is automatically deleted when the private IP is deleted, when
                  the VNIC is terminated, or when the instance is terminated. If the assigned entity is a
                  L(NatGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NatGateway/), the ephemeral public IP is automatically
                  deleted when the NAT gateway is terminated."
                - "* `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP
                  whenever you like. It does not need to be assigned to a private IP at all times."
                - For more information and comparison of the two types,
                  see L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
            returned: on success
            type: str
            sample: EPHEMERAL
        private_ip_id:
            description:
                - Deprecated. Use `assignedEntityId` instead.
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private IP that the public IP is currently
                  assigned to, or in the
                  process of being assigned to.
                - "**Note:** This is `null` if the public IP is not assigned to a private IP, or is
                  in the process of being assigned to one."
            returned: on success
            type: str
            sample: "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx"
        scope:
            description:
                - Whether the public IP is regional or specific to a particular availability domain.
                - "* `REGION`: The public IP exists within a region and is assigned to a regional entity
                  (such as a L(NatGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NatGateway/)), or can be assigned to a private
                  IP in any availability domain in the region. Reserved public IPs and ephemeral public IPs
                  assigned to a regional entity have `scope` = `REGION`."
                - "* `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity
                  it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
                  Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`."
            returned: on success
            type: str
            sample: REGION
        time_created:
            description:
                - The date and time the public IP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        public_ip_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pool object created in the current tenancy.
            returned: on success
            type: str
            sample: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "assigned_entity_id": "ocid1.assignedentity.oc1..xxxxxxEXAMPLExxxxxx",
        "assigned_entity_type": "PRIVATE_IP",
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "lifecycle_state": "PROVISIONING",
        "lifetime": "EPHEMERAL",
        "private_ip_id": "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx",
        "scope": "REGION",
        "time_created": "2013-10-20T19:20:30+01:00",
        "public_ip_pool_id": "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreatePublicIpDetails
    from oci.core.models import UpdatePublicIpDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicIpHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PublicIpHelperGen, self).get_possible_entity_types() + [
            "publicip",
            "publicips",
            "corepublicip",
            "corepublicips",
            "publicipresource",
            "publicipsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "public_ip_id"

    def get_module_resource_id(self):
        return self.module.params.get("public_ip_id")

    def get_get_fn(self):
        return self.client.get_public_ip

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_public_ip,
            public_ip_id=self.module.params.get("public_ip_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "scope",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["lifetime", "public_ip_pool_id"]

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
            self.client.list_public_ips, **kwargs
        )

    def get_create_model_class(self):
        return CreatePublicIpDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_public_ip,
            call_fn_args=(),
            call_fn_kwargs=dict(create_public_ip_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePublicIpDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_public_ip,
            call_fn_args=(),
            call_fn_kwargs=dict(
                public_ip_id=self.module.params.get("public_ip_id"),
                update_public_ip_details=update_details,
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
            call_fn=self.client.delete_public_ip,
            call_fn_args=(),
            call_fn_kwargs=dict(public_ip_id=self.module.params.get("public_ip_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PublicIpHelperCustom = get_custom_class("PublicIpHelperCustom")


class ResourceHelper(PublicIpHelperCustom, PublicIpHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            lifetime=dict(type="str", choices=["EPHEMERAL", "RESERVED"]),
            public_ip_pool_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            private_ip_id=dict(type="str"),
            public_ip_id=dict(aliases=["id"], type="str"),
            scope=dict(type="str", choices=["REGION", "AVAILABILITY_DOMAIN"]),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="public_ip",
        service_client_class=VirtualNetworkClient,
        namespace="core",
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
