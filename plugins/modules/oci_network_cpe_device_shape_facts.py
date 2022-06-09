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
module: oci_network_cpe_device_shape_facts
short_description: Fetches details about one or multiple CpeDeviceShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CpeDeviceShape resources in Oracle Cloud Infrastructure
    - "Lists the CPE device types that the Networking service provides CPE configuration
      content for (example: Cisco ASA). The content helps a network engineer configure
      the actual CPE device represented by a L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/) object."
    - If you want to generate CPE configuration content for one of the returned CPE device types,
      ensure that the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/) object's `cpeDeviceShapeId` attribute is set
      to the CPE device type's L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) (returned by this operation).
    - "For information about generating CPE configuration content, see these operations:"
    - " * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
        * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
        * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
        us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)"
    - If I(cpe_device_shape_id) is specified, the details of a single CpeDeviceShape will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cpe_device_shape_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE device shape.
            - Required to get a specific cpe_device_shape.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cpe_device_shape
  oci_network_cpe_device_shape_facts:
    # required
    cpe_device_shape_id: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"

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
        cpe_device_shape_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE device shape.
                  This value uniquely identifies the type of CPE device.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"
        parameters:
            description:
                - For certain CPE devices types, the customer can provide answers to
                  questions that are specific to the device type. This attribute contains
                  a list of those questions. The Networking service merges the answers with
                  other information and renders a set of CPE configuration content. To
                  provide the answers, use
                  L(UpdateTunnelCpeDeviceConfig,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig).
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - A string that identifies the question.
                    returned: on success
                    type: str
                    sample: key_example
                display_name:
                    description:
                        - A descriptive label for the question (for example, to display in a form in a graphical interface).
                          Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                explanation:
                    description:
                        - A description or explanation of the question, to help the customer answer accurately.
                    returned: on success
                    type: str
                    sample: explanation_example
        template:
            description:
                - "A template of CPE device configuration information that will be merged with the customer's
                  answers to the questions to render the final CPE device configuration content. Also see:"
                - " * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
                    * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
                    * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)"
                - Returned for get operation
            returned: on success
            type: str
            sample: template_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE device shape.
                  This value uniquely identifies the type of CPE device.
                - Returned for list operation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cpe_device_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                vendor:
                    description:
                        - The vendor that makes the CPE device.
                    returned: on success
                    type: str
                    sample: vendor_example
                platform_software_version:
                    description:
                        - The platform or software version of the CPE device.
                    returned: on success
                    type: str
                    sample: platform_software_version_example
    sample: [{
        "cpe_device_shape_id": "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx",
        "parameters": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "explanation": "explanation_example"
        }],
        "template": "template_example",
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
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cpe_device_shape_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cpe_device_shape,
            cpe_device_shape_id=self.module.params.get("cpe_device_shape_id"),
        )

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
    module_args.update(dict(cpe_device_shape_id=dict(aliases=["id"], type="str"),))

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
