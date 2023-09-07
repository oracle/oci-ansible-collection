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
module: oci_tenant_manager_control_plane_available_region_facts
short_description: Fetches details about one or multiple AvailableRegion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailableRegion resources in Oracle Cloud Infrastructure
    - List the available regions based on subscription ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subscription_id:
        description:
            - OCID of the subscription.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List available_regions
  oci_tenant_manager_control_plane_available_region_facts:
    # required
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
available_regions:
    description:
        - List of AvailableRegion resources
    returned: on success
    type: complex
    contains:
        region_name:
            description:
                - Region availability for the subscription.
            returned: on success
            type: str
            sample: us-phoenix-1
    sample: [{
        "region_name": "us-phoenix-1"
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


class AvailableRegionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "subscription_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_available_regions,
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


AvailableRegionFactsHelperCustom = get_custom_class("AvailableRegionFactsHelperCustom")


class ResourceFactsHelper(
    AvailableRegionFactsHelperCustom, AvailableRegionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(subscription_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="available_region",
        service_client_class=SubscriptionClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(available_regions=result)


if __name__ == "__main__":
    main()
