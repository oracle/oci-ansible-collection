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
module: oci_database_migration_advisor_report_facts
short_description: Fetches details about a AdvisorReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AdvisorReport resource in Oracle Cloud Infrastructure
    - Get the Pre-Migration Advisor report details
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The OCID of the job
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific advisor_report
  oci_database_migration_advisor_report_facts:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
advisor_report:
    description:
        - AdvisorReport resource
    returned: on success
    type: complex
    contains:
        report_location_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                object_storage_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        bucket_name:
                            description:
                                - Name of the bucket containing the Premigration Advisor report.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        namespace:
                            description:
                                - Object Storage namespace.
                            returned: on success
                            type: str
                            sample: namespace_example
                        object_name:
                            description:
                                - Premigration Advisor report object name.
                            returned: on success
                            type: str
                            sample: object_name_example
                location_in_source:
                    description:
                        - File system path on the Source Database host where the Premigration Advisor report can be accessed.
                    returned: on success
                    type: str
                    sample: location_in_source_example
        result:
            description:
                - Premigration Advisor result.
            returned: on success
            type: str
            sample: FATAL
        number_of_fatal:
            description:
                - Number of Fatal results in the advisor report.
            returned: on success
            type: int
            sample: 56
        number_of_fatal_blockers:
            description:
                - Number of Fatal Blocker results in the advisor report.
            returned: on success
            type: int
            sample: 56
        number_of_warnings:
            description:
                - Number of Warning results in the advisor report.
            returned: on success
            type: int
            sample: 56
        number_of_informational_results:
            description:
                - Number of Informational results in the advisor report.
            returned: on success
            type: int
            sample: 56
    sample: {
        "report_location_details": {
            "object_storage_details": {
                "bucket_name": "bucket_name_example",
                "namespace": "namespace_example",
                "object_name": "object_name_example"
            },
            "location_in_source": "location_in_source_example"
        },
        "result": "FATAL",
        "number_of_fatal": 56,
        "number_of_fatal_blockers": 56,
        "number_of_warnings": 56,
        "number_of_informational_results": 56
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_migration import DatabaseMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AdvisorReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "job_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_advisor_report, job_id=self.module.params.get("job_id"),
        )


AdvisorReportFactsHelperCustom = get_custom_class("AdvisorReportFactsHelperCustom")


class ResourceFactsHelper(AdvisorReportFactsHelperCustom, AdvisorReportFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(job_id=dict(aliases=["id"], type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="advisor_report",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(advisor_report=result)


if __name__ == "__main__":
    main()
