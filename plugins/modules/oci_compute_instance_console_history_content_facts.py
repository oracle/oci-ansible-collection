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
module: oci_compute_instance_console_history_content_facts
short_description: Fetches details about a InstanceConsoleHistoryContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a InstanceConsoleHistoryContent resource in Oracle Cloud Infrastructure
    - Gets the actual console history data (not the metadata).
      See L(CaptureConsoleHistory,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ConsoleHistory/CaptureConsoleHistory)
      for details about using the console history operations.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_console_history_id:
        description:
            - The OCID of the console history.
        type: str
        aliases: ["id"]
        required: true
    offset:
        description:
            - Offset of the snapshot data to retrieve.
        type: int
    length:
        description:
            - Length of the snapshot data to retrieve.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific instance_console_history_content
  oci_compute_instance_console_history_content_facts:
    # required
    instance_console_history_id: "ocid1.instanceconsolehistory.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    offset: 0
    length: 10240

"""

RETURN = """
instance_console_history_content:
    description:
        - InstanceConsoleHistoryContent resource
    returned: on success
    type: str
    sample: "sample"
"""

from ansible.module_utils._text import to_text
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConsoleHistoryContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "instance_console_history_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "offset",
            "length",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_console_history_content,
            instance_console_history_id=self.module.params.get(
                "instance_console_history_id"
            ),
            **optional_kwargs
        )

    def get(self):
        response_data = self.get_resource().data
        return to_text(response_data)


InstanceConsoleHistoryContentFactsHelperCustom = get_custom_class(
    "InstanceConsoleHistoryContentFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceConsoleHistoryContentFactsHelperCustom,
    InstanceConsoleHistoryContentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_console_history_id=dict(aliases=["id"], type="str", required=True),
            offset=dict(type="int"),
            length=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_console_history_content",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_console_history_content=result)


if __name__ == "__main__":
    main()
