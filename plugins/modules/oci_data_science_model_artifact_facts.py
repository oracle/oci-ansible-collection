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
module: oci_data_science_model_artifact_facts
short_description: Fetches details about a ModelArtifact resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ModelArtifact resource in Oracle Cloud Infrastructure
    - Downloads model artifact content for specified model.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model.
        type: str
        aliases: ["id"]
        required: true
    range:
        description:
            - Optional byte range to fetch, as described in L(RFC 7233,https://tools.ietf.org/html/rfc7232#section-2.1), section 2.1.
              Note that only a single range of bytes is supported.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific model_artifact
  oci_data_science_model_artifact_facts:
    # required
    dest: /tmp/myfile
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    range: range_example

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
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


class DataScienceModelArtifactFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "model_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "range",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_model_artifact_content,
            model_id=self.module.params.get("model_id"),
            **optional_kwargs
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


DataScienceModelArtifactFactsHelperCustom = get_custom_class(
    "DataScienceModelArtifactFactsHelperCustom"
)


class ResourceFactsHelper(
    DataScienceModelArtifactFactsHelperCustom, DataScienceModelArtifactFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            model_id=dict(aliases=["id"], type="str", required=True),
            range=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="model_artifact",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(model_artifact=result)


if __name__ == "__main__":
    main()
