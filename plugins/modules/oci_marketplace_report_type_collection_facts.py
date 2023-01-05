#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_marketplace_report_type_collection_facts
short_description: Fetches details about one or multiple ReportTypeCollection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ReportTypeCollection resources in Oracle Cloud Infrastructure
    - Lists available types of reports for the compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List report_type_collections
  oci_marketplace_report_type_collection_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
report_type_collections:
    description:
        - List of ReportTypeCollection resources
    returned: on success
    type: complex
    contains:
        report_type:
            description:
                - The type of report.
            returned: on success
            type: str
            sample: report_type_example
        name:
            description:
                - The name of the report.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - A description of the report.
            returned: on success
            type: str
            sample: description_example
        columns:
            description:
                - The columns in the report.
            returned: on success
            type: list
            sample: []
    sample: [{
        "report_type": "report_type_example",
        "name": "name_example",
        "description": "description_example",
        "columns": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReportTypeCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_report_types,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ReportTypeCollectionFactsHelperCustom = get_custom_class(
    "ReportTypeCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    ReportTypeCollectionFactsHelperCustom, ReportTypeCollectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(compartment_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="report_type_collection",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(report_type_collections=result)


if __name__ == "__main__":
    main()
