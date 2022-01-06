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
module: oci_network_public_ip_facts
short_description: Fetches details about one or multiple PublicIp resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PublicIp resources in Oracle Cloud Infrastructure
    - Lists the L(PublicIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PublicIp/) objects
      in the specified compartment. You can filter the list by using query parameters.
    - "To list your reserved public IPs:
        * Set `scope` = `REGION`  (required)
        * Leave the `availabilityDomain` parameter empty
        * Set `lifetime` = `RESERVED`"
    - "To list the ephemeral public IPs assigned to a regional entity such as a NAT gateway:
        * Set `scope` = `REGION`  (required)
        * Leave the `availabilityDomain` parameter empty
        * Set `lifetime` = `EPHEMERAL`"
    - "To list the ephemeral public IPs assigned to private IPs:
        * Set `scope` = `AVAILABILITY_DOMAIN` (required)
        * Set the `availabilityDomain` parameter to the desired availability domain (required)
        * Set `lifetime` = `EPHEMERAL`"
    - "**Note:** An ephemeral public IP assigned to a private IP
      is always in the same availability domain and compartment as the private IP."
    - If I(public_ip_id) is specified, the details of a single PublicIp will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    public_ip_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the public IP.
            - Required to get a specific public_ip.
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
            - Required to list multiple public_ips.
        type: str
        choices:
            - "REGION"
            - "AVAILABILITY_DOMAIN"
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple public_ips.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    lifetime:
        description:
            - A filter to return only public IPs that match given lifetime.
        type: str
        choices:
            - "EPHEMERAL"
            - "RESERVED"
    public_ip_pool_id:
        description:
            - A filter to return only resources that belong to the given public IP pool.
        type: str
    private_ip_id:
        description:
            - OCID of the private IP that the public IP is assigned to. Use I(private_ip_id) to retrieve information of a public IP assigned to it.
        type: str
    ip_address:
        description:
            - OCID of the private IP that the public IP is assigned to. Use I(private_ip_id) to retrieve information of a public IP assigned to it.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific public_ip
  oci_network_public_ip_facts:
    # required
    public_ip_id: "ocid1.publicip.oc1..xxxxxxEXAMPLExxxxxx"

- name: List public_ips
  oci_network_public_ip_facts:
    # required
    scope: REGION
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    lifetime: EPHEMERAL
    public_ip_pool_id: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    private_ip_id: private_ip_id_example
    ip_address: ip_address_example

"""

RETURN = """
public_ips:
    description:
        - List of PublicIp resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicIpFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "public_ip_id",
        ]

    def get_required_params_for_list(self):
        return [
            "scope",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_public_ip,
            public_ip_id=self.module.params.get("public_ip_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "lifetime",
            "public_ip_pool_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_public_ips,
            scope=self.module.params.get("scope"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


PublicIpFactsHelperCustom = get_custom_class("PublicIpFactsHelperCustom")


class ResourceFactsHelper(PublicIpFactsHelperCustom, PublicIpFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            public_ip_id=dict(aliases=["id"], type="str"),
            scope=dict(type="str", choices=["REGION", "AVAILABILITY_DOMAIN"]),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            lifetime=dict(type="str", choices=["EPHEMERAL", "RESERVED"]),
            public_ip_pool_id=dict(type="str"),
            private_ip_id=dict(type="str"),
            ip_address=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="public_ip",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(public_ips=result)


if __name__ == "__main__":
    main()
