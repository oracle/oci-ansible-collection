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
module: oci_adm_knowledge_base_actions
short_description: Perform actions on a KnowledgeBase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a KnowledgeBase resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Knowledge Base from one compartment to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    knowledge_base_id:
        description:
            - The Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of a Knowledge Base, as a URL path
              parameter.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to which the resource must be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the KnowledgeBase.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on knowledge_base
  oci_adm_knowledge_base_actions:
    # required
    knowledge_base_id: "ocid1.knowledgebase.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
knowledge_base:
    description:
        - Details of the KnowledgeBase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the Knowledge Base.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the Knowledge Base.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The creation date and time of the Knowledge Base (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the Knowledge Base was last updated (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the Knowledge Base.
            returned: on success
            type: str
            sample: CREATING
        compartment_id:
            description:
                - The Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the Knowledge Base's
                  compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.adm import ApplicationDependencyManagementClient
    from oci.adm.models import ChangeKnowledgeBaseCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KnowledgeBaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "knowledge_base_id"

    def get_module_resource_id(self):
        return self.module.params.get("knowledge_base_id")

    def get_get_fn(self):
        return self.client.get_knowledge_base

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_knowledge_base,
            knowledge_base_id=self.module.params.get("knowledge_base_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeKnowledgeBaseCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_knowledge_base_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                knowledge_base_id=self.module.params.get("knowledge_base_id"),
                change_knowledge_base_compartment_details=action_details,
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


KnowledgeBaseActionsHelperCustom = get_custom_class("KnowledgeBaseActionsHelperCustom")


class ResourceHelper(KnowledgeBaseActionsHelperCustom, KnowledgeBaseActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            knowledge_base_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="knowledge_base",
        service_client_class=ApplicationDependencyManagementClient,
        namespace="adm",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
