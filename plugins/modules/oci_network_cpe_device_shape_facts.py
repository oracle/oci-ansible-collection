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
module: oci_network_cpe_device_shape_facts
short_description: Fetches details about one or multiple CpeDeviceShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CpeDeviceShape resources in Oracle Cloud Infrastructure
    - "Lists the CPE device types that the Networking service provides CPE configuration
      content for (example: Cisco ASA). The content helps a network engineer configure
      the actual CPE device represented by a L(Cpe,https://docs.cloud.oracle.com/#/en/iaas/20160918/Cpe/) object."
    - If you want to generate CPE configuration content for one of the returned CPE device types,
      ensure that the L(Cpe,https://docs.cloud.oracle.com/#/en/iaas/20160918/Cpe/) object's `cpeDeviceShapeId` attribute is set
      to the CPE device type's OCID (returned by this operation).
    - "For information about generating CPE configuration content, see these operations:"
    - " * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/#/en/iaas/20160918/Cpe/GetCpeDeviceConfigContent)
        * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/#/en/iaas/20160918/IPSecConnection/GetIpsecCpeDeviceConfigContent)
        * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/#/en/iaas/20160918/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)"
version_added: "2.9"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List cpe_device_shapes
  oci_network_cpe_device_shape_facts:

"""

RETURN = """
cpe_device_shapes:
    description:
        - List of CpeDeviceShape resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the CPE device shape.
                  This value uniquely identifies the type of CPE device.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        cpe_device_info:
            description:
                - Basic information about this particular CPE device type.
            returned: on success
            type: complex
            contains:
                vendor:
                    description:
                        - The vendor that makes the CPE device.
                    returned: on success
                    type: string
                    sample: vendor_example
                platform_software_version:
                    description:
                        - The platform or software version of the CPE device.
                    returned: on success
                    type: string
                    sample: platform_software_version_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cpe_device_info": {
            "vendor": "vendor_example",
            "platform_software_version": "platform_software_version_example"
        }
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


class CpeDeviceShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cpe_device_shapes, **optional_kwargs
        )


CpeDeviceShapeFactsHelperCustom = get_custom_class("CpeDeviceShapeFactsHelperCustom")


class ResourceFactsHelper(
    CpeDeviceShapeFactsHelperCustom, CpeDeviceShapeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict())

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cpe_device_shape",
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

    module.exit_json(cpe_device_shapes=result)


if __name__ == "__main__":
    main()
