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
module: oci_namespace_facts
short_description: Retrieve facts of a namespace
description: Retrieve facts of the Object Storage namespace.
version_added: "2.5"
options:
    compartment_id:
        description: The tenancy OCID or the compartment OCID within the tenancy whose Object Storage namespace name has
                     to be retrieved.
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get the object storage namespace
  oci_namespace_facts:

- name: Get the object storage namespace using the optional compartment id parameter
  oci_namespace_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
namespaces:
    description: The Object Storage namespace name of the tenancy.
    returned: on success
    type: list
    sample: ["examplenamespace"]
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


class NamespaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        optional_get_method_params = ["compartment_id"]
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
    module_args.update(dict(compartment_id=dict(type="str")))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="namespace",
        service_client_class=ObjectStorageClient,
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(namespaces=result)


if __name__ == "__main__":
    main()
