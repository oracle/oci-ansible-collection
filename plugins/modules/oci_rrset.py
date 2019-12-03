#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_rrset
short_description: Update, Patch or Delete a collection of DNS records of the same domain and type in the specified
                   zone in OCI DNS Service
description:
    - This module allows the user to update, patch or delete a collection of DNS records of the same domain and type in
      the specified DNS zone in OCI DNS Service.
version_added: "2.5"
options:
    zone_id:
        description: The OCID of the target zone. Either I(name) or I(zone_id) must be specified to update or patch
                     the collection of records in the specified zone.
        required: false
        aliases: ['id']
    name:
        description: The name of the zone. Required to create a zone. Either I(name) or I(zone_id) must be specified
                     to update or patch the collection of records in the specified zone.
        required: false
        aliases: ['zone_name']
    compartment_id:
        description: The OCID of the compartment the resource belongs to.
        required: false
    domain:
        description: The target fully-qualified domain name (FQDN) within the target zone.
        required: true
    rtype:
        description: The type of the target RRSet within the target zone.
        required: true
    update_items:
        description: The items to update the RRSet collection to. Replaces records in the specified
                     zone at a domain with the records specified in the request body. If a specified record does not
                     exist, it will be created. If the record exists, then it will be updated to represent the record
                     in the body of the request. If a record in the zone does not exist in the request body, the record
                     will be removed from the zone. Required to update a RRSet.
        required: false
        suboptions:
            domain:
                description: The fully qualified domain name where the record can be located.
                required: true
            record_hash:
                description: A unique identifier for the record within its zone.
                required: false
            is_protected:
                description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                             managed.
                required: false
            rdata:
                description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
                required: true
            rr_set_version:
                description: The latest version of the record's zone in which its RRSet differs from the preceding
                             version.
                required: false
            rtype:
                description: The canonical name for the record's type, such as A or CNAME. For more information, see
                             L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
                required: true
            ttl:
                description: The Time To Live for the record, in seconds.
                required: true
    patch_items:
        description: The record operations to patch the RRSet collection. Updates records in the
                     specified zone at a domain. You can update one record or all records for the specified zone
                     depending on the changes provided in the request body. You can also add or remove records
                     using this option. Required to patch a RRSet.
        required: false
        suboptions:
            domain:
                description: The fully qualified domain name where the record can be located.
                required: false
            record_hash:
                description: A unique identifier for the record within its zone.
                required: false
            is_protected:
                description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                             managed.
                required: false
            rdata:
                description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
                required: false
            rr_set_version:
                description: The latest version of the record's zone in which its RRSet differs from the preceding
                             version.
                required: false
            rtype:
                description: The canonical name for the record's type, such as A or CNAME. For more information, see
                             L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
                required: false
            ttl:
                description: The Time To Live for the record, in seconds.
                required: true
            operation:
                description: A description of how a record relates to a PATCH operation. REQUIRE indicates a
                             precondition that record data must already exist. PROHIBIT indicates a precondition that
                             record data must not already exist. ADD indicates that record data must exist after
                             successful application. REMOVE indicates that record data must not exist after successful
                             application. Note - ADD and REMOVE operations can succeed even if they require no changes
                             when applied, such as when the described records are already present or absent.
                             Note - ADD and REMOVE operations can describe changes for more than one record.
                             Example - { "domain" - "www.example.com", "rtype" - "AAAA", "ttl" - 60 } specifies a new TTL
                             for every record in the www.example.com AAAA RRSet.'
                required: false
                choices: ['REQUIRE', 'PROHIBIT', 'ADD', 'REMOVE']
    state:
        description: State of the RRSet. Use I(state='absent') to delete all records in the specified RRSet.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Update a RRSet by adding a new record. This operation replaces DNS records in the specified RRSet with the
        specified records. So ensure that you include the original RRSet records, if you want to retain existing
        records.
  oci_rrset:
    name: "test_zone_1.com"
    domain: "test_zone_1.com"
    rtype: 'TXT'
    update_items: [ <original zone's TXT records...> , { domain: "test_zone_1.com", ttl: 30, rtype='TXT',
                    rdata='some textual data' } ]

- name: Patch a RRSet
  oci_rrset:
    name: test_zone1.com
    domain: "test_zone_1.com"
    rtype: "TXT"
    patch_items: [{
                    domain: "test_zone_1.com",
                    is_protected: false,
                    rdata: "some textual data",
                    rtype: "TXT",
                    ttl: 30,
                    operation: "REMOVE"
                    }]
