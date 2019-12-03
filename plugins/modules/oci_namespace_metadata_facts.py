#!/usr/bin/python
# Copyright (c) 2019 Oracle and/or its affiliates.
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
module: oci_namespace_metadata_facts
short_description: Gets the metadata for the Object Storage namespace
description: Gets the metadata for the Object Storage namespace, which contains defaultS3CompartmentId and
             defaultSwiftCompartmentId.
version_added: "2.5"
options:
    namespace_name:
        description: The Object Storage namespace.
        required: true
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get the object storage namespace metadata
  oci_namespace_metadata_facts:
    namespace_name: examplenamespace
"""

RETURN = """
namespace_metadatas:
    description: The metadata for the Object Storage namespace, which contains defaultS3CompartmentId and
                 defaultSwiftCompartmentId.
    returned: on success
    type: complex
    contains:
        namespace:
            description: The Object Storage namespace to which the metadata belongs.
            returned: on success
            type: string
            sample: examplenamespace
        default_s3_compartment_id:
            description:  The default compartment assignment for the Amazon S3 Compatibility API.
            returned: on success
            type: string
            sample: ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx
        default_swift_compartment_id:
            description:  The default compartment assignment for the Swift API.
            returned: on success
            type: string
            sample: ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
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
        return []

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
    module_args.update(dict(namespace_name=dict(type="str", required=True)))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="namespace_metadata",
        service_client_class=ObjectStorageClient,
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(namespace_metadatas=result)


if __name__ == "__main__":
    main()
