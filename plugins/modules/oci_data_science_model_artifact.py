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
module: oci_data_science_model_artifact
short_description: Manage a ModelArtifact resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a ModelArtifact resource in Oracle Cloud Infrastructure
    - For I(state=present), creates model artifact for specified model.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_artifact_file:
        description:
            - The model artifact file path to upload
        type: str
        required: true
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model.
        type: str
        required: true
    content_length:
        description:
            - The content length of the body.
        type: int
    model_artifact:
        description:
            - The model artifact to upload. We will soon deprecate this param, so please start using model_artifact_file.
        type: str
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
            - The state of the ModelArtifact.
            - Use I(state=present) to create a ModelArtifact.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create model_artifact
  oci_data_science_model_artifact:
    model_artifact_file: model.zip
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

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
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelArtifactHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_get_fn(self):
        return self.client.get_model_artifact_content

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_artifact_content,
            model_id=self.module.params.get("model_id"),
        )

    def create_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                content_length=self.module.params.get("content_length"),
                model_artifact=self.module.params.get("model_artifact"),
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


DataScienceModelArtifactHelperCustom = get_custom_class(
    "DataScienceModelArtifactHelperCustom"
)


class ResourceHelper(
    DataScienceModelArtifactHelperCustom, DataScienceModelArtifactHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            model_artifact_file=dict(type="str", required=True),
            model_id=dict(type="str", required=True),
            content_length=dict(type="int"),
            model_artifact=dict(type="str"),
            content_disposition=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model_artifact",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
