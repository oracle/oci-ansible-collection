#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_cloud_guard_security_zone_facts
short_description: Fetches details about one or multiple SecurityZone resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SecurityZone resources in Oracle Cloud Infrastructure
    - Gets a list of all security zones in a compartment.
    - If I(security_zone_id) is specified, the details of a single SecurityZone will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    security_zone_id:
        description:
            - The unique identifier of the security zone (`SecurityZone`)
            - Required to get a specific security_zone.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple security_zones.
        type: str
    lifecycle_state:
        description:
            - The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    security_recipe_id:
        description:
            - The unique identifier of the security zone recipe (`SecurityRecipe`)
        type: str
    is_required_security_zones_in_subtree:
        description:
            - security zones in the subtree
        type: bool
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
- name: Get a specific security_zone
  oci_cloud_guard_security_zone_facts:
    # required
    security_zone_id: "ocid1.securityzone.oc1..xxxxxxEXAMPLExxxxxx"

- name: List security_zones
  oci_cloud_guard_security_zone_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    security_recipe_id: "ocid1.securityrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    is_required_security_zones_in_subtree: true
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
security_zones:
    description:
        - List of SecurityZone resources
    returned: on success
    type: complex
    contains:
        security_zone_target_id:
            description:
                - The OCID of the target associated with the security zone
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.securityzonetarget.oc1..xxxxxxEXAMPLExxxxxx"
        inherited_by_compartments:
            description:
                - List of inherited compartments
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The security zone's name
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The security zone's description
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment for the security zone
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        security_zone_recipe_id:
            description:
                - The OCID of the recipe (`SecurityRecipe`) for the security zone
            returned: on success
            type: str
            sample: "ocid1.securityzonerecipe.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the security zone was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the security zone was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the security zone
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the
                  `Failed` state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Avoid entering confidential information.
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
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "security_zone_target_id": "ocid1.securityzonetarget.oc1..xxxxxxEXAMPLExxxxxx",
        "inherited_by_compartments": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "security_zone_recipe_id": "ocid1.securityzonerecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.cloud_guard import CloudGuardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecurityZoneFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "security_zone_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_zone,
            security_zone_id=self.module.params.get("security_zone_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "security_recipe_id",
            "is_required_security_zones_in_subtree",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_security_zones,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SecurityZoneFactsHelperCustom = get_custom_class("SecurityZoneFactsHelperCustom")


class ResourceFactsHelper(SecurityZoneFactsHelperCustom, SecurityZoneFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            security_zone_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            security_recipe_id=dict(type="str"),
            is_required_security_zones_in_subtree=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="security_zone",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(security_zones=result)


if __name__ == "__main__":
    main()
