#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_network_ip_sec_connection
short_description: Manage an IpSecConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IpSecConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new IPSec connection between the specified DRG and CPE. For more information, see
      L(IPSec VPNs,https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPsec.htm).
    - "If you configure at least one tunnel to use static routing, then in the request you must provide
      at least one valid static route (you're allowed a maximum of 10). For example: 10.0.0.0/16.
      If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for
      the static routes. For more information, see the important note in
      L(IPSecConnection,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnection/)."
    - For the purposes of access control, you must provide the OCID of the compartment where you want the
      IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment
      as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to
      use, put the IPSec connection in the same compartment as the DRG. For more information about
      compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "After creating the IPSec connection, you need to configure your on-premises router
      with tunnel-specific information. For tunnel status and the required configuration information, see:"
    - " * L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)
        * L(IPSecConnectionTunnelSharedSecret,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnelSharedSecret/)"
    - For each tunnel, you need the IP address of Oracle's VPN headend and the shared secret
      (that is, the pre-shared key). For more information, see
      L(Configuring Your On-Premises Router for an IPSec VPN,https://docs.cloud.oracle.com/Content/Network/Tasks/configuringCPE.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to contain the IPSec connection.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cpe_id:
        description:
            - The OCID of the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Cpe/) object.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    drg_id:
        description:
            - The OCID of the DRG.
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    cpe_local_identifier:
        description:
            - Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the
              fully qualified domain name (FQDN)). The type of identifier you provide here must correspond
              to the value for `cpeLocalIdentifierType`.
            - If you don't provide a value, the `ipAddress` attribute for the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Cpe/)
              object specified by `cpeId` is used as the `cpeLocalIdentifier`.
            - For information about why you'd provide this value, see
              L(If Your CPE Is Behind a NAT Device,https://docs.cloud.oracle.com/Content/Network/Tasks/overviewIPsec.htm#nat).
            - "Example IP address: `10.0.3.3`"
            - "Example hostname: `cpe.example.com`"
        type: str
    cpe_local_identifier_type:
        description:
            - The type of identifier for your CPE device. The value you provide here must correspond to the value
              for `cpeLocalIdentifier`.
        type: str
        choices:
            - "IP_ADDRESS"
            - "HOSTNAME"
    static_routes:
        description:
            - Static routes to the CPE. A static route's CIDR must not be a
              multicast address or class E address.
            - Used for routing a given IPSec tunnel's traffic only if the tunnel
              is using static routing. If you configure at least one tunnel to use static routing, then
              you must provide at least one valid static route. If you configure both
              tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
              For more information, see the important note in L(IPSecConnection,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/iaas/20160918/IPSecConnection/).
            - "Example: `10.0.1.0/24`"
            - Required for create using I(state=present).
        type: list
    tunnel_configuration:
        description:
            - Information for creating the individual tunnels in the IPSec connection. You can provide a
              maximum of 2 `tunnelConfiguration` objects in the array (one for each of the
              two tunnels).
        type: list
        suboptions:
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                      entering confidential information.
                type: str
                aliases: ["name"]
            routing:
                description:
                    - The type of routing to use for this tunnel (either BGP dynamic routing or static routing).
                type: str
                choices:
                    - "BGP"
                    - "STATIC"
            ike_version:
                description:
                    - Internet Key Exchange protocol version.
                type: str
                choices:
                    - "V1"
                    - "V2"
            shared_secret:
                description:
                    - The shared secret (pre-shared key) to use for the IPSec tunnel. Only numbers, letters, and
                      spaces are allowed. If you don't provide a value,
                      Oracle generates a value for you. You can specify your own shared secret later if
                      you like with L(UpdateIPSecConnectionTunnelSharedSecret,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret).
                type: str
            bgp_session_config:
                description:
                    - Information for establishing a BGP session for the IPSec tunnel. Required if the tunnel uses
                      BGP dynamic routing.
                    - If the tunnel instead uses static routing, you may optionally provide
                      this object and set an IP address for one or both ends of the IPSec tunnel for the purposes
                      of troubleshooting or monitoring the tunnel.
                type: dict
                suboptions:
                    oracle_interface_ip:
                        description:
                            - The IP address for the Oracle end of the inside tunnel interface.
                            - If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)), this IP
                              address
                              is required and used for the tunnel's BGP session.
                            - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                              address to troubleshoot or monitor the tunnel.
                            - The value must be a /30 or /31.
                            - "Example: `10.0.0.4/31`"
                        type: str
                    customer_interface_ip:
                        description:
                            - The IP address for the CPE end of the inside tunnel interface.
                            - If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)), this IP
                              address
                              is required and used for the tunnel's BGP session.
                            - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                              address to troubleshoot or monitor the tunnel.
                            - The value must be a /30 or /31.
                            - "Example: `10.0.0.5/31`"
                        type: str
                    customer_bgp_asn:
                        description:
                            - "If the tunnel's `routing` attribute is set to `BGP`
                              (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)), this ASN
                              is required and used for the tunnel's BGP session. This is the ASN of the network on the
                              CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \\"asplain\\" format."
                            - If the tunnel's `routing` attribute is set to `STATIC`, the `customerBgpAsn` must be null.
                            - "Example: `12345` (2-byte) or `1587232876` (4-byte)"
                        type: str
    ipsc_id:
        description:
            - The OCID of the IPSec connection.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IpSecConnection.
            - Use I(state=present) to create or update an IpSecConnection.
            - Use I(state=absent) to delete an IpSecConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ip_sec_connection
  oci_network_ip_sec_connection:
    display_name: MyIPSecConnection
    cpe_id: ocid1.cpe.oc1.phx.unique_ID
    static_routes:
    - 192.0.2.0/24
    drg_id: ocid1.drg.oc1.phx.unique_ID
    compartment_id: ocid1.compartment.oc1..unique_ID

