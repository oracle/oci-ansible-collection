#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_operator_access_control_operator_action_facts
short_description: Fetches details about one or multiple OperatorAction resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OperatorAction resources in Oracle Cloud Infrastructure
    - Lists all the OperatorActions available in the system.
    - If I(operator_action_id) is specified, the details of a single OperatorAction will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operator_action_id:
        description:
            - Unique Oracle supplied identifier associated with the operator action.
            - Required to get a specific operator_action.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple operator_actions.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
    resource_type:
        description:
            - A filter to return only lists of resources that match the entire given service type.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given OperatorAction lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
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
- name: Get a specific operator_action
  oci_operator_access_control_operator_action_facts:
    # required
    operator_action_id: "ocid1.operatoraction.oc1..xxxxxxEXAMPLExxxxxx"

- name: List operator_actions
  oci_operator_access_control_operator_action_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    resource_type: resource_type_example
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
operator_actions:
    description:
        - List of OperatorAction resources
    returned: on success
    type: complex
    contains:
        customer_display_name:
            description:
                - Display Name of the operator action.
                - Returned for get operation
            returned: on success
            type: str
            sample: customer_display_name_example
        properties:
            description:
                - Fine grained properties associated with the operator control.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the property
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - value of the property
                    returned: on success
                    type: str
                    sample: value_example
        id:
            description:
                - Unique Oracle assigned identifier for the operator action.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Unique name of the operator action.
            returned: on success
            type: str
            sample: name_example
        component:
            description:
                - Name of the infrastructure layer associated with the operator action.
            returned: on success
            type: str
            sample: component_example
        compartment_id:
            description:
                - compartmentId for which the OperatorAction is applicable
                - Returned for list operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_type:
            description:
                - resourceType for which the OperatorAction is applicable
            returned: on success
            type: str
            sample: EXACC
        lifecycle_state:
            description:
                - The current lifecycle state of the operator action.
                - Returned for list operation
            returned: on success
            type: str
            sample: ACTIVE
        description:
            description:
                - Description of the operator action in terms of associated risk profile, and characteristics of the operating system commands made
                  available to the operator under this operator action.
            returned: on success
            type: str
            sample: description_example
    sample: [{
        "customer_display_name": "customer_display_name_example",
        "properties": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "component": "component_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "EXACC",
        "lifecycle_state": "ACTIVE",
        "description": "description_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.operator_access_control import OperatorActionsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorActionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "operator_action_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_action,
            operator_action_id=self.module.params.get("operator_action_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "resource_type",
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
            self.client.list_operator_actions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OperatorActionFactsHelperCustom = get_custom_class("OperatorActionFactsHelperCustom")


class ResourceFactsHelper(
    OperatorActionFactsHelperCustom, OperatorActionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operator_action_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            resource_type=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operator_action",
        service_client_class=OperatorActionsClient,
        namespace="operator_access_control",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(operator_actions=result)


if __name__ == "__main__":
    main()
