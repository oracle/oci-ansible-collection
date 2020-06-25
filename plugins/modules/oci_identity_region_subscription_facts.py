#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_identity_region_subscription_facts
short_description: Fetches details about one or multiple RegionSubscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RegionSubscription resources in Oracle Cloud Infrastructure
    - Lists the region subscriptions for the specified tenancy.
version_added: "2.5"
options:
    tenancy_id:
        description:
            - The OCID of the tenancy.
        type: str
        required: true
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List region_subscriptions
  oci_identity_region_subscription_facts:
    tenancy_id: ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
region_subscriptions:
    description:
        - List of RegionSubscription resources
    returned: on success
    type: complex
    contains:
        region_key:
            description:
                - The region's key.
                - "Allowed values are:
                  - `PHX`
                  - `IAD`
                  - `FRA`
                  - `LHR`
                  - `YYZ`
                  - `NRT`
                  - `ICN`"
            returned: on success
            type: string
            sample: region_key_example
        region_name:
            description:
                - The region's name.
                - "Allowed values are:
                  - `ap-seoul-1`
                  - `ap-tokyo-1`
                  - `ca-toronto-1`
                  - `eu-frankurt-1`
                  - `uk-london-1`
                  - `us-ashburn-1`
                  - `us-phoenix-1`"
            returned: on success
            type: string
            sample: region_name_example
        status:
            description:
                - The region subscription status.
            returned: on success
            type: string
            sample: READY
        is_home_region:
            description:
                - Indicates if the region is the home region or not.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "region_key": "region_key_example",
        "region_name": "region_name_example",
        "status": "READY",
        "is_home_region": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RegionSubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "tenancy_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_region_subscriptions,
            tenancy_id=self.module.params.get("tenancy_id"),
            **optional_kwargs
        )


RegionSubscriptionFactsHelperCustom = get_custom_class(
    "RegionSubscriptionFactsHelperCustom"
)


class ResourceFactsHelper(
    RegionSubscriptionFactsHelperCustom, RegionSubscriptionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(tenancy_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="region_subscription",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(region_subscriptions=result)


if __name__ == "__main__":
    main()
