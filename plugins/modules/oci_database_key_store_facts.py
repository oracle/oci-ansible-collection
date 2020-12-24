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
module: oci_database_key_store_facts
short_description: Fetches details about one or multiple KeyStore resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple KeyStore resources in Oracle Cloud Infrastructure
    - Gets a list of key stores in the specified compartment.
    - If I(key_store_id) is specified, the details of a single KeyStore will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    key_store_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the key store.
            - Required to get a specific key_store.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple key_stores.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List key_stores
  oci_database_key_store_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific key_store
  oci_database_key_store_facts:
    key_store_id: ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
key_stores:
    description:
        - List of KeyStore resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the key store.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name for the key store. The name does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        time_created:
            description:
                - The date and time that the key store was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the key store.
            returned: on success
            type: string
            sample: ACTIVE
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        type_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of key store.
                    returned: on success
                    type: string
                    sample: ORACLE_KEY_VAULT
                connection_ips:
                    description:
                        - The list of Oracle Key Vault connection IP addresses.
                    returned: on success
                    type: list
                    sample: []
                admin_username:
                    description:
                        - The administrator username to connect to Oracle Key Vault
                    returned: on success
                    type: string
                    sample: admin_username_example
                vault_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                          L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                    returned: on success
                    type: string
                    sample: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
                secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                          L(secret,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                    returned: on success
                    type: string
                    sample: ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx
        associated_databases:
            description:
                - List of databases associated with the key store.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                db_name:
                    description:
                        - The name of the database that is associated with the key store.
                    returned: on success
                    type: string
                    sample: db_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "type_details": {
            "type": "ORACLE_KEY_VAULT",
            "connection_ips": [],
            "admin_username": "admin_username_example",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "associated_databases": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "db_name": "db_name_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyStoreFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "key_store_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key_store,
            key_store_id=self.module.params.get("key_store_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_key_stores,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


KeyStoreFactsHelperCustom = get_custom_class("KeyStoreFactsHelperCustom")


class ResourceFactsHelper(KeyStoreFactsHelperCustom, KeyStoreFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            key_store_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="key_store",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(key_stores=result)


if __name__ == "__main__":
    main()
