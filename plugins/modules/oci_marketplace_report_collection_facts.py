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
module: oci_marketplace_report_collection_facts
short_description: Fetches details about one or multiple ReportCollection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ReportCollection resources in Oracle Cloud Infrastructure
    - Lists reports in the compartment that match the specified report type and date.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    report_type:
        description:
            - The type of the report.
        type: str
        required: true
    date:
        description:
            - Date, expressed in `YYYYMMDD` format, where `Y` represents the year, `M` represents the month, and `D` represents the day.
        type: str
        required: true
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List report_collections
  oci_marketplace_report_collection_facts:
    report_type: report_type_example
    date: 2013-10-20T19:20:30+01:00
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
report_collections:
    description:
        - List of ReportCollection resources
    returned: on success
    type: complex
    contains:
        report_type:
            description:
                - The type of report.
            returned: on success
            type: str
            sample: report_type_example
        date:
            description:
                - The date of the report.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        columns:
            description:
                - The columns in the report.
            returned: on success
            type: list
            sample: []
        content:
            description:
                - The contents of the report in comma-separated values (CSV) file format.
            returned: on success
            type: str
            sample: content_example
    sample: [{
        "report_type": "report_type_example",
        "date": "2013-10-20T19:20:30+01:00",
        "columns": [],
        "content": "content_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReportCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "report_type",
            "date",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_reports,
            report_type=self.module.params.get("report_type"),
            date=self.module.params.get("date"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ReportCollectionFactsHelperCustom = get_custom_class(
    "ReportCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    ReportCollectionFactsHelperCustom, ReportCollectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            report_type=dict(type="str", required=True),
            date=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="report_collection",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(report_collections=result)


if __name__ == "__main__":
    main()
