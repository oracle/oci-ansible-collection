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
module: oci_lockbox_approval_template_facts
short_description: Fetches details about one or multiple ApprovalTemplate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ApprovalTemplate resources in Oracle Cloud Infrastructure
    - Retrieves a list of ApprovalTemplateSummary objects in a compartment.
    - If I(approval_template_id) is specified, the details of a single ApprovalTemplate will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    approval_template_id:
        description:
            - The unique identifier (OCID) of the approval template.
            - Required to get a specific approval_template.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources for which their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
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
            - "id"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific approval_template
  oci_lockbox_approval_template_facts:
    # required
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"

- name: List approval_templates
  oci_lockbox_approval_template_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
approval_templates:
    description:
        - List of ApprovalTemplate resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier (OCID) of the approval template, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The approval template display name.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the approval template.
            returned: on success
            type: str
            sample: ACTIVE
        approver_levels:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                level1:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        approver_type:
                            description:
                                - The approver type of this approver level.
                            returned: on success
                            type: str
                            sample: GROUP
                        approver_id:
                            description:
                                - The group or user ocid of the approver for this approver level.
                            returned: on success
                            type: str
                            sample: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
                level2:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        approver_type:
                            description:
                                - The approver type of this approver level.
                            returned: on success
                            type: str
                            sample: GROUP
                        approver_id:
                            description:
                                - The group or user ocid of the approver for this approver level.
                            returned: on success
                            type: str
                            sample: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
                level3:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        approver_type:
                            description:
                                - The approver type of this approver level.
                            returned: on success
                            type: str
                            sample: GROUP
                        approver_id:
                            description:
                                - The group or user ocid of the approver for this approver level.
                            returned: on success
                            type: str
                            sample: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The unique identifier (OCID) of the customer compartment where the approval template is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        auto_approval_state:
            description:
                - The auto approval state of the lockbox.
            returned: on success
            type: str
            sample: ENABLED
        time_created:
            description:
                - The time the the approval template was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the approval template was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "ACTIVE",
        "approver_levels": {
            "level1": {
                "approver_type": "GROUP",
                "approver_id": "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "level2": {
                "approver_type": "GROUP",
                "approver_id": "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "level3": {
                "approver_type": "GROUP",
                "approver_id": "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "auto_approval_state": "ENABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.lockbox import LockboxClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApprovalTemplateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "approval_template_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_approval_template,
            approval_template_id=self.module.params.get("approval_template_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_approval_templates, **optional_kwargs
        )


ApprovalTemplateFactsHelperCustom = get_custom_class(
    "ApprovalTemplateFactsHelperCustom"
)


class ResourceFactsHelper(
    ApprovalTemplateFactsHelperCustom, ApprovalTemplateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            approval_template_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName", "id"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="approval_template",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(approval_templates=result)


if __name__ == "__main__":
    main()
