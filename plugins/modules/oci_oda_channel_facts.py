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
module: oci_oda_channel_facts
short_description: Fetches details about one or multiple Channel resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Channel resources in Oracle Cloud Infrastructure
    - Returns a page of Channels that belong to the specified Digital Assistant instance.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(channel_id) is specified, the details of a single Channel will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    channel_id:
        description:
            - Unique Channel identifier.
            - Required to get a specific channel.
        type: str
        aliases: ["id"]
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    name:
        description:
            - List only the information for Channels with this name. Channels names are unique and may not change.
            - "Example: `MyChannel`"
        type: str
    category:
        description:
            - List only Channels with this category.
        type: str
        choices:
            - "AGENT"
            - "APPLICATION"
            - "BOT"
            - "BOT_AS_AGENT"
            - "SYSTEM"
            - "EVENT"
    type:
        description:
            - List only Channels of this type.
        type: str
        choices:
            - "ANDROID"
            - "APPEVENT"
            - "APPLICATION"
            - "CORTANA"
            - "FACEBOOK"
            - "IOS"
            - "MSTEAMS"
            - "OSS"
            - "OSVC"
            - "SERVICECLOUD"
            - "SLACK"
            - "TEST"
            - "TWILIO"
            - "WEB"
            - "WEBHOOK"
    lifecycle_state:
        description:
            - List only the resources that are in this lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.
            - The default sort order for `timeCreated` and `timeUpdated` is descending, and the default sort order for `name` is ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific channel
  oci_oda_channel_facts:
    # required
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List channels
  oci_oda_channel_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    category: AGENT
    type: ANDROID
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
channels:
    description:
        - List of Channel resources
    returned: on success
    type: complex
    contains:
        is_authenticated_user_id:
            description:
                - True if the user id in the AIC message should be treated as an authenticated user id.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        msa_app_id:
            description:
                - The Microsoft App ID that you obtained when you created your bot registration in Azure.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
        event_sink_bot_ids:
            description:
                - The IDs of the Skills and Digital Assistants that the Channel is routed to.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        inbound_message_topic:
            description:
                - The topic inbound messages are received on.
                - Returned for get operation
            returned: on success
            type: str
            sample: inbound_message_topic_example
        outbound_message_topic:
            description:
                - The topic outbound messages are sent on.
                - Returned for get operation
            returned: on success
            type: str
            sample: outbound_message_topic_example
        bootstrap_servers:
            description:
                - The Oracle Streaming Service bootstrap servers.
                - Returned for get operation
            returned: on success
            type: str
            sample: bootstrap_servers_example
        security_protocol:
            description:
                - The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid
                  values.
                - Returned for get operation
            returned: on success
            type: str
            sample: security_protocol_example
        sasl_mechanism:
            description:
                - The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid
                  values.
                - Returned for get operation
            returned: on success
            type: str
            sample: sasl_mechanism_example
        tenancy_name:
            description:
                - The tenancy to use when connecting to the Oracle Streaming Service.
                - Returned for get operation
            returned: on success
            type: str
            sample: tenancy_name_example
        stream_pool_id:
            description:
                - The stream pool OCI to use when connecting to the Oracle Streaming Service.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        host:
            description:
                - The host.
                - For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface
                  or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch,
                  then the host is sitename.exampledomain.com.
                - "For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL.
                  For example: sitename.exampledomain.com."
                - Returned for get operation
            returned: on success
            type: str
            sample: host_example
        port:
            description:
                - The port.
                - Returned for get operation
            returned: on success
            type: str
            sample: port_example
        total_session_count:
            description:
                - The total session count.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        channel_service:
            description:
                - The type of OSVC service.
                - Returned for get operation
            returned: on success
            type: str
            sample: OSVC
        authentication_provider_name:
            description:
                - The name of the Authentication Provider to use to authenticate the user.
                - Returned for get operation
            returned: on success
            type: str
            sample: authentication_provider_name_example
        domain_name:
            description:
                - The domain name.
                - If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
                  Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
                  is sitename and the domain name is exampledomain.com.
                - If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
                  then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something
                  like sitename-2.exampledomain.com.
                - Returned for get operation
            returned: on success
            type: str
            sample: domain_name_example
        host_name_prefix:
            description:
                - The host prefix.
                - If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
                  Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
                  is sitename and the domain name is exampledomain.com.
                - If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
                  then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something
                  like sitename-2.exampledomain.com.
                - Returned for get operation
            returned: on success
            type: str
            sample: host_name_prefix_example
        user_name:
            description:
                - The user name to use when connecting to the Oracle Streaming Service.
                - Returned for get operation
            returned: on success
            type: str
            sample: user_name_example
        client_type:
            description:
                - The type of Service Cloud client.
                - Returned for get operation
            returned: on success
            type: str
            sample: WSDL
        client_id:
            description:
                - The Slack Client Id for the Slack app.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        auth_success_url:
            description:
                - The URL to redirect to when authentication is successful.
                - Returned for get operation
            returned: on success
            type: str
            sample: auth_success_url_example
        auth_error_url:
            description:
                - The URL to redirect to when authentication is unsuccessful.
                - Returned for get operation
            returned: on success
            type: str
            sample: auth_error_url_example
        account_sid:
            description:
                - The Account SID for the Twilio number.
                - Returned for get operation
            returned: on success
            type: str
            sample: account_sid_example
        phone_number:
            description:
                - The Twilio phone number.
                - Returned for get operation
            returned: on success
            type: str
            sample: phone_number_example
        is_mms_enabled:
            description:
                - Whether MMS is enabled for this channel or not.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        original_connectors_url:
            description:
                - The original connectors URL (used for backward compatibility).
                - Returned for get operation
            returned: on success
            type: str
            sample: original_connectors_url_example
        max_token_expiration_time_in_minutes:
            description:
                - The maximum time until the token expires (in minutes).
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        is_client_authentication_enabled:
            description:
                - Whether client authentication is enabled or not.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        allowed_domains:
            description:
                - A comma-delimited whitelist of allowed domains.
                - "The channel will only communicate with the sites from the domains that you add to this list.
                  For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access
                  to the channel from any domain."
                - Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.
                - Returned for get operation
            returned: on success
            type: str
            sample: allowed_domains_example
        session_expiry_duration_in_milliseconds:
            description:
                - The number of milliseconds before a session expires.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        outbound_url:
            description:
                - The URL for sending errors and responses to.
                - Returned for get operation
            returned: on success
            type: str
            sample: outbound_url_example
        payload_version:
            description:
                - The version for payloads.
                - Returned for get operation
            returned: on success
            type: str
            sample: 1.0
        bot_id:
            description:
                - The ID of the Skill or Digital Assistant that the Channel is routed to.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"
        webhook_url:
            description:
                - The URL to use to send messages to this channel.
                  This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.
                - Returned for get operation
            returned: on success
            type: str
            sample: webhook_url_example
        id:
            description:
                - Unique immutable identifier that was assigned when the Channel was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - A short description of the Channel.
            returned: on success
            type: str
            sample: description_example
        category:
            description:
                - The category of the Channel.
            returned: on success
            type: str
            sample: AGENT
        type:
            description:
                - The Channel type.
            returned: on success
            type: str
            sample: ANDROID
        lifecycle_state:
            description:
                - The Channel's current state.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - When the resource was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the resource was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
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
        "is_authenticated_user_id": true,
        "msa_app_id": "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx",
        "event_sink_bot_ids": [],
        "inbound_message_topic": "inbound_message_topic_example",
        "outbound_message_topic": "outbound_message_topic_example",
        "bootstrap_servers": "bootstrap_servers_example",
        "security_protocol": "security_protocol_example",
        "sasl_mechanism": "sasl_mechanism_example",
        "tenancy_name": "tenancy_name_example",
        "stream_pool_id": "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx",
        "host": "host_example",
        "port": "port_example",
        "total_session_count": 56,
        "channel_service": "OSVC",
        "authentication_provider_name": "authentication_provider_name_example",
        "domain_name": "domain_name_example",
        "host_name_prefix": "host_name_prefix_example",
        "user_name": "user_name_example",
        "client_type": "WSDL",
        "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
        "auth_success_url": "auth_success_url_example",
        "auth_error_url": "auth_error_url_example",
        "account_sid": "account_sid_example",
        "phone_number": "phone_number_example",
        "is_mms_enabled": true,
        "original_connectors_url": "original_connectors_url_example",
        "max_token_expiration_time_in_minutes": 56,
        "is_client_authentication_enabled": true,
        "allowed_domains": "allowed_domains_example",
        "session_expiry_duration_in_milliseconds": 56,
        "outbound_url": "outbound_url_example",
        "payload_version": "1.0",
        "bot_id": "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx",
        "webhook_url": "webhook_url_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "category": "AGENT",
        "type": "ANDROID",
        "lifecycle_state": "CREATING",
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
    from oci.oda import ManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ChannelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "channel_id",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            channel_id=self.module.params.get("channel_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "category",
            "type",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_channels,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            **optional_kwargs
        )


ChannelFactsHelperCustom = get_custom_class("ChannelFactsHelperCustom")


class ResourceFactsHelper(ChannelFactsHelperCustom, ChannelFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            channel_id=dict(aliases=["id"], type="str"),
            oda_instance_id=dict(type="str", required=True),
            name=dict(type="str"),
            category=dict(
                type="str",
                choices=[
                    "AGENT",
                    "APPLICATION",
                    "BOT",
                    "BOT_AS_AGENT",
                    "SYSTEM",
                    "EVENT",
                ],
            ),
            type=dict(
                type="str",
                choices=[
                    "ANDROID",
                    "APPEVENT",
                    "APPLICATION",
                    "CORTANA",
                    "FACEBOOK",
                    "IOS",
                    "MSTEAMS",
                    "OSS",
                    "OSVC",
                    "SERVICECLOUD",
                    "SLACK",
                    "TEST",
                    "TWILIO",
                    "WEB",
                    "WEBHOOK",
                ],
            ),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "timeUpdated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="channel",
        service_client_class=ManagementClient,
        namespace="oda",
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
