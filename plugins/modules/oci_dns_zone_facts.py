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
module: oci_dns_zone_facts
short_description: Fetches details about one or multiple Zone resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Zone resources in Oracle Cloud Infrastructure
    - Gets a list of all zones in the specified compartment.
    - The collection can be filtered by name, time created, scope, associated view, and zone type.
      Filtering by view is only supported for private zones.
    - If I(zone_name_or_id) is specified, the details of a single Zone will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    zone_name_or_id:
        description:
            - The name or OCID of the target zone.
            - Required to get a specific zone.
        type: str
        aliases: ["zone_id", "id"]
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment the zone belongs to.
            - This parameter is deprecated and should be omitted.
            - Required to list multiple zones.
        type: str
    name:
        description:
            - A case-sensitive filter for zone names.
              Will match any zone with a name that equals the provided value.
        type: str
        aliases: ["zone_name"]
    name_contains:
        description:
            - Search by zone name.
              Will match any zone whose name (case-insensitive) contains the provided value.
        type: str
    zone_type:
        description:
            - Search by zone type, `PRIMARY` or `SECONDARY`.
              Will match any zone whose type equals the provided value.
        type: str
        choices:
            - "PRIMARY"
            - "SECONDARY"
    time_created_greater_than_or_equal_to:
        description:
            - An L(RFC 3339,https://www.ietf.org/rfc/rfc3339.txt) timestamp that states
              all returned resources were created on or after the indicated time.
        type: str
    time_created_less_than:
        description:
            - An L(RFC 3339,https://www.ietf.org/rfc/rfc3339.txt) timestamp that states
              all returned resources were created before the indicated time.
        type: str
    lifecycle_state:
        description:
            - The state of a resource.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETED"
            - "DELETING"
            - "FAILED"
            - "UPDATING"
    sort_by:
        description:
            - The field by which to sort zones.
        type: str
        choices:
            - "name"
            - "zoneType"
            - "timeCreated"
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
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
    tsig_key_id:
        description:
            - Search for zones that are associated with a TSIG key.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific zone
  oci_dns_zone_facts:
    # required
    zone_name_or_id: "ocid1.zonenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    if_modified_since: if_modified_since_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    scope: GLOBAL
    view_id: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"

- name: List zones
  oci_dns_zone_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    name_contains: name_contains_example
    zone_type: PRIMARY
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00
    lifecycle_state: ACTIVE
    sort_by: name
    sort_order: ASC
    scope: GLOBAL
    view_id: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"
    tsig_key_id: "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
zones:
    description:
        - List of Zone resources
    returned: on success
    type: complex
    contains:
        external_masters:
            description:
                - External master servers for the zone. `externalMasters` becomes a
                  required parameter when the `zoneType` value is `SECONDARY`.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                address:
                    description:
                        - The server's IP address (IPv4 or IPv6).
                    returned: on success
                    type: str
                    sample: address_example
                port:
                    description:
                        - The server's port. Port value must be a value of 53, otherwise omit
                          the port value.
                    returned: on success
                    type: int
                    sample: 56
                tsig_key_id:
                    description:
                        - The OCID of the TSIG key.
                    returned: on success
                    type: str
                    sample: "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        external_downstreams:
            description:
                - External secondary servers for the zone.
                  This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                address:
                    description:
                        - The server's IP address (IPv4 or IPv6).
                    returned: on success
                    type: str
                    sample: address_example
                port:
                    description:
                        - The server's port. Port value must be a value of 53, otherwise omit
                          the port value.
                    returned: on success
                    type: int
                    sample: 56
                tsig_key_id:
                    description:
                        - The OCID of the TSIG key.
                          A TSIG key is used to secure DNS messages (in this case, zone transfers) between two systems that both have the (shared) secret.
                    returned: on success
                    type: str
                    sample: "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        nameservers:
            description:
                - The authoritative nameservers for the zone.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The hostname of the nameserver.
                    returned: on success
                    type: str
                    sample: hostname_example
        zone_transfer_servers:
            description:
                - The OCI nameservers that transfer the zone data with external nameservers.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                address:
                    description:
                        - The server's IP address (IPv4 or IPv6).
                    returned: on success
                    type: str
                    sample: address_example
                port:
                    description:
                        - The server's port.
                    returned: on success
                    type: int
                    sample: 56
                is_transfer_source:
                    description:
                        - A Boolean flag indicating whether or not the server is a zone data transfer source.
                    returned: on success
                    type: bool
                    sample: true
                is_transfer_destination:
                    description:
                        - A Boolean flag indicating whether or not the server is a zone data transfer destination.
                    returned: on success
                    type: bool
                    sample: true
        name:
            description:
                - The name of the zone.
            returned: on success
            type: str
            sample: name_example
        zone_type:
            description:
                - The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.
            returned: on success
            type: str
            sample: PRIMARY
        compartment_id:
            description:
                - The OCID of the compartment containing the zone.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        view_id:
            description:
                - The OCID of the private view containing the zone. This value will
                  be null for zones in the global DNS, which are publicly resolvable and
                  not part of a private view.
            returned: on success
            type: str
            sample: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"
        scope:
            description:
                - The scope of the zone.
            returned: on success
            type: str
            sample: GLOBAL
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        self_uri:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: str
            sample: _self_example
        id:
            description:
                - The OCID of the zone.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created in \\"YYYY-MM-ddThh:mm:ssZ\\" format
                  with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - Version is the never-repeating, totally-orderable, version of the
                  zone, from which the serial field of the zone's SOA record is
                  derived.
            returned: on success
            type: str
            sample: version_example
        serial:
            description:
                - The current serial of the zone. As seen in the zone's SOA record.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the zone resource.
            returned: on success
            type: str
            sample: ACTIVE
        is_protected:
            description:
                - A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "external_masters": [{
            "address": "address_example",
            "port": 56,
            "tsig_key_id": "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "external_downstreams": [{
            "address": "address_example",
            "port": 56,
            "tsig_key_id": "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "nameservers": [{
            "hostname": "hostname_example"
        }],
        "zone_transfer_servers": [{
            "address": "address_example",
            "port": 56,
            "is_transfer_source": true,
            "is_transfer_destination": true
        }],
        "name": "name_example",
        "zone_type": "PRIMARY",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "view_id": "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx",
        "scope": "GLOBAL",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "self_uri": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "serial": 56,
        "lifecycle_state": "ACTIVE",
        "is_protected": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ZoneFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "zone_name_or_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
            "scope",
            "view_id",
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_zone,
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "name_contains",
            "zone_type",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope",
            "view_id",
            "tsig_key_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_zones,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ZoneFactsHelperCustom = get_custom_class("ZoneFactsHelperCustom")


class ResourceFactsHelper(ZoneFactsHelperCustom, ZoneFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            zone_name_or_id=dict(aliases=["zone_id", "id"], type="str"),
            if_modified_since=dict(type="str"),
            compartment_id=dict(type="str"),
            name=dict(aliases=["zone_name"], type="str"),
            name_contains=dict(type="str"),
            zone_type=dict(type="str", choices=["PRIMARY", "SECONDARY"]),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "DELETED",
                    "DELETING",
                    "FAILED",
                    "UPDATING",
                ],
            ),
            sort_by=dict(type="str", choices=["name", "zoneType", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            view_id=dict(type="str"),
            tsig_key_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="zone",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(zones=result)


if __name__ == "__main__":
    main()
