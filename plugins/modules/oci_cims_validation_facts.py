#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_cims_validation_facts
short_description: Fetches details about a Validation resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Validation resource in Oracle Cloud Infrastructure
    - Checks whether the requested user is valid.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    csi:
        description:
            - The Customer Support Identifier number for the support account.
        type: str
        required: true
    ocid:
        description:
            - User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.
        type: str
        required: true
    problem_type:
        description:
            - The kind of support request.
        type: str
    homeregion:
        description:
            - The region of the tenancy.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific validation
  oci_cims_validation_facts:
    # required
    csi: csi_example
    ocid: ocid_example

    # optional
    problem_type: problem_type_example
    homeregion: us-phoenix-1

"""

RETURN = """
validation:
    description:
        - Validation resource
    returned: on success
    type: complex
    contains:
        is_valid_user:
            description:
                - Boolean value that indicates whether the requested user is valid.
            returned: on success
            type: bool
            sample: true
    sample: {
        "is_valid_user": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cims import IncidentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ValidationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "csi",
            "ocid",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "problem_type",
            "homeregion",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.validate_user,
            csi=self.module.params.get("csi"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )


ValidationFactsHelperCustom = get_custom_class("ValidationFactsHelperCustom")


class ResourceFactsHelper(ValidationFactsHelperCustom, ValidationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            csi=dict(type="str", required=True),
            ocid=dict(type="str", required=True),
            problem_type=dict(type="str"),
            homeregion=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="validation",
        service_client_class=IncidentClient,
        namespace="cims",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(validation=result)


if __name__ == "__main__":
    main()
