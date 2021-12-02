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
module: oci_compute_measured_boot_report_facts
short_description: Fetches details about a MeasuredBootReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a MeasuredBootReport resource in Oracle Cloud Infrastructure
    - Gets the measured boot report for this shielded instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific measured_boot_report
  oci_compute_measured_boot_report_facts:
    # required
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
measured_boot_report:
    description:
        - MeasuredBootReport resource
    returned: on success
    type: complex
    contains:
        is_policy_verification_successful:
            description:
                - Whether the verification succeeded, and the new values match the expected values.
            returned: on success
            type: bool
            sample: true
        measurements:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy:
                    description:
                        - The list of expected PCR entries to use during verification.
                    returned: on success
                    type: complex
                    contains:
                        pcr_index:
                            description:
                                - The index of the policy.
                            returned: on success
                            type: str
                            sample: pcr_index_example
                        value:
                            description:
                                - The hashed PCR value.
                            returned: on success
                            type: str
                            sample: value_example
                        hash_algorithm:
                            description:
                                - The type of algorithm used to calculate the hash.
                            returned: on success
                            type: str
                            sample: hash_algorithm_example
                actual:
                    description:
                        - The list of actual PCR entries measured during boot.
                    returned: on success
                    type: complex
                    contains:
                        pcr_index:
                            description:
                                - The index of the policy.
                            returned: on success
                            type: str
                            sample: pcr_index_example
                        value:
                            description:
                                - The hashed PCR value.
                            returned: on success
                            type: str
                            sample: value_example
                        hash_algorithm:
                            description:
                                - The type of algorithm used to calculate the hash.
                            returned: on success
                            type: str
                            sample: hash_algorithm_example
    sample: {
        "is_policy_verification_successful": true,
        "measurements": {
            "policy": [{
                "pcr_index": "pcr_index_example",
                "value": "value_example",
                "hash_algorithm": "hash_algorithm_example"
            }],
            "actual": [{
                "pcr_index": "pcr_index_example",
                "value": "value_example",
                "hash_algorithm": "hash_algorithm_example"
            }]
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MeasuredBootReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_measured_boot_report,
            instance_id=self.module.params.get("instance_id"),
        )


MeasuredBootReportFactsHelperCustom = get_custom_class(
    "MeasuredBootReportFactsHelperCustom"
)


class ResourceFactsHelper(
    MeasuredBootReportFactsHelperCustom, MeasuredBootReportFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(instance_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="measured_boot_report",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(measured_boot_report=result)


if __name__ == "__main__":
    main()
