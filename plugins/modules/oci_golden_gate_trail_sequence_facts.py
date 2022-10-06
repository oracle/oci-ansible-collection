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
module: oci_golden_gate_trail_sequence_facts
short_description: Fetches details about one or multiple TrailSequence resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TrailSequence resources in Oracle Cloud Infrastructure
    - Lists the Trail Sequences for a TrailFile in a given deployment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - A unique Deployment identifier.
        type: str
        required: true
    trail_file_id:
        description:
            - A Trail File identifier
        type: str
        required: true
    trail_sequence_id:
        description:
            - A Trail Sequence identifier
        type: str
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
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
- name: List trail_sequences
  oci_golden_gate_trail_sequence_facts:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    trail_file_id: "ocid1.trailfile.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    trail_sequence_id: "ocid1.trailsequence.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: timeLastUpdated
    sort_order: ASC

"""

RETURN = """
trail_sequences:
    description:
        - List of TrailSequence resources
    returned: on success
    type: complex
    contains:
        sequence_id:
            description:
                - Sequence Id
            returned: on success
            type: str
            sample: "ocid1.sequence.oc1..xxxxxxEXAMPLExxxxxx"
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
            type: float
            sample: 10
        time_last_updated:
            description:
                - The time the resource was last updated. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "sequence_id": "ocid1.sequence.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "size_in_bytes": 10,
        "time_last_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TrailSequenceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "deployment_id",
            "trail_file_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "trail_sequence_id",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_trail_sequences,
            deployment_id=self.module.params.get("deployment_id"),
            trail_file_id=self.module.params.get("trail_file_id"),
            **optional_kwargs
        )


TrailSequenceFactsHelperCustom = get_custom_class("TrailSequenceFactsHelperCustom")


class ResourceFactsHelper(TrailSequenceFactsHelperCustom, TrailSequenceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(type="str", required=True),
            trail_file_id=dict(type="str", required=True),
            trail_sequence_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeLastUpdated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="trail_sequence",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(trail_sequences=result)


if __name__ == "__main__":
    main()
