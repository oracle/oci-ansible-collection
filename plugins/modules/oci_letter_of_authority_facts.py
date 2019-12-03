#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}


DOCUMENTATION = """
---
module: oci_letter_of_authority_facts
short_description: Fetches details of OCI cross-connect Letter of Authority
description:
     - Fetches details of OCI Letter of Authority
version_added: "2.5"
options:
    cross_connect_id:
        description: Identifier of the cross-connect whose letter of authority needs to be fetched.
        required: true
        aliases: [ 'id' ]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch Letter of Authority
- name: Fetch Letter of Authority
  oci_letter_of_authority_facts:
      cross_connect_id: 'ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_letter_of_authorities:
        description: Attributes of the Letter of Authority.
        returned: success
        type: complex
        contains:
            authorized_entity_name:
                description: The name of the entity authorized by this Letter of Authority.
                returned: always
                type: string
                sample: Example Authorized Entity
            circuit_type:
                description: The type of cross-connect fiber, termination, and optical specification.
                returned: always
                type: string
                sample: Single_mode_LC
            cross_connect_id:
                description: The OCID of the cross-connect.
                returned: always
                type: string
                sample: ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx
            facility_location:
                description: The address of the FastConnect location.
                returned: always
                type: string
                sample: Equinox
            port_name:
                description: The meet-me room port for this cross-connect.
                returned: always
                type: string
                sample: Example Port Name
            time_expires:
                description: The date and time when the Letter of Authority expires, in the format defined by RFC3339.
                returned: always
                type: string
                sample: 2018-03-03T06:55:49.463000+00:00
            time_issued:
                description: The date and time the Letter of Authority was created, in the format defined by RFC3339..
                returned: always
                type: string
                sample: 2018-03-03T06:55:49.463000+00:00
        sample: [{
                    "authorized_entity_name":"Example Authorized Entity Name",
                    "circuit_type":"Single_mode_LC",
                    "cross_connect_id":"ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx",
                    "facility_location":"Equinox",
                    "port_name":"Example Port Name",
                    "time_expires":"2018-03-03T06:55:49.463000+00:00",
                    "time_issued":"2018-02-03T06:55:49.463000+00:00"
                }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_letter_of_authorities(virtual_network_client, module):
    result = dict(letter_of_authorities="")
    existing_letter_of_authorities = None
    cross_connect_id = module.params.get("cross_connect_id")
    try:
        response = oci_utils.call_with_backoff(
            virtual_network_client.get_cross_connect_letter_of_authority,
            cross_connect_id=cross_connect_id,
        )
        existing_letter_of_authorities = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["letter_of_authorities"] = to_dict(existing_letter_of_authorities)
    return result


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(cross_connect_id=dict(type="str", required=True, aliases=["id"]))
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_letter_of_authorities(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
