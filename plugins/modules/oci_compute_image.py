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
module: oci_compute_image
short_description: Manage an Image resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Image resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object
      Storage service.
    - When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and
      the OCID of the compartment containing that instance. For more information about images,
      see L(Managing Custom Images,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).
    - When importing an exported image from Object Storage, you specify the source information
      in L(ImageSourceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails).
    - When importing an image based on the namespace, bucket name, and object name,
      use L(ImageSourceViaObjectStorageTupleDetails,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageTupleDetails).
    - When importing an image based on the Object Storage URL, use
      L(ImageSourceViaObjectStorageUriDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageUriDetails).
      See L(Object Storage URLs,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) and L(Using Pre-Authenticated
      Requests,https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
      for constructing URLs for image import/export.
    - For more information about importing exported images, see
      L(Image Import/Export,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm).
    - "You may optionally specify a *display name* for the image, which is simply a friendly name or description.
      It does not have to be unique, and you can change it. See L(UpdateImage,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Image/UpdateImage).
      Avoid entering confidential information."
    - "This resource has the following action operations in the M(oci_image_actions) module: change_compartment, export."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment you want the image to be created in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name for the image. It does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - You cannot use an Oracle-provided image name as a custom image name.
            - "Example: `My Oracle Linux image`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    image_source_details:
        description:
            - ""
        type: dict
        suboptions:
            operating_system:
                description:
                    - ""
                type: str
            operating_system_version:
                description:
                    - ""
                type: str
            source_image_type:
                description:
                    - The format of the image to be imported. Only monolithic
                      images are supported. This attribute is not used for exported Oracle images with the OCI image format.
                type: str
                choices:
                    - "QCOW2"
                    - "VMDK"
            source_type:
                description:
                    - The source type for the image. Use `objectStorageTuple` when specifying the namespace,
                      bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
                type: str
                choices:
                    - "objectStorageTuple"
                    - "objectStorageUri"
                required: true
            bucket_name:
                description:
                    - The Object Storage bucket for the image.
                    - Required when source_type is 'objectStorageTuple'
                type: str
            namespace_name:
                description:
                    - The Object Storage namespace for the image.
                    - Required when source_type is 'objectStorageTuple'
                type: str
            object_name:
                description:
                    - The Object Storage name for the image.
                    - Required when source_type is 'objectStorageTuple'
                type: str
            source_uri:
                description:
                    - The Object Storage URL for the image.
                    - Required when source_type is 'objectStorageUri'
                type: str
    instance_id:
        description:
            - The OCID of the instance you want to use as the basis for the image.
        type: str
    launch_mode:
        description:
            - "Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
              * `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for Oracle-provided images.
              * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
              * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
              * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter."
        type: str
        choices:
            - "NATIVE"
            - "EMULATED"
            - "PARAVIRTUALIZED"
            - "CUSTOM"
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    operating_system:
        description:
            - Operating system
            - "Example: `Oracle Linux`"
            - This parameter is updatable.
        type: str
    operating_system_version:
        description:
            - Operating system version
            - "Example: `7.4`"
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the Image.
            - Use I(state=present) to create or update an Image.
            - Use I(state=absent) to delete an Image.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create image
  oci_compute_image:
    instance_id: "ocid1.instance.oc1.phx.unique_ID"
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: "MyCustomImage"

- name: Create image
  oci_compute_image:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    image_source_details:
      object_name: "image-to-import.oci"
      bucket_name: "MyBucket"
      namespace_name: "MyNamespace"
      source_type: "objectStorageTuple"

- name: Create image
  oci_compute_image:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: "MyImportedImage"
    image_source_details:
      source_uri: "https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/image-to-import.oci"
      source_type: "objectStorageUri"

- name: Update image using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_image:
    display_name: "MyFavoriteImage"

- name: Update image
  oci_compute_image:
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete image
  oci_compute_image:
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete image using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_image:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: MyCustomImage
    state: absent

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
                - You cannot use an Oracle-provided image name as a custom image name.
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
                  * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
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
                          volumes on Oracle-provided images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                          storage volumes on Oracle-provided images."
                    returned: on success
                    type: string
                    sample: ISCSI
                firmware:
                    description:
                        - "Firmware used to boot VM. Select the option that matches your operating system.
                          * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating
                          systems that boot using MBR style bootloaders.
                          * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the
                          default for Oracle-provided images."
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
                          volumes on Oracle-provided images.
                          * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
                          storage volumes on Oracle-provided images."
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
        "time_created": "2016-08-25T21:10:29.600Z"
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
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import CreateImageDetails
    from oci.core.models import UpdateImageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ImageHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ImageHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "image_id"

    def get_module_resource_id(self):
        return self.module.params.get("image_id")

    def get_get_fn(self):
        return self.client.get_image

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image, image_id=self.module.params.get("image_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "operating_system", "operating_system_version"]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_images, **kwargs)

    def get_create_model_class(self):
        return CreateImageDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_image,
            call_fn_args=(),
            call_fn_kwargs=dict(create_image_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateImageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_image,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                update_image_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_image,
            call_fn_args=(),
            call_fn_kwargs=dict(image_id=self.module.params.get("image_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ImageHelperCustom = get_custom_class("ImageHelperCustom")


class ResourceHelper(ImageHelperCustom, ImageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            image_source_details=dict(
                type="dict",
                options=dict(
                    operating_system=dict(type="str"),
                    operating_system_version=dict(type="str"),
                    source_image_type=dict(type="str", choices=["QCOW2", "VMDK"]),
                    source_type=dict(
                        type="str",
                        required=True,
                        choices=["objectStorageTuple", "objectStorageUri"],
                    ),
                    bucket_name=dict(type="str"),
                    namespace_name=dict(type="str"),
                    object_name=dict(type="str"),
                    source_uri=dict(type="str"),
                ),
            ),
            instance_id=dict(type="str"),
            launch_mode=dict(
                type="str", choices=["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"]
            ),
            image_id=dict(aliases=["id"], type="str"),
            operating_system=dict(type="str"),
            operating_system_version=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
