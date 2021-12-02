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
module: oci_data_safe_security_assessment_comparison_facts
short_description: Fetches details about a SecurityAssessmentComparison resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SecurityAssessmentComparison resource in Oracle Cloud Infrastructure
    - Gets the details of the comparison report on the security assessments submitted for comparison.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    security_assessment_id:
        description:
            - The OCID of the security assessment.
        type: str
        required: true
    comparison_security_assessment_id:
        description:
            - The OCID of the baseline security assessment.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific security_assessment_comparison
  oci_data_safe_security_assessment_comparison_facts:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"
    comparison_security_assessment_id: "ocid1.comparisonsecurityassessment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
security_assessment_comparison:
    description:
        - SecurityAssessmentComparison resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the security assessment that is being compared with a baseline security assessment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        baseline_id:
            description:
                - The OCID of the security assessment that is set as a baseline.
            returned: on success
            type: str
            sample: "ocid1.baseline.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the security assessment comparison.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time when the security assessment comparison was created. Conforms to the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        targets:
            description:
                - A target-based comparison between two security assessments.
            returned: on success
            type: complex
            contains:
                baseline_target_id:
                    description:
                        - The OCID of the target that is used as a baseline in this comparison.
                    returned: on success
                    type: str
                    sample: "ocid1.baselinetarget.oc1..xxxxxxEXAMPLExxxxxx"
                current_target_id:
                    description:
                        - The OCID of the target to be compared against the baseline target.
                    returned: on success
                    type: str
                    sample: "ocid1.currenttarget.oc1..xxxxxxEXAMPLExxxxxx"
                auditing:
                    description:
                        - A comparison between findings belonging to Auditing category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
                authorization_control:
                    description:
                        - A comparison between findings belonging to Authorization Control category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
                data_encryption:
                    description:
                        - Comparison between findings belonging to Data Encryption category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
                db_configuration:
                    description:
                        - Comparison between findings belonging to Database Configuration category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
                fine_grained_access_control:
                    description:
                        - Comparison between findings belonging to Fine-Grained Access Control category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
                privileges_and_roles:
                    description:
                        - Comparison between findings belonging to Privileges and Roles category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
                user_accounts:
                    description:
                        - Comparison between findings belonging to User Accounts category.
                    returned: on success
                    type: complex
                    contains:
                        current:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        baseline:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - A unique identifier for the finding. This is common for the finding across targets.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                severity:
                                    description:
                                        - The severity of the finding.
                                    returned: on success
                                    type: str
                                    sample: HIGH
                                title:
                                    description:
                                        - The short title for the finding.
                                    returned: on success
                                    type: str
                                    sample: title_example
                                remarks:
                                    description:
                                        - The explanation of the issue in this finding. It explains the reason for the rule and, if a risk is reported, it may
                                          also explain the recommended actions for remediation.
                                    returned: on success
                                    type: str
                                    sample: remarks_example
                                details:
                                    description:
                                        - The details of the finding. Provides detailed information to explain the finding summary, typically results from the
                                          assessed database, followed by any recommendations for changes.
                                    returned: on success
                                    type: dict
                                    sample: {}
                                summary:
                                    description:
                                        - The brief summary of the finding. When the finding is informational, the summary typically reports only the number of
                                          data elements that were examined.
                                    returned: on success
                                    type: str
                                    sample: summary_example
                                references:
                                    description:
                                        - Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, STIG rule,
                                          or related to a GDPR Article/Recital.
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
                        removed_items:
                            description:
                                - This array identifies the items that are present in the baseline, but are missing from the current assessment.
                            returned: on success
                            type: list
                            sample: []
                        added_items:
                            description:
                                - This array identifies the items that are present in the current assessment, but are missing from the baseline.
                            returned: on success
                            type: list
                            sample: []
                        modified_items:
                            description:
                                - This array contains the items that are present in both the current assessment and the baseline, but are different in the two
                                  assessments.
                            returned: on success
                            type: list
                            sample: []
                        severity:
                            description:
                                - The severity of this diff.
                            returned: on success
                            type: str
                            sample: HIGH
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "baseline_id": "ocid1.baseline.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "targets": [{
            "baseline_target_id": "ocid1.baselinetarget.oc1..xxxxxxEXAMPLExxxxxx",
            "current_target_id": "ocid1.currenttarget.oc1..xxxxxxEXAMPLExxxxxx",
            "auditing": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }],
            "authorization_control": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }],
            "data_encryption": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }],
            "db_configuration": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }],
            "fine_grained_access_control": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }],
            "privileges_and_roles": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }],
            "user_accounts": [{
                "current": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "baseline": {
                    "key": "key_example",
                    "severity": "HIGH",
                    "title": "title_example",
                    "remarks": "remarks_example",
                    "details": {},
                    "summary": "summary_example",
                    "references": {
                        "stig": "stig_example",
                        "cis": "cis_example",
                        "gdpr": "gdpr_example"
                    }
                },
                "removed_items": [],
                "added_items": [],
                "modified_items": [],
                "severity": "HIGH"
            }]
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeSecurityAssessmentComparisonFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "security_assessment_id",
            "comparison_security_assessment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_assessment_comparison,
            security_assessment_id=self.module.params.get("security_assessment_id"),
            comparison_security_assessment_id=self.module.params.get(
                "comparison_security_assessment_id"
            ),
        )


DataSafeSecurityAssessmentComparisonFactsHelperCustom = get_custom_class(
    "DataSafeSecurityAssessmentComparisonFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeSecurityAssessmentComparisonFactsHelperCustom,
    DataSafeSecurityAssessmentComparisonFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            security_assessment_id=dict(type="str", required=True),
            comparison_security_assessment_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="security_assessment_comparison",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(security_assessment_comparison=result)


if __name__ == "__main__":
    main()
