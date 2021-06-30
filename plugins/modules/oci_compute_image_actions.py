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
module: oci_compute_image_actions
short_description: Perform actions on an Image resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Image resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an image into a different compartment within the same tenancy. For information about moving
      resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=export), exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL,
      or the namespace, bucket name, and object name when specifying the location to export to.
      For more information about exporting images, see L(Image Import/Export,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm).
      To perform an image export, you need write access to the Object Storage bucket for the image,
      see L(Let Users Write Objects to Object Storage Buckets,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#Let4).
      See L(Object Storage URLs,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) and L(Using Pre-Authenticated
      Requests,https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
      for constructing URLs for image import/export.
version_added: "2.9"
author: Oracle (@oracle)
options:
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the image to.
            - Required for I(action=change_compartment).
        type: str
    destination_type:
        description:
            - The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
              Use `objectStorageUri` when specifying the Object Storage URL.
            - Required for I(action=export).
        type: str
        choices:
            - "objectStorageUri"
            - "objectStorageTuple"
    export_format:
        description:
            - The format to export the image to. The default value is `OCI`.
            - "The following image formats are available:"
            - "- `OCI` - Oracle Cloud Infrastructure file with a QCOW2 image and Oracle Cloud Infrastructure metadata (.oci).
              Use this format to export a custom image that you want to import into other tenancies or regions.
              - `QCOW2` - QEMU Copy On Write (.qcow2)
              - `VDI` - Virtual Disk Image (.vdi) for Oracle VM VirtualBox
              - `VHD` - Virtual Hard Disk (.vhd) for Hyper-V
              - `VMDK` - Virtual Machine Disk (.vmdk)"
            - Applicable only for I(action=export).
        type: str
        choices:
            - "QCOW2"
            - "VMDK"
            - "OCI"
            - "VHD"
            - "VDI"
    destination_uri:
        description:
            - The Object Storage URL to export the image to. See L(Object
              Storage URLs,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs)
              and L(Using Pre-Authenticated Requests,https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
              for constructing URLs for image import/export.
            - Applicable only for I(action=export).
            - Required when destination_type is 'objectStorageUri'
        type: str
    bucket_name:
        description:
            - The Object Storage bucket to export the image to.
            - Applicable only for I(action=export).
            - Required when destination_type is 'objectStorageTuple'
        type: str
    namespace_name:
        description:
            - The Object Storage namespace to export the image to.
            - Applicable only for I(action=export).
            - Required when destination_type is 'objectStorageTuple'
        type: str
    object_name:
        description:
            - The Object Storage object name for the exported image.
            - Applicable only for I(action=export).
            - Required when destination_type is 'objectStorageTuple'
        type: str
    action:
        description:
            - The action to perform on the Image.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "export"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on image
  oci_compute_image_actions:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

- name: Perform action export on image
  oci_compute_image_actions:
    object_name: "my-exported-image.oci"
    bucket_name: "MyBucket"
    namespace_name: "MyNamespace"
    destination_type: "objectStorageTuple"
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    action: "export"

- name: Perform action export on image
  oci_compute_image_actions:
    object_name: "my-exported-image.vmdk"
    bucket_name: "MyBucket"
    namespace_name: "MyNamespace"
    destination_type: "objectStorageTuple"
    export_format: "VMDK"
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    action: "export"

"""

RETURN = """
image:
    description:
        - Details of the Image resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        base_image_id:
            description:
                - The OCID of the image originally used to launch the instance.
            returned: on success
            type: string
            sample: "ocid1.baseimage.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the instance you want to use as the basis for the image.
            returned: on success
            type: string
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
            type: string
            sample: My custom Oracle Linux image
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
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        launch_mode:
            description:
                - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
                  * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
                  * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
                  * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
            returned: on success
            type: string
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
                    type: string
                    sample: ISCSI
                firmware:
                    description:
                        - "Firmware used to boot VM. Select the option that matches your operating system.
                          * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                          systems that boot using MBR style bootloaders.
                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                          default for platform images."
                    returned: on success
                    type: string
                    sample: BIOS
                network_type:
                    description:
                        - "Emulation type for the physical network interface card (NIC).
                          * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
                          * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
                          when you launch an instance using hardware-assisted (SR-IOV) networking.
                          * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers."
                    returned: on success
                    type: string
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
                    type: string
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
            type: string
            sample: PROVISIONING
        operating_system:
            description:
                - The image's operating system.
                - "Example: `Oracle Linux`"
            returned: on success
            type: string
            sample: Oracle Linux
        operating_system_version:
            description:
                - The image's operating system version.
                - "Example: `7.2`"
            returned: on success
            type: string
            sample: 7.2
        agent_features:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_monitoring_supported:
                    description:
                        - Whether Oracle Cloud Agent can gather performance metrics and monitor the instance.
                    returned: on success
                    type: bool
                    sample: true
                is_management_supported:
                    description:
                        - Whether Oracle Cloud Agent can run all the available management plugins.
                    returned: on success
                    type: bool
                    sample: true
        listing_type:
            description:
                - "The listing type of the image. The default value is \\"NONE\\"."
            returned: on success
            type: string
            sample: COMMUNITY
        size_in_mbs:
            description:
                - The boot volume size for an instance launched from this image (1 MB = 1,048,576 bytes).
                  Note this is not the same as the size of the image when it was exported or the actual size of the image.
                - "Example: `47694`"
            returned: on success
            type: int
            sample: 47694
        billable_size_in_gbs:
            description:
                - The size of the internal storage for this image that is subject to billing (1 GB = 1,073,741,824 bytes).
                - "Example: `100`"
            returned: on success
            type: int
            sample: 100
        time_created:
            description:
                - The date and time the image was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "base_image_id": "ocid1.baseimage.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "create_image_allowed": true,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "My custom Oracle Linux image",
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
        "operating_system": "Oracle Linux",
        "operating_system_version": "7.2",
        "agent_features": {
            "is_monitoring_supported": true,
            "is_management_supported": true
        },
        "listing_type": "COMMUNITY",
        "size_in_mbs": 47694,
        "billable_size_in_gbs": 100,
        "time_created": "2016-08-25T21:10:29.600Z"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import ChangeImageCompartmentDetails
    from oci.core.models import ExportImageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ImageActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        export
    """

    def __init__(self, *args, **kwargs):
        super(ImageActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "image_id"

    def get_module_resource_id(self):
        return self.module.params.get("image_id")

    def get_get_fn(self):
        return self.client.get_image

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image, image_id=self.module.params.get("image_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeImageCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_image_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                change_image_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def export(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExportImageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_image,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                export_image_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ImageActionsHelperCustom = get_custom_class("ImageActionsHelperCustom")


class ResourceHelper(ImageActionsHelperCustom, ImageActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            image_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            destination_type=dict(
                type="str", choices=["objectStorageUri", "objectStorageTuple"]
            ),
            export_format=dict(
                type="str", choices=["QCOW2", "VMDK", "OCI", "VHD", "VDI"]
            ),
            destination_uri=dict(type="str"),
            bucket_name=dict(type="str"),
            namespace_name=dict(type="str"),
            object_name=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["change_compartment", "export"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="image",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
