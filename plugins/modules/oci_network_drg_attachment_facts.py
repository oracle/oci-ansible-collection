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
module: oci_network_drg_attachment_facts
short_description: Fetches details about one or multiple DrgAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrgAttachment resources in Oracle Cloud Infrastructure
    - Lists the `DrgAttachment` objects for the specified compartment. You can filter the
      results by VCN or DRG.
    - If I(drg_attachment_id) is specified, the details of a single DrgAttachment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    drg_attachment_id:
        description:
            - The OCID of the DRG attachment.
            - Required to get a specific drg_attachment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple drg_attachments.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    drg_id:
        description:
            - The OCID of the DRG.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List drg_attachments
  oci_network_drg_attachment_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific drg_attachment
  oci_network_drg_attachment_facts:
    drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
drg_attachments:
    description:
        - List of DrgAttachment resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the DRG attachment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The DRG attachment's Oracle ID (OCID).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The DRG attachment's current state.
            returned: on success
            type: string
            sample: ATTACHING
        time_created:
            description:
                - The date and time the DRG attachment was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        route_table_id:
            description:
                - The OCID of the route table the DRG attachment is using.
                - "For information about why you would associate a route table with a DRG attachment, see:"
                - " * L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)
                    * L(Transit Routing: Private Access to Oracle
                    Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)"
            returned: on success
            type: string
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: string
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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


class DrgAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "drg_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_attachment,
            drg_attachment_id=self.module.params.get("drg_attachment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
            "drg_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_drg_attachments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DrgAttachmentFactsHelperCustom = get_custom_class("DrgAttachmentFactsHelperCustom")


class ResourceFactsHelper(DrgAttachmentFactsHelperCustom, DrgAttachmentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            drg_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            drg_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_attachment",
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

    module.exit_json(drg_attachments=result)


if __name__ == "__main__":
    main()
