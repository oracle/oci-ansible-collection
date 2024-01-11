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
module: oci_cims_status_facts
short_description: Fetches details about a Status resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Status resource in Oracle Cloud Infrastructure
    - Gets the status of the service.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source:
        description:
            - The system that generated the support ticket, such as My Oracle Support.
        type: str
        required: true
    ocid:
        description:
            - User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.
        type: str
        required: true
    homeregion:
        description:
            - The region of the tenancy.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific status
  oci_cims_status_facts:
    # required
    source: source_example
    ocid: ocid_example

    # optional
    homeregion: us-phoenix-1

"""

RETURN = """
status:
    description:
        - Status resource
    returned: on success
    type: complex
    contains:
        code:
            description:
                - The code unique to this ticket status.
            returned: on success
            type: str
            sample: code_example
        message:
            description:
                - The status message for this ticket.
            returned: on success
            type: str
            sample: message_example
    sample: {
        "code": "code_example",
        "message": "message_example"
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


class StatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "source",
            "ocid",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "homeregion",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_status,
            source=self.module.params.get("source"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )


StatusFactsHelperCustom = get_custom_class("StatusFactsHelperCustom")


class ResourceFactsHelper(StatusFactsHelperCustom, StatusFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            source=dict(type="str", required=True),
            ocid=dict(type="str", required=True),
            homeregion=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="status",
        service_client_class=IncidentClient,
        namespace="cims",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(status=result)


if __name__ == "__main__":
    main()
