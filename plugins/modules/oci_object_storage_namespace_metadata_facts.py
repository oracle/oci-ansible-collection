#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_object_storage_namespace_metadata_facts
short_description: Fetches details about a NamespaceMetadata resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a NamespaceMetadata resource in Oracle Cloud Infrastructure
    - Gets the metadata for the Object Storage namespace, which contains defaultS3CompartmentId and
      defaultSwiftCompartmentId.
    - Any user with the OBJECTSTORAGE_NAMESPACE_READ permission will be able to see the current metadata. If you are
      not authorized, talk to an administrator. If you are an administrator who needs to write policies
      to give users access, see
      L(Getting Started with Policies,https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm).
version_added: "2.5"
options:
    namespace_name:
        description:
            - The Object Storage namespace used for the request.
        type: str
        required: true
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific namespace_metadata
  oci_object_storage_namespace_metadata_facts:
    namespace_name: namespace_name_example

"""

RETURN = """
namespace_metadata:
    description:
        - NamespaceMetadata resource
    returned: on success
    type: complex
    contains:
        namespace:
            description:
                - The Object Storage namespace to which the metadata belongs.
            returned: on success
            type: string
            sample: namespace_example
        default_s3_compartment_id:
            description:
                - If the field is set, specifies the default compartment assignment for the Amazon S3 Compatibility API.
            returned: on success
            type: string
            sample: ocid1.defaults3compartment.oc1..xxxxxxEXAMPLExxxxxx
        default_swift_compartment_id:
            description:
                - If the field is set, specifies the default compartment assignment for the Swift API.
            returned: on success
            type: string
            sample: ocid1.defaultswiftcompartment.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "namespace": "namespace_example",
        "default_s3_compartment_id": "ocid1.defaults3compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "default_swift_compartment_id": "ocid1.defaultswiftcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceMetadataFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace_metadata,
            namespace_name=self.module.params.get("namespace_name"),
        )


NamespaceMetadataFactsHelperCustom = get_custom_class(
    "NamespaceMetadataFactsHelperCustom"
)


class ResourceFactsHelper(
    NamespaceMetadataFactsHelperCustom, NamespaceMetadataFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(namespace_name=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="namespace_metadata",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(namespace_metadata=result)


if __name__ == "__main__":
    main()
