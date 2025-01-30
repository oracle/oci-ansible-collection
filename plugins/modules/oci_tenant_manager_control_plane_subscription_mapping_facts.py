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
module: oci_tenant_manager_control_plane_subscription_mapping_facts
short_description: Fetches details about one or multiple SubscriptionMapping resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SubscriptionMapping resources in Oracle Cloud Infrastructure
    - Lists the subscription mappings for all the subscriptions owned by a given compartmentId. Only the root compartment is allowed.
    - If I(subscription_mapping_id) is specified, the details of a single SubscriptionMapping will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subscription_id:
        description:
            - OCID of the subscription.
            - Required to list multiple subscription_mappings.
        type: str
    subscription_mapping_id:
        description:
            - OCID of the subscriptionMappingId.
            - Required to get a specific subscription_mapping.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - The lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort by. Only one sort order can be provided.
              * The default order for timeCreated is descending.
              * The default order for displayName is ascending.
              * If no value is specified, timeCreated is the default."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific subscription_mapping
  oci_tenant_manager_control_plane_subscription_mapping_facts:
    # required
    subscription_mapping_id: "ocid1.subscriptionmapping.oc1..xxxxxxEXAMPLExxxxxx"

- name: List subscription_mappings
  oci_tenant_manager_control_plane_subscription_mapping_facts:
    # required
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    subscription_mapping_id: "ocid1.subscriptionmapping.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
subscription_mappings:
    description:
        - List of SubscriptionMapping resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the mapping between subscription and compartment identified by the tenancy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_id:
            description:
                - OCID of the subscription.
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the compartment. Always a tenancy OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_explicitly_assigned:
            description:
                - Denotes if the subscription is explicity assigned to the root compartment or tenancy.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - Lifecycle state of the subscriptionMapping.
            returned: on success
            type: str
            sample: CREATING
        time_terminated:
            description:
                - Date-time when subscription mapping was terminated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - Date-time when subscription mapping was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when subscription mapping was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_explicitly_assigned": true,
        "lifecycle_state": "CREATING",
        "time_terminated": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import SubscriptionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionMappingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "subscription_mapping_id",
        ]

    def get_required_params_for_list(self):
        return [
            "subscription_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription_mapping,
            subscription_mapping_id=self.module.params.get("subscription_mapping_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "subscription_mapping_id",
            "compartment_id",
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
            self.client.list_subscription_mappings,
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


SubscriptionMappingFactsHelperCustom = get_custom_class(
    "SubscriptionMappingFactsHelperCustom"
)


class ResourceFactsHelper(
    SubscriptionMappingFactsHelperCustom, SubscriptionMappingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            subscription_id=dict(type="str"),
            subscription_mapping_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscription_mapping",
        service_client_class=SubscriptionClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(subscription_mappings=result)


if __name__ == "__main__":
    main()
