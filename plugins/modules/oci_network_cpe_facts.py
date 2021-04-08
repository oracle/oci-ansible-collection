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
module: oci_network_cpe_facts
short_description: Fetches details about one or multiple Cpe resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Cpe resources in Oracle Cloud Infrastructure
    - Lists the customer-premises equipment objects (CPEs) in the specified compartment.
    - If I(cpe_id) is specified, the details of a single Cpe will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    cpe_id:
        description:
            - The OCID of the CPE.
            - Required to get a specific cpe.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple cpes.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List cpes
  oci_network_cpe_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific cpe
  oci_network_cpe_facts:
    cpe_id: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cpes:
    description:
        - List of Cpe resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the CPE.
            returned: on success
            type: string
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
            type: string
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
                - The CPE's Oracle ID (OCID).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The public IP address of the on-premises router.
            returned: on success
            type: string
            sample: ip_address_example
        cpe_device_shape_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE's device type.
                  The Networking service maintains a general list of CPE device types (for example,
                  Cisco ASA). For each type, Oracle provides CPE configuration content that can help
                  a network engineer configure the CPE. The OCID uniquely identifies the type of
                  device. To get the OCIDs for the device types on the list, see
                  L(ListCpeDeviceShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CpeDeviceShapeSummary/ListCpeDeviceShapes).
                - "For information about how to generate CPE configuration content for a
                  CPE device type, see:"
                - " * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
                    * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
                    * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
                    * L(GetTunnelCpeDeviceConfig,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfig)"
            returned: on success
            type: string
            sample: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the CPE was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "cpe_device_shape_id": "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z"
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


class CpeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cpe_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cpe, cpe_id=self.module.params.get("cpe_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cpes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CpeFactsHelperCustom = get_custom_class("CpeFactsHelperCustom")


class ResourceFactsHelper(CpeFactsHelperCustom, CpeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cpe_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cpe",
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

    module.exit_json(cpes=result)


if __name__ == "__main__":
    main()
