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
module: oci_dns_tsig_key_actions
short_description: Perform actions on a TsigKey resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TsigKey resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a TSIG key into a different compartment.
version_added: "2.9"
author: Oracle (@oracle)
options:
    tsig_key_id:
        description:
            - The OCID of the target TSIG key.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the TSIG key should be moved.
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
            - The action to perform on the TsigKey.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on tsig_key
  oci_dns_tsig_key_actions:
    tsig_key_id: ocid1.tsigkey.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    action: change_compartment

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient
    from oci.dns.models import ChangeTsigKeyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TsigKeyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "tsig_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("tsig_key_id")

    def get_get_fn(self):
        return self.client.get_tsig_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tsig_key, tsig_key_id=self.module.params.get("tsig_key_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeTsigKeyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_tsig_key_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tsig_key_id=self.module.params.get("tsig_key_id"),
                change_tsig_key_compartment_details=action_details,
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


TsigKeyActionsHelperCustom = get_custom_class("TsigKeyActionsHelperCustom")


class ResourceHelper(TsigKeyActionsHelperCustom, TsigKeyActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            tsig_key_id=dict(aliases=["id"], type="str", required=True),
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
        resource_type="tsig_key",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
