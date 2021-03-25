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
module: oci_network_ip_sec_connection_tunnel_cpe_device_config
short_description: Manage an IpSecConnectionTunnelCpeDeviceConfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an IpSecConnectionTunnelCpeDeviceConfig resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The OCID of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.
        type: str
        aliases: ["id"]
        required: true
    tunnel_cpe_device_config:
        description:
            - The set of configuration answers for a CPE device.
            - This parameter is updatable.
        type: list
        suboptions:
            key:
                description:
                    - A string that identifies the question to be answered. See the `key` attribute in
                      L(CpeDeviceConfigQuestion,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/datatypes/CpeDeviceConfigQuestion).
                    - This parameter is updatable.
                type: str
            value:
                description:
                    - The answer to the question.
                    - This parameter is updatable.
                type: str
    state:
        description:
            - The state of the IpSecConnectionTunnelCpeDeviceConfig.
            - Use I(state=present) to update an existing an IpSecConnectionTunnelCpeDeviceConfig.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update ip_sec_connection_tunnel_cpe_device_config
  oci_network_ip_sec_connection_tunnel_cpe_device_config:
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
    tunnel_id: "ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ip_sec_connection_tunnel_cpe_device_config:
    description:
        - Details of the IpSecConnectionTunnelCpeDeviceConfig resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        tunnel_cpe_device_config_parameter:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - A string that identifies the question to be answered. See the `key` attribute in
                          L(CpeDeviceConfigQuestion,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/datatypes/CpeDeviceConfigQuestion).
                    returned: on success
                    type: string
                    sample: key_example
                value:
                    description:
                        - The answer to the question.
                    returned: on success
                    type: string
                    sample: value_example
    sample: {
        "tunnel_cpe_device_config_parameter": [{
            "key": "key_example",
            "value": "value_example"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import UpdateTunnelCpeDeviceConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionTunnelCpeDeviceConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "tunnel_id"

    def get_module_resource_id(self):
        return self.module.params.get("tunnel_id")

    def get_get_fn(self):
        return self.client.get_tunnel_cpe_device_config

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tunnel_cpe_device_config,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )

    def get_update_model_class(self):
        return UpdateTunnelCpeDeviceConfigDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tunnel_cpe_device_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ipsc_id=self.module.params.get("ipsc_id"),
                tunnel_id=self.module.params.get("tunnel_id"),
                update_tunnel_cpe_device_config_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


IpSecConnectionTunnelCpeDeviceConfigHelperCustom = get_custom_class(
    "IpSecConnectionTunnelCpeDeviceConfigHelperCustom"
)


class ResourceHelper(
    IpSecConnectionTunnelCpeDeviceConfigHelperCustom,
    IpSecConnectionTunnelCpeDeviceConfigHelperGen,
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
            tunnel_cpe_device_config=dict(
                type="list",
                elements="dict",
                options=dict(key=dict(type="str"), value=dict(type="str")),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ip_sec_connection_tunnel_cpe_device_config",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
