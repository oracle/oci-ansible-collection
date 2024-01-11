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
module: oci_access_governance_cp_governance_instance_configuration
short_description: Manage a GovernanceInstanceConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a GovernanceInstanceConfiguration resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sender_info:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            display_name:
                description:
                    - The sender's displayName.
                    - This parameter is updatable.
                type: str
                aliases: ["name"]
            email:
                description:
                    - The sender's email.
                    - This parameter is updatable.
                type: str
                required: true
            is_inbox_configured:
                description:
                    - Whether the sender email has inbox configured to receive emails.
                    - This parameter is updatable.
                type: bool
                required: true
            is_resend_notification_email:
                description:
                    - Whether there is a need to resend the verification email.
                    - This parameter is updatable.
                type: bool
    compartment_id:
        description:
            - The OCID of the compartment in which resources are listed.
        type: str
        required: true
    state:
        description:
            - The state of the GovernanceInstanceConfiguration.
            - Use I(state=present) to update an existing a GovernanceInstanceConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update governance_instance_configuration
  oci_access_governance_cp_governance_instance_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sender_info:
      # required
      email: email_example
      is_inbox_configured: true

      # optional
      display_name: display_name_example
      is_resend_notification_email: true

"""

RETURN = """
governance_instance_configuration:
    description:
        - Details of the GovernanceInstanceConfiguration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        sender_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The sender's displayName.
                    returned: on success
                    type: str
                    sample: display_name_example
                email:
                    description:
                        - The sender's email.
                    returned: on success
                    type: str
                    sample: email_example
                is_verified:
                    description:
                        - Whether or not the sender's email has been verified.
                    returned: on success
                    type: bool
                    sample: true
                time_verify_response_expiry:
                    description:
                        - The time when the verify response needs to be received by.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                is_inbox_configured:
                    description:
                        - Whether the sender email has inbox configured to receive emails.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "sender_info": {
            "display_name": "display_name_example",
            "email": "email_example",
            "is_verified": true,
            "time_verify_response_expiry": "2013-10-20T19:20:30+01:00",
            "is_inbox_configured": true
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.access_governance_cp import AccessGovernanceCPClient
    from oci.access_governance_cp.models import (
        UpdateGovernanceInstanceConfigurationDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceInstanceConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            GovernanceInstanceConfigurationHelperGen, self
        ).get_possible_entity_types() + [
            "governanceinstanceconfiguration",
            "governanceinstanceconfigurations",
            "accessGovernanceCpgovernanceinstanceconfiguration",
            "accessGovernanceCpgovernanceinstanceconfigurations",
            "governanceinstanceconfigurationresource",
            "governanceinstanceconfigurationsresource",
            "configuration",
            "configurations",
            "accessGovernanceCpconfiguration",
            "accessGovernanceCpconfigurations",
            "configurationresource",
            "configurationsresource",
            "accessgovernancecp",
        ]

    def get_get_fn(self):
        return self.client.get_governance_instance_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_update_model_class(self):
        return UpdateGovernanceInstanceConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_governance_instance_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_governance_instance_configuration_details=update_details,
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


GovernanceInstanceConfigurationHelperCustom = get_custom_class(
    "GovernanceInstanceConfigurationHelperCustom"
)


class ResourceHelper(
    GovernanceInstanceConfigurationHelperCustom,
    GovernanceInstanceConfigurationHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            sender_info=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    email=dict(type="str", required=True),
                    is_inbox_configured=dict(type="bool", required=True),
                    is_resend_notification_email=dict(type="bool"),
                ),
            ),
            compartment_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="governance_instance_configuration",
        service_client_class=AccessGovernanceCPClient,
        namespace="access_governance_cp",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
