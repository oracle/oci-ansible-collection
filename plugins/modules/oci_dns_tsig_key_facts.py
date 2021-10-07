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
module: oci_dns_tsig_key_facts
short_description: Fetches details about one or multiple TsigKey resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TsigKey resources in Oracle Cloud Infrastructure
    - Gets a list of all TSIG keys in the specified compartment.
    - If I(tsig_key_id) is specified, the details of a single TsigKey will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tsig_key_id:
        description:
            - The OCID of the target TSIG key.
            - Required to get a specific tsig_key.
        type: str
        aliases: ["id"]
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - Required to list multiple tsig_keys.
        type: str
    name:
        description:
            - The name of a resource.
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
            - The field by which to sort TSIG keys. If unspecified, defaults to `timeCreated`.
        type: str
        choices:
            - "name"
            - "timeCreated"
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List tsig_keys
  oci_dns_tsig_key_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific tsig_key
  oci_dns_tsig_key_facts:
    tsig_key_id: "ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
tsig_keys:
    description:
        - List of TsigKey resources
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
            type: str
            sample: algorithm_example
        name:
            description:
                - A globally unique domain name identifying the key for a given pair of hosts.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The OCID of the compartment containing the TSIG key.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        secret:
            description:
                - A base64 string encoding the binary shared secret.
            returned: on success
            type: str
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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: str
            sample: _self_example
        time_created:
            description:
                - The date and time the resource was created, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: str
            sample: ACTIVE
        time_updated:
            description:
                - The date and time the resource was last updated, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
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
    }]
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


class TsigKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "tsig_key_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_tsig_key,
            tsig_key_id=self.module.params.get("tsig_key_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tsig_keys,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TsigKeyFactsHelperCustom = get_custom_class("TsigKeyFactsHelperCustom")


class ResourceFactsHelper(TsigKeyFactsHelperCustom, TsigKeyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tsig_key_id=dict(aliases=["id"], type="str"),
            if_modified_since=dict(type="str"),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
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
            sort_by=dict(type="str", choices=["name", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tsig_key",
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

    module.exit_json(tsig_keys=result)


if __name__ == "__main__":
    main()
