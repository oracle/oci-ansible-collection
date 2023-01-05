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
module: oci_bastion_facts
short_description: Fetches details about one or multiple Bastion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Bastion resources in Oracle Cloud Infrastructure
    - Retrieves a list of BastionSummary objects in a compartment. Bastions provide secured, public access to target resources in the cloud that you cannot
      otherwise reach from the internet.
    - If I(bastion_id) is specified, the details of a single Bastion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment in which to list resources.
            - Required to list multiple bastions.
        type: str
    bastion_lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    bastion_id:
        description:
            - The unique identifier (OCID) of the bastion.
            - Required to get a specific bastion.
        type: str
        aliases: ["id"]
    name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending. If no
              value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific bastion
  oci_bastion_facts:
    # required
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"

- name: List bastions
  oci_bastion_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    bastion_lifecycle_state: CREATING
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
bastions:
    description:
        - List of Bastion resources
    returned: on success
    type: complex
    contains:
        phone_book_entry:
            description:
                - The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.
                - Returned for get operation
            returned: on success
            type: str
            sample: phone_book_entry_example
        client_cidr_block_allow_list:
            description:
                - A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        static_jump_host_ip_addresses:
            description:
                - A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        private_endpoint_ip_address:
            description:
                - The private IP address of the created private endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: private_endpoint_ip_address_example
        max_session_ttl_in_seconds:
            description:
                - The maximum amount of time that any session on the bastion can remain active.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        max_sessions_allowed:
            description:
                - The maximum number of active sessions allowed on the bastion.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        bastion_type:
            description:
                - The type of bastion.
            returned: on success
            type: str
            sample: bastion_type_example
        id:
            description:
                - The unique identifier (OCID) of the bastion, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the bastion, which can't be changed after creation.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The unique identifier (OCID) of the compartment where the bastion is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        target_vcn_id:
            description:
                - The unique identifier (OCID) of the virtual cloud network (VCN) that the bastion connects to.
            returned: on success
            type: str
            sample: "ocid1.targetvcn.oc1..xxxxxxEXAMPLExxxxxx"
        target_subnet_id:
            description:
                - The unique identifier (OCID) of the subnet that the bastion connects to.
            returned: on success
            type: str
            sample: "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        dns_proxy_status:
            description:
                - The current dns proxy status of the bastion.
            returned: on success
            type: str
            sample: DISABLED
        time_created:
            description:
                - "The time the bastion was created. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the bastion was updated. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the bastion.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
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
        "phone_book_entry": "phone_book_entry_example",
        "client_cidr_block_allow_list": [],
        "static_jump_host_ip_addresses": [],
        "private_endpoint_ip_address": "private_endpoint_ip_address_example",
        "max_session_ttl_in_seconds": 56,
        "max_sessions_allowed": 56,
        "bastion_type": "bastion_type_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_vcn_id": "ocid1.targetvcn.oc1..xxxxxxEXAMPLExxxxxx",
        "target_subnet_id": "ocid1.targetsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "dns_proxy_status": "DISABLED",
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
    from oci.bastion import BastionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BastionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "bastion_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bastion, bastion_id=self.module.params.get("bastion_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "bastion_lifecycle_state",
            "bastion_id",
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_bastions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BastionFactsHelperCustom = get_custom_class("BastionFactsHelperCustom")


class ResourceFactsHelper(BastionFactsHelperCustom, BastionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            bastion_lifecycle_state=dict(
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
            bastion_id=dict(aliases=["id"], type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bastion",
        service_client_class=BastionClient,
        namespace="bastion",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bastions=result)


if __name__ == "__main__":
    main()