- name: Update ip_sec_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ip_sec_connection:
    compartment_id: ocid1.compartment.oc1..unique_ID
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyIPSecConnection
    freeform_tags: {'Department': 'Finance'}
    cpe_local_identifier: cpe_local_identifier_example
    cpe_local_identifier_type: IP_ADDRESS
    static_routes: [ "192.0.2.0/24" ]

- name: Update ip_sec_connection
  oci_network_ip_sec_connection:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyIPSecConnection
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete ip_sec_connection
  oci_network_ip_sec_connection:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete ip_sec_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ip_sec_connection:
    compartment_id: ocid1.compartment.oc1..unique_ID
    display_name: MyIPSecConnection
    state: absent

"""

RETURN = """
ip_sec_connection:
    description:
        - Details of the IpSecConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the IPSec connection.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        cpe_id:
            description:
                - The OCID of the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Cpe/) object.
            returned: on success
            type: string
            sample: ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        drg_id:
            description:
                - The OCID of the DRG.
            returned: on success
            type: string
            sample: ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The IPSec connection's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The IPSec connection's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        cpe_local_identifier:
            description:
                - Your identifier for your CPE device. Can be either an IP address or a hostname (specifically,
                  the fully qualified domain name (FQDN)). The type of identifier here must correspond
                  to the value for `cpeLocalIdentifierType`.
                - If you don't provide a value when creating the IPSec connection, the `ipAddress` attribute
                  for the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Cpe/) object specified by `cpeId` is used as the
                  `cpeLocalIdentifier`.
                - For information about why you'd provide this value, see
                  L(If Your CPE Is Behind a NAT Device,https://docs.cloud.oracle.com/Content/Network/Tasks/overviewIPsec.htm#nat).
                - "Example IP address: `10.0.3.3`"
                - "Example hostname: `cpe.example.com`"
            returned: on success
            type: string
            sample: cpe_local_identifier_example
        cpe_local_identifier_type:
            description:
                - The type of identifier for your CPE device. The value here must correspond to the value
                  for `cpeLocalIdentifier`.
            returned: on success
            type: string
            sample: IP_ADDRESS
        static_routes:
            description:
                - Static routes to the CPE. The CIDR must not be a
                  multicast address or class E address.
                - Used for routing a given IPSec tunnel's traffic only if the tunnel
                  is using static routing. If you configure at least one tunnel to use static routing, then
                  you must provide at least one valid static route. If you configure both
                  tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
                - "Example: `10.0.1.0/24`"
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the IPSec connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cpe_id": "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "cpe_local_identifier": "cpe_local_identifier_example",
        "cpe_local_identifier_type": "IP_ADDRESS",
        "static_routes": [],
        "time_created": "2016-08-25T21:10:29.600Z"
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
    from oci.core.models import CreateIPSecConnectionDetails
    from oci.core.models import UpdateIPSecConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "ipsc_id"

    def get_module_resource_id(self):
        return self.module.params.get("ipsc_id")

    def get_get_fn(self):
        return self.client.get_ip_sec_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection,
            ipsc_id=self.module.params.get("ipsc_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["drg_id", "cpe_id"]

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
            self.client.list_ip_sec_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateIPSecConnectionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ip_sec_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ip_sec_connection_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateIPSecConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ip_sec_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ipsc_id=self.module.params.get("ipsc_id"),
                update_ip_sec_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ip_sec_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(ipsc_id=self.module.params.get("ipsc_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


IpSecConnectionHelperCustom = get_custom_class("IpSecConnectionHelperCustom")


class ResourceHelper(IpSecConnectionHelperCustom, IpSecConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cpe_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            drg_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            cpe_local_identifier=dict(type="str"),
            cpe_local_identifier_type=dict(
                type="str", choices=["IP_ADDRESS", "HOSTNAME"]
            ),
            static_routes=dict(type="list"),
            tunnel_configuration=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    routing=dict(type="str", choices=["BGP", "STATIC"]),
                    ike_version=dict(type="str", choices=["V1", "V2"]),
                    shared_secret=dict(type="str"),
                    bgp_session_config=dict(
                        type="dict",
                        options=dict(
                            oracle_interface_ip=dict(type="str"),
                            customer_interface_ip=dict(type="str"),
                            customer_bgp_asn=dict(type="str"),
                        ),
                    ),
                ),
            ),
            ipsc_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ip_sec_connection",
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
