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
module: oci_lockbox_facts
short_description: Fetches details about one or multiple Lockbox resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Lockbox resources in Oracle Cloud Infrastructure
    - Returns a list of Lockboxes.
    - If I(lockbox_id) is specified, the details of a single Lockbox will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lockbox_id:
        description:
            - unique Lockbox identifier
            - Required to get a specific lockbox.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    resource_id:
        description:
            - The ID of the resource associated with the lockbox.
        type: str
    lockbox_partner:
        description:
            - The name of the lockbox partner.
        type: str
        choices:
            - "FAAAS"
            - "CANARY"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "id"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific lockbox
  oci_lockbox_facts:
    # required
    lockbox_id: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"

- name: List lockboxes
  oci_lockbox_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    display_name: display_name_example
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    lockbox_partner: FAAAS
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
lockboxes:
    description:
        - List of Lockbox resources
    returned: on success
    type: complex
    contains:
        access_context_attributes:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of context attributes.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the context attribute
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The description of the context attribute
                            returned: on success
                            type: str
                            sample: description_example
                        default_value:
                            description:
                                - An optional default value used when access request context value is not provided
                            returned: on success
                            type: str
                            sample: default_value_example
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Lockbox Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        lockbox_partner:
            description:
                - The partner using this lockbox to lock a resource.
            returned: on success
            type: str
            sample: FAAAS
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        partner_compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The unique identifier (OCID) of associated resource that the lockbox is created for.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        approval_template_id:
            description:
                - Approval template ID
            returned: on success
            type: str
            sample: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
        max_access_duration:
            description:
                - The maximum amount of time operator has access to associated resources.
            returned: on success
            type: str
            sample: max_access_duration_example
        time_created:
            description:
                - The time the the Lockbox was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Lockbox was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Lockbox.
            returned: on success
            type: str
            sample: ACTIVE
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "access_context_attributes": {
            "items": [{
                "name": "name_example",
                "description": "description_example",
                "default_value": "default_value_example"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lockbox_partner": "FAAAS",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "partner_compartment_id": "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "approval_template_id": "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx",
        "max_access_duration": "max_access_duration_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.lockbox import LockboxClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LockboxFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "lockbox_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lockbox, lockbox_id=self.module.params.get("lockbox_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "resource_id",
            "lockbox_partner",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_lockboxes, **optional_kwargs
        )


LockboxFactsHelperCustom = get_custom_class("LockboxFactsHelperCustom")


class ResourceFactsHelper(LockboxFactsHelperCustom, LockboxFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            lockbox_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            resource_id=dict(type="str"),
            lockbox_partner=dict(type="str", choices=["FAAAS", "CANARY"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName", "id"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="lockbox",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(lockboxes=result)


if __name__ == "__main__":
    main()
