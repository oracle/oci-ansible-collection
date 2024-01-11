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
module: oci_vault_secret_version_facts
short_description: Fetches details about one or multiple SecretVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SecretVersion resources in Oracle Cloud Infrastructure
    - Lists all secret versions for the specified secret.
    - If I(secret_version_number) is specified, the details of a single SecretVersion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    secret_version_number:
        description:
            - The version number of the secret.
            - Required to get a specific secret_version.
        type: int
    secret_id:
        description:
            - The OCID of the secret.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Time created is default ordered as descending. Display name is default ordered as
              ascending.
        type: str
        choices:
            - "VERSION_NUMBER"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific secret_version
  oci_vault_secret_version_facts:
    # required
    secret_version_number: 56
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"

- name: List secret_versions
  oci_vault_secret_version_facts:
    # required
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: VERSION_NUMBER
    sort_order: ASC

"""

RETURN = """
secret_versions:
    description:
        - List of SecretVersion resources
    returned: on success
    type: complex
    contains:
        time_of_current_version_expiry:
            description:
                - "An optional property indicating when the current secret version will expire, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        content_type:
            description:
                - The content type of the secret version's secret contents.
            returned: on success
            type: str
            sample: BASE64
        name:
            description:
                - The name of the secret version. A name is unique across versions of a secret.
            returned: on success
            type: str
            sample: name_example
        secret_id:
            description:
                - The OCID of the secret.
            returned: on success
            type: str
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        stages:
            description:
                - A list of possible rotation states for the secret version. A secret version marked `CURRENT` is currently in use. A secret version
                  marked `PENDING` is staged and available for use, but has not been applied on the target system and, therefore, has not been rotated
                  into current, active use. The secret most recently uploaded to a vault is always marked `LATEST`. (The first version of a secret is
                  always marked as both `CURRENT` and `LATEST`.) A secret version marked `PREVIOUS` is the secret version that was most recently marked
                  `CURRENT`, before the last secret version rotation. A secret version marked `DEPRECATED` is neither current, pending, nor the previous
                  one in use. Only secret versions marked `DEPRECATED` can be scheduled for deletion.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - "A optional property indicating when the secret version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the secret version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_expiry:
            description:
                - "An optional property indicating when the secret version will expire, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
                - Returned for list operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version_number:
            description:
                - The version number of the secret.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "time_of_current_version_expiry": "2013-10-20T19:20:30+01:00",
        "content_type": "BASE64",
        "name": "name_example",
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx",
        "stages": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "time_of_expiry": "2013-10-20T19:20:30+01:00",
        "version_number": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.vault import VaultsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "secret_id",
            "secret_version_number",
        ]

    def get_required_params_for_list(self):
        return [
            "secret_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_secret_version,
            secret_id=self.module.params.get("secret_id"),
            secret_version_number=self.module.params.get("secret_version_number"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_secret_versions,
            secret_id=self.module.params.get("secret_id"),
            **optional_kwargs
        )


SecretVersionFactsHelperCustom = get_custom_class("SecretVersionFactsHelperCustom")


class ResourceFactsHelper(SecretVersionFactsHelperCustom, SecretVersionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            secret_version_number=dict(type="int", no_log=True),
            secret_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["VERSION_NUMBER"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="secret_version",
        service_client_class=VaultsClient,
        namespace="vault",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(secret_versions=result)


if __name__ == "__main__":
    main()
