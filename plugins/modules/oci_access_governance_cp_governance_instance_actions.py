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
module: oci_access_governance_cp_governance_instance_actions
short_description: Perform actions on a GovernanceInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a GovernanceInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a GovernanceInstance resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    governance_instance_id:
        description:
            - The OCID of the GovernanceInstance
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment where the GovernanceInstance resides.
        type: str
        required: true
    action:
        description:
            - The action to perform on the GovernanceInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on governance_instance
  oci_access_governance_cp_governance_instance_actions:
    # required
    governance_instance_id: "ocid1.governanceinstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
governance_instance:
    description:
        - Details of the GovernanceInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID of the GovernanceInstance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name for the GovernanceInstance.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the GovernanceInstance resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the GovernanceInstance was created in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the GovernanceInstance was updated in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the GovernanceInstance.
            returned: on success
            type: str
            sample: CREATING
        description:
            description:
                - The description of the GovernanceInstance.
            returned: on success
            type: str
            sample: description_example
        license_type:
            description:
                - The licenseType being used.
            returned: on success
            type: str
            sample: NEW_LICENSE
        tenancy_namespace:
            description:
                - The namespace for tenancy object storage.
            returned: on success
            type: str
            sample: tenancy_namespace_example
        instance_url:
            description:
                - The access URL of the GovernanceInstance.
            returned: on success
            type: str
            sample: instance_url_example
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "description": "description_example",
        "license_type": "NEW_LICENSE",
        "tenancy_namespace": "tenancy_namespace_example",
        "instance_url": "instance_url_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
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
    from oci.access_governance_cp import AccessGovernanceCPClient
    from oci.access_governance_cp.models import (
        ChangeGovernanceInstanceCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "governance_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("governance_instance_id")

    def get_get_fn(self):
        return self.client.get_governance_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance,
            governance_instance_id=self.module.params.get("governance_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeGovernanceInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_governance_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                governance_instance_id=self.module.params.get("governance_instance_id"),
                change_governance_instance_compartment_details=action_details,
            ),
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


GovernanceInstanceActionsHelperCustom = get_custom_class(
    "GovernanceInstanceActionsHelperCustom"
)


class ResourceHelper(
    GovernanceInstanceActionsHelperCustom, GovernanceInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            governance_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="governance_instance",
        service_client_class=AccessGovernanceCPClient,
        namespace="access_governance_cp",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
