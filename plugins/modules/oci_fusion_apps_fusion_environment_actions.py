#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_fusion_apps_fusion_environment_actions
short_description: Perform actions on a FusionEnvironment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a FusionEnvironment resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a FusionEnvironment into a different compartment. When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fusion_environment_id:
        description:
            - unique FusionEnvironment identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the FusionEnvironment.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on fusion_environment
  oci_fusion_apps_fusion_environment_actions:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
fusion_environment:
    description:
        - Details of the FusionEnvironment resource acted upon by the current operation
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
                - FusionEnvironment Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        maintenance_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                quarterly_upgrade_begin_times:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        override_type:
                            description:
                                - Determines if the maintenance schedule of the Fusion environment is inherited from the Fusion environment family.
                            returned: on success
                            type: str
                            sample: OVERRIDDEN
                        begin_times_value:
                            description:
                                - The frequency and month when maintenance occurs for the Fusion environment.
                            returned: on success
                            type: str
                            sample: begin_times_value_example
                monthly_patching_override:
                    description:
                        - Whether the Fusion environment will be updated monthly or updated on the quarterly cycle. This setting overrides the monthly patching
                          setting of its Fusion environment family.
                    returned: on success
                    type: str
                    sample: monthly_patching_override_example
                environment_maintenance_override:
                    description:
                        - User choice to upgrade both production and non-production environments at the same time. Overrides the Fusion environment family
                          setting.
                    returned: on success
                    type: str
                    sample: environment_maintenance_override_example
        time_upcoming_maintenance:
            description:
                - The next maintenance for this environment
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        fusion_environment_family_id:
            description:
                - FusionEnvironmentFamily Identifier
            returned: on success
            type: str
            sample: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_ids:
            description:
                - List of subscription IDs.
            returned: on success
            type: list
            sample: []
        fusion_environment_type:
            description:
                - Type of the FusionEnvironment.
            returned: on success
            type: str
            sample: PRODUCTION
        kms_key_id:
            description:
                - BYOK key id
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_info:
            description:
                - BYOK key info
            returned: on success
            type: dict
            sample: {}
        domain_id:
            description:
                - The IDCS domain created for the fusion instance
            returned: on success
            type: str
            sample: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
        idcs_domain_url:
            description:
                - The IDCS Domain URL
            returned: on success
            type: str
            sample: idcs_domain_url_example
        applied_patch_bundles:
            description:
                - Patch bundle names
            returned: on success
            type: list
            sample: []
        version:
            description:
                - Version of Fusion Apps used by this environment
            returned: on success
            type: str
            sample: version_example
        public_url:
            description:
                - Public URL
            returned: on success
            type: str
            sample: public_url_example
        dns_prefix:
            description:
                - DNS prefix
            returned: on success
            type: str
            sample: dns_prefix_example
        additional_language_packs:
            description:
                - Language packs
            returned: on success
            type: list
            sample: []
        lockbox_id:
            description:
                - The lockbox Id of this fusion environment. If there's no lockbox id, this field will be null
            returned: on success
            type: str
            sample: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"
        is_break_glass_enabled:
            description:
                - If it's true, then the Break Glass feature is enabled
            returned: on success
            type: bool
            sample: true
        refresh:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_fusion_environment_id:
                    description:
                        - The source environment id for the last refresh
                    returned: on success
                    type: str
                    sample: "ocid1.sourcefusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"
                time_finished:
                    description:
                        - The time of when the last refresh finish
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_of_restoration_point:
                    description:
                        - The point of time of the latest DB backup for the last refresh
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        rules:
            description:
                - Network Access Control Rules
            returned: on success
            type: complex
            contains:
                action:
                    description:
                        - Rule type
                    returned: on success
                    type: str
                    sample: ALLOW
                conditions:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        attribute_name:
                            description:
                                - RuleCondition type
                            returned: on success
                            type: str
                            sample: SOURCE_IP_ADDRESS
                        attribute_value:
                            description:
                                - "An IPv4 or IPv6 address range that the source IP address of an incoming packet must match.
                                  The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y or x:x::x/y) strings.
                                  Specify 0.0.0.0/0 or ::/0 to match all incoming traffic.
                                  example: \\"192.168.0.0/16\\""
                            returned: on success
                            type: str
                            sample: attribute_value_example
                description:
                    description:
                        - "A brief description of the access control rule. Avoid entering confidential information.
                          example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`"
                    returned: on success
                    type: str
                    sample: description_example
        time_created:
            description:
                - The time the the FusionEnvironment was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the FusionEnvironment was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the ServiceInstance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        system_name:
            description:
                - Environment Specific Guid/ System Name
            returned: on success
            type: str
            sample: system_name_example
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "maintenance_policy": {
            "quarterly_upgrade_begin_times": {
                "override_type": "OVERRIDDEN",
                "begin_times_value": "begin_times_value_example"
            },
            "monthly_patching_override": "monthly_patching_override_example",
            "environment_maintenance_override": "environment_maintenance_override_example"
        },
        "time_upcoming_maintenance": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "fusion_environment_family_id": "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_ids": [],
        "fusion_environment_type": "PRODUCTION",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_info": {},
        "domain_id": "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx",
        "idcs_domain_url": "idcs_domain_url_example",
        "applied_patch_bundles": [],
        "version": "version_example",
        "public_url": "public_url_example",
        "dns_prefix": "dns_prefix_example",
        "additional_language_packs": [],
        "lockbox_id": "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx",
        "is_break_glass_enabled": true,
        "refresh": {
            "source_fusion_environment_id": "ocid1.sourcefusionenvironment.oc1..xxxxxxEXAMPLExxxxxx",
            "time_finished": "2013-10-20T19:20:30+01:00",
            "time_of_restoration_point": "2013-10-20T19:20:30+01:00"
        },
        "rules": [{
            "action": "ALLOW",
            "conditions": [{
                "attribute_name": "SOURCE_IP_ADDRESS",
                "attribute_value": "attribute_value_example"
            }],
            "description": "description_example"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "system_name": "system_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.fusion_apps import FusionApplicationsClient
    from oci.fusion_apps.models import ChangeFusionEnvironmentCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FusionEnvironmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "fusion_environment_id"

    def get_module_resource_id(self):
        return self.module.params.get("fusion_environment_id")

    def get_get_fn(self):
        return self.client.get_fusion_environment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeFusionEnvironmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_fusion_environment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fusion_environment_id=self.module.params.get("fusion_environment_id"),
                change_fusion_environment_compartment_details=action_details,
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


FusionEnvironmentActionsHelperCustom = get_custom_class(
    "FusionEnvironmentActionsHelperCustom"
)


class ResourceHelper(
    FusionEnvironmentActionsHelperCustom, FusionEnvironmentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            fusion_environment_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="fusion_environment",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
