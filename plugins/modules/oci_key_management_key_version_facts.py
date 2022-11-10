#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_key_management_key_version_facts
short_description: Fetches details about one or multiple KeyVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple KeyVersion resources in Oracle Cloud Infrastructure
    - Lists all L(KeyVersion,https://docs.cloud.oracle.com/api/#/en/key/latest/KeyVersion/) resources for the specified
      master encryption key.
    - As a management operation, this call is subject to a Key Management limit that applies to the total number
      of requests across all management read operations. Key Management might throttle this call to reject an
      otherwise valid request when the total rate of management read operations exceeds 10 requests per second
      for a given tenancy.
    - If I(key_version_id) is specified, the details of a single KeyVersion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    key_version_id:
        description:
            - The OCID of the key version.
            - Required to get a specific key_version.
        type: str
        aliases: ["id"]
    key_id:
        description:
            - The OCID of the key.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default
              order for `TIMECREATED` is descending. The default order for `DISPLAYNAME`
              is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific key_version
  oci_key_management_key_version_facts:
    # required
    key_version_id: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: List key_versions
  oci_key_management_key_version_facts:
    # required
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
key_versions:
    description:
        - List of KeyVersion resources
    returned: on success
    type: complex
    contains:
        public_key:
            description:
                - The public key in PEM format. (This value pertains only to RSA and ECDSA keys.)
                - Returned for get operation
            returned: on success
            type: str
            sample: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
        replica_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                replication_id:
                    description:
                        - ReplicationId associated with a key version operation
                    returned: on success
                    type: str
                    sample: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        is_primary:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The OCID of the compartment that contains this key version.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The OCID of the key version.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - The OCID of the key associated with this key version.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The key version's current lifecycle state.
                - "Example: `ENABLED`"
            returned: on success
            type: str
            sample: CREATING
        origin:
            description:
                - The source of the key material. When this value is `INTERNAL`, Key Management
                  created the key material. When this value is `EXTERNAL`, the key material
                  was imported from an external source.
            returned: on success
            type: str
            sample: INTERNAL
        time_created:
            description:
                - The date and time this key version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: \\"2018-04-03T21:10:29.600Z\\""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the key version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vault_id:
            description:
                - The OCID of the vault that contains this key version.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...",
        "replica_details": {
            "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_primary": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "origin": "INTERNAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.key_management import KmsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "key_id",
            "key_version_id",
        ]

    def get_required_params_for_list(self):
        return [
            "key_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key_version,
            key_id=self.module.params.get("key_id"),
            key_version_id=self.module.params.get("key_version_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_key_versions,
            key_id=self.module.params.get("key_id"),
            **optional_kwargs
        )


KeyVersionFactsHelperCustom = get_custom_class("KeyVersionFactsHelperCustom")


class ResourceFactsHelper(KeyVersionFactsHelperCustom, KeyVersionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            key_version_id=dict(aliases=["id"], type="str"),
            key_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            service_endpoint=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="key_version",
        service_client_class=KmsManagementClient,
        namespace="key_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(key_versions=result)


if __name__ == "__main__":
    main()
