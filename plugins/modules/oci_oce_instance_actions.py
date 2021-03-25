#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_oce_instance_actions
short_description: Perform actions on an OceInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OceInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a OceInstance into a different compartment
version_added: "2.9"
author: Oracle (@oracle)
options:
    oce_instance_id:
        description:
            - unique OceInstance identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the OceInstance should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the OceInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on oce_instance
  oci_oce_instance_actions:
    oce_instance_id: ocid1.oceinstance.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    action: change_compartment

"""

RETURN = """
oce_instance:
    description:
        - Details of the OceInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        guid:
            description:
                - Unique GUID identifier that is immutable on creation
            returned: on success
            type: string
            sample: guid_example
        description:
            description:
                - OceInstance description, can be updated
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - OceInstance Name
            returned: on success
            type: string
            sample: name_example
        tenancy_id:
            description:
                - Tenancy Identifier
            returned: on success
            type: string
            sample: ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx
        idcs_tenancy:
            description:
                - IDCS Tenancy Identifier
            returned: on success
            type: string
            sample: idcs_tenancy_example
        tenancy_name:
            description:
                - Tenancy Name
            returned: on success
            type: string
            sample: tenancy_name_example
        upgrade_schedule:
            description:
                - Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
                  or delay upgrade of the service to previous released version
            returned: on success
            type: string
            sample: UPGRADE_IMMEDIATELY
        identity_stripe:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                service_name:
                    description:
                        - "Name of the Identity Cloud Service instance in My Services to be used.
                          Example: `secondstripe`"
                    returned: on success
                    type: string
                    sample: secondstripe
                tenancy:
                    description:
                        - "Value of the Identity Cloud Service tenancy.
                          Example: `idcs-8416ebdd0d674f84803f4193cce026e9`"
                    returned: on success
                    type: string
                    sample: idcs-8416ebdd0d674f84803f4193cce026e9
        instance_usage_type:
            description:
                - Instance type based on its usage
            returned: on success
            type: string
            sample: PRIMARY
        object_storage_namespace:
            description:
                - Object Storage Namespace of tenancy
            returned: on success
            type: string
            sample: object_storage_namespace_example
        admin_email:
            description:
                - Admin Email for Notification
            returned: on success
            type: string
            sample: admin_email_example
        waf_primary_domain:
            description:
                - Web Application Firewall(WAF) primary domain
            returned: on success
            type: string
            sample: waf_primary_domain_example
        instance_access_type:
            description:
                - Flag indicating whether the instance access is private or public
            returned: on success
            type: string
            sample: PUBLIC
        instance_license_type:
            description:
                - Flag indicating whether the instance license is new cloud or bring your own license
            returned: on success
            type: string
            sample: NEW
        time_created:
            description:
                - The time the the OceInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the OceInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the file system.
            returned: on success
            type: string
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        service:
            description:
                - "SERVICE data.
                  Example: `{\\"service\\": {\\"IDCS\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "guid": "guid_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "idcs_tenancy": "idcs_tenancy_example",
        "tenancy_name": "tenancy_name_example",
        "upgrade_schedule": "UPGRADE_IMMEDIATELY",
        "identity_stripe": {
            "service_name": "secondstripe",
            "tenancy": "idcs-8416ebdd0d674f84803f4193cce026e9"
        },
        "instance_usage_type": "PRIMARY",
        "object_storage_namespace": "object_storage_namespace_example",
        "admin_email": "admin_email_example",
        "waf_primary_domain": "waf_primary_domain_example",
        "instance_access_type": "PUBLIC",
        "instance_license_type": "NEW",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "service": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.oce import OceInstanceClient
    from oci.oce.models import ChangeOceInstanceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OceInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "oce_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("oce_instance_id")

    def get_get_fn(self):
        return self.client.get_oce_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oce_instance,
            oce_instance_id=self.module.params.get("oce_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOceInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_oce_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oce_instance_id=self.module.params.get("oce_instance_id"),
                change_oce_instance_compartment_details=action_details,
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


OceInstanceActionsHelperCustom = get_custom_class("OceInstanceActionsHelperCustom")


class ResourceHelper(OceInstanceActionsHelperCustom, OceInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            oce_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="oce_instance",
        service_client_class=OceInstanceClient,
        namespace="oce",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
