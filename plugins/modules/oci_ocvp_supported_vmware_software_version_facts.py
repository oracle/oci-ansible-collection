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
module: oci_ocvp_supported_vmware_software_version_facts
short_description: Fetches details about one or multiple SupportedVmwareSoftwareVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SupportedVmwareSoftwareVersion resources in Oracle Cloud Infrastructure
    - Lists the versions of bundled VMware software supported by the Oracle Cloud
      VMware Solution.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List supported_vmware_software_versions
  oci_ocvp_supported_vmware_software_version_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
supported_vmware_software_versions:
    description:
        - List of SupportedVmwareSoftwareVersion resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - A short, unique string that identifies the version of bundled software.
            returned: on success
            type: string
            sample: version_example
        description:
            description:
                - A description of the software in the bundle.
            returned: on success
            type: string
            sample: description_example
    sample: [{
        "version": "version_example",
        "description": "description_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ocvp import SddcClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SupportedVmwareSoftwareVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_supported_vmware_software_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SupportedVmwareSoftwareVersionFactsHelperCustom = get_custom_class(
    "SupportedVmwareSoftwareVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    SupportedVmwareSoftwareVersionFactsHelperCustom,
    SupportedVmwareSoftwareVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="supported_vmware_software_version",
        service_client_class=SddcClient,
        namespace="ocvp",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(supported_vmware_software_versions=result)


if __name__ == "__main__":
    main()
