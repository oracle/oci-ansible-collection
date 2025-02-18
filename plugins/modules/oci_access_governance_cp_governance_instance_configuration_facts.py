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
module: oci_access_governance_cp_governance_instance_configuration_facts
short_description: Fetches details about a GovernanceInstanceConfiguration resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a GovernanceInstanceConfiguration resource in Oracle Cloud Infrastructure
    - Gets the tenancy-wide configuration for GovernanceInstances
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which resources are listed.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific governance_instance_configuration
  oci_access_governance_cp_governance_instance_configuration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
governance_instance_configuration:
    description:
        - GovernanceInstanceConfiguration resource
    returned: on success
    type: complex
    contains:
        sender_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The sender's displayName.
                    returned: on success
                    type: str
                    sample: display_name_example
                email:
                    description:
                        - The sender's email.
                    returned: on success
                    type: str
                    sample: email_example
                is_verified:
                    description:
                        - Whether or not the sender's email has been verified.
                    returned: on success
                    type: bool
                    sample: true
                time_verify_response_expiry:
                    description:
                        - The time when the verify response needs to be received by.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                is_inbox_configured:
                    description:
                        - Whether the sender email has inbox configured to receive emails.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "sender_info": {
            "display_name": "display_name_example",
            "email": "email_example",
            "is_verified": true,
            "time_verify_response_expiry": "2013-10-20T19:20:30+01:00",
            "is_inbox_configured": true
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.access_governance_cp import AccessGovernanceCPClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceInstanceConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )


GovernanceInstanceConfigurationFactsHelperCustom = get_custom_class(
    "GovernanceInstanceConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    GovernanceInstanceConfigurationFactsHelperCustom,
    GovernanceInstanceConfigurationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="governance_instance_configuration",
        service_client_class=AccessGovernanceCPClient,
        namespace="access_governance_cp",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(governance_instance_configuration=result)


if __name__ == "__main__":
    main()
