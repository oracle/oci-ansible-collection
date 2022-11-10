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
module: oci_data_science_job_artifact
short_description: Manage a JobArtifact resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a JobArtifact resource in Oracle Cloud Infrastructure
    - For I(state=present), uploads a job artifact.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_artifact_file:
        description:
            - The path of job_artifact. The job artifact to upload.
        type: str
        required: true
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
        type: str
        required: true
    content_length:
        description:
            - The content length of the body.
        type: int
    content_disposition:
        description:
            - "This header is for specifying a filename during upload. It is used to identify the file type and validate if the
              file type is supported. Example: `--content-disposition \\"attachment; filename=hello-world.py\\"`"
        type: str
    state:
        description:
            - The state of the JobArtifact.
            - Use I(state=present) to create a JobArtifact.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create job_artifact
  oci_data_science_job_artifact:
    # required
    job_artifact_file: job_artifact_file_example
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

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


class DataScienceJobArtifactHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(
            DataScienceJobArtifactHelperGen, self
        ).get_possible_entity_types() + [
            "datasciencejob",
            "datasciencejobs",
            "dataSciencedatasciencejob",
            "dataSciencedatasciencejobs",
            "datasciencejobresource",
            "datasciencejobsresource",
            "jobartifact",
            "jobartifacts",
            "dataSciencejobartifact",
            "dataSciencejobartifacts",
            "jobartifactresource",
            "jobartifactsresource",
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
        file_path = self.module.params.get("job_artifact_file")
        with open(file_path, "rb") as input_file:
            return oci_wait_utils.call_and_wait(
                call_fn=self.client.create_job_artifact,
                call_fn_args=(),
                call_fn_kwargs=dict(
                    job_id=self.module.params.get("job_id"),
                    content_length=self.module.params.get("content_length"),
                    job_artifact=input_file,
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


DataScienceJobArtifactHelperCustom = get_custom_class(
    "DataScienceJobArtifactHelperCustom"
)


class ResourceHelper(
    DataScienceJobArtifactHelperCustom, DataScienceJobArtifactHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            job_artifact_file=dict(type="str", required=True),
            job_id=dict(type="str", required=True),
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
        resource_type="job_artifact",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
