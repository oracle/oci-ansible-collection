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
module: oci_mysql_channel_actions
short_description: Perform actions on a Channel resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Channel resource in Oracle Cloud Infrastructure
    - For I(action=reset), resets the specified Channel by purging its cached information, leaving the Channel
      as if it had just been created. This operation is only accepted in Inactive Channels.
    - For I(action=resume), resumes an enabled Channel that has become Inactive due to an error. The resume operation
      requires that the error that cause the Channel to become Inactive has already been fixed,
      otherwise the operation may fail.
version_added: "2.9"
author: Oracle (@oracle)
options:
    channel_id:
        description:
            - The Channel L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Channel.
        type: str
        required: true
        choices:
            - "reset"
            - "resume"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action reset on channel
  oci_mysql_channel_actions:
    channel_id: ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx
    action: reset

- name: Perform action resume on channel
  oci_mysql_channel_actions:
    channel_id: ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx
    action: resume

"""

RETURN = """
channel:
    description:
        - Details of the Channel resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Channel.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name for the Channel. It does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        is_enabled:
            description:
                - Whether the Channel has been enabled by the user.
            returned: on success
            type: bool
            sample: true
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The specific source identifier.
                    returned: on success
                    type: string
                    sample: MYSQL
                hostname:
                    description:
                        - The network address of the MySQL instance.
                    returned: on success
                    type: string
                    sample: hostname_example
                port:
                    description:
                        - The port the source MySQL instance listens on.
                    returned: on success
                    type: int
                    sample: 56
                username:
                    description:
                        - The name of the replication user on the source MySQL instance.
                          The username has a maximum length of 96 characters. For more information,
                          please see the L(MySQL documentation,https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)
                    returned: on success
                    type: string
                    sample: username_example
                ssl_mode:
                    description:
                        - The SSL mode of the Channel.
                    returned: on success
                    type: string
                    sample: VERIFY_IDENTITY
                ssl_ca_certificate:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        certificate_type:
                            description:
                                - The type of CA certificate.
                            returned: on success
                            type: string
                            sample: PEM
                        contents:
                            description:
                                - The string containing the CA certificate in PEM format.
                            returned: on success
                            type: string
                            sample: contents_example
        target:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                target_type:
                    description:
                        - The specific target identifier.
                    returned: on success
                    type: string
                    sample: DBSYSTEM
                db_system_id:
                    description:
                        - The OCID of the source DB System.
                    returned: on success
                    type: string
                    sample: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
                channel_name:
                    description:
                        - The case-insensitive name that identifies the replication channel. Channel names
                          must follow the rules defined for L(MySQL identifiers,https://dev.mysql.com/doc/refman/8.0/en/identifiers.html).
                          The names of non-Deleted Channels must be unique for each DB System.
                    returned: on success
                    type: string
                    sample: channel_name_example
                applier_username:
                    description:
                        - The username for the replication applier of the target MySQL DB System.
                    returned: on success
                    type: string
                    sample: applier_username_example
        description:
            description:
                - User provided description of the Channel.
            returned: on success
            type: string
            sample: description_example
        lifecycle_state:
            description:
                - The state of the Channel.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the state of the Channel.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the Channel was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the Channel was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "is_enabled": true,
        "source": {
            "source_type": "MYSQL",
            "hostname": "hostname_example",
            "port": 56,
            "username": "username_example",
            "ssl_mode": "VERIFY_IDENTITY",
            "ssl_ca_certificate": {
                "certificate_type": "PEM",
                "contents": "contents_example"
            }
        },
        "target": {
            "target_type": "DBSYSTEM",
            "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
            "channel_name": "channel_name_example",
            "applier_username": "applier_username_example"
        },
        "description": "description_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import ChannelsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlChannelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        reset
        resume
    """

    @staticmethod
    def get_module_resource_id_param():
        return "channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("channel_id")

    def get_get_fn(self):
        return self.client.get_channel

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel, channel_id=self.module.params.get("channel_id"),
        )

    def reset(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(channel_id=self.module.params.get("channel_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def resume(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resume_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(channel_id=self.module.params.get("channel_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlChannelActionsHelperCustom = get_custom_class("MysqlChannelActionsHelperCustom")


class ResourceHelper(MysqlChannelActionsHelperCustom, MysqlChannelActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            channel_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["reset", "resume"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="channel",
        service_client_class=ChannelsClient,
        namespace="mysql",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
