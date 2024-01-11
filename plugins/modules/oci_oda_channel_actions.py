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
module: oci_oda_channel_actions
short_description: Perform actions on a Channel resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Channel resource in Oracle Cloud Infrastructure
    - For I(action=rotate_channel_keys), this will generate new keys for any generated keys in the Channel (eg. secretKey, verifyToken).
      If a Channel has no generated keys then no changes will be made.
      Ensure that you take note of the newly generated keys in the response as they will not be returned again.
    - For I(action=start), starts a Channel so that it will begin accepting messages.
    - For I(action=stop), stops a Channel so that it will no longer accept messages.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    channel_id:
        description:
            - Unique Channel identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Channel.
        type: str
        required: true
        choices:
            - "rotate_channel_keys"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action rotate_channel_keys on channel
  oci_oda_channel_actions:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    action: rotate_channel_keys

- name: Perform action start on channel
  oci_oda_channel_actions:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on channel
  oci_oda_channel_actions:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
channel:
    description:
        - Details of the Channel resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_authenticated_user_id:
            description:
                - True if the user id in the AIC message should be treated as an authenticated user id.
            returned: on success
            type: bool
            sample: true
        msa_app_id:
            description:
                - The Microsoft App ID that you obtained when you created your bot registration in Azure.
            returned: on success
            type: str
            sample: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
        event_sink_bot_ids:
            description:
                - The IDs of the Skills and Digital Assistants that the Channel is routed to.
            returned: on success
            type: list
            sample: []
        inbound_message_topic:
            description:
                - The topic inbound messages are received on.
            returned: on success
            type: str
            sample: inbound_message_topic_example
        outbound_message_topic:
            description:
                - The topic outbound messages are sent on.
            returned: on success
            type: str
            sample: outbound_message_topic_example
        bootstrap_servers:
            description:
                - The Oracle Streaming Service bootstrap servers.
            returned: on success
            type: str
            sample: bootstrap_servers_example
        security_protocol:
            description:
                - The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid
                  values.
            returned: on success
            type: str
            sample: security_protocol_example
        sasl_mechanism:
            description:
                - The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid
                  values.
            returned: on success
            type: str
            sample: sasl_mechanism_example
        tenancy_name:
            description:
                - The tenancy to use when connecting to the Oracle Streaming Service.
            returned: on success
            type: str
            sample: tenancy_name_example
        stream_pool_id:
            description:
                - The stream pool OCI to use when connecting to the Oracle Streaming Service.
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
            returned: on success
            type: str
            sample: host_example
        port:
            description:
                - The port.
            returned: on success
            type: str
            sample: port_example
        total_session_count:
            description:
                - The total session count.
            returned: on success
            type: int
            sample: 56
        channel_service:
            description:
                - The type of OSVC service.
            returned: on success
            type: str
            sample: OSVC
        authentication_provider_name:
            description:
                - The name of the Authentication Provider to use to authenticate the user.
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
            returned: on success
            type: str
            sample: host_name_prefix_example
        user_name:
            description:
                - The user name to use when connecting to the Oracle Streaming Service.
            returned: on success
            type: str
            sample: user_name_example
        client_type:
            description:
                - The type of Service Cloud client.
            returned: on success
            type: str
            sample: WSDL
        client_id:
            description:
                - The Slack Client Id for the Slack app.
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        auth_success_url:
            description:
                - The URL to redirect to when authentication is successful.
            returned: on success
            type: str
            sample: auth_success_url_example
        auth_error_url:
            description:
                - The URL to redirect to when authentication is unsuccessful.
            returned: on success
            type: str
            sample: auth_error_url_example
        account_sid:
            description:
                - The Account SID for the Twilio number.
            returned: on success
            type: str
            sample: account_sid_example
        phone_number:
            description:
                - The Twilio phone number.
            returned: on success
            type: str
            sample: phone_number_example
        is_mms_enabled:
            description:
                - Whether MMS is enabled for this channel or not.
            returned: on success
            type: bool
            sample: true
        original_connectors_url:
            description:
                - The original connectors URL (used for backward compatibility).
            returned: on success
            type: str
            sample: original_connectors_url_example
        max_token_expiration_time_in_minutes:
            description:
                - The maximum time until the token expires (in minutes).
            returned: on success
            type: int
            sample: 56
        is_client_authentication_enabled:
            description:
                - Whether client authentication is enabled or not.
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
            returned: on success
            type: str
            sample: allowed_domains_example
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
        session_expiry_duration_in_milliseconds:
            description:
                - The number of milliseconds before a session expires.
            returned: on success
            type: int
            sample: 56
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
        outbound_url:
            description:
                - The URL for sending errors and responses to.
            returned: on success
            type: str
            sample: outbound_url_example
        payload_version:
            description:
                - The version for payloads.
            returned: on success
            type: str
            sample: 1.0
        bot_id:
            description:
                - The ID of the Skill or Digital Assistant that the Channel is routed to.
            returned: on success
            type: str
            sample: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"
        webhook_url:
            description:
                - The URL to use to send messages to this channel.
                  This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.
            returned: on success
            type: str
            sample: webhook_url_example
    sample: {
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "category": "AGENT",
        "type": "ANDROID",
        "session_expiry_duration_in_milliseconds": 56,
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "outbound_url": "outbound_url_example",
        "payload_version": "1.0",
        "bot_id": "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx",
        "webhook_url": "webhook_url_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.oda import ManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ChannelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        rotate_channel_keys
        start
        stop
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
            self.client.get_channel,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            channel_id=self.module.params.get("channel_id"),
        )

    def rotate_channel_keys(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rotate_channel_keys,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ChannelActionsHelperCustom = get_custom_class("ChannelActionsHelperCustom")


class ResourceHelper(ChannelActionsHelperCustom, ChannelActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            oda_instance_id=dict(type="str", required=True),
            channel_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["rotate_channel_keys", "start", "stop"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="channel",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
