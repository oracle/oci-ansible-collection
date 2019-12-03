#!/usr/bin/python
# Copyright (c) 2017, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_image
short_description: Create, import, update and delete OCI Compute images
description:
    - This module allows the user to create an image, import an exported image, update an image and delete OCI Compute
      Images.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the instance that needs to be used as the basis for the
                     image. Required when an image needs to be created with I(state=present).
    display_name:
        description: A user-friendly name to be associated with the image. This does not have to be unique, and can be
                     changed later. An Oracle-provided image name cannot be used as the name for a custom image's name.
        aliases: ['name']
    instance_id:
        description: The OCID of the instance that needs to be used as the basis for the image. Either C(instance_id)
                     or C(image_source_details) needs to be specified while creating an image using I(state=present).
    image_id:
        description: The OCID of the image. Required while updating an image using I(state=present), and deleting an
                     existing image using I(state=absent).
        aliases: [ 'id' ]
    image_source_details:
        description: Details for creating an image through import. Either C(instance_id) or C(image_source_details)
                     needs to be specified while creating an image using I(state=present).
        suboptions:
            source_type:
                description: The source type for the image. Use 'objectStorageTuple' to get the image from an object in
                             Object Storage and specify C(namespace), C(bucket), and C(object). Use
                             'objectStorageUri' when specifying an Object Storage URL to get the image, and specify
                             C(source_uri).
                aliases: [ 'destination_type' ]
            source_uri:
                description: The Object Storage URL for the image. See Object Storage URLs at
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs)
                             and pre-authenticated requests
                             at U(https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth)
                             for constructing URLs for image import/export.
                             Required when creating an image using I(state=present) and the
                             I(source_type=objectStorageUri) under C(image_source_details).
            bucket_name:
                description: The Object Storage bucket for the image. Required when creating an image using
                             I(state=present) and the I(source_type=objectStorageTuple) under C(image_source_details).
                aliases: [ 'bucket' ]
            namespace_name:
                 description: The Object Storage namespace for the image. Required when creating an image using
                             I(state=present) and the I(source_type=objectStorageTuple) under C(image_source_details).
                 aliases: [ 'namespace' ]
            object_name:
                description: The Object Storage name for the image. Required when creating an image using
                             I(state=present) and the I(source_type=objectStorageTuple) under C(image_source_details).
                aliases: [ 'object' ]
            source_image_type:
                description: The format of source image type to be imported.
                             Available when creating an image using I(state=present) under C(image_source_details).
                choices: ['QCOW2', 'VMDK']
    launch_mode:
        description: The the launch mode Specifies the configuration mode for launching virtual machine (VM) instances.
                     The default value for Oracle-provided images is 'NATIVE', it launches with iSCSI boot and VFIO devices.
        default: "NATIVE"
        choices: ['NATIVE', 'EMULATED', 'PARAVIRTUALIZED', 'CUSTOM']
    state:
        description: The state of the image that must be asserted to. When I(state=present), and the
                     image doesn't exist, the image is created with the specified details. When I(state=absent),
                     the image is deleted.
                     Creation of an image may take longer than the default value of I(wait_timeout). So if I(wait=true),
                     during creation of an image, it is recommended to set a longer timeout value of I(wait_timeout).
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a new image from a specified instance
  oci_image:
    name: my_custom_image_1
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    instance_id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....dszaitd3da"

- name: Create a new image by importing an exported image, where the image is placed in a bucket in Object Storage
        Service
  oci_image:
        name: my_custom_image_2
        compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
        image_source_details:
            source_type: "objectStorageTuple"
            bucket: "my_bucket"
            namespace: "my_namespace"
            object: "image-to-import.qcow2"
            source_image_type: "QCOW2"

- name: Create a new image by importing an exported image, where the image is available through an Object Storage
        Service URL
  oci_image:
        name: my_custom_image_3
        compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
        image_source_details:
            source_type: "objectStorageUri"
            source_uri: "https://objectstorage.us-phoenix-1.oraclecloud.com/n/my_namespace/b/my_bucket/o/image-to-impor
                        t.qcow2"
            source_image_type: "QCOW2"

- name: Update an image's display name
  oci_image:
        id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
        name: my_new_image_name

- name: Delete an image
  oci_image:
        id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
        state: "absent"
"""

RETURN = """
oci_image:
    description: Details of the image
    returned: On success
    type: dict
    sample: { "base_image_id": "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....qcsa7klnoa",
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....lwbvm62xq",
              "create_image_allowed": true,
              "display_name": "my-image-1",
              "id": "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx.....dgb3pmci2q",
              "launch_mode": "NATIVE",
              "launch_options": {
                 "boot_volume_type": "ISCSI",
                 "firmware": "UEFI_64",
                 "is_consistent_volume_naming_enabled": null,
                 "is_pv_encryption_in_transit_enabled": null,
                 "network_type": "VFIO",
                 "remote_data_volume_type": "PARAVIRTUALIZED"
               },
              "lifecycle_state": "AVAILABLE",
              "operating_system": "Canonical Ubuntu",
              "operating_system_version": "16.04",
              "time_created": "2017-11-24T13:18:31.579000+00:00"
           }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import (
        UpdateImageDetails,
        ImageSourceViaObjectStorageTupleDetails,
        ImageSourceViaObjectStorageUriDetails,
        CreateImageDetails,
    )
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "image"