"""

RETURN = """
rrset:
    description: Information about all the DNS records in the RRSet
    returned: On successful update or patch of the RRSet
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
            sample: 722af089872ffe65ba909fc8fea1867e
        is_protected:
            description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                         managed.
            returned: always
            type: boolean
            sample: false
        rdata:
            description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
            returned: always
            type: string
            sample: "ns3.p68.dns.oraclecloud.net."
        rrsetVersion:
            description: The latest version of the record's zone in which its RRSet differs from the preceding version.
            returned: always
            type: string
            sample: "5"
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

try:
    from oci.dns.dns_client import DnsClient
    from oci.dns.models import (
        PatchRRSetDetails,
        RecordOperation,
        RecordDetails,
        UpdateRRSetDetails,
    )
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "rrset"


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


def create_model(model_class, user_values):
    model_instance = model_class()
    for attr in model_instance.attribute_map.keys():
        if attr in user_values:
            setattr(model_instance, attr, user_values[attr])
    return model_instance


def modify_rrset(dns_client, module, modify_operation, modify_kwargs):
    result = {}
    try:
        # get current rrset
        rrset_old = oci_utils.call_with_backoff(
            dns_client.get_rr_set,
            zone_name_or_id=get_zone_name_or_id(module),
            domain=module.params["domain"],
            rtype=module.params["rtype"],
        ).data.items

        # update rrset
        updated_rec_coll = oci_utils.call_with_backoff(
            modify_operation, **modify_kwargs
        ).data
        result[RESOURCE_NAME] = oci_utils.to_dict(updated_rec_coll.items)

        # get rrset after update
        rrset_new = oci_utils.call_with_backoff(
            dns_client.get_rr_set,
            zone_name_or_id=get_zone_name_or_id(module),
            domain=module.params["domain"],
            rtype=module.params["rtype"],
        ).data.items

        # check if there is any change between the old and the new rrsets, and set changed accordingly
        result["changed"] = not oci_utils.are_lists_equal(rrset_old, rrset_new)
    except ServiceError as ex:
        module.fail_json(msg=str(ex))
    return result


def patch_rrset(dns_client, module):
    patch_items = module.params["patch_items"]
    patch_rr_set_details = PatchRRSetDetails()
    patch_rr_set_details.items = [
        create_model(RecordOperation, item) for item in patch_items
    ]
    kwargs = {
        "patch_rr_set_details": patch_rr_set_details,
        "zone_name_or_id": get_zone_name_or_id(module),
        "domain": module.params["domain"],
        "rtype": module.params["rtype"],
    }
    return modify_rrset(
        dns_client,
        module,
        modify_operation=dns_client.patch_rr_set,
        modify_kwargs=kwargs,
    )


def update_rrset(dns_client, module):
    update_items = module.params["update_items"]
    update_rr_set_details = UpdateRRSetDetails()
    update_rr_set_details.items = [
        create_model(RecordDetails, item) for item in update_items
    ]
    kwargs = {
        "update_rr_set_details": update_rr_set_details,
        "zone_name_or_id": get_zone_name_or_id(module),
        "domain": module.params["domain"],
        "rtype": module.params["rtype"],
    }
    return modify_rrset(
        dns_client,
        module,
        modify_operation=dns_client.update_rr_set,
        modify_kwargs=kwargs,
    )


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            zone_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False, aliases=["zone_name"]),
            domain=dict(type="str", required=True),
            rtype=dict(type="str", required=True),
            update_items=dict(type="list", required=False),
            patch_items=dict(type="list", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
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

    state = module.params["state"]
    result = {}
    if state == "absent":
        kwargs = {
            "zone_name_or_id": get_zone_name_or_id(module),
            "domain": module.params["domain"],
            "rtype": module.params["rtype"],
        }
        curr_rr_set = dns_client.get_rr_set(**kwargs).data.items
        if curr_rr_set:
            oci_utils.call_with_backoff(dns_client.delete_rr_set, **kwargs)
            result["changed"] = True
        # XXX: delete_and wait requires the resource to have a lifecycle_state and
        # rr_set doesn't have one.
        # result = oci_utils.delete_and_wait(resource_type=RESOURCE_NAME,
        #                                    client=dns_client,
        #                                    get_fn=dns_client.get_rr_set,
        #                                    kwargs_get=kwargs,
        #                                    delete_fn=dns_client.delete_rr_set,
        #                                    kwargs_delete=kwargs,
        #                                    module=module)
    else:
        if module.params["update_items"] is not None:
            result = update_rrset(dns_client, module)
        else:
            result = patch_rrset(dns_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
