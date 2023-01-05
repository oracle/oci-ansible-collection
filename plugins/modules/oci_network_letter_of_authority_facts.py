#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_network_letter_of_authority_facts
short_description: Fetches details about a LetterOfAuthority resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a LetterOfAuthority resource in Oracle Cloud Infrastructure
    - Gets the Letter of Authority for the specified cross-connect.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cross_connect_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific letter_of_authority
  oci_network_letter_of_authority_facts:
    # required
    cross_connect_id: "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
letter_of_authority:
    description:
        - LetterOfAuthority resource
    returned: on success
    type: complex
    contains:
        authorized_entity_name:
            description:
                - The name of the entity authorized by this Letter of Authority.
            returned: on success
            type: str
            sample: authorized_entity_name_example
        circuit_type:
            description:
                - The type of cross-connect fiber, termination, and optical specification.
            returned: on success
            type: str
            sample: Single_mode_LC
        cross_connect_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect.
            returned: on success
            type: str
            sample: "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx"
        facility_location:
            description:
                - The address of the FastConnect location.
            returned: on success
            type: str
            sample: facility_location_example
        port_name:
            description:
                - The meet-me room port for this cross-connect.
            returned: on success
            type: str
            sample: port_name_example
        time_expires:
            description:
                - The date and time when the Letter of Authority expires, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_issued:
            description:
                - The date and time the Letter of Authority was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "authorized_entity_name": "authorized_entity_name_example",
        "circuit_type": "Single_mode_LC",
        "cross_connect_id": "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx",
        "facility_location": "facility_location_example",
        "port_name": "port_name_example",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "time_issued": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LetterOfAuthorityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cross_connect_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cross_connect_letter_of_authority,
            cross_connect_id=self.module.params.get("cross_connect_id"),
        )


LetterOfAuthorityFactsHelperCustom = get_custom_class(
    "LetterOfAuthorityFactsHelperCustom"
)


class ResourceFactsHelper(
    LetterOfAuthorityFactsHelperCustom, LetterOfAuthorityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(cross_connect_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="letter_of_authority",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(letter_of_authority=result)


if __name__ == "__main__":
    main()
