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
module: oci_operator_access_control_operator_control_facts
short_description: Fetches details about one or multiple OperatorControl resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OperatorControl resources in Oracle Cloud Infrastructure
    - Lists the operator controls in the compartment.
    - If I(operator_control_id) is specified, the details of a single OperatorControl will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operator_control_id:
        description:
            - unique OperatorControl identifier
            - Required to get a specific operator_control.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple operator_controls.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given OperatorControl lifecycleState.
        type: str
        choices:
            - "CREATED"
            - "ASSIGNED"
            - "UNASSIGNED"
            - "DELETED"
    display_name:
        description:
            - A filter to return OperatorControl that match the entire display name given.
        type: str
        aliases: ["name"]
    resource_type:
        description:
            - A filter to return only lists of resources that match the entire given service type.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific operator_control
  oci_operator_access_control_operator_control_facts:
    # required
    operator_control_id: "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx"

- name: List operator_controls
  oci_operator_access_control_operator_control_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATED
    display_name: display_name_example
    resource_type: resource_type_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
operator_controls:
    description:
        - List of OperatorControl resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - Description of operator control.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        approvers_list:
            description:
                - List of users who can approve an access request associated with a target resource under the governance of this operator control.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        approver_groups_list:
            description:
                - List of user groups who can approve an access request associated with a target resource under the governance of this operator control.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        pre_approved_op_action_list:
            description:
                - List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
                  automatically approved if the access request only contain operator actions in the pre-approved list.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        approval_required_op_action_list:
            description:
                - List of operator actions that need explicit approval. Any operator action not in the pre-approved list will require explicit
                  approval. Access requests associated with a resource governed by this operator control will be
                  require explicit approval if the access request contains any operator action in this list.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        email_id_list:
            description:
                - List of emailId.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        system_message:
            description:
                - System message that would be displayed to the operator users on accessing the target resource under the governance of this operator control.
                - Returned for get operation
            returned: on success
            type: str
            sample: system_message_example
        is_default_operator_control:
            description:
                - Whether the operator control is a default Operator Control.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        last_modified_info:
            description:
                - Description associated with the latest modification of the operator control.
                - Returned for get operation
            returned: on success
            type: str
            sample: last_modified_info_example
        id:
            description:
                - The OCID of the operator control.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        operator_control_name:
            description:
                - Name of the operator control. The name must be unique.
            returned: on success
            type: str
            sample: operator_control_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the operator control.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_fully_pre_approved:
            description:
                - Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator
                  control
                  will be auto-approved.
            returned: on success
            type: bool
            sample: true
        resource_type:
            description:
                - resourceType for which the OperatorControl is applicable
            returned: on success
            type: str
            sample: EXACC
        time_of_creation:
            description:
                - "Time when the operator control was created expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_modification:
            description:
                - "Time when the operator control was last modified expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "Time when deleted expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format. Example: '2020-05-22T21:10:29.600Z'.
                  Note a deleted operator control still stays in the system, so that you can still audit operator actions associated with access requests
                  raised on target resources governed by the deleted operator control."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the operator control.
            returned: on success
            type: str
            sample: CREATED
        freeform_tags:
            description:
                - Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "description": "description_example",
        "approvers_list": [],
        "approver_groups_list": [],
        "pre_approved_op_action_list": [],
        "approval_required_op_action_list": [],
        "email_id_list": [],
        "system_message": "system_message_example",
        "is_default_operator_control": true,
        "last_modified_info": "last_modified_info_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "operator_control_name": "operator_control_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_fully_pre_approved": true,
        "resource_type": "EXACC",
        "time_of_creation": "2013-10-20T19:20:30+01:00",
        "time_of_modification": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATED",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.operator_access_control import OperatorControlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorControlFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "operator_control_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control,
            operator_control_id=self.module.params.get("operator_control_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "resource_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_operator_controls,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OperatorControlFactsHelperCustom = get_custom_class("OperatorControlFactsHelperCustom")


class ResourceFactsHelper(
    OperatorControlFactsHelperCustom, OperatorControlFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operator_control_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            resource_type=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operator_control",
        service_client_class=OperatorControlClient,
        namespace="operator_access_control",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(operator_controls=result)


if __name__ == "__main__":
    main()
