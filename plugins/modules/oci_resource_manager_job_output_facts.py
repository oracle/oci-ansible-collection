#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_resource_manager_job_output_facts
short_description: Fetches details about one or multiple JobOutput resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple JobOutput resources in Oracle Cloud Infrastructure
    - Gets the list of outputs associated with the specified job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
        type: str
        required: true
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List job_outputs
  oci_resource_manager_job_output_facts:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
job_outputs:
    description:
        - List of JobOutput resources
    returned: on success
    type: complex
    contains:
        output_name:
            description:
                - Name of the output.
            returned: on success
            type: str
            sample: output_name_example
        output_type:
            description:
                - Output resource type.
            returned: on success
            type: str
            sample: output_type_example
        output_value:
            description:
                - Value of the Terraform output.
            returned: on success
            type: str
            sample: output_value_example
        is_sensitive:
            description:
                - When `true`, output is sensitive.
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - Description of the output.
            returned: on success
            type: str
            sample: description_example
    sample: [{
        "output_name": "output_name_example",
        "output_type": "output_type_example",
        "output_value": "output_value_example",
        "is_sensitive": true,
        "description": "description_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobOutputFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "job_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_job_outputs,
            job_id=self.module.params.get("job_id"),
            **optional_kwargs
        )


JobOutputFactsHelperCustom = get_custom_class("JobOutputFactsHelperCustom")


class ResourceFactsHelper(JobOutputFactsHelperCustom, JobOutputFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(job_id=dict(type="str", required=True), compartment_id=dict(type="str"),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job_output",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(job_outputs=result)


if __name__ == "__main__":
    main()
