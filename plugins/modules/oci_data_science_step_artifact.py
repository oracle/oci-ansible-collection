#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_data_science_step_artifact
short_description: Manage a StepArtifact resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a StepArtifact resource in Oracle Cloud Infrastructure
    - For I(state=present), upload the artifact for a step in the pipeline.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    step_artifact_file:
        description:
            - The path of step_artifact. The step artifact to upload.
        type: str
        required: true
    pipeline_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline.
        type: str
        required: true
    step_name:
        description:
            - Unique Step identifier in a pipeline.
        type: str
        required: true
    content_length:
        description:
            - The content length of the body.
        type: int
    content_disposition:
        description:
            - "This header allows you to specify a filename during upload. This file name is used to dispose of the file contents
              while downloading the file. If this optional field is not populated in the request, then the OCID of the model is used for the file
              name when downloading.
              Example: `{\\"Content-Disposition\\": \\"attachment\\"
                         \\"filename\\"=\\"model.tar.gz\\"
                         \\"Content-Length\\": \\"2347\\"
                         \\"Content-Type\\": \\"application/gzip\\"}`"
        type: str
    state:
        description:
            - The state of the StepArtifact.
            - Use I(state=present) to create a StepArtifact.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create step_artifact
  oci_data_science_step_artifact:
    # required
    step_artifact_file: step_artifact_file_example
    pipeline_id: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"
    step_name: step_name_example

    # optional
    content_length: 56
    content_disposition: content_disposition_example

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceStepArtifactHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(
            DataScienceStepArtifactHelperGen, self
        ).get_possible_entity_types() + [
            "datasciencepipeline",
            "datasciencepipelines",
            "dataSciencedatasciencepipeline",
            "dataSciencedatasciencepipelines",
            "datasciencepipelineresource",
            "datasciencepipelinesresource",
            "stepartifact",
            "stepartifacts",
            "dataSciencestepartifact",
            "dataSciencestepartifacts",
            "stepartifactresource",
            "stepartifactsresource",
            "artifact",
            "artifacts",
            "dataScienceartifact",
            "dataScienceartifacts",
            "artifactresource",
            "artifactsresource",
            "datascience",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def create_resource(self):
        file_path = self.module.params.get("step_artifact_file")
        with open(file_path, "rb") as input_file:
            return oci_wait_utils.call_and_wait(
                call_fn=self.client.create_step_artifact,
                call_fn_args=(),
                call_fn_kwargs=dict(
                    pipeline_id=self.module.params.get("pipeline_id"),
                    step_name=self.module.params.get("step_name"),
                    content_length=self.module.params.get("content_length"),
                    step_artifact=input_file,
                    content_disposition=self.module.params.get("content_disposition"),
                ),
                waiter_type=oci_wait_utils.NONE_WAITER_KEY,
                operation=oci_common_utils.CREATE_OPERATION_KEY,
                waiter_client=self.get_waiter_client(),
                resource_helper=self,
                wait_for_states=self.get_wait_for_states_for_operation(
                    oci_common_utils.CREATE_OPERATION_KEY,
                ),
            )


DataScienceStepArtifactHelperCustom = get_custom_class(
    "DataScienceStepArtifactHelperCustom"
)


class ResourceHelper(
    DataScienceStepArtifactHelperCustom, DataScienceStepArtifactHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            step_artifact_file=dict(type="str", required=True),
            pipeline_id=dict(type="str", required=True),
            step_name=dict(type="str", required=True),
            content_length=dict(type="int"),
            content_disposition=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="step_artifact",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
