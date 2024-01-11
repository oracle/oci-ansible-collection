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
module: oci_waf_web_app_firewall_facts
short_description: Fetches details about one or multiple WebAppFirewall resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WebAppFirewall resources in Oracle Cloud Infrastructure
    - Gets a list of all WebAppFirewalls in a compartment.
    - If I(web_app_firewall_id) is specified, the details of a single WebAppFirewall will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    web_app_firewall_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppFirewall.
            - Required to get a specific web_app_firewall.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
            - Required to list multiple web_app_firewalls.
        type: str
    web_app_firewall_policy_id:
        description:
            - A filter to return only the WebAppFirewall with the given L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of
              related WebAppFirewallPolicy.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycleState.
        type: list
        elements: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for timeCreated is descending.
              Default order for displayName is ascending.
              If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific web_app_firewall
  oci_waf_web_app_firewall_facts:
    # required
    web_app_firewall_id: "ocid1.webappfirewall.oc1..xxxxxxEXAMPLExxxxxx"

- name: List web_app_firewalls
  oci_waf_web_app_firewall_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    web_app_firewall_policy_id: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: [ "lifecycle_state_example" ]
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
web_app_firewalls:
    description:
        - List of WebAppFirewall resources
    returned: on success
    type: complex
    contains:
        load_balancer_id:
            description:
                - LoadBalancer L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) to which the WebAppFirewallPolicy is attached to.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppFirewall.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - WebAppFirewall display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        backend_type:
            description:
                - Type of the WebAppFirewall, as example LOAD_BALANCER.
            returned: on success
            type: str
            sample: LOAD_BALANCER
        web_app_firewall_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of WebAppFirewallPolicy, which is attached to the resource.
            returned: on success
            type: str
            sample: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the WebAppFirewall was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the WebAppFirewall was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the WebAppFirewall.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in FAILED state.
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
        "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "backend_type": "LOAD_BALANCER",
        "web_app_firewall_policy_id": "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
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
    from oci.waf import WafClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppFirewallFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "web_app_firewall_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_firewall,
            web_app_firewall_id=self.module.params.get("web_app_firewall_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "web_app_firewall_policy_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_web_app_firewalls,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


WebAppFirewallFactsHelperCustom = get_custom_class("WebAppFirewallFactsHelperCustom")


class ResourceFactsHelper(
    WebAppFirewallFactsHelperCustom, WebAppFirewallFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            web_app_firewall_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            web_app_firewall_policy_id=dict(type="str"),
            lifecycle_state=dict(type="list", elements="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="web_app_firewall",
        service_client_class=WafClient,
        namespace="waf",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(web_app_firewalls=result)


if __name__ == "__main__":
    main()
