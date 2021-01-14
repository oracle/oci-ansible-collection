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
module: oci_secrets_secret_bundle_facts
short_description: Fetches details about a SecretBundle resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SecretBundle resource in Oracle Cloud Infrastructure
    - Gets a secret bundle that matches either the specified `stage`, `label`, or `versionNumber` parameter.
      If none of these parameters are provided, the bundle for the secret version marked as `CURRENT` will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    secret_id:
        description:
            - The OCID of the secret.
        type: str
        aliases: ["id"]
        required: true
    version_number:
        description:
            - The version number of the secret.
        type: int
    secret_version_name:
        description:
            - The name of the secret. (This might be referred to as the name of the secret version. Names are unique across the different versions of a secret.)
        type: str
    stage:
        description:
            - The rotation state of the secret version.
        type: str
        choices:
            - "CURRENT"
            - "PENDING"
            - "LATEST"
            - "PREVIOUS"
            - "DEPRECATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific secret_bundle
  oci_secrets_secret_bundle_facts:
    secret_id: ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
secret_bundle:
    description:
        - SecretBundle resource
    returned: on success
    type: complex
    contains:
        secret_id:
            description:
                - The OCID of the secret.
            returned: on success
            type: string
            sample: ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The time when the secret bundle was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        version_number:
            description:
                - The version number of the secret.
            returned: on success
            type: int
            sample: 56
        version_name:
            description:
                - The name of the secret version. Labels are unique across the different versions of a particular secret.
            returned: on success
            type: string
            sample: version_name_example
        secret_bundle_content:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                content_type:
                    description:
                        - The formatting type of the secret contents.
                    returned: on success
                    type: string
                    sample: BASE64
                content:
                    description:
                        - The base64-encoded content of the secret.
                    returned: on success
                    type: string
                    sample: content_example
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the secret version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        time_of_expiry:
            description:
                - "An optional property indicating when the secret version will expire, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        stages:
            description:
                - A list of possible rotation states for the secret version.
            returned: on success
            type: list
            sample: []
        metadata:
            description:
                - Customer-provided contextual metadata for the secret.
            returned: on success
            type: dict
            sample: {}
    sample: {
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version_number": 56,
        "version_name": "version_name_example",
        "secret_bundle_content": {
            "content_type": "BASE64",
            "content": "content_example"
        },
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "time_of_expiry": "2019-04-03T21:10:29.600Z",
        "stages": [],
        "metadata": {}
    }
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


class SecretBundleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "secret_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "version_number",
            "secret_version_name",
            "stage",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_secret_bundle,
            secret_id=self.module.params.get("secret_id"),
            **optional_kwargs
        )


SecretBundleFactsHelperCustom = get_custom_class("SecretBundleFactsHelperCustom")


class ResourceFactsHelper(SecretBundleFactsHelperCustom, SecretBundleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            secret_id=dict(aliases=["id"], type="str", required=True),
            version_number=dict(type="int"),
            secret_version_name=dict(type="str"),
            stage=dict(
                type="str",
                choices=["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="secret_bundle",
        service_client_class=SecretsClient,
        namespace="secrets",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(secret_bundle=result)


if __name__ == "__main__":
    main()
