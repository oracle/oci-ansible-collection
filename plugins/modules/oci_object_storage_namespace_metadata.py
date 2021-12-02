#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_object_storage_namespace_metadata
short_description: Manage a NamespaceMetadata resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a NamespaceMetadata resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        type: str
        required: true
    default_s3_compartment_id:
        description:
            - The updated compartment id for use by an S3 client, if this field is set.
            - This parameter is updatable.
        type: str
    default_swift_compartment_id:
        description:
            - The updated compartment id for use by a Swift client, if this field is set.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the NamespaceMetadata.
            - Use I(state=present) to update an existing a NamespaceMetadata.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update namespace_metadata
  oci_object_storage_namespace_metadata:
    # required
    namespace_name: namespace_name_example

    # optional
    default_s3_compartment_id: "ocid.compartment.oc1..exampleuniquecompartmentS3ID"
    default_swift_compartment_id: "ocid.compartment.oc1..exampleuniquecompartmentSwiftID"

"""

RETURN = """
namespace_metadata:
    description:
        - Details of the NamespaceMetadata resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        namespace:
            description:
                - The Object Storage namespace to which the metadata belongs.
            returned: on success
            type: str
            sample: namespace_example
        default_s3_compartment_id:
            description:
                - If the field is set, specifies the default compartment assignment for the Amazon S3 Compatibility API.
            returned: on success
            type: str
            sample: "ocid1.defaults3compartment.oc1..xxxxxxEXAMPLExxxxxx"
        default_swift_compartment_id:
            description:
                - If the field is set, specifies the default compartment assignment for the Swift API.
            returned: on success
            type: str
            sample: "ocid1.defaultswiftcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "namespace": "namespace_example",
        "default_s3_compartment_id": "ocid1.defaults3compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "default_swift_compartment_id": "ocid1.defaultswiftcompartment.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.object_storage import ObjectStorageClient
    from oci.object_storage.models import UpdateNamespaceMetadataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceMetadataHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def get_get_fn(self):
        return self.client.get_namespace_metadata

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace_metadata,
            namespace_name=self.module.params.get("namespace_name"),
        )

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return UpdateNamespaceMetadataDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_namespace_metadata,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                update_namespace_metadata_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


NamespaceMetadataHelperCustom = get_custom_class("NamespaceMetadataHelperCustom")


class ResourceHelper(NamespaceMetadataHelperCustom, NamespaceMetadataHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            default_s3_compartment_id=dict(type="str"),
            default_swift_compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="namespace_metadata",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
