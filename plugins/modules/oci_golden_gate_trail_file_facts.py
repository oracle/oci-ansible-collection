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
module: oci_golden_gate_trail_file_facts
short_description: Fetches details about one or multiple TrailFile resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TrailFile resources in Oracle Cloud Infrastructure
    - Lists the TrailFiles for a deployment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - A unique Deployment identifier.
        type: str
        required: true
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    trail_file_id:
        description:
            - A Trail File identifier
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeLastUpdated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              displayName is the default.
        type: str
        choices:
            - "timeLastUpdated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List trail_files
  oci_golden_gate_trail_file_facts:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    trail_file_id: "ocid1.trailfile.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: timeLastUpdated
    sort_order: ASC

"""

RETURN = """
trail_files:
    description:
        - List of TrailFile resources
    returned: on success
    type: complex
    contains:
        trail_file_id:
            description:
                - The TrailFile Id.
            returned: on success
            type: str
            sample: "ocid1.trailfile.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        size_in_bytes:
            description:
                - The size of the backup stored in object storage (in bytes)
            returned: on success
            type: int
            sample: 56
        time_last_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        number_of_sequences:
            description:
                - Number of sequences for a specific trail file
            returned: on success
            type: int
            sample: 56
        min_sequence_number:
            description:
                - Minimum sequence number
            returned: on success
            type: str
            sample: min_sequence_number_example
        max_sequence_number:
            description:
                - Maximum sequence number
            returned: on success
            type: str
            sample: max_sequence_number_example
        producer:
            description:
                - Producer Process Name if any.
            returned: on success
            type: str
            sample: producer_example
        consumers:
            description:
                - array of consumer process names
            returned: on success
            type: list
            sample: []
    sample: [{
        "trail_file_id": "ocid1.trailfile.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "size_in_bytes": 56,
        "time_last_updated": "2013-10-20T19:20:30+01:00",
        "number_of_sequences": 56,
        "min_sequence_number": "min_sequence_number_example",
        "max_sequence_number": "max_sequence_number_example",
        "producer": "producer_example",
        "consumers": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TrailFileFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "deployment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "trail_file_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_trail_files,
            deployment_id=self.module.params.get("deployment_id"),
            **optional_kwargs
        )


TrailFileFactsHelperCustom = get_custom_class("TrailFileFactsHelperCustom")


class ResourceFactsHelper(TrailFileFactsHelperCustom, TrailFileFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            trail_file_id=dict(type="str"),
            sort_by=dict(type="str", choices=["timeLastUpdated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="trail_file",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(trail_files=result)


if __name__ == "__main__":
    main()
