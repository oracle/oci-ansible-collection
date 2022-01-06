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
module: oci_bastion_session_facts
short_description: Fetches details about one or multiple Session resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Session resources in Oracle Cloud Infrastructure
    - Retrieves a list of SessionSummary objects for an existing bastion. Bastion sessions let authorized users connect to a target resource for a predetermined
      amount of time.
    - If I(session_id) is specified, the details of a single Session will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    session_id:
        description:
            - The unique identifier (OCID) of the session.
            - Required to get a specific session.
        type: str
        aliases: ["id"]
    bastion_id:
        description:
            - The unique identifier (OCID) of the bastion in which to list sessions.
            - Required to list multiple sessions.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    session_lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific session
  oci_bastion_session_facts:
    # required
    session_id: "ocid1.session.oc1..xxxxxxEXAMPLExxxxxx"

- name: List sessions
  oci_bastion_session_facts:
    # required
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    session_id: "ocid1.session.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    session_lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
sessions:
    description:
        - List of Session resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier (OCID) of the session, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the session.
            returned: on success
            type: str
            sample: display_name_example
        bastion_id:
            description:
                - The unique identifier (OCID) of the bastion that is hosting this session.
            returned: on success
            type: str
            sample: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"
        bastion_name:
            description:
                - The name of the bastion that is hosting this session.
            returned: on success
            type: str
            sample: bastion_name_example
        bastion_user_name:
            description:
                - The username that the session uses to connect to the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: bastion_user_name_example
        target_resource_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                session_type:
                    description:
                        - The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions
                          require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.
                    returned: on success
                    type: str
                    sample: MANAGED_SSH
                target_resource_port:
                    description:
                        - The port number to connect to on the target resource.
                    returned: on success
                    type: int
                    sample: 56
                target_resource_operating_system_user_name:
                    description:
                        - The name of the user on the target resource operating system that the session uses for the connection.
                    returned: on success
                    type: str
                    sample: target_resource_operating_system_user_name_example
                target_resource_id:
                    description:
                        - The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.
                    returned: on success
                    type: str
                    sample: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"
                target_resource_private_ip_address:
                    description:
                        - The private IP address of the target resource that the session connects to.
                    returned: on success
                    type: str
                    sample: target_resource_private_ip_address_example
                target_resource_display_name:
                    description:
                        - The display name of the target Compute instance that the session connects to.
                    returned: on success
                    type: str
                    sample: target_resource_display_name_example
        ssh_metadata:
            description:
                - The connection message for the session.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        key_type:
            description:
                - The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.
                - Returned for get operation
            returned: on success
            type: str
            sample: PUB
        key_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                public_key_content:
                    description:
                        - The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private
                          key of the same SSH key pair.
                    returned: on success
                    type: str
                    sample: public_key_content_example
        bastion_public_host_key_info:
            description:
                - The public key of the bastion host. You can use this to verify that you're connecting to the correct bastion.
                - Returned for get operation
            returned: on success
            type: str
            sample: bastion_public_host_key_info_example
        time_created:
            description:
                - "The time the session was created. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the session was updated. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the session.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current session state in more detail.
            returned: on success
            type: str
            sample: lifecycle_details_example
        session_ttl_in_seconds:
            description:
                - The amount of time the session can remain active.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "bastion_id": "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx",
        "bastion_name": "bastion_name_example",
        "bastion_user_name": "bastion_user_name_example",
        "target_resource_details": {
            "session_type": "MANAGED_SSH",
            "target_resource_port": 56,
            "target_resource_operating_system_user_name": "target_resource_operating_system_user_name_example",
            "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx",
            "target_resource_private_ip_address": "target_resource_private_ip_address_example",
            "target_resource_display_name": "target_resource_display_name_example"
        },
        "ssh_metadata": {},
        "key_type": "PUB",
        "key_details": {
            "public_key_content": "public_key_content_example"
        },
        "bastion_public_host_key_info": "bastion_public_host_key_info_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "session_ttl_in_seconds": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.bastion import BastionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SessionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "session_id",
        ]

    def get_required_params_for_list(self):
        return [
            "bastion_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_session, session_id=self.module.params.get("session_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "session_lifecycle_state",
            "session_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sessions,
            bastion_id=self.module.params.get("bastion_id"),
            **optional_kwargs
        )


SessionFactsHelperCustom = get_custom_class("SessionFactsHelperCustom")


class ResourceFactsHelper(SessionFactsHelperCustom, SessionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            session_id=dict(aliases=["id"], type="str"),
            bastion_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            session_lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="session",
        service_client_class=BastionClient,
        namespace="bastion",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sessions=result)


if __name__ == "__main__":
    main()
