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
module: oci_fusion_apps_fusion_environment_family_facts
short_description: Fetches details about one or multiple FusionEnvironmentFamily resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FusionEnvironmentFamily resources in Oracle Cloud Infrastructure
    - Returns a list of FusionEnvironmentFamilies.
    - If I(fusion_environment_family_id) is specified, the details of a single FusionEnvironmentFamily will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple fusion_environment_families.
        type: str
    fusion_environment_family_id:
        description:
            - The unique identifier (OCID) of the FusionEnvironmentFamily.
            - Required to get a specific fusion_environment_family.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter that returns all resources that match the specified lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
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
            - "TIME_CREATED"
            - "DISPLAY_NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific fusion_environment_family
  oci_fusion_apps_fusion_environment_family_facts:
    # required
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"

- name: List fusion_environment_families
  oci_fusion_apps_fusion_environment_family_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: TIME_CREATED

"""

RETURN = """
fusion_environment_families:
    description:
        - List of FusionEnvironmentFamily resources
    returned: on success
    type: complex
    contains:
        system_name:
            description:
                - Environment Specific Guid/ System Name
                - Returned for get operation
            returned: on success
            type: str
            sample: system_name_example
        id:
            description:
                - The unique identifier (OCID) of the environment family. Can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.
            returned: on success
            type: str
            sample: display_name_example
        family_maintenance_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                quarterly_upgrade_begin_times:
                    description:
                        - The quarterly maintenance month group schedule of the Fusion environment family.
                    returned: on success
                    type: str
                    sample: quarterly_upgrade_begin_times_example
                is_monthly_patching_enabled:
                    description:
                        - When True, monthly patching is enabled for the environment family.
                    returned: on success
                    type: bool
                    sample: true
                concurrent_maintenance:
                    description:
                        - Option to upgrade both production and non-production environments at the same time. When set to PROD both types of environnments are
                          upgraded on the production schedule. When set to NON_PROD both types of environments are upgraded on the non-production schedule.
                    returned: on success
                    type: str
                    sample: PROD
        compartment_id:
            description:
                - The OCID of the compartment where the environment family is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_ids:
            description:
                - The list of the IDs of the applications subscriptions that are associated with the environment family.
            returned: on success
            type: list
            sample: []
        is_subscription_update_needed:
            description:
                - When set to True, a subscription update is required for the environment family.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the the FusionEnvironmentFamily was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the FusionEnvironmentFamily was updated. An RFC3339 formatted datetime string.
                - Returned for list operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the FusionEnvironmentFamily.
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
    sample: [{
        "system_name": "system_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "family_maintenance_policy": {
            "quarterly_upgrade_begin_times": "quarterly_upgrade_begin_times_example",
            "is_monthly_patching_enabled": true,
            "concurrent_maintenance": "PROD"
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_ids": [],
        "is_subscription_update_needed": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FusionEnvironmentFamilyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_family_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_family,
            fusion_environment_family_id=self.module.params.get(
                "fusion_environment_family_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "fusion_environment_family_id",
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
            self.client.list_fusion_environment_families,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


FusionEnvironmentFamilyFactsHelperCustom = get_custom_class(
    "FusionEnvironmentFamilyFactsHelperCustom"
)


class ResourceFactsHelper(
    FusionEnvironmentFamilyFactsHelperCustom, FusionEnvironmentFamilyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            fusion_environment_family_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIME_CREATED", "DISPLAY_NAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fusion_environment_family",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(fusion_environment_families=result)


if __name__ == "__main__":
    main()
