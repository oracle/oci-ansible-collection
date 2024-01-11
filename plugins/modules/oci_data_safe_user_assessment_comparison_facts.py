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
module: oci_data_safe_user_assessment_comparison_facts
short_description: Fetches details about a UserAssessmentComparison resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a UserAssessmentComparison resource in Oracle Cloud Infrastructure
    - Gets the details of the comparison report for the user assessments submitted for comparison.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_assessment_id:
        description:
            - The OCID of the user assessment.
        type: str
        required: true
    comparison_user_assessment_id:
        description:
            - The OCID of the baseline user assessment.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific user_assessment_comparison
  oci_data_safe_user_assessment_comparison_facts:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"
    comparison_user_assessment_id: "ocid1.comparisonuserassessment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
user_assessment_comparison:
    description:
        - UserAssessmentComparison resource
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The current state of the user assessment comparison.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the user assessment comparison was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        summary:
            description:
                - "List containing maps as values.
                  Example: `{\\"Operations\\": [ {\\"CostCenter\\": \\"42\\"} ] }`"
            returned: on success
            type: list
            sample: []
    sample: {
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "summary": []
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeUserAssessmentComparisonFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "user_assessment_id",
            "comparison_user_assessment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_assessment_comparison,
            user_assessment_id=self.module.params.get("user_assessment_id"),
            comparison_user_assessment_id=self.module.params.get(
                "comparison_user_assessment_id"
            ),
        )


DataSafeUserAssessmentComparisonFactsHelperCustom = get_custom_class(
    "DataSafeUserAssessmentComparisonFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeUserAssessmentComparisonFactsHelperCustom,
    DataSafeUserAssessmentComparisonFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_assessment_id=dict(type="str", required=True),
            comparison_user_assessment_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="user_assessment_comparison",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(user_assessment_comparison=result)


if __name__ == "__main__":
    main()
