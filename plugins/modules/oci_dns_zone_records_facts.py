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
module: oci_dns_zone_records_facts
short_description: Fetches details about a ZoneRecords resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ZoneRecords resource in Oracle Cloud Infrastructure
    - Gets all records in the specified zone. The results are sorted by `domain` in alphabetical order by default.
      For more information about records, see L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-
      parameters-4).
      For private zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is
      provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query
      parameter is required.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    zone_name_or_id:
        description:
            - The name or OCID of the target zone.
        type: str
        aliases: ["zone_id", "name", "zone_name", "id"]
        required: true
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    zone_version:
        description:
            - The version of the zone for which data is requested.
        type: str
    domain:
        description:
            - Search by domain.
              Will match any record whose domain (case-insensitive) equals the provided value.
        type: str
    domain_contains:
        description:
            - Search by domain.
              Will match any record whose domain (case-insensitive) contains the provided value.
        type: str
    rtype:
        description:
            - Search by record type.
              Will match any record whose L(type,https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4) (case-insensitive)
              equals the provided value.
        type: str
    sort_by:
        description:
            - The field by which to sort records.
        type: str
        choices:
            - "domain"
            - "rtype"
            - "ttl"
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
        type: str
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    view_id:
        description:
            - The OCID of the view the resource is associated with.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific zone_records
  oci_dns_zone_records_facts:
    # required
    zone_name_or_id: "ocid1.zonenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    if_modified_since: if_modified_since_example
    zone_version: zone_version_example
    domain: domain_example
    domain_contains: domain_contains_example
    rtype: rtype_example
    sort_by: domain
    sort_order: ASC
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    scope: GLOBAL
    view_id: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
zone_records:
    description:
        - ZoneRecords resource
    returned: on success
    type: complex
    contains:
        domain:
            description:
                - The fully qualified domain name where the record can be located.
            returned: on success
            type: str
            sample: domain_example
        record_hash:
            description:
                - A unique identifier for the record within its zone.
            returned: on success
            type: str
            sample: record_hash_example
        is_protected:
            description:
                - A Boolean flag indicating whether or not parts of the record
                  are unable to be explicitly managed.
            returned: on success
            type: bool
            sample: true
        rdata:
            description:
                - The record's data, as whitespace-delimited tokens in
                  type-specific presentation format. All RDATA is normalized and the
                  returned presentation of your RDATA may differ from its initial input.
                  For more information about RDATA, see L(Supported DNS Resource Record
                  Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)
            returned: on success
            type: str
            sample: rdata_example
        rrset_version:
            description:
                - The latest version of the record's zone in which its RRSet differs
                  from the preceding version.
            returned: on success
            type: str
            sample: rrset_version_example
        rtype:
            description:
                - The type of DNS record, such as A or CNAME. For more information, see L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-
                  parameters/dns-parameters.xhtml#dns-parameters-4).
            returned: on success
            type: str
            sample: rtype_example
        ttl:
            description:
                - The Time To Live for the record, in seconds.
            returned: on success
            type: int
            sample: 56
    sample: {
        "domain": "domain_example",
        "record_hash": "record_hash_example",
        "is_protected": true,
        "rdata": "rdata_example",
        "rrset_version": "rrset_version_example",
        "rtype": "rtype_example",
        "ttl": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ZoneRecordsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "zone_name_or_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
            "zone_version",
            "domain",
            "domain_contains",
            "rtype",
            "sort_by",
            "sort_order",
            "compartment_id",
            "scope",
            "view_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_zone_records,
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                **optional_kwargs
            ).items
        )


ZoneRecordsFactsHelperCustom = get_custom_class("ZoneRecordsFactsHelperCustom")


class ResourceFactsHelper(ZoneRecordsFactsHelperCustom, ZoneRecordsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            zone_name_or_id=dict(
                aliases=["zone_id", "name", "zone_name", "id"],
                type="str",
                required=True,
            ),
            if_modified_since=dict(type="str"),
            zone_version=dict(type="str"),
            domain=dict(type="str"),
            domain_contains=dict(type="str"),
            rtype=dict(type="str"),
            sort_by=dict(type="str", choices=["domain", "rtype", "ttl"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            compartment_id=dict(type="str"),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            view_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="zone_records",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(zone_records=result)


if __name__ == "__main__":
    main()
