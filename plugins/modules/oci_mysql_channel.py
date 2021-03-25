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
module: oci_mysql_channel
short_description: Manage a Channel resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Channel resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a Channel to establish replication from a source to a target.
    - "This resource has the following action operations in the M(oci_channel_actions) module: reset, resume."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly name for the Channel. It does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    is_enabled:
        description:
            - Whether the Channel should be enabled upon creation. If set to true, the Channel
              will be asynchronously started as a result of the create Channel operation.
            - This parameter is updatable.
        type: bool
    source:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            source_type:
                description:
                    - The specific source identifier.
                    - This parameter is updatable.
                type: str
                choices:
                    - "MYSQL"
                required: true
            hostname:
                description:
                    - The network address of the MySQL instance.
                    - This parameter is updatable.
                    - Applicable when source_type is 'MYSQL'
                type: str
            port:
                description:
                    - The port the source MySQL instance listens on.
                    - This parameter is updatable.
                type: int
            username:
                description:
                    - The name of the replication user on the source MySQL instance.
                      The username has a maximum length of 96 characters. For more information,
                      please see the L(MySQL documentation,https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)
                    - This parameter is updatable.
                    - Applicable when source_type is 'MYSQL'
                type: str
            password:
                description:
                    - The password for the replication user. The password must be
                      between 8 and 32 characters long, and must contain at least 1
                      numeric character, 1 lowercase character, 1 uppercase character,
                      and 1 special (nonalphanumeric) character.
                    - This parameter is updatable.
                    - Applicable when source_type is 'MYSQL'
                type: str
            ssl_mode:
                description:
                    - The SSL mode of the Channel.
                    - This parameter is updatable.
                    - Applicable when source_type is 'MYSQL'
                type: str
            ssl_ca_certificate:
                description:
                    - ""
                type: dict
                suboptions:
                    certificate_type:
                        description:
                            - The type of CA certificate.
                        type: str
                        choices:
                            - "PEM"
                        required: true
                    contents:
                        description:
                            - The string containing the CA certificate in PEM format.
                        type: str
                        required: true
    target:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            target_type:
                description:
                    - The specific target identifier.
                    - This parameter is updatable.
                type: str
                choices:
                    - "DBSYSTEM"
                required: true
            db_system_id:
                description:
                    - The OCID of the target DB System.
                type: str
            channel_name:
                description:
                    - The case-insensitive name that identifies the replication channel. Channel names
                      must follow the rules defined for L(MySQL identifiers,https://dev.mysql.com/doc/refman/8.0/en/identifiers.html).
                      The names of non-Deleted Channels must be unique for each DB System.
                    - This parameter is updatable.
                type: str
            applier_username:
                description:
                    - The username for the replication applier of the target MySQL DB System.
                    - This parameter is updatable.
                type: str
    description:
        description:
            - User provided information about the Channel.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    channel_id:
        description:
            - The Channel L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Channel.
            - Use I(state=present) to create or update a Channel.
            - Use I(state=absent) to delete a Channel.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create channel
  oci_mysql_channel:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source:
      source_type: MYSQL
    target:
      target_type: DBSYSTEM

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_channel:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    is_enabled: true
    source:
      source_type: MYSQL
    target:
      target_type: DBSYSTEM
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel
  oci_mysql_channel:
    display_name: display_name_example
    is_enabled: true
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete channel
  oci_mysql_channel:
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_channel:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                    sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import ChannelsClient
    from oci.mysql.models import CreateChannelDetails
    from oci.mysql.models import UpdateChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlChannelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("channel_id")

    def get_get_fn(self):
        return self.client.get_channel

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel, channel_id=self.module.params.get("channel_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["channel_id", "display_name"]
            if self._use_name_as_identifier()
            else ["channel_id", "display_name", "is_enabled"]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_channels, **kwargs)

    def get_create_model_class(self):
        return CreateChannelDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(create_channel_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateChannelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                channel_id=self.module.params.get("channel_id"),
                update_channel_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(channel_id=self.module.params.get("channel_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlChannelHelperCustom = get_custom_class("MysqlChannelHelperCustom")


class ResourceHelper(MysqlChannelHelperCustom, MysqlChannelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            source=dict(
                type="dict",
                options=dict(
                    source_type=dict(type="str", required=True, choices=["MYSQL"]),
                    hostname=dict(type="str"),
                    port=dict(type="int"),
                    username=dict(type="str"),
                    password=dict(type="str", no_log=True),
                    ssl_mode=dict(type="str"),
                    ssl_ca_certificate=dict(
                        type="dict",
                        options=dict(
                            certificate_type=dict(
                                type="str", required=True, choices=["PEM"]
                            ),
                            contents=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            target=dict(
                type="dict",
                options=dict(
                    target_type=dict(type="str", required=True, choices=["DBSYSTEM"]),
                    db_system_id=dict(type="str"),
                    channel_name=dict(type="str"),
                    applier_username=dict(type="str"),
                ),
            ),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            channel_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