def _get_image_from_id(compute_client, id, module):
    try:
        return oci_utils.call_with_backoff(compute_client.get_image, image_id=id)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def delete_image(compute_client, id, module):
    return oci_utils.delete_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        get_fn=compute_client.get_image,
        kwargs_get={"image_id": id},
        delete_fn=compute_client.delete_image,
        kwargs_delete={"image_id": id},
        module=module,
    )


def update_image(compute_client, id, display_name, module):
    result = dict()
    changed = False
    try:
        uid = UpdateImageDetails()
        uid.display_name = display_name
        oci_utils.add_tags_to_model_from_module(uid, module)
        debug("Instance " + id + " - updating with new name: " + display_name)
        response = oci_utils.call_with_backoff(
            compute_client.update_image, image_id=id, update_image_details=uid
        )
        result["image"] = to_dict(response.data)
        changed = True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    return result


def create_image(compute_client, module):
    cid = _get_create_image_details(module)
    return oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        create_fn=compute_client.create_image,
        kwargs_create={"create_image_details": cid},
        get_fn=compute_client.get_image,
        get_param="image_id",
        module=module,
    )


def _get_create_image_details(module):
    comp_id = module.params["compartment_id"]
    name = module.params["name"]
    instance_id = module.params["instance_id"]
    image_source_details = module.params["image_source_details"]
    launch_mode = module.params["launch_mode"]

    cid = CreateImageDetails()
    cid.compartment_id = comp_id
    cid.display_name = name
    cid.launch_mode = launch_mode
    oci_utils.add_tags_to_model_from_module(cid, module)

    # An image can be created from an instance, or imported from an exported image available in object storage
    if instance_id:
        cid.instance_id = instance_id
    elif image_source_details:
        source_type = image_source_details["source_type"]
        isd = None
        # The exported image can be provided as a tuple(namespace,bucket,object) or a URI
        if source_type == "objectStorageTuple":
            isd = ImageSourceViaObjectStorageTupleDetails()
            isd.source_type = source_type
            isd.namespace_name = image_source_details["namespace"]
            isd.bucket_name = image_source_details["bucket"]
            isd.object_name = image_source_details["object"]
            isd.source_image_type = image_source_details["source_image_type"]
        elif source_type == "objectStorageUri":
            isd = ImageSourceViaObjectStorageUriDetails()
            isd.source_type = source_type
            isd.source_uri = image_source_details["source_uri"]
            isd.source_image_type = image_source_details["source_image_type"]
        cid.image_source_details = isd
    else:
        module.fail_json(
            msg="Specify instance_id or image_source_id while creating an instance."
        )

    return cid


def debug(s):
    get_logger().debug(s)


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def main():
    my_logger = oci_utils.get_logger("oci_instance")
    set_logger(my_logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            name=dict(type="str", required=False, aliases=["display_name"]),
            image_id=dict(type="str", required=False, aliases=["id"]),
            instance_id=dict(type="str", required=False),
            image_source_details=dict(type="dict", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            launch_mode=dict(
                type="str",
                required=False,
                default="NATIVE",
                choices=["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("instance_id", "image_source_details")],
        required_if=[("state", "absent", ["image_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)
    state = module.params["state"]

    result = dict(changed=False)

    id = module.params.get("image_id", None)
    exclude_attributes = {"display_name": True}
    debug("Id is " + str(id))
    if id is not None:
        image_resp = _get_image_from_id(compute_client, id, module)

        if state == "absent":
            debug("Delete " + id + " requested")
            if image_resp.data is not None:
                debug("Deleting " + image_resp.data.id)
                result = delete_image(compute_client, id, module)
            else:
                debug("Image " + id + " already deleted.")
        elif state == "present":
            display_name = module.params["name"]
            current_image = image_resp.data
            attrs_equal = oci_utils.are_attrs_equal(
                current_image, module, ["display_name", "freeform_tags", "defined_tags"]
            )
            if not attrs_equal:
                result = update_image(compute_client, id, display_name, module)
    else:
        result = oci_utils.check_and_create_resource(
            resource_type="image",
            create_fn=create_image,
            kwargs_create={"compute_client": compute_client, "module": module},
            list_fn=compute_client.list_images,
            kwargs_list={"compartment_id": module.params["compartment_id"]},
            module=module,
            model=CreateImageDetails(),
            exclude_attributes=exclude_attributes,
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
