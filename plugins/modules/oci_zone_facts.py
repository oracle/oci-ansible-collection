#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_zone_facts
short_description: Retrieve facts of zones in Oracle Cloud Infrastructure DNS Service
description:
    - This module retrieves information of the specified zone or all zones in the specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment the resource belongs to. Use I(zone_id) to retrieve a specific
                     zone's information using its OCID.
        required: false
    zone_id:
        description: OCID of the target zone.
        required: false
        aliases: ['id']
    name:
        description: A case-sensitive filter for zone names. Will match any zone with a name that equals the
                     provided value.
        required: false
        aliases: ['zone_name']
    zone_type:
        description: Search by zone type, PRIMARY or SECONDARY. Will match any zone whose type equals the provided
                     value.
        required: false
        choices: ['PRIMARY', 'SECONDARY']
    name_contains:
        description: Search by zone name. Will match any zone whose name (case-insensitive) contains the provided
                     value.
        required: false
    time_created_greater_than_or_equal_to:
        description: An L(RFC 3339, https://www.ietf.org/rfc/rfc3339.txt) timestamp that states all returned resources
                     were created on or after the indicated time.
        required: false
    time_created_less_than:
        description: An L(RFC 3339, https://www.ietf.org/rfc/rfc3339.txt) timestamp that states all returned resources
                     were before the indicated time.
        required: false
    lifecycle_state:
        description: The state of a resource. Allowed values are "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"
        required: false
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [oracle]
"""

EXAMPLES = """
- name: Get a list of zones in the specified compartment
  oci_zone_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get a zone with the specified name
  oci_zone_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: test_zone_1.com

- name: Get a list of primary zones in the specified compartment
  oci_zone_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    zone_type: "PRIMARY"

- name: Gets details of a specific zone using the OCID of the zone
  oci_zone_facts:
    zone_id: ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
zones:
    description: List of Zone details
    returned: always
    type: complex
    contains:
        name:
            description: The name of the zone.
            returned: always
            type: string
            sample: "test_zone_1.com"
        compartment_id:
            description: The OCID of the compartment containing the Zone.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        zone_type:
            description: The type of the zone. Must be either PRIMARY or SECONDARY.
            returned: always
            type: string
            sample: "PRIMARY"
        external_masters:
            description: External master servers for the zone.
            returned: always
            type: list
            sample: [...]
        self_uri:
            description: The canonical absolute URL of the resource.
            returned: always
            type: string
            sample: "https://dns.us-ashburn-1.oraclecloud.com/20180115/zones/test_zone_1.com"
        id:
            description: The OCID of the zone
            returned: always
            type: string
            sample: ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx
        time_created:
            description: The date and time the resource was created in "YYYY-MM-ddThh:mmZ" format with a Z offset, as
                         defined by RFC 3339.
            returned: always
            type: string
            sample: "2018-08-23T11:36:26+00:00"
        version:
            description: Version is the never-repeating, totally-orderable, version of the zone, from which the serial
                         field of the zone's SOA record is derived.
            returned: always
            type: string
            sample: "1"
        serial:
            description: The current serial of the zone. As seen in the zone's SOA record.
            returned: always
            type: int
            sample: 1
        lifecycle_state:
            description: The current state of the zone resource.
            returned: always
            type: string
            sample: "ACTIVE"
        nameservers:
            description: The authoritative nameservers for the zone.
            returned: optional
            type: list
            sample: [{ hostname: "XXX" }]
    sample: [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                "external_masters": [],
                "id": "ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx",
                "lifecycle_state": "ACTIVE",
                "name": "test_zone_1.com",
                "self_uri": "https://dns.us-ashburn-1.oraclecloud.com/20180115/zones/test_zone_1.com",
                "serial": 1,
                "time_created": "2018-08-23T11:36:26+00:00",
                "version": "1",
                "zone_type": "PRIMARY"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.dns.dns_client import DnsClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


# DNS client accepts either a zone name or an id through the zone_name_or_id parameter for update and delete scenarios.
# This is different from other resources.
def get_zone_name_or_id(module):
    if module.params["name"]:
        return module.params["name"]
    if module.params["zone_id"]:
        return module.params["zone_id"]
    return None


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            zone_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False, aliases=["zone_name"]),
            compartment_id=dict(type="str", required=False),
            zone_type=dict(
                type="str", required=False, choices=["PRIMARY", "SECONDARY"]
            ),
            name_contains=dict(type="str", required=False),
            time_created_greater_than_or_equal_to=dict(type="str", required=False),
            time_created_less_than=dict(type="str", required=False),
            lifecycle_state=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["zone_id", "compartment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    dns_client = oci_utils.create_service_client(module, DnsClient)

    zone_id = module.params["zone_id"]
    compartment_id = module.params["compartment_id"]

    try:
        if zone_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        dns_client.get_zone, zone_name_or_id=get_zone_name_or_id(module)
                    ).data
                )
            ]
        elif compartment_id is not None:
            optional_list_method_params = [
                "compartment_id",
                "name",
                "zone_type",
                "name_contains",
                "time_created_greater_than_or_equal_to",
                "time_created_less_than",
                "lifecycle_state",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            zone_summaries = to_dict(
                oci_utils.list_all_resources(dns_client.list_zones, **optional_kwargs)
            )

            # Get Zone model from zone-summaries returned by `list_zones`
            result = to_dict(
                [
                    oci_utils.call_with_backoff(
                        dns_client.get_zone, zone_name_or_id=z["id"]
                    ).data
                    for z in zone_summaries
                ]
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(zones=result)


if __name__ == "__main__":
    main()
