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
module: oci_license_manager_bulk_upload_template_facts
short_description: Fetches details about a BulkUploadTemplate resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a BulkUploadTemplate resource in Oracle Cloud Infrastructure
    - Provides the bulk upload file template.
version_added: "2.9.0"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific bulk_upload_template
  oci_license_manager_bulk_upload_template_facts:

"""

RETURN = """
bulk_upload_template:
    description:
        - BulkUploadTemplate resource
    returned: on success
    type: complex
    contains:
        template:
            description:
                - The bulk upload template.
            returned: on success
            type: str
            sample: template_example
    sample: {
        "template": "template_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.license_manager import LicenseManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BulkUploadTemplateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(self.client.get_bulk_upload_template,)


BulkUploadTemplateFactsHelperCustom = get_custom_class(
    "BulkUploadTemplateFactsHelperCustom"
)


class ResourceFactsHelper(
    BulkUploadTemplateFactsHelperCustom, BulkUploadTemplateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict())

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bulk_upload_template",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(bulk_upload_template=result)


if __name__ == "__main__":
    main()
