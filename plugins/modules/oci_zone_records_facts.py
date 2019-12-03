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
module: oci_zone_records_facts
short_description: Retrieve facts of records in a specified zone in Oracle Cloud Infrastructure DNS Service
description:
    - This module retrieves information of records in a specified zone. The results are sorted by domain in
      alphabetical order by default. For more information about records, please see
      L(Resource Record (RR) TYPEs, https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment the resource belongs to. Use I(zone_id) or I(zone_name)
                     to retrieve a specific zone's information using its OCID.
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
    zone_version:
        description: The version of the zone for which data is requested.
        required: false
    domain:
        description: Search by domain. Will match any record whose domain (case-insensitive) equals the
                     provided value.
        required: false
    domain_contains:
        description: Search by domain. Will match any record whose domain (case-insensitive) contains the provided
                     value.
        required: false
    rtype:
        description: Search by record type. Will match any record whose type (case-insensitive) equals the provided
                     value.
        required: false
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get a list of zone records in the specified zone
  oci_zone_records_facts:
    zone_id: ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx

- name: Get a list of zone records in a zone for a specific domain
  oci_zone_records_facts:
    zone_id: ocid1.dns-zone.oc1..xxxxxEXAMPLExxxxx
    domain: test_zone_1.com

- name: Gets a list of NS records in a specific zone
  oci_zone_records_facts:
    name: test_zone_1.com
    rtype: NS
"""

RETURN = """
zone_records:
    description: A collection of DNS resource record objects.
    returned: always
    type: complex
    contains:
        domain:
            description: The fully qualified domain name where the record can be located.
            returned: always
            type: string
            sample: "test_zone_1.com"
        record_hash:
            description: A unique identifier for the record within its zone.
            returned: always
            type: string
            sample: "f439fa9a087ff74757485953fe0a8c7d"
        is_protected:
            description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                         managed.
            returned: always
            type: boolean
            sample: true
        rdata:
            description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
            returned: always
            type: string
            sample: "ns1.p68.dns.oraclecloud.net. hostmaster.test_zone_1.com. 1 3600 600 604800 1800"
        rrset_version:
            description: The latest version of the record's zone in which its RRSet differs from the preceding version.
            returned: always
            type: string
            sample: "1"
        rtype:
            description: The canonical name for the record's type, such as A or CNAME. For more information, see
                         L(Resource Record (RR) TYPEs, https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
            returned: always
            type: string
            sample: "NS"
        ttl:
            description: The Time To Live for the record, in seconds.
            returned: always
            type: string
            sample: "86400"
    sample:
                {
                    "domain": "test_zone_1.com",
                    "is_protected": true,
                    "rdata": "ns2.p68.dns.oraclecloud.net.",
                    "record_hash": "9be3279d81b5e8430fd94c70cfa5f0a8",
                    "rrset_version": "1",
                    "rtype": "NS",
                    "ttl": 86400
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

from ansible.module_utils import six

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
    if module.params["name"] is not None:
        return module.params["name"]
    if module.params["zone_id"] is not None:
        return module.params["zone_id"]
    if module.params["id"] is not None:
        return module.params["id"]
    return None


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            zone_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False, aliases=["zone_name"]),
            compartment_id=dict(type="str", required=False),
            zone_version=dict(type="str", required=False),
            domain=dict(type="str", required=False),
            domain_contains=dict(type="str", required=False),
            rtype=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["zone_id", "name"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    dns_client = oci_utils.create_service_client(module, DnsClient)

    try:
        zone_name_or_id = get_zone_name_or_id(module)
        key_list = [
            "compartment_id",
            "zone_version",
            "domain",
            "domain_contains",
            "rtype",
        ]
        kwargs = dict(
            (k, v)
            for (k, v) in six.iteritems(module.params)
            if k in key_list and v is not None
        )

        result = to_dict(
            oci_utils.list_all_resources(
                dns_client.get_zone_records, zone_name_or_id=zone_name_or_id, **kwargs
            ).items
        )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(zone_records=result)


if __name__ == "__main__":
    main()
