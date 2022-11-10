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
module: oci_compute_measured_boot_report_actions
short_description: Perform actions on a MeasuredBootReport resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MeasuredBootReport resource in Oracle Cloud Infrastructure
    - For I(action=accept_shielded_integrity_policy), accept the changes to the PCR values in the measured boot report.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the MeasuredBootReport.
        type: str
        required: true
        choices:
            - "accept_shielded_integrity_policy"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action accept_shielded_integrity_policy on measured_boot_report
  oci_compute_measured_boot_report_actions:
    # required
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    action: accept_shielded_integrity_policy

"""

RETURN = """
measured_boot_report:
    description:
        - Details of the MeasuredBootReport resource acted upon by the current operation
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

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MeasuredBootReportActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        accept_shielded_integrity_policy
    """

    @staticmethod
    def get_module_resource_id_param():
        return "instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_id")

    def get_get_fn(self):
        return self.client.get_measured_boot_report

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_measured_boot_report,
            instance_id=self.module.params.get("instance_id"),
        )

    def accept_shielded_integrity_policy(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.accept_shielded_integrity_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(instance_id=self.module.params.get("instance_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


MeasuredBootReportActionsHelperCustom = get_custom_class(
    "MeasuredBootReportActionsHelperCustom"
)


class ResourceHelper(
    MeasuredBootReportActionsHelperCustom, MeasuredBootReportActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            instance_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str", required=True, choices=["accept_shielded_integrity_policy"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="measured_boot_report",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
