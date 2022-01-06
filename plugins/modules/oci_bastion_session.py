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
module: oci_bastion_session
short_description: Manage a Session resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Session resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new session in a bastion. A bastion session lets authorized users connect to a target resource for a predetermined amount
      of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that
      the target resource has an OpenSSH server and the Oracle Cloud Agent both running.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The name of the session.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    bastion_id:
        description:
            - The unique identifier (OCID) of the bastion on which to create this session.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    target_resource_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            session_type:
                description:
                    - The session type.
                type: str
                choices:
                    - "MANAGED_SSH"
                    - "PORT_FORWARDING"
                required: true
            target_resource_port:
                description:
                    - The port number to connect to on the target resource.
                type: int
            target_resource_operating_system_user_name:
                description:
                    - The name of the user on the target resource operating system that the session uses for the connection.
                    - Required when session_type is 'MANAGED_SSH'
                type: str
            target_resource_id:
                description:
                    - The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.
                    - Required when session_type is 'MANAGED_SSH'
                type: str
            target_resource_private_ip_address:
                description:
                    - The private IP address of the target resource that the session connects to.
                type: str
    key_type:
        description:
            - The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.
        type: str
        choices:
            - "PUB"
    key_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            public_key_content:
                description:
                    - The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private key of
                      the same SSH key pair.
                type: str
                required: true
    session_ttl_in_seconds:
        description:
            - The amount of time the session can remain active.
        type: int
    session_id:
        description:
            - The unique identifier (OCID) of the session.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Session.
            - Use I(state=present) to create or update a Session.
            - Use I(state=absent) to delete a Session.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create session
  oci_bastion_session:
    # required
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"
    target_resource_details:
      # required
      session_type: MANAGED_SSH
      target_resource_operating_system_user_name: target_resource_operating_system_user_name_example
      target_resource_id: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      target_resource_port: 56
      target_resource_private_ip_address: target_resource_private_ip_address_example
    key_details:
      # required
      public_key_content: public_key_content_example

    # optional
    display_name: display_name_example
    key_type: PUB
    session_ttl_in_seconds: 56

- name: Update session
  oci_bastion_session:
    # required
    session_id: "ocid1.session.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example

- name: Update session using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bastion_session:
    # required
    display_name: display_name_example
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete session
  oci_bastion_session:
    # required
    session_id: "ocid1.session.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete session using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bastion_session:
    # required
    display_name: display_name_example
    bastion_id: "ocid1.bastion.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
session:
    description:
        - Details of the Session resource acted upon by the current operation
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
            returned: on success
            type: dict
            sample: {}
        key_type:
            description:
                - The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.
            returned: on success
            type: str
            sample: PUB
        key_details:
            description:
                - ""
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
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.bastion import BastionClient
    from oci.bastion.models import CreateSessionDetails
    from oci.bastion.models import UpdateSessionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SessionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "session_id"

    def get_module_resource_id(self):
        return self.module.params.get("session_id")

    def get_get_fn(self):
        return self.client.get_session

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_session, session_id=self.module.params.get("session_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "bastion_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "session_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_sessions, **kwargs)

    def get_create_model_class(self):
        return CreateSessionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_session,
            call_fn_args=(),
            call_fn_kwargs=dict(create_session_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSessionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_session,
            call_fn_args=(),
            call_fn_kwargs=dict(
                session_id=self.module.params.get("session_id"),
                update_session_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_session,
            call_fn_args=(),
            call_fn_kwargs=dict(session_id=self.module.params.get("session_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


SessionHelperCustom = get_custom_class("SessionHelperCustom")


class ResourceHelper(SessionHelperCustom, SessionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            bastion_id=dict(type="str"),
            target_resource_details=dict(
                type="dict",
                options=dict(
                    session_type=dict(
                        type="str",
                        required=True,
                        choices=["MANAGED_SSH", "PORT_FORWARDING"],
                    ),
                    target_resource_port=dict(type="int"),
                    target_resource_operating_system_user_name=dict(type="str"),
                    target_resource_id=dict(type="str"),
                    target_resource_private_ip_address=dict(type="str"),
                ),
            ),
            key_type=dict(type="str", choices=["PUB"]),
            key_details=dict(
                type="dict",
                no_log=False,
                options=dict(
                    public_key_content=dict(type="str", required=True, no_log=True)
                ),
            ),
            session_ttl_in_seconds=dict(type="int"),
            session_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="session",
        service_client_class=BastionClient,
        namespace="bastion",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
