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
module: oci_opsi_summarize_awr_sources_summaries_facts
short_description: Fetches details about one or multiple SummarizeAwrSourcesSummaries resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SummarizeAwrSourcesSummaries resources in Oracle Cloud Infrastructure
    - Gets a list of summary of AWR Sources.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    awr_hub_id:
        description:
            - Unique Awr Hub identifier
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    name:
        description:
            - Name for an Awr source database
        type: str
    sort_by:
        description:
            - The order in which Awr sources summary records are listed
        type: str
        choices:
            - "snapshotsUploaded"
            - "name"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List summarize_awr_sources_summaries
  oci_opsi_summarize_awr_sources_summaries_facts:
    # required
    awr_hub_id: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    sort_by: snapshotsUploaded
    sort_order: ASC

"""

RETURN = """
summarize_awr_sources_summaries:
    description:
        - List of SummarizeAwrSourcesSummaries resources
    returned: on success
    type: complex
    contains:
        awr_hub_id:
            description:
                - AWR Hub OCID
            returned: on success
            type: str
            sample: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Database name of the Source database for which AWR Data will be uploaded to AWR Hub.
            returned: on success
            type: str
            sample: name_example
        awr_source_database_id:
            description:
                - DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.
            returned: on success
            type: str
            sample: "ocid1.awrsourcedatabase.oc1..xxxxxxEXAMPLExxxxxx"
        snapshots_uploaded:
            description:
                - Number of AWR snapshots uploaded from the Source database.
            returned: on success
            type: float
            sample: 10
        min_snapshot_identifier:
            description:
                - The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.
            returned: on success
            type: float
            sample: 10
        max_snapshot_identifier:
            description:
                - The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.
            returned: on success
            type: float
            sample: 10
        time_first_snapshot_generated:
            description:
                - The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted
                  datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_snapshot_generated:
            description:
                - The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted
                  datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        hours_since_last_import:
            description:
                - Number of hours since last AWR snapshots import happened from the Source database.
            returned: on success
            type: float
            sample: 1.2
    sample: [{
        "awr_hub_id": "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "awr_source_database_id": "ocid1.awrsourcedatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "snapshots_uploaded": 10,
        "min_snapshot_identifier": 10,
        "max_snapshot_identifier": 10,
        "time_first_snapshot_generated": "2013-10-20T19:20:30+01:00",
        "time_last_snapshot_generated": "2013-10-20T19:20:30+01:00",
        "hours_since_last_import": 1.2
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SummarizeAwrSourcesSummariesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "awr_hub_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_awr_sources_summaries,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            **optional_kwargs
        )


SummarizeAwrSourcesSummariesFactsHelperCustom = get_custom_class(
    "SummarizeAwrSourcesSummariesFactsHelperCustom"
)


class ResourceFactsHelper(
    SummarizeAwrSourcesSummariesFactsHelperCustom,
    SummarizeAwrSourcesSummariesFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            awr_hub_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["snapshotsUploaded", "name"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="summarize_awr_sources_summaries",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(summarize_awr_sources_summaries=result)


if __name__ == "__main__":
    main()
