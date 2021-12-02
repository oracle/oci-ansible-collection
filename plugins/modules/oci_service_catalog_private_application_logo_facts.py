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
module: oci_service_catalog_private_application_logo_facts
short_description: Fetches details about a PrivateApplicationLogo resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a PrivateApplicationLogo resource in Oracle Cloud Infrastructure
    - Downloads the binary payload of the logo image of the private application.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    private_application_id:
        description:
            - The unique identifier for the private application.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific private_application_logo
  oci_service_catalog_private_application_logo_facts:
    # required
    dest: /tmp/myfile
    private_application_id: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.service_catalog import ServiceCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateApplicationLogoFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "private_application_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_application_action_download_logo,
            private_application_id=self.module.params.get("private_application_id"),
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


PrivateApplicationLogoFactsHelperCustom = get_custom_class(
    "PrivateApplicationLogoFactsHelperCustom"
)


class ResourceFactsHelper(
    PrivateApplicationLogoFactsHelperCustom, PrivateApplicationLogoFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            private_application_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="private_application_logo",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(private_application_logo=result)


if __name__ == "__main__":
    main()
