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
module: oci_dns_domain_records
short_description: Manage a DomainRecords resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update, patch and delete a DomainRecords resource in Oracle Cloud Infrastructure
    - This module does not support check mode
version_added: "2.9"
author: Oracle (@oracle)
options:
    zone_name_or_id:
        description:
            - The name or OCID of the target zone.
        type: str
        aliases: ["zone_id", "name", "zone_name", "id"]
        required: true
    domain:
        description:
            - The target fully-qualified domain name (FQDN) within the target zone.
        type: str
        required: true
    update_items:
        description:
            - ""
            - This parameter is updatable.
        type: list
        suboptions:
            domain:
                description:
                    - The fully qualified domain name where the record can be located.
                    - This parameter is updatable.
                type: str
                required: true
            record_hash:
                description:
                    - A unique identifier for the record within its zone.
                    - This parameter is updatable.
                type: str
            is_protected:
                description:
                    - A Boolean flag indicating whether or not parts of the record
                      are unable to be explicitly managed.
                    - This parameter is updatable.
                type: bool
            rdata:
                description:
                    - The record's data, as whitespace-delimited tokens in
                      type-specific presentation format. All RDATA is normalized and the
                      returned presentation of your RDATA may differ from its initial input.
                      For more information about RDATA, see L(Supported DNS Resource Record
                      Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)
                    - This parameter is updatable.
                type: str
                required: true
            rrset_version:
                description:
                    - The latest version of the record's zone in which its RRSet differs
                      from the preceding version.
                    - This parameter is updatable.
                type: str
            rtype:
                description:
                    - The type of DNS record, such as A or CNAME. For more information, see L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-
                      parameters/dns-parameters.xhtml#dns-parameters-4).
                    - This parameter is updatable.
                type: str
                required: true
            ttl:
                description:
                    - The Time To Live for the record, in seconds.
                    - This parameter is updatable.
                type: int
                required: true
    if_unmodified_since:
        description:
            - The `If-Unmodified-Since` header field makes the request method
              conditional on the selected representation's last modification date being
              earlier than or equal to the date provided in the field-value.  This
              field accomplishes the same purpose as If-Match for cases where the user
              agent does not have an entity-tag for the representation.
            - This parameter is updatable.
        type: str
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
            - This parameter is updatable.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    view_id:
        description:
            - The OCID of the view the resource is associated with.
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - This parameter is updatable.
        type: str
    patch_items:
        description:
            - ""
        type: list
        suboptions:
            domain:
                description:
                    - The fully qualified domain name where the record can be located.
                type: str
            record_hash:
                description:
                    - A unique identifier for the record within its zone.
                type: str
            is_protected:
                description:
                    - A Boolean flag indicating whether or not parts of the record
                      are unable to be explicitly managed.
                type: bool
            rdata:
                description:
                    - The record's data, as whitespace-delimited tokens in
                      type-specific presentation format. All RDATA is normalized and the
                      returned presentation of your RDATA may differ from its initial input.
                      For more information about RDATA, see L(Supported DNS Resource Record
                      Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm)
                type: str
            rrset_version:
                description:
                    - The latest version of the record's zone in which its RRSet differs
                      from the preceding version.
                type: str
            rtype:
                description:
                    - The type of DNS record, such as A or CNAME. For more information, see L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-
                      parameters/dns-parameters.xhtml#dns-parameters-4).
                type: str
            ttl:
                description:
                    - The Time To Live for the record, in seconds.
                type: int
            operation:
                description:
                    - A description of how a record relates to a PATCH operation.
                    - "- `REQUIRE` indicates a precondition that record data **must** already exist.
                      - `PROHIBIT` indicates a precondition that record data **must not** already exist.
                      - `ADD` indicates that record data **must** exist after successful application.
                      - `REMOVE` indicates that record data **must not** exist after successful application."
                    - " **Note:** `ADD` and `REMOVE` operations can succeed even if
                        they require no changes when applied, such as when the described
                        records are already present or absent."
                    - " **Note:** `ADD` and `REMOVE` operations can describe changes for
                        more than one record."
                    - " **Example:** `{ \\"domain\\": \\"www.example.com\\", \\"rtype\\": \\"AAAA\\", \\"ttl\\": 60 }`
                        specifies a new TTL for every record in the www.example.com AAAA RRSet."
                type: str
                choices:
                    - "REQUIRE"
                    - "PROHIBIT"
                    - "ADD"
                    - "REMOVE"
    state:
        description:
            - The state of the DomainRecords.
            - Use I(state=present) to update an existing a DomainRecords.
            - Use I(state=absent) to delete a DomainRecords.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update domain_records
  oci_dns_domain_records:
    update_items:
    - domain: www.example.com
      record_hash: 8f356bd7e9c2007c5c898f441fb663e9
      is_protected: false
      rdata: v=spf1 include:example.net -all
      rrset_version: 9
      rtype: TXT
      ttl: 30
    zone_name_or_id: ocid1.zonenameor.oc1..xxxxxxEXAMPLExxxxxx
    domain: domain_example

