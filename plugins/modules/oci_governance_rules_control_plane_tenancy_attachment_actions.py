#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_governance_rules_control_plane_tenancy_attachment_actions
short_description: Perform actions on a TenancyAttachment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TenancyAttachment resource in Oracle Cloud Infrastructure
    - For I(action=retry), retry governance rule application for the specified tenancy attachment id.
      Used by the tenancy admins when all the workflow retries have exhausted.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenancy_attachment_id:
        description:
            - Unique tenancy attachment identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the TenancyAttachment.
        type: str
        required: true
        choices:
            - "retry"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action retry on tenancy_attachment
  oci_governance_rules_control_plane_tenancy_attachment_actions:
    # required
    tenancy_attachment_id: "ocid1.tenancyattachment.oc1..xxxxxxEXAMPLExxxxxx"
    action: retry

"""

RETURN = """
tenancy_attachment:
    description:
        - Details of the TenancyAttachment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the tenancy attachment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the root compartment containing the tenancy
                  attachment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        governance_rule_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the governance rule. Every tenancy
                  attachment is associated with a governance rule.
            returned: on success
            type: str
            sample: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the tenancy to which the governance rule is
                  attached.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the tenancy attachment.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - Date and time the tenancy attachment was created. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date and time the tenancy attachment was updated. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_attempted:
            description:
                - Date and time the tenancy attachment was last attempted. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "governance_rule_id": "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_attempted": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.governance_rules_control_plane import WorkRequestClient
    from oci.governance_rules_control_plane import GovernanceRuleClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TenancyAttachmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        retry
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "tenancy_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("tenancy_attachment_id")

    def get_get_fn(self):
        return self.client.get_tenancy_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tenancy_attachment,
            tenancy_attachment_id=self.module.params.get("tenancy_attachment_id"),
        )

    def retry(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.retry_tenancy_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tenancy_attachment_id=self.module.params.get("tenancy_attachment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TenancyAttachmentActionsHelperCustom = get_custom_class(
    "TenancyAttachmentActionsHelperCustom"
)


class ResourceHelper(
    TenancyAttachmentActionsHelperCustom, TenancyAttachmentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            tenancy_attachment_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["retry"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tenancy_attachment",
        service_client_class=GovernanceRuleClient,
        namespace="governance_rules_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
