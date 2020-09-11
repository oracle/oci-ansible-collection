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
module: oci_dns_tsig_key
short_description: Manage a TsigKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TsigKey resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new TSIG key in the specified compartment. There is no
      `opc-retry-token` header since TSIG key names must be globally unique.
version_added: "2.9"
author: Oracle (@oracle)
options:
    algorithm:
        description:
            - "TSIG key algorithms are encoded as domain names, but most consist of only one
              non-empty label, which is not required to be explicitly absolute.
              Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
              hmac-sha512. For more information on these algorithms, see L(RFC 4635,https://tools.ietf.org/html/rfc4635#section-2)."
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - A globally unique domain name identifying the key for a given pair of hosts.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment containing the TSIG key.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    secret:
        description:
            - A base64 string encoding the binary shared secret.
            - Required for create using I(state=present).
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
    tsig_key_id:
        description:
            - The OCID of the target TSIG key.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
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
            - The state of the TsigKey.
            - Use I(state=present) to create or update a TsigKey.
            - Use I(state=absent) to delete a TsigKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create tsig_key
  oci_dns_tsig_key:
    algorithm: algorithm_example
    name: name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    secret: secret_example

- name: Update tsig_key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_tsig_key:
    name: name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    if_unmodified_since: if_unmodified_since_example

- name: Update tsig_key
  oci_dns_tsig_key:
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    tsig_key_id: ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete tsig_key
  oci_dns_tsig_key:
    tsig_key_id: ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete tsig_key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_tsig_key:
    name: name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
tsig_key:
    description:
        - Details of the TsigKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        algorithm:
            description:
                - "TSIG key algorithms are encoded as domain names, but most consist of only one
                  non-empty label, which is not required to be explicitly absolute.
                  Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
                  hmac-sha512. For more information on these algorithms, see L(RFC 4635,https://tools.ietf.org/html/rfc4635#section-2)."
            returned: on success
            type: string
            sample: algorithm_example
        name:
            description:
                - A globally unique domain name identifying the key for a given pair of hosts.
            returned: on success
            type: string
            sample: name_example
        compartment_id:
            description:
                - The OCID of the compartment containing the TSIG key.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        secret:
            description:
                - A base64 string encoding the binary shared secret.
            returned: on success
            type: string
            sample: secret_example
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
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: string
            sample: _self_example
        time_created:
            description:
                - The date and time the resource was created, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: string
            sample: ACTIVE
        time_updated:
            description:
                - The date and time the resource was last updated, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "algorithm": "algorithm_example",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "secret": "secret_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "_self": "_self_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.dns.models import CreateTsigKeyDetails
    from oci.dns.models import UpdateTsigKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TsigKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "tsig_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("tsig_key_id")

    def get_get_fn(self):
        return self.client.get_tsig_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tsig_key, tsig_key_id=self.module.params.get("tsig_key_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_tsig_keys, **kwargs)

    def get_create_model_class(self):
        return CreateTsigKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tsig_key,
            call_fn_args=(),
            call_fn_kwargs=dict(create_tsig_key_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateTsigKeyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tsig_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tsig_key_id=self.module.params.get("tsig_key_id"),
                update_tsig_key_details=update_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_tsig_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tsig_key_id=self.module.params.get("tsig_key_id"),
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


TsigKeyHelperCustom = get_custom_class("TsigKeyHelperCustom")


class ResourceHelper(TsigKeyHelperCustom, TsigKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            algorithm=dict(type="str"),
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            secret=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            tsig_key_id=dict(aliases=["id"], type="str"),
            if_unmodified_since=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tsig_key",
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