- name: Delete domain_records
  oci_dns_domain_records:
    zone_name_or_id: ocid1.zonenameor.oc1..xxxxxxEXAMPLExxxxxx
    domain: domain_example
    state: absent

"""

RETURN = """
domain_records:
    description:
        - Details of the DomainRecords resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        domain:
            description:
                - The fully qualified domain name where the record can be located.
            returned: on success
            type: string
            sample: domain_example
        record_hash:
            description:
                - A unique identifier for the record within its zone.
            returned: on success
            type: string
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
            type: string
            sample: rdata_example
        rrset_version:
            description:
                - The latest version of the record's zone in which its RRSet differs
                  from the preceding version.
            returned: on success
            type: string
            sample: rrset_version_example
        rtype:
            description:
                - The type of DNS record, such as A or CNAME. For more information, see L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-
                  parameters/dns-parameters.xhtml#dns-parameters-4).
            returned: on success
            type: string
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
    from oci.dns.models import UpdateDomainRecordsDetails
    from oci.dns.models import PatchDomainRecordsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainRecordsHelperGen(OCIResourceHelperBase):
    """Supported operations: update, patch, get and delete"""

    def get_module_resource_id_param(self):
        return "domain"

    def get_module_resource_id(self):
        return self.module.params.get("domain")

    def get_get_fn(self):
        return self.client.get_domain_records

    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_domain_records,
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                domain=self.module.params.get("domain"),
            ).items
        )

    def get_update_model_class(self):
        return UpdateDomainRecordsDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_domain_records,
            call_fn_args=(),
            call_fn_kwargs=dict(
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                domain=self.module.params.get("domain"),
                update_domain_records_details=update_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                scope=self.module.params.get("scope"),
                view_id=self.module.params.get("view_id"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def get_patch_model_class(self):
        return PatchDomainRecordsDetails

    def patch_resource(self):
        patch_details = self.get_patch_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.patch_domain_records,
            call_fn_args=(),
            call_fn_kwargs=dict(
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                domain=self.module.params.get("domain"),
                patch_domain_records_details=patch_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                scope=self.module.params.get("scope"),
                view_id=self.module.params.get("view_id"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.PATCH_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.PATCH_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_domain_records,
            call_fn_args=(),
            call_fn_kwargs=dict(
                zone_name_or_id=self.module.params.get("zone_name_or_id"),
                domain=self.module.params.get("domain"),
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                scope=self.module.params.get("scope"),
                view_id=self.module.params.get("view_id"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )

    def is_resource_dead(self, resource):
        # response model returns a collection. Consider existence of a value as active.
        if not resource:
            return True
        return False


DomainRecordsHelperCustom = get_custom_class("DomainRecordsHelperCustom")


class ResourceHelper(DomainRecordsHelperCustom, DomainRecordsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            zone_name_or_id=dict(
                aliases=["zone_id", "name", "zone_name", "id"],
                type="str",
                required=True,
            ),
            domain=dict(type="str", required=True),
            update_items=dict(
                type="list",
                elements="dict",
                options=dict(
                    domain=dict(type="str", required=True),
                    record_hash=dict(type="str"),
                    is_protected=dict(type="bool"),
                    rdata=dict(type="str", required=True),
                    rrset_version=dict(type="str"),
                    rtype=dict(type="str", required=True),
                    ttl=dict(type="int", required=True),
                ),
            ),
            if_unmodified_since=dict(type="str"),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            view_id=dict(type="str"),
            compartment_id=dict(type="str"),
            patch_items=dict(
                type="list",
                elements="dict",
                options=dict(
                    domain=dict(type="str"),
                    record_hash=dict(type="str"),
                    is_protected=dict(type="bool"),
                    rdata=dict(type="str"),
                    rrset_version=dict(type="str"),
                    rtype=dict(type="str"),
                    ttl=dict(type="int"),
                    operation=dict(
                        type="str", choices=["REQUIRE", "PROHIBIT", "ADD", "REMOVE"]
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="domain_records",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_patch():
        result = resource_helper.patch()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
