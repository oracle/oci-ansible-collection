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
module: oci_data_science_notebook_session_shape_facts
short_description: Fetches details about one or multiple NotebookSessionShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NotebookSessionShape resources in Oracle Cloud Infrastructure
    - Lists the valid notebook session shapes.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List notebook_session_shapes
  oci_data_science_notebook_session_shape_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
notebook_session_shapes:
    description:
        - List of NotebookSessionShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the notebook session shape.
            returned: on success
            type: string
            sample: VM.STANDARD2.1
        core_count:
            description:
                - The number of cores associated with this notebook session shape.
            returned: on success
            type: int
            sample: 1
        memory_in_gbs:
            description:
                - The amount of memory in GBs associated with this notebook session shape.
            returned: on success
            type: int
            sample: 15
    sample: [{
        "name": "VM.STANDARD2.1",
        "core_count": 1,
        "memory_in_gbs": 15
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceNotebookSessionShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_notebook_session_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataScienceNotebookSessionShapeFactsHelperCustom = get_custom_class(
    "DataScienceNotebookSessionShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    DataScienceNotebookSessionShapeFactsHelperCustom,
    DataScienceNotebookSessionShapeFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(compartment_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="notebook_session_shape",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(notebook_session_shapes=result)


if __name__ == "__main__":
    main()
