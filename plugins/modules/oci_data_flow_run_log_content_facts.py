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
module: oci_data_flow_run_log_content_facts
short_description: Fetches details about a RunLogContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a RunLogContent resource in Oracle Cloud Infrastructure
    - Retrieves the content of an run log.
version_added: "2.9"
author: Oracle (@oracle)
options:
    run_id:
        description:
            - The unique ID for the run
        type: str
        required: true
    name:
        description:
            - The name of the log. Avoid entering confidential information.
        type: str
        required: true
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific run_log_content
  oci_data_flow_run_log_content_facts:
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    dest: /usr/local/myfile.zip

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunLogContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "run_id",
            "name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_run_log,
            run_id=self.module.params.get("run_id"),
            name=self.module.params.get("name"),
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


DataFlowRunLogContentFactsHelperCustom = get_custom_class(
    "DataFlowRunLogContentFactsHelperCustom"
)


class ResourceFactsHelper(
    DataFlowRunLogContentFactsHelperCustom, DataFlowRunLogContentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            run_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            dest=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="run_log_content",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(run_log_content=result)


if __name__ == "__main__":
    main()
