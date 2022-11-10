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
module: oci_data_safe_finding_facts
short_description: Fetches details about one or multiple Finding resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Finding resources in Oracle Cloud Infrastructure
    - List all the findings from all the targets in the specified assessment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    security_assessment_id:
        description:
            - The OCID of the security assessment.
        type: str
        required: true
    severity:
        description:
            - A filter to return only findings of a particular risk level.
        type: str
        choices:
            - "HIGH"
            - "MEDIUM"
            - "LOW"
            - "EVALUATE"
            - "ADVISORY"
            - "PASS"
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the
              'accessLevel' setting.
        type: bool
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    finding_key:
        description:
            - Each finding has a key. This key is same for the finding across targets
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List findings
  oci_data_safe_finding_facts:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    severity: HIGH
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    finding_key: finding_key_example

"""

RETURN = """
findings:
    description:
        - List of Finding resources
    returned: on success
    type: complex
    contains:
        severity:
            description:
                - The severity of the finding.
            returned: on success
            type: str
            sample: HIGH
        assessment_id:
            description:
                - The OCID of the assessment that generated this finding.
            returned: on success
            type: str
            sample: "ocid1.assessment.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The OCID of the target database.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        key:
            description:
                - The unique finding key. This is a system-generated identifier. To get the finding key for a finding, use ListFindings.
            returned: on success
            type: str
            sample: key_example
        title:
            description:
                - The short title for the finding.
            returned: on success
            type: str
            sample: title_example
        remarks:
            description:
                - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may also explain the
                  recommended actions for remediation.
            returned: on success
            type: str
            sample: remarks_example
        details:
            description:
                - The details of the finding. Provides detailed information to explain the finding summary, typically results from the assessed database,
                  followed by any recommendations for changes.
            returned: on success
            type: dict
            sample: {}
        summary:
            description:
                - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of data elements that were
                  examined.
            returned: on success
            type: str
            sample: summary_example
        references:
            description:
                - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, a STIG rule, or a GDPR
                  Article/Recital.
            returned: on success
            type: complex
            contains:
                stig:
                    description:
                        - Relevant section from STIG.
                    returned: on success
                    type: str
                    sample: stig_example
                cis:
                    description:
                        - Relevant section from CIS.
                    returned: on success
                    type: str
                    sample: cis_example
                gdpr:
                    description:
                        - Relevant section from GDPR.
                    returned: on success
                    type: str
                    sample: gdpr_example
    sample: [{
        "severity": "HIGH",
        "assessment_id": "ocid1.assessment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "key": "key_example",
        "title": "title_example",
        "remarks": "remarks_example",
        "details": {},
        "summary": "summary_example",
        "references": {
            "stig": "stig_example",
            "cis": "cis_example",
            "gdpr": "gdpr_example"
        }
    }]
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


class DataSafeFindingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "security_assessment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "severity",
            "compartment_id_in_subtree",
            "access_level",
            "finding_key",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_findings,
            security_assessment_id=self.module.params.get("security_assessment_id"),
            **optional_kwargs
        )


DataSafeFindingFactsHelperCustom = get_custom_class("DataSafeFindingFactsHelperCustom")


class ResourceFactsHelper(
    DataSafeFindingFactsHelperCustom, DataSafeFindingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            security_assessment_id=dict(type="str", required=True),
            severity=dict(
                type="str",
                choices=["HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS"],
            ),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            finding_key=dict(type="str", no_log=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="finding",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(findings=result)


if __name__ == "__main__":
    main()
