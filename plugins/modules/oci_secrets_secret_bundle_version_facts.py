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
module: oci_secrets_secret_bundle_version_facts
short_description: Fetches details about one or multiple SecretBundleVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SecretBundleVersion resources in Oracle Cloud Infrastructure
    - Lists all secret bundle versions for the specified secret.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    secret_id:
        description:
            - The OCID of the secret.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default
              order for `VERSION_NUMBER` is ascending.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List secret_bundle_versions
  oci_secrets_secret_bundle_version_facts:
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
secret_bundle_versions:
    description:
        - List of SecretBundleVersion resources
    returned: on success
    type: complex
    contains:
        secret_id:
            description:
                - The OCID of the secret.
            returned: on success
            type: str
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when the secret bundle was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version_number:
            description:
                - The version number of the secret.
            returned: on success
            type: int
            sample: 56
        version_name:
            description:
                - The version name of the secret bundle, as provided when the secret was created or last rotated.
            returned: on success
            type: str
            sample: version_name_example
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the secret version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        time_of_expiry:
            description:
                - "An optional property indicating when the secret version will expire, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        stages:
            description:
                - A list of possible rotation states for the secret bundle.
            returned: on success
            type: list
            sample: []
    sample: [{
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version_number": 56,
        "version_name": "version_name_example",
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "time_of_expiry": "2019-04-03T21:10:29.600Z",
        "stages": []
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.secrets import SecretsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretBundleVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "secret_id",
        ]

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
            self.client.list_secret_bundle_versions,
            secret_id=self.module.params.get("secret_id"),
            **optional_kwargs
        )


SecretBundleVersionFactsHelperCustom = get_custom_class(
    "SecretBundleVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    SecretBundleVersionFactsHelperCustom, SecretBundleVersionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            secret_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["VERSION_NUMBER"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="secret_bundle_version",
        service_client_class=SecretsClient,
        namespace="secrets",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(secret_bundle_versions=result)


if __name__ == "__main__":
    main()
