#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_dns_zone
short_description: Manage a Zone resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Zone resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new zone in the specified compartment. The `compartmentId`
      query parameter is required if the `Content-Type` header for the
      request is `text/dns`.
version_added: "2.9"
author: Oracle (@oracle)
options:
    migration_source:
        description:
            - Discriminator that is used to determine whether to create a new zone (NONE) or to migrate an existing DynECT zone (DYNECT).
        type: str
        choices:
            - "NONE"
            - "DYNECT"
        default: "NONE"
    name:
        description:
            - The name of the zone.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["zone_name"]
    compartment_id:
        description:
            - The OCID of the compartment containing the zone.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "**Example:** `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "**Example:** `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    zone_type:
        description:
            - The type of the zone. Must be either `PRIMARY` or `SECONDARY`.
            - Applicable when migration_source is 'NONE'
        type: str
        choices:
            - "PRIMARY"
            - "SECONDARY"
    external_masters:
        description:
            - External master servers for the zone. `externalMasters` becomes a
              required parameter when the `zoneType` value is `SECONDARY`.
            - This parameter is updatable.
            - Applicable when migration_source is 'NONE'
        type: list
        suboptions:
            address:
                description:
                    - The server's IP address (IPv4 or IPv6).
                    - Required when migration_source is 'NONE'
                type: str
                required: true
            port:
                description:
                    - The server's port. Port value must be a value of 53, otherwise omit
                      the port value.
                    - Applicable when migration_source is 'NONE'
                type: int
            tsig:
                description:
                    - ""
                    - Applicable when migration_source is 'NONE'
                type: dict
                suboptions:
                    name:
                        description:
                            - A domain name identifying the key for a given pair of hosts.
                            - Required when migration_source is 'NONE'
                        type: str
                        required: true
                    secret:
                        description:
                            - A base64 string encoding the binary shared secret.
                            - Required when migration_source is 'NONE'
                        type: str
                        required: true
                    algorithm:
                        description:
                            - "TSIG Algorithms are encoded as domain names, but most consist of only one
                              non-empty label, which is not required to be explicitly absolute.
                              Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
                              hmac-sha512. For more information on these algorithms, see L(RFC 4635,https://tools.ietf.org/html/rfc4635#section-2)."
                            - Required when migration_source is 'NONE'
                        type: str
                        required: true
            tsig_key_id:
                description:
                    - The OCID of the TSIG key.
                    - Applicable when migration_source is 'NONE'
                type: str
    dynect_migration_details:
        description:
            - ""
            - Applicable when migration_source is 'DYNECT'
        type: dict
        suboptions:
            customer_name:
                description:
                    - DynECT customer name the zone belongs to.
                    - Required when migration_source is 'DYNECT'
                type: str
                required: true
            username:
                description:
                    - DynECT API username to perform the migration with.
                    - Required when migration_source is 'DYNECT'
                type: str
                required: true
            password:
                description:
                    - DynECT API password for the provided username.
                    - Required when migration_source is 'DYNECT'
                type: str
                required: true
            http_redirect_replacements:
                description:
                    - A map of fully-qualified domain names (FQDNs) to an array of `MigrationReplacement` objects.
                    - Applicable when migration_source is 'DYNECT'
                type: dict
    zone_name_or_id:
        description:
            - The name or OCID of the target zone.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["zone_id", "id"]
    if_unmodified_since:
        description:
            - The `If-Unmodified-Since` header field makes the request method
              conditional on the selected representation's last modification date being
              earlier than or equal to the date provided in the field-value.  This
              field accomplishes the same purpose as If-Match for cases where the user
              agent does not have an entity-tag for the representation.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the Zone.
            - Use I(state=present) to create or update a Zone.
            - Use I(state=absent) to delete a Zone.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create zone
  oci_dns_zone:
    compartment_id: ocid1.compartment.oc1..
    name: example.com
    zone_type: PRIMARY

- name: Update zone using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_zone:
    freeform_tags: '{''Department'': ''Finance''}'

- name: Update zone
  oci_dns_zone:
    zone_name_or_id: ocid1.zonenameor.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete zone
  oci_dns_zone:
    zone_name_or_id: ocid1.zonenameor.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete zone using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_zone:
    name: example.com
    compartment_id: ocid1.compartment.oc1..
    state: absent

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
                - The type of the zone. Must be either `PRIMARY` or `SECONDARY`.
            returned: on success
            type: string
            sample: PRIMARY
        compartment_id:
            description:
                - The OCID of the compartment containing the zone.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                tsig:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - A domain name identifying the key for a given pair of hosts.
                            returned: on success
                            type: string
                            sample: name_example
                        secret:
                            description:
                                - A base64 string encoding the binary shared secret.
                            returned: on success
                            type: string
                            sample: secret_example
                        algorithm:
                            description:
                                - "TSIG Algorithms are encoded as domain names, but most consist of only one
                                  non-empty label, which is not required to be explicitly absolute.
                                  Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
                                  hmac-sha512. For more information on these algorithms, see L(RFC 4635,https://tools.ietf.org/html/rfc4635#section-2)."
                            returned: on success
                            type: string
                            sample: algorithm_example
                tsig_key_id:
                    description:
                        - The OCID of the TSIG key.
                    returned: on success
                    type: string
                    sample: ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - "The date and time the resource was created in \\"YYYY-MM-ddThh:mmZ\\" format
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
    sample: {
        "name": "name_example",
        "zone_type": "PRIMARY",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "external_masters": [{
            "address": "address_example",
            "port": 56,
            "tsig": {
                "name": "name_example",
                "secret": "secret_example",
                "algorithm": "algorithm_example"
            },
            "tsig_key_id": "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "self_uri": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "serial": 56,
        "lifecycle_state": "ACTIVE",
        "nameservers": [{
            "hostname": "hostname_example"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient
    from oci.dns.models import CreateZoneBaseDetails
    from oci.dns.models import UpdateZoneDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ZoneHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "zone_name_or_id"

    def get_module_resource_id(self):
        return self.module.params.get("zone_name_or_id")

    def get_get_fn(self):
        return self.client.get_zone

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_zone,
            zone_name_or_id=self.module.params.get("zone_name_or_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "zone_type"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_zones, **kwargs)

    def get_create_model_class(self):
        return CreateZoneBaseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_zone,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_zone_details=create_details,
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateZoneDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_zone,
            call_fn_args=(),
            call_fn_kwargs=dict(
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                update_zone_details=update_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_zone,
            call_fn_args=(),
            call_fn_kwargs=dict(
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ZoneHelperCustom = get_custom_class("ZoneHelperCustom")


class ResourceHelper(ZoneHelperCustom, ZoneHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            migration_source=dict(
                type="str", default="NONE", choices=["NONE", "DYNECT"]
            ),
            name=dict(aliases=["zone_name"], type="str"),
            compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            zone_type=dict(type="str", choices=["PRIMARY", "SECONDARY"]),
            external_masters=dict(
                type="list",
                elements="dict",
                options=dict(
                    address=dict(type="str", required=True),
                    port=dict(type="int"),
                    tsig=dict(
                        type="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            secret=dict(type="str", required=True),
                            algorithm=dict(type="str", required=True),
                        ),
                    ),
                    tsig_key_id=dict(type="str"),
                ),
            ),
            dynect_migration_details=dict(
                type="dict",
                options=dict(
                    customer_name=dict(type="str", required=True),
                    username=dict(type="str", required=True),
                    password=dict(type="str", required=True, no_log=True),
                    http_redirect_replacements=dict(type="dict"),
                ),
            ),
            zone_name_or_id=dict(aliases=["zone_id", "id"], type="str"),
            if_unmodified_since=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
