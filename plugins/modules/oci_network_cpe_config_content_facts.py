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
module: oci_network_cpe_config_content_facts
short_description: Fetches details about a CpeConfigContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CpeConfigContent resource in Oracle Cloud Infrastructure
    - Renders a set of CPE configuration content that can help a network engineer configure the actual
      CPE device (for example, a hardware router) represented by the specified L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/)
      object.
    - The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
      L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/) must have the CPE's device type specified by the `cpeDeviceShapeId`
      attribute. The content optionally includes answers that the customer provides (see
      L(UpdateTunnelCpeDeviceConfig,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig)),
      merged with a template of other information specific to the CPE device type.
    - "The operation returns configuration information for *all* of the
      L(IPSecConnection,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnection/) objects that use the specified CPE.
      Here are similar operations:"
    - " * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
        returns CPE configuration content for all IPSec tunnels in a single IPSec connection.
        * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
        returns CPE configuration content for a specific IPSec tunnel in an IPSec connection."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cpe_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the CPE.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cpe_config_content
  oci_network_cpe_config_content_facts:
    # required
    cpe_id: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cpe_config_content:
    description:
        - CpeConfigContent resource
    returned: on success
    type: str
    sample: "sample"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
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


class CpeConfigContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cpe_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cpe_device_config_content,
            cpe_id=self.module.params.get("cpe_id"),
        )

    def get(self):
        response_data = self.get_resource().data
        return to_text(response_data)


CpeConfigContentFactsHelperCustom = get_custom_class(
    "CpeConfigContentFactsHelperCustom"
)


class ResourceFactsHelper(
    CpeConfigContentFactsHelperCustom, CpeConfigContentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(cpe_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cpe_config_content",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(cpe_config_content=result)


if __name__ == "__main__":
    main()
