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
module: oci_object_storage_namespace_facts
short_description: Fetches details about a Namespace resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Namespace resource in Oracle Cloud Infrastructure
    - Each Oracle Cloud Infrastructure tenant is assigned one unique and uneditable Object Storage namespace. The namespace
      is a system-generated string assigned during account creation. For some older tenancies, the namespace string may be
      the tenancy name in all lower-case letters. You cannot edit a namespace.
    - GetNamespace returns the name of the Object Storage namespace for the user making the request.
      If an optional compartmentId query parameter is provided, GetNamespace returns the namespace name of the corresponding
      tenancy, provided the user has access to it.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - This is an optional field representing either the tenancy L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) or the
              compartment
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) within the tenancy whose Object Storage namespace is to be
              retrieved.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific namespace
  oci_object_storage_namespace_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
namespace:
    description:
        - Namespace resource
    returned: on success
    type: str
    sample: "sample"
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.object_storage import ObjectStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace, **optional_kwargs
        )


NamespaceFactsHelperCustom = get_custom_class("NamespaceFactsHelperCustom")


class ResourceFactsHelper(NamespaceFactsHelperCustom, NamespaceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str"),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="namespace",
        service_client_class=ObjectStorageClient,
        namespace="object_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(namespace=result)


if __name__ == "__main__":
    main()
