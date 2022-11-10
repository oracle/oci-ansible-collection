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
module: oci_mysql_channel_facts
short_description: Fetches details about one or multiple Channel resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Channel resources in Oracle Cloud Infrastructure
    - Lists all the Channels that match the specified filters.
    - If I(channel_id) is specified, the details of a single Channel will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple channels.
        type: str
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    channel_id:
        description:
            - The Channel L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific channel.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only the resource matching the given display name exactly.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - The LifecycleState of the Channel.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    is_enabled:
        description:
            - If true, returns only Channels that are enabled. If false, returns only
              Channels that are disabled.
        type: bool
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as
              ascending.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
    sort_order:
        description:
            - The sort order to use (ASC or DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific channel
  oci_mysql_channel_facts:
    # required
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"

- name: List channels
  oci_mysql_channel_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    is_enabled: true
    sort_by: displayName
    sort_order: ASC

"""

RETURN = """
channels:
    description:
        - List of Channel resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - User provided description of the Channel.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        id:
            description:
                - The OCID of the Channel.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                    type: str
                    sample: MYSQL
                hostname:
                    description:
                        - The network address of the MySQL instance.
                    returned: on success
                    type: str
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
                    type: str
                    sample: username_example
                ssl_mode:
                    description:
                        - The SSL mode of the Channel.
                    returned: on success
                    type: str
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
                            type: str
                            sample: PEM
                        contents:
                            description:
                                - The string containing the CA certificate in PEM format.
                            returned: on success
                            type: str
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
                    type: str
                    sample: DBSYSTEM
                db_system_id:
                    description:
                        - The OCID of the source DB System.
                    returned: on success
                    type: str
                    sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
                channel_name:
                    description:
                        - The case-insensitive name that identifies the replication channel. Channel names
                          must follow the rules defined for L(MySQL identifiers,https://dev.mysql.com/doc/refman/8.0/en/identifiers.html).
                          The names of non-Deleted Channels must be unique for each DB System.
                    returned: on success
                    type: str
                    sample: channel_name_example
                applier_username:
                    description:
                        - The username for the replication applier of the target MySQL DB System.
                    returned: on success
                    type: str
                    sample: applier_username_example
        lifecycle_state:
            description:
                - The state of the Channel.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the state of the Channel.
            returned: on success
            type: str
            sample: lifecycle_details_example
        display_name:
            description:
                - The user-friendly name for the Channel. It does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the Channel was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Channel was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "description": "description_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
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
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import ChannelsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlChannelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "channel_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel, channel_id=self.module.params.get("channel_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "db_system_id",
            "channel_id",
            "display_name",
            "lifecycle_state",
            "is_enabled",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_channels,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlChannelFactsHelperCustom = get_custom_class("MysqlChannelFactsHelperCustom")


class ResourceFactsHelper(MysqlChannelFactsHelperCustom, MysqlChannelFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            db_system_id=dict(type="str"),
            channel_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "NEEDS_ATTENTION",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            is_enabled=dict(type="bool"),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="channel",
        service_client_class=ChannelsClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(channels=result)


if __name__ == "__main__":
    main()
