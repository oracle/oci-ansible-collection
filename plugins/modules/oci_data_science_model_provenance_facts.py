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
module: oci_data_science_model_provenance_facts
short_description: Fetches details about a ModelProvenance resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ModelProvenance resource in Oracle Cloud Infrastructure
    - Gets provenance information for specified model.
version_added: "2.9"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific model_provenance
  oci_data_science_model_provenance_facts:
    model_id: ocid1.model.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
model_provenance:
    description:
        - ModelProvenance resource
    returned: on success
    type: complex
    contains:
        repository_url:
            description:
                - For model reproducibility purposes. URL of the git repository associated with model training.
            returned: on success
            type: string
            sample: http://git-remote.com/my-repo
        git_branch:
            description:
                - For model reproducibility purposes. Branch of the git repository associated with model training.
            returned: on success
            type: string
            sample: master
        git_commit:
            description:
                - For model reproducibility purposes. Commit ID of the git repository associated with model training.
            returned: on success
            type: string
            sample: 0978b63
        script_dir:
            description:
                - For model reproducibility purposes. Path to model artifacts.
            returned: on success
            type: string
            sample: script_dir_example
        training_script:
            description:
                - "For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\\""
            returned: on success
            type: string
            sample: model-dev/model1/model-training.ipynb
    sample: {
        "repository_url": "http://git-remote.com/my-repo",
        "git_branch": "master",
        "git_commit": "0978b63",
        "script_dir": "script_dir_example",
        "training_script": "model-dev/model1/model-training.ipynb"
    }
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


class DataScienceModelProvenanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "model_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_provenance,
            model_id=self.module.params.get("model_id"),
        )


DataScienceModelProvenanceFactsHelperCustom = get_custom_class(
    "DataScienceModelProvenanceFactsHelperCustom"
)


class ResourceFactsHelper(
    DataScienceModelProvenanceFactsHelperCustom,
    DataScienceModelProvenanceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(model_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="model_provenance",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(model_provenance=result)


if __name__ == "__main__":
    main()
