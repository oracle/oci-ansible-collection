#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_compute_image_facts
short_description: Fetches details about one or multiple Image resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Image resources in Oracle Cloud Infrastructure
    - Lists a subset of images available in the specified compartment, including
      L(platform images,https://docs.cloud.oracle.com/iaas/Content/Compute/References/images.htm) and
      L(custom images,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).
      The list of platform images includes the three most recently published versions
      of each major distribution. The list does not support filtering based on image tags.
    - The list of images returned is ordered to first show the recent platform images,
      then all of the custom images.
    - "**Caution:** Platform images are refreshed regularly. When new images are released, older versions are replaced.
      The image OCIDs remain available, but when the platform image is replaced, the image OCIDs are no longer returned as part of the platform image list."
    - If I(image_id) is specified, the details of a single Image will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
            - Required to get a specific image.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple images.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    operating_system:
        description:
            - The image's operating system.
            - "Example: `Oracle Linux`"
        type: str
    operating_system_version:
        description:
            - The image's operating system version.
            - "Example: `7.2`"
        type: str
    shape:
        description:
            - Shape name.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state
              value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "IMPORTING"
            - "AVAILABLE"
            - "EXPORTING"
            - "DISABLED"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific image
  oci_compute_image_facts:
    # required
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

- name: List images
  oci_compute_image_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    operating_system: operating_system_example
    operating_system_version: operating_system_version_example
    shape: shape_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING

"""

RETURN = """
images:
    description:
        - List of Image resources
    returned: on success
    type: complex
    contains:
        base_image_id:
            description:
                - The OCID of the image originally used to launch the instance.
            returned: on success
            type: str
            sample: "ocid1.baseimage.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the instance you want to use as the basis for the image.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        create_image_allowed:
            description:
                - Whether instances launched with this image can be used to create new images.
                  For example, you cannot create an image of an Oracle Database instance.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
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
                - A user-friendly name for the image. It does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - You cannot use a platform image name as a custom image name.
                - "Example: `My custom Oracle Linux image`"
            returned: on success
            type: str
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
                - The OCID of the image.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        launch_mode:
            description:
                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
            returned: on success
            type: str
            sample: NATIVE
        launch_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                boot_volume_type:
                    description:
                        - "Emulation type for the boot volume.
                          * `ISCSI` - ISCSI attached block storage device.
                          * `SCSI` - Emulated SCSI disk.
                          * `IDE` - Emulated IDE disk.
                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                          volumes on platform images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                          storage volumes on platform images."
                    returned: on success
                    type: str
                    sample: ISCSI
                firmware:
                    description:
                        - "Firmware used to boot VM. Select the option that matches your operating system.
                          * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                          systems that boot using MBR style bootloaders.
                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                          default for platform images."
                    returned: on success
                    type: str
                    sample: BIOS
                network_type:
                    description:
                        - "Emulation type for the physical network interface card (NIC).
                          * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                    returned: on success
                    type: str
                    sample: E1000
                remote_data_volume_type:
                    description:
                        - "Emulation type for volume.
                          * `ISCSI` - ISCSI attached block storage device.
                          * `SCSI` - Emulated SCSI disk.
                          * `IDE` - Emulated IDE disk.
                          * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data
                          volumes on platform images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                          storage volumes on platform images."
                    returned: on success
                    type: str
                    sample: ISCSI
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
                          L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/datatypes/LaunchInstanceDetails).
                    returned: on success
                    type: bool
                    sample: true
                is_consistent_volume_naming_enabled:
                    description:
                        - Whether to enable consistent volume naming feature. Defaults to false.
                    returned: on success
                    type: bool
                    sample: true
        lifecycle_state:
            description:
                - ""
            returned: on success
            type: str
            sample: PROVISIONING
        operating_system:
            description:
                - The image's operating system.
                - "Example: `Oracle Linux`"
            returned: on success
            type: str
            sample: operating_system_example
        operating_system_version:
            description:
                - The image's operating system version.
                - "Example: `7.2`"
            returned: on success
            type: str
            sample: operating_system_version_example
        agent_features:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_monitoring_supported:
                    description:
                        - This attribute is not used.
                    returned: on success
                    type: bool
                    sample: true
                is_management_supported:
                    description:
                        - This attribute is not used.
                    returned: on success
                    type: bool
                    sample: true
        listing_type:
            description:
                - "The listing type of the image. The default value is \\"NONE\\"."
            returned: on success
            type: str
            sample: COMMUNITY
        size_in_mbs:
            description:
                - The boot volume size for an instance launched from this image (1 MB = 1,048,576 bytes).
                  Note this is not the same as the size of the image when it was exported or the actual size of the image.
                - "Example: `47694`"
            returned: on success
            type: int
            sample: 56
        billable_size_in_gbs:
            description:
                - The size of the internal storage for this image that is subject to billing (1 GB = 1,073,741,824 bytes).
                - "Example: `100`"
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the image was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "base_image_id": "ocid1.baseimage.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "create_image_allowed": true,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "launch_mode": "NATIVE",
        "launch_options": {
            "boot_volume_type": "ISCSI",
            "firmware": "BIOS",
            "network_type": "E1000",
            "remote_data_volume_type": "ISCSI",
            "is_pv_encryption_in_transit_enabled": true,
            "is_consistent_volume_naming_enabled": true
        },
        "lifecycle_state": "PROVISIONING",
        "operating_system": "operating_system_example",
        "operating_system_version": "operating_system_version_example",
        "agent_features": {
            "is_monitoring_supported": true,
            "is_management_supported": true
        },
        "listing_type": "COMMUNITY",
        "size_in_mbs": 56,
        "billable_size_in_gbs": 56,
        "time_created": "2013-10-20T19:20:30+01:00"
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


class ImageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "image_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image, image_id=self.module.params.get("image_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "operating_system",
            "operating_system_version",
            "shape",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_images,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ImageFactsHelperCustom = get_custom_class("ImageFactsHelperCustom")


class ResourceFactsHelper(ImageFactsHelperCustom, ImageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            image_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            operating_system=dict(type="str"),
            operating_system_version=dict(type="str"),
            shape=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "IMPORTING",
                    "AVAILABLE",
                    "EXPORTING",
                    "DISABLED",
                    "DELETED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="image",
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

    module.exit_json(images=result)


if __name__ == "__main__":
    main()
