#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_compute_boot_volume_attachment_facts
short_description: Fetches details about one or multiple BootVolumeAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BootVolumeAttachment resources in Oracle Cloud Infrastructure
    - Lists the boot volume attachments in the specified compartment. You can filter the
      list by specifying an instance OCID, boot volume OCID, or both.
    - If I(boot_volume_attachment_id) is specified, the details of a single BootVolumeAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    boot_volume_attachment_id:
        description:
            - The OCID of the boot volume attachment.
            - Required to get a specific boot_volume_attachment.
        type: str
        aliases: ["id"]
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple boot_volume_attachments.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple boot_volume_attachments.
        type: str
    instance_id:
        description:
            - The OCID of the instance.
        type: str
    boot_volume_id:
        description:
            - The OCID of the boot volume.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific boot_volume_attachment
  oci_compute_boot_volume_attachment_facts:
    # required
    boot_volume_attachment_id: "ocid1.bootvolumeattachment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List boot_volume_attachments
  oci_compute_boot_volume_attachment_facts:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    boot_volume_id: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
boot_volume_attachments:
    description:
        - List of BootVolumeAttachment resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of an instance.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        boot_volume_id:
            description:
                - The OCID of the boot volume.
            returned: on success
            type: str
            sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The OCID of the boot volume attachment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the instance the boot volume is attached to.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the boot volume attachment.
            returned: on success
            type: str
            sample: ATTACHING
        time_created:
            description:
                - The date and time the boot volume was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_pv_encryption_in_transit_enabled:
            description:
                - Whether in-transit encryption for the boot volume's paravirtualized attachment is enabled or not.
            returned: on success
            type: bool
            sample: true
        encryption_in_transit_type:
            description:
                - Refer the top-level definition of encryptionInTransitType.
                  The default value is NONE.
            returned: on success
            type: str
            sample: NONE
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "is_pv_encryption_in_transit_enabled": true,
        "encryption_in_transit_type": "NONE"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "boot_volume_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "availability_domain",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume_attachment,
            boot_volume_attachment_id=self.module.params.get(
                "boot_volume_attachment_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "instance_id",
            "boot_volume_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_boot_volume_attachments,
            availability_domain=self.module.params.get("availability_domain"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BootVolumeAttachmentFactsHelperCustom = get_custom_class(
    "BootVolumeAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    BootVolumeAttachmentFactsHelperCustom, BootVolumeAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            boot_volume_attachment_id=dict(aliases=["id"], type="str"),
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            instance_id=dict(type="str"),
            boot_volume_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="boot_volume_attachment",
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

    module.exit_json(boot_volume_attachments=result)


if __name__ == "__main__":
    main()
