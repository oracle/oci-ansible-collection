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
module: oci_compute_vnic_attachment_facts
short_description: Fetches details about one or multiple VnicAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VnicAttachment resources in Oracle Cloud Infrastructure
    - Lists the VNIC attachments in the specified compartment. A VNIC attachment
      resides in the same compartment as the attached instance. The list can be
      filtered by instance, VNIC, or availability domain.
    - If I(vnic_attachment_id) is specified, the details of a single VnicAttachment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    vnic_attachment_id:
        description:
            - The OCID of the VNIC attachment.
            - Required to get a specific vnic_attachment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple vnic_attachments.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    instance_id:
        description:
            - The OCID of the instance.
        type: str
    vnic_id:
        description:
            - The OCID of the VNIC.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List vnic_attachments
  oci_compute_vnic_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific vnic_attachment
  oci_compute_vnic_attachment_facts:
    vnic_attachment_id: ocid1.vnicattachment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
vnic_attachments:
    description:
        - List of VnicAttachment resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the instance.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment the VNIC attachment is in, which is the same
                  compartment the instance is in.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        id:
            description:
                - The OCID of the VNIC attachment.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        instance_id:
            description:
                - The OCID of the instance.
            returned: on success
            type: string
            sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the VNIC attachment.
            returned: on success
            type: string
            sample: ATTACHING
        nic_index:
            description:
                - Which physical network interface card (NIC) the VNIC uses.
                  Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                  you add a secondary VNIC to one of these instances, you can specify which NIC
                  the VNIC will use. For more information, see
                  L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/Content/Network/Tasks/managingVNICs.htm).
            returned: on success
            type: int
            sample: 56
        subnet_id:
            description:
                - The OCID of the subnet to create the VNIC in.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        vlan_id:
            description:
                - The OCID of the VLAN to create the VNIC in. Creating the VNIC in a VLAN (instead
                  of a subnet) is possible only if you are an Oracle Cloud VMware Solution customer.
                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan).
                - An error is returned if the instance already has a VNIC attached to it from this VLAN.
            returned: on success
            type: string
            sample: ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the VNIC attachment was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vlan_tag:
            description:
                - The Oracle-assigned VLAN tag of the attached VNIC. Available after the
                  attachment process is complete.
                - However, if the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution,
                  the `vlanTag` value is instead the value of the `vlanTag` attribute for the VLAN.
                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan).
                - "Example: `0`"
            returned: on success
            type: int
            sample: 0
        vnic_id:
            description:
                - The OCID of the VNIC. Available after the attachment process is complete.
            returned: on success
            type: string
            sample: ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "nic_index": 56,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vlan_tag": 0,
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VnicAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vnic_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vnic_attachment,
            vnic_attachment_id=self.module.params.get("vnic_attachment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "instance_id",
            "vnic_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vnic_attachments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VnicAttachmentFactsHelperCustom = get_custom_class("VnicAttachmentFactsHelperCustom")


class ResourceFactsHelper(
    VnicAttachmentFactsHelperCustom, VnicAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vnic_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            instance_id=dict(type="str"),
            vnic_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vnic_attachment",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vnic_attachments=result)


if __name__ == "__main__":
    main()
