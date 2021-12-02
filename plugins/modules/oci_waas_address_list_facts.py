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
module: oci_waas_address_list_facts
short_description: Fetches details about one or multiple AddressList resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddressList resources in Oracle Cloud Infrastructure
    - Gets a list of address lists that can be used in a WAAS policy.
    - If I(address_list_id) is specified, the details of a single AddressList will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    address_list_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the address list. This number is generated when the address
              list is added to the compartment.
            - Required to get a specific address_list.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the
              compartment is created.
            - Required to list multiple address_lists.
        type: str
    sort_by:
        description:
            - The value by which address lists are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.
        type: str
        choices:
            - "id"
            - "name"
            - "timeCreated"
    sort_order:
        description:
            - The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    name:
        description:
            - Filter address lists using a list of names.
        type: list
        elements: str
    lifecycle_state:
        description:
            - Filter address lists using a list of lifecycle states.
        type: list
        elements: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
    time_created_greater_than_or_equal_to:
        description:
            - A filter that matches address lists created on or after the specified date-time.
        type: str
    time_created_less_than:
        description:
            - A filter that matches address lists created before the specified date-time.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific address_list
  oci_waas_address_list_facts:
    # required
    address_list_id: "ocid1.addresslist.oc1..xxxxxxEXAMPLExxxxxx"

- name: List address_lists
  oci_waas_address_list_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: id
    sort_order: ASC
    name: [ "$p.getValue()" ]
    lifecycle_state: [ "$p.getValue()" ]
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00

"""

RETURN = """
address_lists:
    description:
        - List of AddressList resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the address list.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the address list's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the address list.
            returned: on success
            type: str
            sample: display_name_example
        address_count:
            description:
                - The total number of unique IP addresses in the address list.
            returned: on success
            type: float
            sample: 10
        addresses:
            description:
                - The list of IP addresses or CIDR notations.
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - The current lifecycle state of the address list.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the address list was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2018-11-16T21:10:29Z"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "address_count": 10,
        "addresses": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_state": "CREATING",
        "time_created": "2018-11-16T21:10:29Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddressListFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "address_list_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_address_list,
            address_list_id=self.module.params.get("address_list_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_address_lists,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AddressListFactsHelperCustom = get_custom_class("AddressListFactsHelperCustom")


class ResourceFactsHelper(AddressListFactsHelperCustom, AddressListFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            address_list_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["id", "name", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="list", elements="str"),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                ],
            ),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="address_list",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(address_lists=result)


if __name__ == "__main__":
    main()
