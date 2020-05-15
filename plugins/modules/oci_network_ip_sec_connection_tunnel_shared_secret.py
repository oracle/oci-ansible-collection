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
module: oci_network_ip_sec_connection_tunnel_shared_secret
short_description: Manage an IpSecConnectionTunnelSharedSecret resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an IpSecConnectionTunnelSharedSecret resource in Oracle Cloud Infrastructure
version_added: "2.5"
options:
    ipsc_id:
        description:
            - The OCID of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the tunnel.
        type: str
        aliases: ["id"]
        required: true
    shared_secret:
        description:
            - The shared secret (pre-shared key) to use for the tunnel. Only numbers, letters, and spaces
              are allowed.
            - "Example: `EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o`"
        type: str
    state:
        description:
            - The state of the IpSecConnectionTunnelSharedSecret.
            - Use I(state=present) to update an existing an IpSecConnectionTunnelSharedSecret.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update ip_sec_connection_tunnel_shared_secret
  oci_network_ip_sec_connection_tunnel_shared_secret:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx
    tunnel_id: ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
ip_sec_connection_tunnel_shared_secret:
    description:
        - Details of the IpSecConnectionTunnelSharedSecret resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        shared_secret:
            description:
                - The tunnel's shared secret (pre-shared key).
                - "Example: `EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o`"
            returned: on success
            type: string
            sample: EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o
    sample: {
        "shared_secret": "EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o"
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
    from oci.core.models import UpdateIPSecConnectionTunnelSharedSecretDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionTunnelSharedSecretHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "tunnel_id"

    def get_module_resource_id(self):
        return self.module.params.get("tunnel_id")

    def get_get_fn(self):
        return self.client.get_ip_sec_connection_tunnel_shared_secret

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_tunnel_shared_secret,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )

    def get_update_model_class(self):
        return UpdateIPSecConnectionTunnelSharedSecretDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ip_sec_connection_tunnel_shared_secret,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ipsc_id=self.module.params.get("ipsc_id"),
                tunnel_id=self.module.params.get("tunnel_id"),
                update_ip_sec_connection_tunnel_shared_secret_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )


IpSecConnectionTunnelSharedSecretHelperCustom = get_custom_class(
    "IpSecConnectionTunnelSharedSecretHelperCustom"
)


class ResourceHelper(
    IpSecConnectionTunnelSharedSecretHelperCustom,
    IpSecConnectionTunnelSharedSecretHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(aliases=["id"], type="str", required=True),
            shared_secret=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ip_sec_connection_tunnel_shared_secret",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
