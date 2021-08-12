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
module: oci_compute_instance_credentials_facts
short_description: Fetches details about a InstanceCredentials resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a InstanceCredentials resource in Oracle Cloud Infrastructure
    - Gets the generated credentials for the instance. Only works for instances that require a password to log in, such as Windows.
      For certain operating systems, users will be forced to change the initial credentials.
version_added: "2.9"
author: Oracle (@oracle)
options:
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific instance_credentials
  oci_compute_instance_credentials_facts:
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
instance_credentials:
    description:
        - InstanceCredentials resource
    returned: on success
    type: complex
    contains:
        password:
            description:
                - The password for the username.
            returned: on success
            type: string
            sample: password_example
        username:
            description:
                - The username.
            returned: on success
            type: string
            sample: username_example
    sample: {
        "password": "password_example",
        "username": "username_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceCredentialsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_windows_instance_initial_credentials,
            instance_id=self.module.params.get("instance_id"),
        )


InstanceCredentialsFactsHelperCustom = get_custom_class(
    "InstanceCredentialsFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceCredentialsFactsHelperCustom, InstanceCredentialsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(instance_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_credentials",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_credentials=result)


if __name__ == "__main__":
    main()
