#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_apm_control_plane_apm_domain_actions
short_description: Perform actions on an ApmDomain resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ApmDomain resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an APM domain into a different compartment. When provided, If-Match is checked against ETag values of the APM
      domain.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The OCID of the APM domain
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the destination compartment for the APM domain.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ApmDomain.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on apm_domain
  oci_apm_control_plane_apm_domain_actions:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
apm_domain:
    description:
        - Details of the ApmDomain resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        data_upload_endpoint:
            description:
                - The endpoint where the APM agents upload their observations and metrics.
            returned: on success
            type: str
            sample: data_upload_endpoint_example
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name of the APM domain, which can be updated.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the APM domain.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment corresponding to the APM domain.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the APM domain.
            returned: on success
            type: str
            sample: CREATING
        is_free_tier:
            description:
                - Indicates if this is an Always Free resource.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the APM domain was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the APM domain was updated, expressed in RFC 3339 timestamp format.
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
    sample: {
        "data_upload_endpoint": "data_upload_endpoint_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "is_free_tier": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.apm_control_plane import ApmDomainClient
    from oci.apm_control_plane.models import ChangeApmDomainCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApmDomainActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "apm_domain_id"

    def get_module_resource_id(self):
        return self.module.params.get("apm_domain_id")

    def get_get_fn(self):
        return self.client.get_apm_domain

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_apm_domain,
            apm_domain_id=self.module.params.get("apm_domain_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeApmDomainCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_apm_domain_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                change_apm_domain_compartment_details=action_details,
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


ApmDomainActionsHelperCustom = get_custom_class("ApmDomainActionsHelperCustom")


class ResourceHelper(ApmDomainActionsHelperCustom, ApmDomainActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            apm_domain_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="apm_domain",
        service_client_class=ApmDomainClient,
        namespace="apm_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
