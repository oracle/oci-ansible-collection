#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_zone
short_description: Manage a Zone in OCI DNS Service
description:
    - This module allows the user to create, update and delete a Zone in OCI DNS Service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the zone. Required to create a zone.
        required: false
    name:
        description: The name of the zone. Required to create a zone. Either I(name) or I(zone_id) must be specified
                     to update or delete a zone.
        required: false
        aliases: ['zone_name']
    zone_id:
        description: The OCID of the target zone. Either I(name) or I(zone_id) must be specified to update or
                     delete a zone.
        required: false
        aliases: ['id']
    zone_type:
        description: The type of the zone. Must be either PRIMARY or SECONDARY. Required to create a zone.
        required: false
        choices: ['PRIMARY', 'SECONDARY']
    external_masters:
        description: External master servers for the Zone
        required: false
        suboptions:
            address:
                description: The server's IP address (IPv4 or IPv6).
                required: true
            port:
                description: The server's port. Port value must be a value of 53, otherwise omit the port value.
                required: false
            tsig:
                description: A L(TSIG, https://tools.ietf.org/html/rfc2845) key.
                required: false
                suboptions:
                    name:
                        description: A domain name identifying the key for a given pair of hosts.
                        required: true
                    secret:
                        description: A base64 string encoding the binary shared secret.
                        required: true
                    algorithm:
                        description: "TSIG Algorithms are encoded as domain names, but most consist of only one
                                     non-empty label, which is not required to be explicitly absolute. Applicable
                                     algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more
                                     information on these algorithms, please see
                                     L(RFC 4635, https://tools.ietf.org/html/rfc4635#section-2)."
                        required: true
    state:
        description: Create or update a zone with I(state=present). Use I(state=absent) to delete a zone.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create a zone
  oci_zone:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: test_zone_1.com
    zone_type: PRIMARY

- name: Update a zone using id
  oci_zone:
    id: ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx
    external_masters: [ { address: "12.123.123.123", tsig: { name: "test_zone_1.com", secret: "XXXX",
                            algorithm: "hmac-sha1" } } ]

- name: Update a zone using name
  oci_zone:
    name: test_zone1.com
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    external_masters: [ { address: "12.123.123.123", tsig: { name: "test_zone_1.com", secret: "XXXX",
                            algorithm: "hmac-sha1" } } ]
- name: Delete a zone
  oci_zone:
    id: ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
zone:
    description: Information about the zone
    returned: On successful create, delete & update operations on zone
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
            sample: { address: "12.123.123.123", tsig: { name: "test_zone_1.com", secret: "XXXX",
                            algorithm: "hmac-sha1" } }
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
    sample: {
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
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.dns.dns_client import DnsClient
    from oci.dns.models import CreateZoneDetails, UpdateZoneDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


# DNS client accepts either a zone name or an id through the zone_name_or_id parameter for update and delete scenarios.
# This is different from other resources.
# XXX: for now only zone_name appears to work, and not OCID. Using an OCID gives an error "Invalid Domain Name".
def get_zone_name_or_id(module):
    if module.params["name"] is not None:
        return module.params["name"]
    if module.params["zone_id"] is not None:
        return module.params["zone_id"]
    if module.params["id"] is not None:
        return module.params["id"]
    return None


def delete_zone(dns_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="zone",
        client=dns_client,
        get_fn=dns_client.get_zone,
        kwargs_get={"zone_name_or_id": get_zone_name_or_id(module)},
        delete_fn=dns_client.delete_zone,
        kwargs_delete={"zone_name_or_id": get_zone_name_or_id(module)},
        module=module,
    )
    return result


def update_zone(dns_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="zone",
        client=dns_client,
        get_fn=dns_client.get_zone,
        kwargs_get={"zone_name_or_id": get_zone_name_or_id(module)},
        update_fn=dns_client.update_zone,
        primitive_params_update=["zone_name_or_id"],
        kwargs_non_primitive_update={UpdateZoneDetails: "update_zone_details"},
        module=module,
        update_attributes=UpdateZoneDetails().attribute_map.keys(),
    )
    return result


# XXX: Importing of a Zone via a zone file in RFC 1035 master file format as exported by BIND (through the Content-Type
# header as `text/dns` as documented in the API?), doesn't appear to be supported in the SDK. It is supported in the
# the console though. Check if this is possible via the SDK
def create_zone(dns_client, module):
    create_zone_details = CreateZoneDetails()
    for attribute in create_zone_details.attribute_map:
        if attribute in module.params:
            setattr(create_zone_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="zone",
        create_fn=dns_client.create_zone,
        kwargs_create={"create_zone_details": create_zone_details},
        client=dns_client,
        get_fn=dns_client.get_zone,
        get_param="zone_name_or_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            name=dict(type="str", required=False, aliases=["zone_name"]),
            zone_id=dict(type="str", required=False, aliases=["id"]),
            zone_type=dict(
                type="str", required=False, choices=["PRIMARY", "SECONDARY"]
            ),
            external_masters=dict(type="list", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("zone_id", "name")],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    dns_client = oci_utils.create_service_client(module, DnsClient)

    state = module.params["state"]
    zone_id = module.params["zone_id"]

    if state == "absent":
        result = delete_zone(dns_client, module)

    else:
        if zone_id is not None:
            module.params["zone_name_or_id"] = get_zone_name_or_id(module)
            result = update_zone(dns_client, module)
            # XXX: also handle case where zone name is specified
        else:
            if module.params["zone_type"] is None:
                module.fail_json(
                    msg="Zone_type must be specified while creating a Zone"
                )
            kwargs_list = {"compartment_id": module.params["compartment_id"]}

            result = oci_utils.check_and_create_resource(
                resource_type="zone",
                create_fn=create_zone,
                kwargs_create={"dns_client": dns_client, "module": module},
                list_fn=dns_client.list_zones,
                kwargs_list=kwargs_list,
                module=module,
                model=CreateZoneDetails(),
                exclude_attributes=None,
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
