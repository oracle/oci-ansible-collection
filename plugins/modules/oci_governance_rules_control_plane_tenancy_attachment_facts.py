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
module: oci_governance_rules_control_plane_tenancy_attachment_facts
short_description: Fetches details about one or multiple TenancyAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TenancyAttachment resources in Oracle Cloud Infrastructure
    - List tenancy attachments. Either compartment id, governance rule id or tenancy attachment id must be supplied.
      An optional lifecycle state or a child tenancy id can also be supplied.
    - If I(tenancy_attachment_id) is specified, the details of a single TenancyAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    tenancy_attachment_id:
        description:
            - Unique tenancy attachment identifier.
            - Required to get a specific tenancy_attachment.
        type: str
        aliases: ["id"]
    governance_rule_id:
        description:
            - Unique governance rule identifier.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources when their lifecycle state matches the given lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "NEEDS_ATTENTION"
            - "DELETING"
            - "DELETED"
    child_tenancy_id:
        description:
            - A filter to return only governance rules that match the given tenancy id.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific tenancy_attachment
  oci_governance_rules_control_plane_tenancy_attachment_facts:
    # required
    tenancy_attachment_id: "ocid1.tenancyattachment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List tenancy_attachments
  oci_governance_rules_control_plane_tenancy_attachment_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    tenancy_attachment_id: "ocid1.tenancyattachment.oc1..xxxxxxEXAMPLExxxxxx"
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    child_tenancy_id: "ocid1.childtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
tenancy_attachments:
    description:
        - List of TenancyAttachment resources
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "governance_rule_id": "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_attempted": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.governance_rules_control_plane import GovernanceRuleClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TenancyAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "tenancy_attachment_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tenancy_attachment,
            tenancy_attachment_id=self.module.params.get("tenancy_attachment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "tenancy_attachment_id",
            "governance_rule_id",
            "lifecycle_state",
            "child_tenancy_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tenancy_attachments, **optional_kwargs
        )


TenancyAttachmentFactsHelperCustom = get_custom_class(
    "TenancyAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    TenancyAttachmentFactsHelperCustom, TenancyAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            tenancy_attachment_id=dict(aliases=["id"], type="str"),
            governance_rule_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "NEEDS_ATTENTION",
                    "DELETING",
                    "DELETED",
                ],
            ),
            child_tenancy_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tenancy_attachment",
        service_client_class=GovernanceRuleClient,
        namespace="governance_rules_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tenancy_attachments=result)


if __name__ == "__main__":
    main()
