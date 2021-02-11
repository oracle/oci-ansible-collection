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
module: oci_network_private_ip
short_description: Manage a PrivateIp resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PrivateIp resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a secondary private IP for the specified VNIC.
      For more information about secondary private IPs, see
      L(IP Addresses,https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPaddresses.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
              entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    hostname_label:
        description:
            - The hostname for the private IP. Used for DNS. The value
              is the hostname portion of the private IP's fully qualified domain name (FQDN)
              (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
              Must be unique across all VNICs in the subnet and comply with
              L(RFC 952,https://tools.ietf.org/html/rfc952) and
              L(RFC 1123,https://tools.ietf.org/html/rfc1123).
            - For more information, see
              L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
            - "Example: `bminstance-1`"
            - This parameter is updatable.
        type: str
    ip_address:
        description:
            - A private IP address of your choice. Must be an available IP address within
              the subnet's CIDR. If you don't specify a value, Oracle automatically
              assigns a private IP address from the subnet.
            - "Example: `10.0.3.3`"
        type: str
    vnic_id:
        description:
            - The OCID of the VNIC to assign the private IP to. The VNIC and private IP
              must be in the same subnet.
            - This parameter is updatable.
        type: str
    vlan_id:
        description:
            - Use this attribute only with the Oracle Cloud VMware Solution.
            - "The OCID of the VLAN from which the private IP is to be drawn. The IP address,
              *if supplied*, must be valid for the given VLAN. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan)."
        type: str
    private_ip_id:
        description:
            - The OCID of the private IP.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PrivateIp.
            - Use I(state=present) to create or update a PrivateIp.
            - Use I(state=absent) to delete a PrivateIp.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create private_ip
  oci_network_private_ip:

- name: Update private_ip using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_private_ip:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    hostname_label: bminstance-1
    vnic_id: ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx

- name: Update private_ip
  oci_network_private_ip:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    private_ip_id: ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete private_ip
  oci_network_private_ip:
    private_ip_id: ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete private_ip using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_private_ip:
    display_name: display_name_example
    state: absent

"""

RETURN = """
private_ip:
    description:
        - Details of the PrivateIp resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - "The private IP's availability domain. This attribute will be null if this is a *secondary*
                  private IP assigned to a VNIC that is in a *regional* subnet."
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment containing the private IP.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                  entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        hostname_label:
            description:
                - The hostname for the private IP. Used for DNS. The value is the hostname
                  portion of the private IP's fully qualified domain name (FQDN)
                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be unique across all VNICs in the subnet and comply with
                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `bminstance-1`"
            returned: on success
            type: string
            sample: bminstance-1
        id:
            description:
                - The private IP's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        ip_address:
            description:
                - The private IP address of the `privateIp` object. The address is within the CIDR
                  of the VNIC's subnet.
                - However, if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution, the address is from the range specified by the
                  `cidrBlock` attribute for the VLAN. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan).
                - "Example: `10.0.3.3`"
            returned: on success
            type: string
            sample: 10.0.3.3
        is_primary:
            description:
                - Whether this private IP is the primary one on the VNIC. Primary private IPs
                  are unassigned and deleted automatically when the VNIC is terminated.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        vlan_id:
            description:
                - Applicable only if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution. The `vlanId` is the OCID of the VLAN. See
                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan).
            returned: on success
            type: string
            sample: ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx
        subnet_id:
            description:
                - The OCID of the subnet the VNIC is in.
                - However, if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution, the `subnetId` is null.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the private IP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vnic_id:
            description:
                - The OCID of the VNIC the private IP is assigned to. The VNIC and private IP
                  must be in the same subnet.
                  However, if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution, the `vnicId` is null.
            returned: on success
            type: string
            sample: ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "hostname_label": "bminstance-1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "10.0.3.3",
        "is_primary": true,
        "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreatePrivateIpDetails
    from oci.core.models import UpdatePrivateIpDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateIpHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "private_ip_id"

    def get_module_resource_id(self):
        return self.module.params.get("private_ip_id")

    def get_get_fn(self):
        return self.client.get_private_ip

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_ip,
            private_ip_id=self.module.params.get("private_ip_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["ip_address", "vlan_id"]
            if self._use_name_as_identifier()
            else ["ip_address", "vnic_id", "vlan_id"]
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
            self.client.list_private_ips, **kwargs
        )

    def get_create_model_class(self):
        return CreatePrivateIpDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_private_ip,
            call_fn_args=(),
            call_fn_kwargs=dict(create_private_ip_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePrivateIpDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_private_ip,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_ip_id=self.module.params.get("private_ip_id"),
                update_private_ip_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_private_ip,
            call_fn_args=(),
            call_fn_kwargs=dict(private_ip_id=self.module.params.get("private_ip_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PrivateIpHelperCustom = get_custom_class("PrivateIpHelperCustom")


class ResourceHelper(PrivateIpHelperCustom, PrivateIpHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            hostname_label=dict(type="str"),
            ip_address=dict(type="str"),
            vnic_id=dict(type="str"),
            vlan_id=dict(type="str"),
            private_ip_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_ip",
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
