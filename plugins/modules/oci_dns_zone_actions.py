#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_dns_zone_actions
short_description: Perform actions on a Zone resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Zone resource in Oracle Cloud Infrastructure
    - "For I(action=change_compartment), moves a zone into a different compartment. Protected zones cannot have their compartment changed. For private
      zones, the scope query parameter is required with a value of `PRIVATE`. When the zone name is provided as a
      path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.
      **Note:** All SteeringPolicyAttachment objects associated with this zone will also be moved into the provided compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    zone_id:
        description:
            - The OCID of the target zone.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the zone should be moved.
        type: str
        required: true
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    action:
        description:
            - The action to perform on the Zone.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on zone
  oci_dns_zone_actions:
    compartment_id: "ocid1.compartment.oc1.."
    zone_id: "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

"""

RETURN = """
zone:
    description:
        - Details of the Zone resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the zone.
            returned: on success
            type: string
            sample: name_example
        zone_type:
            description:
                - The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.
            returned: on success
            type: string
            sample: PRIMARY
        compartment_id:
            description:
                - The OCID of the compartment containing the zone.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        view_id:
            description:
                - The OCID of the private view containing the zone. This value will
                  be null for zones in the global DNS, which are publicly resolvable and
                  not part of a private view.
            returned: on success
            type: string
            sample: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"
        scope:
            description:
                - The scope of the zone.
            returned: on success
            type: string
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
        external_masters:
            description:
                - External master servers for the zone. `externalMasters` becomes a
                  required parameter when the `zoneType` value is `SECONDARY`.
            returned: on success
            type: complex
            contains:
                address:
                    description:
                        - The server's IP address (IPv4 or IPv6).
                    returned: on success
                    type: string
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
                    type: string
                    sample: "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        self_uri:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: string
            sample: _self_example
        id:
            description:
                - The OCID of the zone.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created in \\"YYYY-MM-ddThh:mm:ssZ\\" format
                  with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        version:
            description:
                - Version is the never-repeating, totally-orderable, version of the
                  zone, from which the serial field of the zone's SOA record is
                  derived.
            returned: on success
            type: string
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
            type: string
            sample: ACTIVE
        is_protected:
            description:
                - A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.
            returned: on success
            type: bool
            sample: true
        nameservers:
            description:
                - The authoritative nameservers for the zone.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The hostname of the nameserver.
                    returned: on success
                    type: string
                    sample: hostname_example
        zone_transfer_servers:
            description:
                - The OCI nameservers that transfer the zone data with external nameservers.
            returned: on success
            type: complex
            contains:
                address:
                    description:
                        - The server's IP address (IPv4 or IPv6).
                    returned: on success
                    type: string
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
    sample: {
        "name": "name_example",
        "zone_type": "PRIMARY",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "view_id": "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx",
        "scope": "GLOBAL",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "external_masters": [{
            "address": "address_example",
            "port": 56,
            "tsig_key_id": "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "self_uri": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "serial": 56,
        "lifecycle_state": "ACTIVE",
        "is_protected": true,
        "nameservers": [{
            "hostname": "hostname_example"
        }],
        "zone_transfer_servers": [{
            "address": "address_example",
            "port": 56,
            "is_transfer_source": true,
            "is_transfer_destination": true
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient
    from oci.dns.models import ChangeZoneCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ZoneActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "zone_id"

    def get_module_resource_id(self):
        return self.module.params.get("zone_id")

    def get_get_fn(self):
        return self.client.get_zone

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_zone,
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeZoneCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_zone_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                zone_id=self.module.params.get("zone_id"),
                change_zone_compartment_details=action_details,
                scope=self.module.params.get("scope"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ZoneActionsHelperCustom = get_custom_class("ZoneActionsHelperCustom")


class ResourceHelper(ZoneActionsHelperCustom, ZoneActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            zone_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="zone",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
