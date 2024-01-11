#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_management_agent_install_key_content_facts
short_description: Fetches details about a ManagementAgentInstallKeyContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ManagementAgentInstallKeyContent resource in Oracle Cloud Infrastructure
    - Returns a file with Management Agent install Key in it
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    management_agent_install_key_id:
        description:
            - Unique Management Agent Install Key identifier
        type: str
        aliases: ["id"]
        required: true
    plugin_name:
        description:
            - Filter to return input plugin names uncommented in the output.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific management_agent_install_key_content
  oci_management_agent_install_key_content_facts:
    # required
    dest: /tmp/myfile
    management_agent_install_key_id: "ocid1.managementagentinstallkey.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    plugin_name: [ "plugin_name_example" ]

"""


from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentInstallKeyContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "management_agent_install_key_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "plugin_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_management_agent_install_key_content,
            management_agent_install_key_id=self.module.params.get(
                "management_agent_install_key_id"
            ),
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


ManagementAgentInstallKeyContentFactsHelperCustom = get_custom_class(
    "ManagementAgentInstallKeyContentFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementAgentInstallKeyContentFactsHelperCustom,
    ManagementAgentInstallKeyContentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            management_agent_install_key_id=dict(
                aliases=["id"], type="str", required=True
            ),
            plugin_name=dict(type="list", elements="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent_install_key_content",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agent_install_key_content=result)


if __name__ == "__main__":
    main()
