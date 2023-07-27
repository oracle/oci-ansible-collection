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
module: oci_opa_instance_actions
short_description: Perform actions on an OpaInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OpaInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a OpaInstance resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opa_instance_id:
        description:
            - unique OpaInstance identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the OpaInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on opa_instance
  oci_opa_instance_actions:
    # required
    opa_instance_id: "ocid1.opainstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
opa_instance:
    description:
        - Details of the OpaInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - OpaInstance Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the Process Automation instance.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        instance_url:
            description:
                - OPA Instance URL
            returned: on success
            type: str
            sample: instance_url_example
        consumption_model:
            description:
                - The entitlement used for billing purposes
            returned: on success
            type: str
            sample: UCM
        shape_name:
            description:
                - Shape of the instance.
            returned: on success
            type: str
            sample: DEVELOPMENT
        metering_type:
            description:
                - MeteringType Identifier
            returned: on success
            type: str
            sample: EXECUTION_PACK
        time_created:
            description:
                - The time when OpaInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the OpaInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the OpaInstance.
            returned: on success
            type: str
            sample: CREATING
        identity_app_guid:
            description:
                - This property specifies the GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity
                  application instance may be used to host user role mappings to grant access to this OPA instance for users within the identity domain.
            returned: on success
            type: str
            sample: identity_app_guid_example
        identity_app_display_name:
            description:
                - This property specifies the name of the Identity Application instance OPA has created inside the user-specified identity domain. This identity
                  application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.
            returned: on success
            type: str
            sample: identity_app_display_name_example
        identity_domain_url:
            description:
                - This property specifies the domain url of the Identity Application instance OPA has created inside the user-specified identity domain. This
                  identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity
                  domain.
            returned: on success
            type: str
            sample: identity_domain_url_example
        identity_app_opc_service_instance_guid:
            description:
                - This property specifies the OPC Service Instance GUID of the Identity Application instance OPA has created inside the user-specified identity
                  domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the
                  identity domain.
            returned: on success
            type: str
            sample: identity_app_opc_service_instance_guid_example
        is_breakglass_enabled:
            description:
                - indicates if breakGlass is enabled for the opa instance.
            returned: on success
            type: bool
            sample: true
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
        attachments:
            description:
                - A list of associated attachments to other services
            returned: on success
            type: complex
            contains:
                target_role:
                    description:
                        - "The role of the target attachment.
                             * `PARENT` - The target instance is the parent of this attachment.
                             * `CHILD` - The target instance is the child of this attachment."
                    returned: on success
                    type: str
                    sample: PARENT
                is_implicit:
                    description:
                        - "* If role == `PARENT`, the attached instance was created by this service instance
                          * If role == `CHILD`, this instance was created from attached instance on behalf of a user"
                    returned: on success
                    type: bool
                    sample: true
                target_id:
                    description:
                        - The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.
                    returned: on success
                    type: str
                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                target_instance_url:
                    description:
                        - The dataplane instance URL of the attached instance
                    returned: on success
                    type: str
                    sample: target_instance_url_example
                target_service_type:
                    description:
                        - "The type of the target instance, such as \\"FUSION\\"."
                    returned: on success
                    type: str
                    sample: target_service_type_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_url": "instance_url_example",
        "consumption_model": "UCM",
        "shape_name": "DEVELOPMENT",
        "metering_type": "EXECUTION_PACK",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "identity_app_guid": "identity_app_guid_example",
        "identity_app_display_name": "identity_app_display_name_example",
        "identity_domain_url": "identity_domain_url_example",
        "identity_app_opc_service_instance_guid": "identity_app_opc_service_instance_guid_example",
        "is_breakglass_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }]
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
    from oci.opa import OpaInstanceClient
    from oci.opa.models import ChangeOpaInstanceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpaInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "opa_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("opa_instance_id")

    def get_get_fn(self):
        return self.client.get_opa_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opa_instance,
            opa_instance_id=self.module.params.get("opa_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOpaInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_opa_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opa_instance_id=self.module.params.get("opa_instance_id"),
                change_opa_instance_compartment_details=action_details,
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


OpaInstanceActionsHelperCustom = get_custom_class("OpaInstanceActionsHelperCustom")


class ResourceHelper(OpaInstanceActionsHelperCustom, OpaInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            opa_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opa_instance",
        service_client_class=OpaInstanceClient,
        namespace="opa",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
