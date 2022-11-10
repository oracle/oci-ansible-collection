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
module: oci_database_management_preferred_credential_facts
short_description: Fetches details about one or multiple PreferredCredential resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PreferredCredential resources in Oracle Cloud Infrastructure
    - List the preferred credentials for a given managed database.
    - If I(credential_name) is specified, the details of a single PreferredCredential will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    credential_name:
        description:
            - The name of the preferred credential.
            - Required to get a specific preferred_credential.
        type: str
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific preferred_credential
  oci_database_management_preferred_credential_facts:
    # required
    credential_name: credential_name_example
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List preferred_credentials
  oci_database_management_preferred_credential_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
preferred_credentials:
    description:
        - List of PreferredCredential resources
    returned: on success
    type: complex
    contains:
        type:
            description:
                - Type of the preferred credential.
                - Returned for get operation
            returned: on success
            type: str
            sample: BASIC
        credential_name:
            description:
                - Name of the preferred credential.
            returned: on success
            type: str
            sample: credential_name_example
        status:
            description:
                - Status of the preferred credential.
            returned: on success
            type: str
            sample: SET
        is_accessible:
            description:
                - Is preferred credential accessible.
            returned: on success
            type: bool
            sample: true
        user_name:
            description:
                - The user to connect to the database.
            returned: on success
            type: str
            sample: user_name_example
        role:
            description:
                - Role of the database user.
            returned: on success
            type: str
            sample: NORMAL
        password_secret_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret.
            returned: on success
            type: str
            sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "type": "BASIC",
        "credential_name": "credential_name_example",
        "status": "SET",
        "is_accessible": true,
        "user_name": "user_name_example",
        "role": "NORMAL",
        "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PreferredCredentialFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "credential_name",
        ]

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_preferred_credential,
            managed_database_id=self.module.params.get("managed_database_id"),
            credential_name=self.module.params.get("credential_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_preferred_credentials,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


PreferredCredentialFactsHelperCustom = get_custom_class(
    "PreferredCredentialFactsHelperCustom"
)


class ResourceFactsHelper(
    PreferredCredentialFactsHelperCustom, PreferredCredentialFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            credential_name=dict(type="str"),
            managed_database_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="preferred_credential",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(preferred_credentials=result)


if __name__ == "__main__":
    main()
